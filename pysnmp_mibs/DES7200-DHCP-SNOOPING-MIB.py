_X='myDhcpSnoopingMIBGroup'
_W='mySNDhcpBindingsStatus'
_V='mySNDhcpBindingsLeasedTime'
_U='mySNDhcpBindingsInterface'
_T='mySNDhcpBindingsIpAddress'
_S='mySNDhcpAddressBindEnable'
_R='mySNDhcpIfSuppressionEnable'
_Q='mySNDhcpIfTrustEnable'
_P='mySNDhcpMatchMacAddressEnable'
_O='mySNDhcpRelayAgentInfoOptEnable'
_N='mySNDhcpDatabaseUpdateInterval'
_M='mySNDhcpFeatureEnable'
_L='mySNDhcpBindingsAddrType'
_K='mySNDhcpAddressBindIndex'
_J='mySNDhcpIfSuppressionIndex'
_I='mySNDhcpIfTrustIndex'
_H='seconds'
_G='Integer32'
_F='mySNDhcpBindingsMacAddress'
_E='mySNDhcpBindingsVlan'
_D='not-accessible'
_C='read-write'
_B='DES7200-DHCP-SNOOPING-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
myMgmt,=mibBuilder.importSymbols('DES7200-SMI','myMgmt')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
VlanIndex,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanIndex')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
myDhcpSnoopingMIB=ModuleIdentity((1,3,6,1,4,1,171,10,97,2,42))
if mibBuilder.loadTexts:myDhcpSnoopingMIB.setRevisions(('2007-10-18 00:00',))
_MyDhcpSnoopingMIBObjects_ObjectIdentity=ObjectIdentity
myDhcpSnoopingMIBObjects=_MyDhcpSnoopingMIBObjects_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,42,1))
_MySNDhcpGlobal_ObjectIdentity=ObjectIdentity
mySNDhcpGlobal=_MySNDhcpGlobal_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,42,1,1))
_MySNDhcpFeatureEnable_Type=TruthValue
_MySNDhcpFeatureEnable_Object=MibScalar
mySNDhcpFeatureEnable=_MySNDhcpFeatureEnable_Object((1,3,6,1,4,1,171,10,97,2,42,1,1,1),_MySNDhcpFeatureEnable_Type())
mySNDhcpFeatureEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:mySNDhcpFeatureEnable.setStatus(_A)
_MySNDhcpDatabaseUpdateInterval_Type=Unsigned32
_MySNDhcpDatabaseUpdateInterval_Object=MibScalar
mySNDhcpDatabaseUpdateInterval=_MySNDhcpDatabaseUpdateInterval_Object((1,3,6,1,4,1,171,10,97,2,42,1,1,2),_MySNDhcpDatabaseUpdateInterval_Type())
mySNDhcpDatabaseUpdateInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:mySNDhcpDatabaseUpdateInterval.setStatus(_A)
if mibBuilder.loadTexts:mySNDhcpDatabaseUpdateInterval.setUnits(_H)
_MySNDhcpRelayAgentInfoOptEnable_Type=TruthValue
_MySNDhcpRelayAgentInfoOptEnable_Object=MibScalar
mySNDhcpRelayAgentInfoOptEnable=_MySNDhcpRelayAgentInfoOptEnable_Object((1,3,6,1,4,1,171,10,97,2,42,1,1,3),_MySNDhcpRelayAgentInfoOptEnable_Type())
mySNDhcpRelayAgentInfoOptEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:mySNDhcpRelayAgentInfoOptEnable.setStatus(_A)
_MySNDhcpMatchMacAddressEnable_Type=TruthValue
_MySNDhcpMatchMacAddressEnable_Object=MibScalar
mySNDhcpMatchMacAddressEnable=_MySNDhcpMatchMacAddressEnable_Object((1,3,6,1,4,1,171,10,97,2,42,1,1,4),_MySNDhcpMatchMacAddressEnable_Type())
mySNDhcpMatchMacAddressEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:mySNDhcpMatchMacAddressEnable.setStatus(_A)
_MySNDhcpInterface_ObjectIdentity=ObjectIdentity
mySNDhcpInterface=_MySNDhcpInterface_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,42,1,2))
_MySNDhcpIfTrustTable_Object=MibTable
mySNDhcpIfTrustTable=_MySNDhcpIfTrustTable_Object((1,3,6,1,4,1,171,10,97,2,42,1,2,1))
if mibBuilder.loadTexts:mySNDhcpIfTrustTable.setStatus(_A)
_MySNDhcpIfTrustEntry_Object=MibTableRow
mySNDhcpIfTrustEntry=_MySNDhcpIfTrustEntry_Object((1,3,6,1,4,1,171,10,97,2,42,1,2,1,1))
mySNDhcpIfTrustEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:mySNDhcpIfTrustEntry.setStatus(_A)
_MySNDhcpIfTrustIndex_Type=InterfaceIndex
_MySNDhcpIfTrustIndex_Object=MibTableColumn
mySNDhcpIfTrustIndex=_MySNDhcpIfTrustIndex_Object((1,3,6,1,4,1,171,10,97,2,42,1,2,1,1,1),_MySNDhcpIfTrustIndex_Type())
mySNDhcpIfTrustIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:mySNDhcpIfTrustIndex.setStatus(_A)
_MySNDhcpIfTrustEnable_Type=TruthValue
_MySNDhcpIfTrustEnable_Object=MibTableColumn
mySNDhcpIfTrustEnable=_MySNDhcpIfTrustEnable_Object((1,3,6,1,4,1,171,10,97,2,42,1,2,1,1,2),_MySNDhcpIfTrustEnable_Type())
mySNDhcpIfTrustEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:mySNDhcpIfTrustEnable.setStatus(_A)
_MySNDhcpIfSuppressionTable_Object=MibTable
mySNDhcpIfSuppressionTable=_MySNDhcpIfSuppressionTable_Object((1,3,6,1,4,1,171,10,97,2,42,1,2,2))
if mibBuilder.loadTexts:mySNDhcpIfSuppressionTable.setStatus(_A)
_MySNDhcpIfSuppressionEntry_Object=MibTableRow
mySNDhcpIfSuppressionEntry=_MySNDhcpIfSuppressionEntry_Object((1,3,6,1,4,1,171,10,97,2,42,1,2,2,1))
mySNDhcpIfSuppressionEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:mySNDhcpIfSuppressionEntry.setStatus(_A)
_MySNDhcpIfSuppressionIndex_Type=InterfaceIndex
_MySNDhcpIfSuppressionIndex_Object=MibTableColumn
mySNDhcpIfSuppressionIndex=_MySNDhcpIfSuppressionIndex_Object((1,3,6,1,4,1,171,10,97,2,42,1,2,2,1,1),_MySNDhcpIfSuppressionIndex_Type())
mySNDhcpIfSuppressionIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:mySNDhcpIfSuppressionIndex.setStatus(_A)
_MySNDhcpIfSuppressionEnable_Type=TruthValue
_MySNDhcpIfSuppressionEnable_Object=MibTableColumn
mySNDhcpIfSuppressionEnable=_MySNDhcpIfSuppressionEnable_Object((1,3,6,1,4,1,171,10,97,2,42,1,2,2,1,2),_MySNDhcpIfSuppressionEnable_Type())
mySNDhcpIfSuppressionEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:mySNDhcpIfSuppressionEnable.setStatus(_A)
_MySNDhcpAddressBindTable_Object=MibTable
mySNDhcpAddressBindTable=_MySNDhcpAddressBindTable_Object((1,3,6,1,4,1,171,10,97,2,42,1,2,3))
if mibBuilder.loadTexts:mySNDhcpAddressBindTable.setStatus(_A)
_MySNDhcpAddressBindEntry_Object=MibTableRow
mySNDhcpAddressBindEntry=_MySNDhcpAddressBindEntry_Object((1,3,6,1,4,1,171,10,97,2,42,1,2,3,1))
mySNDhcpAddressBindEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:mySNDhcpAddressBindEntry.setStatus(_A)
_MySNDhcpAddressBindIndex_Type=InterfaceIndex
_MySNDhcpAddressBindIndex_Object=MibTableColumn
mySNDhcpAddressBindIndex=_MySNDhcpAddressBindIndex_Object((1,3,6,1,4,1,171,10,97,2,42,1,2,3,1,1),_MySNDhcpAddressBindIndex_Type())
mySNDhcpAddressBindIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:mySNDhcpAddressBindIndex.setStatus(_A)
_MySNDhcpAddressBindEnable_Type=TruthValue
_MySNDhcpAddressBindEnable_Object=MibTableColumn
mySNDhcpAddressBindEnable=_MySNDhcpAddressBindEnable_Object((1,3,6,1,4,1,171,10,97,2,42,1,2,3,1,2),_MySNDhcpAddressBindEnable_Type())
mySNDhcpAddressBindEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:mySNDhcpAddressBindEnable.setStatus(_A)
_MySNDhcpBindings_ObjectIdentity=ObjectIdentity
mySNDhcpBindings=_MySNDhcpBindings_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,42,1,3))
_MySNDhcpBindingsTable_Object=MibTable
mySNDhcpBindingsTable=_MySNDhcpBindingsTable_Object((1,3,6,1,4,1,171,10,97,2,42,1,3,1))
if mibBuilder.loadTexts:mySNDhcpBindingsTable.setStatus(_A)
_MySNDhcpBindingsEntry_Object=MibTableRow
mySNDhcpBindingsEntry=_MySNDhcpBindingsEntry_Object((1,3,6,1,4,1,171,10,97,2,42,1,3,1,1))
mySNDhcpBindingsEntry.setIndexNames((0,_B,_E),(0,_B,_F),(0,_B,_L))
if mibBuilder.loadTexts:mySNDhcpBindingsEntry.setStatus(_A)
_MySNDhcpBindingsVlan_Type=VlanIndex
_MySNDhcpBindingsVlan_Object=MibTableColumn
mySNDhcpBindingsVlan=_MySNDhcpBindingsVlan_Object((1,3,6,1,4,1,171,10,97,2,42,1,3,1,1,1),_MySNDhcpBindingsVlan_Type())
mySNDhcpBindingsVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:mySNDhcpBindingsVlan.setStatus(_A)
_MySNDhcpBindingsMacAddress_Type=MacAddress
_MySNDhcpBindingsMacAddress_Object=MibTableColumn
mySNDhcpBindingsMacAddress=_MySNDhcpBindingsMacAddress_Object((1,3,6,1,4,1,171,10,97,2,42,1,3,1,1,2),_MySNDhcpBindingsMacAddress_Type())
mySNDhcpBindingsMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:mySNDhcpBindingsMacAddress.setStatus(_A)
class _MySNDhcpBindingsAddrType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dynamic',1),('static',2)))
_MySNDhcpBindingsAddrType_Type.__name__=_G
_MySNDhcpBindingsAddrType_Object=MibTableColumn
mySNDhcpBindingsAddrType=_MySNDhcpBindingsAddrType_Object((1,3,6,1,4,1,171,10,97,2,42,1,3,1,1,3),_MySNDhcpBindingsAddrType_Type())
mySNDhcpBindingsAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:mySNDhcpBindingsAddrType.setStatus(_A)
_MySNDhcpBindingsIpAddress_Type=IpAddress
_MySNDhcpBindingsIpAddress_Object=MibTableColumn
mySNDhcpBindingsIpAddress=_MySNDhcpBindingsIpAddress_Object((1,3,6,1,4,1,171,10,97,2,42,1,3,1,1,4),_MySNDhcpBindingsIpAddress_Type())
mySNDhcpBindingsIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:mySNDhcpBindingsIpAddress.setStatus(_A)
_MySNDhcpBindingsInterface_Type=InterfaceIndex
_MySNDhcpBindingsInterface_Object=MibTableColumn
mySNDhcpBindingsInterface=_MySNDhcpBindingsInterface_Object((1,3,6,1,4,1,171,10,97,2,42,1,3,1,1,5),_MySNDhcpBindingsInterface_Type())
mySNDhcpBindingsInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:mySNDhcpBindingsInterface.setStatus(_A)
_MySNDhcpBindingsLeasedTime_Type=Unsigned32
_MySNDhcpBindingsLeasedTime_Object=MibTableColumn
mySNDhcpBindingsLeasedTime=_MySNDhcpBindingsLeasedTime_Object((1,3,6,1,4,1,171,10,97,2,42,1,3,1,1,6),_MySNDhcpBindingsLeasedTime_Type())
mySNDhcpBindingsLeasedTime.setMaxAccess('read-only')
if mibBuilder.loadTexts:mySNDhcpBindingsLeasedTime.setStatus(_A)
if mibBuilder.loadTexts:mySNDhcpBindingsLeasedTime.setUnits(_H)
_MySNDhcpBindingsStatus_Type=RowStatus
_MySNDhcpBindingsStatus_Object=MibTableColumn
mySNDhcpBindingsStatus=_MySNDhcpBindingsStatus_Object((1,3,6,1,4,1,171,10,97,2,42,1,3,1,1,7),_MySNDhcpBindingsStatus_Type())
mySNDhcpBindingsStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:mySNDhcpBindingsStatus.setStatus(_A)
_MyDhcpSnoopingMIBConformance_ObjectIdentity=ObjectIdentity
myDhcpSnoopingMIBConformance=_MyDhcpSnoopingMIBConformance_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,42,2))
_MyDhcpSnoopingMIBCompliances_ObjectIdentity=ObjectIdentity
myDhcpSnoopingMIBCompliances=_MyDhcpSnoopingMIBCompliances_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,42,2,1))
_MyDhcpSnoopingMIBGroups_ObjectIdentity=ObjectIdentity
myDhcpSnoopingMIBGroups=_MyDhcpSnoopingMIBGroups_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,42,2,2))
myDhcpSnoopingMIBGroup=ObjectGroup((1,3,6,1,4,1,171,10,97,2,42,2,2,1))
myDhcpSnoopingMIBGroup.setObjects(*((_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_E),(_B,_F),(_B,_T),(_B,_U),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:myDhcpSnoopingMIBGroup.setStatus(_A)
myDhcpSnoopingMIBCompliance=ModuleCompliance((1,3,6,1,4,1,171,10,97,2,42,2,1,1))
myDhcpSnoopingMIBCompliance.setObjects((_B,_X))
if mibBuilder.loadTexts:myDhcpSnoopingMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'myDhcpSnoopingMIB':myDhcpSnoopingMIB,'myDhcpSnoopingMIBObjects':myDhcpSnoopingMIBObjects,'mySNDhcpGlobal':mySNDhcpGlobal,_M:mySNDhcpFeatureEnable,_N:mySNDhcpDatabaseUpdateInterval,_O:mySNDhcpRelayAgentInfoOptEnable,_P:mySNDhcpMatchMacAddressEnable,'mySNDhcpInterface':mySNDhcpInterface,'mySNDhcpIfTrustTable':mySNDhcpIfTrustTable,'mySNDhcpIfTrustEntry':mySNDhcpIfTrustEntry,_I:mySNDhcpIfTrustIndex,_Q:mySNDhcpIfTrustEnable,'mySNDhcpIfSuppressionTable':mySNDhcpIfSuppressionTable,'mySNDhcpIfSuppressionEntry':mySNDhcpIfSuppressionEntry,_J:mySNDhcpIfSuppressionIndex,_R:mySNDhcpIfSuppressionEnable,'mySNDhcpAddressBindTable':mySNDhcpAddressBindTable,'mySNDhcpAddressBindEntry':mySNDhcpAddressBindEntry,_K:mySNDhcpAddressBindIndex,_S:mySNDhcpAddressBindEnable,'mySNDhcpBindings':mySNDhcpBindings,'mySNDhcpBindingsTable':mySNDhcpBindingsTable,'mySNDhcpBindingsEntry':mySNDhcpBindingsEntry,_E:mySNDhcpBindingsVlan,_F:mySNDhcpBindingsMacAddress,_L:mySNDhcpBindingsAddrType,_T:mySNDhcpBindingsIpAddress,_U:mySNDhcpBindingsInterface,_V:mySNDhcpBindingsLeasedTime,_W:mySNDhcpBindingsStatus,'myDhcpSnoopingMIBConformance':myDhcpSnoopingMIBConformance,'myDhcpSnoopingMIBCompliances':myDhcpSnoopingMIBCompliances,'myDhcpSnoopingMIBCompliance':myDhcpSnoopingMIBCompliance,'myDhcpSnoopingMIBGroups':myDhcpSnoopingMIBGroups,_X:myDhcpSnoopingMIBGroup})