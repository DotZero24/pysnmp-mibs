_a='hpnicfNdTabLen'
_Z='hpnicfMulticastTabLen'
_Y='hpnicfMulticastTabType'
_X='hpnicfDefaultRtOutIf'
_W='hpnicfDefaultRtNextHop'
_V='hpnicfDefaultRtNextHopType'
_U='hpnicfMacTabLen'
_T='hpnicfTrapConfigIndex'
_S='not-accessible'
_R='hpnicfTrapDesInfoIndex'
_Q='TruthValue'
_P='ifIndex'
_O='ifDescr'
_N='hpnicfRtTabLen'
_M='hpnicfArpTabLen'
_L='SnmpAdminString'
_K='IF-MIB'
_J='read-create'
_I='hpnicfDetailRtProType'
_H='seconds'
_G='disable'
_F='enable'
_E='accessible-for-notify'
_D='HPN-ICF-TRAP-MIB'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
InterfaceIndex,ifDescr,ifIndex=mibBuilder.importSymbols(_K,'InterfaceIndex',_O,_P)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_L)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TAddress','TextualConvention',_Q)
hpnicfTrap=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,38))
if mibBuilder.loadTexts:hpnicfTrap.setRevisions(('2010-06-05 10:50',))
_HpnicfTableGroup_ObjectIdentity=ObjectIdentity
hpnicfTableGroup=_HpnicfTableGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,38,1))
_HpnicfMacTabStatGroup_ObjectIdentity=ObjectIdentity
hpnicfMacTabStatGroup=_HpnicfMacTabStatGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,38,1,1))
class _HpnicfMacTabTrapEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_HpnicfMacTabTrapEnable_Type.__name__=_B
_HpnicfMacTabTrapEnable_Object=MibScalar
hpnicfMacTabTrapEnable=_HpnicfMacTabTrapEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,38,1,1,1),_HpnicfMacTabTrapEnable_Type())
hpnicfMacTabTrapEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMacTabTrapEnable.setStatus(_A)
class _HpnicfMacTabTrapInterval_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,3600))
_HpnicfMacTabTrapInterval_Type.__name__=_B
_HpnicfMacTabTrapInterval_Object=MibScalar
hpnicfMacTabTrapInterval=_HpnicfMacTabTrapInterval_Object((1,3,6,1,4,1,11,2,14,11,15,2,38,1,1,2),_HpnicfMacTabTrapInterval_Type())
hpnicfMacTabTrapInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMacTabTrapInterval.setStatus(_A)
if mibBuilder.loadTexts:hpnicfMacTabTrapInterval.setUnits(_H)
_HpnicfMacTabTrapInfo_ObjectIdentity=ObjectIdentity
hpnicfMacTabTrapInfo=_HpnicfMacTabTrapInfo_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,38,1,1,3))
_HpnicfMacTabLen_Type=Integer32
_HpnicfMacTabLen_Object=MibScalar
hpnicfMacTabLen=_HpnicfMacTabLen_Object((1,3,6,1,4,1,11,2,14,11,15,2,38,1,1,3,1),_HpnicfMacTabLen_Type())
hpnicfMacTabLen.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfMacTabLen.setStatus(_A)
_HpnicfMacTabTrap_ObjectIdentity=ObjectIdentity
hpnicfMacTabTrap=_HpnicfMacTabTrap_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,38,1,1,4))
_HpnicfArpTabStatGroup_ObjectIdentity=ObjectIdentity
hpnicfArpTabStatGroup=_HpnicfArpTabStatGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,38,1,2))
class _HpnicfArpTabTrapEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_HpnicfArpTabTrapEnable_Type.__name__=_B
_HpnicfArpTabTrapEnable_Object=MibScalar
hpnicfArpTabTrapEnable=_HpnicfArpTabTrapEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,38,1,2,1),_HpnicfArpTabTrapEnable_Type())
hpnicfArpTabTrapEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfArpTabTrapEnable.setStatus(_A)
class _HpnicfArpTabTrapInterval_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,3600))
_HpnicfArpTabTrapInterval_Type.__name__=_B
_HpnicfArpTabTrapInterval_Object=MibScalar
hpnicfArpTabTrapInterval=_HpnicfArpTabTrapInterval_Object((1,3,6,1,4,1,11,2,14,11,15,2,38,1,2,2),_HpnicfArpTabTrapInterval_Type())
hpnicfArpTabTrapInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfArpTabTrapInterval.setStatus(_A)
if mibBuilder.loadTexts:hpnicfArpTabTrapInterval.setUnits(_H)
_HpnicfArpTabTrapInfo_ObjectIdentity=ObjectIdentity
hpnicfArpTabTrapInfo=_HpnicfArpTabTrapInfo_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,38,1,2,3))
_HpnicfArpTabLen_Type=Integer32
_HpnicfArpTabLen_Object=MibScalar
hpnicfArpTabLen=_HpnicfArpTabLen_Object((1,3,6,1,4,1,11,2,14,11,15,2,38,1,2,3,1),_HpnicfArpTabLen_Type())
hpnicfArpTabLen.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfArpTabLen.setStatus(_A)
_HpnicfArpTabTrap_ObjectIdentity=ObjectIdentity
hpnicfArpTabTrap=_HpnicfArpTabTrap_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,38,1,2,4))
_HpnicfRtTabStatGroup_ObjectIdentity=ObjectIdentity
hpnicfRtTabStatGroup=_HpnicfRtTabStatGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,38,1,3))
_HpnicfDetailRtTrapTable_Object=MibTable
hpnicfDetailRtTrapTable=_HpnicfDetailRtTrapTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,38,1,3,1))
if mibBuilder.loadTexts:hpnicfDetailRtTrapTable.setStatus(_A)
_HpnicfDetailRtTrapEntry_Object=MibTableRow
hpnicfDetailRtTrapEntry=_HpnicfDetailRtTrapEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,38,1,3,1,1))
hpnicfDetailRtTrapEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:hpnicfDetailRtTrapEntry.setStatus(_A)
class _HpnicfDetailRtProType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('other',1),('local',2),('rip',3),('isis',4),('ospf',5),('bgp',6)))
_HpnicfDetailRtProType_Type.__name__=_B
_HpnicfDetailRtProType_Object=MibTableColumn
hpnicfDetailRtProType=_HpnicfDetailRtProType_Object((1,3,6,1,4,1,11,2,14,11,15,2,38,1,3,1,1,1),_HpnicfDetailRtProType_Type())
hpnicfDetailRtProType.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDetailRtProType.setStatus(_A)
class _HpnicfDetailRtEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_HpnicfDetailRtEnable_Type.__name__=_B
_HpnicfDetailRtEnable_Object=MibTableColumn
hpnicfDetailRtEnable=_HpnicfDetailRtEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,38,1,3,1,1,2),_HpnicfDetailRtEnable_Type())
hpnicfDetailRtEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDetailRtEnable.setStatus(_A)
class _HpnicfRtTabTrapEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_HpnicfRtTabTrapEnable_Type.__name__=_B
_HpnicfRtTabTrapEnable_Object=MibScalar
hpnicfRtTabTrapEnable=_HpnicfRtTabTrapEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,38,1,3,2),_HpnicfRtTabTrapEnable_Type())
hpnicfRtTabTrapEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRtTabTrapEnable.setStatus(_A)
class _HpnicfRtTabTrapInterval_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,3600))
_HpnicfRtTabTrapInterval_Type.__name__=_B
_HpnicfRtTabTrapInterval_Object=MibScalar
hpnicfRtTabTrapInterval=_HpnicfRtTabTrapInterval_Object((1,3,6,1,4,1,11,2,14,11,15,2,38,1,3,3),_HpnicfRtTabTrapInterval_Type())
hpnicfRtTabTrapInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRtTabTrapInterval.setStatus(_A)
if mibBuilder.loadTexts:hpnicfRtTabTrapInterval.setUnits(_H)
_HpnicfRtTabTrapInfo_ObjectIdentity=ObjectIdentity
hpnicfRtTabTrapInfo=_HpnicfRtTabTrapInfo_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,38,1,3,4))
_HpnicfRtTabLen_Type=Integer32
_HpnicfRtTabLen_Object=MibScalar
hpnicfRtTabLen=_HpnicfRtTabLen_Object((1,3,6,1,4,1,11,2,14,11,15,2,38,1,3,4,1),_HpnicfRtTabLen_Type())
hpnicfRtTabLen.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfRtTabLen.setStatus(_A)
_HpnicfDefaultRtNextHopType_Type=InetAddressType
_HpnicfDefaultRtNextHopType_Object=MibScalar
hpnicfDefaultRtNextHopType=_HpnicfDefaultRtNextHopType_Object((1,3,6,1,4,1,11,2,14,11,15,2,38,1,3,4,2),_HpnicfDefaultRtNextHopType_Type())
hpnicfDefaultRtNextHopType.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDefaultRtNextHopType.setStatus(_A)
_HpnicfDefaultRtNextHop_Type=InetAddress
_HpnicfDefaultRtNextHop_Object=MibScalar
hpnicfDefaultRtNextHop=_HpnicfDefaultRtNextHop_Object((1,3,6,1,4,1,11,2,14,11,15,2,38,1,3,4,3),_HpnicfDefaultRtNextHop_Type())
hpnicfDefaultRtNextHop.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDefaultRtNextHop.setStatus(_A)
_HpnicfDefaultRtOutIf_Type=InterfaceIndex
_HpnicfDefaultRtOutIf_Object=MibScalar
hpnicfDefaultRtOutIf=_HpnicfDefaultRtOutIf_Object((1,3,6,1,4,1,11,2,14,11,15,2,38,1,3,4,4),_HpnicfDefaultRtOutIf_Type())
hpnicfDefaultRtOutIf.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDefaultRtOutIf.setStatus(_A)
_HpnicfRtTabTrap_ObjectIdentity=ObjectIdentity
hpnicfRtTabTrap=_HpnicfRtTabTrap_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,38,1,3,5))
class _HpnicfDefaultRtDelTrapEnable_Type(TruthValue):defaultValue=2
_HpnicfDefaultRtDelTrapEnable_Type.__name__=_Q
_HpnicfDefaultRtDelTrapEnable_Object=MibScalar
hpnicfDefaultRtDelTrapEnable=_HpnicfDefaultRtDelTrapEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,38,1,3,6),_HpnicfDefaultRtDelTrapEnable_Type())
hpnicfDefaultRtDelTrapEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDefaultRtDelTrapEnable.setStatus(_A)
_HpnicfMulticastTabStatGroup_ObjectIdentity=ObjectIdentity
hpnicfMulticastTabStatGroup=_HpnicfMulticastTabStatGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,38,1,4))
class _HpnicfMulticastTabTrapEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_HpnicfMulticastTabTrapEnable_Type.__name__=_B
_HpnicfMulticastTabTrapEnable_Object=MibScalar
hpnicfMulticastTabTrapEnable=_HpnicfMulticastTabTrapEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,38,1,4,1),_HpnicfMulticastTabTrapEnable_Type())
hpnicfMulticastTabTrapEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMulticastTabTrapEnable.setStatus(_A)
class _HpnicfMulticastTabTrapInterval_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,3600))
_HpnicfMulticastTabTrapInterval_Type.__name__=_B
_HpnicfMulticastTabTrapInterval_Object=MibScalar
hpnicfMulticastTabTrapInterval=_HpnicfMulticastTabTrapInterval_Object((1,3,6,1,4,1,11,2,14,11,15,2,38,1,4,2),_HpnicfMulticastTabTrapInterval_Type())
hpnicfMulticastTabTrapInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMulticastTabTrapInterval.setStatus(_A)
if mibBuilder.loadTexts:hpnicfMulticastTabTrapInterval.setUnits(_H)
_HpnicfMulticastTabTrapInfo_ObjectIdentity=ObjectIdentity
hpnicfMulticastTabTrapInfo=_HpnicfMulticastTabTrapInfo_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,38,1,4,3))
class _HpnicfMulticastTabType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('lay2',1),('lay3',2)))
_HpnicfMulticastTabType_Type.__name__=_B
_HpnicfMulticastTabType_Object=MibScalar
hpnicfMulticastTabType=_HpnicfMulticastTabType_Object((1,3,6,1,4,1,11,2,14,11,15,2,38,1,4,3,1),_HpnicfMulticastTabType_Type())
hpnicfMulticastTabType.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfMulticastTabType.setStatus(_A)
_HpnicfMulticastTabLen_Type=Integer32
_HpnicfMulticastTabLen_Object=MibScalar
hpnicfMulticastTabLen=_HpnicfMulticastTabLen_Object((1,3,6,1,4,1,11,2,14,11,15,2,38,1,4,3,2),_HpnicfMulticastTabLen_Type())
hpnicfMulticastTabLen.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfMulticastTabLen.setStatus(_A)
_HpnicfMulticastTabTrap_ObjectIdentity=ObjectIdentity
hpnicfMulticastTabTrap=_HpnicfMulticastTabTrap_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,38,1,4,4))
_HpnicfNdTabStatGroup_ObjectIdentity=ObjectIdentity
hpnicfNdTabStatGroup=_HpnicfNdTabStatGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,38,1,5))
class _HpnicfNdTabTrapEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_HpnicfNdTabTrapEnable_Type.__name__=_B
_HpnicfNdTabTrapEnable_Object=MibScalar
hpnicfNdTabTrapEnable=_HpnicfNdTabTrapEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,38,1,5,1),_HpnicfNdTabTrapEnable_Type())
hpnicfNdTabTrapEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfNdTabTrapEnable.setStatus(_A)
class _HpnicfNdTabTrapInterval_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,3600))
_HpnicfNdTabTrapInterval_Type.__name__=_B
_HpnicfNdTabTrapInterval_Object=MibScalar
hpnicfNdTabTrapInterval=_HpnicfNdTabTrapInterval_Object((1,3,6,1,4,1,11,2,14,11,15,2,38,1,5,2),_HpnicfNdTabTrapInterval_Type())
hpnicfNdTabTrapInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfNdTabTrapInterval.setStatus(_A)
if mibBuilder.loadTexts:hpnicfNdTabTrapInterval.setUnits(_H)
_HpnicfNdTabTrapInfo_ObjectIdentity=ObjectIdentity
hpnicfNdTabTrapInfo=_HpnicfNdTabTrapInfo_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,38,1,5,3))
_HpnicfNdTabLen_Type=Integer32
_HpnicfNdTabLen_Object=MibScalar
hpnicfNdTabLen=_HpnicfNdTabLen_Object((1,3,6,1,4,1,11,2,14,11,15,2,38,1,5,3,1),_HpnicfNdTabLen_Type())
hpnicfNdTabLen.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfNdTabLen.setStatus(_A)
_HpnicfNdTabTrap_ObjectIdentity=ObjectIdentity
hpnicfNdTabTrap=_HpnicfNdTabTrap_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,38,1,5,4))
_HpnicfPeriodicalTrapGroup_ObjectIdentity=ObjectIdentity
hpnicfPeriodicalTrapGroup=_HpnicfPeriodicalTrapGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,38,1,6))
_HpnicfPeriodicalTrapObjects_ObjectIdentity=ObjectIdentity
hpnicfPeriodicalTrapObjects=_HpnicfPeriodicalTrapObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,38,1,6,1))
class _HpnicfPeriodicalTrapInterval_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(10,3600))
_HpnicfPeriodicalTrapInterval_Type.__name__=_B
_HpnicfPeriodicalTrapInterval_Object=MibScalar
hpnicfPeriodicalTrapInterval=_HpnicfPeriodicalTrapInterval_Object((1,3,6,1,4,1,11,2,14,11,15,2,38,1,6,1,1),_HpnicfPeriodicalTrapInterval_Type())
hpnicfPeriodicalTrapInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPeriodicalTrapInterval.setStatus(_A)
if mibBuilder.loadTexts:hpnicfPeriodicalTrapInterval.setUnits(_H)
class _HpnicfPeriodicalTrapSwitch_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_HpnicfPeriodicalTrapSwitch_Type.__name__=_B
_HpnicfPeriodicalTrapSwitch_Object=MibScalar
hpnicfPeriodicalTrapSwitch=_HpnicfPeriodicalTrapSwitch_Object((1,3,6,1,4,1,11,2,14,11,15,2,38,1,6,1,2),_HpnicfPeriodicalTrapSwitch_Type())
hpnicfPeriodicalTrapSwitch.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPeriodicalTrapSwitch.setStatus(_A)
class _HpnicfPeriodicalTrapSwitch2_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('off',0),('on',1)))
_HpnicfPeriodicalTrapSwitch2_Type.__name__=_B
_HpnicfPeriodicalTrapSwitch2_Object=MibScalar
hpnicfPeriodicalTrapSwitch2=_HpnicfPeriodicalTrapSwitch2_Object((1,3,6,1,4,1,11,2,14,11,15,2,38,1,6,1,3),_HpnicfPeriodicalTrapSwitch2_Type())
hpnicfPeriodicalTrapSwitch2.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPeriodicalTrapSwitch2.setStatus(_A)
_HpnicfPeriodicalTrapInfo_ObjectIdentity=ObjectIdentity
hpnicfPeriodicalTrapInfo=_HpnicfPeriodicalTrapInfo_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,38,1,6,2))
_HpnicfPeriodicalNotification_ObjectIdentity=ObjectIdentity
hpnicfPeriodicalNotification=_HpnicfPeriodicalNotification_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,38,1,6,3))
_HpnicfPeriodicalNotificationPrefix_ObjectIdentity=ObjectIdentity
hpnicfPeriodicalNotificationPrefix=_HpnicfPeriodicalNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,38,1,6,3,0))
_HpnicfTrapDesInfo_ObjectIdentity=ObjectIdentity
hpnicfTrapDesInfo=_HpnicfTrapDesInfo_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,38,1,7))
_HpnicfTrapDesInfoTable_Object=MibTable
hpnicfTrapDesInfoTable=_HpnicfTrapDesInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,38,1,7,1))
if mibBuilder.loadTexts:hpnicfTrapDesInfoTable.setStatus(_A)
_HpnicfTrapDesInfoEntry_Object=MibTableRow
hpnicfTrapDesInfoEntry=_HpnicfTrapDesInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,38,1,7,1,1))
hpnicfTrapDesInfoEntry.setIndexNames((0,_D,_R))
if mibBuilder.loadTexts:hpnicfTrapDesInfoEntry.setStatus(_A)
class _HpnicfTrapDesInfoIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_HpnicfTrapDesInfoIndex_Type.__name__=_B
_HpnicfTrapDesInfoIndex_Object=MibTableColumn
hpnicfTrapDesInfoIndex=_HpnicfTrapDesInfoIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,38,1,7,1,1,1),_HpnicfTrapDesInfoIndex_Type())
hpnicfTrapDesInfoIndex.setMaxAccess(_S)
if mibBuilder.loadTexts:hpnicfTrapDesInfoIndex.setStatus(_A)
_HpnicfTrapDesIPAddress_Type=IpAddress
_HpnicfTrapDesIPAddress_Object=MibTableColumn
hpnicfTrapDesIPAddress=_HpnicfTrapDesIPAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,38,1,7,1,1,2),_HpnicfTrapDesIPAddress_Type())
hpnicfTrapDesIPAddress.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfTrapDesIPAddress.setStatus(_A)
class _HpnicfTrapDesPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfTrapDesPort_Type.__name__=_B
_HpnicfTrapDesPort_Object=MibTableColumn
hpnicfTrapDesPort=_HpnicfTrapDesPort_Object((1,3,6,1,4,1,11,2,14,11,15,2,38,1,7,1,1,3),_HpnicfTrapDesPort_Type())
hpnicfTrapDesPort.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfTrapDesPort.setStatus(_A)
_HpnicfTrapDesRowStatus_Type=RowStatus
_HpnicfTrapDesRowStatus_Object=MibTableColumn
hpnicfTrapDesRowStatus=_HpnicfTrapDesRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,38,1,7,1,1,4),_HpnicfTrapDesRowStatus_Type())
hpnicfTrapDesRowStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfTrapDesRowStatus.setStatus(_A)
_HpnicfTrapDesAddrTAddress_Type=TAddress
_HpnicfTrapDesAddrTAddress_Object=MibTableColumn
hpnicfTrapDesAddrTAddress=_HpnicfTrapDesAddrTAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,38,1,7,1,1,5),_HpnicfTrapDesAddrTAddress_Type())
hpnicfTrapDesAddrTAddress.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfTrapDesAddrTAddress.setStatus(_A)
_HpnicfTrapConfig_ObjectIdentity=ObjectIdentity
hpnicfTrapConfig=_HpnicfTrapConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,38,1,8))
_HpnicfTrapConfigTable_Object=MibTable
hpnicfTrapConfigTable=_HpnicfTrapConfigTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,38,1,8,1))
if mibBuilder.loadTexts:hpnicfTrapConfigTable.setStatus(_A)
_HpnicfTrapConfigEntry_Object=MibTableRow
hpnicfTrapConfigEntry=_HpnicfTrapConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,38,1,8,1,1))
hpnicfTrapConfigEntry.setIndexNames((0,_D,_T))
if mibBuilder.loadTexts:hpnicfTrapConfigEntry.setStatus(_A)
class _HpnicfTrapConfigIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfTrapConfigIndex_Type.__name__=_B
_HpnicfTrapConfigIndex_Object=MibTableColumn
hpnicfTrapConfigIndex=_HpnicfTrapConfigIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,38,1,8,1,1,1),_HpnicfTrapConfigIndex_Type())
hpnicfTrapConfigIndex.setMaxAccess(_S)
if mibBuilder.loadTexts:hpnicfTrapConfigIndex.setStatus(_A)
class _HpnicfTrapConfigName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_HpnicfTrapConfigName_Type.__name__=_L
_HpnicfTrapConfigName_Object=MibTableColumn
hpnicfTrapConfigName=_HpnicfTrapConfigName_Object((1,3,6,1,4,1,11,2,14,11,15,2,38,1,8,1,1,2),_HpnicfTrapConfigName_Type())
hpnicfTrapConfigName.setMaxAccess('read-only')
if mibBuilder.loadTexts:hpnicfTrapConfigName.setStatus(_A)
class _HpnicfTrapConfigDescr_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_HpnicfTrapConfigDescr_Type.__name__=_L
_HpnicfTrapConfigDescr_Object=MibTableColumn
hpnicfTrapConfigDescr=_HpnicfTrapConfigDescr_Object((1,3,6,1,4,1,11,2,14,11,15,2,38,1,8,1,1,3),_HpnicfTrapConfigDescr_Type())
hpnicfTrapConfigDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfTrapConfigDescr.setStatus(_A)
class _HpnicfTrapConfigSwitch_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_HpnicfTrapConfigSwitch_Type.__name__=_B
_HpnicfTrapConfigSwitch_Object=MibTableColumn
hpnicfTrapConfigSwitch=_HpnicfTrapConfigSwitch_Object((1,3,6,1,4,1,11,2,14,11,15,2,38,1,8,1,1,4),_HpnicfTrapConfigSwitch_Type())
hpnicfTrapConfigSwitch.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfTrapConfigSwitch.setStatus(_A)
class _HpnicfTrapConfigSwitch2_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('off',0),('on',1)))
_HpnicfTrapConfigSwitch2_Type.__name__=_B
_HpnicfTrapConfigSwitch2_Object=MibTableColumn
hpnicfTrapConfigSwitch2=_HpnicfTrapConfigSwitch2_Object((1,3,6,1,4,1,11,2,14,11,15,2,38,1,8,1,1,5),_HpnicfTrapConfigSwitch2_Type())
hpnicfTrapConfigSwitch2.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfTrapConfigSwitch2.setStatus(_A)
hpnicfMacTabFullTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,38,1,1,4,1))
hpnicfMacTabFullTrap.setObjects((_D,_U))
if mibBuilder.loadTexts:hpnicfMacTabFullTrap.setStatus(_A)
hpnicfMacTabAlmostFullTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,38,1,1,4,2))
if mibBuilder.loadTexts:hpnicfMacTabAlmostFullTrap.setStatus(_A)
hpnicfArpTabFullTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,38,1,2,4,1))
hpnicfArpTabFullTrap.setObjects((_D,_M))
if mibBuilder.loadTexts:hpnicfArpTabFullTrap.setStatus(_A)
hpnicfArpPortDynamicEntryFullTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,38,1,2,4,2))
hpnicfArpPortDynamicEntryFullTrap.setObjects(*((_D,_M),(_K,_P),(_K,_O)))
if mibBuilder.loadTexts:hpnicfArpPortDynamicEntryFullTrap.setStatus(_A)
hpnicfRtTabFullTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,38,1,3,5,1))
hpnicfRtTabFullTrap.setObjects((_D,_N))
if mibBuilder.loadTexts:hpnicfRtTabFullTrap.setStatus(_A)
hpnicfDetailRtTabFullTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,38,1,3,5,2))
hpnicfDetailRtTabFullTrap.setObjects(*((_D,_I),(_D,_N)))
if mibBuilder.loadTexts:hpnicfDetailRtTabFullTrap.setStatus(_A)
hpnicfDefaultRtDelTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,38,1,3,5,3))
hpnicfDefaultRtDelTrap.setObjects(*((_D,_I),(_D,_V),(_D,_W),(_D,_X)))
if mibBuilder.loadTexts:hpnicfDefaultRtDelTrap.setStatus(_A)
hpnicfMulticastTabFullTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,38,1,4,4,1))
hpnicfMulticastTabFullTrap.setObjects(*((_D,_Y),(_D,_Z)))
if mibBuilder.loadTexts:hpnicfMulticastTabFullTrap.setStatus(_A)
hpnicfNdTabFullTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,38,1,5,4,1))
hpnicfNdTabFullTrap.setObjects((_D,_a))
if mibBuilder.loadTexts:hpnicfNdTabFullTrap.setStatus(_A)
hpnicfPeriodicalTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,38,1,6,3,0,1))
if mibBuilder.loadTexts:hpnicfPeriodicalTrap.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'hpnicfTrap':hpnicfTrap,'hpnicfTableGroup':hpnicfTableGroup,'hpnicfMacTabStatGroup':hpnicfMacTabStatGroup,'hpnicfMacTabTrapEnable':hpnicfMacTabTrapEnable,'hpnicfMacTabTrapInterval':hpnicfMacTabTrapInterval,'hpnicfMacTabTrapInfo':hpnicfMacTabTrapInfo,_U:hpnicfMacTabLen,'hpnicfMacTabTrap':hpnicfMacTabTrap,'hpnicfMacTabFullTrap':hpnicfMacTabFullTrap,'hpnicfMacTabAlmostFullTrap':hpnicfMacTabAlmostFullTrap,'hpnicfArpTabStatGroup':hpnicfArpTabStatGroup,'hpnicfArpTabTrapEnable':hpnicfArpTabTrapEnable,'hpnicfArpTabTrapInterval':hpnicfArpTabTrapInterval,'hpnicfArpTabTrapInfo':hpnicfArpTabTrapInfo,_M:hpnicfArpTabLen,'hpnicfArpTabTrap':hpnicfArpTabTrap,'hpnicfArpTabFullTrap':hpnicfArpTabFullTrap,'hpnicfArpPortDynamicEntryFullTrap':hpnicfArpPortDynamicEntryFullTrap,'hpnicfRtTabStatGroup':hpnicfRtTabStatGroup,'hpnicfDetailRtTrapTable':hpnicfDetailRtTrapTable,'hpnicfDetailRtTrapEntry':hpnicfDetailRtTrapEntry,_I:hpnicfDetailRtProType,'hpnicfDetailRtEnable':hpnicfDetailRtEnable,'hpnicfRtTabTrapEnable':hpnicfRtTabTrapEnable,'hpnicfRtTabTrapInterval':hpnicfRtTabTrapInterval,'hpnicfRtTabTrapInfo':hpnicfRtTabTrapInfo,_N:hpnicfRtTabLen,_V:hpnicfDefaultRtNextHopType,_W:hpnicfDefaultRtNextHop,_X:hpnicfDefaultRtOutIf,'hpnicfRtTabTrap':hpnicfRtTabTrap,'hpnicfRtTabFullTrap':hpnicfRtTabFullTrap,'hpnicfDetailRtTabFullTrap':hpnicfDetailRtTabFullTrap,'hpnicfDefaultRtDelTrap':hpnicfDefaultRtDelTrap,'hpnicfDefaultRtDelTrapEnable':hpnicfDefaultRtDelTrapEnable,'hpnicfMulticastTabStatGroup':hpnicfMulticastTabStatGroup,'hpnicfMulticastTabTrapEnable':hpnicfMulticastTabTrapEnable,'hpnicfMulticastTabTrapInterval':hpnicfMulticastTabTrapInterval,'hpnicfMulticastTabTrapInfo':hpnicfMulticastTabTrapInfo,_Y:hpnicfMulticastTabType,_Z:hpnicfMulticastTabLen,'hpnicfMulticastTabTrap':hpnicfMulticastTabTrap,'hpnicfMulticastTabFullTrap':hpnicfMulticastTabFullTrap,'hpnicfNdTabStatGroup':hpnicfNdTabStatGroup,'hpnicfNdTabTrapEnable':hpnicfNdTabTrapEnable,'hpnicfNdTabTrapInterval':hpnicfNdTabTrapInterval,'hpnicfNdTabTrapInfo':hpnicfNdTabTrapInfo,_a:hpnicfNdTabLen,'hpnicfNdTabTrap':hpnicfNdTabTrap,'hpnicfNdTabFullTrap':hpnicfNdTabFullTrap,'hpnicfPeriodicalTrapGroup':hpnicfPeriodicalTrapGroup,'hpnicfPeriodicalTrapObjects':hpnicfPeriodicalTrapObjects,'hpnicfPeriodicalTrapInterval':hpnicfPeriodicalTrapInterval,'hpnicfPeriodicalTrapSwitch':hpnicfPeriodicalTrapSwitch,'hpnicfPeriodicalTrapSwitch2':hpnicfPeriodicalTrapSwitch2,'hpnicfPeriodicalTrapInfo':hpnicfPeriodicalTrapInfo,'hpnicfPeriodicalNotification':hpnicfPeriodicalNotification,'hpnicfPeriodicalNotificationPrefix':hpnicfPeriodicalNotificationPrefix,'hpnicfPeriodicalTrap':hpnicfPeriodicalTrap,'hpnicfTrapDesInfo':hpnicfTrapDesInfo,'hpnicfTrapDesInfoTable':hpnicfTrapDesInfoTable,'hpnicfTrapDesInfoEntry':hpnicfTrapDesInfoEntry,_R:hpnicfTrapDesInfoIndex,'hpnicfTrapDesIPAddress':hpnicfTrapDesIPAddress,'hpnicfTrapDesPort':hpnicfTrapDesPort,'hpnicfTrapDesRowStatus':hpnicfTrapDesRowStatus,'hpnicfTrapDesAddrTAddress':hpnicfTrapDesAddrTAddress,'hpnicfTrapConfig':hpnicfTrapConfig,'hpnicfTrapConfigTable':hpnicfTrapConfigTable,'hpnicfTrapConfigEntry':hpnicfTrapConfigEntry,_T:hpnicfTrapConfigIndex,'hpnicfTrapConfigName':hpnicfTrapConfigName,'hpnicfTrapConfigDescr':hpnicfTrapConfigDescr,'hpnicfTrapConfigSwitch':hpnicfTrapConfigSwitch,'hpnicfTrapConfigSwitch2':hpnicfTrapConfigSwitch2})