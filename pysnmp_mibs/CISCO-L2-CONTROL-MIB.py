_AX='clcMacAddressStatsGroup'
_AW='deprecated'
_AV='clcIfVlanMacLimitHighNotif'
_AU='clcIfVlanMacLimitLowNotif'
_AT='clcIfMacLimitHighNotif'
_AS='clcIfMacLimitLowNotif'
_AR='clcVlanMacLimitHighNotif'
_AQ='clcVlanMacLimitNotif'
_AP='clcFdbMacAddressStatsNumber'
_AO='clcIfVlanMacLimitHighNotifEnable'
_AN='clcIfVlanMacLimitLowNotifEnable'
_AM='clcIfVlanMacLimitEnable'
_AL='clcIfVlanMacLimitStatus'
_AK='clcIfVlanMacLimitHiExceedAction'
_AJ='clcIfVlanMacLimitLowExceedAction'
_AI='clcIfVlanMacLimitGlobalConfig'
_AH='clcIfMacLimitHighNotifEnable'
_AG='clcIfMacLimitLowNotifEnable'
_AF='clcIfMacLimitEnable'
_AE='clcIfMacLimitStatus'
_AD='clcIfMacLimitHighExceedAction'
_AC='clcIfMacLimitLowExceedAction'
_AB='clcIfMacLimitGlobalConfig'
_AA='clcMacLimitHighNotifEnable'
_A9='clcMacLimitNotifEnable'
_A8='clcVlanMacLimitEnable'
_A7='clcVlanMacLimitHighExceedAction'
_A6='clcMacLimitHighExceedActionDef'
_A5='clcMacLimitHighDefault'
_A4='clcMacLimitInterval'
_A3='clcUnicastFloodOperEnable'
_A2='clcUnicastFloodAdminEnable'
_A1='clcVlanMacLimitStatus'
_A0='clcVlanMacLimitExceededAction'
_z='clcVlanMacLimitGlobalConfig'
_y='clcMacLimitExceedNotifOption'
_x='clcMacLimitExceededActionDefault'
_w='clcMaxMacLimitDefault'
_v='clcMacLimitEnable'
_u='clcFdbMacAddressStatsType'
_t='Unsigned32'
_s='Integer32'
_r='ifIndex'
_q='IF-MIB'
_p='clcIfVlanMacLimitNotifsGroup'
_o='clcIfVlanMacLimitNotifControlGroup'
_n='clcIfVlanMacLimitEnableGroup'
_m='clcIfVlanMacAddressLimitGroup'
_l='clcIfMacLimitNotifsGroup'
_k='clcIfMacLimitNotifControlGroup'
_j='clcIfMacLimitEnableGroup'
_i='clcIfMacAddressLimitGroup'
_h='clcVlanMacLimitEnableGroup'
_g='clcVlanMacLimitNotifsGroup1'
_f='clcMacAddressLimitIntervalGroup'
_e='clcVlanMacLimitNotifControlGroup1'
_d='clcVlanMacLimitNotifControlGroup'
_c='clcVlanMacAddressLimitGroup1'
_b='clcMacAddressLimitGroup1'
_a='clcIfVlanMacLimitHigh'
_Z='clcIfVlanMacLimitLow'
_Y='clcIfMacLimitHigh'
_X='clcIfMacLimitLow'
_W='clcVlanMacLimitHigh'
_V='clcVlanMaxMacLimit'
_U='clcIfVlanMacLimitVlanIndex'
_T='clcIfVlanMacLimitIfIndex'
_S='clcIfMacLimitIfIndex'
_R='clcVlanMacLimitIndex'
_Q='clcUnicastFloodGroup'
_P='clcVlanMacLimitNotifsGroup'
_O='clcVlanMacAddressLimitGroup'
_N='clcMacAddressLimitGroup'
_M='clcFdbIfVlanMacUsage'
_L='clcFdbIfMacUsage'
_K='clcFdbVlanMacUsage'
_J='TruthValue'
_I='Bits'
_H='entPhysicalIndex'
_G='ENTITY-MIB'
_F='not-accessible'
_E='read-only'
_D='read-write'
_C='read-create'
_B='current'
_A='CISCO-L2-CONTROL-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
entPhysicalIndex,=mibBuilder.importSymbols(_G,_H)
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_q,'InterfaceIndex',_r)
VlanIndex,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_I,'Counter32','Counter64','Gauge32',_s,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_t,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_J)
ciscoL2ControlMIB=ModuleIdentity((1,3,6,1,4,1,9,9,313))
if mibBuilder.loadTexts:ciscoL2ControlMIB.setRevisions(('2013-07-03 00:00','2007-01-10 00:00','2003-12-01 00:00'))
class MacLimitExceededAction(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('warning',1),('limit',2),('limitNoFlood',3),('shutdown',4)))
class ClcMacAddressStatsType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('allMac',1),('dynamicMac',2),('staticMac',3),('mcastMac',4),('pvlanCloneMac',5),('overlayMac',6),('secureMac',7)))
_CiscoL2ControlMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoL2ControlMIBNotifs=_CiscoL2ControlMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,313,0))
_CiscoL2ControlMIBObjects_ObjectIdentity=ObjectIdentity
ciscoL2ControlMIBObjects=_CiscoL2ControlMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,313,1))
_ClcMacAddressLimitObjects_ObjectIdentity=ObjectIdentity
clcMacAddressLimitObjects=_ClcMacAddressLimitObjects_ObjectIdentity((1,3,6,1,4,1,9,9,313,1,1))
_ClcMacLimitEnable_Type=TruthValue
_ClcMacLimitEnable_Object=MibScalar
clcMacLimitEnable=_ClcMacLimitEnable_Object((1,3,6,1,4,1,9,9,313,1,1,1),_ClcMacLimitEnable_Type())
clcMacLimitEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:clcMacLimitEnable.setStatus(_B)
_ClcMaxMacLimitDefault_Type=Unsigned32
_ClcMaxMacLimitDefault_Object=MibScalar
clcMaxMacLimitDefault=_ClcMaxMacLimitDefault_Object((1,3,6,1,4,1,9,9,313,1,1,2),_ClcMaxMacLimitDefault_Type())
clcMaxMacLimitDefault.setMaxAccess(_D)
if mibBuilder.loadTexts:clcMaxMacLimitDefault.setStatus(_B)
_ClcMacLimitExceededActionDefault_Type=MacLimitExceededAction
_ClcMacLimitExceededActionDefault_Object=MibScalar
clcMacLimitExceededActionDefault=_ClcMacLimitExceededActionDefault_Object((1,3,6,1,4,1,9,9,313,1,1,3),_ClcMacLimitExceededActionDefault_Type())
clcMacLimitExceededActionDefault.setMaxAccess(_D)
if mibBuilder.loadTexts:clcMacLimitExceededActionDefault.setStatus(_B)
class _ClcMacLimitExceedNotifOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('sysLog',1),('snmpNotif',2),('both',3)))
_ClcMacLimitExceedNotifOption_Type.__name__=_s
_ClcMacLimitExceedNotifOption_Object=MibScalar
clcMacLimitExceedNotifOption=_ClcMacLimitExceedNotifOption_Object((1,3,6,1,4,1,9,9,313,1,1,4),_ClcMacLimitExceedNotifOption_Type())
clcMacLimitExceedNotifOption.setMaxAccess(_D)
if mibBuilder.loadTexts:clcMacLimitExceedNotifOption.setStatus(_B)
_ClcMacLimitNotifEnable_Type=TruthValue
_ClcMacLimitNotifEnable_Object=MibScalar
clcMacLimitNotifEnable=_ClcMacLimitNotifEnable_Object((1,3,6,1,4,1,9,9,313,1,1,5),_ClcMacLimitNotifEnable_Type())
clcMacLimitNotifEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:clcMacLimitNotifEnable.setStatus(_B)
_ClcVlanMacLimitTable_Object=MibTable
clcVlanMacLimitTable=_ClcVlanMacLimitTable_Object((1,3,6,1,4,1,9,9,313,1,1,6))
if mibBuilder.loadTexts:clcVlanMacLimitTable.setStatus(_B)
_ClcVlanMacLimitEntry_Object=MibTableRow
clcVlanMacLimitEntry=_ClcVlanMacLimitEntry_Object((1,3,6,1,4,1,9,9,313,1,1,6,1))
clcVlanMacLimitEntry.setIndexNames((0,_A,_R))
if mibBuilder.loadTexts:clcVlanMacLimitEntry.setStatus(_B)
class _ClcVlanMacLimitIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4096))
_ClcVlanMacLimitIndex_Type.__name__=_t
_ClcVlanMacLimitIndex_Object=MibTableColumn
clcVlanMacLimitIndex=_ClcVlanMacLimitIndex_Object((1,3,6,1,4,1,9,9,313,1,1,6,1,1),_ClcVlanMacLimitIndex_Type())
clcVlanMacLimitIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:clcVlanMacLimitIndex.setStatus(_B)
class _ClcVlanMacLimitGlobalConfig_Type(Bits):namedValues=NamedValues(*(('vlanMaxMacLimit',0),('vlanLimitExceededAction',1),('vlanMacLimitHigh',2),('vlanLimitHighExceededAction',3)))
_ClcVlanMacLimitGlobalConfig_Type.__name__=_I
_ClcVlanMacLimitGlobalConfig_Object=MibTableColumn
clcVlanMacLimitGlobalConfig=_ClcVlanMacLimitGlobalConfig_Object((1,3,6,1,4,1,9,9,313,1,1,6,1,2),_ClcVlanMacLimitGlobalConfig_Type())
clcVlanMacLimitGlobalConfig.setMaxAccess(_E)
if mibBuilder.loadTexts:clcVlanMacLimitGlobalConfig.setStatus(_B)
_ClcVlanMaxMacLimit_Type=Unsigned32
_ClcVlanMaxMacLimit_Object=MibTableColumn
clcVlanMaxMacLimit=_ClcVlanMaxMacLimit_Object((1,3,6,1,4,1,9,9,313,1,1,6,1,3),_ClcVlanMaxMacLimit_Type())
clcVlanMaxMacLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:clcVlanMaxMacLimit.setStatus(_B)
_ClcVlanMacLimitExceededAction_Type=MacLimitExceededAction
_ClcVlanMacLimitExceededAction_Object=MibTableColumn
clcVlanMacLimitExceededAction=_ClcVlanMacLimitExceededAction_Object((1,3,6,1,4,1,9,9,313,1,1,6,1,4),_ClcVlanMacLimitExceededAction_Type())
clcVlanMacLimitExceededAction.setMaxAccess(_C)
if mibBuilder.loadTexts:clcVlanMacLimitExceededAction.setStatus(_B)
_ClcVlanMacLimitStatus_Type=RowStatus
_ClcVlanMacLimitStatus_Object=MibTableColumn
clcVlanMacLimitStatus=_ClcVlanMacLimitStatus_Object((1,3,6,1,4,1,9,9,313,1,1,6,1,5),_ClcVlanMacLimitStatus_Type())
clcVlanMacLimitStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:clcVlanMacLimitStatus.setStatus(_B)
class _ClcVlanMacLimitEnable_Type(TruthValue):defaultValue=2
_ClcVlanMacLimitEnable_Type.__name__=_J
_ClcVlanMacLimitEnable_Object=MibTableColumn
clcVlanMacLimitEnable=_ClcVlanMacLimitEnable_Object((1,3,6,1,4,1,9,9,313,1,1,6,1,6),_ClcVlanMacLimitEnable_Type())
clcVlanMacLimitEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:clcVlanMacLimitEnable.setStatus(_B)
_ClcVlanMacLimitHigh_Type=Unsigned32
_ClcVlanMacLimitHigh_Object=MibTableColumn
clcVlanMacLimitHigh=_ClcVlanMacLimitHigh_Object((1,3,6,1,4,1,9,9,313,1,1,6,1,7),_ClcVlanMacLimitHigh_Type())
clcVlanMacLimitHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:clcVlanMacLimitHigh.setStatus(_B)
_ClcVlanMacLimitHighExceedAction_Type=MacLimitExceededAction
_ClcVlanMacLimitHighExceedAction_Object=MibTableColumn
clcVlanMacLimitHighExceedAction=_ClcVlanMacLimitHighExceedAction_Object((1,3,6,1,4,1,9,9,313,1,1,6,1,8),_ClcVlanMacLimitHighExceedAction_Type())
clcVlanMacLimitHighExceedAction.setMaxAccess(_C)
if mibBuilder.loadTexts:clcVlanMacLimitHighExceedAction.setStatus(_B)
_ClcFdbVlanInfoTable_Object=MibTable
clcFdbVlanInfoTable=_ClcFdbVlanInfoTable_Object((1,3,6,1,4,1,9,9,313,1,1,7))
if mibBuilder.loadTexts:clcFdbVlanInfoTable.setStatus(_B)
_ClcFdbVlanInfoEntry_Object=MibTableRow
clcFdbVlanInfoEntry=_ClcFdbVlanInfoEntry_Object((1,3,6,1,4,1,9,9,313,1,1,7,1))
clcFdbVlanInfoEntry.setIndexNames((0,_G,_H),(0,_A,_R))
if mibBuilder.loadTexts:clcFdbVlanInfoEntry.setStatus(_B)
_ClcFdbVlanMacUsage_Type=Unsigned32
_ClcFdbVlanMacUsage_Object=MibTableColumn
clcFdbVlanMacUsage=_ClcFdbVlanMacUsage_Object((1,3,6,1,4,1,9,9,313,1,1,7,1,1),_ClcFdbVlanMacUsage_Type())
clcFdbVlanMacUsage.setMaxAccess(_E)
if mibBuilder.loadTexts:clcFdbVlanMacUsage.setStatus(_B)
_ClcMacLimitInterval_Type=Unsigned32
_ClcMacLimitInterval_Object=MibScalar
clcMacLimitInterval=_ClcMacLimitInterval_Object((1,3,6,1,4,1,9,9,313,1,1,8),_ClcMacLimitInterval_Type())
clcMacLimitInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:clcMacLimitInterval.setStatus(_B)
if mibBuilder.loadTexts:clcMacLimitInterval.setUnits('seconds')
_ClcMacLimitHighDefault_Type=Unsigned32
_ClcMacLimitHighDefault_Object=MibScalar
clcMacLimitHighDefault=_ClcMacLimitHighDefault_Object((1,3,6,1,4,1,9,9,313,1,1,9),_ClcMacLimitHighDefault_Type())
clcMacLimitHighDefault.setMaxAccess(_D)
if mibBuilder.loadTexts:clcMacLimitHighDefault.setStatus(_B)
_ClcMacLimitHighExceedActionDef_Type=MacLimitExceededAction
_ClcMacLimitHighExceedActionDef_Object=MibScalar
clcMacLimitHighExceedActionDef=_ClcMacLimitHighExceedActionDef_Object((1,3,6,1,4,1,9,9,313,1,1,10),_ClcMacLimitHighExceedActionDef_Type())
clcMacLimitHighExceedActionDef.setMaxAccess(_D)
if mibBuilder.loadTexts:clcMacLimitHighExceedActionDef.setStatus(_B)
_ClcMacLimitHighNotifEnable_Type=TruthValue
_ClcMacLimitHighNotifEnable_Object=MibScalar
clcMacLimitHighNotifEnable=_ClcMacLimitHighNotifEnable_Object((1,3,6,1,4,1,9,9,313,1,1,11),_ClcMacLimitHighNotifEnable_Type())
clcMacLimitHighNotifEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:clcMacLimitHighNotifEnable.setStatus(_B)
_ClcUnicastFloodObjects_ObjectIdentity=ObjectIdentity
clcUnicastFloodObjects=_ClcUnicastFloodObjects_ObjectIdentity((1,3,6,1,4,1,9,9,313,1,2))
_ClcUnicastFloodTable_Object=MibTable
clcUnicastFloodTable=_ClcUnicastFloodTable_Object((1,3,6,1,4,1,9,9,313,1,2,1))
if mibBuilder.loadTexts:clcUnicastFloodTable.setStatus(_B)
_ClcUnicastFloodEntry_Object=MibTableRow
clcUnicastFloodEntry=_ClcUnicastFloodEntry_Object((1,3,6,1,4,1,9,9,313,1,2,1,1))
clcUnicastFloodEntry.setIndexNames((0,_q,_r))
if mibBuilder.loadTexts:clcUnicastFloodEntry.setStatus(_B)
_ClcUnicastFloodAdminEnable_Type=TruthValue
_ClcUnicastFloodAdminEnable_Object=MibTableColumn
clcUnicastFloodAdminEnable=_ClcUnicastFloodAdminEnable_Object((1,3,6,1,4,1,9,9,313,1,2,1,1,1),_ClcUnicastFloodAdminEnable_Type())
clcUnicastFloodAdminEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:clcUnicastFloodAdminEnable.setStatus(_B)
_ClcUnicastFloodOperEnable_Type=TruthValue
_ClcUnicastFloodOperEnable_Object=MibTableColumn
clcUnicastFloodOperEnable=_ClcUnicastFloodOperEnable_Object((1,3,6,1,4,1,9,9,313,1,2,1,1,2),_ClcUnicastFloodOperEnable_Type())
clcUnicastFloodOperEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:clcUnicastFloodOperEnable.setStatus(_B)
_ClcIfMacAddressLimitObjects_ObjectIdentity=ObjectIdentity
clcIfMacAddressLimitObjects=_ClcIfMacAddressLimitObjects_ObjectIdentity((1,3,6,1,4,1,9,9,313,1,3))
_ClcIfMacLimitTable_Object=MibTable
clcIfMacLimitTable=_ClcIfMacLimitTable_Object((1,3,6,1,4,1,9,9,313,1,3,1))
if mibBuilder.loadTexts:clcIfMacLimitTable.setStatus(_B)
_ClcIfMacLimitEntry_Object=MibTableRow
clcIfMacLimitEntry=_ClcIfMacLimitEntry_Object((1,3,6,1,4,1,9,9,313,1,3,1,1))
clcIfMacLimitEntry.setIndexNames((0,_A,_S))
if mibBuilder.loadTexts:clcIfMacLimitEntry.setStatus(_B)
_ClcIfMacLimitIfIndex_Type=InterfaceIndex
_ClcIfMacLimitIfIndex_Object=MibTableColumn
clcIfMacLimitIfIndex=_ClcIfMacLimitIfIndex_Object((1,3,6,1,4,1,9,9,313,1,3,1,1,1),_ClcIfMacLimitIfIndex_Type())
clcIfMacLimitIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:clcIfMacLimitIfIndex.setStatus(_B)
class _ClcIfMacLimitEnable_Type(TruthValue):defaultValue=2
_ClcIfMacLimitEnable_Type.__name__=_J
_ClcIfMacLimitEnable_Object=MibTableColumn
clcIfMacLimitEnable=_ClcIfMacLimitEnable_Object((1,3,6,1,4,1,9,9,313,1,3,1,1,2),_ClcIfMacLimitEnable_Type())
clcIfMacLimitEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:clcIfMacLimitEnable.setStatus(_B)
class _ClcIfMacLimitGlobalConfig_Type(Bits):namedValues=NamedValues(*(('ifMacLimitLow',0),('ifLimitLowExceededAction',1),('ifMacLimitHigh',2),('ifLimitHighExceededAction',3)))
_ClcIfMacLimitGlobalConfig_Type.__name__=_I
_ClcIfMacLimitGlobalConfig_Object=MibTableColumn
clcIfMacLimitGlobalConfig=_ClcIfMacLimitGlobalConfig_Object((1,3,6,1,4,1,9,9,313,1,3,1,1,3),_ClcIfMacLimitGlobalConfig_Type())
clcIfMacLimitGlobalConfig.setMaxAccess(_E)
if mibBuilder.loadTexts:clcIfMacLimitGlobalConfig.setStatus(_B)
_ClcIfMacLimitLow_Type=Unsigned32
_ClcIfMacLimitLow_Object=MibTableColumn
clcIfMacLimitLow=_ClcIfMacLimitLow_Object((1,3,6,1,4,1,9,9,313,1,3,1,1,4),_ClcIfMacLimitLow_Type())
clcIfMacLimitLow.setMaxAccess(_C)
if mibBuilder.loadTexts:clcIfMacLimitLow.setStatus(_B)
_ClcIfMacLimitLowExceedAction_Type=MacLimitExceededAction
_ClcIfMacLimitLowExceedAction_Object=MibTableColumn
clcIfMacLimitLowExceedAction=_ClcIfMacLimitLowExceedAction_Object((1,3,6,1,4,1,9,9,313,1,3,1,1,5),_ClcIfMacLimitLowExceedAction_Type())
clcIfMacLimitLowExceedAction.setMaxAccess(_C)
if mibBuilder.loadTexts:clcIfMacLimitLowExceedAction.setStatus(_B)
_ClcIfMacLimitHigh_Type=Unsigned32
_ClcIfMacLimitHigh_Object=MibTableColumn
clcIfMacLimitHigh=_ClcIfMacLimitHigh_Object((1,3,6,1,4,1,9,9,313,1,3,1,1,6),_ClcIfMacLimitHigh_Type())
clcIfMacLimitHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:clcIfMacLimitHigh.setStatus(_B)
_ClcIfMacLimitHighExceedAction_Type=MacLimitExceededAction
_ClcIfMacLimitHighExceedAction_Object=MibTableColumn
clcIfMacLimitHighExceedAction=_ClcIfMacLimitHighExceedAction_Object((1,3,6,1,4,1,9,9,313,1,3,1,1,7),_ClcIfMacLimitHighExceedAction_Type())
clcIfMacLimitHighExceedAction.setMaxAccess(_C)
if mibBuilder.loadTexts:clcIfMacLimitHighExceedAction.setStatus(_B)
_ClcIfMacLimitStatus_Type=RowStatus
_ClcIfMacLimitStatus_Object=MibTableColumn
clcIfMacLimitStatus=_ClcIfMacLimitStatus_Object((1,3,6,1,4,1,9,9,313,1,3,1,1,8),_ClcIfMacLimitStatus_Type())
clcIfMacLimitStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:clcIfMacLimitStatus.setStatus(_B)
_ClcFdbIfInfoTable_Object=MibTable
clcFdbIfInfoTable=_ClcFdbIfInfoTable_Object((1,3,6,1,4,1,9,9,313,1,3,2))
if mibBuilder.loadTexts:clcFdbIfInfoTable.setStatus(_B)
_ClcFdbIfInfoEntry_Object=MibTableRow
clcFdbIfInfoEntry=_ClcFdbIfInfoEntry_Object((1,3,6,1,4,1,9,9,313,1,3,2,1))
clcFdbIfInfoEntry.setIndexNames((0,_G,_H),(0,_A,_S))
if mibBuilder.loadTexts:clcFdbIfInfoEntry.setStatus(_B)
_ClcFdbIfMacUsage_Type=Unsigned32
_ClcFdbIfMacUsage_Object=MibTableColumn
clcFdbIfMacUsage=_ClcFdbIfMacUsage_Object((1,3,6,1,4,1,9,9,313,1,3,2,1,1),_ClcFdbIfMacUsage_Type())
clcFdbIfMacUsage.setMaxAccess(_E)
if mibBuilder.loadTexts:clcFdbIfMacUsage.setStatus(_B)
_ClcIfMacLimitLowNotifEnable_Type=TruthValue
_ClcIfMacLimitLowNotifEnable_Object=MibScalar
clcIfMacLimitLowNotifEnable=_ClcIfMacLimitLowNotifEnable_Object((1,3,6,1,4,1,9,9,313,1,3,3),_ClcIfMacLimitLowNotifEnable_Type())
clcIfMacLimitLowNotifEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:clcIfMacLimitLowNotifEnable.setStatus(_B)
_ClcIfMacLimitHighNotifEnable_Type=TruthValue
_ClcIfMacLimitHighNotifEnable_Object=MibScalar
clcIfMacLimitHighNotifEnable=_ClcIfMacLimitHighNotifEnable_Object((1,3,6,1,4,1,9,9,313,1,3,4),_ClcIfMacLimitHighNotifEnable_Type())
clcIfMacLimitHighNotifEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:clcIfMacLimitHighNotifEnable.setStatus(_B)
_ClcIfVlanMacAddressLimitObjects_ObjectIdentity=ObjectIdentity
clcIfVlanMacAddressLimitObjects=_ClcIfVlanMacAddressLimitObjects_ObjectIdentity((1,3,6,1,4,1,9,9,313,1,4))
_ClcIfVlanMacLimitTable_Object=MibTable
clcIfVlanMacLimitTable=_ClcIfVlanMacLimitTable_Object((1,3,6,1,4,1,9,9,313,1,4,1))
if mibBuilder.loadTexts:clcIfVlanMacLimitTable.setStatus(_B)
_ClcIfVlanMacLimitEntry_Object=MibTableRow
clcIfVlanMacLimitEntry=_ClcIfVlanMacLimitEntry_Object((1,3,6,1,4,1,9,9,313,1,4,1,1))
clcIfVlanMacLimitEntry.setIndexNames((0,_A,_T),(0,_A,_U))
if mibBuilder.loadTexts:clcIfVlanMacLimitEntry.setStatus(_B)
_ClcIfVlanMacLimitIfIndex_Type=InterfaceIndex
_ClcIfVlanMacLimitIfIndex_Object=MibTableColumn
clcIfVlanMacLimitIfIndex=_ClcIfVlanMacLimitIfIndex_Object((1,3,6,1,4,1,9,9,313,1,4,1,1,1),_ClcIfVlanMacLimitIfIndex_Type())
clcIfVlanMacLimitIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:clcIfVlanMacLimitIfIndex.setStatus(_B)
_ClcIfVlanMacLimitVlanIndex_Type=VlanIndex
_ClcIfVlanMacLimitVlanIndex_Object=MibTableColumn
clcIfVlanMacLimitVlanIndex=_ClcIfVlanMacLimitVlanIndex_Object((1,3,6,1,4,1,9,9,313,1,4,1,1,2),_ClcIfVlanMacLimitVlanIndex_Type())
clcIfVlanMacLimitVlanIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:clcIfVlanMacLimitVlanIndex.setStatus(_B)
class _ClcIfVlanMacLimitEnable_Type(TruthValue):defaultValue=2
_ClcIfVlanMacLimitEnable_Type.__name__=_J
_ClcIfVlanMacLimitEnable_Object=MibTableColumn
clcIfVlanMacLimitEnable=_ClcIfVlanMacLimitEnable_Object((1,3,6,1,4,1,9,9,313,1,4,1,1,3),_ClcIfVlanMacLimitEnable_Type())
clcIfVlanMacLimitEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:clcIfVlanMacLimitEnable.setStatus(_B)
class _ClcIfVlanMacLimitGlobalConfig_Type(Bits):namedValues=NamedValues(*(('ifVlanMacLimitLow',0),('ifVlanLimitLowExceededAction',1),('ifVlanMacLimitHigh',2),('ifVlanLimitHighExceededAction',3)))
_ClcIfVlanMacLimitGlobalConfig_Type.__name__=_I
_ClcIfVlanMacLimitGlobalConfig_Object=MibTableColumn
clcIfVlanMacLimitGlobalConfig=_ClcIfVlanMacLimitGlobalConfig_Object((1,3,6,1,4,1,9,9,313,1,4,1,1,4),_ClcIfVlanMacLimitGlobalConfig_Type())
clcIfVlanMacLimitGlobalConfig.setMaxAccess(_E)
if mibBuilder.loadTexts:clcIfVlanMacLimitGlobalConfig.setStatus(_B)
_ClcIfVlanMacLimitLow_Type=Unsigned32
_ClcIfVlanMacLimitLow_Object=MibTableColumn
clcIfVlanMacLimitLow=_ClcIfVlanMacLimitLow_Object((1,3,6,1,4,1,9,9,313,1,4,1,1,5),_ClcIfVlanMacLimitLow_Type())
clcIfVlanMacLimitLow.setMaxAccess(_C)
if mibBuilder.loadTexts:clcIfVlanMacLimitLow.setStatus(_B)
_ClcIfVlanMacLimitLowExceedAction_Type=MacLimitExceededAction
_ClcIfVlanMacLimitLowExceedAction_Object=MibTableColumn
clcIfVlanMacLimitLowExceedAction=_ClcIfVlanMacLimitLowExceedAction_Object((1,3,6,1,4,1,9,9,313,1,4,1,1,6),_ClcIfVlanMacLimitLowExceedAction_Type())
clcIfVlanMacLimitLowExceedAction.setMaxAccess(_C)
if mibBuilder.loadTexts:clcIfVlanMacLimitLowExceedAction.setStatus(_B)
_ClcIfVlanMacLimitHigh_Type=Unsigned32
_ClcIfVlanMacLimitHigh_Object=MibTableColumn
clcIfVlanMacLimitHigh=_ClcIfVlanMacLimitHigh_Object((1,3,6,1,4,1,9,9,313,1,4,1,1,7),_ClcIfVlanMacLimitHigh_Type())
clcIfVlanMacLimitHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:clcIfVlanMacLimitHigh.setStatus(_B)
_ClcIfVlanMacLimitHiExceedAction_Type=MacLimitExceededAction
_ClcIfVlanMacLimitHiExceedAction_Object=MibTableColumn
clcIfVlanMacLimitHiExceedAction=_ClcIfVlanMacLimitHiExceedAction_Object((1,3,6,1,4,1,9,9,313,1,4,1,1,8),_ClcIfVlanMacLimitHiExceedAction_Type())
clcIfVlanMacLimitHiExceedAction.setMaxAccess(_C)
if mibBuilder.loadTexts:clcIfVlanMacLimitHiExceedAction.setStatus(_B)
_ClcIfVlanMacLimitStatus_Type=RowStatus
_ClcIfVlanMacLimitStatus_Object=MibTableColumn
clcIfVlanMacLimitStatus=_ClcIfVlanMacLimitStatus_Object((1,3,6,1,4,1,9,9,313,1,4,1,1,9),_ClcIfVlanMacLimitStatus_Type())
clcIfVlanMacLimitStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:clcIfVlanMacLimitStatus.setStatus(_B)
_ClcFdbIfVlanInfoTable_Object=MibTable
clcFdbIfVlanInfoTable=_ClcFdbIfVlanInfoTable_Object((1,3,6,1,4,1,9,9,313,1,4,2))
if mibBuilder.loadTexts:clcFdbIfVlanInfoTable.setStatus(_B)
_ClcFdbIfVlanInfoEntry_Object=MibTableRow
clcFdbIfVlanInfoEntry=_ClcFdbIfVlanInfoEntry_Object((1,3,6,1,4,1,9,9,313,1,4,2,1))
clcFdbIfVlanInfoEntry.setIndexNames((0,_G,_H),(0,_A,_T),(0,_A,_U))
if mibBuilder.loadTexts:clcFdbIfVlanInfoEntry.setStatus(_B)
_ClcFdbIfVlanMacUsage_Type=Unsigned32
_ClcFdbIfVlanMacUsage_Object=MibTableColumn
clcFdbIfVlanMacUsage=_ClcFdbIfVlanMacUsage_Object((1,3,6,1,4,1,9,9,313,1,4,2,1,1),_ClcFdbIfVlanMacUsage_Type())
clcFdbIfVlanMacUsage.setMaxAccess(_E)
if mibBuilder.loadTexts:clcFdbIfVlanMacUsage.setStatus(_B)
_ClcIfVlanMacLimitLowNotifEnable_Type=TruthValue
_ClcIfVlanMacLimitLowNotifEnable_Object=MibScalar
clcIfVlanMacLimitLowNotifEnable=_ClcIfVlanMacLimitLowNotifEnable_Object((1,3,6,1,4,1,9,9,313,1,4,3),_ClcIfVlanMacLimitLowNotifEnable_Type())
clcIfVlanMacLimitLowNotifEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:clcIfVlanMacLimitLowNotifEnable.setStatus(_B)
_ClcIfVlanMacLimitHighNotifEnable_Type=TruthValue
_ClcIfVlanMacLimitHighNotifEnable_Object=MibScalar
clcIfVlanMacLimitHighNotifEnable=_ClcIfVlanMacLimitHighNotifEnable_Object((1,3,6,1,4,1,9,9,313,1,4,4),_ClcIfVlanMacLimitHighNotifEnable_Type())
clcIfVlanMacLimitHighNotifEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:clcIfVlanMacLimitHighNotifEnable.setStatus(_B)
_ClcMacAddressStatsObjects_ObjectIdentity=ObjectIdentity
clcMacAddressStatsObjects=_ClcMacAddressStatsObjects_ObjectIdentity((1,3,6,1,4,1,9,9,313,1,5))
_ClcFdbMacAddressStatsTable_Object=MibTable
clcFdbMacAddressStatsTable=_ClcFdbMacAddressStatsTable_Object((1,3,6,1,4,1,9,9,313,1,5,1))
if mibBuilder.loadTexts:clcFdbMacAddressStatsTable.setStatus(_B)
_ClcFdbMacAddressStatsEntry_Object=MibTableRow
clcFdbMacAddressStatsEntry=_ClcFdbMacAddressStatsEntry_Object((1,3,6,1,4,1,9,9,313,1,5,1,1))
clcFdbMacAddressStatsEntry.setIndexNames((0,_A,_u))
if mibBuilder.loadTexts:clcFdbMacAddressStatsEntry.setStatus(_B)
_ClcFdbMacAddressStatsType_Type=ClcMacAddressStatsType
_ClcFdbMacAddressStatsType_Object=MibTableColumn
clcFdbMacAddressStatsType=_ClcFdbMacAddressStatsType_Object((1,3,6,1,4,1,9,9,313,1,5,1,1,1),_ClcFdbMacAddressStatsType_Type())
clcFdbMacAddressStatsType.setMaxAccess(_F)
if mibBuilder.loadTexts:clcFdbMacAddressStatsType.setStatus(_B)
_ClcFdbMacAddressStatsNumber_Type=Unsigned32
_ClcFdbMacAddressStatsNumber_Object=MibTableColumn
clcFdbMacAddressStatsNumber=_ClcFdbMacAddressStatsNumber_Object((1,3,6,1,4,1,9,9,313,1,5,1,1,2),_ClcFdbMacAddressStatsNumber_Type())
clcFdbMacAddressStatsNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:clcFdbMacAddressStatsNumber.setStatus(_B)
_CiscoL2ControlMIBConformance_ObjectIdentity=ObjectIdentity
ciscoL2ControlMIBConformance=_CiscoL2ControlMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,313,2))
_CiscoL2ControlMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoL2ControlMIBCompliances=_CiscoL2ControlMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,313,2,1))
_CiscoL2ControlMIBGroups_ObjectIdentity=ObjectIdentity
ciscoL2ControlMIBGroups=_CiscoL2ControlMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,313,2,2))
clcMacAddressLimitGroup=ObjectGroup((1,3,6,1,4,1,9,9,313,2,2,1))
clcMacAddressLimitGroup.setObjects(*((_A,_v),(_A,_w),(_A,_x),(_A,_y)))
if mibBuilder.loadTexts:clcMacAddressLimitGroup.setStatus(_B)
clcVlanMacAddressLimitGroup=ObjectGroup((1,3,6,1,4,1,9,9,313,2,2,2))
clcVlanMacAddressLimitGroup.setObjects(*((_A,_z),(_A,_V),(_A,_A0),(_A,_A1),(_A,_K)))
if mibBuilder.loadTexts:clcVlanMacAddressLimitGroup.setStatus(_B)
clcUnicastFloodGroup=ObjectGroup((1,3,6,1,4,1,9,9,313,2,2,4))
clcUnicastFloodGroup.setObjects(*((_A,_A2),(_A,_A3)))
if mibBuilder.loadTexts:clcUnicastFloodGroup.setStatus(_B)
clcMacAddressLimitIntervalGroup=ObjectGroup((1,3,6,1,4,1,9,9,313,2,2,5))
clcMacAddressLimitIntervalGroup.setObjects((_A,_A4))
if mibBuilder.loadTexts:clcMacAddressLimitIntervalGroup.setStatus(_B)
clcMacAddressLimitGroup1=ObjectGroup((1,3,6,1,4,1,9,9,313,2,2,6))
clcMacAddressLimitGroup1.setObjects(*((_A,_A5),(_A,_A6)))
if mibBuilder.loadTexts:clcMacAddressLimitGroup1.setStatus(_B)
clcVlanMacAddressLimitGroup1=ObjectGroup((1,3,6,1,4,1,9,9,313,2,2,7))
clcVlanMacAddressLimitGroup1.setObjects(*((_A,_W),(_A,_A7)))
if mibBuilder.loadTexts:clcVlanMacAddressLimitGroup1.setStatus(_B)
clcVlanMacLimitEnableGroup=ObjectGroup((1,3,6,1,4,1,9,9,313,2,2,8))
clcVlanMacLimitEnableGroup.setObjects((_A,_A8))
if mibBuilder.loadTexts:clcVlanMacLimitEnableGroup.setStatus(_B)
clcVlanMacLimitNotifControlGroup=ObjectGroup((1,3,6,1,4,1,9,9,313,2,2,9))
clcVlanMacLimitNotifControlGroup.setObjects((_A,_A9))
if mibBuilder.loadTexts:clcVlanMacLimitNotifControlGroup.setStatus(_B)
clcVlanMacLimitNotifControlGroup1=ObjectGroup((1,3,6,1,4,1,9,9,313,2,2,10))
clcVlanMacLimitNotifControlGroup1.setObjects((_A,_AA))
if mibBuilder.loadTexts:clcVlanMacLimitNotifControlGroup1.setStatus(_B)
clcIfMacAddressLimitGroup=ObjectGroup((1,3,6,1,4,1,9,9,313,2,2,12))
clcIfMacAddressLimitGroup.setObjects(*((_A,_AB),(_A,_X),(_A,_AC),(_A,_Y),(_A,_AD),(_A,_AE),(_A,_L)))
if mibBuilder.loadTexts:clcIfMacAddressLimitGroup.setStatus(_B)
clcIfMacLimitEnableGroup=ObjectGroup((1,3,6,1,4,1,9,9,313,2,2,13))
clcIfMacLimitEnableGroup.setObjects((_A,_AF))
if mibBuilder.loadTexts:clcIfMacLimitEnableGroup.setStatus(_B)
clcIfMacLimitNotifControlGroup=ObjectGroup((1,3,6,1,4,1,9,9,313,2,2,14))
clcIfMacLimitNotifControlGroup.setObjects(*((_A,_AG),(_A,_AH)))
if mibBuilder.loadTexts:clcIfMacLimitNotifControlGroup.setStatus(_B)
clcIfVlanMacAddressLimitGroup=ObjectGroup((1,3,6,1,4,1,9,9,313,2,2,16))
clcIfVlanMacAddressLimitGroup.setObjects(*((_A,_AI),(_A,_Z),(_A,_AJ),(_A,_a),(_A,_AK),(_A,_AL),(_A,_M)))
if mibBuilder.loadTexts:clcIfVlanMacAddressLimitGroup.setStatus(_B)
clcIfVlanMacLimitEnableGroup=ObjectGroup((1,3,6,1,4,1,9,9,313,2,2,17))
clcIfVlanMacLimitEnableGroup.setObjects((_A,_AM))
if mibBuilder.loadTexts:clcIfVlanMacLimitEnableGroup.setStatus(_B)
clcIfVlanMacLimitNotifControlGroup=ObjectGroup((1,3,6,1,4,1,9,9,313,2,2,18))
clcIfVlanMacLimitNotifControlGroup.setObjects(*((_A,_AN),(_A,_AO)))
if mibBuilder.loadTexts:clcIfVlanMacLimitNotifControlGroup.setStatus(_B)
clcMacAddressStatsGroup=ObjectGroup((1,3,6,1,4,1,9,9,313,2,2,20))
clcMacAddressStatsGroup.setObjects((_A,_AP))
if mibBuilder.loadTexts:clcMacAddressStatsGroup.setStatus(_B)
clcVlanMacLimitNotif=NotificationType((1,3,6,1,4,1,9,9,313,0,1))
clcVlanMacLimitNotif.setObjects(*((_A,_K),(_A,_V)))
if mibBuilder.loadTexts:clcVlanMacLimitNotif.setStatus(_B)
clcVlanMacLimitHighNotif=NotificationType((1,3,6,1,4,1,9,9,313,0,2))
clcVlanMacLimitHighNotif.setObjects(*((_A,_K),(_A,_W)))
if mibBuilder.loadTexts:clcVlanMacLimitHighNotif.setStatus(_B)
clcIfMacLimitLowNotif=NotificationType((1,3,6,1,4,1,9,9,313,0,3))
clcIfMacLimitLowNotif.setObjects(*((_A,_L),(_A,_X)))
if mibBuilder.loadTexts:clcIfMacLimitLowNotif.setStatus(_B)
clcIfMacLimitHighNotif=NotificationType((1,3,6,1,4,1,9,9,313,0,4))
clcIfMacLimitHighNotif.setObjects(*((_A,_L),(_A,_Y)))
if mibBuilder.loadTexts:clcIfMacLimitHighNotif.setStatus(_B)
clcIfVlanMacLimitLowNotif=NotificationType((1,3,6,1,4,1,9,9,313,0,5))
clcIfVlanMacLimitLowNotif.setObjects(*((_A,_M),(_A,_Z)))
if mibBuilder.loadTexts:clcIfVlanMacLimitLowNotif.setStatus(_B)
clcIfVlanMacLimitHighNotif=NotificationType((1,3,6,1,4,1,9,9,313,0,6))
clcIfVlanMacLimitHighNotif.setObjects(*((_A,_M),(_A,_a)))
if mibBuilder.loadTexts:clcIfVlanMacLimitHighNotif.setStatus(_B)
clcVlanMacLimitNotifsGroup=NotificationGroup((1,3,6,1,4,1,9,9,313,2,2,3))
clcVlanMacLimitNotifsGroup.setObjects((_A,_AQ))
if mibBuilder.loadTexts:clcVlanMacLimitNotifsGroup.setStatus(_B)
clcVlanMacLimitNotifsGroup1=NotificationGroup((1,3,6,1,4,1,9,9,313,2,2,11))
clcVlanMacLimitNotifsGroup1.setObjects((_A,_AR))
if mibBuilder.loadTexts:clcVlanMacLimitNotifsGroup1.setStatus(_B)
clcIfMacLimitNotifsGroup=NotificationGroup((1,3,6,1,4,1,9,9,313,2,2,15))
clcIfMacLimitNotifsGroup.setObjects(*((_A,_AS),(_A,_AT)))
if mibBuilder.loadTexts:clcIfMacLimitNotifsGroup.setStatus(_B)
clcIfVlanMacLimitNotifsGroup=NotificationGroup((1,3,6,1,4,1,9,9,313,2,2,19))
clcIfVlanMacLimitNotifsGroup.setObjects(*((_A,_AU),(_A,_AV)))
if mibBuilder.loadTexts:clcIfVlanMacLimitNotifsGroup.setStatus(_B)
ciscoL2ControlMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,313,2,1,1))
ciscoL2ControlMIBCompliance.setObjects(*((_A,_N),(_A,_O),(_A,_P),(_A,_Q)))
if mibBuilder.loadTexts:ciscoL2ControlMIBCompliance.setStatus(_AW)
ciscoL2ControlMIBCompliance2=ModuleCompliance((1,3,6,1,4,1,9,9,313,2,1,2))
ciscoL2ControlMIBCompliance2.setObjects(*((_A,_N),(_A,_b),(_A,_O),(_A,_c),(_A,_d),(_A,_e),(_A,_Q),(_A,_f),(_A,_P),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p)))
if mibBuilder.loadTexts:ciscoL2ControlMIBCompliance2.setStatus(_AW)
ciscoL2ControlMIBCompliance3=ModuleCompliance((1,3,6,1,4,1,9,9,313,2,1,3))
ciscoL2ControlMIBCompliance3.setObjects(*((_A,_N),(_A,_b),(_A,_O),(_A,_c),(_A,_d),(_A,_e),(_A,_Q),(_A,_f),(_A,_P),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_AX)))
if mibBuilder.loadTexts:ciscoL2ControlMIBCompliance3.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'MacLimitExceededAction':MacLimitExceededAction,'ClcMacAddressStatsType':ClcMacAddressStatsType,'ciscoL2ControlMIB':ciscoL2ControlMIB,'ciscoL2ControlMIBNotifs':ciscoL2ControlMIBNotifs,_AQ:clcVlanMacLimitNotif,_AR:clcVlanMacLimitHighNotif,_AS:clcIfMacLimitLowNotif,_AT:clcIfMacLimitHighNotif,_AU:clcIfVlanMacLimitLowNotif,_AV:clcIfVlanMacLimitHighNotif,'ciscoL2ControlMIBObjects':ciscoL2ControlMIBObjects,'clcMacAddressLimitObjects':clcMacAddressLimitObjects,_v:clcMacLimitEnable,_w:clcMaxMacLimitDefault,_x:clcMacLimitExceededActionDefault,_y:clcMacLimitExceedNotifOption,_A9:clcMacLimitNotifEnable,'clcVlanMacLimitTable':clcVlanMacLimitTable,'clcVlanMacLimitEntry':clcVlanMacLimitEntry,_R:clcVlanMacLimitIndex,_z:clcVlanMacLimitGlobalConfig,_V:clcVlanMaxMacLimit,_A0:clcVlanMacLimitExceededAction,_A1:clcVlanMacLimitStatus,_A8:clcVlanMacLimitEnable,_W:clcVlanMacLimitHigh,_A7:clcVlanMacLimitHighExceedAction,'clcFdbVlanInfoTable':clcFdbVlanInfoTable,'clcFdbVlanInfoEntry':clcFdbVlanInfoEntry,_K:clcFdbVlanMacUsage,_A4:clcMacLimitInterval,_A5:clcMacLimitHighDefault,_A6:clcMacLimitHighExceedActionDef,_AA:clcMacLimitHighNotifEnable,'clcUnicastFloodObjects':clcUnicastFloodObjects,'clcUnicastFloodTable':clcUnicastFloodTable,'clcUnicastFloodEntry':clcUnicastFloodEntry,_A2:clcUnicastFloodAdminEnable,_A3:clcUnicastFloodOperEnable,'clcIfMacAddressLimitObjects':clcIfMacAddressLimitObjects,'clcIfMacLimitTable':clcIfMacLimitTable,'clcIfMacLimitEntry':clcIfMacLimitEntry,_S:clcIfMacLimitIfIndex,_AF:clcIfMacLimitEnable,_AB:clcIfMacLimitGlobalConfig,_X:clcIfMacLimitLow,_AC:clcIfMacLimitLowExceedAction,_Y:clcIfMacLimitHigh,_AD:clcIfMacLimitHighExceedAction,_AE:clcIfMacLimitStatus,'clcFdbIfInfoTable':clcFdbIfInfoTable,'clcFdbIfInfoEntry':clcFdbIfInfoEntry,_L:clcFdbIfMacUsage,_AG:clcIfMacLimitLowNotifEnable,_AH:clcIfMacLimitHighNotifEnable,'clcIfVlanMacAddressLimitObjects':clcIfVlanMacAddressLimitObjects,'clcIfVlanMacLimitTable':clcIfVlanMacLimitTable,'clcIfVlanMacLimitEntry':clcIfVlanMacLimitEntry,_T:clcIfVlanMacLimitIfIndex,_U:clcIfVlanMacLimitVlanIndex,_AM:clcIfVlanMacLimitEnable,_AI:clcIfVlanMacLimitGlobalConfig,_Z:clcIfVlanMacLimitLow,_AJ:clcIfVlanMacLimitLowExceedAction,_a:clcIfVlanMacLimitHigh,_AK:clcIfVlanMacLimitHiExceedAction,_AL:clcIfVlanMacLimitStatus,'clcFdbIfVlanInfoTable':clcFdbIfVlanInfoTable,'clcFdbIfVlanInfoEntry':clcFdbIfVlanInfoEntry,_M:clcFdbIfVlanMacUsage,_AN:clcIfVlanMacLimitLowNotifEnable,_AO:clcIfVlanMacLimitHighNotifEnable,'clcMacAddressStatsObjects':clcMacAddressStatsObjects,'clcFdbMacAddressStatsTable':clcFdbMacAddressStatsTable,'clcFdbMacAddressStatsEntry':clcFdbMacAddressStatsEntry,_u:clcFdbMacAddressStatsType,_AP:clcFdbMacAddressStatsNumber,'ciscoL2ControlMIBConformance':ciscoL2ControlMIBConformance,'ciscoL2ControlMIBCompliances':ciscoL2ControlMIBCompliances,'ciscoL2ControlMIBCompliance':ciscoL2ControlMIBCompliance,'ciscoL2ControlMIBCompliance2':ciscoL2ControlMIBCompliance2,'ciscoL2ControlMIBCompliance3':ciscoL2ControlMIBCompliance3,'ciscoL2ControlMIBGroups':ciscoL2ControlMIBGroups,_N:clcMacAddressLimitGroup,_O:clcVlanMacAddressLimitGroup,_P:clcVlanMacLimitNotifsGroup,_Q:clcUnicastFloodGroup,_f:clcMacAddressLimitIntervalGroup,_b:clcMacAddressLimitGroup1,_c:clcVlanMacAddressLimitGroup1,_h:clcVlanMacLimitEnableGroup,_d:clcVlanMacLimitNotifControlGroup,_e:clcVlanMacLimitNotifControlGroup1,_g:clcVlanMacLimitNotifsGroup1,_i:clcIfMacAddressLimitGroup,_j:clcIfMacLimitEnableGroup,_k:clcIfMacLimitNotifControlGroup,_l:clcIfMacLimitNotifsGroup,_m:clcIfVlanMacAddressLimitGroup,_n:clcIfVlanMacLimitEnableGroup,_o:clcIfVlanMacLimitNotifControlGroup,_p:clcIfVlanMacLimitNotifsGroup,_AX:clcMacAddressStatsGroup})