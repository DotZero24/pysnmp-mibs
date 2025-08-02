_A9='ctAliasInterfaceGroup'
_A8='ctAliasConfigurationGroup2'
_A7='ctAliasConfigurationGroupI'
_A6='ctAliasControlGroupI'
_A5='ctAliasProtocolAddressGroup'
_A4='ctAliasMacAddressGroup'
_A3='ctAliasInterfaceTime'
_A2='ctAliasInterfaceAddressText'
_A1='ctAliasInterfaceIsActive'
_A0='ctAliasInterfaceVlanID'
_z='ctAliasInterfaceAddress'
_y='ctAliasInterfaceProtocol'
_x='ctAliasInterfaceMacAddress'
_w='ctAliasConfigurationProtocolEnableState'
_v='ctAliasConfigurationNumQueueWraps'
_u='ctAliasEntryClearAll'
_t='ctAliasEntryStatus'
_s='ctAliasProtocolAddressTime'
_r='ctAliasProtocolAddressAddressText'
_q='ctAliasProtocolAddressIsActive'
_p='ctAliasProtocolAddressVlanID'
_o='ctAliasProtocolAddressInterface'
_n='ctAliasMacAddressTime'
_m='ctAliasMacAddressAddressText'
_l='ctAliasMacAddressIsActive'
_k='ctAliasMacAddressVlanID'
_j='ctAliasMacAddressInterface'
_i='ctAliasMarkInactive'
_h='ctAliasTableStatsState'
_g='ctAliasTableStatsPurgeTime'
_f='ctAliasTableStatsActiveEntries'
_e='ctAliasTableStatsTotalEntries'
_d='ctAliasAddressText'
_c='ctAliasIsActive'
_b='ctAliasVlanID'
_a='ctAliasID'
_Z='ctAliasTimeFilter'
_Y='netBios'
_X='bootpc'
_W='bootps'
_V='unknown'
_U='EnabledStatus'
_T='ctAliasStatsGroup'
_S='ctAliasBasicGroup'
_R='ctAliasConfigurationInterfaceEnableState'
_Q='ctAliasConfigurationInterfaceMaxEntries'
_P='ctAliasConfigurationInterfaceTotalEntries'
_O='ctAliasConfigurationSystemTotalEntries'
_N='ctAliasConfigurationSystemAllocatedEntries'
_M='deprecated'
_L='not-accessible'
_K='ctAliasGroup'
_J='ctAliasAddress'
_I='ctAliasProtocol'
_H='ctAliasMacAddress'
_G='ctAliasInterface'
_F='ctAliasReference'
_E='Integer32'
_D='read-write'
_C='read-only'
_B='current'
_A='CTRON-ALIAS-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ctAliasMib,=mibBuilder.importSymbols('CTRON-MIB-NAMES','ctAliasMib')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB',_U)
VlanIndex,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanIndex')
TimeFilter,=mibBuilder.importSymbols('RMON2-MIB','TimeFilter')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention','TruthValue')
cabletronAliasMib=ModuleIdentity((1,3,6,1,4,1,52,4,1,3,7,1))
if mibBuilder.loadTexts:cabletronAliasMib.setRevisions(('2013-02-15 14:30','2011-02-14 15:25','2003-04-22 13:39','2002-01-30 13:01','2002-01-23 20:56','2002-01-18 20:22','1999-09-26 00:00','1999-09-04 00:00','1999-08-06 00:00','1999-07-28 00:00'))
class CabletronProtocolTC(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29)));namedValues=NamedValues(*((_V,0),('ip',1),('apl',2),('mac',3),('hsrp',4),('dhcps',5),('dhcpc',6),(_W,7),(_X,8),('ospf',9),('vrrp',10),('ipx',11),('xrip',12),('xsap',13),('xnlsp',14),('ipx20',15),('rtmp',16),(_Y,17),('nbt',18),('n802q',19),('bgp',20),('rip',21),('igrp',22),('dec',23),('bpdu',24),('udp',25),('ipv6',26),('mdns',27),('llmnr',28),('ssdp',29)))
class AliasAddress(TextualConvention,OctetString):status=_B;displayHint='1x ';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
class CabletronProtocolBits(TextualConvention,Bits):status=_B;namedValues=NamedValues(*((_V,0),('ipv4',1),('apl',2),('mac',3),('hsrp',4),('dhcps',5),('dhcpc',6),(_W,7),(_X,8),('ospf',9),('vrrp',10),('ipx',11),('xrip',12),('xsap',13),('xnlsp',14),('ipx20',15),('rtmp',16),(_Y,17),('nbt',18),('n802q',19),('bgp',20),('rip',21),('igrp',22),('dec',23),('bpdu',24),('udp',25),('ipv6',26),('mdns',27),('llmnr',28),('ssdp',29)))
_CtAlias_ObjectIdentity=ObjectIdentity
ctAlias=_CtAlias_ObjectIdentity((1,3,6,1,4,1,52,4,1,3,7,1,1))
_CtAliasTable_Object=MibTable
ctAliasTable=_CtAliasTable_Object((1,3,6,1,4,1,52,4,1,3,7,1,1,1))
if mibBuilder.loadTexts:ctAliasTable.setStatus(_B)
_CtAliasEntry_Object=MibTableRow
ctAliasEntry=_CtAliasEntry_Object((1,3,6,1,4,1,52,4,1,3,7,1,1,1,1))
ctAliasEntry.setIndexNames((0,_A,_Z),(0,_A,_F))
if mibBuilder.loadTexts:ctAliasEntry.setStatus(_B)
_CtAliasTimeFilter_Type=TimeFilter
_CtAliasTimeFilter_Object=MibTableColumn
ctAliasTimeFilter=_CtAliasTimeFilter_Object((1,3,6,1,4,1,52,4,1,3,7,1,1,1,1,1),_CtAliasTimeFilter_Type())
ctAliasTimeFilter.setMaxAccess(_L)
if mibBuilder.loadTexts:ctAliasTimeFilter.setStatus(_B)
class _CtAliasReference_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CtAliasReference_Type.__name__=_E
_CtAliasReference_Object=MibTableColumn
ctAliasReference=_CtAliasReference_Object((1,3,6,1,4,1,52,4,1,3,7,1,1,1,1,2),_CtAliasReference_Type())
ctAliasReference.setMaxAccess(_L)
if mibBuilder.loadTexts:ctAliasReference.setStatus(_B)
_CtAliasInterface_Type=InterfaceIndex
_CtAliasInterface_Object=MibTableColumn
ctAliasInterface=_CtAliasInterface_Object((1,3,6,1,4,1,52,4,1,3,7,1,1,1,1,3),_CtAliasInterface_Type())
ctAliasInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAliasInterface.setStatus(_B)
_CtAliasMacAddress_Type=MacAddress
_CtAliasMacAddress_Object=MibTableColumn
ctAliasMacAddress=_CtAliasMacAddress_Object((1,3,6,1,4,1,52,4,1,3,7,1,1,1,1,4),_CtAliasMacAddress_Type())
ctAliasMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAliasMacAddress.setStatus(_B)
_CtAliasVlanID_Type=VlanIndex
_CtAliasVlanID_Object=MibTableColumn
ctAliasVlanID=_CtAliasVlanID_Object((1,3,6,1,4,1,52,4,1,3,7,1,1,1,1,5),_CtAliasVlanID_Type())
ctAliasVlanID.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAliasVlanID.setStatus(_B)
_CtAliasProtocol_Type=CabletronProtocolTC
_CtAliasProtocol_Object=MibTableColumn
ctAliasProtocol=_CtAliasProtocol_Object((1,3,6,1,4,1,52,4,1,3,7,1,1,1,1,6),_CtAliasProtocol_Type())
ctAliasProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAliasProtocol.setStatus(_B)
_CtAliasAddress_Type=AliasAddress
_CtAliasAddress_Object=MibTableColumn
ctAliasAddress=_CtAliasAddress_Object((1,3,6,1,4,1,52,4,1,3,7,1,1,1,1,7),_CtAliasAddress_Type())
ctAliasAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAliasAddress.setStatus(_B)
_CtAliasIsActive_Type=TruthValue
_CtAliasIsActive_Object=MibTableColumn
ctAliasIsActive=_CtAliasIsActive_Object((1,3,6,1,4,1,52,4,1,3,7,1,1,1,1,8),_CtAliasIsActive_Type())
ctAliasIsActive.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAliasIsActive.setStatus(_B)
_CtAliasAddressText_Type=SnmpAdminString
_CtAliasAddressText_Object=MibTableColumn
ctAliasAddressText=_CtAliasAddressText_Object((1,3,6,1,4,1,52,4,1,3,7,1,1,1,1,9),_CtAliasAddressText_Type())
ctAliasAddressText.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAliasAddressText.setStatus(_B)
_CtAliasControlTable_Object=MibTable
ctAliasControlTable=_CtAliasControlTable_Object((1,3,6,1,4,1,52,4,1,3,7,1,1,2))
if mibBuilder.loadTexts:ctAliasControlTable.setStatus(_B)
_CtAliasControlEntry_Object=MibTableRow
ctAliasControlEntry=_CtAliasControlEntry_Object((1,3,6,1,4,1,52,4,1,3,7,1,1,2,1))
ctAliasControlEntry.setIndexNames((0,_A,_a))
if mibBuilder.loadTexts:ctAliasControlEntry.setStatus(_B)
class _CtAliasID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CtAliasID_Type.__name__=_E
_CtAliasID_Object=MibTableColumn
ctAliasID=_CtAliasID_Object((1,3,6,1,4,1,52,4,1,3,7,1,1,2,1,1),_CtAliasID_Type())
ctAliasID.setMaxAccess(_L)
if mibBuilder.loadTexts:ctAliasID.setStatus(_B)
_CtAliasMarkInactive_Type=TruthValue
_CtAliasMarkInactive_Object=MibTableColumn
ctAliasMarkInactive=_CtAliasMarkInactive_Object((1,3,6,1,4,1,52,4,1,3,7,1,1,2,1,2),_CtAliasMarkInactive_Type())
ctAliasMarkInactive.setMaxAccess(_D)
if mibBuilder.loadTexts:ctAliasMarkInactive.setStatus(_M)
class _CtAliasEntryStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('active',1),('inactive',2),('remove',3)))
_CtAliasEntryStatus_Type.__name__=_E
_CtAliasEntryStatus_Object=MibTableColumn
ctAliasEntryStatus=_CtAliasEntryStatus_Object((1,3,6,1,4,1,52,4,1,3,7,1,1,2,1,3),_CtAliasEntryStatus_Type())
ctAliasEntryStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ctAliasEntryStatus.setStatus(_B)
_CtAliasStats_ObjectIdentity=ObjectIdentity
ctAliasStats=_CtAliasStats_ObjectIdentity((1,3,6,1,4,1,52,4,1,3,7,1,1,3))
_CtAliasTableStatsTotalEntries_Type=Gauge32
_CtAliasTableStatsTotalEntries_Object=MibScalar
ctAliasTableStatsTotalEntries=_CtAliasTableStatsTotalEntries_Object((1,3,6,1,4,1,52,4,1,3,7,1,1,3,1),_CtAliasTableStatsTotalEntries_Type())
ctAliasTableStatsTotalEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAliasTableStatsTotalEntries.setStatus(_B)
_CtAliasTableStatsActiveEntries_Type=Gauge32
_CtAliasTableStatsActiveEntries_Object=MibScalar
ctAliasTableStatsActiveEntries=_CtAliasTableStatsActiveEntries_Object((1,3,6,1,4,1,52,4,1,3,7,1,1,3,2),_CtAliasTableStatsActiveEntries_Type())
ctAliasTableStatsActiveEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAliasTableStatsActiveEntries.setStatus(_B)
_CtAliasTableStatsPurgeTime_Type=TimeTicks
_CtAliasTableStatsPurgeTime_Object=MibScalar
ctAliasTableStatsPurgeTime=_CtAliasTableStatsPurgeTime_Object((1,3,6,1,4,1,52,4,1,3,7,1,1,3,3),_CtAliasTableStatsPurgeTime_Type())
ctAliasTableStatsPurgeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAliasTableStatsPurgeTime.setStatus(_B)
class _CtAliasTableStatsState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notStarted',1),('ready',2),('full',3)))
_CtAliasTableStatsState_Type.__name__=_E
_CtAliasTableStatsState_Object=MibScalar
ctAliasTableStatsState=_CtAliasTableStatsState_Object((1,3,6,1,4,1,52,4,1,3,7,1,1,3,4),_CtAliasTableStatsState_Type())
ctAliasTableStatsState.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAliasTableStatsState.setStatus(_B)
_CtAliasConfiguration_ObjectIdentity=ObjectIdentity
ctAliasConfiguration=_CtAliasConfiguration_ObjectIdentity((1,3,6,1,4,1,52,4,1,3,7,1,1,4))
_CtAliasConfigurationSystemAllocatedEntries_Type=Gauge32
_CtAliasConfigurationSystemAllocatedEntries_Object=MibScalar
ctAliasConfigurationSystemAllocatedEntries=_CtAliasConfigurationSystemAllocatedEntries_Object((1,3,6,1,4,1,52,4,1,3,7,1,1,4,1),_CtAliasConfigurationSystemAllocatedEntries_Type())
ctAliasConfigurationSystemAllocatedEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAliasConfigurationSystemAllocatedEntries.setStatus(_B)
_CtAliasConfigurationSystemTotalEntries_Type=Gauge32
_CtAliasConfigurationSystemTotalEntries_Object=MibScalar
ctAliasConfigurationSystemTotalEntries=_CtAliasConfigurationSystemTotalEntries_Object((1,3,6,1,4,1,52,4,1,3,7,1,1,4,2),_CtAliasConfigurationSystemTotalEntries_Type())
ctAliasConfigurationSystemTotalEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAliasConfigurationSystemTotalEntries.setStatus(_B)
_CtAliasConfigurationTable_Object=MibTable
ctAliasConfigurationTable=_CtAliasConfigurationTable_Object((1,3,6,1,4,1,52,4,1,3,7,1,1,4,3))
if mibBuilder.loadTexts:ctAliasConfigurationTable.setStatus(_B)
_CtAliasConfigurationEntry_Object=MibTableRow
ctAliasConfigurationEntry=_CtAliasConfigurationEntry_Object((1,3,6,1,4,1,52,4,1,3,7,1,1,4,3,1))
ctAliasConfigurationEntry.setIndexNames((0,_A,_G))
if mibBuilder.loadTexts:ctAliasConfigurationEntry.setStatus(_B)
_CtAliasConfigurationInterfaceTotalEntries_Type=Gauge32
_CtAliasConfigurationInterfaceTotalEntries_Object=MibTableColumn
ctAliasConfigurationInterfaceTotalEntries=_CtAliasConfigurationInterfaceTotalEntries_Object((1,3,6,1,4,1,52,4,1,3,7,1,1,4,3,1,1),_CtAliasConfigurationInterfaceTotalEntries_Type())
ctAliasConfigurationInterfaceTotalEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAliasConfigurationInterfaceTotalEntries.setStatus(_B)
_CtAliasConfigurationInterfaceMaxEntries_Type=Gauge32
_CtAliasConfigurationInterfaceMaxEntries_Object=MibTableColumn
ctAliasConfigurationInterfaceMaxEntries=_CtAliasConfigurationInterfaceMaxEntries_Object((1,3,6,1,4,1,52,4,1,3,7,1,1,4,3,1,2),_CtAliasConfigurationInterfaceMaxEntries_Type())
ctAliasConfigurationInterfaceMaxEntries.setMaxAccess(_D)
if mibBuilder.loadTexts:ctAliasConfigurationInterfaceMaxEntries.setStatus(_B)
class _CtAliasConfigurationInterfaceEnableState_Type(EnabledStatus):defaultValue=1
_CtAliasConfigurationInterfaceEnableState_Type.__name__=_U
_CtAliasConfigurationInterfaceEnableState_Object=MibTableColumn
ctAliasConfigurationInterfaceEnableState=_CtAliasConfigurationInterfaceEnableState_Object((1,3,6,1,4,1,52,4,1,3,7,1,1,4,3,1,3),_CtAliasConfigurationInterfaceEnableState_Type())
ctAliasConfigurationInterfaceEnableState.setMaxAccess(_D)
if mibBuilder.loadTexts:ctAliasConfigurationInterfaceEnableState.setStatus(_B)
_CtAliasConfigurationNumQueueWraps_Type=Counter32
_CtAliasConfigurationNumQueueWraps_Object=MibTableColumn
ctAliasConfigurationNumQueueWraps=_CtAliasConfigurationNumQueueWraps_Object((1,3,6,1,4,1,52,4,1,3,7,1,1,4,3,1,4),_CtAliasConfigurationNumQueueWraps_Type())
ctAliasConfigurationNumQueueWraps.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAliasConfigurationNumQueueWraps.setStatus(_B)
_CtAliasConfigurationProtocolEnableState_Type=CabletronProtocolBits
_CtAliasConfigurationProtocolEnableState_Object=MibScalar
ctAliasConfigurationProtocolEnableState=_CtAliasConfigurationProtocolEnableState_Object((1,3,6,1,4,1,52,4,1,3,7,1,1,4,4),_CtAliasConfigurationProtocolEnableState_Type())
ctAliasConfigurationProtocolEnableState.setMaxAccess(_D)
if mibBuilder.loadTexts:ctAliasConfigurationProtocolEnableState.setStatus(_B)
_CtAliasMacAddressTable_Object=MibTable
ctAliasMacAddressTable=_CtAliasMacAddressTable_Object((1,3,6,1,4,1,52,4,1,3,7,1,1,5))
if mibBuilder.loadTexts:ctAliasMacAddressTable.setStatus(_B)
_CtAliasMacAddressEntry_Object=MibTableRow
ctAliasMacAddressEntry=_CtAliasMacAddressEntry_Object((1,3,6,1,4,1,52,4,1,3,7,1,1,5,1))
ctAliasMacAddressEntry.setIndexNames((0,_A,_H),(0,_A,_I),(0,_A,_J),(0,_A,_F))
if mibBuilder.loadTexts:ctAliasMacAddressEntry.setStatus(_B)
_CtAliasMacAddressInterface_Type=InterfaceIndex
_CtAliasMacAddressInterface_Object=MibTableColumn
ctAliasMacAddressInterface=_CtAliasMacAddressInterface_Object((1,3,6,1,4,1,52,4,1,3,7,1,1,5,1,1),_CtAliasMacAddressInterface_Type())
ctAliasMacAddressInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAliasMacAddressInterface.setStatus(_B)
_CtAliasMacAddressVlanID_Type=VlanIndex
_CtAliasMacAddressVlanID_Object=MibTableColumn
ctAliasMacAddressVlanID=_CtAliasMacAddressVlanID_Object((1,3,6,1,4,1,52,4,1,3,7,1,1,5,1,2),_CtAliasMacAddressVlanID_Type())
ctAliasMacAddressVlanID.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAliasMacAddressVlanID.setStatus(_B)
_CtAliasMacAddressIsActive_Type=TruthValue
_CtAliasMacAddressIsActive_Object=MibTableColumn
ctAliasMacAddressIsActive=_CtAliasMacAddressIsActive_Object((1,3,6,1,4,1,52,4,1,3,7,1,1,5,1,3),_CtAliasMacAddressIsActive_Type())
ctAliasMacAddressIsActive.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAliasMacAddressIsActive.setStatus(_B)
_CtAliasMacAddressAddressText_Type=SnmpAdminString
_CtAliasMacAddressAddressText_Object=MibTableColumn
ctAliasMacAddressAddressText=_CtAliasMacAddressAddressText_Object((1,3,6,1,4,1,52,4,1,3,7,1,1,5,1,4),_CtAliasMacAddressAddressText_Type())
ctAliasMacAddressAddressText.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAliasMacAddressAddressText.setStatus(_B)
_CtAliasMacAddressTime_Type=TimeTicks
_CtAliasMacAddressTime_Object=MibTableColumn
ctAliasMacAddressTime=_CtAliasMacAddressTime_Object((1,3,6,1,4,1,52,4,1,3,7,1,1,5,1,5),_CtAliasMacAddressTime_Type())
ctAliasMacAddressTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAliasMacAddressTime.setStatus(_B)
_CtAliasProtocolAddressTable_Object=MibTable
ctAliasProtocolAddressTable=_CtAliasProtocolAddressTable_Object((1,3,6,1,4,1,52,4,1,3,7,1,1,6))
if mibBuilder.loadTexts:ctAliasProtocolAddressTable.setStatus(_B)
_CtAliasProtocolAddressEntry_Object=MibTableRow
ctAliasProtocolAddressEntry=_CtAliasProtocolAddressEntry_Object((1,3,6,1,4,1,52,4,1,3,7,1,1,6,1))
ctAliasProtocolAddressEntry.setIndexNames((0,_A,_I),(0,_A,_J),(0,_A,_H),(0,_A,_F))
if mibBuilder.loadTexts:ctAliasProtocolAddressEntry.setStatus(_B)
_CtAliasProtocolAddressInterface_Type=InterfaceIndex
_CtAliasProtocolAddressInterface_Object=MibTableColumn
ctAliasProtocolAddressInterface=_CtAliasProtocolAddressInterface_Object((1,3,6,1,4,1,52,4,1,3,7,1,1,6,1,1),_CtAliasProtocolAddressInterface_Type())
ctAliasProtocolAddressInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAliasProtocolAddressInterface.setStatus(_B)
_CtAliasProtocolAddressVlanID_Type=VlanIndex
_CtAliasProtocolAddressVlanID_Object=MibTableColumn
ctAliasProtocolAddressVlanID=_CtAliasProtocolAddressVlanID_Object((1,3,6,1,4,1,52,4,1,3,7,1,1,6,1,2),_CtAliasProtocolAddressVlanID_Type())
ctAliasProtocolAddressVlanID.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAliasProtocolAddressVlanID.setStatus(_B)
_CtAliasProtocolAddressIsActive_Type=TruthValue
_CtAliasProtocolAddressIsActive_Object=MibTableColumn
ctAliasProtocolAddressIsActive=_CtAliasProtocolAddressIsActive_Object((1,3,6,1,4,1,52,4,1,3,7,1,1,6,1,3),_CtAliasProtocolAddressIsActive_Type())
ctAliasProtocolAddressIsActive.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAliasProtocolAddressIsActive.setStatus(_B)
_CtAliasProtocolAddressAddressText_Type=SnmpAdminString
_CtAliasProtocolAddressAddressText_Object=MibTableColumn
ctAliasProtocolAddressAddressText=_CtAliasProtocolAddressAddressText_Object((1,3,6,1,4,1,52,4,1,3,7,1,1,6,1,4),_CtAliasProtocolAddressAddressText_Type())
ctAliasProtocolAddressAddressText.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAliasProtocolAddressAddressText.setStatus(_B)
_CtAliasProtocolAddressTime_Type=TimeTicks
_CtAliasProtocolAddressTime_Object=MibTableColumn
ctAliasProtocolAddressTime=_CtAliasProtocolAddressTime_Object((1,3,6,1,4,1,52,4,1,3,7,1,1,6,1,5),_CtAliasProtocolAddressTime_Type())
ctAliasProtocolAddressTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAliasProtocolAddressTime.setStatus(_B)
_CtAliasEntryClearAll_Type=TruthValue
_CtAliasEntryClearAll_Object=MibScalar
ctAliasEntryClearAll=_CtAliasEntryClearAll_Object((1,3,6,1,4,1,52,4,1,3,7,1,1,7),_CtAliasEntryClearAll_Type())
ctAliasEntryClearAll.setMaxAccess(_D)
if mibBuilder.loadTexts:ctAliasEntryClearAll.setStatus(_B)
_CtAliasInterfaceTable_Object=MibTable
ctAliasInterfaceTable=_CtAliasInterfaceTable_Object((1,3,6,1,4,1,52,4,1,3,7,1,1,8))
if mibBuilder.loadTexts:ctAliasInterfaceTable.setStatus(_B)
_CtAliasInterfaceEntry_Object=MibTableRow
ctAliasInterfaceEntry=_CtAliasInterfaceEntry_Object((1,3,6,1,4,1,52,4,1,3,7,1,1,8,1))
ctAliasInterfaceEntry.setIndexNames((0,_A,_G),(0,_A,_F))
if mibBuilder.loadTexts:ctAliasInterfaceEntry.setStatus(_B)
_CtAliasInterfaceMacAddress_Type=MacAddress
_CtAliasInterfaceMacAddress_Object=MibTableColumn
ctAliasInterfaceMacAddress=_CtAliasInterfaceMacAddress_Object((1,3,6,1,4,1,52,4,1,3,7,1,1,8,1,1),_CtAliasInterfaceMacAddress_Type())
ctAliasInterfaceMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAliasInterfaceMacAddress.setStatus(_B)
_CtAliasInterfaceProtocol_Type=CabletronProtocolTC
_CtAliasInterfaceProtocol_Object=MibTableColumn
ctAliasInterfaceProtocol=_CtAliasInterfaceProtocol_Object((1,3,6,1,4,1,52,4,1,3,7,1,1,8,1,2),_CtAliasInterfaceProtocol_Type())
ctAliasInterfaceProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAliasInterfaceProtocol.setStatus(_B)
_CtAliasInterfaceAddress_Type=AliasAddress
_CtAliasInterfaceAddress_Object=MibTableColumn
ctAliasInterfaceAddress=_CtAliasInterfaceAddress_Object((1,3,6,1,4,1,52,4,1,3,7,1,1,8,1,3),_CtAliasInterfaceAddress_Type())
ctAliasInterfaceAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAliasInterfaceAddress.setStatus(_B)
_CtAliasInterfaceVlanID_Type=VlanIndex
_CtAliasInterfaceVlanID_Object=MibTableColumn
ctAliasInterfaceVlanID=_CtAliasInterfaceVlanID_Object((1,3,6,1,4,1,52,4,1,3,7,1,1,8,1,4),_CtAliasInterfaceVlanID_Type())
ctAliasInterfaceVlanID.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAliasInterfaceVlanID.setStatus(_B)
_CtAliasInterfaceIsActive_Type=TruthValue
_CtAliasInterfaceIsActive_Object=MibTableColumn
ctAliasInterfaceIsActive=_CtAliasInterfaceIsActive_Object((1,3,6,1,4,1,52,4,1,3,7,1,1,8,1,5),_CtAliasInterfaceIsActive_Type())
ctAliasInterfaceIsActive.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAliasInterfaceIsActive.setStatus(_B)
_CtAliasInterfaceAddressText_Type=SnmpAdminString
_CtAliasInterfaceAddressText_Object=MibTableColumn
ctAliasInterfaceAddressText=_CtAliasInterfaceAddressText_Object((1,3,6,1,4,1,52,4,1,3,7,1,1,8,1,6),_CtAliasInterfaceAddressText_Type())
ctAliasInterfaceAddressText.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAliasInterfaceAddressText.setStatus(_B)
_CtAliasInterfaceTime_Type=TimeTicks
_CtAliasInterfaceTime_Object=MibTableColumn
ctAliasInterfaceTime=_CtAliasInterfaceTime_Object((1,3,6,1,4,1,52,4,1,3,7,1,1,8,1,7),_CtAliasInterfaceTime_Type())
ctAliasInterfaceTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAliasInterfaceTime.setStatus(_B)
_CtAliasConformance_ObjectIdentity=ObjectIdentity
ctAliasConformance=_CtAliasConformance_ObjectIdentity((1,3,6,1,4,1,52,4,1,3,7,2))
_CtAliasGroups_ObjectIdentity=ObjectIdentity
ctAliasGroups=_CtAliasGroups_ObjectIdentity((1,3,6,1,4,1,52,4,1,3,7,2,1))
_CtAliasCompliances_ObjectIdentity=ObjectIdentity
ctAliasCompliances=_CtAliasCompliances_ObjectIdentity((1,3,6,1,4,1,52,4,1,3,7,2,2))
ctAliasBasicGroup=ObjectGroup((1,3,6,1,4,1,52,4,1,3,7,2,1,1))
ctAliasBasicGroup.setObjects(*((_A,_G),(_A,_H),(_A,_b),(_A,_I),(_A,_J),(_A,_c),(_A,_d)))
if mibBuilder.loadTexts:ctAliasBasicGroup.setStatus(_B)
ctAliasStatsGroup=ObjectGroup((1,3,6,1,4,1,52,4,1,3,7,2,1,2))
ctAliasStatsGroup.setObjects(*((_A,_e),(_A,_f),(_A,_g),(_A,_h)))
if mibBuilder.loadTexts:ctAliasStatsGroup.setStatus(_B)
ctAliasControlGroup=ObjectGroup((1,3,6,1,4,1,52,4,1,3,7,2,1,3))
ctAliasControlGroup.setObjects((_A,_i))
if mibBuilder.loadTexts:ctAliasControlGroup.setStatus(_M)
ctAliasConfigurationGroup=ObjectGroup((1,3,6,1,4,1,52,4,1,3,7,2,1,4))
ctAliasConfigurationGroup.setObjects(*((_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:ctAliasConfigurationGroup.setStatus(_M)
ctAliasMacAddressGroup=ObjectGroup((1,3,6,1,4,1,52,4,1,3,7,2,1,5))
ctAliasMacAddressGroup.setObjects(*((_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n)))
if mibBuilder.loadTexts:ctAliasMacAddressGroup.setStatus(_B)
ctAliasProtocolAddressGroup=ObjectGroup((1,3,6,1,4,1,52,4,1,3,7,2,1,6))
ctAliasProtocolAddressGroup.setObjects(*((_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s)))
if mibBuilder.loadTexts:ctAliasProtocolAddressGroup.setStatus(_B)
ctAliasControlGroupI=ObjectGroup((1,3,6,1,4,1,52,4,1,3,7,2,1,7))
ctAliasControlGroupI.setObjects((_A,_t))
if mibBuilder.loadTexts:ctAliasControlGroupI.setStatus(_B)
ctAliasGroup=ObjectGroup((1,3,6,1,4,1,52,4,1,3,7,2,1,8))
ctAliasGroup.setObjects((_A,_u))
if mibBuilder.loadTexts:ctAliasGroup.setStatus(_B)
ctAliasConfigurationGroupI=ObjectGroup((1,3,6,1,4,1,52,4,1,3,7,2,1,9))
ctAliasConfigurationGroupI.setObjects((_A,_v))
if mibBuilder.loadTexts:ctAliasConfigurationGroupI.setStatus(_B)
ctAliasConfigurationGroup2=ObjectGroup((1,3,6,1,4,1,52,4,1,3,7,2,1,10))
ctAliasConfigurationGroup2.setObjects(*((_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_w)))
if mibBuilder.loadTexts:ctAliasConfigurationGroup2.setStatus(_B)
ctAliasInterfaceGroup=ObjectGroup((1,3,6,1,4,1,52,4,1,3,7,2,1,11))
ctAliasInterfaceGroup.setObjects(*((_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3)))
if mibBuilder.loadTexts:ctAliasInterfaceGroup.setStatus(_B)
ctAliasCompliance=ModuleCompliance((1,3,6,1,4,1,52,4,1,3,7,2,2,1))
ctAliasCompliance.setObjects(*((_A,_S),(_A,_T),(_A,_K)))
if mibBuilder.loadTexts:ctAliasCompliance.setStatus(_B)
ctAliasCompliance2=ModuleCompliance((1,3,6,1,4,1,52,4,1,3,7,2,2,2))
ctAliasCompliance2.setObjects(*((_A,_S),(_A,_T),(_A,_K),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_K),(_A,_A7),(_A,_A8),(_A,_A9)))
if mibBuilder.loadTexts:ctAliasCompliance2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'CabletronProtocolTC':CabletronProtocolTC,'AliasAddress':AliasAddress,'CabletronProtocolBits':CabletronProtocolBits,'cabletronAliasMib':cabletronAliasMib,'ctAlias':ctAlias,'ctAliasTable':ctAliasTable,'ctAliasEntry':ctAliasEntry,_Z:ctAliasTimeFilter,_F:ctAliasReference,_G:ctAliasInterface,_H:ctAliasMacAddress,_b:ctAliasVlanID,_I:ctAliasProtocol,_J:ctAliasAddress,_c:ctAliasIsActive,_d:ctAliasAddressText,'ctAliasControlTable':ctAliasControlTable,'ctAliasControlEntry':ctAliasControlEntry,_a:ctAliasID,_i:ctAliasMarkInactive,_t:ctAliasEntryStatus,'ctAliasStats':ctAliasStats,_e:ctAliasTableStatsTotalEntries,_f:ctAliasTableStatsActiveEntries,_g:ctAliasTableStatsPurgeTime,_h:ctAliasTableStatsState,'ctAliasConfiguration':ctAliasConfiguration,_N:ctAliasConfigurationSystemAllocatedEntries,_O:ctAliasConfigurationSystemTotalEntries,'ctAliasConfigurationTable':ctAliasConfigurationTable,'ctAliasConfigurationEntry':ctAliasConfigurationEntry,_P:ctAliasConfigurationInterfaceTotalEntries,_Q:ctAliasConfigurationInterfaceMaxEntries,_R:ctAliasConfigurationInterfaceEnableState,_v:ctAliasConfigurationNumQueueWraps,_w:ctAliasConfigurationProtocolEnableState,'ctAliasMacAddressTable':ctAliasMacAddressTable,'ctAliasMacAddressEntry':ctAliasMacAddressEntry,_j:ctAliasMacAddressInterface,_k:ctAliasMacAddressVlanID,_l:ctAliasMacAddressIsActive,_m:ctAliasMacAddressAddressText,_n:ctAliasMacAddressTime,'ctAliasProtocolAddressTable':ctAliasProtocolAddressTable,'ctAliasProtocolAddressEntry':ctAliasProtocolAddressEntry,_o:ctAliasProtocolAddressInterface,_p:ctAliasProtocolAddressVlanID,_q:ctAliasProtocolAddressIsActive,_r:ctAliasProtocolAddressAddressText,_s:ctAliasProtocolAddressTime,_u:ctAliasEntryClearAll,'ctAliasInterfaceTable':ctAliasInterfaceTable,'ctAliasInterfaceEntry':ctAliasInterfaceEntry,_x:ctAliasInterfaceMacAddress,_y:ctAliasInterfaceProtocol,_z:ctAliasInterfaceAddress,_A0:ctAliasInterfaceVlanID,_A1:ctAliasInterfaceIsActive,_A2:ctAliasInterfaceAddressText,_A3:ctAliasInterfaceTime,'ctAliasConformance':ctAliasConformance,'ctAliasGroups':ctAliasGroups,_S:ctAliasBasicGroup,_T:ctAliasStatsGroup,'ctAliasControlGroup':ctAliasControlGroup,'ctAliasConfigurationGroup':ctAliasConfigurationGroup,_A4:ctAliasMacAddressGroup,_A5:ctAliasProtocolAddressGroup,_A6:ctAliasControlGroupI,_K:ctAliasGroup,_A7:ctAliasConfigurationGroupI,_A8:ctAliasConfigurationGroup2,_A9:ctAliasInterfaceGroup,'ctAliasCompliances':ctAliasCompliances,'ctAliasCompliance':ctAliasCompliance,'ctAliasCompliance2':ctAliasCompliance2})