_I='fmpo50Group'
_H='fmpo50ProvSerialNumber'
_G='fmpo50ProvEqptType'
_F='fmpo50MoId'
_E='read-create'
_D='entLPPhysicalIndex'
_C='ENTITY-MIB'
_B='INFINERA-ENTITY-FMPO50-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entLPPhysicalIndex,=mibBuilder.importSymbols(_C,_D)
equipment,=mibBuilder.importSymbols('INFINERA-REG-MIB','equipment')
InfnEqptType,=mibBuilder.importSymbols('INFINERA-TC-MIB','InfnEqptType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
fmpo50MIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,1,52))
_Fmpo50Table_Object=MibTable
fmpo50Table=_Fmpo50Table_Object((1,3,6,1,4,1,21296,2,2,2,1,52,1))
if mibBuilder.loadTexts:fmpo50Table.setStatus(_A)
_Fmpo50Entry_Object=MibTableRow
fmpo50Entry=_Fmpo50Entry_Object((1,3,6,1,4,1,21296,2,2,2,1,52,1,1))
fmpo50Entry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:fmpo50Entry.setStatus(_A)
_Fmpo50MoId_Type=DisplayString
_Fmpo50MoId_Object=MibTableColumn
fmpo50MoId=_Fmpo50MoId_Object((1,3,6,1,4,1,21296,2,2,2,1,52,1,1,1),_Fmpo50MoId_Type())
fmpo50MoId.setMaxAccess(_E)
if mibBuilder.loadTexts:fmpo50MoId.setStatus(_A)
_Fmpo50ProvEqptType_Type=InfnEqptType
_Fmpo50ProvEqptType_Object=MibTableColumn
fmpo50ProvEqptType=_Fmpo50ProvEqptType_Object((1,3,6,1,4,1,21296,2,2,2,1,52,1,1,2),_Fmpo50ProvEqptType_Type())
fmpo50ProvEqptType.setMaxAccess(_E)
if mibBuilder.loadTexts:fmpo50ProvEqptType.setStatus(_A)
_Fmpo50ProvSerialNumber_Type=DisplayString
_Fmpo50ProvSerialNumber_Object=MibTableColumn
fmpo50ProvSerialNumber=_Fmpo50ProvSerialNumber_Object((1,3,6,1,4,1,21296,2,2,2,1,52,1,1,3),_Fmpo50ProvSerialNumber_Type())
fmpo50ProvSerialNumber.setMaxAccess('read-write')
if mibBuilder.loadTexts:fmpo50ProvSerialNumber.setStatus(_A)
_Fmpo50Conformance_ObjectIdentity=ObjectIdentity
fmpo50Conformance=_Fmpo50Conformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,52,3))
_Fmpo50Compliances_ObjectIdentity=ObjectIdentity
fmpo50Compliances=_Fmpo50Compliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,52,3,1))
_Fmpo50Groups_ObjectIdentity=ObjectIdentity
fmpo50Groups=_Fmpo50Groups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,52,3,2))
fmpo50Group=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,1,52,3,2,1))
fmpo50Group.setObjects(*((_B,_F),(_B,_G),(_B,_H)))
if mibBuilder.loadTexts:fmpo50Group.setStatus(_A)
fmpo50Compliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,1,52,3,1,1))
fmpo50Compliance.setObjects((_B,_I))
if mibBuilder.loadTexts:fmpo50Compliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fmpo50MIB':fmpo50MIB,'fmpo50Table':fmpo50Table,'fmpo50Entry':fmpo50Entry,_F:fmpo50MoId,_G:fmpo50ProvEqptType,_H:fmpo50ProvSerialNumber,'fmpo50Conformance':fmpo50Conformance,'fmpo50Compliances':fmpo50Compliances,'fmpo50Compliance':fmpo50Compliance,'fmpo50Groups':fmpo50Groups,_I:fmpo50Group})