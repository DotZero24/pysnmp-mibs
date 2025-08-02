_Z='hpicfUrpfConfigTableGroup1'
_Y='hpicfUrpfConfigTableGroup'
_X='hpicfUrpfConfigAllowlistAclName'
_W='hpicfUrpfConfigHasAllowlistAcl'
_V='hpicfUrpfStatsBlockedOctets'
_U='hpicfUrpfStatsBlockedPackets'
_T='deprecated'
_S='hpicfUrpfConfigGlobalLogTimeout'
_R='hpicfUrpfConfigGlobalEnable'
_Q='read-only'
_P='not-accessible'
_O='hpicfUrpfStatsTableGroup'
_N='hpicfUrpfScalarGroup'
_M='hpicfUrpfConfigWhitelistAclName'
_L='hpicfUrpfConfigHasWhitelistAcl'
_K='hpicfUrpfConfigLogging'
_J='hpicfUrpfConfigAllowDhcp'
_I='hpicfUrpfConfigDefRoute'
_H='hpicfUrpfConfigMode'
_G='hpicfUrpfAddrFamily'
_F='hpicfUrpfIfIndex'
_E='Integer32'
_D='TruthValue'
_C='read-write'
_B='current'
_A='HP-ICF-URPF-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpSwitch,=mibBuilder.importSymbols('HP-ICF-OID','hpSwitch')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddressType,=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_D)
hpicfUrpfMIB=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,5,1,131))
if mibBuilder.loadTexts:hpicfUrpfMIB.setRevisions(('2021-06-10 00:00','2016-06-14 00:00'))
_HpicfUrpfConfig_ObjectIdentity=ObjectIdentity
hpicfUrpfConfig=_HpicfUrpfConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,131,1))
class _HpicfUrpfConfigGlobalEnable_Type(TruthValue):defaultValue=2
_HpicfUrpfConfigGlobalEnable_Type.__name__=_D
_HpicfUrpfConfigGlobalEnable_Object=MibScalar
hpicfUrpfConfigGlobalEnable=_HpicfUrpfConfigGlobalEnable_Object((1,3,6,1,4,1,11,2,14,11,5,1,131,1,1),_HpicfUrpfConfigGlobalEnable_Type())
hpicfUrpfConfigGlobalEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfUrpfConfigGlobalEnable.setStatus(_B)
class _HpicfUrpfConfigGlobalLogTimeout_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,300))
_HpicfUrpfConfigGlobalLogTimeout_Type.__name__=_E
_HpicfUrpfConfigGlobalLogTimeout_Object=MibScalar
hpicfUrpfConfigGlobalLogTimeout=_HpicfUrpfConfigGlobalLogTimeout_Object((1,3,6,1,4,1,11,2,14,11,5,1,131,1,2),_HpicfUrpfConfigGlobalLogTimeout_Type())
hpicfUrpfConfigGlobalLogTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfUrpfConfigGlobalLogTimeout.setStatus(_B)
_HpicfUrpfConfigTable_Object=MibTable
hpicfUrpfConfigTable=_HpicfUrpfConfigTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,131,1,3))
if mibBuilder.loadTexts:hpicfUrpfConfigTable.setStatus(_B)
_HpicfUrpfConfigEntry_Object=MibTableRow
hpicfUrpfConfigEntry=_HpicfUrpfConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,131,1,3,1))
hpicfUrpfConfigEntry.setIndexNames((0,_A,_F),(0,_A,_G))
if mibBuilder.loadTexts:hpicfUrpfConfigEntry.setStatus(_B)
_HpicfUrpfIfIndex_Type=InterfaceIndex
_HpicfUrpfIfIndex_Object=MibTableColumn
hpicfUrpfIfIndex=_HpicfUrpfIfIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,131,1,3,1,1),_HpicfUrpfIfIndex_Type())
hpicfUrpfIfIndex.setMaxAccess(_P)
if mibBuilder.loadTexts:hpicfUrpfIfIndex.setStatus(_B)
_HpicfUrpfAddrFamily_Type=InetAddressType
_HpicfUrpfAddrFamily_Object=MibTableColumn
hpicfUrpfAddrFamily=_HpicfUrpfAddrFamily_Object((1,3,6,1,4,1,11,2,14,11,5,1,131,1,3,1,2),_HpicfUrpfAddrFamily_Type())
hpicfUrpfAddrFamily.setMaxAccess(_P)
if mibBuilder.loadTexts:hpicfUrpfAddrFamily.setStatus(_B)
class _HpicfUrpfConfigMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('strict',2),('loose',3)))
_HpicfUrpfConfigMode_Type.__name__=_E
_HpicfUrpfConfigMode_Object=MibTableColumn
hpicfUrpfConfigMode=_HpicfUrpfConfigMode_Object((1,3,6,1,4,1,11,2,14,11,5,1,131,1,3,1,3),_HpicfUrpfConfigMode_Type())
hpicfUrpfConfigMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfUrpfConfigMode.setStatus(_B)
class _HpicfUrpfConfigDefRoute_Type(TruthValue):defaultValue=2
_HpicfUrpfConfigDefRoute_Type.__name__=_D
_HpicfUrpfConfigDefRoute_Object=MibTableColumn
hpicfUrpfConfigDefRoute=_HpicfUrpfConfigDefRoute_Object((1,3,6,1,4,1,11,2,14,11,5,1,131,1,3,1,4),_HpicfUrpfConfigDefRoute_Type())
hpicfUrpfConfigDefRoute.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfUrpfConfigDefRoute.setStatus(_B)
class _HpicfUrpfConfigAllowDhcp_Type(TruthValue):defaultValue=2
_HpicfUrpfConfigAllowDhcp_Type.__name__=_D
_HpicfUrpfConfigAllowDhcp_Object=MibTableColumn
hpicfUrpfConfigAllowDhcp=_HpicfUrpfConfigAllowDhcp_Object((1,3,6,1,4,1,11,2,14,11,5,1,131,1,3,1,5),_HpicfUrpfConfigAllowDhcp_Type())
hpicfUrpfConfigAllowDhcp.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfUrpfConfigAllowDhcp.setStatus(_B)
class _HpicfUrpfConfigLogging_Type(TruthValue):defaultValue=2
_HpicfUrpfConfigLogging_Type.__name__=_D
_HpicfUrpfConfigLogging_Object=MibTableColumn
hpicfUrpfConfigLogging=_HpicfUrpfConfigLogging_Object((1,3,6,1,4,1,11,2,14,11,5,1,131,1,3,1,6),_HpicfUrpfConfigLogging_Type())
hpicfUrpfConfigLogging.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfUrpfConfigLogging.setStatus(_B)
class _HpicfUrpfConfigHasWhitelistAcl_Type(TruthValue):defaultValue=2
_HpicfUrpfConfigHasWhitelistAcl_Type.__name__=_D
_HpicfUrpfConfigHasWhitelistAcl_Object=MibTableColumn
hpicfUrpfConfigHasWhitelistAcl=_HpicfUrpfConfigHasWhitelistAcl_Object((1,3,6,1,4,1,11,2,14,11,5,1,131,1,3,1,7),_HpicfUrpfConfigHasWhitelistAcl_Type())
hpicfUrpfConfigHasWhitelistAcl.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfUrpfConfigHasWhitelistAcl.setStatus(_B)
_HpicfUrpfConfigWhitelistAclName_Type=SnmpAdminString
_HpicfUrpfConfigWhitelistAclName_Object=MibTableColumn
hpicfUrpfConfigWhitelistAclName=_HpicfUrpfConfigWhitelistAclName_Object((1,3,6,1,4,1,11,2,14,11,5,1,131,1,3,1,8),_HpicfUrpfConfigWhitelistAclName_Type())
hpicfUrpfConfigWhitelistAclName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfUrpfConfigWhitelistAclName.setStatus(_B)
class _HpicfUrpfConfigHasAllowlistAcl_Type(TruthValue):defaultValue=2
_HpicfUrpfConfigHasAllowlistAcl_Type.__name__=_D
_HpicfUrpfConfigHasAllowlistAcl_Object=MibTableColumn
hpicfUrpfConfigHasAllowlistAcl=_HpicfUrpfConfigHasAllowlistAcl_Object((1,3,6,1,4,1,11,2,14,11,5,1,131,1,3,1,9),_HpicfUrpfConfigHasAllowlistAcl_Type())
hpicfUrpfConfigHasAllowlistAcl.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfUrpfConfigHasAllowlistAcl.setStatus(_B)
_HpicfUrpfConfigAllowlistAclName_Type=SnmpAdminString
_HpicfUrpfConfigAllowlistAclName_Object=MibTableColumn
hpicfUrpfConfigAllowlistAclName=_HpicfUrpfConfigAllowlistAclName_Object((1,3,6,1,4,1,11,2,14,11,5,1,131,1,3,1,10),_HpicfUrpfConfigAllowlistAclName_Type())
hpicfUrpfConfigAllowlistAclName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfUrpfConfigAllowlistAclName.setStatus(_B)
_HpicfUrpfStats_ObjectIdentity=ObjectIdentity
hpicfUrpfStats=_HpicfUrpfStats_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,131,2))
_HpicfUrpfStatsTable_Object=MibTable
hpicfUrpfStatsTable=_HpicfUrpfStatsTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,131,2,1))
if mibBuilder.loadTexts:hpicfUrpfStatsTable.setStatus(_B)
_HpicfUrpfStatsEntry_Object=MibTableRow
hpicfUrpfStatsEntry=_HpicfUrpfStatsEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,131,2,1,1))
hpicfUrpfStatsEntry.setIndexNames((0,_A,_F),(0,_A,_G))
if mibBuilder.loadTexts:hpicfUrpfStatsEntry.setStatus(_B)
_HpicfUrpfStatsBlockedPackets_Type=Counter64
_HpicfUrpfStatsBlockedPackets_Object=MibTableColumn
hpicfUrpfStatsBlockedPackets=_HpicfUrpfStatsBlockedPackets_Object((1,3,6,1,4,1,11,2,14,11,5,1,131,2,1,1,1),_HpicfUrpfStatsBlockedPackets_Type())
hpicfUrpfStatsBlockedPackets.setMaxAccess(_Q)
if mibBuilder.loadTexts:hpicfUrpfStatsBlockedPackets.setStatus(_B)
_HpicfUrpfStatsBlockedOctets_Type=Counter64
_HpicfUrpfStatsBlockedOctets_Object=MibTableColumn
hpicfUrpfStatsBlockedOctets=_HpicfUrpfStatsBlockedOctets_Object((1,3,6,1,4,1,11,2,14,11,5,1,131,2,1,1,2),_HpicfUrpfStatsBlockedOctets_Type())
hpicfUrpfStatsBlockedOctets.setMaxAccess(_Q)
if mibBuilder.loadTexts:hpicfUrpfStatsBlockedOctets.setStatus(_B)
_HpicfUrpfConformance_ObjectIdentity=ObjectIdentity
hpicfUrpfConformance=_HpicfUrpfConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,131,3))
_HpicfUrpfMIBGroups_ObjectIdentity=ObjectIdentity
hpicfUrpfMIBGroups=_HpicfUrpfMIBGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,131,3,1))
_HpicfUrpfMIBCompliances_ObjectIdentity=ObjectIdentity
hpicfUrpfMIBCompliances=_HpicfUrpfMIBCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,131,3,2))
hpicfUrpfScalarGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,131,3,1,1))
hpicfUrpfScalarGroup.setObjects(*((_A,_R),(_A,_S)))
if mibBuilder.loadTexts:hpicfUrpfScalarGroup.setStatus(_B)
hpicfUrpfConfigTableGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,131,3,1,2))
hpicfUrpfConfigTableGroup.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:hpicfUrpfConfigTableGroup.setStatus(_T)
hpicfUrpfStatsTableGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,131,3,1,3))
hpicfUrpfStatsTableGroup.setObjects(*((_A,_U),(_A,_V)))
if mibBuilder.loadTexts:hpicfUrpfStatsTableGroup.setStatus(_B)
hpicfUrpfConfigTableGroup1=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,131,3,1,4))
hpicfUrpfConfigTableGroup1.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:hpicfUrpfConfigTableGroup1.setStatus(_B)
hpicfUrpfMIBCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,131,3,2,1))
hpicfUrpfMIBCompliance.setObjects(*((_A,_N),(_A,_Y),(_A,_O)))
if mibBuilder.loadTexts:hpicfUrpfMIBCompliance.setStatus(_T)
hpicfUrpfMIBCompliance1=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,131,3,2,2))
hpicfUrpfMIBCompliance1.setObjects(*((_A,_N),(_A,_Z),(_A,_O)))
if mibBuilder.loadTexts:hpicfUrpfMIBCompliance1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'hpicfUrpfMIB':hpicfUrpfMIB,'hpicfUrpfConfig':hpicfUrpfConfig,_R:hpicfUrpfConfigGlobalEnable,_S:hpicfUrpfConfigGlobalLogTimeout,'hpicfUrpfConfigTable':hpicfUrpfConfigTable,'hpicfUrpfConfigEntry':hpicfUrpfConfigEntry,_F:hpicfUrpfIfIndex,_G:hpicfUrpfAddrFamily,_H:hpicfUrpfConfigMode,_I:hpicfUrpfConfigDefRoute,_J:hpicfUrpfConfigAllowDhcp,_K:hpicfUrpfConfigLogging,_L:hpicfUrpfConfigHasWhitelistAcl,_M:hpicfUrpfConfigWhitelistAclName,_W:hpicfUrpfConfigHasAllowlistAcl,_X:hpicfUrpfConfigAllowlistAclName,'hpicfUrpfStats':hpicfUrpfStats,'hpicfUrpfStatsTable':hpicfUrpfStatsTable,'hpicfUrpfStatsEntry':hpicfUrpfStatsEntry,_U:hpicfUrpfStatsBlockedPackets,_V:hpicfUrpfStatsBlockedOctets,'hpicfUrpfConformance':hpicfUrpfConformance,'hpicfUrpfMIBGroups':hpicfUrpfMIBGroups,_N:hpicfUrpfScalarGroup,_Y:hpicfUrpfConfigTableGroup,_O:hpicfUrpfStatsTableGroup,_Z:hpicfUrpfConfigTableGroup1,'hpicfUrpfMIBCompliances':hpicfUrpfMIBCompliances,'hpicfUrpfMIBCompliance':hpicfUrpfMIBCompliance,'hpicfUrpfMIBCompliance1':hpicfUrpfMIBCompliance1})