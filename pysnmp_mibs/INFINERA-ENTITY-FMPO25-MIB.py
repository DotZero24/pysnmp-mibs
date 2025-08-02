_I='fmpo25Group'
_H='fmpo25ProvSerialNumber'
_G='fmpo25ProvEqptType'
_F='fmpo25MoId'
_E='read-create'
_D='entLPPhysicalIndex'
_C='ENTITY-MIB'
_B='INFINERA-ENTITY-FMPO25-MIB'
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
fmpo25MIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,1,51))
_Fmpo25Table_Object=MibTable
fmpo25Table=_Fmpo25Table_Object((1,3,6,1,4,1,21296,2,2,2,1,51,1))
if mibBuilder.loadTexts:fmpo25Table.setStatus(_A)
_Fmpo25Entry_Object=MibTableRow
fmpo25Entry=_Fmpo25Entry_Object((1,3,6,1,4,1,21296,2,2,2,1,51,1,1))
fmpo25Entry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:fmpo25Entry.setStatus(_A)
_Fmpo25MoId_Type=DisplayString
_Fmpo25MoId_Object=MibTableColumn
fmpo25MoId=_Fmpo25MoId_Object((1,3,6,1,4,1,21296,2,2,2,1,51,1,1,1),_Fmpo25MoId_Type())
fmpo25MoId.setMaxAccess(_E)
if mibBuilder.loadTexts:fmpo25MoId.setStatus(_A)
_Fmpo25ProvEqptType_Type=InfnEqptType
_Fmpo25ProvEqptType_Object=MibTableColumn
fmpo25ProvEqptType=_Fmpo25ProvEqptType_Object((1,3,6,1,4,1,21296,2,2,2,1,51,1,1,2),_Fmpo25ProvEqptType_Type())
fmpo25ProvEqptType.setMaxAccess(_E)
if mibBuilder.loadTexts:fmpo25ProvEqptType.setStatus(_A)
_Fmpo25ProvSerialNumber_Type=DisplayString
_Fmpo25ProvSerialNumber_Object=MibTableColumn
fmpo25ProvSerialNumber=_Fmpo25ProvSerialNumber_Object((1,3,6,1,4,1,21296,2,2,2,1,51,1,1,3),_Fmpo25ProvSerialNumber_Type())
fmpo25ProvSerialNumber.setMaxAccess('read-write')
if mibBuilder.loadTexts:fmpo25ProvSerialNumber.setStatus(_A)
_Fmpo25Conformance_ObjectIdentity=ObjectIdentity
fmpo25Conformance=_Fmpo25Conformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,51,3))
_Fmpo25Compliances_ObjectIdentity=ObjectIdentity
fmpo25Compliances=_Fmpo25Compliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,51,3,1))
_Fmpo25Groups_ObjectIdentity=ObjectIdentity
fmpo25Groups=_Fmpo25Groups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,51,3,2))
fmpo25Group=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,1,51,3,2,1))
fmpo25Group.setObjects(*((_B,_F),(_B,_G),(_B,_H)))
if mibBuilder.loadTexts:fmpo25Group.setStatus(_A)
fmpo25Compliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,1,51,3,1,1))
fmpo25Compliance.setObjects((_B,_I))
if mibBuilder.loadTexts:fmpo25Compliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fmpo25MIB':fmpo25MIB,'fmpo25Table':fmpo25Table,'fmpo25Entry':fmpo25Entry,_F:fmpo25MoId,_G:fmpo25ProvEqptType,_H:fmpo25ProvSerialNumber,'fmpo25Conformance':fmpo25Conformance,'fmpo25Compliances':fmpo25Compliances,'fmpo25Compliance':fmpo25Compliance,'fmpo25Groups':fmpo25Groups,_I:fmpo25Group})