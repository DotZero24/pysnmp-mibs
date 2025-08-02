_X='ciscoLwappOpendnsTagGroupVer2'
_W='claOpendnsWlanDhcpOpt6'
_V='claOpendnsApiToken'
_U='claOpendnsForceEnable'
_T='claOpendnsEnable'
_S='read-only'
_R='claOpendnsProfileName'
_Q='cLWlanIndex'
_P='CISCO-LWAPP-WLAN-MIB'
_O='ciscoLwappOpendnsConfigGroup'
_N='deprecated'
_M='claOpendnsProfileIdentity'
_L='claOpendnsProfileStatus'
_K='claOpendnsWlanProfileStatus'
_J='claOpendnsWlanMode'
_I='claOpendnsWlanProfileName'
_H='claOpendnsProfileRowStatus'
_G='Integer32'
_F='SnmpAdminString'
_E='ciscoLwappOpendnsTagGroup'
_D='TruthValue'
_C='read-write'
_B='current'
_A='CISCO-LWAPP-OPENDNS-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cLWlanIndex,=mibBuilder.importSymbols(_P,_Q)
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_D)
ciscoLwappOpendnsMIB=ModuleIdentity((1,3,6,1,4,1,9,9,837))
if mibBuilder.loadTexts:ciscoLwappOpendnsMIB.setRevisions(('2018-07-03 00:00','2017-02-10 00:00'))
_CiscoLwappOpendnsMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoLwappOpendnsMIBNotifs=_CiscoLwappOpendnsMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,837,0))
_CiscoLwappOpendnsMIBObjects_ObjectIdentity=ObjectIdentity
ciscoLwappOpendnsMIBObjects=_CiscoLwappOpendnsMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,837,1))
_CiscoLwappOpendnsTag_ObjectIdentity=ObjectIdentity
ciscoLwappOpendnsTag=_CiscoLwappOpendnsTag_ObjectIdentity((1,3,6,1,4,1,9,9,837,1,1))
_ClaOpendnsProfileTable_Object=MibTable
claOpendnsProfileTable=_ClaOpendnsProfileTable_Object((1,3,6,1,4,1,9,9,837,1,1,1))
if mibBuilder.loadTexts:claOpendnsProfileTable.setStatus(_B)
_ClaOpendnsProfileEntry_Object=MibTableRow
claOpendnsProfileEntry=_ClaOpendnsProfileEntry_Object((1,3,6,1,4,1,9,9,837,1,1,1,1))
claOpendnsProfileEntry.setIndexNames((0,_A,_R))
if mibBuilder.loadTexts:claOpendnsProfileEntry.setStatus(_B)
_ClaOpendnsProfileName_Type=SnmpAdminString
_ClaOpendnsProfileName_Object=MibTableColumn
claOpendnsProfileName=_ClaOpendnsProfileName_Object((1,3,6,1,4,1,9,9,837,1,1,1,1,1),_ClaOpendnsProfileName_Type())
claOpendnsProfileName.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:claOpendnsProfileName.setStatus(_B)
_ClaOpendnsProfileRowStatus_Type=RowStatus
_ClaOpendnsProfileRowStatus_Object=MibTableColumn
claOpendnsProfileRowStatus=_ClaOpendnsProfileRowStatus_Object((1,3,6,1,4,1,9,9,837,1,1,1,1,2),_ClaOpendnsProfileRowStatus_Type())
claOpendnsProfileRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:claOpendnsProfileRowStatus.setStatus(_B)
class _ClaOpendnsProfileStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('notInuse',1),('inProgress',2),('success',3),('failed',4),('inuse',5)))
_ClaOpendnsProfileStatus_Type.__name__=_G
_ClaOpendnsProfileStatus_Object=MibTableColumn
claOpendnsProfileStatus=_ClaOpendnsProfileStatus_Object((1,3,6,1,4,1,9,9,837,1,1,1,1,3),_ClaOpendnsProfileStatus_Type())
claOpendnsProfileStatus.setMaxAccess(_S)
if mibBuilder.loadTexts:claOpendnsProfileStatus.setStatus(_B)
_ClaOpendnsProfileIdentity_Type=SnmpAdminString
_ClaOpendnsProfileIdentity_Object=MibTableColumn
claOpendnsProfileIdentity=_ClaOpendnsProfileIdentity_Object((1,3,6,1,4,1,9,9,837,1,1,1,1,4),_ClaOpendnsProfileIdentity_Type())
claOpendnsProfileIdentity.setMaxAccess(_S)
if mibBuilder.loadTexts:claOpendnsProfileIdentity.setStatus(_B)
_ClaOpendnsWlanTable_Object=MibTable
claOpendnsWlanTable=_ClaOpendnsWlanTable_Object((1,3,6,1,4,1,9,9,837,1,1,2))
if mibBuilder.loadTexts:claOpendnsWlanTable.setStatus(_B)
_ClaOpendnsWlanEntry_Object=MibTableRow
claOpendnsWlanEntry=_ClaOpendnsWlanEntry_Object((1,3,6,1,4,1,9,9,837,1,1,2,1))
claOpendnsWlanEntry.setIndexNames((0,_P,_Q))
if mibBuilder.loadTexts:claOpendnsWlanEntry.setStatus(_B)
class _ClaOpendnsWlanProfileName_Type(SnmpAdminString):defaultValue=OctetString('')
_ClaOpendnsWlanProfileName_Type.__name__=_F
_ClaOpendnsWlanProfileName_Object=MibTableColumn
claOpendnsWlanProfileName=_ClaOpendnsWlanProfileName_Object((1,3,6,1,4,1,9,9,837,1,1,2,1,1),_ClaOpendnsWlanProfileName_Type())
claOpendnsWlanProfileName.setMaxAccess(_C)
if mibBuilder.loadTexts:claOpendnsWlanProfileName.setStatus(_B)
class _ClaOpendnsWlanMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ignore',1),('force',2),('copy',3)))
_ClaOpendnsWlanMode_Type.__name__=_G
_ClaOpendnsWlanMode_Object=MibTableColumn
claOpendnsWlanMode=_ClaOpendnsWlanMode_Object((1,3,6,1,4,1,9,9,837,1,1,2,1,2),_ClaOpendnsWlanMode_Type())
claOpendnsWlanMode.setMaxAccess(_C)
if mibBuilder.loadTexts:claOpendnsWlanMode.setStatus(_B)
class _ClaOpendnsWlanProfileStatus_Type(TruthValue):defaultValue=2
_ClaOpendnsWlanProfileStatus_Type.__name__=_D
_ClaOpendnsWlanProfileStatus_Object=MibTableColumn
claOpendnsWlanProfileStatus=_ClaOpendnsWlanProfileStatus_Object((1,3,6,1,4,1,9,9,837,1,1,2,1,3),_ClaOpendnsWlanProfileStatus_Type())
claOpendnsWlanProfileStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:claOpendnsWlanProfileStatus.setStatus(_B)
class _ClaOpendnsWlanDhcpOpt6_Type(TruthValue):defaultValue=1
_ClaOpendnsWlanDhcpOpt6_Type.__name__=_D
_ClaOpendnsWlanDhcpOpt6_Object=MibTableColumn
claOpendnsWlanDhcpOpt6=_ClaOpendnsWlanDhcpOpt6_Object((1,3,6,1,4,1,9,9,837,1,1,2,1,4),_ClaOpendnsWlanDhcpOpt6_Type())
claOpendnsWlanDhcpOpt6.setMaxAccess(_C)
if mibBuilder.loadTexts:claOpendnsWlanDhcpOpt6.setStatus(_B)
_CiscoLwappOpendnsConfig_ObjectIdentity=ObjectIdentity
ciscoLwappOpendnsConfig=_CiscoLwappOpendnsConfig_ObjectIdentity((1,3,6,1,4,1,9,9,837,1,2))
class _ClaOpendnsEnable_Type(TruthValue):defaultValue=2
_ClaOpendnsEnable_Type.__name__=_D
_ClaOpendnsEnable_Object=MibScalar
claOpendnsEnable=_ClaOpendnsEnable_Object((1,3,6,1,4,1,9,9,837,1,2,1),_ClaOpendnsEnable_Type())
claOpendnsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:claOpendnsEnable.setStatus(_B)
class _ClaOpendnsForceEnable_Type(TruthValue):defaultValue=2
_ClaOpendnsForceEnable_Type.__name__=_D
_ClaOpendnsForceEnable_Object=MibScalar
claOpendnsForceEnable=_ClaOpendnsForceEnable_Object((1,3,6,1,4,1,9,9,837,1,2,2),_ClaOpendnsForceEnable_Type())
claOpendnsForceEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:claOpendnsForceEnable.setStatus(_B)
class _ClaOpendnsApiToken_Type(SnmpAdminString):defaultValue=OctetString('')
_ClaOpendnsApiToken_Type.__name__=_F
_ClaOpendnsApiToken_Object=MibScalar
claOpendnsApiToken=_ClaOpendnsApiToken_Object((1,3,6,1,4,1,9,9,837,1,2,3),_ClaOpendnsApiToken_Type())
claOpendnsApiToken.setMaxAccess(_C)
if mibBuilder.loadTexts:claOpendnsApiToken.setStatus(_B)
_CiscoLwappOpendnsMIBConform_ObjectIdentity=ObjectIdentity
ciscoLwappOpendnsMIBConform=_CiscoLwappOpendnsMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,837,2))
_CiscoLwappOpendnsMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoLwappOpendnsMIBCompliances=_CiscoLwappOpendnsMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,837,2,1))
_CiscoLwappOpendnsMIBGroups_ObjectIdentity=ObjectIdentity
ciscoLwappOpendnsMIBGroups=_CiscoLwappOpendnsMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,837,2,2))
ciscoLwappOpendnsTagGroup=ObjectGroup((1,3,6,1,4,1,9,9,837,2,2,1))
ciscoLwappOpendnsTagGroup.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:ciscoLwappOpendnsTagGroup.setStatus(_N)
ciscoLwappOpendnsConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,837,2,2,2))
ciscoLwappOpendnsConfigGroup.setObjects(*((_A,_T),(_A,_U),(_A,_V)))
if mibBuilder.loadTexts:ciscoLwappOpendnsConfigGroup.setStatus(_B)
ciscoLwappOpendnsTagGroupVer2=ObjectGroup((1,3,6,1,4,1,9,9,837,2,2,3))
ciscoLwappOpendnsTagGroupVer2.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_W)))
if mibBuilder.loadTexts:ciscoLwappOpendnsTagGroupVer2.setStatus(_B)
ciscoLwappOpendnsMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,837,2,1,1))
ciscoLwappOpendnsMIBCompliance.setObjects((_A,_E))
if mibBuilder.loadTexts:ciscoLwappOpendnsMIBCompliance.setStatus(_N)
ciscoLwappOpendnsMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,837,2,1,2))
ciscoLwappOpendnsMIBComplianceRev1.setObjects(*((_A,_E),(_A,_O)))
if mibBuilder.loadTexts:ciscoLwappOpendnsMIBComplianceRev1.setStatus(_N)
ciscoLwappOpendnsMIBComplianceRev2=ModuleCompliance((1,3,6,1,4,1,9,9,837,2,1,3))
ciscoLwappOpendnsMIBComplianceRev2.setObjects(*((_A,_E),(_A,_O),(_A,_X)))
if mibBuilder.loadTexts:ciscoLwappOpendnsMIBComplianceRev2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoLwappOpendnsMIB':ciscoLwappOpendnsMIB,'ciscoLwappOpendnsMIBNotifs':ciscoLwappOpendnsMIBNotifs,'ciscoLwappOpendnsMIBObjects':ciscoLwappOpendnsMIBObjects,'ciscoLwappOpendnsTag':ciscoLwappOpendnsTag,'claOpendnsProfileTable':claOpendnsProfileTable,'claOpendnsProfileEntry':claOpendnsProfileEntry,_R:claOpendnsProfileName,_H:claOpendnsProfileRowStatus,_L:claOpendnsProfileStatus,_M:claOpendnsProfileIdentity,'claOpendnsWlanTable':claOpendnsWlanTable,'claOpendnsWlanEntry':claOpendnsWlanEntry,_I:claOpendnsWlanProfileName,_J:claOpendnsWlanMode,_K:claOpendnsWlanProfileStatus,_W:claOpendnsWlanDhcpOpt6,'ciscoLwappOpendnsConfig':ciscoLwappOpendnsConfig,_T:claOpendnsEnable,_U:claOpendnsForceEnable,_V:claOpendnsApiToken,'ciscoLwappOpendnsMIBConform':ciscoLwappOpendnsMIBConform,'ciscoLwappOpendnsMIBCompliances':ciscoLwappOpendnsMIBCompliances,'ciscoLwappOpendnsMIBCompliance':ciscoLwappOpendnsMIBCompliance,'ciscoLwappOpendnsMIBComplianceRev1':ciscoLwappOpendnsMIBComplianceRev1,'ciscoLwappOpendnsMIBComplianceRev2':ciscoLwappOpendnsMIBComplianceRev2,'ciscoLwappOpendnsMIBGroups':ciscoLwappOpendnsMIBGroups,_E:ciscoLwappOpendnsTagGroup,_O:ciscoLwappOpendnsConfigGroup,_X:ciscoLwappOpendnsTagGroupVer2})