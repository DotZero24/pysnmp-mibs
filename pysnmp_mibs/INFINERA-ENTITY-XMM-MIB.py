_J='xmmGroup'
_I='xmmRowStatus'
_H='xmmProvType'
_G='xmmMoId'
_F='xmmBrandingFault'
_E='entLPPhysicalIndex'
_D='ENTITY-MIB'
_C='read-create'
_B='INFINERA-ENTITY-XMM-MIB'
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
xmmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,1,36))
_XmmTable_Object=MibTable
xmmTable=_XmmTable_Object((1,3,6,1,4,1,21296,2,2,2,1,36,1))
if mibBuilder.loadTexts:xmmTable.setStatus(_A)
_XmmEntry_Object=MibTableRow
xmmEntry=_XmmEntry_Object((1,3,6,1,4,1,21296,2,2,2,1,36,1,1))
xmmEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:xmmEntry.setStatus(_A)
_XmmMoId_Type=DisplayString
_XmmMoId_Object=MibTableColumn
xmmMoId=_XmmMoId_Object((1,3,6,1,4,1,21296,2,2,2,1,36,1,1,1),_XmmMoId_Type())
xmmMoId.setMaxAccess(_C)
if mibBuilder.loadTexts:xmmMoId.setStatus(_A)
_XmmProvType_Type=InfnEqptType
_XmmProvType_Object=MibTableColumn
xmmProvType=_XmmProvType_Object((1,3,6,1,4,1,21296,2,2,2,1,36,1,1,2),_XmmProvType_Type())
xmmProvType.setMaxAccess(_C)
if mibBuilder.loadTexts:xmmProvType.setStatus(_A)
_XmmBrandingFault_Type=TruthValue
_XmmBrandingFault_Object=MibTableColumn
xmmBrandingFault=_XmmBrandingFault_Object((1,3,6,1,4,1,21296,2,2,2,1,36,1,1,3),_XmmBrandingFault_Type())
xmmBrandingFault.setMaxAccess('read-only')
if mibBuilder.loadTexts:xmmBrandingFault.setStatus(_A)
_XmmRowStatus_Type=RowStatus
_XmmRowStatus_Object=MibTableColumn
xmmRowStatus=_XmmRowStatus_Object((1,3,6,1,4,1,21296,2,2,2,1,36,1,1,4),_XmmRowStatus_Type())
xmmRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:xmmRowStatus.setStatus(_A)
_XmmConformance_ObjectIdentity=ObjectIdentity
xmmConformance=_XmmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,36,3))
_XmmCompliances_ObjectIdentity=ObjectIdentity
xmmCompliances=_XmmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,36,3,1))
_XmmGroups_ObjectIdentity=ObjectIdentity
xmmGroups=_XmmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,36,3,2))
xmmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,1,36,3,2,1))
xmmGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:xmmGroup.setStatus(_A)
xmmCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,1,36,3,1,1))
xmmCompliance.setObjects((_B,_J))
if mibBuilder.loadTexts:xmmCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'xmmMIB':xmmMIB,'xmmTable':xmmTable,'xmmEntry':xmmEntry,_G:xmmMoId,_H:xmmProvType,_F:xmmBrandingFault,_I:xmmRowStatus,'xmmConformance':xmmConformance,'xmmCompliances':xmmCompliances,'xmmCompliance':xmmCompliance,'xmmGroups':xmmGroups,_J:xmmGroup})