_I='cmmGroup'
_H='cmmRowStatus'
_G='cmmProvEqptType'
_F='cmmMoId'
_E='entLPPhysicalIndex'
_D='ENTITY-MIB'
_C='read-create'
_B='INFINERA-ENTITY-CMM-MIB'
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
cmmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,1,19))
_CmmTable_Object=MibTable
cmmTable=_CmmTable_Object((1,3,6,1,4,1,21296,2,2,2,1,19,1))
if mibBuilder.loadTexts:cmmTable.setStatus(_A)
_CmmEntry_Object=MibTableRow
cmmEntry=_CmmEntry_Object((1,3,6,1,4,1,21296,2,2,2,1,19,1,1))
cmmEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:cmmEntry.setStatus(_A)
_CmmMoId_Type=DisplayString
_CmmMoId_Object=MibTableColumn
cmmMoId=_CmmMoId_Object((1,3,6,1,4,1,21296,2,2,2,1,19,1,1,1),_CmmMoId_Type())
cmmMoId.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmMoId.setStatus(_A)
_CmmProvEqptType_Type=InfnEqptType
_CmmProvEqptType_Object=MibTableColumn
cmmProvEqptType=_CmmProvEqptType_Object((1,3,6,1,4,1,21296,2,2,2,1,19,1,1,2),_CmmProvEqptType_Type())
cmmProvEqptType.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmProvEqptType.setStatus(_A)
_CmmRowStatus_Type=RowStatus
_CmmRowStatus_Object=MibTableColumn
cmmRowStatus=_CmmRowStatus_Object((1,3,6,1,4,1,21296,2,2,2,1,19,1,1,3),_CmmRowStatus_Type())
cmmRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmRowStatus.setStatus(_A)
_CmmConformance_ObjectIdentity=ObjectIdentity
cmmConformance=_CmmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,19,14))
_CmmCompliances_ObjectIdentity=ObjectIdentity
cmmCompliances=_CmmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,19,14,1))
_CmmGroups_ObjectIdentity=ObjectIdentity
cmmGroups=_CmmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,19,14,2))
cmmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,1,19,14,2,1))
cmmGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H)))
if mibBuilder.loadTexts:cmmGroup.setStatus(_A)
cmmCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,1,19,14,1,1))
cmmCompliance.setObjects((_B,_I))
if mibBuilder.loadTexts:cmmCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'cmmMIB':cmmMIB,'cmmTable':cmmTable,'cmmEntry':cmmEntry,_F:cmmMoId,_G:cmmProvEqptType,_H:cmmRowStatus,'cmmConformance':cmmConformance,'cmmCompliances':cmmCompliances,'cmmCompliance':cmmCompliance,'cmmGroups':cmmGroups,_I:cmmGroup})