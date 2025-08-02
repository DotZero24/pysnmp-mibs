_J='otmGroup'
_I='actvTimingSource'
_H='otmRowStatus'
_G='otmProvEqptType'
_F='otmMoId'
_E='entLPPhysicalIndex'
_D='ENTITY-MIB'
_C='read-create'
_B='INFINERA-ENTITY-OTM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entLPPhysicalIndex,=mibBuilder.importSymbols(_D,_E)
equipment,=mibBuilder.importSymbols('INFINERA-REG-MIB','equipment')
InfnEqptType,=mibBuilder.importSymbols('INFINERA-TC-MIB','InfnEqptType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
otmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,1,24))
_OtmTable_Object=MibTable
otmTable=_OtmTable_Object((1,3,6,1,4,1,21296,2,2,2,1,24,1))
if mibBuilder.loadTexts:otmTable.setStatus(_A)
_OtmEntry_Object=MibTableRow
otmEntry=_OtmEntry_Object((1,3,6,1,4,1,21296,2,2,2,1,24,1,1))
otmEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:otmEntry.setStatus(_A)
_OtmMoId_Type=DisplayString
_OtmMoId_Object=MibTableColumn
otmMoId=_OtmMoId_Object((1,3,6,1,4,1,21296,2,2,2,1,24,1,1,1),_OtmMoId_Type())
otmMoId.setMaxAccess(_C)
if mibBuilder.loadTexts:otmMoId.setStatus(_A)
_OtmProvEqptType_Type=InfnEqptType
_OtmProvEqptType_Object=MibTableColumn
otmProvEqptType=_OtmProvEqptType_Object((1,3,6,1,4,1,21296,2,2,2,1,24,1,1,2),_OtmProvEqptType_Type())
otmProvEqptType.setMaxAccess(_C)
if mibBuilder.loadTexts:otmProvEqptType.setStatus(_A)
_OtmRowStatus_Type=RowStatus
_OtmRowStatus_Object=MibTableColumn
otmRowStatus=_OtmRowStatus_Object((1,3,6,1,4,1,21296,2,2,2,1,24,1,1,3),_OtmRowStatus_Type())
otmRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:otmRowStatus.setStatus(_A)
_ActvTimingSource_Type=DisplayString
_ActvTimingSource_Object=MibTableColumn
actvTimingSource=_ActvTimingSource_Object((1,3,6,1,4,1,21296,2,2,2,1,24,1,1,4),_ActvTimingSource_Type())
actvTimingSource.setMaxAccess('read-only')
if mibBuilder.loadTexts:actvTimingSource.setStatus(_A)
_OtmConformance_ObjectIdentity=ObjectIdentity
otmConformance=_OtmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,24,3))
_OtmCompliances_ObjectIdentity=ObjectIdentity
otmCompliances=_OtmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,24,3,1))
_OtmGroups_ObjectIdentity=ObjectIdentity
otmGroups=_OtmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,24,3,2))
otmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,1,24,3,2,1))
otmGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:otmGroup.setStatus(_A)
otmCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,1,24,3,1,1))
otmCompliance.setObjects((_B,_J))
if mibBuilder.loadTexts:otmCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'otmMIB':otmMIB,'otmTable':otmTable,'otmEntry':otmEntry,_F:otmMoId,_G:otmProvEqptType,_H:otmRowStatus,_I:actvTimingSource,'otmConformance':otmConformance,'otmCompliances':otmCompliances,'otmCompliance':otmCompliance,'otmGroups':otmGroups,_J:otmGroup})