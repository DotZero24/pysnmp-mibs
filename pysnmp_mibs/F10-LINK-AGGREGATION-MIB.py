_A3='f10LinkAggNotificationGroup'
_A2='f10LinkAggPortGroup'
_A1='f10LinkAggCommonGroupRev1'
_A0='f10LinkAggCommonGroup'
_z='linkBundleImbalanceClear'
_y='linkBundleImbalance'
_x='dot3adAggLacpStateChange'
_w='dot3adAggPortPartnerAdminState'
_v='dot3adAggPortActorAdminState'
_u='dot3adAggPortPartnerOperKey'
_t='dot3adAggPortActorOperKey'
_s='dot3aAggFdbDistributedPort'
_r='dot3aAggFdbStatus'
_q='dot3aAggDistributedPort'
_p='dot3aAggStatus'
_o='dot3aAggCfgPortList'
_n='accessible-for-notify'
_m='dot3adAggPortIndex'
_l='dot3aCommonAggFdbVlanId'
_k='dot3aCommonAggFdbIndex'
_j='dot3aCurAggFdbIndex'
_i='dot3aCurAggFdbMacAddr'
_h='dot3aCurAggFdbVlanId'
_g='dot3aCurAggIndex'
_f='dot3aCurAggMacAddr'
_e='dot3aCurAggVlanId'
_d='dot3aAggFdbMacAddr'
_c='dot3aAggFdbVlanId'
_b='dot3aAggFdbIndex'
_a='dot3aAggMacAddr'
_Z='dot3aAggVlanId'
_Y='dot3aAggIndex'
_X='dot3aAggCfgId'
_W='dot3adAggPortPartnerOperState'
_V='dot3adAggPortActorOperState'
_U='dot3aClearFdb'
_T='dot3aCommonAggFdbStatus'
_S='dot3aCommonAggFdbTagConfig'
_R='dot3aCurAggFdbStatus'
_Q='dot3aCurAggStatus'
_P='dot3aAggCfgOperStatus'
_O='dot3aAggCfgLacpSupported'
_N='dot3aAggCfgPortListString'
_M='dot3aAggCfgNumPorts'
_L='dot3aAggCfgIfIndex'
_K='dot3aAggCfgMacAddr'
_J='linkBundleNumber'
_I='linkBundleType'
_H='inactive'
_G='active'
_F='Integer32'
_E='deprecated'
_D='not-accessible'
_C='read-only'
_B='current'
_A='F10-LINK-AGGREGATION-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
f10Mgmt,=mibBuilder.importSymbols('FORCE10-SMI','f10Mgmt')
PortList,=mibBuilder.importSymbols('FORCE10-TC','PortList')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention','TruthValue')
f10LinkAggMib=ModuleIdentity((1,3,6,1,4,1,6027,3,2))
if mibBuilder.loadTexts:f10LinkAggMib.setRevisions(('2013-04-16 00:00','2012-11-26 00:00','2011-07-04 00:00','2003-08-01 00:00','2002-03-12 00:00','2001-03-01 00:00','2000-11-21 00:00'))
class F10LacpKey(TextualConvention,Unsigned32):status=_B;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
class F10LacpState(TextualConvention,Bits):status=_B;namedValues=NamedValues(*(('lacpActivity',0),('lacpTimeout',1),('aggregation',2),('synchronization',3),('collecting',4),('distributing',5),('defaulted',6),('expired',7)))
_F10LinkAggObjects_ObjectIdentity=ObjectIdentity
f10LinkAggObjects=_F10LinkAggObjects_ObjectIdentity((1,3,6,1,4,1,6027,3,2,1))
_F10dot3dAgg_ObjectIdentity=ObjectIdentity
f10dot3dAgg=_F10dot3dAgg_ObjectIdentity((1,3,6,1,4,1,6027,3,2,1,1))
_Dot3aAggConfigTable_Object=MibTable
dot3aAggConfigTable=_Dot3aAggConfigTable_Object((1,3,6,1,4,1,6027,3,2,1,1,1))
if mibBuilder.loadTexts:dot3aAggConfigTable.setStatus(_B)
_Dot3aAggConfigEntry_Object=MibTableRow
dot3aAggConfigEntry=_Dot3aAggConfigEntry_Object((1,3,6,1,4,1,6027,3,2,1,1,1,1))
dot3aAggConfigEntry.setIndexNames((0,_A,_X))
if mibBuilder.loadTexts:dot3aAggConfigEntry.setStatus(_B)
_Dot3aAggCfgId_Type=Unsigned32
_Dot3aAggCfgId_Object=MibTableColumn
dot3aAggCfgId=_Dot3aAggCfgId_Object((1,3,6,1,4,1,6027,3,2,1,1,1,1,1),_Dot3aAggCfgId_Type())
dot3aAggCfgId.setMaxAccess(_D)
if mibBuilder.loadTexts:dot3aAggCfgId.setStatus(_B)
_Dot3aAggCfgMacAddr_Type=MacAddress
_Dot3aAggCfgMacAddr_Object=MibTableColumn
dot3aAggCfgMacAddr=_Dot3aAggCfgMacAddr_Object((1,3,6,1,4,1,6027,3,2,1,1,1,1,2),_Dot3aAggCfgMacAddr_Type())
dot3aAggCfgMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3aAggCfgMacAddr.setStatus(_B)
_Dot3aAggCfgIfIndex_Type=Unsigned32
_Dot3aAggCfgIfIndex_Object=MibTableColumn
dot3aAggCfgIfIndex=_Dot3aAggCfgIfIndex_Object((1,3,6,1,4,1,6027,3,2,1,1,1,1,3),_Dot3aAggCfgIfIndex_Type())
dot3aAggCfgIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3aAggCfgIfIndex.setStatus(_B)
_Dot3aAggCfgNumPorts_Type=Unsigned32
_Dot3aAggCfgNumPorts_Object=MibTableColumn
dot3aAggCfgNumPorts=_Dot3aAggCfgNumPorts_Object((1,3,6,1,4,1,6027,3,2,1,1,1,1,4),_Dot3aAggCfgNumPorts_Type())
dot3aAggCfgNumPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3aAggCfgNumPorts.setStatus(_B)
_Dot3aAggCfgPortList_Type=PortList
_Dot3aAggCfgPortList_Object=MibTableColumn
dot3aAggCfgPortList=_Dot3aAggCfgPortList_Object((1,3,6,1,4,1,6027,3,2,1,1,1,1,5),_Dot3aAggCfgPortList_Type())
dot3aAggCfgPortList.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3aAggCfgPortList.setStatus(_E)
_Dot3aAggCfgPortListString_Type=OctetString
_Dot3aAggCfgPortListString_Object=MibTableColumn
dot3aAggCfgPortListString=_Dot3aAggCfgPortListString_Object((1,3,6,1,4,1,6027,3,2,1,1,1,1,6),_Dot3aAggCfgPortListString_Type())
dot3aAggCfgPortListString.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3aAggCfgPortListString.setStatus(_B)
_Dot3aAggCfgLacpSupported_Type=TruthValue
_Dot3aAggCfgLacpSupported_Object=MibTableColumn
dot3aAggCfgLacpSupported=_Dot3aAggCfgLacpSupported_Object((1,3,6,1,4,1,6027,3,2,1,1,1,1,7),_Dot3aAggCfgLacpSupported_Type())
dot3aAggCfgLacpSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3aAggCfgLacpSupported.setStatus(_B)
class _Dot3aAggCfgOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_Dot3aAggCfgOperStatus_Type.__name__=_F
_Dot3aAggCfgOperStatus_Object=MibTableColumn
dot3aAggCfgOperStatus=_Dot3aAggCfgOperStatus_Object((1,3,6,1,4,1,6027,3,2,1,1,1,1,8),_Dot3aAggCfgOperStatus_Type())
dot3aAggCfgOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3aAggCfgOperStatus.setStatus(_B)
_Dot3aAggStaticTable_Object=MibTable
dot3aAggStaticTable=_Dot3aAggStaticTable_Object((1,3,6,1,4,1,6027,3,2,1,1,2))
if mibBuilder.loadTexts:dot3aAggStaticTable.setStatus(_B)
_Dot3aAggStaticEntry_Object=MibTableRow
dot3aAggStaticEntry=_Dot3aAggStaticEntry_Object((1,3,6,1,4,1,6027,3,2,1,1,2,1))
dot3aAggStaticEntry.setIndexNames((0,_A,_Y),(0,_A,_Z),(0,_A,_a))
if mibBuilder.loadTexts:dot3aAggStaticEntry.setStatus(_E)
_Dot3aAggIndex_Type=Unsigned32
_Dot3aAggIndex_Object=MibTableColumn
dot3aAggIndex=_Dot3aAggIndex_Object((1,3,6,1,4,1,6027,3,2,1,1,2,1,1),_Dot3aAggIndex_Type())
dot3aAggIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:dot3aAggIndex.setStatus(_E)
_Dot3aAggVlanId_Type=Unsigned32
_Dot3aAggVlanId_Object=MibTableColumn
dot3aAggVlanId=_Dot3aAggVlanId_Object((1,3,6,1,4,1,6027,3,2,1,1,2,1,2),_Dot3aAggVlanId_Type())
dot3aAggVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:dot3aAggVlanId.setStatus(_E)
_Dot3aAggMacAddr_Type=MacAddress
_Dot3aAggMacAddr_Object=MibTableColumn
dot3aAggMacAddr=_Dot3aAggMacAddr_Object((1,3,6,1,4,1,6027,3,2,1,1,2,1,3),_Dot3aAggMacAddr_Type())
dot3aAggMacAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:dot3aAggMacAddr.setStatus(_E)
class _Dot3aAggStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_Dot3aAggStatus_Type.__name__=_F
_Dot3aAggStatus_Object=MibTableColumn
dot3aAggStatus=_Dot3aAggStatus_Object((1,3,6,1,4,1,6027,3,2,1,1,2,1,4),_Dot3aAggStatus_Type())
dot3aAggStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3aAggStatus.setStatus(_E)
_Dot3aAggDistributedPort_Type=OctetString
_Dot3aAggDistributedPort_Object=MibTableColumn
dot3aAggDistributedPort=_Dot3aAggDistributedPort_Object((1,3,6,1,4,1,6027,3,2,1,1,2,1,5),_Dot3aAggDistributedPort_Type())
dot3aAggDistributedPort.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3aAggDistributedPort.setStatus(_E)
_Dot3aAggFdbTable_Object=MibTable
dot3aAggFdbTable=_Dot3aAggFdbTable_Object((1,3,6,1,4,1,6027,3,2,1,1,3))
if mibBuilder.loadTexts:dot3aAggFdbTable.setStatus(_B)
_Dot3aAggFdbEntry_Object=MibTableRow
dot3aAggFdbEntry=_Dot3aAggFdbEntry_Object((1,3,6,1,4,1,6027,3,2,1,1,3,1))
dot3aAggFdbEntry.setIndexNames((0,_A,_b),(0,_A,_c),(0,_A,_d))
if mibBuilder.loadTexts:dot3aAggFdbEntry.setStatus(_E)
_Dot3aAggFdbIndex_Type=Unsigned32
_Dot3aAggFdbIndex_Object=MibTableColumn
dot3aAggFdbIndex=_Dot3aAggFdbIndex_Object((1,3,6,1,4,1,6027,3,2,1,1,3,1,1),_Dot3aAggFdbIndex_Type())
dot3aAggFdbIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:dot3aAggFdbIndex.setStatus(_E)
_Dot3aAggFdbVlanId_Type=Unsigned32
_Dot3aAggFdbVlanId_Object=MibTableColumn
dot3aAggFdbVlanId=_Dot3aAggFdbVlanId_Object((1,3,6,1,4,1,6027,3,2,1,1,3,1,2),_Dot3aAggFdbVlanId_Type())
dot3aAggFdbVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:dot3aAggFdbVlanId.setStatus(_E)
_Dot3aAggFdbMacAddr_Type=MacAddress
_Dot3aAggFdbMacAddr_Object=MibTableColumn
dot3aAggFdbMacAddr=_Dot3aAggFdbMacAddr_Object((1,3,6,1,4,1,6027,3,2,1,1,3,1,3),_Dot3aAggFdbMacAddr_Type())
dot3aAggFdbMacAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:dot3aAggFdbMacAddr.setStatus(_E)
class _Dot3aAggFdbStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_Dot3aAggFdbStatus_Type.__name__=_F
_Dot3aAggFdbStatus_Object=MibTableColumn
dot3aAggFdbStatus=_Dot3aAggFdbStatus_Object((1,3,6,1,4,1,6027,3,2,1,1,3,1,4),_Dot3aAggFdbStatus_Type())
dot3aAggFdbStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3aAggFdbStatus.setStatus(_E)
_Dot3aAggFdbDistributedPort_Type=OctetString
_Dot3aAggFdbDistributedPort_Object=MibTableColumn
dot3aAggFdbDistributedPort=_Dot3aAggFdbDistributedPort_Object((1,3,6,1,4,1,6027,3,2,1,1,3,1,5),_Dot3aAggFdbDistributedPort_Type())
dot3aAggFdbDistributedPort.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3aAggFdbDistributedPort.setStatus(_E)
_Dot3aCurAggStaticTable_Object=MibTable
dot3aCurAggStaticTable=_Dot3aCurAggStaticTable_Object((1,3,6,1,4,1,6027,3,2,1,1,4))
if mibBuilder.loadTexts:dot3aCurAggStaticTable.setStatus(_B)
_Dot3aCurAggStaticEntry_Object=MibTableRow
dot3aCurAggStaticEntry=_Dot3aCurAggStaticEntry_Object((1,3,6,1,4,1,6027,3,2,1,1,4,1))
dot3aCurAggStaticEntry.setIndexNames((0,_A,_e),(0,_A,_f),(0,_A,_g))
if mibBuilder.loadTexts:dot3aCurAggStaticEntry.setStatus(_B)
_Dot3aCurAggVlanId_Type=Unsigned32
_Dot3aCurAggVlanId_Object=MibTableColumn
dot3aCurAggVlanId=_Dot3aCurAggVlanId_Object((1,3,6,1,4,1,6027,3,2,1,1,4,1,1),_Dot3aCurAggVlanId_Type())
dot3aCurAggVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:dot3aCurAggVlanId.setStatus(_B)
_Dot3aCurAggMacAddr_Type=MacAddress
_Dot3aCurAggMacAddr_Object=MibTableColumn
dot3aCurAggMacAddr=_Dot3aCurAggMacAddr_Object((1,3,6,1,4,1,6027,3,2,1,1,4,1,2),_Dot3aCurAggMacAddr_Type())
dot3aCurAggMacAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:dot3aCurAggMacAddr.setStatus(_B)
_Dot3aCurAggIndex_Type=Unsigned32
_Dot3aCurAggIndex_Object=MibTableColumn
dot3aCurAggIndex=_Dot3aCurAggIndex_Object((1,3,6,1,4,1,6027,3,2,1,1,4,1,3),_Dot3aCurAggIndex_Type())
dot3aCurAggIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:dot3aCurAggIndex.setStatus(_B)
class _Dot3aCurAggStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_Dot3aCurAggStatus_Type.__name__=_F
_Dot3aCurAggStatus_Object=MibTableColumn
dot3aCurAggStatus=_Dot3aCurAggStatus_Object((1,3,6,1,4,1,6027,3,2,1,1,4,1,4),_Dot3aCurAggStatus_Type())
dot3aCurAggStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3aCurAggStatus.setStatus(_B)
_Dot3aCurAggFdbTable_Object=MibTable
dot3aCurAggFdbTable=_Dot3aCurAggFdbTable_Object((1,3,6,1,4,1,6027,3,2,1,1,5))
if mibBuilder.loadTexts:dot3aCurAggFdbTable.setStatus(_B)
_Dot3aCurAggFdbEntry_Object=MibTableRow
dot3aCurAggFdbEntry=_Dot3aCurAggFdbEntry_Object((1,3,6,1,4,1,6027,3,2,1,1,5,1))
dot3aCurAggFdbEntry.setIndexNames((0,_A,_h),(0,_A,_i),(0,_A,_j))
if mibBuilder.loadTexts:dot3aCurAggFdbEntry.setStatus(_B)
_Dot3aCurAggFdbVlanId_Type=Unsigned32
_Dot3aCurAggFdbVlanId_Object=MibTableColumn
dot3aCurAggFdbVlanId=_Dot3aCurAggFdbVlanId_Object((1,3,6,1,4,1,6027,3,2,1,1,5,1,1),_Dot3aCurAggFdbVlanId_Type())
dot3aCurAggFdbVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:dot3aCurAggFdbVlanId.setStatus(_B)
_Dot3aCurAggFdbMacAddr_Type=MacAddress
_Dot3aCurAggFdbMacAddr_Object=MibTableColumn
dot3aCurAggFdbMacAddr=_Dot3aCurAggFdbMacAddr_Object((1,3,6,1,4,1,6027,3,2,1,1,5,1,2),_Dot3aCurAggFdbMacAddr_Type())
dot3aCurAggFdbMacAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:dot3aCurAggFdbMacAddr.setStatus(_B)
_Dot3aCurAggFdbIndex_Type=Unsigned32
_Dot3aCurAggFdbIndex_Object=MibTableColumn
dot3aCurAggFdbIndex=_Dot3aCurAggFdbIndex_Object((1,3,6,1,4,1,6027,3,2,1,1,5,1,3),_Dot3aCurAggFdbIndex_Type())
dot3aCurAggFdbIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:dot3aCurAggFdbIndex.setStatus(_B)
class _Dot3aCurAggFdbStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_Dot3aCurAggFdbStatus_Type.__name__=_F
_Dot3aCurAggFdbStatus_Object=MibTableColumn
dot3aCurAggFdbStatus=_Dot3aCurAggFdbStatus_Object((1,3,6,1,4,1,6027,3,2,1,1,5,1,4),_Dot3aCurAggFdbStatus_Type())
dot3aCurAggFdbStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3aCurAggFdbStatus.setStatus(_B)
_Dot3aCommonAggFdbTable_Object=MibTable
dot3aCommonAggFdbTable=_Dot3aCommonAggFdbTable_Object((1,3,6,1,4,1,6027,3,2,1,1,6))
if mibBuilder.loadTexts:dot3aCommonAggFdbTable.setStatus(_B)
_Dot3aCommonAggFdbEntry_Object=MibTableRow
dot3aCommonAggFdbEntry=_Dot3aCommonAggFdbEntry_Object((1,3,6,1,4,1,6027,3,2,1,1,6,1))
dot3aCommonAggFdbEntry.setIndexNames((0,_A,_k),(0,_A,_l))
if mibBuilder.loadTexts:dot3aCommonAggFdbEntry.setStatus(_B)
_Dot3aCommonAggFdbIndex_Type=Unsigned32
_Dot3aCommonAggFdbIndex_Object=MibTableColumn
dot3aCommonAggFdbIndex=_Dot3aCommonAggFdbIndex_Object((1,3,6,1,4,1,6027,3,2,1,1,6,1,1),_Dot3aCommonAggFdbIndex_Type())
dot3aCommonAggFdbIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:dot3aCommonAggFdbIndex.setStatus(_B)
_Dot3aCommonAggFdbVlanId_Type=Unsigned32
_Dot3aCommonAggFdbVlanId_Object=MibTableColumn
dot3aCommonAggFdbVlanId=_Dot3aCommonAggFdbVlanId_Object((1,3,6,1,4,1,6027,3,2,1,1,6,1,2),_Dot3aCommonAggFdbVlanId_Type())
dot3aCommonAggFdbVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:dot3aCommonAggFdbVlanId.setStatus(_B)
class _Dot3aCommonAggFdbTagConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('tagged',1),('untagged',2)))
_Dot3aCommonAggFdbTagConfig_Type.__name__=_F
_Dot3aCommonAggFdbTagConfig_Object=MibTableColumn
dot3aCommonAggFdbTagConfig=_Dot3aCommonAggFdbTagConfig_Object((1,3,6,1,4,1,6027,3,2,1,1,6,1,3),_Dot3aCommonAggFdbTagConfig_Type())
dot3aCommonAggFdbTagConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3aCommonAggFdbTagConfig.setStatus(_B)
class _Dot3aCommonAggFdbStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_Dot3aCommonAggFdbStatus_Type.__name__=_F
_Dot3aCommonAggFdbStatus_Object=MibTableColumn
dot3aCommonAggFdbStatus=_Dot3aCommonAggFdbStatus_Object((1,3,6,1,4,1,6027,3,2,1,1,6,1,4),_Dot3aCommonAggFdbStatus_Type())
dot3aCommonAggFdbStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3aCommonAggFdbStatus.setStatus(_B)
_Dot3adAggPortTable_Object=MibTable
dot3adAggPortTable=_Dot3adAggPortTable_Object((1,3,6,1,4,1,6027,3,2,1,1,7))
if mibBuilder.loadTexts:dot3adAggPortTable.setStatus(_B)
_Dot3adAggPortEntry_Object=MibTableRow
dot3adAggPortEntry=_Dot3adAggPortEntry_Object((1,3,6,1,4,1,6027,3,2,1,1,7,1))
dot3adAggPortEntry.setIndexNames((0,_A,_m))
if mibBuilder.loadTexts:dot3adAggPortEntry.setStatus(_B)
_Dot3adAggPortIndex_Type=Unsigned32
_Dot3adAggPortIndex_Object=MibTableColumn
dot3adAggPortIndex=_Dot3adAggPortIndex_Object((1,3,6,1,4,1,6027,3,2,1,1,7,1,1),_Dot3adAggPortIndex_Type())
dot3adAggPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:dot3adAggPortIndex.setStatus(_B)
_Dot3adAggPortActorOperKey_Type=F10LacpKey
_Dot3adAggPortActorOperKey_Object=MibTableColumn
dot3adAggPortActorOperKey=_Dot3adAggPortActorOperKey_Object((1,3,6,1,4,1,6027,3,2,1,1,7,1,2),_Dot3adAggPortActorOperKey_Type())
dot3adAggPortActorOperKey.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3adAggPortActorOperKey.setStatus(_B)
_Dot3adAggPortPartnerOperKey_Type=F10LacpKey
_Dot3adAggPortPartnerOperKey_Object=MibTableColumn
dot3adAggPortPartnerOperKey=_Dot3adAggPortPartnerOperKey_Object((1,3,6,1,4,1,6027,3,2,1,1,7,1,3),_Dot3adAggPortPartnerOperKey_Type())
dot3adAggPortPartnerOperKey.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3adAggPortPartnerOperKey.setStatus(_B)
_Dot3adAggPortActorAdminState_Type=F10LacpState
_Dot3adAggPortActorAdminState_Object=MibTableColumn
dot3adAggPortActorAdminState=_Dot3adAggPortActorAdminState_Object((1,3,6,1,4,1,6027,3,2,1,1,7,1,4),_Dot3adAggPortActorAdminState_Type())
dot3adAggPortActorAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3adAggPortActorAdminState.setStatus(_B)
_Dot3adAggPortActorOperState_Type=F10LacpState
_Dot3adAggPortActorOperState_Object=MibTableColumn
dot3adAggPortActorOperState=_Dot3adAggPortActorOperState_Object((1,3,6,1,4,1,6027,3,2,1,1,7,1,5),_Dot3adAggPortActorOperState_Type())
dot3adAggPortActorOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3adAggPortActorOperState.setStatus(_B)
_Dot3adAggPortPartnerAdminState_Type=F10LacpState
_Dot3adAggPortPartnerAdminState_Object=MibTableColumn
dot3adAggPortPartnerAdminState=_Dot3adAggPortPartnerAdminState_Object((1,3,6,1,4,1,6027,3,2,1,1,7,1,6),_Dot3adAggPortPartnerAdminState_Type())
dot3adAggPortPartnerAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3adAggPortPartnerAdminState.setStatus(_B)
_Dot3adAggPortPartnerOperState_Type=F10LacpState
_Dot3adAggPortPartnerOperState_Object=MibTableColumn
dot3adAggPortPartnerOperState=_Dot3adAggPortPartnerOperState_Object((1,3,6,1,4,1,6027,3,2,1,1,7,1,7),_Dot3adAggPortPartnerOperState_Type())
dot3adAggPortPartnerOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3adAggPortPartnerOperState.setStatus(_B)
_F10LinkAggMgmt_ObjectIdentity=ObjectIdentity
f10LinkAggMgmt=_F10LinkAggMgmt_ObjectIdentity((1,3,6,1,4,1,6027,3,2,1,2))
class _Dot3aClearFdb_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_Dot3aClearFdb_Type.__name__=_F
_Dot3aClearFdb_Object=MibScalar
dot3aClearFdb=_Dot3aClearFdb_Object((1,3,6,1,4,1,6027,3,2,1,2,1),_Dot3aClearFdb_Type())
dot3aClearFdb.setMaxAccess('read-write')
if mibBuilder.loadTexts:dot3aClearFdb.setStatus(_B)
_F10LinkAggAlarms_ObjectIdentity=ObjectIdentity
f10LinkAggAlarms=_F10LinkAggAlarms_ObjectIdentity((1,3,6,1,4,1,6027,3,2,2))
_F10Dot3adAggNotifications_ObjectIdentity=ObjectIdentity
f10Dot3adAggNotifications=_F10Dot3adAggNotifications_ObjectIdentity((1,3,6,1,4,1,6027,3,2,2,0))
_F10LinkBundleNotifications_ObjectIdentity=ObjectIdentity
f10LinkBundleNotifications=_F10LinkBundleNotifications_ObjectIdentity((1,3,6,1,4,1,6027,3,2,2,1))
class _LinkBundleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ecmpBundle',1),('lagBundle',2)))
_LinkBundleType_Type.__name__=_F
_LinkBundleType_Object=MibScalar
linkBundleType=_LinkBundleType_Object((1,3,6,1,4,1,6027,3,2,2,2),_LinkBundleType_Type())
linkBundleType.setMaxAccess(_n)
if mibBuilder.loadTexts:linkBundleType.setStatus(_B)
_LinkBundleNumber_Type=Integer32
_LinkBundleNumber_Object=MibScalar
linkBundleNumber=_LinkBundleNumber_Object((1,3,6,1,4,1,6027,3,2,2,3),_LinkBundleNumber_Type())
linkBundleNumber.setMaxAccess(_n)
if mibBuilder.loadTexts:linkBundleNumber.setStatus(_B)
_F10LinkAggMibConformance_ObjectIdentity=ObjectIdentity
f10LinkAggMibConformance=_F10LinkAggMibConformance_ObjectIdentity((1,3,6,1,4,1,6027,3,2,3))
_F10LinkAggMibCompliances_ObjectIdentity=ObjectIdentity
f10LinkAggMibCompliances=_F10LinkAggMibCompliances_ObjectIdentity((1,3,6,1,4,1,6027,3,2,3,1))
_F10LinkAggMibGroups_ObjectIdentity=ObjectIdentity
f10LinkAggMibGroups=_F10LinkAggMibGroups_ObjectIdentity((1,3,6,1,4,1,6027,3,2,3,2))
f10LinkAggCommonGroup=ObjectGroup((1,3,6,1,4,1,6027,3,2,3,2,1))
f10LinkAggCommonGroup.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s)))
if mibBuilder.loadTexts:f10LinkAggCommonGroup.setStatus(_E)
f10LinkAggCommonGroupRev1=ObjectGroup((1,3,6,1,4,1,6027,3,2,3,2,2))
f10LinkAggCommonGroupRev1.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U)))
if mibBuilder.loadTexts:f10LinkAggCommonGroupRev1.setStatus(_B)
f10LinkAggPortGroup=ObjectGroup((1,3,6,1,4,1,6027,3,2,3,2,3))
f10LinkAggPortGroup.setObjects(*((_A,_t),(_A,_u),(_A,_v),(_A,_V),(_A,_w),(_A,_W)))
if mibBuilder.loadTexts:f10LinkAggPortGroup.setStatus(_B)
f10LinkAggAlarmObjectGroup=ObjectGroup((1,3,6,1,4,1,6027,3,2,3,2,5))
f10LinkAggAlarmObjectGroup.setObjects(*((_A,_I),(_A,_J)))
if mibBuilder.loadTexts:f10LinkAggAlarmObjectGroup.setStatus(_B)
dot3adAggLacpStateChange=NotificationType((1,3,6,1,4,1,6027,3,2,2,0,1))
dot3adAggLacpStateChange.setObjects(*((_A,_V),(_A,_W)))
if mibBuilder.loadTexts:dot3adAggLacpStateChange.setStatus(_B)
linkBundleImbalance=NotificationType((1,3,6,1,4,1,6027,3,2,2,1,1))
linkBundleImbalance.setObjects(*((_A,_I),(_A,_J)))
if mibBuilder.loadTexts:linkBundleImbalance.setStatus(_B)
linkBundleImbalanceClear=NotificationType((1,3,6,1,4,1,6027,3,2,2,1,2))
linkBundleImbalanceClear.setObjects(*((_A,_I),(_A,_J)))
if mibBuilder.loadTexts:linkBundleImbalanceClear.setStatus(_B)
f10LinkAggNotificationGroup=NotificationGroup((1,3,6,1,4,1,6027,3,2,3,2,4))
f10LinkAggNotificationGroup.setObjects(*((_A,_x),(_A,_y),(_A,_z)))
if mibBuilder.loadTexts:f10LinkAggNotificationGroup.setStatus(_B)
f10LinkAggMibCompliance=ModuleCompliance((1,3,6,1,4,1,6027,3,2,3,1,1))
f10LinkAggMibCompliance.setObjects((_A,_A0))
if mibBuilder.loadTexts:f10LinkAggMibCompliance.setStatus(_E)
f10LinkAggMibComplianceRev1=ModuleCompliance((1,3,6,1,4,1,6027,3,2,3,1,2))
f10LinkAggMibComplianceRev1.setObjects(*((_A,_A1),(_A,_A2),(_A,_A3)))
if mibBuilder.loadTexts:f10LinkAggMibComplianceRev1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'F10LacpKey':F10LacpKey,'F10LacpState':F10LacpState,'f10LinkAggMib':f10LinkAggMib,'f10LinkAggObjects':f10LinkAggObjects,'f10dot3dAgg':f10dot3dAgg,'dot3aAggConfigTable':dot3aAggConfigTable,'dot3aAggConfigEntry':dot3aAggConfigEntry,_X:dot3aAggCfgId,_K:dot3aAggCfgMacAddr,_L:dot3aAggCfgIfIndex,_M:dot3aAggCfgNumPorts,_o:dot3aAggCfgPortList,_N:dot3aAggCfgPortListString,_O:dot3aAggCfgLacpSupported,_P:dot3aAggCfgOperStatus,'dot3aAggStaticTable':dot3aAggStaticTable,'dot3aAggStaticEntry':dot3aAggStaticEntry,_Y:dot3aAggIndex,_Z:dot3aAggVlanId,_a:dot3aAggMacAddr,_p:dot3aAggStatus,_q:dot3aAggDistributedPort,'dot3aAggFdbTable':dot3aAggFdbTable,'dot3aAggFdbEntry':dot3aAggFdbEntry,_b:dot3aAggFdbIndex,_c:dot3aAggFdbVlanId,_d:dot3aAggFdbMacAddr,_r:dot3aAggFdbStatus,_s:dot3aAggFdbDistributedPort,'dot3aCurAggStaticTable':dot3aCurAggStaticTable,'dot3aCurAggStaticEntry':dot3aCurAggStaticEntry,_e:dot3aCurAggVlanId,_f:dot3aCurAggMacAddr,_g:dot3aCurAggIndex,_Q:dot3aCurAggStatus,'dot3aCurAggFdbTable':dot3aCurAggFdbTable,'dot3aCurAggFdbEntry':dot3aCurAggFdbEntry,_h:dot3aCurAggFdbVlanId,_i:dot3aCurAggFdbMacAddr,_j:dot3aCurAggFdbIndex,_R:dot3aCurAggFdbStatus,'dot3aCommonAggFdbTable':dot3aCommonAggFdbTable,'dot3aCommonAggFdbEntry':dot3aCommonAggFdbEntry,_k:dot3aCommonAggFdbIndex,_l:dot3aCommonAggFdbVlanId,_S:dot3aCommonAggFdbTagConfig,_T:dot3aCommonAggFdbStatus,'dot3adAggPortTable':dot3adAggPortTable,'dot3adAggPortEntry':dot3adAggPortEntry,_m:dot3adAggPortIndex,_t:dot3adAggPortActorOperKey,_u:dot3adAggPortPartnerOperKey,_v:dot3adAggPortActorAdminState,_V:dot3adAggPortActorOperState,_w:dot3adAggPortPartnerAdminState,_W:dot3adAggPortPartnerOperState,'f10LinkAggMgmt':f10LinkAggMgmt,_U:dot3aClearFdb,'f10LinkAggAlarms':f10LinkAggAlarms,'f10Dot3adAggNotifications':f10Dot3adAggNotifications,_x:dot3adAggLacpStateChange,'f10LinkBundleNotifications':f10LinkBundleNotifications,_y:linkBundleImbalance,_z:linkBundleImbalanceClear,_I:linkBundleType,_J:linkBundleNumber,'f10LinkAggMibConformance':f10LinkAggMibConformance,'f10LinkAggMibCompliances':f10LinkAggMibCompliances,'f10LinkAggMibCompliance':f10LinkAggMibCompliance,'f10LinkAggMibComplianceRev1':f10LinkAggMibComplianceRev1,'f10LinkAggMibGroups':f10LinkAggMibGroups,_A0:f10LinkAggCommonGroup,_A1:f10LinkAggCommonGroupRev1,_A2:f10LinkAggPortGroup,_A3:f10LinkAggNotificationGroup,'f10LinkAggAlarmObjectGroup':f10LinkAggAlarmObjectGroup})