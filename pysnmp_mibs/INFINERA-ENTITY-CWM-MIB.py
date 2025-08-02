_I='cwmGroup'
_H='cwmAssociatedDegree'
_G='cwmProvEqptType'
_F='cwmMoId'
_E='entPhysicalIndex'
_D='ENTITY-MIB'
_C='read-write'
_B='INFINERA-ENTITY-CWM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entPhysicalIndex,=mibBuilder.importSymbols(_D,_E)
equipment,=mibBuilder.importSymbols('INFINERA-REG-MIB','equipment')
InfnEqptType,=mibBuilder.importSymbols('INFINERA-TC-MIB','InfnEqptType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
cwmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,1,57))
_CwmTable_Object=MibTable
cwmTable=_CwmTable_Object((1,3,6,1,4,1,21296,2,2,2,1,57,1))
if mibBuilder.loadTexts:cwmTable.setStatus(_A)
_CwmEntry_Object=MibTableRow
cwmEntry=_CwmEntry_Object((1,3,6,1,4,1,21296,2,2,2,1,57,1,1))
cwmEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:cwmEntry.setStatus(_A)
_CwmMoId_Type=DisplayString
_CwmMoId_Object=MibTableColumn
cwmMoId=_CwmMoId_Object((1,3,6,1,4,1,21296,2,2,2,1,57,1,1,1),_CwmMoId_Type())
cwmMoId.setMaxAccess(_C)
if mibBuilder.loadTexts:cwmMoId.setStatus(_A)
_CwmProvEqptType_Type=InfnEqptType
_CwmProvEqptType_Object=MibTableColumn
cwmProvEqptType=_CwmProvEqptType_Object((1,3,6,1,4,1,21296,2,2,2,1,57,1,1,2),_CwmProvEqptType_Type())
cwmProvEqptType.setMaxAccess(_C)
if mibBuilder.loadTexts:cwmProvEqptType.setStatus(_A)
_CwmAssociatedDegree_Type=DisplayString
_CwmAssociatedDegree_Object=MibTableColumn
cwmAssociatedDegree=_CwmAssociatedDegree_Object((1,3,6,1,4,1,21296,2,2,2,1,57,1,1,3),_CwmAssociatedDegree_Type())
cwmAssociatedDegree.setMaxAccess(_C)
if mibBuilder.loadTexts:cwmAssociatedDegree.setStatus(_A)
_CwmConformance_ObjectIdentity=ObjectIdentity
cwmConformance=_CwmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,57,3))
_CwmCompliances_ObjectIdentity=ObjectIdentity
cwmCompliances=_CwmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,57,3,1))
_CwmGroups_ObjectIdentity=ObjectIdentity
cwmGroups=_CwmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,57,3,2))
cwmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,1,57,3,2,1))
cwmGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H)))
if mibBuilder.loadTexts:cwmGroup.setStatus(_A)
cwmCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,1,57,3,1,1))
cwmCompliance.setObjects((_B,_I))
if mibBuilder.loadTexts:cwmCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'cwmMIB':cwmMIB,'cwmTable':cwmTable,'cwmEntry':cwmEntry,_F:cwmMoId,_G:cwmProvEqptType,_H:cwmAssociatedDegree,'cwmConformance':cwmConformance,'cwmCompliances':cwmCompliances,'cwmCompliance':cwmCompliance,'cwmGroups':cwmGroups,_I:cwmGroup})