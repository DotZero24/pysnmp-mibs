_P='xlmGroup'
_O='xlmRowStatus'
_N='xlmInstalledOcgNumber'
_M='xlmProvisionedOcgNumber'
_L='xlmProvEqptType'
_K='xlmPicDspVer'
_J='xlmMoId'
_I='read-only'
_H='InfnOperatingMode'
_G='entLPPhysicalIndex'
_F='ENTITY-MIB'
_E='xlmOperatingMode'
_D='xlmAvailableTunableOcgNumbers'
_C='read-create'
_B='INFINERA-ENTITY-XLM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entLPPhysicalIndex,=mibBuilder.importSymbols(_F,_G)
equipment,=mibBuilder.importSymbols('INFINERA-REG-MIB','equipment')
InfnEqptType,InfnOperatingMode=mibBuilder.importSymbols('INFINERA-TC-MIB','InfnEqptType',_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
xlmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,1,5))
_XlmTable_Object=MibTable
xlmTable=_XlmTable_Object((1,3,6,1,4,1,21296,2,2,2,1,5,1))
if mibBuilder.loadTexts:xlmTable.setStatus(_A)
_XlmEntry_Object=MibTableRow
xlmEntry=_XlmEntry_Object((1,3,6,1,4,1,21296,2,2,2,1,5,1,1))
xlmEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:xlmEntry.setStatus(_A)
_XlmMoId_Type=DisplayString
_XlmMoId_Object=MibTableColumn
xlmMoId=_XlmMoId_Object((1,3,6,1,4,1,21296,2,2,2,1,5,1,1,1),_XlmMoId_Type())
xlmMoId.setMaxAccess(_C)
if mibBuilder.loadTexts:xlmMoId.setStatus(_A)
_XlmProvEqptType_Type=InfnEqptType
_XlmProvEqptType_Object=MibTableColumn
xlmProvEqptType=_XlmProvEqptType_Object((1,3,6,1,4,1,21296,2,2,2,1,5,1,1,2),_XlmProvEqptType_Type())
xlmProvEqptType.setMaxAccess(_C)
if mibBuilder.loadTexts:xlmProvEqptType.setStatus(_A)
_XlmPicDspVer_Type=DisplayString
_XlmPicDspVer_Object=MibTableColumn
xlmPicDspVer=_XlmPicDspVer_Object((1,3,6,1,4,1,21296,2,2,2,1,5,1,1,3),_XlmPicDspVer_Type())
xlmPicDspVer.setMaxAccess(_I)
if mibBuilder.loadTexts:xlmPicDspVer.setStatus(_A)
class _XlmOperatingMode_Type(InfnOperatingMode):defaultValue=2
_XlmOperatingMode_Type.__name__=_H
_XlmOperatingMode_Object=MibTableColumn
xlmOperatingMode=_XlmOperatingMode_Object((1,3,6,1,4,1,21296,2,2,2,1,5,1,1,4),_XlmOperatingMode_Type())
xlmOperatingMode.setMaxAccess(_C)
if mibBuilder.loadTexts:xlmOperatingMode.setStatus(_A)
_XlmAvailableTunableOcgNumbers_Type=Integer32
_XlmAvailableTunableOcgNumbers_Object=MibTableColumn
xlmAvailableTunableOcgNumbers=_XlmAvailableTunableOcgNumbers_Object((1,3,6,1,4,1,21296,2,2,2,1,5,1,1,5),_XlmAvailableTunableOcgNumbers_Type())
xlmAvailableTunableOcgNumbers.setMaxAccess(_I)
if mibBuilder.loadTexts:xlmAvailableTunableOcgNumbers.setStatus(_A)
_XlmProvisionedOcgNumber_Type=Integer32
_XlmProvisionedOcgNumber_Object=MibTableColumn
xlmProvisionedOcgNumber=_XlmProvisionedOcgNumber_Object((1,3,6,1,4,1,21296,2,2,2,1,5,1,1,6),_XlmProvisionedOcgNumber_Type())
xlmProvisionedOcgNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:xlmProvisionedOcgNumber.setStatus(_A)
_XlmInstalledOcgNumber_Type=Integer32
_XlmInstalledOcgNumber_Object=MibTableColumn
xlmInstalledOcgNumber=_XlmInstalledOcgNumber_Object((1,3,6,1,4,1,21296,2,2,2,1,5,1,1,7),_XlmInstalledOcgNumber_Type())
xlmInstalledOcgNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:xlmInstalledOcgNumber.setStatus(_A)
_XlmRowStatus_Type=RowStatus
_XlmRowStatus_Object=MibTableColumn
xlmRowStatus=_XlmRowStatus_Object((1,3,6,1,4,1,21296,2,2,2,1,5,1,1,8),_XlmRowStatus_Type())
xlmRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:xlmRowStatus.setStatus(_A)
_XlmConformance_ObjectIdentity=ObjectIdentity
xlmConformance=_XlmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,5,3))
_XlmCompliances_ObjectIdentity=ObjectIdentity
xlmCompliances=_XlmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,5,3,1))
_XlmGroups_ObjectIdentity=ObjectIdentity
xlmGroups=_XlmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,5,3,2))
xlmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,1,5,3,2,1))
xlmGroup.setObjects(*((_B,_D),(_B,_J),(_B,_E),(_B,_K),(_B,_L),(_B,_E),(_B,_D),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:xlmGroup.setStatus(_A)
xlmCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,1,5,3,1,1))
xlmCompliance.setObjects((_B,_P))
if mibBuilder.loadTexts:xlmCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'xlmMIB':xlmMIB,'xlmTable':xlmTable,'xlmEntry':xlmEntry,_J:xlmMoId,_L:xlmProvEqptType,_K:xlmPicDspVer,_E:xlmOperatingMode,_D:xlmAvailableTunableOcgNumbers,_M:xlmProvisionedOcgNumber,_N:xlmInstalledOcgNumber,_O:xlmRowStatus,'xlmConformance':xlmConformance,'xlmCompliances':xlmCompliances,'xlmCompliance':xlmCompliance,'xlmGroups':xlmGroups,_P:xlmGroup})