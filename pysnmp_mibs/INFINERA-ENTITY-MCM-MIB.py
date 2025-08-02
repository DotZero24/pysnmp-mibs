_M='mcmGroup'
_L='mcmRowStatus'
_K='mcmRedundancyStatus'
_J='mcmProvType'
_I='mcmMoId'
_H='mcmBrandingFault'
_G='read-only'
_F='Integer32'
_E='entLPPhysicalIndex'
_D='ENTITY-MIB'
_C='read-create'
_B='INFINERA-ENTITY-MCM-MIB'
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
mcmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,1,2))
_McmTable_Object=MibTable
mcmTable=_McmTable_Object((1,3,6,1,4,1,21296,2,2,2,1,2,1))
if mibBuilder.loadTexts:mcmTable.setStatus(_A)
_McmEntry_Object=MibTableRow
mcmEntry=_McmEntry_Object((1,3,6,1,4,1,21296,2,2,2,1,2,1,1))
mcmEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:mcmEntry.setStatus(_A)
_McmMoId_Type=DisplayString
_McmMoId_Object=MibTableColumn
mcmMoId=_McmMoId_Object((1,3,6,1,4,1,21296,2,2,2,1,2,1,1,1),_McmMoId_Type())
mcmMoId.setMaxAccess(_C)
if mibBuilder.loadTexts:mcmMoId.setStatus(_A)
_McmProvType_Type=InfnEqptType
_McmProvType_Object=MibTableColumn
mcmProvType=_McmProvType_Object((1,3,6,1,4,1,21296,2,2,2,1,2,1,1,2),_McmProvType_Type())
mcmProvType.setMaxAccess(_C)
if mibBuilder.loadTexts:mcmProvType.setStatus(_A)
class _McmRedundancyStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('none',1),('single',2),('active',3),('standby',4),('makeStandbyInProgress',5),('oos',6),('lock',7)))
_McmRedundancyStatus_Type.__name__=_F
_McmRedundancyStatus_Object=MibTableColumn
mcmRedundancyStatus=_McmRedundancyStatus_Object((1,3,6,1,4,1,21296,2,2,2,1,2,1,1,3),_McmRedundancyStatus_Type())
mcmRedundancyStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:mcmRedundancyStatus.setStatus(_A)
_McmBrandingFault_Type=TruthValue
_McmBrandingFault_Object=MibTableColumn
mcmBrandingFault=_McmBrandingFault_Object((1,3,6,1,4,1,21296,2,2,2,1,2,1,1,4),_McmBrandingFault_Type())
mcmBrandingFault.setMaxAccess(_G)
if mibBuilder.loadTexts:mcmBrandingFault.setStatus(_A)
_McmRowStatus_Type=RowStatus
_McmRowStatus_Object=MibTableColumn
mcmRowStatus=_McmRowStatus_Object((1,3,6,1,4,1,21296,2,2,2,1,2,1,1,5),_McmRowStatus_Type())
mcmRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mcmRowStatus.setStatus(_A)
_McmConformance_ObjectIdentity=ObjectIdentity
mcmConformance=_McmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,2,3))
_McmCompliances_ObjectIdentity=ObjectIdentity
mcmCompliances=_McmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,2,3,1))
_McmGroups_ObjectIdentity=ObjectIdentity
mcmGroups=_McmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,2,3,2))
mcmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,1,2,3,2,1))
mcmGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:mcmGroup.setStatus(_A)
mcmCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,1,2,3,1,1))
mcmCompliance.setObjects((_B,_M))
if mibBuilder.loadTexts:mcmCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'mcmMIB':mcmMIB,'mcmTable':mcmTable,'mcmEntry':mcmEntry,_I:mcmMoId,_J:mcmProvType,_K:mcmRedundancyStatus,_H:mcmBrandingFault,_L:mcmRowStatus,'mcmConformance':mcmConformance,'mcmCompliances':mcmCompliances,'mcmCompliance':mcmCompliance,'mcmGroups':mcmGroups,_M:mcmGroup})