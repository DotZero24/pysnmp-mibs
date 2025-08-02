_K='fspGroup'
_J='fspAid'
_I='fspLabel'
_H='fspProvSerialNumber'
_G='fspType'
_F='Integer32'
_E='entLPPhysicalIndex'
_D='ENTITY-MIB'
_C='read-write'
_B='INFINERA-ENTITY-FSP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entLPPhysicalIndex,=mibBuilder.importSymbols(_D,_E)
equipment,=mibBuilder.importSymbols('INFINERA-REG-MIB','equipment')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
fspMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,1,35))
_FspTable_Object=MibTable
fspTable=_FspTable_Object((1,3,6,1,4,1,21296,2,2,2,1,35,1))
if mibBuilder.loadTexts:fspTable.setStatus(_A)
_FspEntry_Object=MibTableRow
fspEntry=_FspEntry_Object((1,3,6,1,4,1,21296,2,2,2,1,35,1,1))
fspEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:fspEntry.setStatus(_A)
class _FspType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(7805,7806,7807,7808)));namedValues=NamedValues(*(('fspE9D18MPO',7805),('fspS4D8MPO',7806),('fspC1D1MPO',7807),('fmpC8fourLcMPO',7808)))
_FspType_Type.__name__=_F
_FspType_Object=MibTableColumn
fspType=_FspType_Object((1,3,6,1,4,1,21296,2,2,2,1,35,1,1,1),_FspType_Type())
fspType.setMaxAccess(_C)
if mibBuilder.loadTexts:fspType.setStatus(_A)
_FspProvSerialNumber_Type=DisplayString
_FspProvSerialNumber_Object=MibTableColumn
fspProvSerialNumber=_FspProvSerialNumber_Object((1,3,6,1,4,1,21296,2,2,2,1,35,1,1,2),_FspProvSerialNumber_Type())
fspProvSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:fspProvSerialNumber.setStatus(_A)
_FspLabel_Type=DisplayString
_FspLabel_Object=MibTableColumn
fspLabel=_FspLabel_Object((1,3,6,1,4,1,21296,2,2,2,1,35,1,1,3),_FspLabel_Type())
fspLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:fspLabel.setStatus(_A)
_FspAid_Type=DisplayString
_FspAid_Object=MibTableColumn
fspAid=_FspAid_Object((1,3,6,1,4,1,21296,2,2,2,1,35,1,1,4),_FspAid_Type())
fspAid.setMaxAccess(_C)
if mibBuilder.loadTexts:fspAid.setStatus(_A)
_FspConformance_ObjectIdentity=ObjectIdentity
fspConformance=_FspConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,35,3))
_FspCompliances_ObjectIdentity=ObjectIdentity
fspCompliances=_FspCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,35,3,1))
_FspGroups_ObjectIdentity=ObjectIdentity
fspGroups=_FspGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,35,3,2))
fspGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,1,35,3,2,1))
fspGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:fspGroup.setStatus(_A)
fspCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,1,35,3,1,1))
fspCompliance.setObjects((_B,_K))
if mibBuilder.loadTexts:fspCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fspMIB':fspMIB,'fspTable':fspTable,'fspEntry':fspEntry,_G:fspType,_H:fspProvSerialNumber,_I:fspLabel,_J:fspAid,'fspConformance':fspConformance,'fspCompliances':fspCompliances,'fspCompliance':fspCompliance,'fspGroups':fspGroups,_K:fspGroup})