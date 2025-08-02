_AU='hpUnknownUcastLimitIngressPortConfigGroup2'
_AT='hpEgressRateLimitPortQueueConfigEntryGroup'
_AS='hpEgressRateLimitPortConfigGroup3'
_AR='hpicfIngressRateLimitVlanGroup'
_AQ='hpIngressRateLimitPortConfigGroup'
_AP='hpEgressRateLimitPortConfigGroup'
_AO='hpMcastLimitIngressPortConfigGroup'
_AN='hpBcastLimitIngressPortConfigGroup'
_AM='hpICMPRateLimitPortConfigGroup2'
_AL='hpICMPRateLimitPortConfigGroup'
_AK='hpICMPRateLimitPortNotification'
_AJ='hpEgressRateLimitPortQueueMax'
_AI='hpEgressRateLimitPortQueueControlMode'
_AH='hpUnknownUnicastLimitPortSingleControlKbps'
_AG='hpicfIngressRateLimitVlanKbps'
_AF='hpicfIngressRateLimitVlanControlMode'
_AE='hpICMPRateLimitPortIpPacketType'
_AD='hpIngressMcastLimitPortSingleControlKbps'
_AC='hpIngressBcastLimitPortSingleControlKbps'
_AB='hpIngressRateLimitPortBps'
_AA='hpIngressRateLimitPortSingleControlBps'
_A9='hpEgressRateLimitPortBps'
_A8='hpEgressRateLimitPortSingleControlBps'
_A7='hpBWMinEgressPortPrct'
_A6='hpBWMinEgressPortNumQueues'
_A5='hpBWMinIngressPortPrct'
_A4='hpBWMinIngressPortNumQueues'
_A3='hpICMPRateLimitPortState'
_A2='hpicfIngressRateLimitVlanIndex'
_A1='hpUnknownUnicastLimitPortIndex'
_A0='hpIngressMcastLimitPortIndex'
_z='hpIngressBcastLimitPortIndex'
_y='hpIngressRateLimitPortBpsQueue'
_x='hpIngressRateLimitPortPrctQueue'
_w='hpEgressRateLimitPortQueueIndex'
_v='hpEgressRateLimitPortBpsQueue'
_u='hpEgressRateLimitPortPrctQueue'
_t='hpBWMinIngressPortPrctQueue'
_s='hpBWMinEgressPortPrctQueue'
_r='hpICMPRateLimitPortConfigIndex'
_q='hpMcastLimitIngressPortConfigGroup2'
_p='hpBcastLimitIngressPortConfigGroup2'
_o='hpICMPRateLimitPortConfigGroup3'
_n='hpUnknownUcastLimitIngressPortConfigGroup'
_m='hpEgressRateLimitPortConfigGroup2'
_l='hpUnknownUnicastLimitPortSingleControlPrct'
_k='hpUnknownUnicastLimitPortControlMode'
_j='hpIngressMcastLimitPortSingleControlPrct'
_i='hpIngressMcastLimitPortControlMode'
_h='hpIngressBcastLimitPortSingleControlPrct'
_g='hpIngressBcastLimitPortControlMode'
_f='hpICMPRateLimitPortControlMode'
_e='hpICMPRateLimitPortKbps'
_d='hpIngressRateLimitPortSingleControlKbps'
_c='hpIngressRateLimitPortPrct'
_b='hpIngressRateLimitPortSingleControlPrct'
_a='hpIngressRateLimitPortControlMode'
_Z='hpIngressRateLimitPortNumQueues'
_Y='ifIndex'
_X='IF-MIB'
_W='hpIngressRateLimitPortConfigGroup2'
_V='hpBWMinEgressPortConfigGroup'
_U='hpBWMinIngressPortConfigGroup'
_T='hpEgressRateLimitPortSingleControlKbps'
_S='hpEgressRateLimitPortPrct'
_R='hpEgressRateLimitPortSingleControlPrct'
_Q='hpEgressRateLimitPortControlMode'
_P='hpEgressRateLimitPortNumQueues'
_O='hpICMPRateLimitPortAlarmFlag'
_N='hpICMPRateLimitPortPrct'
_M='hpIngressRateLimitPortIndex'
_L='read-only'
_K='hpICMPRateLimitPortNotifyGroup'
_J='hpICMPRateLimitNotifyPortIndex'
_I='hpEgressRateLimitPortIndex'
_H='Unsigned32'
_G='disabled'
_F='not-accessible'
_E='deprecated'
_D='read-write'
_C='Integer32'
_B='current'
_A='HP-ICF-RATE-LIMIT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpicfObjectModules,hpicfRateLimitTrapsPrefix=mibBuilder.importSymbols('HP-ICF-OID','hpicfObjectModules','hpicfRateLimitTrapsPrefix')
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_X,'InterfaceIndex',_Y)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hpicfRateLimitMIB=ModuleIdentity((1,3,6,1,4,1,11,2,14,10,2,14))
if mibBuilder.loadTexts:hpicfRateLimitMIB.setRevisions(('2017-10-13 00:00','2016-08-03 00:00','2015-09-04 00:00','2014-11-18 10:00','2014-11-17 00:00','2013-07-11 00:00','2013-03-12 15:10','2012-10-05 19:30','2012-03-12 12:30','2010-09-27 11:30','2010-07-14 16:10','2007-12-04 12:30','2007-08-29 11:20','2007-07-27 19:20','2007-06-01 11:46','2007-05-30 16:10','2006-07-07 18:33','2005-04-20 11:30','2004-08-22 10:30'))
_HpicfRateLimitObjects_ObjectIdentity=ObjectIdentity
hpicfRateLimitObjects=_HpicfRateLimitObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,10,2,14,1))
_HpicfICMPRateLimitObjects_ObjectIdentity=ObjectIdentity
hpicfICMPRateLimitObjects=_HpicfICMPRateLimitObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,10,2,14,1,1))
_HpICMPRateLimitConfig_ObjectIdentity=ObjectIdentity
hpICMPRateLimitConfig=_HpICMPRateLimitConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,10,2,14,1,1,1))
_HpICMPRateLimitPortConfigTable_Object=MibTable
hpICMPRateLimitPortConfigTable=_HpICMPRateLimitPortConfigTable_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,1,1,1))
if mibBuilder.loadTexts:hpICMPRateLimitPortConfigTable.setStatus(_B)
_HpICMPRateLimitPortConfigEntry_Object=MibTableRow
hpICMPRateLimitPortConfigEntry=_HpICMPRateLimitPortConfigEntry_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,1,1,1,1))
hpICMPRateLimitPortConfigEntry.setIndexNames((0,_A,_r))
if mibBuilder.loadTexts:hpICMPRateLimitPortConfigEntry.setStatus(_B)
_HpICMPRateLimitPortConfigIndex_Type=InterfaceIndex
_HpICMPRateLimitPortConfigIndex_Object=MibTableColumn
hpICMPRateLimitPortConfigIndex=_HpICMPRateLimitPortConfigIndex_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,1,1,1,1,1),_HpICMPRateLimitPortConfigIndex_Type())
hpICMPRateLimitPortConfigIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpICMPRateLimitPortConfigIndex.setStatus(_B)
class _HpICMPRateLimitPortState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),(_G,2)))
_HpICMPRateLimitPortState_Type.__name__=_C
_HpICMPRateLimitPortState_Object=MibTableColumn
hpICMPRateLimitPortState=_HpICMPRateLimitPortState_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,1,1,1,1,2),_HpICMPRateLimitPortState_Type())
hpICMPRateLimitPortState.setMaxAccess(_D)
if mibBuilder.loadTexts:hpICMPRateLimitPortState.setStatus(_E)
class _HpICMPRateLimitPortPrct_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpICMPRateLimitPortPrct_Type.__name__=_C
_HpICMPRateLimitPortPrct_Object=MibTableColumn
hpICMPRateLimitPortPrct=_HpICMPRateLimitPortPrct_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,1,1,1,1,3),_HpICMPRateLimitPortPrct_Type())
hpICMPRateLimitPortPrct.setMaxAccess(_D)
if mibBuilder.loadTexts:hpICMPRateLimitPortPrct.setStatus(_B)
class _HpICMPRateLimitPortAlarmFlag_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('clear',1),('set',2)))
_HpICMPRateLimitPortAlarmFlag_Type.__name__=_C
_HpICMPRateLimitPortAlarmFlag_Object=MibTableColumn
hpICMPRateLimitPortAlarmFlag=_HpICMPRateLimitPortAlarmFlag_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,1,1,1,1,4),_HpICMPRateLimitPortAlarmFlag_Type())
hpICMPRateLimitPortAlarmFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:hpICMPRateLimitPortAlarmFlag.setStatus(_B)
_HpICMPRateLimitPortKbps_Type=Integer32
_HpICMPRateLimitPortKbps_Object=MibTableColumn
hpICMPRateLimitPortKbps=_HpICMPRateLimitPortKbps_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,1,1,1,1,5),_HpICMPRateLimitPortKbps_Type())
hpICMPRateLimitPortKbps.setMaxAccess(_D)
if mibBuilder.loadTexts:hpICMPRateLimitPortKbps.setStatus(_B)
class _HpICMPRateLimitPortControlMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),('portPrct',2),('portKbps',3)))
_HpICMPRateLimitPortControlMode_Type.__name__=_C
_HpICMPRateLimitPortControlMode_Object=MibTableColumn
hpICMPRateLimitPortControlMode=_HpICMPRateLimitPortControlMode_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,1,1,1,1,6),_HpICMPRateLimitPortControlMode_Type())
hpICMPRateLimitPortControlMode.setMaxAccess(_D)
if mibBuilder.loadTexts:hpICMPRateLimitPortControlMode.setStatus(_B)
class _HpICMPRateLimitPortIpPacketType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ipv4PacketsOnly',1),('ipv6PacketsOnly',2),('ipv4AndIpv6Packets',3)))
_HpICMPRateLimitPortIpPacketType_Type.__name__=_C
_HpICMPRateLimitPortIpPacketType_Object=MibTableColumn
hpICMPRateLimitPortIpPacketType=_HpICMPRateLimitPortIpPacketType_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,1,1,1,1,7),_HpICMPRateLimitPortIpPacketType_Type())
hpICMPRateLimitPortIpPacketType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpICMPRateLimitPortIpPacketType.setStatus(_B)
_HpICMPRateLimitNotifyPortIndex_Type=InterfaceIndex
_HpICMPRateLimitNotifyPortIndex_Object=MibScalar
hpICMPRateLimitNotifyPortIndex=_HpICMPRateLimitNotifyPortIndex_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,1,2),_HpICMPRateLimitNotifyPortIndex_Type())
hpICMPRateLimitNotifyPortIndex.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:hpICMPRateLimitNotifyPortIndex.setStatus(_B)
_HpicfBWMinEgressObjects_ObjectIdentity=ObjectIdentity
hpicfBWMinEgressObjects=_HpicfBWMinEgressObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,10,2,14,1,2))
_HpBWMinEgressPortConfig_ObjectIdentity=ObjectIdentity
hpBWMinEgressPortConfig=_HpBWMinEgressPortConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,10,2,14,1,2,1))
_HpBWMinEgressPortNumQueues_Type=Integer32
_HpBWMinEgressPortNumQueues_Object=MibScalar
hpBWMinEgressPortNumQueues=_HpBWMinEgressPortNumQueues_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,2,1,1),_HpBWMinEgressPortNumQueues_Type())
hpBWMinEgressPortNumQueues.setMaxAccess(_L)
if mibBuilder.loadTexts:hpBWMinEgressPortNumQueues.setStatus(_B)
_HpBWMinEgressPortPrctTable_Object=MibTable
hpBWMinEgressPortPrctTable=_HpBWMinEgressPortPrctTable_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,2,1,2))
if mibBuilder.loadTexts:hpBWMinEgressPortPrctTable.setStatus(_B)
_HpBWMinEgressPortPrctEntry_Object=MibTableRow
hpBWMinEgressPortPrctEntry=_HpBWMinEgressPortPrctEntry_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,2,1,2,1))
hpBWMinEgressPortPrctEntry.setIndexNames((0,_X,_Y),(0,_A,_s))
if mibBuilder.loadTexts:hpBWMinEgressPortPrctEntry.setStatus(_B)
class _HpBWMinEgressPortPrctQueue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,9000))
_HpBWMinEgressPortPrctQueue_Type.__name__=_C
_HpBWMinEgressPortPrctQueue_Object=MibTableColumn
hpBWMinEgressPortPrctQueue=_HpBWMinEgressPortPrctQueue_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,2,1,2,1,1),_HpBWMinEgressPortPrctQueue_Type())
hpBWMinEgressPortPrctQueue.setMaxAccess(_F)
if mibBuilder.loadTexts:hpBWMinEgressPortPrctQueue.setStatus(_B)
class _HpBWMinEgressPortPrct_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpBWMinEgressPortPrct_Type.__name__=_C
_HpBWMinEgressPortPrct_Object=MibTableColumn
hpBWMinEgressPortPrct=_HpBWMinEgressPortPrct_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,2,1,2,1,2),_HpBWMinEgressPortPrct_Type())
hpBWMinEgressPortPrct.setMaxAccess(_D)
if mibBuilder.loadTexts:hpBWMinEgressPortPrct.setStatus(_B)
_HpicfBWMinIngressObjects_ObjectIdentity=ObjectIdentity
hpicfBWMinIngressObjects=_HpicfBWMinIngressObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,10,2,14,1,3))
_HpBWMinIngressPortConfig_ObjectIdentity=ObjectIdentity
hpBWMinIngressPortConfig=_HpBWMinIngressPortConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,10,2,14,1,3,1))
_HpBWMinIngressPortNumQueues_Type=Integer32
_HpBWMinIngressPortNumQueues_Object=MibScalar
hpBWMinIngressPortNumQueues=_HpBWMinIngressPortNumQueues_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,3,1,1),_HpBWMinIngressPortNumQueues_Type())
hpBWMinIngressPortNumQueues.setMaxAccess(_L)
if mibBuilder.loadTexts:hpBWMinIngressPortNumQueues.setStatus(_B)
_HpBWMinIngressPortPrctTable_Object=MibTable
hpBWMinIngressPortPrctTable=_HpBWMinIngressPortPrctTable_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,3,1,2))
if mibBuilder.loadTexts:hpBWMinIngressPortPrctTable.setStatus(_B)
_HpBWMinIngressPortPrctEntry_Object=MibTableRow
hpBWMinIngressPortPrctEntry=_HpBWMinIngressPortPrctEntry_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,3,1,2,1))
hpBWMinIngressPortPrctEntry.setIndexNames((0,_X,_Y),(0,_A,_t))
if mibBuilder.loadTexts:hpBWMinIngressPortPrctEntry.setStatus(_B)
class _HpBWMinIngressPortPrctQueue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,9000))
_HpBWMinIngressPortPrctQueue_Type.__name__=_C
_HpBWMinIngressPortPrctQueue_Object=MibTableColumn
hpBWMinIngressPortPrctQueue=_HpBWMinIngressPortPrctQueue_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,3,1,2,1,1),_HpBWMinIngressPortPrctQueue_Type())
hpBWMinIngressPortPrctQueue.setMaxAccess(_F)
if mibBuilder.loadTexts:hpBWMinIngressPortPrctQueue.setStatus(_B)
class _HpBWMinIngressPortPrct_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpBWMinIngressPortPrct_Type.__name__=_C
_HpBWMinIngressPortPrct_Object=MibTableColumn
hpBWMinIngressPortPrct=_HpBWMinIngressPortPrct_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,3,1,2,1,2),_HpBWMinIngressPortPrct_Type())
hpBWMinIngressPortPrct.setMaxAccess(_D)
if mibBuilder.loadTexts:hpBWMinIngressPortPrct.setStatus(_B)
_HpicfRateLimitPortObjects_ObjectIdentity=ObjectIdentity
hpicfRateLimitPortObjects=_HpicfRateLimitPortObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,10,2,14,1,4))
_HpRateLimitPortConfig_ObjectIdentity=ObjectIdentity
hpRateLimitPortConfig=_HpRateLimitPortConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,10,2,14,1,4,1))
_HpEgressRateLimitPortNumQueues_Type=Integer32
_HpEgressRateLimitPortNumQueues_Object=MibScalar
hpEgressRateLimitPortNumQueues=_HpEgressRateLimitPortNumQueues_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,4,1,1),_HpEgressRateLimitPortNumQueues_Type())
hpEgressRateLimitPortNumQueues.setMaxAccess(_L)
if mibBuilder.loadTexts:hpEgressRateLimitPortNumQueues.setStatus(_B)
_HpEgressRateLimitPortConfigTable_Object=MibTable
hpEgressRateLimitPortConfigTable=_HpEgressRateLimitPortConfigTable_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,4,1,2))
if mibBuilder.loadTexts:hpEgressRateLimitPortConfigTable.setStatus(_B)
_HpEgressRateLimitPortConfigEntry_Object=MibTableRow
hpEgressRateLimitPortConfigEntry=_HpEgressRateLimitPortConfigEntry_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,4,1,2,1))
hpEgressRateLimitPortConfigEntry.setIndexNames((0,_A,_I))
if mibBuilder.loadTexts:hpEgressRateLimitPortConfigEntry.setStatus(_B)
_HpEgressRateLimitPortIndex_Type=InterfaceIndex
_HpEgressRateLimitPortIndex_Object=MibTableColumn
hpEgressRateLimitPortIndex=_HpEgressRateLimitPortIndex_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,4,1,2,1,1),_HpEgressRateLimitPortIndex_Type())
hpEgressRateLimitPortIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpEgressRateLimitPortIndex.setStatus(_B)
class _HpEgressRateLimitPortControlMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_G,1),('egressRateLimitPerPortOnly',2),('egressRateLimitPerQueue',3),('egressRateLimitPerPortOnlyBpsMode',4),('egressRateLimitPerQueueBpsMode',5),('egressRateLimitPerPortOnlyKbpsMode',6)))
_HpEgressRateLimitPortControlMode_Type.__name__=_C
_HpEgressRateLimitPortControlMode_Object=MibTableColumn
hpEgressRateLimitPortControlMode=_HpEgressRateLimitPortControlMode_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,4,1,2,1,2),_HpEgressRateLimitPortControlMode_Type())
hpEgressRateLimitPortControlMode.setMaxAccess(_D)
if mibBuilder.loadTexts:hpEgressRateLimitPortControlMode.setStatus(_B)
class _HpEgressRateLimitPortSingleControlPrct_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpEgressRateLimitPortSingleControlPrct_Type.__name__=_C
_HpEgressRateLimitPortSingleControlPrct_Object=MibTableColumn
hpEgressRateLimitPortSingleControlPrct=_HpEgressRateLimitPortSingleControlPrct_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,4,1,2,1,3),_HpEgressRateLimitPortSingleControlPrct_Type())
hpEgressRateLimitPortSingleControlPrct.setMaxAccess(_D)
if mibBuilder.loadTexts:hpEgressRateLimitPortSingleControlPrct.setStatus(_B)
class _HpEgressRateLimitPortSingleControlBps_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4200000000))
_HpEgressRateLimitPortSingleControlBps_Type.__name__=_H
_HpEgressRateLimitPortSingleControlBps_Object=MibTableColumn
hpEgressRateLimitPortSingleControlBps=_HpEgressRateLimitPortSingleControlBps_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,4,1,2,1,4),_HpEgressRateLimitPortSingleControlBps_Type())
hpEgressRateLimitPortSingleControlBps.setMaxAccess(_D)
if mibBuilder.loadTexts:hpEgressRateLimitPortSingleControlBps.setStatus(_E)
class _HpEgressRateLimitPortSingleControlKbps_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000000))
_HpEgressRateLimitPortSingleControlKbps_Type.__name__=_C
_HpEgressRateLimitPortSingleControlKbps_Object=MibTableColumn
hpEgressRateLimitPortSingleControlKbps=_HpEgressRateLimitPortSingleControlKbps_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,4,1,2,1,5),_HpEgressRateLimitPortSingleControlKbps_Type())
hpEgressRateLimitPortSingleControlKbps.setMaxAccess(_D)
if mibBuilder.loadTexts:hpEgressRateLimitPortSingleControlKbps.setStatus(_B)
class _HpEgressRateLimitPortQueueControlMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),('egressRateLimitQueuePrctMode',2),('egressRateLimitQueueKbpsMode',3)))
_HpEgressRateLimitPortQueueControlMode_Type.__name__=_C
_HpEgressRateLimitPortQueueControlMode_Object=MibTableColumn
hpEgressRateLimitPortQueueControlMode=_HpEgressRateLimitPortQueueControlMode_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,4,1,2,1,6),_HpEgressRateLimitPortQueueControlMode_Type())
hpEgressRateLimitPortQueueControlMode.setMaxAccess(_D)
if mibBuilder.loadTexts:hpEgressRateLimitPortQueueControlMode.setStatus(_B)
_HpEgressRateLimitPortPrctTable_Object=MibTable
hpEgressRateLimitPortPrctTable=_HpEgressRateLimitPortPrctTable_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,4,1,3))
if mibBuilder.loadTexts:hpEgressRateLimitPortPrctTable.setStatus(_B)
_HpEgressRateLimitPortPrctEntry_Object=MibTableRow
hpEgressRateLimitPortPrctEntry=_HpEgressRateLimitPortPrctEntry_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,4,1,3,1))
hpEgressRateLimitPortPrctEntry.setIndexNames((0,_A,_I),(0,_A,_u))
if mibBuilder.loadTexts:hpEgressRateLimitPortPrctEntry.setStatus(_B)
class _HpEgressRateLimitPortPrctQueue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,9000))
_HpEgressRateLimitPortPrctQueue_Type.__name__=_C
_HpEgressRateLimitPortPrctQueue_Object=MibTableColumn
hpEgressRateLimitPortPrctQueue=_HpEgressRateLimitPortPrctQueue_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,4,1,3,1,1),_HpEgressRateLimitPortPrctQueue_Type())
hpEgressRateLimitPortPrctQueue.setMaxAccess(_F)
if mibBuilder.loadTexts:hpEgressRateLimitPortPrctQueue.setStatus(_B)
class _HpEgressRateLimitPortPrct_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpEgressRateLimitPortPrct_Type.__name__=_C
_HpEgressRateLimitPortPrct_Object=MibTableColumn
hpEgressRateLimitPortPrct=_HpEgressRateLimitPortPrct_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,4,1,3,1,2),_HpEgressRateLimitPortPrct_Type())
hpEgressRateLimitPortPrct.setMaxAccess(_D)
if mibBuilder.loadTexts:hpEgressRateLimitPortPrct.setStatus(_B)
_HpEgressRateLimitPortBpsTable_Object=MibTable
hpEgressRateLimitPortBpsTable=_HpEgressRateLimitPortBpsTable_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,4,1,4))
if mibBuilder.loadTexts:hpEgressRateLimitPortBpsTable.setStatus(_E)
_HpEgressRateLimitPortBpsEntry_Object=MibTableRow
hpEgressRateLimitPortBpsEntry=_HpEgressRateLimitPortBpsEntry_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,4,1,4,1))
hpEgressRateLimitPortBpsEntry.setIndexNames((0,_A,_I),(0,_A,_v))
if mibBuilder.loadTexts:hpEgressRateLimitPortBpsEntry.setStatus(_E)
class _HpEgressRateLimitPortBpsQueue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_HpEgressRateLimitPortBpsQueue_Type.__name__=_C
_HpEgressRateLimitPortBpsQueue_Object=MibTableColumn
hpEgressRateLimitPortBpsQueue=_HpEgressRateLimitPortBpsQueue_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,4,1,4,1,1),_HpEgressRateLimitPortBpsQueue_Type())
hpEgressRateLimitPortBpsQueue.setMaxAccess(_F)
if mibBuilder.loadTexts:hpEgressRateLimitPortBpsQueue.setStatus(_E)
class _HpEgressRateLimitPortBps_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4200000000))
_HpEgressRateLimitPortBps_Type.__name__=_H
_HpEgressRateLimitPortBps_Object=MibTableColumn
hpEgressRateLimitPortBps=_HpEgressRateLimitPortBps_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,4,1,4,1,2),_HpEgressRateLimitPortBps_Type())
hpEgressRateLimitPortBps.setMaxAccess(_D)
if mibBuilder.loadTexts:hpEgressRateLimitPortBps.setStatus(_E)
_HpEgressRateLimitPortQueueConfigTable_Object=MibTable
hpEgressRateLimitPortQueueConfigTable=_HpEgressRateLimitPortQueueConfigTable_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,4,1,5))
if mibBuilder.loadTexts:hpEgressRateLimitPortQueueConfigTable.setStatus(_B)
_HpEgressRateLimitPortQueueConfigEntry_Object=MibTableRow
hpEgressRateLimitPortQueueConfigEntry=_HpEgressRateLimitPortQueueConfigEntry_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,4,1,5,1))
hpEgressRateLimitPortQueueConfigEntry.setIndexNames((0,_A,_I),(0,_A,_w))
if mibBuilder.loadTexts:hpEgressRateLimitPortQueueConfigEntry.setStatus(_B)
class _HpEgressRateLimitPortQueueIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,9000))
_HpEgressRateLimitPortQueueIndex_Type.__name__=_C
_HpEgressRateLimitPortQueueIndex_Object=MibTableColumn
hpEgressRateLimitPortQueueIndex=_HpEgressRateLimitPortQueueIndex_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,4,1,5,1,1),_HpEgressRateLimitPortQueueIndex_Type())
hpEgressRateLimitPortQueueIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpEgressRateLimitPortQueueIndex.setStatus(_B)
class _HpEgressRateLimitPortQueueMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000000))
_HpEgressRateLimitPortQueueMax_Type.__name__=_C
_HpEgressRateLimitPortQueueMax_Object=MibTableColumn
hpEgressRateLimitPortQueueMax=_HpEgressRateLimitPortQueueMax_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,4,1,5,1,2),_HpEgressRateLimitPortQueueMax_Type())
hpEgressRateLimitPortQueueMax.setMaxAccess(_D)
if mibBuilder.loadTexts:hpEgressRateLimitPortQueueMax.setStatus(_B)
_HpicfIngressRateLimitPortObjects_ObjectIdentity=ObjectIdentity
hpicfIngressRateLimitPortObjects=_HpicfIngressRateLimitPortObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,10,2,14,1,5))
_HpRateLimitIngressPortConfig_ObjectIdentity=ObjectIdentity
hpRateLimitIngressPortConfig=_HpRateLimitIngressPortConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,10,2,14,1,5,1))
_HpIngressRateLimitPortNumQueues_Type=Integer32
_HpIngressRateLimitPortNumQueues_Object=MibScalar
hpIngressRateLimitPortNumQueues=_HpIngressRateLimitPortNumQueues_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,5,1,1),_HpIngressRateLimitPortNumQueues_Type())
hpIngressRateLimitPortNumQueues.setMaxAccess(_L)
if mibBuilder.loadTexts:hpIngressRateLimitPortNumQueues.setStatus(_B)
_HpIngressRateLimitPortConfigTable_Object=MibTable
hpIngressRateLimitPortConfigTable=_HpIngressRateLimitPortConfigTable_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,5,1,2))
if mibBuilder.loadTexts:hpIngressRateLimitPortConfigTable.setStatus(_B)
_HpIngressRateLimitPortConfigEntry_Object=MibTableRow
hpIngressRateLimitPortConfigEntry=_HpIngressRateLimitPortConfigEntry_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,5,1,2,1))
hpIngressRateLimitPortConfigEntry.setIndexNames((0,_A,_M))
if mibBuilder.loadTexts:hpIngressRateLimitPortConfigEntry.setStatus(_B)
_HpIngressRateLimitPortIndex_Type=InterfaceIndex
_HpIngressRateLimitPortIndex_Object=MibTableColumn
hpIngressRateLimitPortIndex=_HpIngressRateLimitPortIndex_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,5,1,2,1,1),_HpIngressRateLimitPortIndex_Type())
hpIngressRateLimitPortIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpIngressRateLimitPortIndex.setStatus(_B)
class _HpIngressRateLimitPortControlMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_G,1),('ingressRateLimitPerPortOnly',2),('ingressRateLimitPerQueue',3),('ingressRateLimitPerPortOnlyBpsMode',4),('ingressRateLimitPerQueueBpsMode',5),('ingressRateLimitPerPortOnlyKbpsMode',6)))
_HpIngressRateLimitPortControlMode_Type.__name__=_C
_HpIngressRateLimitPortControlMode_Object=MibTableColumn
hpIngressRateLimitPortControlMode=_HpIngressRateLimitPortControlMode_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,5,1,2,1,2),_HpIngressRateLimitPortControlMode_Type())
hpIngressRateLimitPortControlMode.setMaxAccess(_D)
if mibBuilder.loadTexts:hpIngressRateLimitPortControlMode.setStatus(_B)
class _HpIngressRateLimitPortSingleControlPrct_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpIngressRateLimitPortSingleControlPrct_Type.__name__=_C
_HpIngressRateLimitPortSingleControlPrct_Object=MibTableColumn
hpIngressRateLimitPortSingleControlPrct=_HpIngressRateLimitPortSingleControlPrct_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,5,1,2,1,3),_HpIngressRateLimitPortSingleControlPrct_Type())
hpIngressRateLimitPortSingleControlPrct.setMaxAccess(_D)
if mibBuilder.loadTexts:hpIngressRateLimitPortSingleControlPrct.setStatus(_B)
class _HpIngressRateLimitPortSingleControlBps_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4200000000))
_HpIngressRateLimitPortSingleControlBps_Type.__name__=_H
_HpIngressRateLimitPortSingleControlBps_Object=MibTableColumn
hpIngressRateLimitPortSingleControlBps=_HpIngressRateLimitPortSingleControlBps_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,5,1,2,1,4),_HpIngressRateLimitPortSingleControlBps_Type())
hpIngressRateLimitPortSingleControlBps.setMaxAccess(_D)
if mibBuilder.loadTexts:hpIngressRateLimitPortSingleControlBps.setStatus(_E)
class _HpIngressRateLimitPortSingleControlKbps_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000000))
_HpIngressRateLimitPortSingleControlKbps_Type.__name__=_C
_HpIngressRateLimitPortSingleControlKbps_Object=MibTableColumn
hpIngressRateLimitPortSingleControlKbps=_HpIngressRateLimitPortSingleControlKbps_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,5,1,2,1,5),_HpIngressRateLimitPortSingleControlKbps_Type())
hpIngressRateLimitPortSingleControlKbps.setMaxAccess(_D)
if mibBuilder.loadTexts:hpIngressRateLimitPortSingleControlKbps.setStatus(_B)
_HpIngressRateLimitPortPrctTable_Object=MibTable
hpIngressRateLimitPortPrctTable=_HpIngressRateLimitPortPrctTable_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,5,1,3))
if mibBuilder.loadTexts:hpIngressRateLimitPortPrctTable.setStatus(_B)
_HpIngressRateLimitPortPrctEntry_Object=MibTableRow
hpIngressRateLimitPortPrctEntry=_HpIngressRateLimitPortPrctEntry_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,5,1,3,1))
hpIngressRateLimitPortPrctEntry.setIndexNames((0,_A,_M),(0,_A,_x))
if mibBuilder.loadTexts:hpIngressRateLimitPortPrctEntry.setStatus(_B)
class _HpIngressRateLimitPortPrctQueue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,9000))
_HpIngressRateLimitPortPrctQueue_Type.__name__=_C
_HpIngressRateLimitPortPrctQueue_Object=MibTableColumn
hpIngressRateLimitPortPrctQueue=_HpIngressRateLimitPortPrctQueue_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,5,1,3,1,1),_HpIngressRateLimitPortPrctQueue_Type())
hpIngressRateLimitPortPrctQueue.setMaxAccess(_F)
if mibBuilder.loadTexts:hpIngressRateLimitPortPrctQueue.setStatus(_B)
class _HpIngressRateLimitPortPrct_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpIngressRateLimitPortPrct_Type.__name__=_C
_HpIngressRateLimitPortPrct_Object=MibTableColumn
hpIngressRateLimitPortPrct=_HpIngressRateLimitPortPrct_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,5,1,3,1,2),_HpIngressRateLimitPortPrct_Type())
hpIngressRateLimitPortPrct.setMaxAccess(_D)
if mibBuilder.loadTexts:hpIngressRateLimitPortPrct.setStatus(_B)
_HpIngressRateLimitPortBpsTable_Object=MibTable
hpIngressRateLimitPortBpsTable=_HpIngressRateLimitPortBpsTable_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,5,1,4))
if mibBuilder.loadTexts:hpIngressRateLimitPortBpsTable.setStatus(_E)
_HpIngressRateLimitPortBpsEntry_Object=MibTableRow
hpIngressRateLimitPortBpsEntry=_HpIngressRateLimitPortBpsEntry_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,5,1,4,1))
hpIngressRateLimitPortBpsEntry.setIndexNames((0,_A,_M),(0,_A,_y))
if mibBuilder.loadTexts:hpIngressRateLimitPortBpsEntry.setStatus(_E)
class _HpIngressRateLimitPortBpsQueue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_HpIngressRateLimitPortBpsQueue_Type.__name__=_C
_HpIngressRateLimitPortBpsQueue_Object=MibTableColumn
hpIngressRateLimitPortBpsQueue=_HpIngressRateLimitPortBpsQueue_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,5,1,4,1,1),_HpIngressRateLimitPortBpsQueue_Type())
hpIngressRateLimitPortBpsQueue.setMaxAccess(_F)
if mibBuilder.loadTexts:hpIngressRateLimitPortBpsQueue.setStatus(_E)
class _HpIngressRateLimitPortBps_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4200000000))
_HpIngressRateLimitPortBps_Type.__name__=_H
_HpIngressRateLimitPortBps_Object=MibTableColumn
hpIngressRateLimitPortBps=_HpIngressRateLimitPortBps_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,5,1,4,1,2),_HpIngressRateLimitPortBps_Type())
hpIngressRateLimitPortBps.setMaxAccess(_D)
if mibBuilder.loadTexts:hpIngressRateLimitPortBps.setStatus(_E)
_HpicfIngressBcastLimitPortObjects_ObjectIdentity=ObjectIdentity
hpicfIngressBcastLimitPortObjects=_HpicfIngressBcastLimitPortObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,10,2,14,1,6))
_HpBcastLimitIngressPortConfig_ObjectIdentity=ObjectIdentity
hpBcastLimitIngressPortConfig=_HpBcastLimitIngressPortConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,10,2,14,1,6,1))
_HpIngressBcastLimitPortConfigTable_Object=MibTable
hpIngressBcastLimitPortConfigTable=_HpIngressBcastLimitPortConfigTable_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,6,1,1))
if mibBuilder.loadTexts:hpIngressBcastLimitPortConfigTable.setStatus(_B)
_HpIngressBcastLimitPortConfigEntry_Object=MibTableRow
hpIngressBcastLimitPortConfigEntry=_HpIngressBcastLimitPortConfigEntry_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,6,1,1,1))
hpIngressBcastLimitPortConfigEntry.setIndexNames((0,_A,_z))
if mibBuilder.loadTexts:hpIngressBcastLimitPortConfigEntry.setStatus(_B)
_HpIngressBcastLimitPortIndex_Type=InterfaceIndex
_HpIngressBcastLimitPortIndex_Object=MibTableColumn
hpIngressBcastLimitPortIndex=_HpIngressBcastLimitPortIndex_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,6,1,1,1,1),_HpIngressBcastLimitPortIndex_Type())
hpIngressBcastLimitPortIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpIngressBcastLimitPortIndex.setStatus(_B)
class _HpIngressBcastLimitPortControlMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),('ingressBcastLimitPerPortOnly',2),('ingressBcastLimitPerPortOnlyKbpsMode',3)))
_HpIngressBcastLimitPortControlMode_Type.__name__=_C
_HpIngressBcastLimitPortControlMode_Object=MibTableColumn
hpIngressBcastLimitPortControlMode=_HpIngressBcastLimitPortControlMode_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,6,1,1,1,2),_HpIngressBcastLimitPortControlMode_Type())
hpIngressBcastLimitPortControlMode.setMaxAccess(_D)
if mibBuilder.loadTexts:hpIngressBcastLimitPortControlMode.setStatus(_B)
class _HpIngressBcastLimitPortSingleControlPrct_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpIngressBcastLimitPortSingleControlPrct_Type.__name__=_C
_HpIngressBcastLimitPortSingleControlPrct_Object=MibTableColumn
hpIngressBcastLimitPortSingleControlPrct=_HpIngressBcastLimitPortSingleControlPrct_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,6,1,1,1,3),_HpIngressBcastLimitPortSingleControlPrct_Type())
hpIngressBcastLimitPortSingleControlPrct.setMaxAccess(_D)
if mibBuilder.loadTexts:hpIngressBcastLimitPortSingleControlPrct.setStatus(_B)
class _HpIngressBcastLimitPortSingleControlKbps_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000000))
_HpIngressBcastLimitPortSingleControlKbps_Type.__name__=_C
_HpIngressBcastLimitPortSingleControlKbps_Object=MibTableColumn
hpIngressBcastLimitPortSingleControlKbps=_HpIngressBcastLimitPortSingleControlKbps_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,6,1,1,1,4),_HpIngressBcastLimitPortSingleControlKbps_Type())
hpIngressBcastLimitPortSingleControlKbps.setMaxAccess(_D)
if mibBuilder.loadTexts:hpIngressBcastLimitPortSingleControlKbps.setStatus(_B)
_HpicfIngressMcastLimitPortObjects_ObjectIdentity=ObjectIdentity
hpicfIngressMcastLimitPortObjects=_HpicfIngressMcastLimitPortObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,10,2,14,1,7))
_HpMcastLimitIngressPortConfig_ObjectIdentity=ObjectIdentity
hpMcastLimitIngressPortConfig=_HpMcastLimitIngressPortConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,10,2,14,1,7,1))
_HpIngressMcastLimitPortConfigTable_Object=MibTable
hpIngressMcastLimitPortConfigTable=_HpIngressMcastLimitPortConfigTable_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,7,1,1))
if mibBuilder.loadTexts:hpIngressMcastLimitPortConfigTable.setStatus(_B)
_HpIngressMcastLimitPortConfigEntry_Object=MibTableRow
hpIngressMcastLimitPortConfigEntry=_HpIngressMcastLimitPortConfigEntry_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,7,1,1,1))
hpIngressMcastLimitPortConfigEntry.setIndexNames((0,_A,_A0))
if mibBuilder.loadTexts:hpIngressMcastLimitPortConfigEntry.setStatus(_B)
_HpIngressMcastLimitPortIndex_Type=InterfaceIndex
_HpIngressMcastLimitPortIndex_Object=MibTableColumn
hpIngressMcastLimitPortIndex=_HpIngressMcastLimitPortIndex_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,7,1,1,1,1),_HpIngressMcastLimitPortIndex_Type())
hpIngressMcastLimitPortIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpIngressMcastLimitPortIndex.setStatus(_B)
class _HpIngressMcastLimitPortControlMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),('ingressMcastLimitPerPortOnly',2),('ingressMcastLimitPerPortOnlyKbpsMode',3)))
_HpIngressMcastLimitPortControlMode_Type.__name__=_C
_HpIngressMcastLimitPortControlMode_Object=MibTableColumn
hpIngressMcastLimitPortControlMode=_HpIngressMcastLimitPortControlMode_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,7,1,1,1,2),_HpIngressMcastLimitPortControlMode_Type())
hpIngressMcastLimitPortControlMode.setMaxAccess(_D)
if mibBuilder.loadTexts:hpIngressMcastLimitPortControlMode.setStatus(_B)
class _HpIngressMcastLimitPortSingleControlPrct_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpIngressMcastLimitPortSingleControlPrct_Type.__name__=_C
_HpIngressMcastLimitPortSingleControlPrct_Object=MibTableColumn
hpIngressMcastLimitPortSingleControlPrct=_HpIngressMcastLimitPortSingleControlPrct_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,7,1,1,1,3),_HpIngressMcastLimitPortSingleControlPrct_Type())
hpIngressMcastLimitPortSingleControlPrct.setMaxAccess(_D)
if mibBuilder.loadTexts:hpIngressMcastLimitPortSingleControlPrct.setStatus(_B)
class _HpIngressMcastLimitPortSingleControlKbps_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000000))
_HpIngressMcastLimitPortSingleControlKbps_Type.__name__=_C
_HpIngressMcastLimitPortSingleControlKbps_Object=MibTableColumn
hpIngressMcastLimitPortSingleControlKbps=_HpIngressMcastLimitPortSingleControlKbps_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,7,1,1,1,4),_HpIngressMcastLimitPortSingleControlKbps_Type())
hpIngressMcastLimitPortSingleControlKbps.setMaxAccess(_D)
if mibBuilder.loadTexts:hpIngressMcastLimitPortSingleControlKbps.setStatus(_B)
_HpicfUnknownUnicastLimitPortObjects_ObjectIdentity=ObjectIdentity
hpicfUnknownUnicastLimitPortObjects=_HpicfUnknownUnicastLimitPortObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,10,2,14,1,8))
_HpUnknownUnicastLimitPortConfig_ObjectIdentity=ObjectIdentity
hpUnknownUnicastLimitPortConfig=_HpUnknownUnicastLimitPortConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,10,2,14,1,8,1))
_HpUnknownUnicastLimitConfigTable_Object=MibTable
hpUnknownUnicastLimitConfigTable=_HpUnknownUnicastLimitConfigTable_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,8,1,1))
if mibBuilder.loadTexts:hpUnknownUnicastLimitConfigTable.setStatus(_B)
_HpUnknownUnicastLimitConfigEntry_Object=MibTableRow
hpUnknownUnicastLimitConfigEntry=_HpUnknownUnicastLimitConfigEntry_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,8,1,1,1))
hpUnknownUnicastLimitConfigEntry.setIndexNames((0,_A,_A1))
if mibBuilder.loadTexts:hpUnknownUnicastLimitConfigEntry.setStatus(_B)
_HpUnknownUnicastLimitPortIndex_Type=InterfaceIndex
_HpUnknownUnicastLimitPortIndex_Object=MibTableColumn
hpUnknownUnicastLimitPortIndex=_HpUnknownUnicastLimitPortIndex_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,8,1,1,1,1),_HpUnknownUnicastLimitPortIndex_Type())
hpUnknownUnicastLimitPortIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpUnknownUnicastLimitPortIndex.setStatus(_B)
class _HpUnknownUnicastLimitPortControlMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),('unknownUnicastLimitPerPortOnly',2),('unknownUnicastLimitPerPortOnlyKbpsMode',3)))
_HpUnknownUnicastLimitPortControlMode_Type.__name__=_C
_HpUnknownUnicastLimitPortControlMode_Object=MibTableColumn
hpUnknownUnicastLimitPortControlMode=_HpUnknownUnicastLimitPortControlMode_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,8,1,1,1,2),_HpUnknownUnicastLimitPortControlMode_Type())
hpUnknownUnicastLimitPortControlMode.setMaxAccess(_D)
if mibBuilder.loadTexts:hpUnknownUnicastLimitPortControlMode.setStatus(_B)
class _HpUnknownUnicastLimitPortSingleControlPrct_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpUnknownUnicastLimitPortSingleControlPrct_Type.__name__=_C
_HpUnknownUnicastLimitPortSingleControlPrct_Object=MibTableColumn
hpUnknownUnicastLimitPortSingleControlPrct=_HpUnknownUnicastLimitPortSingleControlPrct_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,8,1,1,1,3),_HpUnknownUnicastLimitPortSingleControlPrct_Type())
hpUnknownUnicastLimitPortSingleControlPrct.setMaxAccess(_D)
if mibBuilder.loadTexts:hpUnknownUnicastLimitPortSingleControlPrct.setStatus(_B)
class _HpUnknownUnicastLimitPortSingleControlKbps_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000000))
_HpUnknownUnicastLimitPortSingleControlKbps_Type.__name__=_C
_HpUnknownUnicastLimitPortSingleControlKbps_Object=MibTableColumn
hpUnknownUnicastLimitPortSingleControlKbps=_HpUnknownUnicastLimitPortSingleControlKbps_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,8,1,1,1,4),_HpUnknownUnicastLimitPortSingleControlKbps_Type())
hpUnknownUnicastLimitPortSingleControlKbps.setMaxAccess(_D)
if mibBuilder.loadTexts:hpUnknownUnicastLimitPortSingleControlKbps.setStatus(_B)
_HpicfIngressRateLimitVlanObjects_ObjectIdentity=ObjectIdentity
hpicfIngressRateLimitVlanObjects=_HpicfIngressRateLimitVlanObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,10,2,14,1,9))
_HpicfIngressRateLimitVlanConfigTable_Object=MibTable
hpicfIngressRateLimitVlanConfigTable=_HpicfIngressRateLimitVlanConfigTable_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,9,1))
if mibBuilder.loadTexts:hpicfIngressRateLimitVlanConfigTable.setStatus(_B)
_HpicfIngressRateLimitVlanConfigEntry_Object=MibTableRow
hpicfIngressRateLimitVlanConfigEntry=_HpicfIngressRateLimitVlanConfigEntry_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,9,1,1))
hpicfIngressRateLimitVlanConfigEntry.setIndexNames((0,_A,_A2))
if mibBuilder.loadTexts:hpicfIngressRateLimitVlanConfigEntry.setStatus(_B)
_HpicfIngressRateLimitVlanIndex_Type=InterfaceIndex
_HpicfIngressRateLimitVlanIndex_Object=MibTableColumn
hpicfIngressRateLimitVlanIndex=_HpicfIngressRateLimitVlanIndex_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,9,1,1,1),_HpicfIngressRateLimitVlanIndex_Type())
hpicfIngressRateLimitVlanIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpicfIngressRateLimitVlanIndex.setStatus(_B)
class _HpicfIngressRateLimitVlanControlMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),('ingressVlanKbps',2)))
_HpicfIngressRateLimitVlanControlMode_Type.__name__=_C
_HpicfIngressRateLimitVlanControlMode_Object=MibTableColumn
hpicfIngressRateLimitVlanControlMode=_HpicfIngressRateLimitVlanControlMode_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,9,1,1,2),_HpicfIngressRateLimitVlanControlMode_Type())
hpicfIngressRateLimitVlanControlMode.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfIngressRateLimitVlanControlMode.setStatus(_B)
class _HpicfIngressRateLimitVlanKbps_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,260000000))
_HpicfIngressRateLimitVlanKbps_Type.__name__=_H
_HpicfIngressRateLimitVlanKbps_Object=MibTableColumn
hpicfIngressRateLimitVlanKbps=_HpicfIngressRateLimitVlanKbps_Object((1,3,6,1,4,1,11,2,14,10,2,14,1,9,1,1,3),_HpicfIngressRateLimitVlanKbps_Type())
hpicfIngressRateLimitVlanKbps.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfIngressRateLimitVlanKbps.setStatus(_B)
_HpicfRateLimitConformance_ObjectIdentity=ObjectIdentity
hpicfRateLimitConformance=_HpicfRateLimitConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,10,2,14,2))
_HpicfRateLimitGroups_ObjectIdentity=ObjectIdentity
hpicfRateLimitGroups=_HpicfRateLimitGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,10,2,14,2,1))
_HpicfRateLimitCompliances_ObjectIdentity=ObjectIdentity
hpicfRateLimitCompliances=_HpicfRateLimitCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,10,2,14,2,2))
hpICMPRateLimitPortConfigGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,10,2,14,2,1,1))
hpICMPRateLimitPortConfigGroup.setObjects(*((_A,_A3),(_A,_N),(_A,_O),(_A,_J)))
if mibBuilder.loadTexts:hpICMPRateLimitPortConfigGroup.setStatus(_E)
hpBWMinIngressPortConfigGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,10,2,14,2,1,3))
hpBWMinIngressPortConfigGroup.setObjects(*((_A,_A4),(_A,_A5)))
if mibBuilder.loadTexts:hpBWMinIngressPortConfigGroup.setStatus(_B)
hpBWMinEgressPortConfigGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,10,2,14,2,1,4))
hpBWMinEgressPortConfigGroup.setObjects(*((_A,_A6),(_A,_A7)))
if mibBuilder.loadTexts:hpBWMinEgressPortConfigGroup.setStatus(_B)
hpEgressRateLimitPortConfigGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,10,2,14,2,1,5))
hpEgressRateLimitPortConfigGroup.setObjects(*((_A,_P),(_A,_Q),(_A,_R),(_A,_A8),(_A,_S),(_A,_A9),(_A,_T)))
if mibBuilder.loadTexts:hpEgressRateLimitPortConfigGroup.setStatus(_E)
hpIngressRateLimitPortConfigGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,10,2,14,2,1,6))
hpIngressRateLimitPortConfigGroup.setObjects(*((_A,_Z),(_A,_a),(_A,_b),(_A,_AA),(_A,_c),(_A,_AB),(_A,_d)))
if mibBuilder.loadTexts:hpIngressRateLimitPortConfigGroup.setStatus(_E)
hpICMPRateLimitPortConfigGroup2=ObjectGroup((1,3,6,1,4,1,11,2,14,10,2,14,2,1,7))
hpICMPRateLimitPortConfigGroup2.setObjects(*((_A,_N),(_A,_O),(_A,_J),(_A,_e),(_A,_f)))
if mibBuilder.loadTexts:hpICMPRateLimitPortConfigGroup2.setStatus(_E)
hpEgressRateLimitPortConfigGroup2=ObjectGroup((1,3,6,1,4,1,11,2,14,10,2,14,2,1,8))
hpEgressRateLimitPortConfigGroup2.setObjects(*((_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T)))
if mibBuilder.loadTexts:hpEgressRateLimitPortConfigGroup2.setStatus(_E)
hpIngressRateLimitPortConfigGroup2=ObjectGroup((1,3,6,1,4,1,11,2,14,10,2,14,2,1,9))
hpIngressRateLimitPortConfigGroup2.setObjects(*((_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d)))
if mibBuilder.loadTexts:hpIngressRateLimitPortConfigGroup2.setStatus(_B)
hpBcastLimitIngressPortConfigGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,10,2,14,2,1,10))
hpBcastLimitIngressPortConfigGroup.setObjects(*((_A,_g),(_A,_h)))
if mibBuilder.loadTexts:hpBcastLimitIngressPortConfigGroup.setStatus(_E)
hpMcastLimitIngressPortConfigGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,10,2,14,2,1,11))
hpMcastLimitIngressPortConfigGroup.setObjects(*((_A,_i),(_A,_j)))
if mibBuilder.loadTexts:hpMcastLimitIngressPortConfigGroup.setStatus(_B)
hpBcastLimitIngressPortConfigGroup2=ObjectGroup((1,3,6,1,4,1,11,2,14,10,2,14,2,1,12))
hpBcastLimitIngressPortConfigGroup2.setObjects(*((_A,_g),(_A,_h),(_A,_AC)))
if mibBuilder.loadTexts:hpBcastLimitIngressPortConfigGroup2.setStatus(_B)
hpMcastLimitIngressPortConfigGroup2=ObjectGroup((1,3,6,1,4,1,11,2,14,10,2,14,2,1,13))
hpMcastLimitIngressPortConfigGroup2.setObjects(*((_A,_i),(_A,_j),(_A,_AD)))
if mibBuilder.loadTexts:hpMcastLimitIngressPortConfigGroup2.setStatus(_B)
hpICMPRateLimitPortConfigGroup3=ObjectGroup((1,3,6,1,4,1,11,2,14,10,2,14,2,1,14))
hpICMPRateLimitPortConfigGroup3.setObjects(*((_A,_N),(_A,_O),(_A,_J),(_A,_e),(_A,_f),(_A,_AE)))
if mibBuilder.loadTexts:hpICMPRateLimitPortConfigGroup3.setStatus(_B)
hpUnknownUcastLimitIngressPortConfigGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,10,2,14,2,1,15))
hpUnknownUcastLimitIngressPortConfigGroup.setObjects(*((_A,_k),(_A,_l)))
if mibBuilder.loadTexts:hpUnknownUcastLimitIngressPortConfigGroup.setStatus(_E)
hpicfIngressRateLimitVlanGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,10,2,14,2,1,16))
hpicfIngressRateLimitVlanGroup.setObjects(*((_A,_AF),(_A,_AG)))
if mibBuilder.loadTexts:hpicfIngressRateLimitVlanGroup.setStatus(_B)
hpUnknownUcastLimitIngressPortConfigGroup2=ObjectGroup((1,3,6,1,4,1,11,2,14,10,2,14,2,1,17))
hpUnknownUcastLimitIngressPortConfigGroup2.setObjects(*((_A,_k),(_A,_l),(_A,_AH)))
if mibBuilder.loadTexts:hpUnknownUcastLimitIngressPortConfigGroup2.setStatus(_B)
hpEgressRateLimitPortConfigGroup3=ObjectGroup((1,3,6,1,4,1,11,2,14,10,2,14,2,1,18))
hpEgressRateLimitPortConfigGroup3.setObjects(*((_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_AI)))
if mibBuilder.loadTexts:hpEgressRateLimitPortConfigGroup3.setStatus(_B)
hpEgressRateLimitPortQueueConfigEntryGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,10,2,14,2,1,19))
hpEgressRateLimitPortQueueConfigEntryGroup.setObjects((_A,_AJ))
if mibBuilder.loadTexts:hpEgressRateLimitPortQueueConfigEntryGroup.setStatus(_B)
hpICMPRateLimitPortNotification=NotificationType((1,3,6,1,4,1,11,2,14,12,5,0,1))
hpICMPRateLimitPortNotification.setObjects((_A,_J))
if mibBuilder.loadTexts:hpICMPRateLimitPortNotification.setStatus(_B)
hpICMPRateLimitPortNotifyGroup=NotificationGroup((1,3,6,1,4,1,11,2,14,10,2,14,2,1,2))
hpICMPRateLimitPortNotifyGroup.setObjects((_A,_AK))
if mibBuilder.loadTexts:hpICMPRateLimitPortNotifyGroup.setStatus(_B)
hpicfRateLimitCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,10,2,14,2,2,1))
hpicfRateLimitCompliance.setObjects(*((_A,_AL),(_A,_K)))
if mibBuilder.loadTexts:hpicfRateLimitCompliance.setStatus(_E)
hpicfRateLimitCompliance1=ModuleCompliance((1,3,6,1,4,1,11,2,14,10,2,14,2,2,2))
hpicfRateLimitCompliance1.setObjects(*((_A,_AM),(_A,_K),(_A,_U),(_A,_V),(_A,_m),(_A,_W),(_A,_AN),(_A,_AO),(_A,_n)))
if mibBuilder.loadTexts:hpicfRateLimitCompliance1.setStatus(_E)
hpicfRateLimitCompliance2=ModuleCompliance((1,3,6,1,4,1,11,2,14,10,2,14,2,2,3))
hpicfRateLimitCompliance2.setObjects(*((_A,_o),(_A,_K),(_A,_V),(_A,_U),(_A,_AP),(_A,_m),(_A,_AQ),(_A,_W),(_A,_p),(_A,_q),(_A,_n)))
if mibBuilder.loadTexts:hpicfRateLimitCompliance2.setStatus(_E)
hpicfRateLimitCompliance3=ModuleCompliance((1,3,6,1,4,1,11,2,14,10,2,14,2,2,4))
hpicfRateLimitCompliance3.setObjects((_A,_AR))
if mibBuilder.loadTexts:hpicfRateLimitCompliance3.setStatus(_B)
hpicfRateLimitCompliance4=ModuleCompliance((1,3,6,1,4,1,11,2,14,10,2,14,2,2,5))
hpicfRateLimitCompliance4.setObjects(*((_A,_o),(_A,_K),(_A,_V),(_A,_U),(_A,_AS),(_A,_AT),(_A,_W),(_A,_p),(_A,_q),(_A,_AU)))
if mibBuilder.loadTexts:hpicfRateLimitCompliance4.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'hpicfRateLimitMIB':hpicfRateLimitMIB,'hpicfRateLimitObjects':hpicfRateLimitObjects,'hpicfICMPRateLimitObjects':hpicfICMPRateLimitObjects,'hpICMPRateLimitConfig':hpICMPRateLimitConfig,'hpICMPRateLimitPortConfigTable':hpICMPRateLimitPortConfigTable,'hpICMPRateLimitPortConfigEntry':hpICMPRateLimitPortConfigEntry,_r:hpICMPRateLimitPortConfigIndex,_A3:hpICMPRateLimitPortState,_N:hpICMPRateLimitPortPrct,_O:hpICMPRateLimitPortAlarmFlag,_e:hpICMPRateLimitPortKbps,_f:hpICMPRateLimitPortControlMode,_AE:hpICMPRateLimitPortIpPacketType,_J:hpICMPRateLimitNotifyPortIndex,'hpicfBWMinEgressObjects':hpicfBWMinEgressObjects,'hpBWMinEgressPortConfig':hpBWMinEgressPortConfig,_A6:hpBWMinEgressPortNumQueues,'hpBWMinEgressPortPrctTable':hpBWMinEgressPortPrctTable,'hpBWMinEgressPortPrctEntry':hpBWMinEgressPortPrctEntry,_s:hpBWMinEgressPortPrctQueue,_A7:hpBWMinEgressPortPrct,'hpicfBWMinIngressObjects':hpicfBWMinIngressObjects,'hpBWMinIngressPortConfig':hpBWMinIngressPortConfig,_A4:hpBWMinIngressPortNumQueues,'hpBWMinIngressPortPrctTable':hpBWMinIngressPortPrctTable,'hpBWMinIngressPortPrctEntry':hpBWMinIngressPortPrctEntry,_t:hpBWMinIngressPortPrctQueue,_A5:hpBWMinIngressPortPrct,'hpicfRateLimitPortObjects':hpicfRateLimitPortObjects,'hpRateLimitPortConfig':hpRateLimitPortConfig,_P:hpEgressRateLimitPortNumQueues,'hpEgressRateLimitPortConfigTable':hpEgressRateLimitPortConfigTable,'hpEgressRateLimitPortConfigEntry':hpEgressRateLimitPortConfigEntry,_I:hpEgressRateLimitPortIndex,_Q:hpEgressRateLimitPortControlMode,_R:hpEgressRateLimitPortSingleControlPrct,_A8:hpEgressRateLimitPortSingleControlBps,_T:hpEgressRateLimitPortSingleControlKbps,_AI:hpEgressRateLimitPortQueueControlMode,'hpEgressRateLimitPortPrctTable':hpEgressRateLimitPortPrctTable,'hpEgressRateLimitPortPrctEntry':hpEgressRateLimitPortPrctEntry,_u:hpEgressRateLimitPortPrctQueue,_S:hpEgressRateLimitPortPrct,'hpEgressRateLimitPortBpsTable':hpEgressRateLimitPortBpsTable,'hpEgressRateLimitPortBpsEntry':hpEgressRateLimitPortBpsEntry,_v:hpEgressRateLimitPortBpsQueue,_A9:hpEgressRateLimitPortBps,'hpEgressRateLimitPortQueueConfigTable':hpEgressRateLimitPortQueueConfigTable,'hpEgressRateLimitPortQueueConfigEntry':hpEgressRateLimitPortQueueConfigEntry,_w:hpEgressRateLimitPortQueueIndex,_AJ:hpEgressRateLimitPortQueueMax,'hpicfIngressRateLimitPortObjects':hpicfIngressRateLimitPortObjects,'hpRateLimitIngressPortConfig':hpRateLimitIngressPortConfig,_Z:hpIngressRateLimitPortNumQueues,'hpIngressRateLimitPortConfigTable':hpIngressRateLimitPortConfigTable,'hpIngressRateLimitPortConfigEntry':hpIngressRateLimitPortConfigEntry,_M:hpIngressRateLimitPortIndex,_a:hpIngressRateLimitPortControlMode,_b:hpIngressRateLimitPortSingleControlPrct,_AA:hpIngressRateLimitPortSingleControlBps,_d:hpIngressRateLimitPortSingleControlKbps,'hpIngressRateLimitPortPrctTable':hpIngressRateLimitPortPrctTable,'hpIngressRateLimitPortPrctEntry':hpIngressRateLimitPortPrctEntry,_x:hpIngressRateLimitPortPrctQueue,_c:hpIngressRateLimitPortPrct,'hpIngressRateLimitPortBpsTable':hpIngressRateLimitPortBpsTable,'hpIngressRateLimitPortBpsEntry':hpIngressRateLimitPortBpsEntry,_y:hpIngressRateLimitPortBpsQueue,_AB:hpIngressRateLimitPortBps,'hpicfIngressBcastLimitPortObjects':hpicfIngressBcastLimitPortObjects,'hpBcastLimitIngressPortConfig':hpBcastLimitIngressPortConfig,'hpIngressBcastLimitPortConfigTable':hpIngressBcastLimitPortConfigTable,'hpIngressBcastLimitPortConfigEntry':hpIngressBcastLimitPortConfigEntry,_z:hpIngressBcastLimitPortIndex,_g:hpIngressBcastLimitPortControlMode,_h:hpIngressBcastLimitPortSingleControlPrct,_AC:hpIngressBcastLimitPortSingleControlKbps,'hpicfIngressMcastLimitPortObjects':hpicfIngressMcastLimitPortObjects,'hpMcastLimitIngressPortConfig':hpMcastLimitIngressPortConfig,'hpIngressMcastLimitPortConfigTable':hpIngressMcastLimitPortConfigTable,'hpIngressMcastLimitPortConfigEntry':hpIngressMcastLimitPortConfigEntry,_A0:hpIngressMcastLimitPortIndex,_i:hpIngressMcastLimitPortControlMode,_j:hpIngressMcastLimitPortSingleControlPrct,_AD:hpIngressMcastLimitPortSingleControlKbps,'hpicfUnknownUnicastLimitPortObjects':hpicfUnknownUnicastLimitPortObjects,'hpUnknownUnicastLimitPortConfig':hpUnknownUnicastLimitPortConfig,'hpUnknownUnicastLimitConfigTable':hpUnknownUnicastLimitConfigTable,'hpUnknownUnicastLimitConfigEntry':hpUnknownUnicastLimitConfigEntry,_A1:hpUnknownUnicastLimitPortIndex,_k:hpUnknownUnicastLimitPortControlMode,_l:hpUnknownUnicastLimitPortSingleControlPrct,_AH:hpUnknownUnicastLimitPortSingleControlKbps,'hpicfIngressRateLimitVlanObjects':hpicfIngressRateLimitVlanObjects,'hpicfIngressRateLimitVlanConfigTable':hpicfIngressRateLimitVlanConfigTable,'hpicfIngressRateLimitVlanConfigEntry':hpicfIngressRateLimitVlanConfigEntry,_A2:hpicfIngressRateLimitVlanIndex,_AF:hpicfIngressRateLimitVlanControlMode,_AG:hpicfIngressRateLimitVlanKbps,'hpicfRateLimitConformance':hpicfRateLimitConformance,'hpicfRateLimitGroups':hpicfRateLimitGroups,_AL:hpICMPRateLimitPortConfigGroup,_K:hpICMPRateLimitPortNotifyGroup,_U:hpBWMinIngressPortConfigGroup,_V:hpBWMinEgressPortConfigGroup,_AP:hpEgressRateLimitPortConfigGroup,_AQ:hpIngressRateLimitPortConfigGroup,_AM:hpICMPRateLimitPortConfigGroup2,_m:hpEgressRateLimitPortConfigGroup2,_W:hpIngressRateLimitPortConfigGroup2,_AN:hpBcastLimitIngressPortConfigGroup,_AO:hpMcastLimitIngressPortConfigGroup,_p:hpBcastLimitIngressPortConfigGroup2,_q:hpMcastLimitIngressPortConfigGroup2,_o:hpICMPRateLimitPortConfigGroup3,_n:hpUnknownUcastLimitIngressPortConfigGroup,_AR:hpicfIngressRateLimitVlanGroup,_AU:hpUnknownUcastLimitIngressPortConfigGroup2,_AS:hpEgressRateLimitPortConfigGroup3,_AT:hpEgressRateLimitPortQueueConfigEntryGroup,'hpicfRateLimitCompliances':hpicfRateLimitCompliances,'hpicfRateLimitCompliance':hpicfRateLimitCompliance,'hpicfRateLimitCompliance1':hpicfRateLimitCompliance1,'hpicfRateLimitCompliance2':hpicfRateLimitCompliance2,'hpicfRateLimitCompliance3':hpicfRateLimitCompliance3,'hpicfRateLimitCompliance4':hpicfRateLimitCompliance4,_AK:hpICMPRateLimitPortNotification})