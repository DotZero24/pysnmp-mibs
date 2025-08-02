_N='gamGroup'
_M='gamInstOperatingMode'
_L='gamOperatingMode'
_K='gamRowStatus'
_J='gamProvEqptType'
_I='gamMoId'
_H='aseGain'
_G='aseSource'
_F='entLPPhysicalIndex'
_E='ENTITY-MIB'
_D='Integer32'
_C='read-create'
_B='INFINERA-ENTITY-GAM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entLPPhysicalIndex,=mibBuilder.importSymbols(_E,_F)
equipment,=mibBuilder.importSymbols('INFINERA-REG-MIB','equipment')
InfnEqptType,=mibBuilder.importSymbols('INFINERA-TC-MIB','InfnEqptType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
gamMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,1,8))
_GamTable_Object=MibTable
gamTable=_GamTable_Object((1,3,6,1,4,1,21296,2,2,2,1,8,1))
if mibBuilder.loadTexts:gamTable.setStatus(_A)
_GamEntry_Object=MibTableRow
gamEntry=_GamEntry_Object((1,3,6,1,4,1,21296,2,2,2,1,8,1,1))
gamEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:gamEntry.setStatus(_A)
_GamMoId_Type=DisplayString
_GamMoId_Object=MibTableColumn
gamMoId=_GamMoId_Object((1,3,6,1,4,1,21296,2,2,2,1,8,1,1,1),_GamMoId_Type())
gamMoId.setMaxAccess(_C)
if mibBuilder.loadTexts:gamMoId.setStatus(_A)
_GamProvEqptType_Type=InfnEqptType
_GamProvEqptType_Object=MibTableColumn
gamProvEqptType=_GamProvEqptType_Object((1,3,6,1,4,1,21296,2,2,2,1,8,1,1,2),_GamProvEqptType_Type())
gamProvEqptType.setMaxAccess(_C)
if mibBuilder.loadTexts:gamProvEqptType.setStatus(_A)
_GamRowStatus_Type=RowStatus
_GamRowStatus_Object=MibTableColumn
gamRowStatus=_GamRowStatus_Object((1,3,6,1,4,1,21296,2,2,2,1,8,1,1,3),_GamRowStatus_Type())
gamRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:gamRowStatus.setStatus(_A)
class _GamOperatingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('gam',2),(_G,3),(_H,4)))
_GamOperatingMode_Type.__name__=_D
_GamOperatingMode_Object=MibTableColumn
gamOperatingMode=_GamOperatingMode_Object((1,3,6,1,4,1,21296,2,2,2,1,8,1,1,4),_GamOperatingMode_Type())
gamOperatingMode.setMaxAccess(_C)
if mibBuilder.loadTexts:gamOperatingMode.setStatus(_A)
class _GamInstOperatingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('gam',2),(_G,3),(_H,4)))
_GamInstOperatingMode_Type.__name__=_D
_GamInstOperatingMode_Object=MibTableColumn
gamInstOperatingMode=_GamInstOperatingMode_Object((1,3,6,1,4,1,21296,2,2,2,1,8,1,1,5),_GamInstOperatingMode_Type())
gamInstOperatingMode.setMaxAccess('read-only')
if mibBuilder.loadTexts:gamInstOperatingMode.setStatus(_A)
_GamConformance_ObjectIdentity=ObjectIdentity
gamConformance=_GamConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,8,3))
_GamCompliances_ObjectIdentity=ObjectIdentity
gamCompliances=_GamCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,8,3,1))
_GamGroups_ObjectIdentity=ObjectIdentity
gamGroups=_GamGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,8,3,2))
gamGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,1,8,3,2,1))
gamGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:gamGroup.setStatus(_A)
gamCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,1,8,3,1,1))
gamCompliance.setObjects((_B,_N))
if mibBuilder.loadTexts:gamCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'gamMIB':gamMIB,'gamTable':gamTable,'gamEntry':gamEntry,_I:gamMoId,_J:gamProvEqptType,_K:gamRowStatus,_L:gamOperatingMode,_M:gamInstOperatingMode,'gamConformance':gamConformance,'gamCompliances':gamCompliances,'gamCompliance':gamCompliance,'gamGroups':gamGroups,_N:gamGroup})