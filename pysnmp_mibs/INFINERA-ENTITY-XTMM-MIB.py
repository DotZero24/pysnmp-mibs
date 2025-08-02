_J='xtmmGroup'
_I='xtmmRowStatus'
_H='xtmmProvType'
_G='xtmmMoId'
_F='xtmmBrandingFault'
_E='entLPPhysicalIndex'
_D='ENTITY-MIB'
_C='read-create'
_B='INFINERA-ENTITY-XTMM-MIB'
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
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
xtmmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,1,54))
_XtmmTable_Object=MibTable
xtmmTable=_XtmmTable_Object((1,3,6,1,4,1,21296,2,2,2,1,54,1))
if mibBuilder.loadTexts:xtmmTable.setStatus(_A)
_XtmmEntry_Object=MibTableRow
xtmmEntry=_XtmmEntry_Object((1,3,6,1,4,1,21296,2,2,2,1,54,1,1))
xtmmEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:xtmmEntry.setStatus(_A)
_XtmmMoId_Type=DisplayString
_XtmmMoId_Object=MibTableColumn
xtmmMoId=_XtmmMoId_Object((1,3,6,1,4,1,21296,2,2,2,1,54,1,1,1),_XtmmMoId_Type())
xtmmMoId.setMaxAccess(_C)
if mibBuilder.loadTexts:xtmmMoId.setStatus(_A)
_XtmmProvType_Type=InfnEqptType
_XtmmProvType_Object=MibTableColumn
xtmmProvType=_XtmmProvType_Object((1,3,6,1,4,1,21296,2,2,2,1,54,1,1,2),_XtmmProvType_Type())
xtmmProvType.setMaxAccess(_C)
if mibBuilder.loadTexts:xtmmProvType.setStatus(_A)
_XtmmBrandingFault_Type=TruthValue
_XtmmBrandingFault_Object=MibTableColumn
xtmmBrandingFault=_XtmmBrandingFault_Object((1,3,6,1,4,1,21296,2,2,2,1,54,1,1,3),_XtmmBrandingFault_Type())
xtmmBrandingFault.setMaxAccess('read-only')
if mibBuilder.loadTexts:xtmmBrandingFault.setStatus(_A)
_XtmmRowStatus_Type=RowStatus
_XtmmRowStatus_Object=MibTableColumn
xtmmRowStatus=_XtmmRowStatus_Object((1,3,6,1,4,1,21296,2,2,2,1,54,1,1,4),_XtmmRowStatus_Type())
xtmmRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:xtmmRowStatus.setStatus(_A)
_XtmmConformance_ObjectIdentity=ObjectIdentity
xtmmConformance=_XtmmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,54,3))
_XtmmCompliances_ObjectIdentity=ObjectIdentity
xtmmCompliances=_XtmmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,54,3,1))
_XtmmGroups_ObjectIdentity=ObjectIdentity
xtmmGroups=_XtmmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,54,3,2))
xtmmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,1,54,3,2,1))
xtmmGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:xtmmGroup.setStatus(_A)
xtmmCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,1,54,3,1,1))
xtmmCompliance.setObjects((_B,_J))
if mibBuilder.loadTexts:xtmmCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'xtmmMIB':xtmmMIB,'xtmmTable':xtmmTable,'xtmmEntry':xtmmEntry,_G:xtmmMoId,_H:xtmmProvType,_F:xtmmBrandingFault,_I:xtmmRowStatus,'xtmmConformance':xtmmConformance,'xtmmCompliances':xtmmCompliances,'xtmmCompliance':xtmmCompliance,'xtmmGroups':xtmmGroups,_J:xtmmGroup})