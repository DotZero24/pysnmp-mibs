_X='hpnicfPortalForbiddenRuleIndex'
_W='invalid'
_V='hpnicfPortalFreeRuleIndex'
_U='hpnicfPortalMacTriggerOnIfIfIndex'
_T='hpnicfPortalMacTriggerSrvIndex'
_S='hpnicfPortalSSIDFreeRuleIndex'
_R='hpnicfPortalIfVlanNasIDVlanID'
_Q='hpnicfPortalIfVlanNasIDIfIndex'
_P='hpnicfPortalIfServerIndex'
_O='ifIndex'
_N='IF-MIB'
_M='hpnicfPortalServerPort'
_L='hpnicfPortalServerIP'
_K='hpnicfPortalFirstTrapTime'
_J='accessible-for-notify'
_I='hpnicfPortalServerName'
_H='read-write'
_G='OctetString'
_F='not-accessible'
_E='Integer32'
_D='HPN-ICF-PORTAL-MIB'
_C='read-create'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_N,'InterfaceIndex',_O)
InetAddress,InetAddressIPv4,InetAddressPrefixLength,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressIPv4','InetAddressPrefixLength','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
hpnicfPortal=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,99))
_HpnicfPortalConfig_ObjectIdentity=ObjectIdentity
hpnicfPortalConfig=_HpnicfPortalConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,99,1))
_HpnicfPortalMaxUserNumber_Type=Integer32
_HpnicfPortalMaxUserNumber_Object=MibScalar
hpnicfPortalMaxUserNumber=_HpnicfPortalMaxUserNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,1,1),_HpnicfPortalMaxUserNumber_Type())
hpnicfPortalMaxUserNumber.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfPortalMaxUserNumber.setStatus(_A)
_HpnicfPortalCurrentUserNumber_Type=Integer32
_HpnicfPortalCurrentUserNumber_Object=MibScalar
hpnicfPortalCurrentUserNumber=_HpnicfPortalCurrentUserNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,1,2),_HpnicfPortalCurrentUserNumber_Type())
hpnicfPortalCurrentUserNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPortalCurrentUserNumber.setStatus(_A)
class _HpnicfPortalStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_HpnicfPortalStatus_Type.__name__=_E
_HpnicfPortalStatus_Object=MibScalar
hpnicfPortalStatus=_HpnicfPortalStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,1,3),_HpnicfPortalStatus_Type())
hpnicfPortalStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPortalStatus.setStatus(_A)
_HpnicfPortalUserNumberUpperLimit_Type=Integer32
_HpnicfPortalUserNumberUpperLimit_Object=MibScalar
hpnicfPortalUserNumberUpperLimit=_HpnicfPortalUserNumberUpperLimit_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,1,4),_HpnicfPortalUserNumberUpperLimit_Type())
hpnicfPortalUserNumberUpperLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPortalUserNumberUpperLimit.setStatus(_A)
_HpnicfPortalNasId_Type=OctetString
_HpnicfPortalNasId_Object=MibScalar
hpnicfPortalNasId=_HpnicfPortalNasId_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,1,5),_HpnicfPortalNasId_Type())
hpnicfPortalNasId.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfPortalNasId.setStatus(_A)
_HpnicfPortalTables_ObjectIdentity=ObjectIdentity
hpnicfPortalTables=_HpnicfPortalTables_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,99,2))
_HpnicfPortalServerTable_Object=MibTable
hpnicfPortalServerTable=_HpnicfPortalServerTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,2,1))
if mibBuilder.loadTexts:hpnicfPortalServerTable.setStatus(_A)
_HpnicfPortalServerEntry_Object=MibTableRow
hpnicfPortalServerEntry=_HpnicfPortalServerEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,2,1,1))
hpnicfPortalServerEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:hpnicfPortalServerEntry.setStatus(_A)
class _HpnicfPortalServerName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HpnicfPortalServerName_Type.__name__=_G
_HpnicfPortalServerName_Object=MibTableColumn
hpnicfPortalServerName=_HpnicfPortalServerName_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,2,1,1,1),_HpnicfPortalServerName_Type())
hpnicfPortalServerName.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfPortalServerName.setStatus(_A)
class _HpnicfPortalServerUrl_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,127))
_HpnicfPortalServerUrl_Type.__name__=_G
_HpnicfPortalServerUrl_Object=MibTableColumn
hpnicfPortalServerUrl=_HpnicfPortalServerUrl_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,2,1,1,2),_HpnicfPortalServerUrl_Type())
hpnicfPortalServerUrl.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfPortalServerUrl.setStatus(_A)
class _HpnicfPortalServerPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65534))
_HpnicfPortalServerPort_Type.__name__=_E
_HpnicfPortalServerPort_Object=MibTableColumn
hpnicfPortalServerPort=_HpnicfPortalServerPort_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,2,1,1,3),_HpnicfPortalServerPort_Type())
hpnicfPortalServerPort.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfPortalServerPort.setStatus(_A)
_HpnicfPortalIfInfoTable_Object=MibTable
hpnicfPortalIfInfoTable=_HpnicfPortalIfInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,2,2))
if mibBuilder.loadTexts:hpnicfPortalIfInfoTable.setStatus(_A)
_HpnicfPortalIfInfoEntry_Object=MibTableRow
hpnicfPortalIfInfoEntry=_HpnicfPortalIfInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,2,2,1))
hpnicfPortalIfInfoEntry.setIndexNames((0,_N,_O))
if mibBuilder.loadTexts:hpnicfPortalIfInfoEntry.setStatus(_A)
_HpnicfPortalAuthReqNumber_Type=Integer32
_HpnicfPortalAuthReqNumber_Object=MibTableColumn
hpnicfPortalAuthReqNumber=_HpnicfPortalAuthReqNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,2,2,1,1),_HpnicfPortalAuthReqNumber_Type())
hpnicfPortalAuthReqNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPortalAuthReqNumber.setStatus(_A)
_HpnicfPortalAuthSuccNumber_Type=Integer32
_HpnicfPortalAuthSuccNumber_Object=MibTableColumn
hpnicfPortalAuthSuccNumber=_HpnicfPortalAuthSuccNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,2,2,1,2),_HpnicfPortalAuthSuccNumber_Type())
hpnicfPortalAuthSuccNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPortalAuthSuccNumber.setStatus(_A)
_HpnicfPortalAuthFailNumber_Type=Integer32
_HpnicfPortalAuthFailNumber_Object=MibTableColumn
hpnicfPortalAuthFailNumber=_HpnicfPortalAuthFailNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,2,2,1,3),_HpnicfPortalAuthFailNumber_Type())
hpnicfPortalAuthFailNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPortalAuthFailNumber.setStatus(_A)
_HpnicfPortalIfServerTable_Object=MibTable
hpnicfPortalIfServerTable=_HpnicfPortalIfServerTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,2,3))
if mibBuilder.loadTexts:hpnicfPortalIfServerTable.setStatus(_A)
_HpnicfPortalIfServerEntry_Object=MibTableRow
hpnicfPortalIfServerEntry=_HpnicfPortalIfServerEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,2,3,1))
hpnicfPortalIfServerEntry.setIndexNames((0,_D,_P))
if mibBuilder.loadTexts:hpnicfPortalIfServerEntry.setStatus(_A)
class _HpnicfPortalIfServerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpnicfPortalIfServerIndex_Type.__name__=_E
_HpnicfPortalIfServerIndex_Object=MibTableColumn
hpnicfPortalIfServerIndex=_HpnicfPortalIfServerIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,2,3,1,1),_HpnicfPortalIfServerIndex_Type())
hpnicfPortalIfServerIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfPortalIfServerIndex.setStatus(_A)
_HpnicfPortalIfServerUrl_Type=OctetString
_HpnicfPortalIfServerUrl_Object=MibTableColumn
hpnicfPortalIfServerUrl=_HpnicfPortalIfServerUrl_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,2,3,1,2),_HpnicfPortalIfServerUrl_Type())
hpnicfPortalIfServerUrl.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPortalIfServerUrl.setStatus(_A)
_HpnicfPortalIfServerRowStatus_Type=RowStatus
_HpnicfPortalIfServerRowStatus_Object=MibTableColumn
hpnicfPortalIfServerRowStatus=_HpnicfPortalIfServerRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,2,3,1,3),_HpnicfPortalIfServerRowStatus_Type())
hpnicfPortalIfServerRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPortalIfServerRowStatus.setStatus(_A)
_HpnicfPortalIfVlanNasIDTable_Object=MibTable
hpnicfPortalIfVlanNasIDTable=_HpnicfPortalIfVlanNasIDTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,2,4))
if mibBuilder.loadTexts:hpnicfPortalIfVlanNasIDTable.setStatus(_A)
_HpnicfPortalIfVlanNasIDEntry_Object=MibTableRow
hpnicfPortalIfVlanNasIDEntry=_HpnicfPortalIfVlanNasIDEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,2,4,1))
hpnicfPortalIfVlanNasIDEntry.setIndexNames((0,_D,_Q),(0,_D,_R))
if mibBuilder.loadTexts:hpnicfPortalIfVlanNasIDEntry.setStatus(_A)
_HpnicfPortalIfVlanNasIDIfIndex_Type=InterfaceIndex
_HpnicfPortalIfVlanNasIDIfIndex_Object=MibTableColumn
hpnicfPortalIfVlanNasIDIfIndex=_HpnicfPortalIfVlanNasIDIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,2,4,1,1),_HpnicfPortalIfVlanNasIDIfIndex_Type())
hpnicfPortalIfVlanNasIDIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfPortalIfVlanNasIDIfIndex.setStatus(_A)
class _HpnicfPortalIfVlanNasIDVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfPortalIfVlanNasIDVlanID_Type.__name__=_E
_HpnicfPortalIfVlanNasIDVlanID_Object=MibTableColumn
hpnicfPortalIfVlanNasIDVlanID=_HpnicfPortalIfVlanNasIDVlanID_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,2,4,1,2),_HpnicfPortalIfVlanNasIDVlanID_Type())
hpnicfPortalIfVlanNasIDVlanID.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfPortalIfVlanNasIDVlanID.setStatus(_A)
class _HpnicfPortalIfVlanNasIDNasID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_HpnicfPortalIfVlanNasIDNasID_Type.__name__=_G
_HpnicfPortalIfVlanNasIDNasID_Object=MibTableColumn
hpnicfPortalIfVlanNasIDNasID=_HpnicfPortalIfVlanNasIDNasID_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,2,4,1,3),_HpnicfPortalIfVlanNasIDNasID_Type())
hpnicfPortalIfVlanNasIDNasID.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPortalIfVlanNasIDNasID.setStatus(_A)
_HpnicfPortalSSIDFreeRuleTable_Object=MibTable
hpnicfPortalSSIDFreeRuleTable=_HpnicfPortalSSIDFreeRuleTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,2,5))
if mibBuilder.loadTexts:hpnicfPortalSSIDFreeRuleTable.setStatus(_A)
_HpnicfPortalSSIDFreeRuleEntry_Object=MibTableRow
hpnicfPortalSSIDFreeRuleEntry=_HpnicfPortalSSIDFreeRuleEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,2,5,1))
hpnicfPortalSSIDFreeRuleEntry.setIndexNames((0,_D,_S))
if mibBuilder.loadTexts:hpnicfPortalSSIDFreeRuleEntry.setStatus(_A)
class _HpnicfPortalSSIDFreeRuleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpnicfPortalSSIDFreeRuleIndex_Type.__name__=_E
_HpnicfPortalSSIDFreeRuleIndex_Object=MibTableColumn
hpnicfPortalSSIDFreeRuleIndex=_HpnicfPortalSSIDFreeRuleIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,2,5,1,1),_HpnicfPortalSSIDFreeRuleIndex_Type())
hpnicfPortalSSIDFreeRuleIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfPortalSSIDFreeRuleIndex.setStatus(_A)
class _HpnicfPortalSSIDFreeRuleSrcSSID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_HpnicfPortalSSIDFreeRuleSrcSSID_Type.__name__=_G
_HpnicfPortalSSIDFreeRuleSrcSSID_Object=MibTableColumn
hpnicfPortalSSIDFreeRuleSrcSSID=_HpnicfPortalSSIDFreeRuleSrcSSID_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,2,5,1,2),_HpnicfPortalSSIDFreeRuleSrcSSID_Type())
hpnicfPortalSSIDFreeRuleSrcSSID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPortalSSIDFreeRuleSrcSSID.setStatus(_A)
_HpnicfPortalSSIDFreeRuleRowStatus_Type=RowStatus
_HpnicfPortalSSIDFreeRuleRowStatus_Object=MibTableColumn
hpnicfPortalSSIDFreeRuleRowStatus=_HpnicfPortalSSIDFreeRuleRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,2,5,1,3),_HpnicfPortalSSIDFreeRuleRowStatus_Type())
hpnicfPortalSSIDFreeRuleRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPortalSSIDFreeRuleRowStatus.setStatus(_A)
class _HpnicfPortalSSIDFreeRuleSrcSpot_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_HpnicfPortalSSIDFreeRuleSrcSpot_Type.__name__=_G
_HpnicfPortalSSIDFreeRuleSrcSpot_Object=MibTableColumn
hpnicfPortalSSIDFreeRuleSrcSpot=_HpnicfPortalSSIDFreeRuleSrcSpot_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,2,5,1,4),_HpnicfPortalSSIDFreeRuleSrcSpot_Type())
hpnicfPortalSSIDFreeRuleSrcSpot.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPortalSSIDFreeRuleSrcSpot.setStatus(_A)
_HpnicfPortalMacTriggerSrvTable_Object=MibTable
hpnicfPortalMacTriggerSrvTable=_HpnicfPortalMacTriggerSrvTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,2,6))
if mibBuilder.loadTexts:hpnicfPortalMacTriggerSrvTable.setStatus(_A)
_HpnicfPortalMacTriggerSrvEntry_Object=MibTableRow
hpnicfPortalMacTriggerSrvEntry=_HpnicfPortalMacTriggerSrvEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,2,6,1))
hpnicfPortalMacTriggerSrvEntry.setIndexNames((0,_D,_T))
if mibBuilder.loadTexts:hpnicfPortalMacTriggerSrvEntry.setStatus(_A)
class _HpnicfPortalMacTriggerSrvIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpnicfPortalMacTriggerSrvIndex_Type.__name__=_E
_HpnicfPortalMacTriggerSrvIndex_Object=MibTableColumn
hpnicfPortalMacTriggerSrvIndex=_HpnicfPortalMacTriggerSrvIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,2,6,1,1),_HpnicfPortalMacTriggerSrvIndex_Type())
hpnicfPortalMacTriggerSrvIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfPortalMacTriggerSrvIndex.setStatus(_A)
_HpnicfPortalMacTriggerSrvIPAddrType_Type=InetAddressType
_HpnicfPortalMacTriggerSrvIPAddrType_Object=MibTableColumn
hpnicfPortalMacTriggerSrvIPAddrType=_HpnicfPortalMacTriggerSrvIPAddrType_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,2,6,1,2),_HpnicfPortalMacTriggerSrvIPAddrType_Type())
hpnicfPortalMacTriggerSrvIPAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPortalMacTriggerSrvIPAddrType.setStatus(_A)
_HpnicfPortalMacTriggerSrvIP_Type=InetAddress
_HpnicfPortalMacTriggerSrvIP_Object=MibTableColumn
hpnicfPortalMacTriggerSrvIP=_HpnicfPortalMacTriggerSrvIP_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,2,6,1,3),_HpnicfPortalMacTriggerSrvIP_Type())
hpnicfPortalMacTriggerSrvIP.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPortalMacTriggerSrvIP.setStatus(_A)
class _HpnicfPortalMacTriggerSrvPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65534))
_HpnicfPortalMacTriggerSrvPort_Type.__name__=_E
_HpnicfPortalMacTriggerSrvPort_Object=MibTableColumn
hpnicfPortalMacTriggerSrvPort=_HpnicfPortalMacTriggerSrvPort_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,2,6,1,4),_HpnicfPortalMacTriggerSrvPort_Type())
hpnicfPortalMacTriggerSrvPort.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPortalMacTriggerSrvPort.setStatus(_A)
_HpnicfPortalMacTriggerSrvRowStatus_Type=RowStatus
_HpnicfPortalMacTriggerSrvRowStatus_Object=MibTableColumn
hpnicfPortalMacTriggerSrvRowStatus=_HpnicfPortalMacTriggerSrvRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,2,6,1,5),_HpnicfPortalMacTriggerSrvRowStatus_Type())
hpnicfPortalMacTriggerSrvRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPortalMacTriggerSrvRowStatus.setStatus(_A)
_HpnicfPortalMacTriggerOnIfTable_Object=MibTable
hpnicfPortalMacTriggerOnIfTable=_HpnicfPortalMacTriggerOnIfTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,2,7))
if mibBuilder.loadTexts:hpnicfPortalMacTriggerOnIfTable.setStatus(_A)
_HpnicfPortalMacTriggerOnIfEntry_Object=MibTableRow
hpnicfPortalMacTriggerOnIfEntry=_HpnicfPortalMacTriggerOnIfEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,2,7,1))
hpnicfPortalMacTriggerOnIfEntry.setIndexNames((0,_D,_U))
if mibBuilder.loadTexts:hpnicfPortalMacTriggerOnIfEntry.setStatus(_A)
_HpnicfPortalMacTriggerOnIfIfIndex_Type=InterfaceIndex
_HpnicfPortalMacTriggerOnIfIfIndex_Object=MibTableColumn
hpnicfPortalMacTriggerOnIfIfIndex=_HpnicfPortalMacTriggerOnIfIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,2,7,1,1),_HpnicfPortalMacTriggerOnIfIfIndex_Type())
hpnicfPortalMacTriggerOnIfIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfPortalMacTriggerOnIfIfIndex.setStatus(_A)
_HpnicfPortalMacTriggerOnIfDetctFlowPeriod_Type=Integer32
_HpnicfPortalMacTriggerOnIfDetctFlowPeriod_Object=MibTableColumn
hpnicfPortalMacTriggerOnIfDetctFlowPeriod=_HpnicfPortalMacTriggerOnIfDetctFlowPeriod_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,2,7,1,2),_HpnicfPortalMacTriggerOnIfDetctFlowPeriod_Type())
hpnicfPortalMacTriggerOnIfDetctFlowPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPortalMacTriggerOnIfDetctFlowPeriod.setStatus(_A)
_HpnicfPortalMacTriggerOnIfThresholdFlow_Type=Unsigned32
_HpnicfPortalMacTriggerOnIfThresholdFlow_Object=MibTableColumn
hpnicfPortalMacTriggerOnIfThresholdFlow=_HpnicfPortalMacTriggerOnIfThresholdFlow_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,2,7,1,3),_HpnicfPortalMacTriggerOnIfThresholdFlow_Type())
hpnicfPortalMacTriggerOnIfThresholdFlow.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPortalMacTriggerOnIfThresholdFlow.setStatus(_A)
_HpnicfPortalMacTriggerOnIfRowStatus_Type=RowStatus
_HpnicfPortalMacTriggerOnIfRowStatus_Object=MibTableColumn
hpnicfPortalMacTriggerOnIfRowStatus=_HpnicfPortalMacTriggerOnIfRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,2,7,1,4),_HpnicfPortalMacTriggerOnIfRowStatus_Type())
hpnicfPortalMacTriggerOnIfRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPortalMacTriggerOnIfRowStatus.setStatus(_A)
_HpnicfPortalFreeRuleTable_Object=MibTable
hpnicfPortalFreeRuleTable=_HpnicfPortalFreeRuleTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,2,8))
if mibBuilder.loadTexts:hpnicfPortalFreeRuleTable.setStatus(_A)
_HpnicfPortalFreeRuleEntry_Object=MibTableRow
hpnicfPortalFreeRuleEntry=_HpnicfPortalFreeRuleEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,2,8,1))
hpnicfPortalFreeRuleEntry.setIndexNames((0,_D,_V))
if mibBuilder.loadTexts:hpnicfPortalFreeRuleEntry.setStatus(_A)
class _HpnicfPortalFreeRuleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpnicfPortalFreeRuleIndex_Type.__name__=_E
_HpnicfPortalFreeRuleIndex_Object=MibTableColumn
hpnicfPortalFreeRuleIndex=_HpnicfPortalFreeRuleIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,2,8,1,1),_HpnicfPortalFreeRuleIndex_Type())
hpnicfPortalFreeRuleIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfPortalFreeRuleIndex.setStatus(_A)
_HpnicfPortalFreeRuleSrcIfIndex_Type=InterfaceIndex
_HpnicfPortalFreeRuleSrcIfIndex_Object=MibTableColumn
hpnicfPortalFreeRuleSrcIfIndex=_HpnicfPortalFreeRuleSrcIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,2,8,1,2),_HpnicfPortalFreeRuleSrcIfIndex_Type())
hpnicfPortalFreeRuleSrcIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPortalFreeRuleSrcIfIndex.setStatus(_A)
_HpnicfPortalFreeRuleSrcVlanID_Type=Integer32
_HpnicfPortalFreeRuleSrcVlanID_Object=MibTableColumn
hpnicfPortalFreeRuleSrcVlanID=_HpnicfPortalFreeRuleSrcVlanID_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,2,8,1,3),_HpnicfPortalFreeRuleSrcVlanID_Type())
hpnicfPortalFreeRuleSrcVlanID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPortalFreeRuleSrcVlanID.setStatus(_A)
_HpnicfPortalFreeRuleSrcMac_Type=MacAddress
_HpnicfPortalFreeRuleSrcMac_Object=MibTableColumn
hpnicfPortalFreeRuleSrcMac=_HpnicfPortalFreeRuleSrcMac_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,2,8,1,4),_HpnicfPortalFreeRuleSrcMac_Type())
hpnicfPortalFreeRuleSrcMac.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPortalFreeRuleSrcMac.setStatus(_A)
_HpnicfPortalFreeRuleAddrType_Type=InetAddressType
_HpnicfPortalFreeRuleAddrType_Object=MibTableColumn
hpnicfPortalFreeRuleAddrType=_HpnicfPortalFreeRuleAddrType_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,2,8,1,5),_HpnicfPortalFreeRuleAddrType_Type())
hpnicfPortalFreeRuleAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPortalFreeRuleAddrType.setStatus(_A)
_HpnicfPortalFreeRuleSrcAddr_Type=InetAddress
_HpnicfPortalFreeRuleSrcAddr_Object=MibTableColumn
hpnicfPortalFreeRuleSrcAddr=_HpnicfPortalFreeRuleSrcAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,2,8,1,6),_HpnicfPortalFreeRuleSrcAddr_Type())
hpnicfPortalFreeRuleSrcAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPortalFreeRuleSrcAddr.setStatus(_A)
_HpnicfPortalFreeRuleSrcPrefix_Type=InetAddressPrefixLength
_HpnicfPortalFreeRuleSrcPrefix_Object=MibTableColumn
hpnicfPortalFreeRuleSrcPrefix=_HpnicfPortalFreeRuleSrcPrefix_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,2,8,1,7),_HpnicfPortalFreeRuleSrcPrefix_Type())
hpnicfPortalFreeRuleSrcPrefix.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPortalFreeRuleSrcPrefix.setStatus(_A)
_HpnicfPortalFreeRuleDstAddr_Type=InetAddress
_HpnicfPortalFreeRuleDstAddr_Object=MibTableColumn
hpnicfPortalFreeRuleDstAddr=_HpnicfPortalFreeRuleDstAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,2,8,1,8),_HpnicfPortalFreeRuleDstAddr_Type())
hpnicfPortalFreeRuleDstAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPortalFreeRuleDstAddr.setStatus(_A)
_HpnicfPortalFreeRuleDstPrefix_Type=InetAddressPrefixLength
_HpnicfPortalFreeRuleDstPrefix_Object=MibTableColumn
hpnicfPortalFreeRuleDstPrefix=_HpnicfPortalFreeRuleDstPrefix_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,2,8,1,9),_HpnicfPortalFreeRuleDstPrefix_Type())
hpnicfPortalFreeRuleDstPrefix.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPortalFreeRuleDstPrefix.setStatus(_A)
class _HpnicfPortalFreeRuleProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,6,17)));namedValues=NamedValues(*((_W,0),('tcp',6),('udp',17)))
_HpnicfPortalFreeRuleProtocol_Type.__name__=_E
_HpnicfPortalFreeRuleProtocol_Object=MibTableColumn
hpnicfPortalFreeRuleProtocol=_HpnicfPortalFreeRuleProtocol_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,2,8,1,10),_HpnicfPortalFreeRuleProtocol_Type())
hpnicfPortalFreeRuleProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPortalFreeRuleProtocol.setStatus(_A)
_HpnicfPortalFreeRuleSrcPort_Type=Integer32
_HpnicfPortalFreeRuleSrcPort_Object=MibTableColumn
hpnicfPortalFreeRuleSrcPort=_HpnicfPortalFreeRuleSrcPort_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,2,8,1,11),_HpnicfPortalFreeRuleSrcPort_Type())
hpnicfPortalFreeRuleSrcPort.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPortalFreeRuleSrcPort.setStatus(_A)
_HpnicfPortalFreeRuleDstPort_Type=Integer32
_HpnicfPortalFreeRuleDstPort_Object=MibTableColumn
hpnicfPortalFreeRuleDstPort=_HpnicfPortalFreeRuleDstPort_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,2,8,1,12),_HpnicfPortalFreeRuleDstPort_Type())
hpnicfPortalFreeRuleDstPort.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPortalFreeRuleDstPort.setStatus(_A)
_HpnicfPortalFreeRuleRowStatus_Type=RowStatus
_HpnicfPortalFreeRuleRowStatus_Object=MibTableColumn
hpnicfPortalFreeRuleRowStatus=_HpnicfPortalFreeRuleRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,2,8,1,13),_HpnicfPortalFreeRuleRowStatus_Type())
hpnicfPortalFreeRuleRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPortalFreeRuleRowStatus.setStatus(_A)
_HpnicfPortalForbiddenRuleTable_Object=MibTable
hpnicfPortalForbiddenRuleTable=_HpnicfPortalForbiddenRuleTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,2,9))
if mibBuilder.loadTexts:hpnicfPortalForbiddenRuleTable.setStatus(_A)
_HpnicfPortalForbiddenRuleEntry_Object=MibTableRow
hpnicfPortalForbiddenRuleEntry=_HpnicfPortalForbiddenRuleEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,2,9,1))
hpnicfPortalForbiddenRuleEntry.setIndexNames((0,_D,_X))
if mibBuilder.loadTexts:hpnicfPortalForbiddenRuleEntry.setStatus(_A)
class _HpnicfPortalForbiddenRuleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpnicfPortalForbiddenRuleIndex_Type.__name__=_E
_HpnicfPortalForbiddenRuleIndex_Object=MibTableColumn
hpnicfPortalForbiddenRuleIndex=_HpnicfPortalForbiddenRuleIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,2,9,1,1),_HpnicfPortalForbiddenRuleIndex_Type())
hpnicfPortalForbiddenRuleIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfPortalForbiddenRuleIndex.setStatus(_A)
_HpnicfPortalForbiddenRuleSrcIfIndex_Type=InterfaceIndex
_HpnicfPortalForbiddenRuleSrcIfIndex_Object=MibTableColumn
hpnicfPortalForbiddenRuleSrcIfIndex=_HpnicfPortalForbiddenRuleSrcIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,2,9,1,2),_HpnicfPortalForbiddenRuleSrcIfIndex_Type())
hpnicfPortalForbiddenRuleSrcIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPortalForbiddenRuleSrcIfIndex.setStatus(_A)
_HpnicfPortalForbiddenRuleSrcVlanID_Type=Integer32
_HpnicfPortalForbiddenRuleSrcVlanID_Object=MibTableColumn
hpnicfPortalForbiddenRuleSrcVlanID=_HpnicfPortalForbiddenRuleSrcVlanID_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,2,9,1,3),_HpnicfPortalForbiddenRuleSrcVlanID_Type())
hpnicfPortalForbiddenRuleSrcVlanID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPortalForbiddenRuleSrcVlanID.setStatus(_A)
_HpnicfPortalForbiddenRuleSrcMac_Type=MacAddress
_HpnicfPortalForbiddenRuleSrcMac_Object=MibTableColumn
hpnicfPortalForbiddenRuleSrcMac=_HpnicfPortalForbiddenRuleSrcMac_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,2,9,1,4),_HpnicfPortalForbiddenRuleSrcMac_Type())
hpnicfPortalForbiddenRuleSrcMac.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPortalForbiddenRuleSrcMac.setStatus(_A)
_HpnicfPortalForbiddenRuleAddrType_Type=InetAddressType
_HpnicfPortalForbiddenRuleAddrType_Object=MibTableColumn
hpnicfPortalForbiddenRuleAddrType=_HpnicfPortalForbiddenRuleAddrType_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,2,9,1,5),_HpnicfPortalForbiddenRuleAddrType_Type())
hpnicfPortalForbiddenRuleAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPortalForbiddenRuleAddrType.setStatus(_A)
_HpnicfPortalForbiddenRuleSrcAddr_Type=InetAddress
_HpnicfPortalForbiddenRuleSrcAddr_Object=MibTableColumn
hpnicfPortalForbiddenRuleSrcAddr=_HpnicfPortalForbiddenRuleSrcAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,2,9,1,6),_HpnicfPortalForbiddenRuleSrcAddr_Type())
hpnicfPortalForbiddenRuleSrcAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPortalForbiddenRuleSrcAddr.setStatus(_A)
_HpnicfPortalForbiddenRuleSrcPrefix_Type=InetAddressPrefixLength
_HpnicfPortalForbiddenRuleSrcPrefix_Object=MibTableColumn
hpnicfPortalForbiddenRuleSrcPrefix=_HpnicfPortalForbiddenRuleSrcPrefix_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,2,9,1,7),_HpnicfPortalForbiddenRuleSrcPrefix_Type())
hpnicfPortalForbiddenRuleSrcPrefix.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPortalForbiddenRuleSrcPrefix.setStatus(_A)
_HpnicfPortalForbiddenRuleDstAddr_Type=InetAddress
_HpnicfPortalForbiddenRuleDstAddr_Object=MibTableColumn
hpnicfPortalForbiddenRuleDstAddr=_HpnicfPortalForbiddenRuleDstAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,2,9,1,8),_HpnicfPortalForbiddenRuleDstAddr_Type())
hpnicfPortalForbiddenRuleDstAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPortalForbiddenRuleDstAddr.setStatus(_A)
_HpnicfPortalForbiddenRuleDstPrefix_Type=InetAddressPrefixLength
_HpnicfPortalForbiddenRuleDstPrefix_Object=MibTableColumn
hpnicfPortalForbiddenRuleDstPrefix=_HpnicfPortalForbiddenRuleDstPrefix_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,2,9,1,9),_HpnicfPortalForbiddenRuleDstPrefix_Type())
hpnicfPortalForbiddenRuleDstPrefix.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPortalForbiddenRuleDstPrefix.setStatus(_A)
class _HpnicfPortalForbiddenRuleProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,6,17)));namedValues=NamedValues(*((_W,0),('tcp',6),('udp',17)))
_HpnicfPortalForbiddenRuleProtocol_Type.__name__=_E
_HpnicfPortalForbiddenRuleProtocol_Object=MibTableColumn
hpnicfPortalForbiddenRuleProtocol=_HpnicfPortalForbiddenRuleProtocol_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,2,9,1,10),_HpnicfPortalForbiddenRuleProtocol_Type())
hpnicfPortalForbiddenRuleProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPortalForbiddenRuleProtocol.setStatus(_A)
_HpnicfPortalForbiddenRuleSrcPort_Type=Integer32
_HpnicfPortalForbiddenRuleSrcPort_Object=MibTableColumn
hpnicfPortalForbiddenRuleSrcPort=_HpnicfPortalForbiddenRuleSrcPort_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,2,9,1,11),_HpnicfPortalForbiddenRuleSrcPort_Type())
hpnicfPortalForbiddenRuleSrcPort.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPortalForbiddenRuleSrcPort.setStatus(_A)
_HpnicfPortalForbiddenRuleDstPort_Type=Integer32
_HpnicfPortalForbiddenRuleDstPort_Object=MibTableColumn
hpnicfPortalForbiddenRuleDstPort=_HpnicfPortalForbiddenRuleDstPort_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,2,9,1,12),_HpnicfPortalForbiddenRuleDstPort_Type())
hpnicfPortalForbiddenRuleDstPort.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPortalForbiddenRuleDstPort.setStatus(_A)
_HpnicfPortalForbiddenRuleRowStatus_Type=RowStatus
_HpnicfPortalForbiddenRuleRowStatus_Object=MibTableColumn
hpnicfPortalForbiddenRuleRowStatus=_HpnicfPortalForbiddenRuleRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,2,9,1,13),_HpnicfPortalForbiddenRuleRowStatus_Type())
hpnicfPortalForbiddenRuleRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPortalForbiddenRuleRowStatus.setStatus(_A)
_HpnicfPortalTraps_ObjectIdentity=ObjectIdentity
hpnicfPortalTraps=_HpnicfPortalTraps_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,99,3))
_HpnicfPortalTrapPrefix_ObjectIdentity=ObjectIdentity
hpnicfPortalTrapPrefix=_HpnicfPortalTrapPrefix_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,99,3,0))
_HpnicfPortalTrapVarObjects_ObjectIdentity=ObjectIdentity
hpnicfPortalTrapVarObjects=_HpnicfPortalTrapVarObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,99,3,1))
_HpnicfPortalFirstTrapTime_Type=TimeTicks
_HpnicfPortalFirstTrapTime_Object=MibScalar
hpnicfPortalFirstTrapTime=_HpnicfPortalFirstTrapTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,3,1,1),_HpnicfPortalFirstTrapTime_Type())
hpnicfPortalFirstTrapTime.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfPortalFirstTrapTime.setStatus(_A)
_HpnicfPortalServerIP_Type=InetAddressIPv4
_HpnicfPortalServerIP_Object=MibScalar
hpnicfPortalServerIP=_HpnicfPortalServerIP_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,3,1,2),_HpnicfPortalServerIP_Type())
hpnicfPortalServerIP.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfPortalServerIP.setStatus(_A)
_HpnicfPortalStatistic_ObjectIdentity=ObjectIdentity
hpnicfPortalStatistic=_HpnicfPortalStatistic_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,99,4))
_HpnicfPortalStatAuthReq_Type=Counter64
_HpnicfPortalStatAuthReq_Object=MibScalar
hpnicfPortalStatAuthReq=_HpnicfPortalStatAuthReq_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,4,1),_HpnicfPortalStatAuthReq_Type())
hpnicfPortalStatAuthReq.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPortalStatAuthReq.setStatus(_A)
_HpnicfPortalStatAckLogout_Type=Counter64
_HpnicfPortalStatAckLogout_Object=MibScalar
hpnicfPortalStatAckLogout=_HpnicfPortalStatAckLogout_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,4,2),_HpnicfPortalStatAckLogout_Type())
hpnicfPortalStatAckLogout.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPortalStatAckLogout.setStatus(_A)
_HpnicfPortalStatNotifyLogout_Type=Counter64
_HpnicfPortalStatNotifyLogout_Object=MibScalar
hpnicfPortalStatNotifyLogout=_HpnicfPortalStatNotifyLogout_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,4,3),_HpnicfPortalStatNotifyLogout_Type())
hpnicfPortalStatNotifyLogout.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPortalStatNotifyLogout.setStatus(_A)
_HpnicfPortalStatChallengeTimeout_Type=Counter64
_HpnicfPortalStatChallengeTimeout_Object=MibScalar
hpnicfPortalStatChallengeTimeout=_HpnicfPortalStatChallengeTimeout_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,4,4),_HpnicfPortalStatChallengeTimeout_Type())
hpnicfPortalStatChallengeTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPortalStatChallengeTimeout.setStatus(_A)
_HpnicfPortalStatChallengeBusy_Type=Counter64
_HpnicfPortalStatChallengeBusy_Object=MibScalar
hpnicfPortalStatChallengeBusy=_HpnicfPortalStatChallengeBusy_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,4,5),_HpnicfPortalStatChallengeBusy_Type())
hpnicfPortalStatChallengeBusy.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPortalStatChallengeBusy.setStatus(_A)
_HpnicfPortalStatChallengeFail_Type=Counter64
_HpnicfPortalStatChallengeFail_Object=MibScalar
hpnicfPortalStatChallengeFail=_HpnicfPortalStatChallengeFail_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,4,6),_HpnicfPortalStatChallengeFail_Type())
hpnicfPortalStatChallengeFail.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPortalStatChallengeFail.setStatus(_A)
_HpnicfPortalStatAuthTimeout_Type=Counter64
_HpnicfPortalStatAuthTimeout_Object=MibScalar
hpnicfPortalStatAuthTimeout=_HpnicfPortalStatAuthTimeout_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,4,7),_HpnicfPortalStatAuthTimeout_Type())
hpnicfPortalStatAuthTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPortalStatAuthTimeout.setStatus(_A)
_HpnicfPortalStatAuthFail_Type=Counter64
_HpnicfPortalStatAuthFail_Object=MibScalar
hpnicfPortalStatAuthFail=_HpnicfPortalStatAuthFail_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,4,8),_HpnicfPortalStatAuthFail_Type())
hpnicfPortalStatAuthFail.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPortalStatAuthFail.setStatus(_A)
_HpnicfPortalStatPwdError_Type=Counter64
_HpnicfPortalStatPwdError_Object=MibScalar
hpnicfPortalStatPwdError=_HpnicfPortalStatPwdError_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,4,9),_HpnicfPortalStatPwdError_Type())
hpnicfPortalStatPwdError.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPortalStatPwdError.setStatus(_A)
_HpnicfPortalStatAuthBusy_Type=Counter64
_HpnicfPortalStatAuthBusy_Object=MibScalar
hpnicfPortalStatAuthBusy=_HpnicfPortalStatAuthBusy_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,4,10),_HpnicfPortalStatAuthBusy_Type())
hpnicfPortalStatAuthBusy.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPortalStatAuthBusy.setStatus(_A)
_HpnicfPortalStatAuthDisordered_Type=Counter64
_HpnicfPortalStatAuthDisordered_Object=MibScalar
hpnicfPortalStatAuthDisordered=_HpnicfPortalStatAuthDisordered_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,4,11),_HpnicfPortalStatAuthDisordered_Type())
hpnicfPortalStatAuthDisordered.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPortalStatAuthDisordered.setStatus(_A)
_HpnicfPortalStatAuthUnknownError_Type=Counter64
_HpnicfPortalStatAuthUnknownError_Object=MibScalar
hpnicfPortalStatAuthUnknownError=_HpnicfPortalStatAuthUnknownError_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,4,12),_HpnicfPortalStatAuthUnknownError_Type())
hpnicfPortalStatAuthUnknownError.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPortalStatAuthUnknownError.setStatus(_A)
_HpnicfPortalStatAuthResp_Type=Counter64
_HpnicfPortalStatAuthResp_Object=MibScalar
hpnicfPortalStatAuthResp=_HpnicfPortalStatAuthResp_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,4,13),_HpnicfPortalStatAuthResp_Type())
hpnicfPortalStatAuthResp.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPortalStatAuthResp.setStatus(_A)
_HpnicfPortalStatChallengeReq_Type=Counter64
_HpnicfPortalStatChallengeReq_Object=MibScalar
hpnicfPortalStatChallengeReq=_HpnicfPortalStatChallengeReq_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,4,14),_HpnicfPortalStatChallengeReq_Type())
hpnicfPortalStatChallengeReq.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPortalStatChallengeReq.setStatus(_A)
_HpnicfPortalStatChallengeResp_Type=Counter64
_HpnicfPortalStatChallengeResp_Object=MibScalar
hpnicfPortalStatChallengeResp=_HpnicfPortalStatChallengeResp_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,4,15),_HpnicfPortalStatChallengeResp_Type())
hpnicfPortalStatChallengeResp.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPortalStatChallengeResp.setStatus(_A)
_HpnicfPortalStatHttpReq_Type=Counter64
_HpnicfPortalStatHttpReq_Object=MibScalar
hpnicfPortalStatHttpReq=_HpnicfPortalStatHttpReq_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,4,16),_HpnicfPortalStatHttpReq_Type())
hpnicfPortalStatHttpReq.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPortalStatHttpReq.setStatus(_A)
_HpnicfPortalStatHttpResp_Type=Counter64
_HpnicfPortalStatHttpResp_Object=MibScalar
hpnicfPortalStatHttpResp=_HpnicfPortalStatHttpResp_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,4,17),_HpnicfPortalStatHttpResp_Type())
hpnicfPortalStatHttpResp.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPortalStatHttpResp.setStatus(_A)
_HpnicfPortalPktStatistic_ObjectIdentity=ObjectIdentity
hpnicfPortalPktStatistic=_HpnicfPortalPktStatistic_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,99,5))
_HpnicfPortalPktStaReqAuthNum_Type=Counter64
_HpnicfPortalPktStaReqAuthNum_Object=MibScalar
hpnicfPortalPktStaReqAuthNum=_HpnicfPortalPktStaReqAuthNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,5,1),_HpnicfPortalPktStaReqAuthNum_Type())
hpnicfPortalPktStaReqAuthNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPortalPktStaReqAuthNum.setStatus(_A)
_HpnicfPortalPktStaAckAuthSuccess_Type=Counter64
_HpnicfPortalPktStaAckAuthSuccess_Object=MibScalar
hpnicfPortalPktStaAckAuthSuccess=_HpnicfPortalPktStaAckAuthSuccess_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,5,2),_HpnicfPortalPktStaAckAuthSuccess_Type())
hpnicfPortalPktStaAckAuthSuccess.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPortalPktStaAckAuthSuccess.setStatus(_A)
_HpnicfPortalPktStaAckAuthReject_Type=Counter64
_HpnicfPortalPktStaAckAuthReject_Object=MibScalar
hpnicfPortalPktStaAckAuthReject=_HpnicfPortalPktStaAckAuthReject_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,5,3),_HpnicfPortalPktStaAckAuthReject_Type())
hpnicfPortalPktStaAckAuthReject.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPortalPktStaAckAuthReject.setStatus(_A)
_HpnicfPortalPktStaAckAuthEstablish_Type=Counter64
_HpnicfPortalPktStaAckAuthEstablish_Object=MibScalar
hpnicfPortalPktStaAckAuthEstablish=_HpnicfPortalPktStaAckAuthEstablish_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,5,4),_HpnicfPortalPktStaAckAuthEstablish_Type())
hpnicfPortalPktStaAckAuthEstablish.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPortalPktStaAckAuthEstablish.setStatus(_A)
_HpnicfPortalPktStaAckAuthBusy_Type=Counter64
_HpnicfPortalPktStaAckAuthBusy_Object=MibScalar
hpnicfPortalPktStaAckAuthBusy=_HpnicfPortalPktStaAckAuthBusy_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,5,5),_HpnicfPortalPktStaAckAuthBusy_Type())
hpnicfPortalPktStaAckAuthBusy.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPortalPktStaAckAuthBusy.setStatus(_A)
_HpnicfPortalPktStaAckAuthAuthFail_Type=Counter64
_HpnicfPortalPktStaAckAuthAuthFail_Object=MibScalar
hpnicfPortalPktStaAckAuthAuthFail=_HpnicfPortalPktStaAckAuthAuthFail_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,5,6),_HpnicfPortalPktStaAckAuthAuthFail_Type())
hpnicfPortalPktStaAckAuthAuthFail.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPortalPktStaAckAuthAuthFail.setStatus(_A)
_HpnicfPortalPktStaReqChallengeNum_Type=Counter64
_HpnicfPortalPktStaReqChallengeNum_Object=MibScalar
hpnicfPortalPktStaReqChallengeNum=_HpnicfPortalPktStaReqChallengeNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,5,7),_HpnicfPortalPktStaReqChallengeNum_Type())
hpnicfPortalPktStaReqChallengeNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPortalPktStaReqChallengeNum.setStatus(_A)
_HpnicfPortalPktStaAckChallengeSuccess_Type=Counter64
_HpnicfPortalPktStaAckChallengeSuccess_Object=MibScalar
hpnicfPortalPktStaAckChallengeSuccess=_HpnicfPortalPktStaAckChallengeSuccess_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,5,8),_HpnicfPortalPktStaAckChallengeSuccess_Type())
hpnicfPortalPktStaAckChallengeSuccess.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPortalPktStaAckChallengeSuccess.setStatus(_A)
_HpnicfPortalPktStaAckChallengeReject_Type=Counter64
_HpnicfPortalPktStaAckChallengeReject_Object=MibScalar
hpnicfPortalPktStaAckChallengeReject=_HpnicfPortalPktStaAckChallengeReject_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,5,9),_HpnicfPortalPktStaAckChallengeReject_Type())
hpnicfPortalPktStaAckChallengeReject.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPortalPktStaAckChallengeReject.setStatus(_A)
_HpnicfPortalPktStaAckChallengeEstablish_Type=Counter64
_HpnicfPortalPktStaAckChallengeEstablish_Object=MibScalar
hpnicfPortalPktStaAckChallengeEstablish=_HpnicfPortalPktStaAckChallengeEstablish_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,5,10),_HpnicfPortalPktStaAckChallengeEstablish_Type())
hpnicfPortalPktStaAckChallengeEstablish.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPortalPktStaAckChallengeEstablish.setStatus(_A)
_HpnicfPortalPktStaAckChallengeBusy_Type=Counter64
_HpnicfPortalPktStaAckChallengeBusy_Object=MibScalar
hpnicfPortalPktStaAckChallengeBusy=_HpnicfPortalPktStaAckChallengeBusy_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,5,11),_HpnicfPortalPktStaAckChallengeBusy_Type())
hpnicfPortalPktStaAckChallengeBusy.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPortalPktStaAckChallengeBusy.setStatus(_A)
_HpnicfPortalPktStaAckChallengeAuthFail_Type=Counter64
_HpnicfPortalPktStaAckChallengeAuthFail_Object=MibScalar
hpnicfPortalPktStaAckChallengeAuthFail=_HpnicfPortalPktStaAckChallengeAuthFail_Object((1,3,6,1,4,1,11,2,14,11,15,2,99,5,12),_HpnicfPortalPktStaAckChallengeAuthFail_Type())
hpnicfPortalPktStaAckChallengeAuthFail.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPortalPktStaAckChallengeAuthFail.setStatus(_A)
hpnicfPortalServerLost=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,99,3,0,1))
hpnicfPortalServerLost.setObjects(*((_D,_I),(_D,_K),(_D,_L),(_D,_M)))
if mibBuilder.loadTexts:hpnicfPortalServerLost.setStatus(_A)
hpnicfPortalServerGet=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,99,3,0,2))
hpnicfPortalServerGet.setObjects(*((_D,_I),(_D,_K),(_D,_L),(_D,_M)))
if mibBuilder.loadTexts:hpnicfPortalServerGet.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'hpnicfPortal':hpnicfPortal,'hpnicfPortalConfig':hpnicfPortalConfig,'hpnicfPortalMaxUserNumber':hpnicfPortalMaxUserNumber,'hpnicfPortalCurrentUserNumber':hpnicfPortalCurrentUserNumber,'hpnicfPortalStatus':hpnicfPortalStatus,'hpnicfPortalUserNumberUpperLimit':hpnicfPortalUserNumberUpperLimit,'hpnicfPortalNasId':hpnicfPortalNasId,'hpnicfPortalTables':hpnicfPortalTables,'hpnicfPortalServerTable':hpnicfPortalServerTable,'hpnicfPortalServerEntry':hpnicfPortalServerEntry,_I:hpnicfPortalServerName,'hpnicfPortalServerUrl':hpnicfPortalServerUrl,_M:hpnicfPortalServerPort,'hpnicfPortalIfInfoTable':hpnicfPortalIfInfoTable,'hpnicfPortalIfInfoEntry':hpnicfPortalIfInfoEntry,'hpnicfPortalAuthReqNumber':hpnicfPortalAuthReqNumber,'hpnicfPortalAuthSuccNumber':hpnicfPortalAuthSuccNumber,'hpnicfPortalAuthFailNumber':hpnicfPortalAuthFailNumber,'hpnicfPortalIfServerTable':hpnicfPortalIfServerTable,'hpnicfPortalIfServerEntry':hpnicfPortalIfServerEntry,_P:hpnicfPortalIfServerIndex,'hpnicfPortalIfServerUrl':hpnicfPortalIfServerUrl,'hpnicfPortalIfServerRowStatus':hpnicfPortalIfServerRowStatus,'hpnicfPortalIfVlanNasIDTable':hpnicfPortalIfVlanNasIDTable,'hpnicfPortalIfVlanNasIDEntry':hpnicfPortalIfVlanNasIDEntry,_Q:hpnicfPortalIfVlanNasIDIfIndex,_R:hpnicfPortalIfVlanNasIDVlanID,'hpnicfPortalIfVlanNasIDNasID':hpnicfPortalIfVlanNasIDNasID,'hpnicfPortalSSIDFreeRuleTable':hpnicfPortalSSIDFreeRuleTable,'hpnicfPortalSSIDFreeRuleEntry':hpnicfPortalSSIDFreeRuleEntry,_S:hpnicfPortalSSIDFreeRuleIndex,'hpnicfPortalSSIDFreeRuleSrcSSID':hpnicfPortalSSIDFreeRuleSrcSSID,'hpnicfPortalSSIDFreeRuleRowStatus':hpnicfPortalSSIDFreeRuleRowStatus,'hpnicfPortalSSIDFreeRuleSrcSpot':hpnicfPortalSSIDFreeRuleSrcSpot,'hpnicfPortalMacTriggerSrvTable':hpnicfPortalMacTriggerSrvTable,'hpnicfPortalMacTriggerSrvEntry':hpnicfPortalMacTriggerSrvEntry,_T:hpnicfPortalMacTriggerSrvIndex,'hpnicfPortalMacTriggerSrvIPAddrType':hpnicfPortalMacTriggerSrvIPAddrType,'hpnicfPortalMacTriggerSrvIP':hpnicfPortalMacTriggerSrvIP,'hpnicfPortalMacTriggerSrvPort':hpnicfPortalMacTriggerSrvPort,'hpnicfPortalMacTriggerSrvRowStatus':hpnicfPortalMacTriggerSrvRowStatus,'hpnicfPortalMacTriggerOnIfTable':hpnicfPortalMacTriggerOnIfTable,'hpnicfPortalMacTriggerOnIfEntry':hpnicfPortalMacTriggerOnIfEntry,_U:hpnicfPortalMacTriggerOnIfIfIndex,'hpnicfPortalMacTriggerOnIfDetctFlowPeriod':hpnicfPortalMacTriggerOnIfDetctFlowPeriod,'hpnicfPortalMacTriggerOnIfThresholdFlow':hpnicfPortalMacTriggerOnIfThresholdFlow,'hpnicfPortalMacTriggerOnIfRowStatus':hpnicfPortalMacTriggerOnIfRowStatus,'hpnicfPortalFreeRuleTable':hpnicfPortalFreeRuleTable,'hpnicfPortalFreeRuleEntry':hpnicfPortalFreeRuleEntry,_V:hpnicfPortalFreeRuleIndex,'hpnicfPortalFreeRuleSrcIfIndex':hpnicfPortalFreeRuleSrcIfIndex,'hpnicfPortalFreeRuleSrcVlanID':hpnicfPortalFreeRuleSrcVlanID,'hpnicfPortalFreeRuleSrcMac':hpnicfPortalFreeRuleSrcMac,'hpnicfPortalFreeRuleAddrType':hpnicfPortalFreeRuleAddrType,'hpnicfPortalFreeRuleSrcAddr':hpnicfPortalFreeRuleSrcAddr,'hpnicfPortalFreeRuleSrcPrefix':hpnicfPortalFreeRuleSrcPrefix,'hpnicfPortalFreeRuleDstAddr':hpnicfPortalFreeRuleDstAddr,'hpnicfPortalFreeRuleDstPrefix':hpnicfPortalFreeRuleDstPrefix,'hpnicfPortalFreeRuleProtocol':hpnicfPortalFreeRuleProtocol,'hpnicfPortalFreeRuleSrcPort':hpnicfPortalFreeRuleSrcPort,'hpnicfPortalFreeRuleDstPort':hpnicfPortalFreeRuleDstPort,'hpnicfPortalFreeRuleRowStatus':hpnicfPortalFreeRuleRowStatus,'hpnicfPortalForbiddenRuleTable':hpnicfPortalForbiddenRuleTable,'hpnicfPortalForbiddenRuleEntry':hpnicfPortalForbiddenRuleEntry,_X:hpnicfPortalForbiddenRuleIndex,'hpnicfPortalForbiddenRuleSrcIfIndex':hpnicfPortalForbiddenRuleSrcIfIndex,'hpnicfPortalForbiddenRuleSrcVlanID':hpnicfPortalForbiddenRuleSrcVlanID,'hpnicfPortalForbiddenRuleSrcMac':hpnicfPortalForbiddenRuleSrcMac,'hpnicfPortalForbiddenRuleAddrType':hpnicfPortalForbiddenRuleAddrType,'hpnicfPortalForbiddenRuleSrcAddr':hpnicfPortalForbiddenRuleSrcAddr,'hpnicfPortalForbiddenRuleSrcPrefix':hpnicfPortalForbiddenRuleSrcPrefix,'hpnicfPortalForbiddenRuleDstAddr':hpnicfPortalForbiddenRuleDstAddr,'hpnicfPortalForbiddenRuleDstPrefix':hpnicfPortalForbiddenRuleDstPrefix,'hpnicfPortalForbiddenRuleProtocol':hpnicfPortalForbiddenRuleProtocol,'hpnicfPortalForbiddenRuleSrcPort':hpnicfPortalForbiddenRuleSrcPort,'hpnicfPortalForbiddenRuleDstPort':hpnicfPortalForbiddenRuleDstPort,'hpnicfPortalForbiddenRuleRowStatus':hpnicfPortalForbiddenRuleRowStatus,'hpnicfPortalTraps':hpnicfPortalTraps,'hpnicfPortalTrapPrefix':hpnicfPortalTrapPrefix,'hpnicfPortalServerLost':hpnicfPortalServerLost,'hpnicfPortalServerGet':hpnicfPortalServerGet,'hpnicfPortalTrapVarObjects':hpnicfPortalTrapVarObjects,_K:hpnicfPortalFirstTrapTime,_L:hpnicfPortalServerIP,'hpnicfPortalStatistic':hpnicfPortalStatistic,'hpnicfPortalStatAuthReq':hpnicfPortalStatAuthReq,'hpnicfPortalStatAckLogout':hpnicfPortalStatAckLogout,'hpnicfPortalStatNotifyLogout':hpnicfPortalStatNotifyLogout,'hpnicfPortalStatChallengeTimeout':hpnicfPortalStatChallengeTimeout,'hpnicfPortalStatChallengeBusy':hpnicfPortalStatChallengeBusy,'hpnicfPortalStatChallengeFail':hpnicfPortalStatChallengeFail,'hpnicfPortalStatAuthTimeout':hpnicfPortalStatAuthTimeout,'hpnicfPortalStatAuthFail':hpnicfPortalStatAuthFail,'hpnicfPortalStatPwdError':hpnicfPortalStatPwdError,'hpnicfPortalStatAuthBusy':hpnicfPortalStatAuthBusy,'hpnicfPortalStatAuthDisordered':hpnicfPortalStatAuthDisordered,'hpnicfPortalStatAuthUnknownError':hpnicfPortalStatAuthUnknownError,'hpnicfPortalStatAuthResp':hpnicfPortalStatAuthResp,'hpnicfPortalStatChallengeReq':hpnicfPortalStatChallengeReq,'hpnicfPortalStatChallengeResp':hpnicfPortalStatChallengeResp,'hpnicfPortalStatHttpReq':hpnicfPortalStatHttpReq,'hpnicfPortalStatHttpResp':hpnicfPortalStatHttpResp,'hpnicfPortalPktStatistic':hpnicfPortalPktStatistic,'hpnicfPortalPktStaReqAuthNum':hpnicfPortalPktStaReqAuthNum,'hpnicfPortalPktStaAckAuthSuccess':hpnicfPortalPktStaAckAuthSuccess,'hpnicfPortalPktStaAckAuthReject':hpnicfPortalPktStaAckAuthReject,'hpnicfPortalPktStaAckAuthEstablish':hpnicfPortalPktStaAckAuthEstablish,'hpnicfPortalPktStaAckAuthBusy':hpnicfPortalPktStaAckAuthBusy,'hpnicfPortalPktStaAckAuthAuthFail':hpnicfPortalPktStaAckAuthAuthFail,'hpnicfPortalPktStaReqChallengeNum':hpnicfPortalPktStaReqChallengeNum,'hpnicfPortalPktStaAckChallengeSuccess':hpnicfPortalPktStaAckChallengeSuccess,'hpnicfPortalPktStaAckChallengeReject':hpnicfPortalPktStaAckChallengeReject,'hpnicfPortalPktStaAckChallengeEstablish':hpnicfPortalPktStaAckChallengeEstablish,'hpnicfPortalPktStaAckChallengeBusy':hpnicfPortalPktStaAckChallengeBusy,'hpnicfPortalPktStaAckChallengeAuthFail':hpnicfPortalPktStaAckChallengeAuthFail})