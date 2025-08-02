_K='cilConfMIBGroupRev1'
_J='cilConfMIBGroup'
_I='cilTargetModuleFramingType'
_H='deprecated'
_G='cilSourceInterface'
_F='Integer32'
_E='cilRowStatus'
_D='cilTargetModuleInterface'
_C='read-create'
_B='current'
_A='CISCO-IF-LINK-CONFIG-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoLocationSpecifier,=mibBuilder.importSymbols('CISCO-TC','CiscoLocationSpecifier')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
ciscoIfLinkConfigMIB=ModuleIdentity((1,3,6,1,4,1,9,9,175))
if mibBuilder.loadTexts:ciscoIfLinkConfigMIB.setRevisions(('2001-10-05 00:00','2000-09-14 00:00'))
_CilConfigMIBObjects_ObjectIdentity=ObjectIdentity
cilConfigMIBObjects=_CilConfigMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,175,1))
_CilConfig_ObjectIdentity=ObjectIdentity
cilConfig=_CilConfig_ObjectIdentity((1,3,6,1,4,1,9,9,175,1,1))
_CilConfTable_Object=MibTable
cilConfTable=_CilConfTable_Object((1,3,6,1,4,1,9,9,175,1,1,1))
if mibBuilder.loadTexts:cilConfTable.setStatus(_B)
_CilConfEntry_Object=MibTableRow
cilConfEntry=_CilConfEntry_Object((1,3,6,1,4,1,9,9,175,1,1,1,1))
cilConfEntry.setIndexNames((0,_A,_G))
if mibBuilder.loadTexts:cilConfEntry.setStatus(_B)
_CilSourceInterface_Type=InterfaceIndex
_CilSourceInterface_Object=MibTableColumn
cilSourceInterface=_CilSourceInterface_Object((1,3,6,1,4,1,9,9,175,1,1,1,1,1),_CilSourceInterface_Type())
cilSourceInterface.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cilSourceInterface.setStatus(_B)
_CilTargetModuleInterface_Type=CiscoLocationSpecifier
_CilTargetModuleInterface_Object=MibTableColumn
cilTargetModuleInterface=_CilTargetModuleInterface_Object((1,3,6,1,4,1,9,9,175,1,1,1,1,2),_CilTargetModuleInterface_Type())
cilTargetModuleInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:cilTargetModuleInterface.setStatus(_B)
_CilRowStatus_Type=RowStatus
_CilRowStatus_Object=MibTableColumn
cilRowStatus=_CilRowStatus_Object((1,3,6,1,4,1,9,9,175,1,1,1,1,3),_CilRowStatus_Type())
cilRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cilRowStatus.setStatus(_B)
class _CilTargetModuleFramingType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notApplicable',1),('dsx1D4',2),('dsx1ESF',3)))
_CilTargetModuleFramingType_Type.__name__=_F
_CilTargetModuleFramingType_Object=MibTableColumn
cilTargetModuleFramingType=_CilTargetModuleFramingType_Object((1,3,6,1,4,1,9,9,175,1,1,1,1,4),_CilTargetModuleFramingType_Type())
cilTargetModuleFramingType.setMaxAccess(_C)
if mibBuilder.loadTexts:cilTargetModuleFramingType.setStatus(_B)
_CilConfigMIBConformance_ObjectIdentity=ObjectIdentity
cilConfigMIBConformance=_CilConfigMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,175,3))
_CilConfigMIBCompliances_ObjectIdentity=ObjectIdentity
cilConfigMIBCompliances=_CilConfigMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,175,3,1))
_CilConfigMIBGroups_ObjectIdentity=ObjectIdentity
cilConfigMIBGroups=_CilConfigMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,175,3,2))
cilConfMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,175,3,2,1))
cilConfMIBGroup.setObjects(*((_A,_D),(_A,_E)))
if mibBuilder.loadTexts:cilConfMIBGroup.setStatus(_H)
cilConfMIBGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,175,3,2,2))
cilConfMIBGroupRev1.setObjects(*((_A,_D),(_A,_E),(_A,_I)))
if mibBuilder.loadTexts:cilConfMIBGroupRev1.setStatus(_B)
cilConfigMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,175,3,1,1))
cilConfigMIBCompliance.setObjects((_A,_J))
if mibBuilder.loadTexts:cilConfigMIBCompliance.setStatus(_H)
cilConfigMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,175,3,1,2))
cilConfigMIBComplianceRev1.setObjects((_A,_K))
if mibBuilder.loadTexts:cilConfigMIBComplianceRev1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoIfLinkConfigMIB':ciscoIfLinkConfigMIB,'cilConfigMIBObjects':cilConfigMIBObjects,'cilConfig':cilConfig,'cilConfTable':cilConfTable,'cilConfEntry':cilConfEntry,_G:cilSourceInterface,_D:cilTargetModuleInterface,_E:cilRowStatus,_I:cilTargetModuleFramingType,'cilConfigMIBConformance':cilConfigMIBConformance,'cilConfigMIBCompliances':cilConfigMIBCompliances,'cilConfigMIBCompliance':cilConfigMIBCompliance,'cilConfigMIBComplianceRev1':cilConfigMIBComplianceRev1,'cilConfigMIBGroups':cilConfigMIBGroups,_J:cilConfMIBGroup,_K:cilConfMIBGroupRev1})