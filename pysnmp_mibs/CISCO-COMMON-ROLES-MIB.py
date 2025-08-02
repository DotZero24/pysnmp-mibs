_e='ccrmConfigurationExtGroup'
_d='ccrmConfigurationGroup'
_c='commonRoleRuleRowStatus'
_b='commonRoleRuleOperPermitted'
_a='commonRoleRuleOperation'
_Z='commonRoleRuleFeatureName'
_Y='commonRoleRowStatus'
_X='commonRoleScope2'
_W='commonRoleScope1'
_V='commonRoleScopeRestriction'
_U='commonRoleDescription'
_T='commonRoleFeatureOperation'
_S='commonRoleFeatureName'
_R='commonRoleRuleIndex'
_Q='commonRoleAccessMethod'
_P='commonRoleFeatureIndex'
_O='config'
_N='TruthValue'
_M='commonRoleMaxRulesPerRole'
_L='commonRoleMaxRoles'
_K='commonRoleSupportedOperation'
_J='commonRoleName'
_I='Integer32'
_H='OctetString'
_G='not-accessible'
_F='read-only'
_E='Unsigned32'
_D='SnmpAdminString'
_C='read-create'
_B='CISCO-COMMON-ROLES-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_D)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_N)
ciscoCommonRolesMIB=ModuleIdentity((1,3,6,1,4,1,9,9,361))
if mibBuilder.loadTexts:ciscoCommonRolesMIB.setRevisions(('2008-02-15 00:00','2003-09-15 00:00','2003-06-30 00:00'))
class CommonRoleOperation(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('clear',1),(_O,2),('debug',3),('show',4),('exec',5)))
_CiscoCommonRolesNotifications_ObjectIdentity=ObjectIdentity
ciscoCommonRolesNotifications=_CiscoCommonRolesNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,361,0))
_CiscoCommonRolesMIBObjects_ObjectIdentity=ObjectIdentity
ciscoCommonRolesMIBObjects=_CiscoCommonRolesMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,361,1))
_CcrInfo_ObjectIdentity=ObjectIdentity
ccrInfo=_CcrInfo_ObjectIdentity((1,3,6,1,4,1,9,9,361,1,1))
_CommonRoleFeatureTable_Object=MibTable
commonRoleFeatureTable=_CommonRoleFeatureTable_Object((1,3,6,1,4,1,9,9,361,1,1,1))
if mibBuilder.loadTexts:commonRoleFeatureTable.setStatus(_A)
_CommonRoleFeatureEntry_Object=MibTableRow
commonRoleFeatureEntry=_CommonRoleFeatureEntry_Object((1,3,6,1,4,1,9,9,361,1,1,1,1))
commonRoleFeatureEntry.setIndexNames((0,_B,_P))
if mibBuilder.loadTexts:commonRoleFeatureEntry.setStatus(_A)
class _CommonRoleFeatureIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CommonRoleFeatureIndex_Type.__name__=_E
_CommonRoleFeatureIndex_Object=MibTableColumn
commonRoleFeatureIndex=_CommonRoleFeatureIndex_Object((1,3,6,1,4,1,9,9,361,1,1,1,1,1),_CommonRoleFeatureIndex_Type())
commonRoleFeatureIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:commonRoleFeatureIndex.setStatus(_A)
class _CommonRoleFeatureName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CommonRoleFeatureName_Type.__name__=_D
_CommonRoleFeatureName_Object=MibTableColumn
commonRoleFeatureName=_CommonRoleFeatureName_Object((1,3,6,1,4,1,9,9,361,1,1,1,1,2),_CommonRoleFeatureName_Type())
commonRoleFeatureName.setMaxAccess(_F)
if mibBuilder.loadTexts:commonRoleFeatureName.setStatus(_A)
_CommonRoleFeatureOperation_Type=CommonRoleOperation
_CommonRoleFeatureOperation_Object=MibTableColumn
commonRoleFeatureOperation=_CommonRoleFeatureOperation_Object((1,3,6,1,4,1,9,9,361,1,1,1,1,3),_CommonRoleFeatureOperation_Type())
commonRoleFeatureOperation.setMaxAccess(_F)
if mibBuilder.loadTexts:commonRoleFeatureOperation.setStatus(_A)
_CommonRoleSupportedOperTable_Object=MibTable
commonRoleSupportedOperTable=_CommonRoleSupportedOperTable_Object((1,3,6,1,4,1,9,9,361,1,1,2))
if mibBuilder.loadTexts:commonRoleSupportedOperTable.setStatus(_A)
_CommonRoleSupportedOperEntry_Object=MibTableRow
commonRoleSupportedOperEntry=_CommonRoleSupportedOperEntry_Object((1,3,6,1,4,1,9,9,361,1,1,2,1))
commonRoleSupportedOperEntry.setIndexNames((0,_B,_Q))
if mibBuilder.loadTexts:commonRoleSupportedOperEntry.setStatus(_A)
class _CommonRoleAccessMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('cli',1),('snmp',2)))
_CommonRoleAccessMethod_Type.__name__=_I
_CommonRoleAccessMethod_Object=MibTableColumn
commonRoleAccessMethod=_CommonRoleAccessMethod_Object((1,3,6,1,4,1,9,9,361,1,1,2,1,1),_CommonRoleAccessMethod_Type())
commonRoleAccessMethod.setMaxAccess(_G)
if mibBuilder.loadTexts:commonRoleAccessMethod.setStatus(_A)
class _CommonRoleSupportedOperation_Type(Bits):namedValues=NamedValues(*(('clear',0),(_O,1),('debug',2),('show',3),('exec',4),('read',5),('readWrite',6)))
_CommonRoleSupportedOperation_Type.__name__='Bits'
_CommonRoleSupportedOperation_Object=MibTableColumn
commonRoleSupportedOperation=_CommonRoleSupportedOperation_Object((1,3,6,1,4,1,9,9,361,1,1,2,1,2),_CommonRoleSupportedOperation_Type())
commonRoleSupportedOperation.setMaxAccess(_F)
if mibBuilder.loadTexts:commonRoleSupportedOperation.setStatus(_A)
_CcrRoleConfig_ObjectIdentity=ObjectIdentity
ccrRoleConfig=_CcrRoleConfig_ObjectIdentity((1,3,6,1,4,1,9,9,361,1,2))
class _CommonRoleMaxRoles_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CommonRoleMaxRoles_Type.__name__=_E
_CommonRoleMaxRoles_Object=MibScalar
commonRoleMaxRoles=_CommonRoleMaxRoles_Object((1,3,6,1,4,1,9,9,361,1,2,1),_CommonRoleMaxRoles_Type())
commonRoleMaxRoles.setMaxAccess(_F)
if mibBuilder.loadTexts:commonRoleMaxRoles.setStatus(_A)
_CommonRoleTable_Object=MibTable
commonRoleTable=_CommonRoleTable_Object((1,3,6,1,4,1,9,9,361,1,2,2))
if mibBuilder.loadTexts:commonRoleTable.setStatus(_A)
_CommonRoleEntry_Object=MibTableRow
commonRoleEntry=_CommonRoleEntry_Object((1,3,6,1,4,1,9,9,361,1,2,2,1))
commonRoleEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:commonRoleEntry.setStatus(_A)
class _CommonRoleName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_CommonRoleName_Type.__name__=_D
_CommonRoleName_Object=MibTableColumn
commonRoleName=_CommonRoleName_Object((1,3,6,1,4,1,9,9,361,1,2,2,1,1),_CommonRoleName_Type())
commonRoleName.setMaxAccess(_G)
if mibBuilder.loadTexts:commonRoleName.setStatus(_A)
class _CommonRoleDescription_Type(SnmpAdminString):defaultHexValue='';subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CommonRoleDescription_Type.__name__=_D
_CommonRoleDescription_Object=MibTableColumn
commonRoleDescription=_CommonRoleDescription_Object((1,3,6,1,4,1,9,9,361,1,2,2,1,2),_CommonRoleDescription_Type())
commonRoleDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:commonRoleDescription.setStatus(_A)
class _CommonRoleScopeRestriction_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('none',1),('vsan',2)))
_CommonRoleScopeRestriction_Type.__name__=_I
_CommonRoleScopeRestriction_Object=MibTableColumn
commonRoleScopeRestriction=_CommonRoleScopeRestriction_Object((1,3,6,1,4,1,9,9,361,1,2,2,1,3),_CommonRoleScopeRestriction_Type())
commonRoleScopeRestriction.setMaxAccess(_C)
if mibBuilder.loadTexts:commonRoleScopeRestriction.setStatus(_A)
class _CommonRoleScope1_Type(OctetString):defaultHexValue=''
_CommonRoleScope1_Type.__name__=_H
_CommonRoleScope1_Object=MibTableColumn
commonRoleScope1=_CommonRoleScope1_Object((1,3,6,1,4,1,9,9,361,1,2,2,1,4),_CommonRoleScope1_Type())
commonRoleScope1.setMaxAccess(_C)
if mibBuilder.loadTexts:commonRoleScope1.setStatus(_A)
class _CommonRoleScope2_Type(OctetString):defaultHexValue=''
_CommonRoleScope2_Type.__name__=_H
_CommonRoleScope2_Object=MibTableColumn
commonRoleScope2=_CommonRoleScope2_Object((1,3,6,1,4,1,9,9,361,1,2,2,1,5),_CommonRoleScope2_Type())
commonRoleScope2.setMaxAccess(_C)
if mibBuilder.loadTexts:commonRoleScope2.setStatus(_A)
_CommonRoleRowStatus_Type=RowStatus
_CommonRoleRowStatus_Object=MibTableColumn
commonRoleRowStatus=_CommonRoleRowStatus_Object((1,3,6,1,4,1,9,9,361,1,2,2,1,6),_CommonRoleRowStatus_Type())
commonRoleRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:commonRoleRowStatus.setStatus(_A)
_CcrRuleConfig_ObjectIdentity=ObjectIdentity
ccrRuleConfig=_CcrRuleConfig_ObjectIdentity((1,3,6,1,4,1,9,9,361,1,3))
class _CommonRoleMaxRulesPerRole_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CommonRoleMaxRulesPerRole_Type.__name__=_E
_CommonRoleMaxRulesPerRole_Object=MibScalar
commonRoleMaxRulesPerRole=_CommonRoleMaxRulesPerRole_Object((1,3,6,1,4,1,9,9,361,1,3,1),_CommonRoleMaxRulesPerRole_Type())
commonRoleMaxRulesPerRole.setMaxAccess(_F)
if mibBuilder.loadTexts:commonRoleMaxRulesPerRole.setStatus(_A)
_CommonRoleRuleTable_Object=MibTable
commonRoleRuleTable=_CommonRoleRuleTable_Object((1,3,6,1,4,1,9,9,361,1,3,2))
if mibBuilder.loadTexts:commonRoleRuleTable.setStatus(_A)
_CommonRoleRuleEntry_Object=MibTableRow
commonRoleRuleEntry=_CommonRoleRuleEntry_Object((1,3,6,1,4,1,9,9,361,1,3,2,1))
commonRoleRuleEntry.setIndexNames((0,_B,_J),(0,_B,_R))
if mibBuilder.loadTexts:commonRoleRuleEntry.setStatus(_A)
class _CommonRoleRuleIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CommonRoleRuleIndex_Type.__name__=_E
_CommonRoleRuleIndex_Object=MibTableColumn
commonRoleRuleIndex=_CommonRoleRuleIndex_Object((1,3,6,1,4,1,9,9,361,1,3,2,1,1),_CommonRoleRuleIndex_Type())
commonRoleRuleIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:commonRoleRuleIndex.setStatus(_A)
class _CommonRoleRuleFeatureName_Type(SnmpAdminString):defaultHexValue='';subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CommonRoleRuleFeatureName_Type.__name__=_D
_CommonRoleRuleFeatureName_Object=MibTableColumn
commonRoleRuleFeatureName=_CommonRoleRuleFeatureName_Object((1,3,6,1,4,1,9,9,361,1,3,2,1,2),_CommonRoleRuleFeatureName_Type())
commonRoleRuleFeatureName.setMaxAccess(_C)
if mibBuilder.loadTexts:commonRoleRuleFeatureName.setStatus(_A)
_CommonRoleRuleOperation_Type=CommonRoleOperation
_CommonRoleRuleOperation_Object=MibTableColumn
commonRoleRuleOperation=_CommonRoleRuleOperation_Object((1,3,6,1,4,1,9,9,361,1,3,2,1,3),_CommonRoleRuleOperation_Type())
commonRoleRuleOperation.setMaxAccess(_C)
if mibBuilder.loadTexts:commonRoleRuleOperation.setStatus(_A)
class _CommonRoleRuleOperPermitted_Type(TruthValue):defaultValue=1
_CommonRoleRuleOperPermitted_Type.__name__=_N
_CommonRoleRuleOperPermitted_Object=MibTableColumn
commonRoleRuleOperPermitted=_CommonRoleRuleOperPermitted_Object((1,3,6,1,4,1,9,9,361,1,3,2,1,4),_CommonRoleRuleOperPermitted_Type())
commonRoleRuleOperPermitted.setMaxAccess(_C)
if mibBuilder.loadTexts:commonRoleRuleOperPermitted.setStatus(_A)
_CommonRoleRuleRowStatus_Type=RowStatus
_CommonRoleRuleRowStatus_Object=MibTableColumn
commonRoleRuleRowStatus=_CommonRoleRuleRowStatus_Object((1,3,6,1,4,1,9,9,361,1,3,2,1,5),_CommonRoleRuleRowStatus_Type())
commonRoleRuleRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:commonRoleRuleRowStatus.setStatus(_A)
_CiscoCommonRolesMIBConformance_ObjectIdentity=ObjectIdentity
ciscoCommonRolesMIBConformance=_CiscoCommonRolesMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,361,2))
_CiscoCommonRolesMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoCommonRolesMIBCompliances=_CiscoCommonRolesMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,361,2,1))
_CiscoCommonRolesMIBGroups_ObjectIdentity=ObjectIdentity
ciscoCommonRolesMIBGroups=_CiscoCommonRolesMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,361,2,2))
ccrmConfigurationGroup=ObjectGroup((1,3,6,1,4,1,9,9,361,2,2,1))
ccrmConfigurationGroup.setObjects(*((_B,_S),(_B,_T),(_B,_K),(_B,_L),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_M),(_B,_Z),(_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:ccrmConfigurationGroup.setStatus(_A)
ccrmConfigurationExtGroup=ObjectGroup((1,3,6,1,4,1,9,9,361,2,2,2))
ccrmConfigurationExtGroup.setObjects(*((_B,_L),(_B,_K),(_B,_M)))
if mibBuilder.loadTexts:ccrmConfigurationExtGroup.setStatus(_A)
ciscoCommonRolesMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,361,2,1,1))
ciscoCommonRolesMIBCompliance.setObjects((_B,_d))
if mibBuilder.loadTexts:ciscoCommonRolesMIBCompliance.setStatus(_A)
ciscoCommonRolesExtMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,361,2,1,2))
ciscoCommonRolesExtMIBCompliance.setObjects((_B,_e))
if mibBuilder.loadTexts:ciscoCommonRolesExtMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CommonRoleOperation':CommonRoleOperation,'ciscoCommonRolesMIB':ciscoCommonRolesMIB,'ciscoCommonRolesNotifications':ciscoCommonRolesNotifications,'ciscoCommonRolesMIBObjects':ciscoCommonRolesMIBObjects,'ccrInfo':ccrInfo,'commonRoleFeatureTable':commonRoleFeatureTable,'commonRoleFeatureEntry':commonRoleFeatureEntry,_P:commonRoleFeatureIndex,_S:commonRoleFeatureName,_T:commonRoleFeatureOperation,'commonRoleSupportedOperTable':commonRoleSupportedOperTable,'commonRoleSupportedOperEntry':commonRoleSupportedOperEntry,_Q:commonRoleAccessMethod,_K:commonRoleSupportedOperation,'ccrRoleConfig':ccrRoleConfig,_L:commonRoleMaxRoles,'commonRoleTable':commonRoleTable,'commonRoleEntry':commonRoleEntry,_J:commonRoleName,_U:commonRoleDescription,_V:commonRoleScopeRestriction,_W:commonRoleScope1,_X:commonRoleScope2,_Y:commonRoleRowStatus,'ccrRuleConfig':ccrRuleConfig,_M:commonRoleMaxRulesPerRole,'commonRoleRuleTable':commonRoleRuleTable,'commonRoleRuleEntry':commonRoleRuleEntry,_R:commonRoleRuleIndex,_Z:commonRoleRuleFeatureName,_a:commonRoleRuleOperation,_b:commonRoleRuleOperPermitted,_c:commonRoleRuleRowStatus,'ciscoCommonRolesMIBConformance':ciscoCommonRolesMIBConformance,'ciscoCommonRolesMIBCompliances':ciscoCommonRolesMIBCompliances,'ciscoCommonRolesMIBCompliance':ciscoCommonRolesMIBCompliance,'ciscoCommonRolesExtMIBCompliance':ciscoCommonRolesExtMIBCompliance,'ciscoCommonRolesMIBGroups':ciscoCommonRolesMIBGroups,_d:ccrmConfigurationGroup,_e:ccrmConfigurationExtGroup})