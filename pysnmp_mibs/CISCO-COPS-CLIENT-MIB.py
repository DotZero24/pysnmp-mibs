_g='ccopsRoleGroup'
_f='ccopsGlobalGroupRev2'
_e='ccopsGlobalGroup'
_d='ccopsRoleConfigSupported'
_c='deprecated'
_b='ccopsRoleName'
_a='CopsDomainName'
_Z='ccopsDomainClientType'
_Y='ccopsServerConfigName'
_X='ccopsServerConfigClientType'
_W='DisplayString'
_V='ifIndex'
_U='IF-MIB'
_T='ccopsIfRoleCombination'
_S='ccopsRoleStatus'
_R='ccopsMaxRoleCombination'
_Q='ccopsMaxRole'
_P='ccopsDomainName'
_O='ccopsTimeoutMax'
_N='ccopsTimeoutIncrement'
_M='ccopsInitialTimeout'
_L='ccopsServerConfigStatus'
_K='ccopsServerConfigPort'
_J='ccopsServerConfigPriority'
_I='ccopsServerMax'
_H='seconds'
_G='read-create'
_F='not-accessible'
_E='read-only'
_D='read-write'
_C='Unsigned32'
_B='current'
_A='CISCO-COPS-CLIENT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ifIndex,=mibBuilder.importSymbols(_U,_V)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_C,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_W,'PhysAddress','RowStatus','TextualConvention','TruthValue')
ciscoCopsClientMIB=ModuleIdentity((1,3,6,1,4,1,9,9,140))
if mibBuilder.loadTexts:ciscoCopsClientMIB.setRevisions(('2005-11-14 00:00','2000-06-11 00:00','1999-09-16 00:40'))
class CopsRole(TextualConvention,OctetString):status=_B;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
class CopsRoleCombination(TextualConvention,OctetString):status=_B;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
class CopsDomainName(TextualConvention,OctetString):status=_B;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
class CopsClientType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('rsvp',1),('provisioning',2)))
_CcopsMIBObjects_ObjectIdentity=ObjectIdentity
ccopsMIBObjects=_CcopsMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,140,1))
_CcopsGlobalObjects_ObjectIdentity=ObjectIdentity
ccopsGlobalObjects=_CcopsGlobalObjects_ObjectIdentity((1,3,6,1,4,1,9,9,140,1,1))
class _CcopsServerMax_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CcopsServerMax_Type.__name__=_C
_CcopsServerMax_Object=MibScalar
ccopsServerMax=_CcopsServerMax_Object((1,3,6,1,4,1,9,9,140,1,1,1),_CcopsServerMax_Type())
ccopsServerMax.setMaxAccess(_E)
if mibBuilder.loadTexts:ccopsServerMax.setStatus(_B)
if mibBuilder.loadTexts:ccopsServerMax.setUnits('servers')
_CcopsMaxRole_Type=Unsigned32
_CcopsMaxRole_Object=MibScalar
ccopsMaxRole=_CcopsMaxRole_Object((1,3,6,1,4,1,9,9,140,1,1,2),_CcopsMaxRole_Type())
ccopsMaxRole.setMaxAccess(_E)
if mibBuilder.loadTexts:ccopsMaxRole.setStatus(_B)
if mibBuilder.loadTexts:ccopsMaxRole.setUnits('roles')
_CcopsMaxRoleCombination_Type=Unsigned32
_CcopsMaxRoleCombination_Object=MibScalar
ccopsMaxRoleCombination=_CcopsMaxRoleCombination_Object((1,3,6,1,4,1,9,9,140,1,1,3),_CcopsMaxRoleCombination_Type())
ccopsMaxRoleCombination.setMaxAccess(_E)
if mibBuilder.loadTexts:ccopsMaxRoleCombination.setStatus(_B)
if mibBuilder.loadTexts:ccopsMaxRoleCombination.setUnits('role-combinations')
_CcopsServerConfigTable_Object=MibTable
ccopsServerConfigTable=_CcopsServerConfigTable_Object((1,3,6,1,4,1,9,9,140,1,1,4))
if mibBuilder.loadTexts:ccopsServerConfigTable.setStatus(_B)
_CcopsServerConfigEntry_Object=MibTableRow
ccopsServerConfigEntry=_CcopsServerConfigEntry_Object((1,3,6,1,4,1,9,9,140,1,1,4,1))
ccopsServerConfigEntry.setIndexNames((0,_A,_X),(1,_A,_Y))
if mibBuilder.loadTexts:ccopsServerConfigEntry.setStatus(_B)
_CcopsServerConfigClientType_Type=CopsClientType
_CcopsServerConfigClientType_Object=MibTableColumn
ccopsServerConfigClientType=_CcopsServerConfigClientType_Object((1,3,6,1,4,1,9,9,140,1,1,4,1,1),_CcopsServerConfigClientType_Type())
ccopsServerConfigClientType.setMaxAccess(_F)
if mibBuilder.loadTexts:ccopsServerConfigClientType.setStatus(_B)
class _CcopsServerConfigName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CcopsServerConfigName_Type.__name__=_W
_CcopsServerConfigName_Object=MibTableColumn
ccopsServerConfigName=_CcopsServerConfigName_Object((1,3,6,1,4,1,9,9,140,1,1,4,1,2),_CcopsServerConfigName_Type())
ccopsServerConfigName.setMaxAccess(_F)
if mibBuilder.loadTexts:ccopsServerConfigName.setStatus(_B)
class _CcopsServerConfigPriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CcopsServerConfigPriority_Type.__name__=_C
_CcopsServerConfigPriority_Object=MibTableColumn
ccopsServerConfigPriority=_CcopsServerConfigPriority_Object((1,3,6,1,4,1,9,9,140,1,1,4,1,3),_CcopsServerConfigPriority_Type())
ccopsServerConfigPriority.setMaxAccess(_G)
if mibBuilder.loadTexts:ccopsServerConfigPriority.setStatus(_B)
class _CcopsServerConfigPort_Type(Unsigned32):defaultValue=3288;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CcopsServerConfigPort_Type.__name__=_C
_CcopsServerConfigPort_Object=MibTableColumn
ccopsServerConfigPort=_CcopsServerConfigPort_Object((1,3,6,1,4,1,9,9,140,1,1,4,1,4),_CcopsServerConfigPort_Type())
ccopsServerConfigPort.setMaxAccess(_G)
if mibBuilder.loadTexts:ccopsServerConfigPort.setStatus(_B)
_CcopsServerConfigStatus_Type=RowStatus
_CcopsServerConfigStatus_Object=MibTableColumn
ccopsServerConfigStatus=_CcopsServerConfigStatus_Object((1,3,6,1,4,1,9,9,140,1,1,4,1,5),_CcopsServerConfigStatus_Type())
ccopsServerConfigStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:ccopsServerConfigStatus.setStatus(_B)
class _CcopsInitialTimeout_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CcopsInitialTimeout_Type.__name__=_C
_CcopsInitialTimeout_Object=MibScalar
ccopsInitialTimeout=_CcopsInitialTimeout_Object((1,3,6,1,4,1,9,9,140,1,1,5),_CcopsInitialTimeout_Type())
ccopsInitialTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:ccopsInitialTimeout.setStatus(_B)
if mibBuilder.loadTexts:ccopsInitialTimeout.setUnits(_H)
class _CcopsTimeoutIncrement_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CcopsTimeoutIncrement_Type.__name__=_C
_CcopsTimeoutIncrement_Object=MibScalar
ccopsTimeoutIncrement=_CcopsTimeoutIncrement_Object((1,3,6,1,4,1,9,9,140,1,1,6),_CcopsTimeoutIncrement_Type())
ccopsTimeoutIncrement.setMaxAccess(_D)
if mibBuilder.loadTexts:ccopsTimeoutIncrement.setStatus(_B)
if mibBuilder.loadTexts:ccopsTimeoutIncrement.setUnits(_H)
class _CcopsTimeoutMax_Type(Unsigned32):defaultValue=300;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CcopsTimeoutMax_Type.__name__=_C
_CcopsTimeoutMax_Object=MibScalar
ccopsTimeoutMax=_CcopsTimeoutMax_Object((1,3,6,1,4,1,9,9,140,1,1,7),_CcopsTimeoutMax_Type())
ccopsTimeoutMax.setMaxAccess(_D)
if mibBuilder.loadTexts:ccopsTimeoutMax.setStatus(_B)
if mibBuilder.loadTexts:ccopsTimeoutMax.setUnits(_H)
_CcopsDomainTable_Object=MibTable
ccopsDomainTable=_CcopsDomainTable_Object((1,3,6,1,4,1,9,9,140,1,1,8))
if mibBuilder.loadTexts:ccopsDomainTable.setStatus(_B)
_CcopsDomainEntry_Object=MibTableRow
ccopsDomainEntry=_CcopsDomainEntry_Object((1,3,6,1,4,1,9,9,140,1,1,8,1))
ccopsDomainEntry.setIndexNames((0,_A,_Z))
if mibBuilder.loadTexts:ccopsDomainEntry.setStatus(_B)
_CcopsDomainClientType_Type=CopsClientType
_CcopsDomainClientType_Object=MibTableColumn
ccopsDomainClientType=_CcopsDomainClientType_Object((1,3,6,1,4,1,9,9,140,1,1,8,1,1),_CcopsDomainClientType_Type())
ccopsDomainClientType.setMaxAccess(_F)
if mibBuilder.loadTexts:ccopsDomainClientType.setStatus(_B)
class _CcopsDomainName_Type(CopsDomainName):defaultHexValue=''
_CcopsDomainName_Type.__name__=_a
_CcopsDomainName_Object=MibTableColumn
ccopsDomainName=_CcopsDomainName_Object((1,3,6,1,4,1,9,9,140,1,1,8,1,2),_CcopsDomainName_Type())
ccopsDomainName.setMaxAccess(_D)
if mibBuilder.loadTexts:ccopsDomainName.setStatus(_B)
_CcopsRoleTable_Object=MibTable
ccopsRoleTable=_CcopsRoleTable_Object((1,3,6,1,4,1,9,9,140,1,1,9))
if mibBuilder.loadTexts:ccopsRoleTable.setStatus(_B)
_CcopsRoleEntry_Object=MibTableRow
ccopsRoleEntry=_CcopsRoleEntry_Object((1,3,6,1,4,1,9,9,140,1,1,9,1))
ccopsRoleEntry.setIndexNames((1,_A,_b))
if mibBuilder.loadTexts:ccopsRoleEntry.setStatus(_B)
_CcopsRoleName_Type=CopsRole
_CcopsRoleName_Object=MibTableColumn
ccopsRoleName=_CcopsRoleName_Object((1,3,6,1,4,1,9,9,140,1,1,9,1,1),_CcopsRoleName_Type())
ccopsRoleName.setMaxAccess(_F)
if mibBuilder.loadTexts:ccopsRoleName.setStatus(_B)
_CcopsRoleStatus_Type=RowStatus
_CcopsRoleStatus_Object=MibTableColumn
ccopsRoleStatus=_CcopsRoleStatus_Object((1,3,6,1,4,1,9,9,140,1,1,9,1,2),_CcopsRoleStatus_Type())
ccopsRoleStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:ccopsRoleStatus.setStatus(_B)
_CcopsIfTable_Object=MibTable
ccopsIfTable=_CcopsIfTable_Object((1,3,6,1,4,1,9,9,140,1,1,10))
if mibBuilder.loadTexts:ccopsIfTable.setStatus(_B)
_CcopsIfEntry_Object=MibTableRow
ccopsIfEntry=_CcopsIfEntry_Object((1,3,6,1,4,1,9,9,140,1,1,10,1))
ccopsIfEntry.setIndexNames((0,_U,_V))
if mibBuilder.loadTexts:ccopsIfEntry.setStatus(_B)
_CcopsIfRoleCombination_Type=CopsRoleCombination
_CcopsIfRoleCombination_Object=MibTableColumn
ccopsIfRoleCombination=_CcopsIfRoleCombination_Object((1,3,6,1,4,1,9,9,140,1,1,10,1,1),_CcopsIfRoleCombination_Type())
ccopsIfRoleCombination.setMaxAccess(_D)
if mibBuilder.loadTexts:ccopsIfRoleCombination.setStatus(_B)
_CcopsRoleConfigSupported_Type=TruthValue
_CcopsRoleConfigSupported_Object=MibScalar
ccopsRoleConfigSupported=_CcopsRoleConfigSupported_Object((1,3,6,1,4,1,9,9,140,1,1,11),_CcopsRoleConfigSupported_Type())
ccopsRoleConfigSupported.setMaxAccess(_E)
if mibBuilder.loadTexts:ccopsRoleConfigSupported.setStatus(_B)
_CcopsMIBNotifications_ObjectIdentity=ObjectIdentity
ccopsMIBNotifications=_CcopsMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,140,2))
_CcopsMIBConformance_ObjectIdentity=ObjectIdentity
ccopsMIBConformance=_CcopsMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,140,3))
_CcopsMIBCompliances_ObjectIdentity=ObjectIdentity
ccopsMIBCompliances=_CcopsMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,140,3,1))
_CcopsMIBGroups_ObjectIdentity=ObjectIdentity
ccopsMIBGroups=_CcopsMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,140,3,2))
ccopsGlobalGroup=ObjectGroup((1,3,6,1,4,1,9,9,140,3,2,1))
ccopsGlobalGroup.setObjects(*((_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T)))
if mibBuilder.loadTexts:ccopsGlobalGroup.setStatus(_c)
ccopsGlobalGroupRev2=ObjectGroup((1,3,6,1,4,1,9,9,140,3,2,2))
ccopsGlobalGroupRev2.setObjects(*((_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_R),(_A,_T),(_A,_d)))
if mibBuilder.loadTexts:ccopsGlobalGroupRev2.setStatus(_B)
ccopsRoleGroup=ObjectGroup((1,3,6,1,4,1,9,9,140,3,2,3))
ccopsRoleGroup.setObjects(*((_A,_Q),(_A,_S)))
if mibBuilder.loadTexts:ccopsRoleGroup.setStatus(_B)
ccopsMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,140,3,1,1))
ccopsMIBCompliance.setObjects((_A,_e))
if mibBuilder.loadTexts:ccopsMIBCompliance.setStatus(_c)
ccopsMIBComplianceRev2=ModuleCompliance((1,3,6,1,4,1,9,9,140,3,1,2))
ccopsMIBComplianceRev2.setObjects(*((_A,_f),(_A,_g)))
if mibBuilder.loadTexts:ccopsMIBComplianceRev2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'CopsRole':CopsRole,'CopsRoleCombination':CopsRoleCombination,_a:CopsDomainName,'CopsClientType':CopsClientType,'ciscoCopsClientMIB':ciscoCopsClientMIB,'ccopsMIBObjects':ccopsMIBObjects,'ccopsGlobalObjects':ccopsGlobalObjects,_I:ccopsServerMax,_Q:ccopsMaxRole,_R:ccopsMaxRoleCombination,'ccopsServerConfigTable':ccopsServerConfigTable,'ccopsServerConfigEntry':ccopsServerConfigEntry,_X:ccopsServerConfigClientType,_Y:ccopsServerConfigName,_J:ccopsServerConfigPriority,_K:ccopsServerConfigPort,_L:ccopsServerConfigStatus,_M:ccopsInitialTimeout,_N:ccopsTimeoutIncrement,_O:ccopsTimeoutMax,'ccopsDomainTable':ccopsDomainTable,'ccopsDomainEntry':ccopsDomainEntry,_Z:ccopsDomainClientType,_P:ccopsDomainName,'ccopsRoleTable':ccopsRoleTable,'ccopsRoleEntry':ccopsRoleEntry,_b:ccopsRoleName,_S:ccopsRoleStatus,'ccopsIfTable':ccopsIfTable,'ccopsIfEntry':ccopsIfEntry,_T:ccopsIfRoleCombination,_d:ccopsRoleConfigSupported,'ccopsMIBNotifications':ccopsMIBNotifications,'ccopsMIBConformance':ccopsMIBConformance,'ccopsMIBCompliances':ccopsMIBCompliances,'ccopsMIBCompliance':ccopsMIBCompliance,'ccopsMIBComplianceRev2':ccopsMIBComplianceRev2,'ccopsMIBGroups':ccopsMIBGroups,_e:ccopsGlobalGroup,_f:ccopsGlobalGroupRev2,_g:ccopsRoleGroup})