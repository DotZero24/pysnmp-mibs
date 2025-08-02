_g='ccreConfigurationGroup'
_f='ccreRuleRowStatus'
_e='ccreRuleOperationPermitted'
_d='ccreRuleOperation'
_c='ccreRuleFeatureElementType'
_b='ccreRuleFeatureElementName'
_a='ccreRoleScopeRowStatus'
_Z='ccreRoleScopeValue'
_Y='ccreRoleScopeRestriction'
_X='ccreRoleRowStatus'
_W='ccreRoleResourceAccess'
_V='ccreRoleDescription'
_U='ccreFeatureRowStatus'
_T='ccreFeatureElementType'
_S='ccreFeatureElementName'
_R='ccreRuleNumber'
_Q='ccreRoleScopeIndex'
_P='feature'
_O='command'
_N='ccreFeatureElementIndex'
_M='ccreFeatureName'
_L='interface'
_K='TruthValue'
_J='ccrmConfigurationExtGroup'
_I='CISCO-COMMON-ROLES-MIB'
_H='ccreRoleName'
_G='Unsigned32'
_F='not-accessible'
_E='Integer32'
_D='SnmpAdminString'
_C='read-create'
_B='CISCO-COMMON-ROLES-EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ccrmConfigurationExtGroup,=mibBuilder.importSymbols(_I,_J)
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_D)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_K)
ciscoCommonRolesExtMIB=ModuleIdentity((1,3,6,1,4,1,9,9,651))
if mibBuilder.loadTexts:ciscoCommonRolesExtMIB.setRevisions(('2008-02-15 00:00',))
class CcreOperation(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('read',1),('readWrite',2)))
class CcreResourceAccess(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('vsan',0),('vlan',1),(_L,2)))
_CiscoCommonRolesExtNotifications_ObjectIdentity=ObjectIdentity
ciscoCommonRolesExtNotifications=_CiscoCommonRolesExtNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,651,0))
_CiscoCommonRolesExtMIBObjects_ObjectIdentity=ObjectIdentity
ciscoCommonRolesExtMIBObjects=_CiscoCommonRolesExtMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,651,1))
_CcreInfo_ObjectIdentity=ObjectIdentity
ccreInfo=_CcreInfo_ObjectIdentity((1,3,6,1,4,1,9,9,651,1,1))
_CcreFeatureElementTable_Object=MibTable
ccreFeatureElementTable=_CcreFeatureElementTable_Object((1,3,6,1,4,1,9,9,651,1,1,1))
if mibBuilder.loadTexts:ccreFeatureElementTable.setStatus(_A)
_CcreFeatureElementEntry_Object=MibTableRow
ccreFeatureElementEntry=_CcreFeatureElementEntry_Object((1,3,6,1,4,1,9,9,651,1,1,1,1))
ccreFeatureElementEntry.setIndexNames((0,_B,_M),(0,_B,_N))
if mibBuilder.loadTexts:ccreFeatureElementEntry.setStatus(_A)
class _CcreFeatureName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CcreFeatureName_Type.__name__=_D
_CcreFeatureName_Object=MibTableColumn
ccreFeatureName=_CcreFeatureName_Object((1,3,6,1,4,1,9,9,651,1,1,1,1,1),_CcreFeatureName_Type())
ccreFeatureName.setMaxAccess(_F)
if mibBuilder.loadTexts:ccreFeatureName.setStatus(_A)
class _CcreFeatureElementIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CcreFeatureElementIndex_Type.__name__=_G
_CcreFeatureElementIndex_Object=MibTableColumn
ccreFeatureElementIndex=_CcreFeatureElementIndex_Object((1,3,6,1,4,1,9,9,651,1,1,1,1,2),_CcreFeatureElementIndex_Type())
ccreFeatureElementIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:ccreFeatureElementIndex.setStatus(_A)
class _CcreFeatureElementName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CcreFeatureElementName_Type.__name__=_D
_CcreFeatureElementName_Object=MibTableColumn
ccreFeatureElementName=_CcreFeatureElementName_Object((1,3,6,1,4,1,9,9,651,1,1,1,1,3),_CcreFeatureElementName_Type())
ccreFeatureElementName.setMaxAccess(_C)
if mibBuilder.loadTexts:ccreFeatureElementName.setStatus(_A)
class _CcreFeatureElementType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_O,1),(_P,2),('none',3)))
_CcreFeatureElementType_Type.__name__=_E
_CcreFeatureElementType_Object=MibTableColumn
ccreFeatureElementType=_CcreFeatureElementType_Object((1,3,6,1,4,1,9,9,651,1,1,1,1,4),_CcreFeatureElementType_Type())
ccreFeatureElementType.setMaxAccess(_C)
if mibBuilder.loadTexts:ccreFeatureElementType.setStatus(_A)
_CcreFeatureRowStatus_Type=RowStatus
_CcreFeatureRowStatus_Object=MibTableColumn
ccreFeatureRowStatus=_CcreFeatureRowStatus_Object((1,3,6,1,4,1,9,9,651,1,1,1,1,5),_CcreFeatureRowStatus_Type())
ccreFeatureRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ccreFeatureRowStatus.setStatus(_A)
_CcreRoleConfig_ObjectIdentity=ObjectIdentity
ccreRoleConfig=_CcreRoleConfig_ObjectIdentity((1,3,6,1,4,1,9,9,651,1,2))
_CcreRoleTable_Object=MibTable
ccreRoleTable=_CcreRoleTable_Object((1,3,6,1,4,1,9,9,651,1,2,2))
if mibBuilder.loadTexts:ccreRoleTable.setStatus(_A)
_CcreRoleEntry_Object=MibTableRow
ccreRoleEntry=_CcreRoleEntry_Object((1,3,6,1,4,1,9,9,651,1,2,2,1))
ccreRoleEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:ccreRoleEntry.setStatus(_A)
class _CcreRoleName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_CcreRoleName_Type.__name__=_D
_CcreRoleName_Object=MibTableColumn
ccreRoleName=_CcreRoleName_Object((1,3,6,1,4,1,9,9,651,1,2,2,1,1),_CcreRoleName_Type())
ccreRoleName.setMaxAccess(_F)
if mibBuilder.loadTexts:ccreRoleName.setStatus(_A)
class _CcreRoleDescription_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CcreRoleDescription_Type.__name__=_D
_CcreRoleDescription_Object=MibTableColumn
ccreRoleDescription=_CcreRoleDescription_Object((1,3,6,1,4,1,9,9,651,1,2,2,1,2),_CcreRoleDescription_Type())
ccreRoleDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:ccreRoleDescription.setStatus(_A)
_CcreRoleResourceAccess_Type=CcreResourceAccess
_CcreRoleResourceAccess_Object=MibTableColumn
ccreRoleResourceAccess=_CcreRoleResourceAccess_Object((1,3,6,1,4,1,9,9,651,1,2,2,1,3),_CcreRoleResourceAccess_Type())
ccreRoleResourceAccess.setMaxAccess(_C)
if mibBuilder.loadTexts:ccreRoleResourceAccess.setStatus(_A)
_CcreRoleRowStatus_Type=RowStatus
_CcreRoleRowStatus_Object=MibTableColumn
ccreRoleRowStatus=_CcreRoleRowStatus_Object((1,3,6,1,4,1,9,9,651,1,2,2,1,4),_CcreRoleRowStatus_Type())
ccreRoleRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ccreRoleRowStatus.setStatus(_A)
_CcreRoleScopeTable_Object=MibTable
ccreRoleScopeTable=_CcreRoleScopeTable_Object((1,3,6,1,4,1,9,9,651,1,2,3))
if mibBuilder.loadTexts:ccreRoleScopeTable.setStatus(_A)
_CcreRoleScopeEntry_Object=MibTableRow
ccreRoleScopeEntry=_CcreRoleScopeEntry_Object((1,3,6,1,4,1,9,9,651,1,2,3,1))
ccreRoleScopeEntry.setIndexNames((0,_B,_H),(0,_B,_Q))
if mibBuilder.loadTexts:ccreRoleScopeEntry.setStatus(_A)
class _CcreRoleScopeIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CcreRoleScopeIndex_Type.__name__=_G
_CcreRoleScopeIndex_Object=MibTableColumn
ccreRoleScopeIndex=_CcreRoleScopeIndex_Object((1,3,6,1,4,1,9,9,651,1,2,3,1,1),_CcreRoleScopeIndex_Type())
ccreRoleScopeIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:ccreRoleScopeIndex.setStatus(_A)
class _CcreRoleScopeRestriction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('vsan',1),('vlan',2),(_L,3)))
_CcreRoleScopeRestriction_Type.__name__=_E
_CcreRoleScopeRestriction_Object=MibTableColumn
ccreRoleScopeRestriction=_CcreRoleScopeRestriction_Object((1,3,6,1,4,1,9,9,651,1,2,3,1,2),_CcreRoleScopeRestriction_Type())
ccreRoleScopeRestriction.setMaxAccess(_C)
if mibBuilder.loadTexts:ccreRoleScopeRestriction.setStatus(_A)
class _CcreRoleScopeValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CcreRoleScopeValue_Type.__name__=_E
_CcreRoleScopeValue_Object=MibTableColumn
ccreRoleScopeValue=_CcreRoleScopeValue_Object((1,3,6,1,4,1,9,9,651,1,2,3,1,3),_CcreRoleScopeValue_Type())
ccreRoleScopeValue.setMaxAccess(_C)
if mibBuilder.loadTexts:ccreRoleScopeValue.setStatus(_A)
_CcreRoleScopeRowStatus_Type=RowStatus
_CcreRoleScopeRowStatus_Object=MibTableColumn
ccreRoleScopeRowStatus=_CcreRoleScopeRowStatus_Object((1,3,6,1,4,1,9,9,651,1,2,3,1,4),_CcreRoleScopeRowStatus_Type())
ccreRoleScopeRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ccreRoleScopeRowStatus.setStatus(_A)
_CcreRuleConfig_ObjectIdentity=ObjectIdentity
ccreRuleConfig=_CcreRuleConfig_ObjectIdentity((1,3,6,1,4,1,9,9,651,1,3))
_CcreRuleTable_Object=MibTable
ccreRuleTable=_CcreRuleTable_Object((1,3,6,1,4,1,9,9,651,1,3,2))
if mibBuilder.loadTexts:ccreRuleTable.setStatus(_A)
_CcreRuleEntry_Object=MibTableRow
ccreRuleEntry=_CcreRuleEntry_Object((1,3,6,1,4,1,9,9,651,1,3,2,1))
ccreRuleEntry.setIndexNames((0,_B,_H),(0,_B,_R))
if mibBuilder.loadTexts:ccreRuleEntry.setStatus(_A)
class _CcreRuleNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_CcreRuleNumber_Type.__name__=_G
_CcreRuleNumber_Object=MibTableColumn
ccreRuleNumber=_CcreRuleNumber_Object((1,3,6,1,4,1,9,9,651,1,3,2,1,1),_CcreRuleNumber_Type())
ccreRuleNumber.setMaxAccess(_F)
if mibBuilder.loadTexts:ccreRuleNumber.setStatus(_A)
class _CcreRuleFeatureElementName_Type(SnmpAdminString):defaultHexValue='';subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CcreRuleFeatureElementName_Type.__name__=_D
_CcreRuleFeatureElementName_Object=MibTableColumn
ccreRuleFeatureElementName=_CcreRuleFeatureElementName_Object((1,3,6,1,4,1,9,9,651,1,3,2,1,2),_CcreRuleFeatureElementName_Type())
ccreRuleFeatureElementName.setMaxAccess(_C)
if mibBuilder.loadTexts:ccreRuleFeatureElementName.setStatus(_A)
class _CcreRuleFeatureElementType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_O,1),(_P,2),('featureGroup',3),('all',4)))
_CcreRuleFeatureElementType_Type.__name__=_E
_CcreRuleFeatureElementType_Object=MibTableColumn
ccreRuleFeatureElementType=_CcreRuleFeatureElementType_Object((1,3,6,1,4,1,9,9,651,1,3,2,1,3),_CcreRuleFeatureElementType_Type())
ccreRuleFeatureElementType.setMaxAccess(_C)
if mibBuilder.loadTexts:ccreRuleFeatureElementType.setStatus(_A)
_CcreRuleOperation_Type=CcreOperation
_CcreRuleOperation_Object=MibTableColumn
ccreRuleOperation=_CcreRuleOperation_Object((1,3,6,1,4,1,9,9,651,1,3,2,1,4),_CcreRuleOperation_Type())
ccreRuleOperation.setMaxAccess(_C)
if mibBuilder.loadTexts:ccreRuleOperation.setStatus(_A)
class _CcreRuleOperationPermitted_Type(TruthValue):defaultValue=1
_CcreRuleOperationPermitted_Type.__name__=_K
_CcreRuleOperationPermitted_Object=MibTableColumn
ccreRuleOperationPermitted=_CcreRuleOperationPermitted_Object((1,3,6,1,4,1,9,9,651,1,3,2,1,5),_CcreRuleOperationPermitted_Type())
ccreRuleOperationPermitted.setMaxAccess(_C)
if mibBuilder.loadTexts:ccreRuleOperationPermitted.setStatus(_A)
_CcreRuleRowStatus_Type=RowStatus
_CcreRuleRowStatus_Object=MibTableColumn
ccreRuleRowStatus=_CcreRuleRowStatus_Object((1,3,6,1,4,1,9,9,651,1,3,2,1,6),_CcreRuleRowStatus_Type())
ccreRuleRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ccreRuleRowStatus.setStatus(_A)
_CiscoCommonRolesExtMIBConformance_ObjectIdentity=ObjectIdentity
ciscoCommonRolesExtMIBConformance=_CiscoCommonRolesExtMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,651,2))
_CcreMIBCompliances_ObjectIdentity=ObjectIdentity
ccreMIBCompliances=_CcreMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,651,2,1))
_CcreMIBGroups_ObjectIdentity=ObjectIdentity
ccreMIBGroups=_CcreMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,651,2,2))
ccreConfigurationGroup=ObjectGroup((1,3,6,1,4,1,9,9,651,2,2,1))
ccreConfigurationGroup.setObjects(*((_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f)))
if mibBuilder.loadTexts:ccreConfigurationGroup.setStatus(_A)
ccreMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,651,2,1,1))
ccreMIBCompliance.setObjects(*((_B,_g),(_I,_J)))
if mibBuilder.loadTexts:ccreMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CcreOperation':CcreOperation,'CcreResourceAccess':CcreResourceAccess,'ciscoCommonRolesExtMIB':ciscoCommonRolesExtMIB,'ciscoCommonRolesExtNotifications':ciscoCommonRolesExtNotifications,'ciscoCommonRolesExtMIBObjects':ciscoCommonRolesExtMIBObjects,'ccreInfo':ccreInfo,'ccreFeatureElementTable':ccreFeatureElementTable,'ccreFeatureElementEntry':ccreFeatureElementEntry,_M:ccreFeatureName,_N:ccreFeatureElementIndex,_S:ccreFeatureElementName,_T:ccreFeatureElementType,_U:ccreFeatureRowStatus,'ccreRoleConfig':ccreRoleConfig,'ccreRoleTable':ccreRoleTable,'ccreRoleEntry':ccreRoleEntry,_H:ccreRoleName,_V:ccreRoleDescription,_W:ccreRoleResourceAccess,_X:ccreRoleRowStatus,'ccreRoleScopeTable':ccreRoleScopeTable,'ccreRoleScopeEntry':ccreRoleScopeEntry,_Q:ccreRoleScopeIndex,_Y:ccreRoleScopeRestriction,_Z:ccreRoleScopeValue,_a:ccreRoleScopeRowStatus,'ccreRuleConfig':ccreRuleConfig,'ccreRuleTable':ccreRuleTable,'ccreRuleEntry':ccreRuleEntry,_R:ccreRuleNumber,_b:ccreRuleFeatureElementName,_c:ccreRuleFeatureElementType,_d:ccreRuleOperation,_e:ccreRuleOperationPermitted,_f:ccreRuleRowStatus,'ciscoCommonRolesExtMIBConformance':ciscoCommonRolesExtMIBConformance,'ccreMIBCompliances':ccreMIBCompliances,'ccreMIBCompliance':ccreMIBCompliance,'ccreMIBGroups':ccreMIBGroups,_g:ccreConfigurationGroup})