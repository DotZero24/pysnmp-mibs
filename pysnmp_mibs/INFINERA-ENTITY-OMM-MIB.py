_M='ommGroup'
_L='ommRowStatus'
_K='ommRedundancyStatus'
_J='ommProvType'
_I='ommMoId'
_H='ommBrandingFault'
_G='read-only'
_F='Integer32'
_E='entLPPhysicalIndex'
_D='ENTITY-MIB'
_C='read-create'
_B='INFINERA-ENTITY-OMM-MIB'
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
ommMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,1,10))
_OmmTable_Object=MibTable
ommTable=_OmmTable_Object((1,3,6,1,4,1,21296,2,2,2,1,10,1))
if mibBuilder.loadTexts:ommTable.setStatus(_A)
_OmmEntry_Object=MibTableRow
ommEntry=_OmmEntry_Object((1,3,6,1,4,1,21296,2,2,2,1,10,1,1))
ommEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:ommEntry.setStatus(_A)
_OmmMoId_Type=DisplayString
_OmmMoId_Object=MibTableColumn
ommMoId=_OmmMoId_Object((1,3,6,1,4,1,21296,2,2,2,1,10,1,1,1),_OmmMoId_Type())
ommMoId.setMaxAccess(_C)
if mibBuilder.loadTexts:ommMoId.setStatus(_A)
_OmmProvType_Type=InfnEqptType
_OmmProvType_Object=MibTableColumn
ommProvType=_OmmProvType_Object((1,3,6,1,4,1,21296,2,2,2,1,10,1,1,2),_OmmProvType_Type())
ommProvType.setMaxAccess(_C)
if mibBuilder.loadTexts:ommProvType.setStatus(_A)
class _OmmRedundancyStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('none',1),('single',2),('active',3),('standby',4),('makeStandbyInProgress',5),('oos',6),('lock',7)))
_OmmRedundancyStatus_Type.__name__=_F
_OmmRedundancyStatus_Object=MibTableColumn
ommRedundancyStatus=_OmmRedundancyStatus_Object((1,3,6,1,4,1,21296,2,2,2,1,10,1,1,3),_OmmRedundancyStatus_Type())
ommRedundancyStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:ommRedundancyStatus.setStatus(_A)
_OmmBrandingFault_Type=TruthValue
_OmmBrandingFault_Object=MibTableColumn
ommBrandingFault=_OmmBrandingFault_Object((1,3,6,1,4,1,21296,2,2,2,1,10,1,1,4),_OmmBrandingFault_Type())
ommBrandingFault.setMaxAccess(_G)
if mibBuilder.loadTexts:ommBrandingFault.setStatus(_A)
_OmmRowStatus_Type=RowStatus
_OmmRowStatus_Object=MibTableColumn
ommRowStatus=_OmmRowStatus_Object((1,3,6,1,4,1,21296,2,2,2,1,10,1,1,5),_OmmRowStatus_Type())
ommRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ommRowStatus.setStatus(_A)
_OmmConformance_ObjectIdentity=ObjectIdentity
ommConformance=_OmmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,10,3))
_OmmCompliances_ObjectIdentity=ObjectIdentity
ommCompliances=_OmmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,10,3,1))
_OmmGroups_ObjectIdentity=ObjectIdentity
ommGroups=_OmmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,10,3,2))
ommGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,1,10,3,2,1))
ommGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:ommGroup.setStatus(_A)
ommCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,1,10,3,1,1))
ommCompliance.setObjects((_B,_M))
if mibBuilder.loadTexts:ommCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ommMIB':ommMIB,'ommTable':ommTable,'ommEntry':ommEntry,_I:ommMoId,_J:ommProvType,_K:ommRedundancyStatus,_H:ommBrandingFault,_L:ommRowStatus,'ommConformance':ommConformance,'ommCompliances':ommCompliances,'ommCompliance':ommCompliance,'ommGroups':ommGroups,_M:ommGroup})