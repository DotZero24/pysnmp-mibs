_a='h3cNdTabLen'
_Z='h3cMulticastTabLen'
_Y='h3cMulticastTabType'
_X='h3cDefaultRtOutIf'
_W='h3cDefaultRtNextHop'
_V='h3cDefaultRtNextHopType'
_U='h3cMacTabLen'
_T='h3cTrapConfigIndex'
_S='not-accessible'
_R='h3cTrapDesInfoIndex'
_Q='TruthValue'
_P='ifIndex'
_O='ifDescr'
_N='h3cRtTabLen'
_M='h3cArpTabLen'
_L='SnmpAdminString'
_K='IF-MIB'
_J='read-create'
_I='h3cDetailRtProType'
_H='seconds'
_G='disable'
_F='enable'
_E='accessible-for-notify'
_D='H3C-TRAP-MIB'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
InterfaceIndex,ifDescr,ifIndex=mibBuilder.importSymbols(_K,'InterfaceIndex',_O,_P)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_L)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TAddress','TextualConvention',_Q)
h3cTrap=ModuleIdentity((1,3,6,1,4,1,2011,10,2,38))
if mibBuilder.loadTexts:h3cTrap.setRevisions(('2010-06-05 10:50',))
_H3cTableGroup_ObjectIdentity=ObjectIdentity
h3cTableGroup=_H3cTableGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,38,1))
_H3cMacTabStatGroup_ObjectIdentity=ObjectIdentity
h3cMacTabStatGroup=_H3cMacTabStatGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,38,1,1))
class _H3cMacTabTrapEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_H3cMacTabTrapEnable_Type.__name__=_B
_H3cMacTabTrapEnable_Object=MibScalar
h3cMacTabTrapEnable=_H3cMacTabTrapEnable_Object((1,3,6,1,4,1,2011,10,2,38,1,1,1),_H3cMacTabTrapEnable_Type())
h3cMacTabTrapEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cMacTabTrapEnable.setStatus(_A)
class _H3cMacTabTrapInterval_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,3600))
_H3cMacTabTrapInterval_Type.__name__=_B
_H3cMacTabTrapInterval_Object=MibScalar
h3cMacTabTrapInterval=_H3cMacTabTrapInterval_Object((1,3,6,1,4,1,2011,10,2,38,1,1,2),_H3cMacTabTrapInterval_Type())
h3cMacTabTrapInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cMacTabTrapInterval.setStatus(_A)
if mibBuilder.loadTexts:h3cMacTabTrapInterval.setUnits(_H)
_H3cMacTabTrapInfo_ObjectIdentity=ObjectIdentity
h3cMacTabTrapInfo=_H3cMacTabTrapInfo_ObjectIdentity((1,3,6,1,4,1,2011,10,2,38,1,1,3))
_H3cMacTabLen_Type=Integer32
_H3cMacTabLen_Object=MibScalar
h3cMacTabLen=_H3cMacTabLen_Object((1,3,6,1,4,1,2011,10,2,38,1,1,3,1),_H3cMacTabLen_Type())
h3cMacTabLen.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cMacTabLen.setStatus(_A)
_H3cMacTabTrap_ObjectIdentity=ObjectIdentity
h3cMacTabTrap=_H3cMacTabTrap_ObjectIdentity((1,3,6,1,4,1,2011,10,2,38,1,1,4))
_H3cArpTabStatGroup_ObjectIdentity=ObjectIdentity
h3cArpTabStatGroup=_H3cArpTabStatGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,38,1,2))
class _H3cArpTabTrapEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_H3cArpTabTrapEnable_Type.__name__=_B
_H3cArpTabTrapEnable_Object=MibScalar
h3cArpTabTrapEnable=_H3cArpTabTrapEnable_Object((1,3,6,1,4,1,2011,10,2,38,1,2,1),_H3cArpTabTrapEnable_Type())
h3cArpTabTrapEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cArpTabTrapEnable.setStatus(_A)
class _H3cArpTabTrapInterval_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,3600))
_H3cArpTabTrapInterval_Type.__name__=_B
_H3cArpTabTrapInterval_Object=MibScalar
h3cArpTabTrapInterval=_H3cArpTabTrapInterval_Object((1,3,6,1,4,1,2011,10,2,38,1,2,2),_H3cArpTabTrapInterval_Type())
h3cArpTabTrapInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cArpTabTrapInterval.setStatus(_A)
if mibBuilder.loadTexts:h3cArpTabTrapInterval.setUnits(_H)
_H3cArpTabTrapInfo_ObjectIdentity=ObjectIdentity
h3cArpTabTrapInfo=_H3cArpTabTrapInfo_ObjectIdentity((1,3,6,1,4,1,2011,10,2,38,1,2,3))
_H3cArpTabLen_Type=Integer32
_H3cArpTabLen_Object=MibScalar
h3cArpTabLen=_H3cArpTabLen_Object((1,3,6,1,4,1,2011,10,2,38,1,2,3,1),_H3cArpTabLen_Type())
h3cArpTabLen.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cArpTabLen.setStatus(_A)
_H3cArpTabTrap_ObjectIdentity=ObjectIdentity
h3cArpTabTrap=_H3cArpTabTrap_ObjectIdentity((1,3,6,1,4,1,2011,10,2,38,1,2,4))
_H3cRtTabStatGroup_ObjectIdentity=ObjectIdentity
h3cRtTabStatGroup=_H3cRtTabStatGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,38,1,3))
_H3cDetailRtTrapTable_Object=MibTable
h3cDetailRtTrapTable=_H3cDetailRtTrapTable_Object((1,3,6,1,4,1,2011,10,2,38,1,3,1))
if mibBuilder.loadTexts:h3cDetailRtTrapTable.setStatus(_A)
_H3cDetailRtTrapEntry_Object=MibTableRow
h3cDetailRtTrapEntry=_H3cDetailRtTrapEntry_Object((1,3,6,1,4,1,2011,10,2,38,1,3,1,1))
h3cDetailRtTrapEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:h3cDetailRtTrapEntry.setStatus(_A)
class _H3cDetailRtProType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('other',1),('local',2),('rip',3),('isis',4),('ospf',5),('bgp',6)))
_H3cDetailRtProType_Type.__name__=_B
_H3cDetailRtProType_Object=MibTableColumn
h3cDetailRtProType=_H3cDetailRtProType_Object((1,3,6,1,4,1,2011,10,2,38,1,3,1,1,1),_H3cDetailRtProType_Type())
h3cDetailRtProType.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cDetailRtProType.setStatus(_A)
class _H3cDetailRtEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_H3cDetailRtEnable_Type.__name__=_B
_H3cDetailRtEnable_Object=MibTableColumn
h3cDetailRtEnable=_H3cDetailRtEnable_Object((1,3,6,1,4,1,2011,10,2,38,1,3,1,1,2),_H3cDetailRtEnable_Type())
h3cDetailRtEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDetailRtEnable.setStatus(_A)
class _H3cRtTabTrapEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_H3cRtTabTrapEnable_Type.__name__=_B
_H3cRtTabTrapEnable_Object=MibScalar
h3cRtTabTrapEnable=_H3cRtTabTrapEnable_Object((1,3,6,1,4,1,2011,10,2,38,1,3,2),_H3cRtTabTrapEnable_Type())
h3cRtTabTrapEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cRtTabTrapEnable.setStatus(_A)
class _H3cRtTabTrapInterval_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,3600))
_H3cRtTabTrapInterval_Type.__name__=_B
_H3cRtTabTrapInterval_Object=MibScalar
h3cRtTabTrapInterval=_H3cRtTabTrapInterval_Object((1,3,6,1,4,1,2011,10,2,38,1,3,3),_H3cRtTabTrapInterval_Type())
h3cRtTabTrapInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cRtTabTrapInterval.setStatus(_A)
if mibBuilder.loadTexts:h3cRtTabTrapInterval.setUnits(_H)
_H3cRtTabTrapInfo_ObjectIdentity=ObjectIdentity
h3cRtTabTrapInfo=_H3cRtTabTrapInfo_ObjectIdentity((1,3,6,1,4,1,2011,10,2,38,1,3,4))
_H3cRtTabLen_Type=Integer32
_H3cRtTabLen_Object=MibScalar
h3cRtTabLen=_H3cRtTabLen_Object((1,3,6,1,4,1,2011,10,2,38,1,3,4,1),_H3cRtTabLen_Type())
h3cRtTabLen.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cRtTabLen.setStatus(_A)
_H3cDefaultRtNextHopType_Type=InetAddressType
_H3cDefaultRtNextHopType_Object=MibScalar
h3cDefaultRtNextHopType=_H3cDefaultRtNextHopType_Object((1,3,6,1,4,1,2011,10,2,38,1,3,4,2),_H3cDefaultRtNextHopType_Type())
h3cDefaultRtNextHopType.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cDefaultRtNextHopType.setStatus(_A)
_H3cDefaultRtNextHop_Type=InetAddress
_H3cDefaultRtNextHop_Object=MibScalar
h3cDefaultRtNextHop=_H3cDefaultRtNextHop_Object((1,3,6,1,4,1,2011,10,2,38,1,3,4,3),_H3cDefaultRtNextHop_Type())
h3cDefaultRtNextHop.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cDefaultRtNextHop.setStatus(_A)
_H3cDefaultRtOutIf_Type=InterfaceIndex
_H3cDefaultRtOutIf_Object=MibScalar
h3cDefaultRtOutIf=_H3cDefaultRtOutIf_Object((1,3,6,1,4,1,2011,10,2,38,1,3,4,4),_H3cDefaultRtOutIf_Type())
h3cDefaultRtOutIf.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cDefaultRtOutIf.setStatus(_A)
_H3cRtTabTrap_ObjectIdentity=ObjectIdentity
h3cRtTabTrap=_H3cRtTabTrap_ObjectIdentity((1,3,6,1,4,1,2011,10,2,38,1,3,5))
class _H3cDefaultRtDelTrapEnable_Type(TruthValue):defaultValue=2
_H3cDefaultRtDelTrapEnable_Type.__name__=_Q
_H3cDefaultRtDelTrapEnable_Object=MibScalar
h3cDefaultRtDelTrapEnable=_H3cDefaultRtDelTrapEnable_Object((1,3,6,1,4,1,2011,10,2,38,1,3,6),_H3cDefaultRtDelTrapEnable_Type())
h3cDefaultRtDelTrapEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDefaultRtDelTrapEnable.setStatus(_A)
_H3cMulticastTabStatGroup_ObjectIdentity=ObjectIdentity
h3cMulticastTabStatGroup=_H3cMulticastTabStatGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,38,1,4))
class _H3cMulticastTabTrapEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_H3cMulticastTabTrapEnable_Type.__name__=_B
_H3cMulticastTabTrapEnable_Object=MibScalar
h3cMulticastTabTrapEnable=_H3cMulticastTabTrapEnable_Object((1,3,6,1,4,1,2011,10,2,38,1,4,1),_H3cMulticastTabTrapEnable_Type())
h3cMulticastTabTrapEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cMulticastTabTrapEnable.setStatus(_A)
class _H3cMulticastTabTrapInterval_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,3600))
_H3cMulticastTabTrapInterval_Type.__name__=_B
_H3cMulticastTabTrapInterval_Object=MibScalar
h3cMulticastTabTrapInterval=_H3cMulticastTabTrapInterval_Object((1,3,6,1,4,1,2011,10,2,38,1,4,2),_H3cMulticastTabTrapInterval_Type())
h3cMulticastTabTrapInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cMulticastTabTrapInterval.setStatus(_A)
if mibBuilder.loadTexts:h3cMulticastTabTrapInterval.setUnits(_H)
_H3cMulticastTabTrapInfo_ObjectIdentity=ObjectIdentity
h3cMulticastTabTrapInfo=_H3cMulticastTabTrapInfo_ObjectIdentity((1,3,6,1,4,1,2011,10,2,38,1,4,3))
class _H3cMulticastTabType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('lay2',1),('lay3',2)))
_H3cMulticastTabType_Type.__name__=_B
_H3cMulticastTabType_Object=MibScalar
h3cMulticastTabType=_H3cMulticastTabType_Object((1,3,6,1,4,1,2011,10,2,38,1,4,3,1),_H3cMulticastTabType_Type())
h3cMulticastTabType.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cMulticastTabType.setStatus(_A)
_H3cMulticastTabLen_Type=Integer32
_H3cMulticastTabLen_Object=MibScalar
h3cMulticastTabLen=_H3cMulticastTabLen_Object((1,3,6,1,4,1,2011,10,2,38,1,4,3,2),_H3cMulticastTabLen_Type())
h3cMulticastTabLen.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cMulticastTabLen.setStatus(_A)
_H3cMulticastTabTrap_ObjectIdentity=ObjectIdentity
h3cMulticastTabTrap=_H3cMulticastTabTrap_ObjectIdentity((1,3,6,1,4,1,2011,10,2,38,1,4,4))
_H3cNdTabStatGroup_ObjectIdentity=ObjectIdentity
h3cNdTabStatGroup=_H3cNdTabStatGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,38,1,5))
class _H3cNdTabTrapEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_H3cNdTabTrapEnable_Type.__name__=_B
_H3cNdTabTrapEnable_Object=MibScalar
h3cNdTabTrapEnable=_H3cNdTabTrapEnable_Object((1,3,6,1,4,1,2011,10,2,38,1,5,1),_H3cNdTabTrapEnable_Type())
h3cNdTabTrapEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cNdTabTrapEnable.setStatus(_A)
class _H3cNdTabTrapInterval_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,3600))
_H3cNdTabTrapInterval_Type.__name__=_B
_H3cNdTabTrapInterval_Object=MibScalar
h3cNdTabTrapInterval=_H3cNdTabTrapInterval_Object((1,3,6,1,4,1,2011,10,2,38,1,5,2),_H3cNdTabTrapInterval_Type())
h3cNdTabTrapInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cNdTabTrapInterval.setStatus(_A)
if mibBuilder.loadTexts:h3cNdTabTrapInterval.setUnits(_H)
_H3cNdTabTrapInfo_ObjectIdentity=ObjectIdentity
h3cNdTabTrapInfo=_H3cNdTabTrapInfo_ObjectIdentity((1,3,6,1,4,1,2011,10,2,38,1,5,3))
_H3cNdTabLen_Type=Integer32
_H3cNdTabLen_Object=MibScalar
h3cNdTabLen=_H3cNdTabLen_Object((1,3,6,1,4,1,2011,10,2,38,1,5,3,1),_H3cNdTabLen_Type())
h3cNdTabLen.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cNdTabLen.setStatus(_A)
_H3cNdTabTrap_ObjectIdentity=ObjectIdentity
h3cNdTabTrap=_H3cNdTabTrap_ObjectIdentity((1,3,6,1,4,1,2011,10,2,38,1,5,4))
_H3cPeriodicalTrapGroup_ObjectIdentity=ObjectIdentity
h3cPeriodicalTrapGroup=_H3cPeriodicalTrapGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,38,1,6))
_H3cPeriodicalTrapObjects_ObjectIdentity=ObjectIdentity
h3cPeriodicalTrapObjects=_H3cPeriodicalTrapObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,38,1,6,1))
class _H3cPeriodicalTrapInterval_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(10,3600))
_H3cPeriodicalTrapInterval_Type.__name__=_B
_H3cPeriodicalTrapInterval_Object=MibScalar
h3cPeriodicalTrapInterval=_H3cPeriodicalTrapInterval_Object((1,3,6,1,4,1,2011,10,2,38,1,6,1,1),_H3cPeriodicalTrapInterval_Type())
h3cPeriodicalTrapInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPeriodicalTrapInterval.setStatus(_A)
if mibBuilder.loadTexts:h3cPeriodicalTrapInterval.setUnits(_H)
class _H3cPeriodicalTrapSwitch_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_H3cPeriodicalTrapSwitch_Type.__name__=_B
_H3cPeriodicalTrapSwitch_Object=MibScalar
h3cPeriodicalTrapSwitch=_H3cPeriodicalTrapSwitch_Object((1,3,6,1,4,1,2011,10,2,38,1,6,1,2),_H3cPeriodicalTrapSwitch_Type())
h3cPeriodicalTrapSwitch.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPeriodicalTrapSwitch.setStatus(_A)
class _H3cPeriodicalTrapSwitch2_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('off',0),('on',1)))
_H3cPeriodicalTrapSwitch2_Type.__name__=_B
_H3cPeriodicalTrapSwitch2_Object=MibScalar
h3cPeriodicalTrapSwitch2=_H3cPeriodicalTrapSwitch2_Object((1,3,6,1,4,1,2011,10,2,38,1,6,1,3),_H3cPeriodicalTrapSwitch2_Type())
h3cPeriodicalTrapSwitch2.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPeriodicalTrapSwitch2.setStatus(_A)
_H3cPeriodicalTrapInfo_ObjectIdentity=ObjectIdentity
h3cPeriodicalTrapInfo=_H3cPeriodicalTrapInfo_ObjectIdentity((1,3,6,1,4,1,2011,10,2,38,1,6,2))
_H3cPeriodicalNotification_ObjectIdentity=ObjectIdentity
h3cPeriodicalNotification=_H3cPeriodicalNotification_ObjectIdentity((1,3,6,1,4,1,2011,10,2,38,1,6,3))
_H3cPeriodicalNotificationPrefix_ObjectIdentity=ObjectIdentity
h3cPeriodicalNotificationPrefix=_H3cPeriodicalNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,2011,10,2,38,1,6,3,0))
_H3cTrapDesInfo_ObjectIdentity=ObjectIdentity
h3cTrapDesInfo=_H3cTrapDesInfo_ObjectIdentity((1,3,6,1,4,1,2011,10,2,38,1,7))
_H3cTrapDesInfoTable_Object=MibTable
h3cTrapDesInfoTable=_H3cTrapDesInfoTable_Object((1,3,6,1,4,1,2011,10,2,38,1,7,1))
if mibBuilder.loadTexts:h3cTrapDesInfoTable.setStatus(_A)
_H3cTrapDesInfoEntry_Object=MibTableRow
h3cTrapDesInfoEntry=_H3cTrapDesInfoEntry_Object((1,3,6,1,4,1,2011,10,2,38,1,7,1,1))
h3cTrapDesInfoEntry.setIndexNames((0,_D,_R))
if mibBuilder.loadTexts:h3cTrapDesInfoEntry.setStatus(_A)
class _H3cTrapDesInfoIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_H3cTrapDesInfoIndex_Type.__name__=_B
_H3cTrapDesInfoIndex_Object=MibTableColumn
h3cTrapDesInfoIndex=_H3cTrapDesInfoIndex_Object((1,3,6,1,4,1,2011,10,2,38,1,7,1,1,1),_H3cTrapDesInfoIndex_Type())
h3cTrapDesInfoIndex.setMaxAccess(_S)
if mibBuilder.loadTexts:h3cTrapDesInfoIndex.setStatus(_A)
_H3cTrapDesIPAddress_Type=IpAddress
_H3cTrapDesIPAddress_Object=MibTableColumn
h3cTrapDesIPAddress=_H3cTrapDesIPAddress_Object((1,3,6,1,4,1,2011,10,2,38,1,7,1,1,2),_H3cTrapDesIPAddress_Type())
h3cTrapDesIPAddress.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cTrapDesIPAddress.setStatus(_A)
class _H3cTrapDesPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_H3cTrapDesPort_Type.__name__=_B
_H3cTrapDesPort_Object=MibTableColumn
h3cTrapDesPort=_H3cTrapDesPort_Object((1,3,6,1,4,1,2011,10,2,38,1,7,1,1,3),_H3cTrapDesPort_Type())
h3cTrapDesPort.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cTrapDesPort.setStatus(_A)
_H3cTrapDesRowStatus_Type=RowStatus
_H3cTrapDesRowStatus_Object=MibTableColumn
h3cTrapDesRowStatus=_H3cTrapDesRowStatus_Object((1,3,6,1,4,1,2011,10,2,38,1,7,1,1,4),_H3cTrapDesRowStatus_Type())
h3cTrapDesRowStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cTrapDesRowStatus.setStatus(_A)
_H3cTrapDesAddrTAddress_Type=TAddress
_H3cTrapDesAddrTAddress_Object=MibTableColumn
h3cTrapDesAddrTAddress=_H3cTrapDesAddrTAddress_Object((1,3,6,1,4,1,2011,10,2,38,1,7,1,1,5),_H3cTrapDesAddrTAddress_Type())
h3cTrapDesAddrTAddress.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cTrapDesAddrTAddress.setStatus(_A)
_H3cTrapConfig_ObjectIdentity=ObjectIdentity
h3cTrapConfig=_H3cTrapConfig_ObjectIdentity((1,3,6,1,4,1,2011,10,2,38,1,8))
_H3cTrapConfigTable_Object=MibTable
h3cTrapConfigTable=_H3cTrapConfigTable_Object((1,3,6,1,4,1,2011,10,2,38,1,8,1))
if mibBuilder.loadTexts:h3cTrapConfigTable.setStatus(_A)
_H3cTrapConfigEntry_Object=MibTableRow
h3cTrapConfigEntry=_H3cTrapConfigEntry_Object((1,3,6,1,4,1,2011,10,2,38,1,8,1,1))
h3cTrapConfigEntry.setIndexNames((0,_D,_T))
if mibBuilder.loadTexts:h3cTrapConfigEntry.setStatus(_A)
class _H3cTrapConfigIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cTrapConfigIndex_Type.__name__=_B
_H3cTrapConfigIndex_Object=MibTableColumn
h3cTrapConfigIndex=_H3cTrapConfigIndex_Object((1,3,6,1,4,1,2011,10,2,38,1,8,1,1,1),_H3cTrapConfigIndex_Type())
h3cTrapConfigIndex.setMaxAccess(_S)
if mibBuilder.loadTexts:h3cTrapConfigIndex.setStatus(_A)
class _H3cTrapConfigName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_H3cTrapConfigName_Type.__name__=_L
_H3cTrapConfigName_Object=MibTableColumn
h3cTrapConfigName=_H3cTrapConfigName_Object((1,3,6,1,4,1,2011,10,2,38,1,8,1,1,2),_H3cTrapConfigName_Type())
h3cTrapConfigName.setMaxAccess('read-only')
if mibBuilder.loadTexts:h3cTrapConfigName.setStatus(_A)
class _H3cTrapConfigDescr_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_H3cTrapConfigDescr_Type.__name__=_L
_H3cTrapConfigDescr_Object=MibTableColumn
h3cTrapConfigDescr=_H3cTrapConfigDescr_Object((1,3,6,1,4,1,2011,10,2,38,1,8,1,1,3),_H3cTrapConfigDescr_Type())
h3cTrapConfigDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cTrapConfigDescr.setStatus(_A)
class _H3cTrapConfigSwitch_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_H3cTrapConfigSwitch_Type.__name__=_B
_H3cTrapConfigSwitch_Object=MibTableColumn
h3cTrapConfigSwitch=_H3cTrapConfigSwitch_Object((1,3,6,1,4,1,2011,10,2,38,1,8,1,1,4),_H3cTrapConfigSwitch_Type())
h3cTrapConfigSwitch.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cTrapConfigSwitch.setStatus(_A)
class _H3cTrapConfigSwitch2_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('off',0),('on',1)))
_H3cTrapConfigSwitch2_Type.__name__=_B
_H3cTrapConfigSwitch2_Object=MibTableColumn
h3cTrapConfigSwitch2=_H3cTrapConfigSwitch2_Object((1,3,6,1,4,1,2011,10,2,38,1,8,1,1,5),_H3cTrapConfigSwitch2_Type())
h3cTrapConfigSwitch2.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cTrapConfigSwitch2.setStatus(_A)
h3cMacTabFullTrap=NotificationType((1,3,6,1,4,1,2011,10,2,38,1,1,4,1))
h3cMacTabFullTrap.setObjects((_D,_U))
if mibBuilder.loadTexts:h3cMacTabFullTrap.setStatus(_A)
h3cMacTabAlmostFullTrap=NotificationType((1,3,6,1,4,1,2011,10,2,38,1,1,4,2))
if mibBuilder.loadTexts:h3cMacTabAlmostFullTrap.setStatus(_A)
h3cArpTabFullTrap=NotificationType((1,3,6,1,4,1,2011,10,2,38,1,2,4,1))
h3cArpTabFullTrap.setObjects((_D,_M))
if mibBuilder.loadTexts:h3cArpTabFullTrap.setStatus(_A)
h3cArpPortDynamicEntryFullTrap=NotificationType((1,3,6,1,4,1,2011,10,2,38,1,2,4,2))
h3cArpPortDynamicEntryFullTrap.setObjects(*((_D,_M),(_K,_P),(_K,_O)))
if mibBuilder.loadTexts:h3cArpPortDynamicEntryFullTrap.setStatus(_A)
h3cRtTabFullTrap=NotificationType((1,3,6,1,4,1,2011,10,2,38,1,3,5,1))
h3cRtTabFullTrap.setObjects((_D,_N))
if mibBuilder.loadTexts:h3cRtTabFullTrap.setStatus(_A)
h3cDetailRtTabFullTrap=NotificationType((1,3,6,1,4,1,2011,10,2,38,1,3,5,2))
h3cDetailRtTabFullTrap.setObjects(*((_D,_I),(_D,_N)))
if mibBuilder.loadTexts:h3cDetailRtTabFullTrap.setStatus(_A)
h3cDefaultRtDelTrap=NotificationType((1,3,6,1,4,1,2011,10,2,38,1,3,5,3))
h3cDefaultRtDelTrap.setObjects(*((_D,_I),(_D,_V),(_D,_W),(_D,_X)))
if mibBuilder.loadTexts:h3cDefaultRtDelTrap.setStatus(_A)
h3cMulticastTabFullTrap=NotificationType((1,3,6,1,4,1,2011,10,2,38,1,4,4,1))
h3cMulticastTabFullTrap.setObjects(*((_D,_Y),(_D,_Z)))
if mibBuilder.loadTexts:h3cMulticastTabFullTrap.setStatus(_A)
h3cNdTabFullTrap=NotificationType((1,3,6,1,4,1,2011,10,2,38,1,5,4,1))
h3cNdTabFullTrap.setObjects((_D,_a))
if mibBuilder.loadTexts:h3cNdTabFullTrap.setStatus(_A)
h3cPeriodicalTrap=NotificationType((1,3,6,1,4,1,2011,10,2,38,1,6,3,0,1))
if mibBuilder.loadTexts:h3cPeriodicalTrap.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'h3cTrap':h3cTrap,'h3cTableGroup':h3cTableGroup,'h3cMacTabStatGroup':h3cMacTabStatGroup,'h3cMacTabTrapEnable':h3cMacTabTrapEnable,'h3cMacTabTrapInterval':h3cMacTabTrapInterval,'h3cMacTabTrapInfo':h3cMacTabTrapInfo,_U:h3cMacTabLen,'h3cMacTabTrap':h3cMacTabTrap,'h3cMacTabFullTrap':h3cMacTabFullTrap,'h3cMacTabAlmostFullTrap':h3cMacTabAlmostFullTrap,'h3cArpTabStatGroup':h3cArpTabStatGroup,'h3cArpTabTrapEnable':h3cArpTabTrapEnable,'h3cArpTabTrapInterval':h3cArpTabTrapInterval,'h3cArpTabTrapInfo':h3cArpTabTrapInfo,_M:h3cArpTabLen,'h3cArpTabTrap':h3cArpTabTrap,'h3cArpTabFullTrap':h3cArpTabFullTrap,'h3cArpPortDynamicEntryFullTrap':h3cArpPortDynamicEntryFullTrap,'h3cRtTabStatGroup':h3cRtTabStatGroup,'h3cDetailRtTrapTable':h3cDetailRtTrapTable,'h3cDetailRtTrapEntry':h3cDetailRtTrapEntry,_I:h3cDetailRtProType,'h3cDetailRtEnable':h3cDetailRtEnable,'h3cRtTabTrapEnable':h3cRtTabTrapEnable,'h3cRtTabTrapInterval':h3cRtTabTrapInterval,'h3cRtTabTrapInfo':h3cRtTabTrapInfo,_N:h3cRtTabLen,_V:h3cDefaultRtNextHopType,_W:h3cDefaultRtNextHop,_X:h3cDefaultRtOutIf,'h3cRtTabTrap':h3cRtTabTrap,'h3cRtTabFullTrap':h3cRtTabFullTrap,'h3cDetailRtTabFullTrap':h3cDetailRtTabFullTrap,'h3cDefaultRtDelTrap':h3cDefaultRtDelTrap,'h3cDefaultRtDelTrapEnable':h3cDefaultRtDelTrapEnable,'h3cMulticastTabStatGroup':h3cMulticastTabStatGroup,'h3cMulticastTabTrapEnable':h3cMulticastTabTrapEnable,'h3cMulticastTabTrapInterval':h3cMulticastTabTrapInterval,'h3cMulticastTabTrapInfo':h3cMulticastTabTrapInfo,_Y:h3cMulticastTabType,_Z:h3cMulticastTabLen,'h3cMulticastTabTrap':h3cMulticastTabTrap,'h3cMulticastTabFullTrap':h3cMulticastTabFullTrap,'h3cNdTabStatGroup':h3cNdTabStatGroup,'h3cNdTabTrapEnable':h3cNdTabTrapEnable,'h3cNdTabTrapInterval':h3cNdTabTrapInterval,'h3cNdTabTrapInfo':h3cNdTabTrapInfo,_a:h3cNdTabLen,'h3cNdTabTrap':h3cNdTabTrap,'h3cNdTabFullTrap':h3cNdTabFullTrap,'h3cPeriodicalTrapGroup':h3cPeriodicalTrapGroup,'h3cPeriodicalTrapObjects':h3cPeriodicalTrapObjects,'h3cPeriodicalTrapInterval':h3cPeriodicalTrapInterval,'h3cPeriodicalTrapSwitch':h3cPeriodicalTrapSwitch,'h3cPeriodicalTrapSwitch2':h3cPeriodicalTrapSwitch2,'h3cPeriodicalTrapInfo':h3cPeriodicalTrapInfo,'h3cPeriodicalNotification':h3cPeriodicalNotification,'h3cPeriodicalNotificationPrefix':h3cPeriodicalNotificationPrefix,'h3cPeriodicalTrap':h3cPeriodicalTrap,'h3cTrapDesInfo':h3cTrapDesInfo,'h3cTrapDesInfoTable':h3cTrapDesInfoTable,'h3cTrapDesInfoEntry':h3cTrapDesInfoEntry,_R:h3cTrapDesInfoIndex,'h3cTrapDesIPAddress':h3cTrapDesIPAddress,'h3cTrapDesPort':h3cTrapDesPort,'h3cTrapDesRowStatus':h3cTrapDesRowStatus,'h3cTrapDesAddrTAddress':h3cTrapDesAddrTAddress,'h3cTrapConfig':h3cTrapConfig,'h3cTrapConfigTable':h3cTrapConfigTable,'h3cTrapConfigEntry':h3cTrapConfigEntry,_T:h3cTrapConfigIndex,'h3cTrapConfigName':h3cTrapConfigName,'h3cTrapConfigDescr':h3cTrapConfigDescr,'h3cTrapConfigSwitch':h3cTrapConfigSwitch,'h3cTrapConfigSwitch2':h3cTrapConfigSwitch2})