_S='dhcp6FilterInterface'
_R='dhcp6FilterServerIp'
_Q='value30pps'
_P='value25pps'
_O='value20pps'
_N='value15pps'
_M='value10pps'
_L='value5pps'
_K='read-only'
_J='enable'
_I='ifIndex'
_H='IF-MIB'
_G='read-create'
_F='TPLINK-DHCP6FILTER-MIB'
_E='read-write'
_D='disable'
_C='OctetString'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_H,_I)
InetAddress,=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tplinkMgmt,=mibBuilder.importSymbols('TPLINK-MIB','tplinkMgmt')
TPRowStatus,=mibBuilder.importSymbols('TPLINK-TC-MIB','TPRowStatus')
tplinkDhcp6FilterMIB=ModuleIdentity((1,3,6,1,4,1,11863,6,67))
if mibBuilder.loadTexts:tplinkDhcp6FilterMIB.setRevisions(('2012-12-17 10:14',))
_TplinkDhcp6FilterMIBObjects_ObjectIdentity=ObjectIdentity
tplinkDhcp6FilterMIBObjects=_TplinkDhcp6FilterMIBObjects_ObjectIdentity((1,3,6,1,4,1,11863,6,67,1))
_Dhcp6FilterGlobalConfig_ObjectIdentity=ObjectIdentity
dhcp6FilterGlobalConfig=_Dhcp6FilterGlobalConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,67,1,1))
class _Dhcp6FilterEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_J,1)))
_Dhcp6FilterEnable_Type.__name__=_B
_Dhcp6FilterEnable_Object=MibScalar
dhcp6FilterEnable=_Dhcp6FilterEnable_Object((1,3,6,1,4,1,11863,6,67,1,1,1),_Dhcp6FilterEnable_Type())
dhcp6FilterEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:dhcp6FilterEnable.setStatus(_A)
_Dhcp6FilterPortConfig_ObjectIdentity=ObjectIdentity
dhcp6FilterPortConfig=_Dhcp6FilterPortConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,67,1,2))
_Dhcp6FilterPortConfigTable_Object=MibTable
dhcp6FilterPortConfigTable=_Dhcp6FilterPortConfigTable_Object((1,3,6,1,4,1,11863,6,67,1,2,1))
if mibBuilder.loadTexts:dhcp6FilterPortConfigTable.setStatus(_A)
_Dhcp6FilterPortConfigEntry_Object=MibTableRow
dhcp6FilterPortConfigEntry=_Dhcp6FilterPortConfigEntry_Object((1,3,6,1,4,1,11863,6,67,1,2,1,1))
dhcp6FilterPortConfigEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:dhcp6FilterPortConfigEntry.setStatus(_A)
class _Dhcp6FilterPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Dhcp6FilterPort_Type.__name__=_C
_Dhcp6FilterPort_Object=MibTableColumn
dhcp6FilterPort=_Dhcp6FilterPort_Object((1,3,6,1,4,1,11863,6,67,1,2,1,1,1),_Dhcp6FilterPort_Type())
dhcp6FilterPort.setMaxAccess(_K)
if mibBuilder.loadTexts:dhcp6FilterPort.setStatus(_A)
class _Dhcp6FilterPortConfigState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_J,1)))
_Dhcp6FilterPortConfigState_Type.__name__=_B
_Dhcp6FilterPortConfigState_Object=MibTableColumn
dhcp6FilterPortConfigState=_Dhcp6FilterPortConfigState_Object((1,3,6,1,4,1,11863,6,67,1,2,1,1,2),_Dhcp6FilterPortConfigState_Type())
dhcp6FilterPortConfigState.setMaxAccess(_E)
if mibBuilder.loadTexts:dhcp6FilterPortConfigState.setStatus(_A)
class _Dhcp6FilterPortConfigRateLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,5,10,15,20,25,30)));namedValues=NamedValues(*((_D,0),(_L,5),(_M,10),(_N,15),(_O,20),(_P,25),(_Q,30)))
_Dhcp6FilterPortConfigRateLimit_Type.__name__=_B
_Dhcp6FilterPortConfigRateLimit_Object=MibTableColumn
dhcp6FilterPortConfigRateLimit=_Dhcp6FilterPortConfigRateLimit_Object((1,3,6,1,4,1,11863,6,67,1,2,1,1,3),_Dhcp6FilterPortConfigRateLimit_Type())
dhcp6FilterPortConfigRateLimit.setMaxAccess(_E)
if mibBuilder.loadTexts:dhcp6FilterPortConfigRateLimit.setStatus(_A)
class _Dhcp6FilterPortConfigDeclineRateLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,5,10,15,20,25,30)));namedValues=NamedValues(*((_D,0),(_L,5),(_M,10),(_N,15),(_O,20),(_P,25),(_Q,30)))
_Dhcp6FilterPortConfigDeclineRateLimit_Type.__name__=_B
_Dhcp6FilterPortConfigDeclineRateLimit_Object=MibTableColumn
dhcp6FilterPortConfigDeclineRateLimit=_Dhcp6FilterPortConfigDeclineRateLimit_Object((1,3,6,1,4,1,11863,6,67,1,2,1,1,4),_Dhcp6FilterPortConfigDeclineRateLimit_Type())
dhcp6FilterPortConfigDeclineRateLimit.setMaxAccess(_E)
if mibBuilder.loadTexts:dhcp6FilterPortConfigDeclineRateLimit.setStatus(_A)
class _Dhcp6FilterPortConfigPortLag_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Dhcp6FilterPortConfigPortLag_Type.__name__=_C
_Dhcp6FilterPortConfigPortLag_Object=MibTableColumn
dhcp6FilterPortConfigPortLag=_Dhcp6FilterPortConfigPortLag_Object((1,3,6,1,4,1,11863,6,67,1,2,1,1,5),_Dhcp6FilterPortConfigPortLag_Type())
dhcp6FilterPortConfigPortLag.setMaxAccess(_K)
if mibBuilder.loadTexts:dhcp6FilterPortConfigPortLag.setStatus(_A)
_Dhcp6FilterServerPermitEntryCofig_ObjectIdentity=ObjectIdentity
dhcp6FilterServerPermitEntryCofig=_Dhcp6FilterServerPermitEntryCofig_ObjectIdentity((1,3,6,1,4,1,11863,6,67,1,3))
_Dhcp6FilterServerPermitEntryTable_Object=MibTable
dhcp6FilterServerPermitEntryTable=_Dhcp6FilterServerPermitEntryTable_Object((1,3,6,1,4,1,11863,6,67,1,3,1))
if mibBuilder.loadTexts:dhcp6FilterServerPermitEntryTable.setStatus(_A)
_Dhcp6FilterServerPermitEntry_Object=MibTableRow
dhcp6FilterServerPermitEntry=_Dhcp6FilterServerPermitEntry_Object((1,3,6,1,4,1,11863,6,67,1,3,1,1))
dhcp6FilterServerPermitEntry.setIndexNames((0,_F,_R),(0,_F,_S))
if mibBuilder.loadTexts:dhcp6FilterServerPermitEntry.setStatus(_A)
_Dhcp6FilterServerIp_Type=InetAddress
_Dhcp6FilterServerIp_Object=MibTableColumn
dhcp6FilterServerIp=_Dhcp6FilterServerIp_Object((1,3,6,1,4,1,11863,6,67,1,3,1,1,1),_Dhcp6FilterServerIp_Type())
dhcp6FilterServerIp.setMaxAccess(_G)
if mibBuilder.loadTexts:dhcp6FilterServerIp.setStatus(_A)
class _Dhcp6FilterInterface_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_Dhcp6FilterInterface_Type.__name__=_C
_Dhcp6FilterInterface_Object=MibTableColumn
dhcp6FilterInterface=_Dhcp6FilterInterface_Object((1,3,6,1,4,1,11863,6,67,1,3,1,1,2),_Dhcp6FilterInterface_Type())
dhcp6FilterInterface.setMaxAccess(_G)
if mibBuilder.loadTexts:dhcp6FilterInterface.setStatus(_A)
_Dhcp6FilterRowStatus_Type=TPRowStatus
_Dhcp6FilterRowStatus_Object=MibTableColumn
dhcp6FilterRowStatus=_Dhcp6FilterRowStatus_Object((1,3,6,1,4,1,11863,6,67,1,3,1,1,3),_Dhcp6FilterRowStatus_Type())
dhcp6FilterRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:dhcp6FilterRowStatus.setStatus(_A)
_TplinkDhcp6FilterNotifications_ObjectIdentity=ObjectIdentity
tplinkDhcp6FilterNotifications=_TplinkDhcp6FilterNotifications_ObjectIdentity((1,3,6,1,4,1,11863,6,67,2))
mibBuilder.exportSymbols(_F,**{'tplinkDhcp6FilterMIB':tplinkDhcp6FilterMIB,'tplinkDhcp6FilterMIBObjects':tplinkDhcp6FilterMIBObjects,'dhcp6FilterGlobalConfig':dhcp6FilterGlobalConfig,'dhcp6FilterEnable':dhcp6FilterEnable,'dhcp6FilterPortConfig':dhcp6FilterPortConfig,'dhcp6FilterPortConfigTable':dhcp6FilterPortConfigTable,'dhcp6FilterPortConfigEntry':dhcp6FilterPortConfigEntry,'dhcp6FilterPort':dhcp6FilterPort,'dhcp6FilterPortConfigState':dhcp6FilterPortConfigState,'dhcp6FilterPortConfigRateLimit':dhcp6FilterPortConfigRateLimit,'dhcp6FilterPortConfigDeclineRateLimit':dhcp6FilterPortConfigDeclineRateLimit,'dhcp6FilterPortConfigPortLag':dhcp6FilterPortConfigPortLag,'dhcp6FilterServerPermitEntryCofig':dhcp6FilterServerPermitEntryCofig,'dhcp6FilterServerPermitEntryTable':dhcp6FilterServerPermitEntryTable,'dhcp6FilterServerPermitEntry':dhcp6FilterServerPermitEntry,_R:dhcp6FilterServerIp,_S:dhcp6FilterInterface,'dhcp6FilterRowStatus':dhcp6FilterRowStatus,'tplinkDhcp6FilterNotifications':tplinkDhcp6FilterNotifications})