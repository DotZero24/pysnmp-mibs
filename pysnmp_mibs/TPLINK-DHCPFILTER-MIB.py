_T='interface'
_S='clientMac'
_R='serverIp'
_Q='value30pps'
_P='value25pps'
_O='value20pps'
_N='value15pps'
_M='value10pps'
_L='value5pps'
_K='read-only'
_J='ifIndex'
_I='IF-MIB'
_H='enable'
_G='read-create'
_F='TPLINK-DHCPFILTER-MIB'
_E='read-write'
_D='disable'
_C='OctetString'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_I,_J)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tplinkMgmt,=mibBuilder.importSymbols('TPLINK-MIB','tplinkMgmt')
TPRowStatus,=mibBuilder.importSymbols('TPLINK-TC-MIB','TPRowStatus')
tplinkDhcpFilterMIB=ModuleIdentity((1,3,6,1,4,1,11863,6,48))
if mibBuilder.loadTexts:tplinkDhcpFilterMIB.setRevisions(('2012-12-17 10:14',))
_TplinkDhcpFilterMIBObjects_ObjectIdentity=ObjectIdentity
tplinkDhcpFilterMIBObjects=_TplinkDhcpFilterMIBObjects_ObjectIdentity((1,3,6,1,4,1,11863,6,48,1))
_DhcpFilterGlobalConfig_ObjectIdentity=ObjectIdentity
dhcpFilterGlobalConfig=_DhcpFilterGlobalConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,48,1,1))
class _DhcpFilterEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_H,1)))
_DhcpFilterEnable_Type.__name__=_B
_DhcpFilterEnable_Object=MibScalar
dhcpFilterEnable=_DhcpFilterEnable_Object((1,3,6,1,4,1,11863,6,48,1,1,1),_DhcpFilterEnable_Type())
dhcpFilterEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:dhcpFilterEnable.setStatus(_A)
_DhcpFilterPortConfig_ObjectIdentity=ObjectIdentity
dhcpFilterPortConfig=_DhcpFilterPortConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,48,1,2))
_DhcpFilterPortConfigTable_Object=MibTable
dhcpFilterPortConfigTable=_DhcpFilterPortConfigTable_Object((1,3,6,1,4,1,11863,6,48,1,2,1))
if mibBuilder.loadTexts:dhcpFilterPortConfigTable.setStatus(_A)
_DhcpFilterPortConfigEntry_Object=MibTableRow
dhcpFilterPortConfigEntry=_DhcpFilterPortConfigEntry_Object((1,3,6,1,4,1,11863,6,48,1,2,1,1))
dhcpFilterPortConfigEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:dhcpFilterPortConfigEntry.setStatus(_A)
class _DhcpFilterPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DhcpFilterPort_Type.__name__=_C
_DhcpFilterPort_Object=MibTableColumn
dhcpFilterPort=_DhcpFilterPort_Object((1,3,6,1,4,1,11863,6,48,1,2,1,1,1),_DhcpFilterPort_Type())
dhcpFilterPort.setMaxAccess(_K)
if mibBuilder.loadTexts:dhcpFilterPort.setStatus(_A)
class _DhcpFilterPortConfigState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_H,1)))
_DhcpFilterPortConfigState_Type.__name__=_B
_DhcpFilterPortConfigState_Object=MibTableColumn
dhcpFilterPortConfigState=_DhcpFilterPortConfigState_Object((1,3,6,1,4,1,11863,6,48,1,2,1,1,2),_DhcpFilterPortConfigState_Type())
dhcpFilterPortConfigState.setMaxAccess(_E)
if mibBuilder.loadTexts:dhcpFilterPortConfigState.setStatus(_A)
class _DhcpFilterPortConfigMacVerify_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_H,1)))
_DhcpFilterPortConfigMacVerify_Type.__name__=_B
_DhcpFilterPortConfigMacVerify_Object=MibTableColumn
dhcpFilterPortConfigMacVerify=_DhcpFilterPortConfigMacVerify_Object((1,3,6,1,4,1,11863,6,48,1,2,1,1,3),_DhcpFilterPortConfigMacVerify_Type())
dhcpFilterPortConfigMacVerify.setMaxAccess(_E)
if mibBuilder.loadTexts:dhcpFilterPortConfigMacVerify.setStatus(_A)
class _DhcpFilterPortConfigRateLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,5,10,15,20,25,30)));namedValues=NamedValues(*((_D,0),(_L,5),(_M,10),(_N,15),(_O,20),(_P,25),(_Q,30)))
_DhcpFilterPortConfigRateLimit_Type.__name__=_B
_DhcpFilterPortConfigRateLimit_Object=MibTableColumn
dhcpFilterPortConfigRateLimit=_DhcpFilterPortConfigRateLimit_Object((1,3,6,1,4,1,11863,6,48,1,2,1,1,4),_DhcpFilterPortConfigRateLimit_Type())
dhcpFilterPortConfigRateLimit.setMaxAccess(_E)
if mibBuilder.loadTexts:dhcpFilterPortConfigRateLimit.setStatus(_A)
class _DhcpFilterPortConfigDeclineRateLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,5,10,15,20,25,30)));namedValues=NamedValues(*((_D,0),(_L,5),(_M,10),(_N,15),(_O,20),(_P,25),(_Q,30)))
_DhcpFilterPortConfigDeclineRateLimit_Type.__name__=_B
_DhcpFilterPortConfigDeclineRateLimit_Object=MibTableColumn
dhcpFilterPortConfigDeclineRateLimit=_DhcpFilterPortConfigDeclineRateLimit_Object((1,3,6,1,4,1,11863,6,48,1,2,1,1,5),_DhcpFilterPortConfigDeclineRateLimit_Type())
dhcpFilterPortConfigDeclineRateLimit.setMaxAccess(_E)
if mibBuilder.loadTexts:dhcpFilterPortConfigDeclineRateLimit.setStatus(_A)
class _DhcpFilterPortConfigPortLag_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_DhcpFilterPortConfigPortLag_Type.__name__=_C
_DhcpFilterPortConfigPortLag_Object=MibTableColumn
dhcpFilterPortConfigPortLag=_DhcpFilterPortConfigPortLag_Object((1,3,6,1,4,1,11863,6,48,1,2,1,1,6),_DhcpFilterPortConfigPortLag_Type())
dhcpFilterPortConfigPortLag.setMaxAccess(_K)
if mibBuilder.loadTexts:dhcpFilterPortConfigPortLag.setStatus(_A)
_DhcpFilterServerPermitEntryCofig_ObjectIdentity=ObjectIdentity
dhcpFilterServerPermitEntryCofig=_DhcpFilterServerPermitEntryCofig_ObjectIdentity((1,3,6,1,4,1,11863,6,48,1,3))
_DhcpFilterServerPermitEntryTable_Object=MibTable
dhcpFilterServerPermitEntryTable=_DhcpFilterServerPermitEntryTable_Object((1,3,6,1,4,1,11863,6,48,1,3,1))
if mibBuilder.loadTexts:dhcpFilterServerPermitEntryTable.setStatus(_A)
_DhcpFilterServerPermitEntry_Object=MibTableRow
dhcpFilterServerPermitEntry=_DhcpFilterServerPermitEntry_Object((1,3,6,1,4,1,11863,6,48,1,3,1,1))
dhcpFilterServerPermitEntry.setIndexNames((0,_F,_R),(0,_F,_S),(0,_F,_T))
if mibBuilder.loadTexts:dhcpFilterServerPermitEntry.setStatus(_A)
_ServerIp_Type=IpAddress
_ServerIp_Object=MibTableColumn
serverIp=_ServerIp_Object((1,3,6,1,4,1,11863,6,48,1,3,1,1,1),_ServerIp_Type())
serverIp.setMaxAccess(_G)
if mibBuilder.loadTexts:serverIp.setStatus(_A)
class _ClientMac_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,17))
_ClientMac_Type.__name__=_C
_ClientMac_Object=MibTableColumn
clientMac=_ClientMac_Object((1,3,6,1,4,1,11863,6,48,1,3,1,1,2),_ClientMac_Type())
clientMac.setMaxAccess(_G)
if mibBuilder.loadTexts:clientMac.setStatus(_A)
class _Interface_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_Interface_Type.__name__=_C
_Interface_Object=MibTableColumn
interface=_Interface_Object((1,3,6,1,4,1,11863,6,48,1,3,1,1,3),_Interface_Type())
interface.setMaxAccess(_G)
if mibBuilder.loadTexts:interface.setStatus(_A)
_RowStatus_Type=TPRowStatus
_RowStatus_Object=MibTableColumn
rowStatus=_RowStatus_Object((1,3,6,1,4,1,11863,6,48,1,3,1,1,4),_RowStatus_Type())
rowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:rowStatus.setStatus(_A)
_TplinkDhcpFilterNotifications_ObjectIdentity=ObjectIdentity
tplinkDhcpFilterNotifications=_TplinkDhcpFilterNotifications_ObjectIdentity((1,3,6,1,4,1,11863,6,48,2))
dhcpFilterRxIllegalServerPacket=NotificationType((1,3,6,1,4,1,11863,6,48,2,1))
if mibBuilder.loadTexts:dhcpFilterRxIllegalServerPacket.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'tplinkDhcpFilterMIB':tplinkDhcpFilterMIB,'tplinkDhcpFilterMIBObjects':tplinkDhcpFilterMIBObjects,'dhcpFilterGlobalConfig':dhcpFilterGlobalConfig,'dhcpFilterEnable':dhcpFilterEnable,'dhcpFilterPortConfig':dhcpFilterPortConfig,'dhcpFilterPortConfigTable':dhcpFilterPortConfigTable,'dhcpFilterPortConfigEntry':dhcpFilterPortConfigEntry,'dhcpFilterPort':dhcpFilterPort,'dhcpFilterPortConfigState':dhcpFilterPortConfigState,'dhcpFilterPortConfigMacVerify':dhcpFilterPortConfigMacVerify,'dhcpFilterPortConfigRateLimit':dhcpFilterPortConfigRateLimit,'dhcpFilterPortConfigDeclineRateLimit':dhcpFilterPortConfigDeclineRateLimit,'dhcpFilterPortConfigPortLag':dhcpFilterPortConfigPortLag,'dhcpFilterServerPermitEntryCofig':dhcpFilterServerPermitEntryCofig,'dhcpFilterServerPermitEntryTable':dhcpFilterServerPermitEntryTable,'dhcpFilterServerPermitEntry':dhcpFilterServerPermitEntry,_R:serverIp,_S:clientMac,_T:interface,'rowStatus':rowStatus,'tplinkDhcpFilterNotifications':tplinkDhcpFilterNotifications,'dhcpFilterRxIllegalServerPacket':dhcpFilterRxIllegalServerPacket})