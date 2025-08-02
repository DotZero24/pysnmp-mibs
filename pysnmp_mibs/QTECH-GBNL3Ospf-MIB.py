_F='ospfRedistributeProtocal'
_E='QTECH-GBNL3Ospf-MIB'
_D='Metric'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
gbnL3,=mibBuilder.importSymbols('QTECH-MASTER-MIB','gbnL3')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
gbnL3OspfMib=ModuleIdentity((1,3,6,1,4,1,27514,1,2,5,3))
if mibBuilder.loadTexts:gbnL3OspfMib.setRevisions(('1903-08-18 00:01',))
class Metric(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_GbnL3OspfGroup_ObjectIdentity=ObjectIdentity
gbnL3OspfGroup=_GbnL3OspfGroup_ObjectIdentity((1,3,6,1,4,1,27514,1,2,5,3,1))
class _OspfRedistriDefaultMetric_Type(Metric):defaultValue=1
_OspfRedistriDefaultMetric_Type.__name__=_D
_OspfRedistriDefaultMetric_Object=MibScalar
ospfRedistriDefaultMetric=_OspfRedistriDefaultMetric_Object((1,3,6,1,4,1,27514,1,2,5,3,1,1),_OspfRedistriDefaultMetric_Type())
ospfRedistriDefaultMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfRedistriDefaultMetric.setStatus(_A)
class _OspfRedistriDefaultType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('type1',1),('type2',2)))
_OspfRedistriDefaultType_Type.__name__=_C
_OspfRedistriDefaultType_Object=MibScalar
ospfRedistriDefaultType=_OspfRedistriDefaultType_Object((1,3,6,1,4,1,27514,1,2,5,3,1,2),_OspfRedistriDefaultType_Type())
ospfRedistriDefaultType.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfRedistriDefaultType.setStatus(_A)
class _OspfRedistriDefaultTag_Type(Integer32):defaultValue=10
_OspfRedistriDefaultTag_Type.__name__=_C
_OspfRedistriDefaultTag_Object=MibScalar
ospfRedistriDefaultTag=_OspfRedistriDefaultTag_Object((1,3,6,1,4,1,27514,1,2,5,3,1,3),_OspfRedistriDefaultTag_Type())
ospfRedistriDefaultTag.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfRedistriDefaultTag.setStatus(_A)
class _OspfRedistriDefaultInterval_Type(Integer32):defaultValue=1
_OspfRedistriDefaultInterval_Type.__name__=_C
_OspfRedistriDefaultInterval_Object=MibScalar
ospfRedistriDefaultInterval=_OspfRedistriDefaultInterval_Object((1,3,6,1,4,1,27514,1,2,5,3,1,4),_OspfRedistriDefaultInterval_Type())
ospfRedistriDefaultInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfRedistriDefaultInterval.setStatus(_A)
class _OspfRedistriDefaultLimit_Type(Integer32):defaultValue=1000
_OspfRedistriDefaultLimit_Type.__name__=_C
_OspfRedistriDefaultLimit_Object=MibScalar
ospfRedistriDefaultLimit=_OspfRedistriDefaultLimit_Object((1,3,6,1,4,1,27514,1,2,5,3,1,5),_OspfRedistriDefaultLimit_Type())
ospfRedistriDefaultLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfRedistriDefaultLimit.setStatus(_A)
_OspfRedistributeTable_Object=MibTable
ospfRedistributeTable=_OspfRedistributeTable_Object((1,3,6,1,4,1,27514,1,2,5,3,2))
if mibBuilder.loadTexts:ospfRedistributeTable.setStatus(_A)
_OspfRedistributeEntry_Object=MibTableRow
ospfRedistributeEntry=_OspfRedistributeEntry_Object((1,3,6,1,4,1,27514,1,2,5,3,2,1))
ospfRedistributeEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:ospfRedistributeEntry.setStatus(_A)
_OspfRedistributeProtocal_Type=Integer32
_OspfRedistributeProtocal_Object=MibTableColumn
ospfRedistributeProtocal=_OspfRedistributeProtocal_Object((1,3,6,1,4,1,27514,1,2,5,3,2,1,1),_OspfRedistributeProtocal_Type())
ospfRedistributeProtocal.setMaxAccess('read-only')
if mibBuilder.loadTexts:ospfRedistributeProtocal.setStatus(_A)
_OspfRedistributeMetric_Type=Metric
_OspfRedistributeMetric_Object=MibTableColumn
ospfRedistributeMetric=_OspfRedistributeMetric_Object((1,3,6,1,4,1,27514,1,2,5,3,2,1,2),_OspfRedistributeMetric_Type())
ospfRedistributeMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfRedistributeMetric.setStatus(_A)
class _OspfRedistributeType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('type1',1),('type2',2)))
_OspfRedistributeType_Type.__name__=_C
_OspfRedistributeType_Object=MibTableColumn
ospfRedistributeType=_OspfRedistributeType_Object((1,3,6,1,4,1,27514,1,2,5,3,2,1,3),_OspfRedistributeType_Type())
ospfRedistributeType.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfRedistributeType.setStatus(_A)
_OspfRedistributeTag_Type=Integer32
_OspfRedistributeTag_Object=MibTableColumn
ospfRedistributeTag=_OspfRedistributeTag_Object((1,3,6,1,4,1,27514,1,2,5,3,2,1,4),_OspfRedistributeTag_Type())
ospfRedistributeTag.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfRedistributeTag.setStatus(_A)
_OspfRedistributeStatus_Type=RowStatus
_OspfRedistributeStatus_Object=MibTableColumn
ospfRedistributeStatus=_OspfRedistributeStatus_Object((1,3,6,1,4,1,27514,1,2,5,3,2,1,5),_OspfRedistributeStatus_Type())
ospfRedistributeStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfRedistributeStatus.setStatus(_A)
_OspfRedistributeAlways_Type=TruthValue
_OspfRedistributeAlways_Object=MibTableColumn
ospfRedistributeAlways=_OspfRedistributeAlways_Object((1,3,6,1,4,1,27514,1,2,5,3,2,1,6),_OspfRedistributeAlways_Type())
ospfRedistributeAlways.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfRedistributeAlways.setStatus(_A)
mibBuilder.exportSymbols(_E,**{_D:Metric,'gbnL3OspfMib':gbnL3OspfMib,'gbnL3OspfGroup':gbnL3OspfGroup,'ospfRedistriDefaultMetric':ospfRedistriDefaultMetric,'ospfRedistriDefaultType':ospfRedistriDefaultType,'ospfRedistriDefaultTag':ospfRedistriDefaultTag,'ospfRedistriDefaultInterval':ospfRedistriDefaultInterval,'ospfRedistriDefaultLimit':ospfRedistriDefaultLimit,'ospfRedistributeTable':ospfRedistributeTable,'ospfRedistributeEntry':ospfRedistributeEntry,_F:ospfRedistributeProtocal,'ospfRedistributeMetric':ospfRedistributeMetric,'ospfRedistributeType':ospfRedistributeType,'ospfRedistributeTag':ospfRedistributeTag,'ospfRedistributeStatus':ospfRedistributeStatus,'ospfRedistributeAlways':ospfRedistributeAlways})