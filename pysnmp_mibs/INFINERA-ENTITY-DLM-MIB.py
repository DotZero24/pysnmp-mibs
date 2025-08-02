_Q='dlmGroup'
_P='dlmOpticsFirmwareVer'
_O='dlmRowStatus'
_N='dlmInstalledOcgNumber'
_M='dlmProvisionedOcgNumber'
_L='dlmProvEqptType'
_K='dlmPicDspVer'
_J='dlmOperatingMode'
_I='dlmMoId'
_H='dlmAvailableTunableOcgNumbers'
_G='InfnOperatingMode'
_F='entLPPhysicalIndex'
_E='ENTITY-MIB'
_D='read-only'
_C='read-create'
_B='INFINERA-ENTITY-DLM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entLPPhysicalIndex,=mibBuilder.importSymbols(_E,_F)
equipment,=mibBuilder.importSymbols('INFINERA-REG-MIB','equipment')
InfnEqptType,InfnOperatingMode=mibBuilder.importSymbols('INFINERA-TC-MIB','InfnEqptType',_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
dlmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,1,4))
_DlmTable_Object=MibTable
dlmTable=_DlmTable_Object((1,3,6,1,4,1,21296,2,2,2,1,4,1))
if mibBuilder.loadTexts:dlmTable.setStatus(_A)
_DlmEntry_Object=MibTableRow
dlmEntry=_DlmEntry_Object((1,3,6,1,4,1,21296,2,2,2,1,4,1,1))
dlmEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:dlmEntry.setStatus(_A)
_DlmMoId_Type=DisplayString
_DlmMoId_Object=MibTableColumn
dlmMoId=_DlmMoId_Object((1,3,6,1,4,1,21296,2,2,2,1,4,1,1,1),_DlmMoId_Type())
dlmMoId.setMaxAccess(_C)
if mibBuilder.loadTexts:dlmMoId.setStatus(_A)
_DlmProvEqptType_Type=InfnEqptType
_DlmProvEqptType_Object=MibTableColumn
dlmProvEqptType=_DlmProvEqptType_Object((1,3,6,1,4,1,21296,2,2,2,1,4,1,1,2),_DlmProvEqptType_Type())
dlmProvEqptType.setMaxAccess(_C)
if mibBuilder.loadTexts:dlmProvEqptType.setStatus(_A)
_DlmPicDspVer_Type=DisplayString
_DlmPicDspVer_Object=MibTableColumn
dlmPicDspVer=_DlmPicDspVer_Object((1,3,6,1,4,1,21296,2,2,2,1,4,1,1,3),_DlmPicDspVer_Type())
dlmPicDspVer.setMaxAccess(_D)
if mibBuilder.loadTexts:dlmPicDspVer.setStatus(_A)
class _DlmOperatingMode_Type(InfnOperatingMode):defaultValue=2
_DlmOperatingMode_Type.__name__=_G
_DlmOperatingMode_Object=MibTableColumn
dlmOperatingMode=_DlmOperatingMode_Object((1,3,6,1,4,1,21296,2,2,2,1,4,1,1,4),_DlmOperatingMode_Type())
dlmOperatingMode.setMaxAccess(_C)
if mibBuilder.loadTexts:dlmOperatingMode.setStatus(_A)
_DlmAvailableTunableOcgNumbers_Type=Integer32
_DlmAvailableTunableOcgNumbers_Object=MibTableColumn
dlmAvailableTunableOcgNumbers=_DlmAvailableTunableOcgNumbers_Object((1,3,6,1,4,1,21296,2,2,2,1,4,1,1,5),_DlmAvailableTunableOcgNumbers_Type())
dlmAvailableTunableOcgNumbers.setMaxAccess(_D)
if mibBuilder.loadTexts:dlmAvailableTunableOcgNumbers.setStatus(_A)
_DlmProvisionedOcgNumber_Type=Integer32
_DlmProvisionedOcgNumber_Object=MibTableColumn
dlmProvisionedOcgNumber=_DlmProvisionedOcgNumber_Object((1,3,6,1,4,1,21296,2,2,2,1,4,1,1,6),_DlmProvisionedOcgNumber_Type())
dlmProvisionedOcgNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:dlmProvisionedOcgNumber.setStatus(_A)
_DlmInstalledOcgNumber_Type=Integer32
_DlmInstalledOcgNumber_Object=MibTableColumn
dlmInstalledOcgNumber=_DlmInstalledOcgNumber_Object((1,3,6,1,4,1,21296,2,2,2,1,4,1,1,7),_DlmInstalledOcgNumber_Type())
dlmInstalledOcgNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:dlmInstalledOcgNumber.setStatus(_A)
_DlmRowStatus_Type=RowStatus
_DlmRowStatus_Object=MibTableColumn
dlmRowStatus=_DlmRowStatus_Object((1,3,6,1,4,1,21296,2,2,2,1,4,1,1,8),_DlmRowStatus_Type())
dlmRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dlmRowStatus.setStatus(_A)
_DlmOpticsFirmwareVer_Type=DisplayString
_DlmOpticsFirmwareVer_Object=MibTableColumn
dlmOpticsFirmwareVer=_DlmOpticsFirmwareVer_Object((1,3,6,1,4,1,21296,2,2,2,1,4,1,1,9),_DlmOpticsFirmwareVer_Type())
dlmOpticsFirmwareVer.setMaxAccess(_D)
if mibBuilder.loadTexts:dlmOpticsFirmwareVer.setStatus(_A)
_DlmConformance_ObjectIdentity=ObjectIdentity
dlmConformance=_DlmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,4,3))
_DlmCompliances_ObjectIdentity=ObjectIdentity
dlmCompliances=_DlmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,4,3,1))
_DlmGroups_ObjectIdentity=ObjectIdentity
dlmGroups=_DlmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,4,3,2))
dlmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,1,4,3,2,1))
dlmGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:dlmGroup.setStatus(_A)
dlmCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,1,4,3,1,1))
dlmCompliance.setObjects((_B,_Q))
if mibBuilder.loadTexts:dlmCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'dlmMIB':dlmMIB,'dlmTable':dlmTable,'dlmEntry':dlmEntry,_I:dlmMoId,_L:dlmProvEqptType,_K:dlmPicDspVer,_J:dlmOperatingMode,_H:dlmAvailableTunableOcgNumbers,_M:dlmProvisionedOcgNumber,_N:dlmInstalledOcgNumber,_O:dlmRowStatus,_P:dlmOpticsFirmwareVer,'dlmConformance':dlmConformance,'dlmCompliances':dlmCompliances,'dlmCompliance':dlmCompliance,'dlmGroups':dlmGroups,_Q:dlmGroup})