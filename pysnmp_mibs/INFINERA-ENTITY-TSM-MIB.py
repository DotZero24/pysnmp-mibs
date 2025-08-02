_K='tsmGroup'
_J='cardRedundancyState'
_I='tsmRowStatus'
_H='tsmProvEqptType'
_G='tsmMoId'
_F='Integer32'
_E='entLPPhysicalIndex'
_D='ENTITY-MIB'
_C='read-create'
_B='INFINERA-ENTITY-TSM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entLPPhysicalIndex,=mibBuilder.importSymbols(_D,_E)
equipment,=mibBuilder.importSymbols('INFINERA-REG-MIB','equipment')
InfnEqptType,=mibBuilder.importSymbols('INFINERA-TC-MIB','InfnEqptType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
tsmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,1,22))
_TsmTable_Object=MibTable
tsmTable=_TsmTable_Object((1,3,6,1,4,1,21296,2,2,2,1,22,1))
if mibBuilder.loadTexts:tsmTable.setStatus(_A)
_TsmEntry_Object=MibTableRow
tsmEntry=_TsmEntry_Object((1,3,6,1,4,1,21296,2,2,2,1,22,1,1))
tsmEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:tsmEntry.setStatus(_A)
_TsmMoId_Type=DisplayString
_TsmMoId_Object=MibTableColumn
tsmMoId=_TsmMoId_Object((1,3,6,1,4,1,21296,2,2,2,1,22,1,1,1),_TsmMoId_Type())
tsmMoId.setMaxAccess(_C)
if mibBuilder.loadTexts:tsmMoId.setStatus(_A)
_TsmProvEqptType_Type=InfnEqptType
_TsmProvEqptType_Object=MibTableColumn
tsmProvEqptType=_TsmProvEqptType_Object((1,3,6,1,4,1,21296,2,2,2,1,22,1,1,2),_TsmProvEqptType_Type())
tsmProvEqptType.setMaxAccess(_C)
if mibBuilder.loadTexts:tsmProvEqptType.setStatus(_A)
_TsmRowStatus_Type=RowStatus
_TsmRowStatus_Object=MibTableColumn
tsmRowStatus=_TsmRowStatus_Object((1,3,6,1,4,1,21296,2,2,2,1,22,1,1,3),_TsmRowStatus_Type())
tsmRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tsmRowStatus.setStatus(_A)
class _CardRedundancyState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('active',2),('standby',3)))
_CardRedundancyState_Type.__name__=_F
_CardRedundancyState_Object=MibTableColumn
cardRedundancyState=_CardRedundancyState_Object((1,3,6,1,4,1,21296,2,2,2,1,22,1,1,4),_CardRedundancyState_Type())
cardRedundancyState.setMaxAccess('read-only')
if mibBuilder.loadTexts:cardRedundancyState.setStatus(_A)
_TsmConformance_ObjectIdentity=ObjectIdentity
tsmConformance=_TsmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,22,3))
_TsmCompliances_ObjectIdentity=ObjectIdentity
tsmCompliances=_TsmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,22,3,1))
_TsmGroups_ObjectIdentity=ObjectIdentity
tsmGroups=_TsmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,22,3,2))
tsmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,1,22,3,2,1))
tsmGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:tsmGroup.setStatus(_A)
tsmCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,1,22,3,1,1))
tsmCompliance.setObjects((_B,_K))
if mibBuilder.loadTexts:tsmCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'tsmMIB':tsmMIB,'tsmTable':tsmTable,'tsmEntry':tsmEntry,_G:tsmMoId,_H:tsmProvEqptType,_I:tsmRowStatus,_J:cardRedundancyState,'tsmConformance':tsmConformance,'tsmCompliances':tsmCompliances,'tsmCompliance':tsmCompliance,'tsmGroups':tsmGroups,_K:tsmGroup})