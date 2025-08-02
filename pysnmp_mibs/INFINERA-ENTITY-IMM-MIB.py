_K='immGroup'
_J='immFlashStatus'
_I='immInterfaceTypeNCT'
_H='immProvEqptType'
_G='immMoId'
_F='Integer32'
_E='entLPPhysicalIndex'
_D='ENTITY-MIB'
_C='read-create'
_B='INFINERA-ENTITY-IMM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entLPPhysicalIndex,=mibBuilder.importSymbols(_D,_E)
equipment,=mibBuilder.importSymbols('INFINERA-REG-MIB','equipment')
InfnEqptType,InfnFlashStatus=mibBuilder.importSymbols('INFINERA-TC-MIB','InfnEqptType','InfnFlashStatus')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
immMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,1,27))
_ImmTable_Object=MibTable
immTable=_ImmTable_Object((1,3,6,1,4,1,21296,2,2,2,1,27,1))
if mibBuilder.loadTexts:immTable.setStatus(_A)
_ImmEntry_Object=MibTableRow
immEntry=_ImmEntry_Object((1,3,6,1,4,1,21296,2,2,2,1,27,1,1))
immEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:immEntry.setStatus(_A)
_ImmMoId_Type=DisplayString
_ImmMoId_Object=MibTableColumn
immMoId=_ImmMoId_Object((1,3,6,1,4,1,21296,2,2,2,1,27,1,1,1),_ImmMoId_Type())
immMoId.setMaxAccess(_C)
if mibBuilder.loadTexts:immMoId.setStatus(_A)
_ImmProvEqptType_Type=InfnEqptType
_ImmProvEqptType_Object=MibTableColumn
immProvEqptType=_ImmProvEqptType_Object((1,3,6,1,4,1,21296,2,2,2,1,27,1,1,2),_ImmProvEqptType_Type())
immProvEqptType.setMaxAccess(_C)
if mibBuilder.loadTexts:immProvEqptType.setStatus(_A)
class _ImmInterfaceTypeNCT_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('copper',1),('fiber',2)))
_ImmInterfaceTypeNCT_Type.__name__=_F
_ImmInterfaceTypeNCT_Object=MibTableColumn
immInterfaceTypeNCT=_ImmInterfaceTypeNCT_Object((1,3,6,1,4,1,21296,2,2,2,1,27,1,1,3),_ImmInterfaceTypeNCT_Type())
immInterfaceTypeNCT.setMaxAccess(_C)
if mibBuilder.loadTexts:immInterfaceTypeNCT.setStatus(_A)
_ImmFlashStatus_Type=InfnFlashStatus
_ImmFlashStatus_Object=MibTableColumn
immFlashStatus=_ImmFlashStatus_Object((1,3,6,1,4,1,21296,2,2,2,1,27,1,1,4),_ImmFlashStatus_Type())
immFlashStatus.setMaxAccess('read-only')
if mibBuilder.loadTexts:immFlashStatus.setStatus(_A)
_ImmConformance_ObjectIdentity=ObjectIdentity
immConformance=_ImmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,27,3))
_ImmCompliances_ObjectIdentity=ObjectIdentity
immCompliances=_ImmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,27,3,1))
_ImmGroups_ObjectIdentity=ObjectIdentity
immGroups=_ImmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,27,3,2))
immGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,1,27,3,2,1))
immGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:immGroup.setStatus(_A)
immCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,1,27,3,1,1))
immCompliance.setObjects((_B,_K))
if mibBuilder.loadTexts:immCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'immMIB':immMIB,'immTable':immTable,'immEntry':immEntry,_G:immMoId,_H:immProvEqptType,_I:immInterfaceTypeNCT,_J:immFlashStatus,'immConformance':immConformance,'immCompliances':immCompliances,'immCompliance':immCompliance,'immGroups':immGroups,_K:immGroup})