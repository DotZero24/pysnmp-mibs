_i='h3cPortalDot11Ipv6SrvTemName'
_h='h3cPortalDot11SrvTemName'
_g='h3cPortalExtIfIpv6Index'
_f='h3cPortalExtIfIndex'
_e='h3cPortalExtMTSrvName'
_d='h3cPortalExtWebSrvName'
_c='h3cPortalExtSrvName'
_b='h3cPortalForbiddenRuleIndex'
_a='h3cPortalFreeRuleIndex'
_Z='seconds'
_Y='h3cPortalMacTriggerOnIfIfIndex'
_X='h3cPortalMacTriggerSrvIndex'
_W='h3cPortalSSIDFreeRuleIndex'
_V='h3cPortalIfVlanNasIDVlanID'
_U='h3cPortalIfVlanNasIDIfIndex'
_T='h3cPortalIfServerIndex'
_S='disabled'
_R='enabled'
_Q='ifIndex'
_P='IF-MIB'
_O='h3cPortalServerPort'
_N='h3cPortalServerIP'
_M='h3cPortalFirstTrapTime'
_L='accessible-for-notify'
_K='invalid'
_J='Unsigned32'
_I='h3cPortalServerName'
_H='OctetString'
_G='not-accessible'
_F='Integer32'
_E='read-write'
_D='H3C-PORTAL-MIB'
_C='read-only'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_P,'InterfaceIndex',_Q)
InetAddress,InetAddressIPv4,InetAddressPrefixLength,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressIPv4','InetAddressPrefixLength','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_J,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
h3cPortal=ModuleIdentity((1,3,6,1,4,1,2011,10,2,99))
if mibBuilder.loadTexts:h3cPortal.setRevisions(('2016-07-14 10:20','2015-10-08 10:20'))
class H3cPortalAuthMethod(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_K,1),('direct',2),('layer3',3),('redhcp',4)))
_H3cPortalConfig_ObjectIdentity=ObjectIdentity
h3cPortalConfig=_H3cPortalConfig_ObjectIdentity((1,3,6,1,4,1,2011,10,2,99,1))
_H3cPortalMaxUserNumber_Type=Integer32
_H3cPortalMaxUserNumber_Object=MibScalar
h3cPortalMaxUserNumber=_H3cPortalMaxUserNumber_Object((1,3,6,1,4,1,2011,10,2,99,1,1),_H3cPortalMaxUserNumber_Type())
h3cPortalMaxUserNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPortalMaxUserNumber.setStatus(_A)
_H3cPortalCurrentUserNumber_Type=Integer32
_H3cPortalCurrentUserNumber_Object=MibScalar
h3cPortalCurrentUserNumber=_H3cPortalCurrentUserNumber_Object((1,3,6,1,4,1,2011,10,2,99,1,2),_H3cPortalCurrentUserNumber_Type())
h3cPortalCurrentUserNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPortalCurrentUserNumber.setStatus(_A)
class _H3cPortalStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_S,2)))
_H3cPortalStatus_Type.__name__=_F
_H3cPortalStatus_Object=MibScalar
h3cPortalStatus=_H3cPortalStatus_Object((1,3,6,1,4,1,2011,10,2,99,1,3),_H3cPortalStatus_Type())
h3cPortalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPortalStatus.setStatus(_A)
_H3cPortalUserNumberUpperLimit_Type=Integer32
_H3cPortalUserNumberUpperLimit_Object=MibScalar
h3cPortalUserNumberUpperLimit=_H3cPortalUserNumberUpperLimit_Object((1,3,6,1,4,1,2011,10,2,99,1,4),_H3cPortalUserNumberUpperLimit_Type())
h3cPortalUserNumberUpperLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPortalUserNumberUpperLimit.setStatus(_A)
_H3cPortalNasId_Type=OctetString
_H3cPortalNasId_Object=MibScalar
h3cPortalNasId=_H3cPortalNasId_Object((1,3,6,1,4,1,2011,10,2,99,1,5),_H3cPortalNasId_Type())
h3cPortalNasId.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPortalNasId.setStatus(_A)
_H3cPortalTables_ObjectIdentity=ObjectIdentity
h3cPortalTables=_H3cPortalTables_ObjectIdentity((1,3,6,1,4,1,2011,10,2,99,2))
_H3cPortalServerTable_Object=MibTable
h3cPortalServerTable=_H3cPortalServerTable_Object((1,3,6,1,4,1,2011,10,2,99,2,1))
if mibBuilder.loadTexts:h3cPortalServerTable.setStatus(_A)
_H3cPortalServerEntry_Object=MibTableRow
h3cPortalServerEntry=_H3cPortalServerEntry_Object((1,3,6,1,4,1,2011,10,2,99,2,1,1))
h3cPortalServerEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:h3cPortalServerEntry.setStatus(_A)
class _H3cPortalServerName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_H3cPortalServerName_Type.__name__=_H
_H3cPortalServerName_Object=MibTableColumn
h3cPortalServerName=_H3cPortalServerName_Object((1,3,6,1,4,1,2011,10,2,99,2,1,1,1),_H3cPortalServerName_Type())
h3cPortalServerName.setMaxAccess(_L)
if mibBuilder.loadTexts:h3cPortalServerName.setStatus(_A)
class _H3cPortalServerUrl_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,127))
_H3cPortalServerUrl_Type.__name__=_H
_H3cPortalServerUrl_Object=MibTableColumn
h3cPortalServerUrl=_H3cPortalServerUrl_Object((1,3,6,1,4,1,2011,10,2,99,2,1,1,2),_H3cPortalServerUrl_Type())
h3cPortalServerUrl.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPortalServerUrl.setStatus(_A)
class _H3cPortalServerPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65534))
_H3cPortalServerPort_Type.__name__=_F
_H3cPortalServerPort_Object=MibTableColumn
h3cPortalServerPort=_H3cPortalServerPort_Object((1,3,6,1,4,1,2011,10,2,99,2,1,1,3),_H3cPortalServerPort_Type())
h3cPortalServerPort.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPortalServerPort.setStatus(_A)
_H3cPortalIfInfoTable_Object=MibTable
h3cPortalIfInfoTable=_H3cPortalIfInfoTable_Object((1,3,6,1,4,1,2011,10,2,99,2,2))
if mibBuilder.loadTexts:h3cPortalIfInfoTable.setStatus(_A)
_H3cPortalIfInfoEntry_Object=MibTableRow
h3cPortalIfInfoEntry=_H3cPortalIfInfoEntry_Object((1,3,6,1,4,1,2011,10,2,99,2,2,1))
h3cPortalIfInfoEntry.setIndexNames((0,_P,_Q))
if mibBuilder.loadTexts:h3cPortalIfInfoEntry.setStatus(_A)
_H3cPortalAuthReqNumber_Type=Integer32
_H3cPortalAuthReqNumber_Object=MibTableColumn
h3cPortalAuthReqNumber=_H3cPortalAuthReqNumber_Object((1,3,6,1,4,1,2011,10,2,99,2,2,1,1),_H3cPortalAuthReqNumber_Type())
h3cPortalAuthReqNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPortalAuthReqNumber.setStatus(_A)
_H3cPortalAuthSuccNumber_Type=Integer32
_H3cPortalAuthSuccNumber_Object=MibTableColumn
h3cPortalAuthSuccNumber=_H3cPortalAuthSuccNumber_Object((1,3,6,1,4,1,2011,10,2,99,2,2,1,2),_H3cPortalAuthSuccNumber_Type())
h3cPortalAuthSuccNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPortalAuthSuccNumber.setStatus(_A)
_H3cPortalAuthFailNumber_Type=Integer32
_H3cPortalAuthFailNumber_Object=MibTableColumn
h3cPortalAuthFailNumber=_H3cPortalAuthFailNumber_Object((1,3,6,1,4,1,2011,10,2,99,2,2,1,3),_H3cPortalAuthFailNumber_Type())
h3cPortalAuthFailNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPortalAuthFailNumber.setStatus(_A)
_H3cPortalIfServerTable_Object=MibTable
h3cPortalIfServerTable=_H3cPortalIfServerTable_Object((1,3,6,1,4,1,2011,10,2,99,2,3))
if mibBuilder.loadTexts:h3cPortalIfServerTable.setStatus(_A)
_H3cPortalIfServerEntry_Object=MibTableRow
h3cPortalIfServerEntry=_H3cPortalIfServerEntry_Object((1,3,6,1,4,1,2011,10,2,99,2,3,1))
h3cPortalIfServerEntry.setIndexNames((0,_D,_T))
if mibBuilder.loadTexts:h3cPortalIfServerEntry.setStatus(_A)
class _H3cPortalIfServerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_H3cPortalIfServerIndex_Type.__name__=_F
_H3cPortalIfServerIndex_Object=MibTableColumn
h3cPortalIfServerIndex=_H3cPortalIfServerIndex_Object((1,3,6,1,4,1,2011,10,2,99,2,3,1,1),_H3cPortalIfServerIndex_Type())
h3cPortalIfServerIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cPortalIfServerIndex.setStatus(_A)
_H3cPortalIfServerUrl_Type=OctetString
_H3cPortalIfServerUrl_Object=MibTableColumn
h3cPortalIfServerUrl=_H3cPortalIfServerUrl_Object((1,3,6,1,4,1,2011,10,2,99,2,3,1,2),_H3cPortalIfServerUrl_Type())
h3cPortalIfServerUrl.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPortalIfServerUrl.setStatus(_A)
_H3cPortalIfServerRowStatus_Type=RowStatus
_H3cPortalIfServerRowStatus_Object=MibTableColumn
h3cPortalIfServerRowStatus=_H3cPortalIfServerRowStatus_Object((1,3,6,1,4,1,2011,10,2,99,2,3,1,3),_H3cPortalIfServerRowStatus_Type())
h3cPortalIfServerRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPortalIfServerRowStatus.setStatus(_A)
_H3cPortalIfVlanNasIDTable_Object=MibTable
h3cPortalIfVlanNasIDTable=_H3cPortalIfVlanNasIDTable_Object((1,3,6,1,4,1,2011,10,2,99,2,4))
if mibBuilder.loadTexts:h3cPortalIfVlanNasIDTable.setStatus(_A)
_H3cPortalIfVlanNasIDEntry_Object=MibTableRow
h3cPortalIfVlanNasIDEntry=_H3cPortalIfVlanNasIDEntry_Object((1,3,6,1,4,1,2011,10,2,99,2,4,1))
h3cPortalIfVlanNasIDEntry.setIndexNames((0,_D,_U),(0,_D,_V))
if mibBuilder.loadTexts:h3cPortalIfVlanNasIDEntry.setStatus(_A)
_H3cPortalIfVlanNasIDIfIndex_Type=InterfaceIndex
_H3cPortalIfVlanNasIDIfIndex_Object=MibTableColumn
h3cPortalIfVlanNasIDIfIndex=_H3cPortalIfVlanNasIDIfIndex_Object((1,3,6,1,4,1,2011,10,2,99,2,4,1,1),_H3cPortalIfVlanNasIDIfIndex_Type())
h3cPortalIfVlanNasIDIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cPortalIfVlanNasIDIfIndex.setStatus(_A)
class _H3cPortalIfVlanNasIDVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cPortalIfVlanNasIDVlanID_Type.__name__=_F
_H3cPortalIfVlanNasIDVlanID_Object=MibTableColumn
h3cPortalIfVlanNasIDVlanID=_H3cPortalIfVlanNasIDVlanID_Object((1,3,6,1,4,1,2011,10,2,99,2,4,1,2),_H3cPortalIfVlanNasIDVlanID_Type())
h3cPortalIfVlanNasIDVlanID.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cPortalIfVlanNasIDVlanID.setStatus(_A)
class _H3cPortalIfVlanNasIDNasID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_H3cPortalIfVlanNasIDNasID_Type.__name__=_H
_H3cPortalIfVlanNasIDNasID_Object=MibTableColumn
h3cPortalIfVlanNasIDNasID=_H3cPortalIfVlanNasIDNasID_Object((1,3,6,1,4,1,2011,10,2,99,2,4,1,3),_H3cPortalIfVlanNasIDNasID_Type())
h3cPortalIfVlanNasIDNasID.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPortalIfVlanNasIDNasID.setStatus(_A)
_H3cPortalSSIDFreeRuleTable_Object=MibTable
h3cPortalSSIDFreeRuleTable=_H3cPortalSSIDFreeRuleTable_Object((1,3,6,1,4,1,2011,10,2,99,2,5))
if mibBuilder.loadTexts:h3cPortalSSIDFreeRuleTable.setStatus(_A)
_H3cPortalSSIDFreeRuleEntry_Object=MibTableRow
h3cPortalSSIDFreeRuleEntry=_H3cPortalSSIDFreeRuleEntry_Object((1,3,6,1,4,1,2011,10,2,99,2,5,1))
h3cPortalSSIDFreeRuleEntry.setIndexNames((0,_D,_W))
if mibBuilder.loadTexts:h3cPortalSSIDFreeRuleEntry.setStatus(_A)
class _H3cPortalSSIDFreeRuleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_H3cPortalSSIDFreeRuleIndex_Type.__name__=_F
_H3cPortalSSIDFreeRuleIndex_Object=MibTableColumn
h3cPortalSSIDFreeRuleIndex=_H3cPortalSSIDFreeRuleIndex_Object((1,3,6,1,4,1,2011,10,2,99,2,5,1,1),_H3cPortalSSIDFreeRuleIndex_Type())
h3cPortalSSIDFreeRuleIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cPortalSSIDFreeRuleIndex.setStatus(_A)
class _H3cPortalSSIDFreeRuleSrcSSID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_H3cPortalSSIDFreeRuleSrcSSID_Type.__name__=_H
_H3cPortalSSIDFreeRuleSrcSSID_Object=MibTableColumn
h3cPortalSSIDFreeRuleSrcSSID=_H3cPortalSSIDFreeRuleSrcSSID_Object((1,3,6,1,4,1,2011,10,2,99,2,5,1,2),_H3cPortalSSIDFreeRuleSrcSSID_Type())
h3cPortalSSIDFreeRuleSrcSSID.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPortalSSIDFreeRuleSrcSSID.setStatus(_A)
_H3cPortalSSIDFreeRuleRowStatus_Type=RowStatus
_H3cPortalSSIDFreeRuleRowStatus_Object=MibTableColumn
h3cPortalSSIDFreeRuleRowStatus=_H3cPortalSSIDFreeRuleRowStatus_Object((1,3,6,1,4,1,2011,10,2,99,2,5,1,3),_H3cPortalSSIDFreeRuleRowStatus_Type())
h3cPortalSSIDFreeRuleRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPortalSSIDFreeRuleRowStatus.setStatus(_A)
class _H3cPortalSSIDFreeRuleSrcSpot_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_H3cPortalSSIDFreeRuleSrcSpot_Type.__name__=_H
_H3cPortalSSIDFreeRuleSrcSpot_Object=MibTableColumn
h3cPortalSSIDFreeRuleSrcSpot=_H3cPortalSSIDFreeRuleSrcSpot_Object((1,3,6,1,4,1,2011,10,2,99,2,5,1,4),_H3cPortalSSIDFreeRuleSrcSpot_Type())
h3cPortalSSIDFreeRuleSrcSpot.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPortalSSIDFreeRuleSrcSpot.setStatus(_A)
_H3cPortalMacTriggerSrvTable_Object=MibTable
h3cPortalMacTriggerSrvTable=_H3cPortalMacTriggerSrvTable_Object((1,3,6,1,4,1,2011,10,2,99,2,6))
if mibBuilder.loadTexts:h3cPortalMacTriggerSrvTable.setStatus(_A)
_H3cPortalMacTriggerSrvEntry_Object=MibTableRow
h3cPortalMacTriggerSrvEntry=_H3cPortalMacTriggerSrvEntry_Object((1,3,6,1,4,1,2011,10,2,99,2,6,1))
h3cPortalMacTriggerSrvEntry.setIndexNames((0,_D,_X))
if mibBuilder.loadTexts:h3cPortalMacTriggerSrvEntry.setStatus(_A)
class _H3cPortalMacTriggerSrvIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_H3cPortalMacTriggerSrvIndex_Type.__name__=_F
_H3cPortalMacTriggerSrvIndex_Object=MibTableColumn
h3cPortalMacTriggerSrvIndex=_H3cPortalMacTriggerSrvIndex_Object((1,3,6,1,4,1,2011,10,2,99,2,6,1,1),_H3cPortalMacTriggerSrvIndex_Type())
h3cPortalMacTriggerSrvIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cPortalMacTriggerSrvIndex.setStatus(_A)
_H3cPortalMacTriggerSrvIPAddrType_Type=InetAddressType
_H3cPortalMacTriggerSrvIPAddrType_Object=MibTableColumn
h3cPortalMacTriggerSrvIPAddrType=_H3cPortalMacTriggerSrvIPAddrType_Object((1,3,6,1,4,1,2011,10,2,99,2,6,1,2),_H3cPortalMacTriggerSrvIPAddrType_Type())
h3cPortalMacTriggerSrvIPAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPortalMacTriggerSrvIPAddrType.setStatus(_A)
_H3cPortalMacTriggerSrvIP_Type=InetAddress
_H3cPortalMacTriggerSrvIP_Object=MibTableColumn
h3cPortalMacTriggerSrvIP=_H3cPortalMacTriggerSrvIP_Object((1,3,6,1,4,1,2011,10,2,99,2,6,1,3),_H3cPortalMacTriggerSrvIP_Type())
h3cPortalMacTriggerSrvIP.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPortalMacTriggerSrvIP.setStatus(_A)
class _H3cPortalMacTriggerSrvPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65534))
_H3cPortalMacTriggerSrvPort_Type.__name__=_F
_H3cPortalMacTriggerSrvPort_Object=MibTableColumn
h3cPortalMacTriggerSrvPort=_H3cPortalMacTriggerSrvPort_Object((1,3,6,1,4,1,2011,10,2,99,2,6,1,4),_H3cPortalMacTriggerSrvPort_Type())
h3cPortalMacTriggerSrvPort.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPortalMacTriggerSrvPort.setStatus(_A)
_H3cPortalMacTriggerSrvRowStatus_Type=RowStatus
_H3cPortalMacTriggerSrvRowStatus_Object=MibTableColumn
h3cPortalMacTriggerSrvRowStatus=_H3cPortalMacTriggerSrvRowStatus_Object((1,3,6,1,4,1,2011,10,2,99,2,6,1,5),_H3cPortalMacTriggerSrvRowStatus_Type())
h3cPortalMacTriggerSrvRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPortalMacTriggerSrvRowStatus.setStatus(_A)
_H3cPortalMacTriggerOnIfTable_Object=MibTable
h3cPortalMacTriggerOnIfTable=_H3cPortalMacTriggerOnIfTable_Object((1,3,6,1,4,1,2011,10,2,99,2,7))
if mibBuilder.loadTexts:h3cPortalMacTriggerOnIfTable.setStatus(_A)
_H3cPortalMacTriggerOnIfEntry_Object=MibTableRow
h3cPortalMacTriggerOnIfEntry=_H3cPortalMacTriggerOnIfEntry_Object((1,3,6,1,4,1,2011,10,2,99,2,7,1))
h3cPortalMacTriggerOnIfEntry.setIndexNames((0,_D,_Y))
if mibBuilder.loadTexts:h3cPortalMacTriggerOnIfEntry.setStatus(_A)
_H3cPortalMacTriggerOnIfIfIndex_Type=InterfaceIndex
_H3cPortalMacTriggerOnIfIfIndex_Object=MibTableColumn
h3cPortalMacTriggerOnIfIfIndex=_H3cPortalMacTriggerOnIfIfIndex_Object((1,3,6,1,4,1,2011,10,2,99,2,7,1,1),_H3cPortalMacTriggerOnIfIfIndex_Type())
h3cPortalMacTriggerOnIfIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cPortalMacTriggerOnIfIfIndex.setStatus(_A)
class _H3cPortalMacTriggerOnIfDetctFlowPeriod_Type(Integer32):defaultValue=300
_H3cPortalMacTriggerOnIfDetctFlowPeriod_Type.__name__=_F
_H3cPortalMacTriggerOnIfDetctFlowPeriod_Object=MibTableColumn
h3cPortalMacTriggerOnIfDetctFlowPeriod=_H3cPortalMacTriggerOnIfDetctFlowPeriod_Object((1,3,6,1,4,1,2011,10,2,99,2,7,1,2),_H3cPortalMacTriggerOnIfDetctFlowPeriod_Type())
h3cPortalMacTriggerOnIfDetctFlowPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPortalMacTriggerOnIfDetctFlowPeriod.setStatus(_A)
if mibBuilder.loadTexts:h3cPortalMacTriggerOnIfDetctFlowPeriod.setUnits(_Z)
class _H3cPortalMacTriggerOnIfThresholdFlow_Type(Unsigned32):defaultValue=0
_H3cPortalMacTriggerOnIfThresholdFlow_Type.__name__=_J
_H3cPortalMacTriggerOnIfThresholdFlow_Object=MibTableColumn
h3cPortalMacTriggerOnIfThresholdFlow=_H3cPortalMacTriggerOnIfThresholdFlow_Object((1,3,6,1,4,1,2011,10,2,99,2,7,1,3),_H3cPortalMacTriggerOnIfThresholdFlow_Type())
h3cPortalMacTriggerOnIfThresholdFlow.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPortalMacTriggerOnIfThresholdFlow.setStatus(_A)
if mibBuilder.loadTexts:h3cPortalMacTriggerOnIfThresholdFlow.setUnits('bytes')
_H3cPortalMacTriggerOnIfRowStatus_Type=RowStatus
_H3cPortalMacTriggerOnIfRowStatus_Object=MibTableColumn
h3cPortalMacTriggerOnIfRowStatus=_H3cPortalMacTriggerOnIfRowStatus_Object((1,3,6,1,4,1,2011,10,2,99,2,7,1,4),_H3cPortalMacTriggerOnIfRowStatus_Type())
h3cPortalMacTriggerOnIfRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPortalMacTriggerOnIfRowStatus.setStatus(_A)
_H3cPortalFreeRuleTable_Object=MibTable
h3cPortalFreeRuleTable=_H3cPortalFreeRuleTable_Object((1,3,6,1,4,1,2011,10,2,99,2,8))
if mibBuilder.loadTexts:h3cPortalFreeRuleTable.setStatus(_A)
_H3cPortalFreeRuleEntry_Object=MibTableRow
h3cPortalFreeRuleEntry=_H3cPortalFreeRuleEntry_Object((1,3,6,1,4,1,2011,10,2,99,2,8,1))
h3cPortalFreeRuleEntry.setIndexNames((0,_D,_a))
if mibBuilder.loadTexts:h3cPortalFreeRuleEntry.setStatus(_A)
class _H3cPortalFreeRuleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_H3cPortalFreeRuleIndex_Type.__name__=_F
_H3cPortalFreeRuleIndex_Object=MibTableColumn
h3cPortalFreeRuleIndex=_H3cPortalFreeRuleIndex_Object((1,3,6,1,4,1,2011,10,2,99,2,8,1,1),_H3cPortalFreeRuleIndex_Type())
h3cPortalFreeRuleIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cPortalFreeRuleIndex.setStatus(_A)
_H3cPortalFreeRuleSrcIfIndex_Type=InterfaceIndex
_H3cPortalFreeRuleSrcIfIndex_Object=MibTableColumn
h3cPortalFreeRuleSrcIfIndex=_H3cPortalFreeRuleSrcIfIndex_Object((1,3,6,1,4,1,2011,10,2,99,2,8,1,2),_H3cPortalFreeRuleSrcIfIndex_Type())
h3cPortalFreeRuleSrcIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPortalFreeRuleSrcIfIndex.setStatus(_A)
_H3cPortalFreeRuleSrcVlanID_Type=Integer32
_H3cPortalFreeRuleSrcVlanID_Object=MibTableColumn
h3cPortalFreeRuleSrcVlanID=_H3cPortalFreeRuleSrcVlanID_Object((1,3,6,1,4,1,2011,10,2,99,2,8,1,3),_H3cPortalFreeRuleSrcVlanID_Type())
h3cPortalFreeRuleSrcVlanID.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPortalFreeRuleSrcVlanID.setStatus(_A)
_H3cPortalFreeRuleSrcMac_Type=MacAddress
_H3cPortalFreeRuleSrcMac_Object=MibTableColumn
h3cPortalFreeRuleSrcMac=_H3cPortalFreeRuleSrcMac_Object((1,3,6,1,4,1,2011,10,2,99,2,8,1,4),_H3cPortalFreeRuleSrcMac_Type())
h3cPortalFreeRuleSrcMac.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPortalFreeRuleSrcMac.setStatus(_A)
_H3cPortalFreeRuleAddrType_Type=InetAddressType
_H3cPortalFreeRuleAddrType_Object=MibTableColumn
h3cPortalFreeRuleAddrType=_H3cPortalFreeRuleAddrType_Object((1,3,6,1,4,1,2011,10,2,99,2,8,1,5),_H3cPortalFreeRuleAddrType_Type())
h3cPortalFreeRuleAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPortalFreeRuleAddrType.setStatus(_A)
_H3cPortalFreeRuleSrcAddr_Type=InetAddress
_H3cPortalFreeRuleSrcAddr_Object=MibTableColumn
h3cPortalFreeRuleSrcAddr=_H3cPortalFreeRuleSrcAddr_Object((1,3,6,1,4,1,2011,10,2,99,2,8,1,6),_H3cPortalFreeRuleSrcAddr_Type())
h3cPortalFreeRuleSrcAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPortalFreeRuleSrcAddr.setStatus(_A)
_H3cPortalFreeRuleSrcPrefix_Type=InetAddressPrefixLength
_H3cPortalFreeRuleSrcPrefix_Object=MibTableColumn
h3cPortalFreeRuleSrcPrefix=_H3cPortalFreeRuleSrcPrefix_Object((1,3,6,1,4,1,2011,10,2,99,2,8,1,7),_H3cPortalFreeRuleSrcPrefix_Type())
h3cPortalFreeRuleSrcPrefix.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPortalFreeRuleSrcPrefix.setStatus(_A)
_H3cPortalFreeRuleDstAddr_Type=InetAddress
_H3cPortalFreeRuleDstAddr_Object=MibTableColumn
h3cPortalFreeRuleDstAddr=_H3cPortalFreeRuleDstAddr_Object((1,3,6,1,4,1,2011,10,2,99,2,8,1,8),_H3cPortalFreeRuleDstAddr_Type())
h3cPortalFreeRuleDstAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPortalFreeRuleDstAddr.setStatus(_A)
_H3cPortalFreeRuleDstPrefix_Type=InetAddressPrefixLength
_H3cPortalFreeRuleDstPrefix_Object=MibTableColumn
h3cPortalFreeRuleDstPrefix=_H3cPortalFreeRuleDstPrefix_Object((1,3,6,1,4,1,2011,10,2,99,2,8,1,9),_H3cPortalFreeRuleDstPrefix_Type())
h3cPortalFreeRuleDstPrefix.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPortalFreeRuleDstPrefix.setStatus(_A)
class _H3cPortalFreeRuleProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,6,17)));namedValues=NamedValues(*((_K,0),('tcp',6),('udp',17)))
_H3cPortalFreeRuleProtocol_Type.__name__=_F
_H3cPortalFreeRuleProtocol_Object=MibTableColumn
h3cPortalFreeRuleProtocol=_H3cPortalFreeRuleProtocol_Object((1,3,6,1,4,1,2011,10,2,99,2,8,1,10),_H3cPortalFreeRuleProtocol_Type())
h3cPortalFreeRuleProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPortalFreeRuleProtocol.setStatus(_A)
_H3cPortalFreeRuleSrcPort_Type=Integer32
_H3cPortalFreeRuleSrcPort_Object=MibTableColumn
h3cPortalFreeRuleSrcPort=_H3cPortalFreeRuleSrcPort_Object((1,3,6,1,4,1,2011,10,2,99,2,8,1,11),_H3cPortalFreeRuleSrcPort_Type())
h3cPortalFreeRuleSrcPort.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPortalFreeRuleSrcPort.setStatus(_A)
_H3cPortalFreeRuleDstPort_Type=Integer32
_H3cPortalFreeRuleDstPort_Object=MibTableColumn
h3cPortalFreeRuleDstPort=_H3cPortalFreeRuleDstPort_Object((1,3,6,1,4,1,2011,10,2,99,2,8,1,12),_H3cPortalFreeRuleDstPort_Type())
h3cPortalFreeRuleDstPort.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPortalFreeRuleDstPort.setStatus(_A)
_H3cPortalFreeRuleRowStatus_Type=RowStatus
_H3cPortalFreeRuleRowStatus_Object=MibTableColumn
h3cPortalFreeRuleRowStatus=_H3cPortalFreeRuleRowStatus_Object((1,3,6,1,4,1,2011,10,2,99,2,8,1,13),_H3cPortalFreeRuleRowStatus_Type())
h3cPortalFreeRuleRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPortalFreeRuleRowStatus.setStatus(_A)
_H3cPortalForbiddenRuleTable_Object=MibTable
h3cPortalForbiddenRuleTable=_H3cPortalForbiddenRuleTable_Object((1,3,6,1,4,1,2011,10,2,99,2,9))
if mibBuilder.loadTexts:h3cPortalForbiddenRuleTable.setStatus(_A)
_H3cPortalForbiddenRuleEntry_Object=MibTableRow
h3cPortalForbiddenRuleEntry=_H3cPortalForbiddenRuleEntry_Object((1,3,6,1,4,1,2011,10,2,99,2,9,1))
h3cPortalForbiddenRuleEntry.setIndexNames((0,_D,_b))
if mibBuilder.loadTexts:h3cPortalForbiddenRuleEntry.setStatus(_A)
class _H3cPortalForbiddenRuleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_H3cPortalForbiddenRuleIndex_Type.__name__=_F
_H3cPortalForbiddenRuleIndex_Object=MibTableColumn
h3cPortalForbiddenRuleIndex=_H3cPortalForbiddenRuleIndex_Object((1,3,6,1,4,1,2011,10,2,99,2,9,1,1),_H3cPortalForbiddenRuleIndex_Type())
h3cPortalForbiddenRuleIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cPortalForbiddenRuleIndex.setStatus(_A)
_H3cPortalForbiddenRuleSrcIfIndex_Type=InterfaceIndex
_H3cPortalForbiddenRuleSrcIfIndex_Object=MibTableColumn
h3cPortalForbiddenRuleSrcIfIndex=_H3cPortalForbiddenRuleSrcIfIndex_Object((1,3,6,1,4,1,2011,10,2,99,2,9,1,2),_H3cPortalForbiddenRuleSrcIfIndex_Type())
h3cPortalForbiddenRuleSrcIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPortalForbiddenRuleSrcIfIndex.setStatus(_A)
_H3cPortalForbiddenRuleSrcVlanID_Type=Integer32
_H3cPortalForbiddenRuleSrcVlanID_Object=MibTableColumn
h3cPortalForbiddenRuleSrcVlanID=_H3cPortalForbiddenRuleSrcVlanID_Object((1,3,6,1,4,1,2011,10,2,99,2,9,1,3),_H3cPortalForbiddenRuleSrcVlanID_Type())
h3cPortalForbiddenRuleSrcVlanID.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPortalForbiddenRuleSrcVlanID.setStatus(_A)
_H3cPortalForbiddenRuleSrcMac_Type=MacAddress
_H3cPortalForbiddenRuleSrcMac_Object=MibTableColumn
h3cPortalForbiddenRuleSrcMac=_H3cPortalForbiddenRuleSrcMac_Object((1,3,6,1,4,1,2011,10,2,99,2,9,1,4),_H3cPortalForbiddenRuleSrcMac_Type())
h3cPortalForbiddenRuleSrcMac.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPortalForbiddenRuleSrcMac.setStatus(_A)
_H3cPortalForbiddenRuleAddrType_Type=InetAddressType
_H3cPortalForbiddenRuleAddrType_Object=MibTableColumn
h3cPortalForbiddenRuleAddrType=_H3cPortalForbiddenRuleAddrType_Object((1,3,6,1,4,1,2011,10,2,99,2,9,1,5),_H3cPortalForbiddenRuleAddrType_Type())
h3cPortalForbiddenRuleAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPortalForbiddenRuleAddrType.setStatus(_A)
_H3cPortalForbiddenRuleSrcAddr_Type=InetAddress
_H3cPortalForbiddenRuleSrcAddr_Object=MibTableColumn
h3cPortalForbiddenRuleSrcAddr=_H3cPortalForbiddenRuleSrcAddr_Object((1,3,6,1,4,1,2011,10,2,99,2,9,1,6),_H3cPortalForbiddenRuleSrcAddr_Type())
h3cPortalForbiddenRuleSrcAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPortalForbiddenRuleSrcAddr.setStatus(_A)
_H3cPortalForbiddenRuleSrcPrefix_Type=InetAddressPrefixLength
_H3cPortalForbiddenRuleSrcPrefix_Object=MibTableColumn
h3cPortalForbiddenRuleSrcPrefix=_H3cPortalForbiddenRuleSrcPrefix_Object((1,3,6,1,4,1,2011,10,2,99,2,9,1,7),_H3cPortalForbiddenRuleSrcPrefix_Type())
h3cPortalForbiddenRuleSrcPrefix.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPortalForbiddenRuleSrcPrefix.setStatus(_A)
_H3cPortalForbiddenRuleDstAddr_Type=InetAddress
_H3cPortalForbiddenRuleDstAddr_Object=MibTableColumn
h3cPortalForbiddenRuleDstAddr=_H3cPortalForbiddenRuleDstAddr_Object((1,3,6,1,4,1,2011,10,2,99,2,9,1,8),_H3cPortalForbiddenRuleDstAddr_Type())
h3cPortalForbiddenRuleDstAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPortalForbiddenRuleDstAddr.setStatus(_A)
_H3cPortalForbiddenRuleDstPrefix_Type=InetAddressPrefixLength
_H3cPortalForbiddenRuleDstPrefix_Object=MibTableColumn
h3cPortalForbiddenRuleDstPrefix=_H3cPortalForbiddenRuleDstPrefix_Object((1,3,6,1,4,1,2011,10,2,99,2,9,1,9),_H3cPortalForbiddenRuleDstPrefix_Type())
h3cPortalForbiddenRuleDstPrefix.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPortalForbiddenRuleDstPrefix.setStatus(_A)
class _H3cPortalForbiddenRuleProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,6,17)));namedValues=NamedValues(*((_K,0),('tcp',6),('udp',17)))
_H3cPortalForbiddenRuleProtocol_Type.__name__=_F
_H3cPortalForbiddenRuleProtocol_Object=MibTableColumn
h3cPortalForbiddenRuleProtocol=_H3cPortalForbiddenRuleProtocol_Object((1,3,6,1,4,1,2011,10,2,99,2,9,1,10),_H3cPortalForbiddenRuleProtocol_Type())
h3cPortalForbiddenRuleProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPortalForbiddenRuleProtocol.setStatus(_A)
_H3cPortalForbiddenRuleSrcPort_Type=Integer32
_H3cPortalForbiddenRuleSrcPort_Object=MibTableColumn
h3cPortalForbiddenRuleSrcPort=_H3cPortalForbiddenRuleSrcPort_Object((1,3,6,1,4,1,2011,10,2,99,2,9,1,11),_H3cPortalForbiddenRuleSrcPort_Type())
h3cPortalForbiddenRuleSrcPort.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPortalForbiddenRuleSrcPort.setStatus(_A)
_H3cPortalForbiddenRuleDstPort_Type=Integer32
_H3cPortalForbiddenRuleDstPort_Object=MibTableColumn
h3cPortalForbiddenRuleDstPort=_H3cPortalForbiddenRuleDstPort_Object((1,3,6,1,4,1,2011,10,2,99,2,9,1,12),_H3cPortalForbiddenRuleDstPort_Type())
h3cPortalForbiddenRuleDstPort.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPortalForbiddenRuleDstPort.setStatus(_A)
_H3cPortalForbiddenRuleRowStatus_Type=RowStatus
_H3cPortalForbiddenRuleRowStatus_Object=MibTableColumn
h3cPortalForbiddenRuleRowStatus=_H3cPortalForbiddenRuleRowStatus_Object((1,3,6,1,4,1,2011,10,2,99,2,9,1,13),_H3cPortalForbiddenRuleRowStatus_Type())
h3cPortalForbiddenRuleRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPortalForbiddenRuleRowStatus.setStatus(_A)
class _H3cPortalForbiddenRuleSsidName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_H3cPortalForbiddenRuleSsidName_Type.__name__=_H
_H3cPortalForbiddenRuleSsidName_Object=MibTableColumn
h3cPortalForbiddenRuleSsidName=_H3cPortalForbiddenRuleSsidName_Object((1,3,6,1,4,1,2011,10,2,99,2,9,1,14),_H3cPortalForbiddenRuleSsidName_Type())
h3cPortalForbiddenRuleSsidName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPortalForbiddenRuleSsidName.setStatus(_A)
_H3cPortalTraps_ObjectIdentity=ObjectIdentity
h3cPortalTraps=_H3cPortalTraps_ObjectIdentity((1,3,6,1,4,1,2011,10,2,99,3))
_H3cPortalTrapPrefix_ObjectIdentity=ObjectIdentity
h3cPortalTrapPrefix=_H3cPortalTrapPrefix_ObjectIdentity((1,3,6,1,4,1,2011,10,2,99,3,0))
_H3cPortalTrapVarObjects_ObjectIdentity=ObjectIdentity
h3cPortalTrapVarObjects=_H3cPortalTrapVarObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,99,3,1))
_H3cPortalFirstTrapTime_Type=TimeTicks
_H3cPortalFirstTrapTime_Object=MibScalar
h3cPortalFirstTrapTime=_H3cPortalFirstTrapTime_Object((1,3,6,1,4,1,2011,10,2,99,3,1,1),_H3cPortalFirstTrapTime_Type())
h3cPortalFirstTrapTime.setMaxAccess(_L)
if mibBuilder.loadTexts:h3cPortalFirstTrapTime.setStatus(_A)
_H3cPortalServerIP_Type=InetAddressIPv4
_H3cPortalServerIP_Object=MibScalar
h3cPortalServerIP=_H3cPortalServerIP_Object((1,3,6,1,4,1,2011,10,2,99,3,1,2),_H3cPortalServerIP_Type())
h3cPortalServerIP.setMaxAccess(_L)
if mibBuilder.loadTexts:h3cPortalServerIP.setStatus(_A)
_H3cPortalStatistic_ObjectIdentity=ObjectIdentity
h3cPortalStatistic=_H3cPortalStatistic_ObjectIdentity((1,3,6,1,4,1,2011,10,2,99,4))
_H3cPortalStatAuthReq_Type=Counter64
_H3cPortalStatAuthReq_Object=MibScalar
h3cPortalStatAuthReq=_H3cPortalStatAuthReq_Object((1,3,6,1,4,1,2011,10,2,99,4,1),_H3cPortalStatAuthReq_Type())
h3cPortalStatAuthReq.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPortalStatAuthReq.setStatus(_A)
_H3cPortalStatAckLogout_Type=Counter64
_H3cPortalStatAckLogout_Object=MibScalar
h3cPortalStatAckLogout=_H3cPortalStatAckLogout_Object((1,3,6,1,4,1,2011,10,2,99,4,2),_H3cPortalStatAckLogout_Type())
h3cPortalStatAckLogout.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPortalStatAckLogout.setStatus(_A)
_H3cPortalStatNotifyLogout_Type=Counter64
_H3cPortalStatNotifyLogout_Object=MibScalar
h3cPortalStatNotifyLogout=_H3cPortalStatNotifyLogout_Object((1,3,6,1,4,1,2011,10,2,99,4,3),_H3cPortalStatNotifyLogout_Type())
h3cPortalStatNotifyLogout.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPortalStatNotifyLogout.setStatus(_A)
_H3cPortalStatChallengeTimeout_Type=Counter64
_H3cPortalStatChallengeTimeout_Object=MibScalar
h3cPortalStatChallengeTimeout=_H3cPortalStatChallengeTimeout_Object((1,3,6,1,4,1,2011,10,2,99,4,4),_H3cPortalStatChallengeTimeout_Type())
h3cPortalStatChallengeTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPortalStatChallengeTimeout.setStatus(_A)
_H3cPortalStatChallengeBusy_Type=Counter64
_H3cPortalStatChallengeBusy_Object=MibScalar
h3cPortalStatChallengeBusy=_H3cPortalStatChallengeBusy_Object((1,3,6,1,4,1,2011,10,2,99,4,5),_H3cPortalStatChallengeBusy_Type())
h3cPortalStatChallengeBusy.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPortalStatChallengeBusy.setStatus(_A)
_H3cPortalStatChallengeFail_Type=Counter64
_H3cPortalStatChallengeFail_Object=MibScalar
h3cPortalStatChallengeFail=_H3cPortalStatChallengeFail_Object((1,3,6,1,4,1,2011,10,2,99,4,6),_H3cPortalStatChallengeFail_Type())
h3cPortalStatChallengeFail.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPortalStatChallengeFail.setStatus(_A)
_H3cPortalStatAuthTimeout_Type=Counter64
_H3cPortalStatAuthTimeout_Object=MibScalar
h3cPortalStatAuthTimeout=_H3cPortalStatAuthTimeout_Object((1,3,6,1,4,1,2011,10,2,99,4,7),_H3cPortalStatAuthTimeout_Type())
h3cPortalStatAuthTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPortalStatAuthTimeout.setStatus(_A)
_H3cPortalStatAuthFail_Type=Counter64
_H3cPortalStatAuthFail_Object=MibScalar
h3cPortalStatAuthFail=_H3cPortalStatAuthFail_Object((1,3,6,1,4,1,2011,10,2,99,4,8),_H3cPortalStatAuthFail_Type())
h3cPortalStatAuthFail.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPortalStatAuthFail.setStatus(_A)
_H3cPortalStatPwdError_Type=Counter64
_H3cPortalStatPwdError_Object=MibScalar
h3cPortalStatPwdError=_H3cPortalStatPwdError_Object((1,3,6,1,4,1,2011,10,2,99,4,9),_H3cPortalStatPwdError_Type())
h3cPortalStatPwdError.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPortalStatPwdError.setStatus(_A)
_H3cPortalStatAuthBusy_Type=Counter64
_H3cPortalStatAuthBusy_Object=MibScalar
h3cPortalStatAuthBusy=_H3cPortalStatAuthBusy_Object((1,3,6,1,4,1,2011,10,2,99,4,10),_H3cPortalStatAuthBusy_Type())
h3cPortalStatAuthBusy.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPortalStatAuthBusy.setStatus(_A)
_H3cPortalStatAuthDisordered_Type=Counter64
_H3cPortalStatAuthDisordered_Object=MibScalar
h3cPortalStatAuthDisordered=_H3cPortalStatAuthDisordered_Object((1,3,6,1,4,1,2011,10,2,99,4,11),_H3cPortalStatAuthDisordered_Type())
h3cPortalStatAuthDisordered.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPortalStatAuthDisordered.setStatus(_A)
_H3cPortalStatAuthUnknownError_Type=Counter64
_H3cPortalStatAuthUnknownError_Object=MibScalar
h3cPortalStatAuthUnknownError=_H3cPortalStatAuthUnknownError_Object((1,3,6,1,4,1,2011,10,2,99,4,12),_H3cPortalStatAuthUnknownError_Type())
h3cPortalStatAuthUnknownError.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPortalStatAuthUnknownError.setStatus(_A)
_H3cPortalStatAuthResp_Type=Counter64
_H3cPortalStatAuthResp_Object=MibScalar
h3cPortalStatAuthResp=_H3cPortalStatAuthResp_Object((1,3,6,1,4,1,2011,10,2,99,4,13),_H3cPortalStatAuthResp_Type())
h3cPortalStatAuthResp.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPortalStatAuthResp.setStatus(_A)
_H3cPortalStatChallengeReq_Type=Counter64
_H3cPortalStatChallengeReq_Object=MibScalar
h3cPortalStatChallengeReq=_H3cPortalStatChallengeReq_Object((1,3,6,1,4,1,2011,10,2,99,4,14),_H3cPortalStatChallengeReq_Type())
h3cPortalStatChallengeReq.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPortalStatChallengeReq.setStatus(_A)
_H3cPortalStatChallengeResp_Type=Counter64
_H3cPortalStatChallengeResp_Object=MibScalar
h3cPortalStatChallengeResp=_H3cPortalStatChallengeResp_Object((1,3,6,1,4,1,2011,10,2,99,4,15),_H3cPortalStatChallengeResp_Type())
h3cPortalStatChallengeResp.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPortalStatChallengeResp.setStatus(_A)
_H3cPortalStatHttpReq_Type=Counter64
_H3cPortalStatHttpReq_Object=MibScalar
h3cPortalStatHttpReq=_H3cPortalStatHttpReq_Object((1,3,6,1,4,1,2011,10,2,99,4,16),_H3cPortalStatHttpReq_Type())
h3cPortalStatHttpReq.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPortalStatHttpReq.setStatus(_A)
_H3cPortalStatHttpResp_Type=Counter64
_H3cPortalStatHttpResp_Object=MibScalar
h3cPortalStatHttpResp=_H3cPortalStatHttpResp_Object((1,3,6,1,4,1,2011,10,2,99,4,17),_H3cPortalStatHttpResp_Type())
h3cPortalStatHttpResp.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPortalStatHttpResp.setStatus(_A)
_H3cPortalStatHttpsReq_Type=Counter64
_H3cPortalStatHttpsReq_Object=MibScalar
h3cPortalStatHttpsReq=_H3cPortalStatHttpsReq_Object((1,3,6,1,4,1,2011,10,2,99,4,18),_H3cPortalStatHttpsReq_Type())
h3cPortalStatHttpsReq.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPortalStatHttpsReq.setStatus(_A)
_H3cPortalStatHttpsResp_Type=Counter64
_H3cPortalStatHttpsResp_Object=MibScalar
h3cPortalStatHttpsResp=_H3cPortalStatHttpsResp_Object((1,3,6,1,4,1,2011,10,2,99,4,19),_H3cPortalStatHttpsResp_Type())
h3cPortalStatHttpsResp.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPortalStatHttpsResp.setStatus(_A)
_H3cPortalPktStatistic_ObjectIdentity=ObjectIdentity
h3cPortalPktStatistic=_H3cPortalPktStatistic_ObjectIdentity((1,3,6,1,4,1,2011,10,2,99,5))
_H3cPortalPktStaReqAuthNum_Type=Counter64
_H3cPortalPktStaReqAuthNum_Object=MibScalar
h3cPortalPktStaReqAuthNum=_H3cPortalPktStaReqAuthNum_Object((1,3,6,1,4,1,2011,10,2,99,5,1),_H3cPortalPktStaReqAuthNum_Type())
h3cPortalPktStaReqAuthNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPortalPktStaReqAuthNum.setStatus(_A)
_H3cPortalPktStaAckAuthSuccess_Type=Counter64
_H3cPortalPktStaAckAuthSuccess_Object=MibScalar
h3cPortalPktStaAckAuthSuccess=_H3cPortalPktStaAckAuthSuccess_Object((1,3,6,1,4,1,2011,10,2,99,5,2),_H3cPortalPktStaAckAuthSuccess_Type())
h3cPortalPktStaAckAuthSuccess.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPortalPktStaAckAuthSuccess.setStatus(_A)
_H3cPortalPktStaAckAuthReject_Type=Counter64
_H3cPortalPktStaAckAuthReject_Object=MibScalar
h3cPortalPktStaAckAuthReject=_H3cPortalPktStaAckAuthReject_Object((1,3,6,1,4,1,2011,10,2,99,5,3),_H3cPortalPktStaAckAuthReject_Type())
h3cPortalPktStaAckAuthReject.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPortalPktStaAckAuthReject.setStatus(_A)
_H3cPortalPktStaAckAuthEstablish_Type=Counter64
_H3cPortalPktStaAckAuthEstablish_Object=MibScalar
h3cPortalPktStaAckAuthEstablish=_H3cPortalPktStaAckAuthEstablish_Object((1,3,6,1,4,1,2011,10,2,99,5,4),_H3cPortalPktStaAckAuthEstablish_Type())
h3cPortalPktStaAckAuthEstablish.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPortalPktStaAckAuthEstablish.setStatus(_A)
_H3cPortalPktStaAckAuthBusy_Type=Counter64
_H3cPortalPktStaAckAuthBusy_Object=MibScalar
h3cPortalPktStaAckAuthBusy=_H3cPortalPktStaAckAuthBusy_Object((1,3,6,1,4,1,2011,10,2,99,5,5),_H3cPortalPktStaAckAuthBusy_Type())
h3cPortalPktStaAckAuthBusy.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPortalPktStaAckAuthBusy.setStatus(_A)
_H3cPortalPktStaAckAuthAuthFail_Type=Counter64
_H3cPortalPktStaAckAuthAuthFail_Object=MibScalar
h3cPortalPktStaAckAuthAuthFail=_H3cPortalPktStaAckAuthAuthFail_Object((1,3,6,1,4,1,2011,10,2,99,5,6),_H3cPortalPktStaAckAuthAuthFail_Type())
h3cPortalPktStaAckAuthAuthFail.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPortalPktStaAckAuthAuthFail.setStatus(_A)
_H3cPortalPktStaReqChallengeNum_Type=Counter64
_H3cPortalPktStaReqChallengeNum_Object=MibScalar
h3cPortalPktStaReqChallengeNum=_H3cPortalPktStaReqChallengeNum_Object((1,3,6,1,4,1,2011,10,2,99,5,7),_H3cPortalPktStaReqChallengeNum_Type())
h3cPortalPktStaReqChallengeNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPortalPktStaReqChallengeNum.setStatus(_A)
_H3cPortalPktStaAckChallengeSuccess_Type=Counter64
_H3cPortalPktStaAckChallengeSuccess_Object=MibScalar
h3cPortalPktStaAckChallengeSuccess=_H3cPortalPktStaAckChallengeSuccess_Object((1,3,6,1,4,1,2011,10,2,99,5,8),_H3cPortalPktStaAckChallengeSuccess_Type())
h3cPortalPktStaAckChallengeSuccess.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPortalPktStaAckChallengeSuccess.setStatus(_A)
_H3cPortalPktStaAckChallengeReject_Type=Counter64
_H3cPortalPktStaAckChallengeReject_Object=MibScalar
h3cPortalPktStaAckChallengeReject=_H3cPortalPktStaAckChallengeReject_Object((1,3,6,1,4,1,2011,10,2,99,5,9),_H3cPortalPktStaAckChallengeReject_Type())
h3cPortalPktStaAckChallengeReject.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPortalPktStaAckChallengeReject.setStatus(_A)
_H3cPortalPktStaAckChallengeEstablish_Type=Counter64
_H3cPortalPktStaAckChallengeEstablish_Object=MibScalar
h3cPortalPktStaAckChallengeEstablish=_H3cPortalPktStaAckChallengeEstablish_Object((1,3,6,1,4,1,2011,10,2,99,5,10),_H3cPortalPktStaAckChallengeEstablish_Type())
h3cPortalPktStaAckChallengeEstablish.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPortalPktStaAckChallengeEstablish.setStatus(_A)
_H3cPortalPktStaAckChallengeBusy_Type=Counter64
_H3cPortalPktStaAckChallengeBusy_Object=MibScalar
h3cPortalPktStaAckChallengeBusy=_H3cPortalPktStaAckChallengeBusy_Object((1,3,6,1,4,1,2011,10,2,99,5,11),_H3cPortalPktStaAckChallengeBusy_Type())
h3cPortalPktStaAckChallengeBusy.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPortalPktStaAckChallengeBusy.setStatus(_A)
_H3cPortalPktStaAckChallengeAuthFail_Type=Counter64
_H3cPortalPktStaAckChallengeAuthFail_Object=MibScalar
h3cPortalPktStaAckChallengeAuthFail=_H3cPortalPktStaAckChallengeAuthFail_Object((1,3,6,1,4,1,2011,10,2,99,5,12),_H3cPortalPktStaAckChallengeAuthFail_Type())
h3cPortalPktStaAckChallengeAuthFail.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPortalPktStaAckChallengeAuthFail.setStatus(_A)
_H3cPortalExtConfig_ObjectIdentity=ObjectIdentity
h3cPortalExtConfig=_H3cPortalExtConfig_ObjectIdentity((1,3,6,1,4,1,2011,10,2,99,6))
_H3cPortalExtMaxUserNumber_Type=Unsigned32
_H3cPortalExtMaxUserNumber_Object=MibScalar
h3cPortalExtMaxUserNumber=_H3cPortalExtMaxUserNumber_Object((1,3,6,1,4,1,2011,10,2,99,6,1),_H3cPortalExtMaxUserNumber_Type())
h3cPortalExtMaxUserNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPortalExtMaxUserNumber.setStatus(_A)
_H3cPortalExtCurrentUserNumber_Type=Unsigned32
_H3cPortalExtCurrentUserNumber_Object=MibScalar
h3cPortalExtCurrentUserNumber=_H3cPortalExtCurrentUserNumber_Object((1,3,6,1,4,1,2011,10,2,99,6,2),_H3cPortalExtCurrentUserNumber_Type())
h3cPortalExtCurrentUserNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPortalExtCurrentUserNumber.setStatus(_A)
class _H3cPortalExtStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_S,2)))
_H3cPortalExtStatus_Type.__name__=_F
_H3cPortalExtStatus_Object=MibScalar
h3cPortalExtStatus=_H3cPortalExtStatus_Object((1,3,6,1,4,1,2011,10,2,99,6,3),_H3cPortalExtStatus_Type())
h3cPortalExtStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPortalExtStatus.setStatus(_A)
_H3cPortalExtTables_ObjectIdentity=ObjectIdentity
h3cPortalExtTables=_H3cPortalExtTables_ObjectIdentity((1,3,6,1,4,1,2011,10,2,99,7))
_H3cPortalExtSrvTable_Object=MibTable
h3cPortalExtSrvTable=_H3cPortalExtSrvTable_Object((1,3,6,1,4,1,2011,10,2,99,7,1))
if mibBuilder.loadTexts:h3cPortalExtSrvTable.setStatus(_A)
_H3cPortalExtSrvEntry_Object=MibTableRow
h3cPortalExtSrvEntry=_H3cPortalExtSrvEntry_Object((1,3,6,1,4,1,2011,10,2,99,7,1,1))
h3cPortalExtSrvEntry.setIndexNames((0,_D,_c))
if mibBuilder.loadTexts:h3cPortalExtSrvEntry.setStatus(_A)
class _H3cPortalExtSrvName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_H3cPortalExtSrvName_Type.__name__=_H
_H3cPortalExtSrvName_Object=MibTableColumn
h3cPortalExtSrvName=_H3cPortalExtSrvName_Object((1,3,6,1,4,1,2011,10,2,99,7,1,1,1),_H3cPortalExtSrvName_Type())
h3cPortalExtSrvName.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cPortalExtSrvName.setStatus(_A)
_H3cPortalExtSrvIPAddrType_Type=InetAddressType
_H3cPortalExtSrvIPAddrType_Object=MibTableColumn
h3cPortalExtSrvIPAddrType=_H3cPortalExtSrvIPAddrType_Object((1,3,6,1,4,1,2011,10,2,99,7,1,1,2),_H3cPortalExtSrvIPAddrType_Type())
h3cPortalExtSrvIPAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPortalExtSrvIPAddrType.setStatus(_A)
_H3cPortalExtSrvIP_Type=InetAddress
_H3cPortalExtSrvIP_Object=MibTableColumn
h3cPortalExtSrvIP=_H3cPortalExtSrvIP_Object((1,3,6,1,4,1,2011,10,2,99,7,1,1,3),_H3cPortalExtSrvIP_Type())
h3cPortalExtSrvIP.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPortalExtSrvIP.setStatus(_A)
_H3cPortalExtSrvPort_Type=Integer32
_H3cPortalExtSrvPort_Object=MibTableColumn
h3cPortalExtSrvPort=_H3cPortalExtSrvPort_Object((1,3,6,1,4,1,2011,10,2,99,7,1,1,4),_H3cPortalExtSrvPort_Type())
h3cPortalExtSrvPort.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPortalExtSrvPort.setStatus(_A)
_H3cPortalExtSrvRowStatus_Type=RowStatus
_H3cPortalExtSrvRowStatus_Object=MibTableColumn
h3cPortalExtSrvRowStatus=_H3cPortalExtSrvRowStatus_Object((1,3,6,1,4,1,2011,10,2,99,7,1,1,5),_H3cPortalExtSrvRowStatus_Type())
h3cPortalExtSrvRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPortalExtSrvRowStatus.setStatus(_A)
_H3cPortalExtWebSrvTable_Object=MibTable
h3cPortalExtWebSrvTable=_H3cPortalExtWebSrvTable_Object((1,3,6,1,4,1,2011,10,2,99,7,2))
if mibBuilder.loadTexts:h3cPortalExtWebSrvTable.setStatus(_A)
_H3cPortalExtWebSrvEntry_Object=MibTableRow
h3cPortalExtWebSrvEntry=_H3cPortalExtWebSrvEntry_Object((1,3,6,1,4,1,2011,10,2,99,7,2,1))
h3cPortalExtWebSrvEntry.setIndexNames((0,_D,_d))
if mibBuilder.loadTexts:h3cPortalExtWebSrvEntry.setStatus(_A)
class _H3cPortalExtWebSrvName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_H3cPortalExtWebSrvName_Type.__name__=_H
_H3cPortalExtWebSrvName_Object=MibTableColumn
h3cPortalExtWebSrvName=_H3cPortalExtWebSrvName_Object((1,3,6,1,4,1,2011,10,2,99,7,2,1,1),_H3cPortalExtWebSrvName_Type())
h3cPortalExtWebSrvName.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cPortalExtWebSrvName.setStatus(_A)
_H3cPortalExtWebSrvUrl_Type=OctetString
_H3cPortalExtWebSrvUrl_Object=MibTableColumn
h3cPortalExtWebSrvUrl=_H3cPortalExtWebSrvUrl_Object((1,3,6,1,4,1,2011,10,2,99,7,2,1,2),_H3cPortalExtWebSrvUrl_Type())
h3cPortalExtWebSrvUrl.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPortalExtWebSrvUrl.setStatus(_A)
_H3cPortalExtWebSrvRowStatus_Type=RowStatus
_H3cPortalExtWebSrvRowStatus_Object=MibTableColumn
h3cPortalExtWebSrvRowStatus=_H3cPortalExtWebSrvRowStatus_Object((1,3,6,1,4,1,2011,10,2,99,7,2,1,3),_H3cPortalExtWebSrvRowStatus_Type())
h3cPortalExtWebSrvRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPortalExtWebSrvRowStatus.setStatus(_A)
_H3cPortalExtMTSrvTable_Object=MibTable
h3cPortalExtMTSrvTable=_H3cPortalExtMTSrvTable_Object((1,3,6,1,4,1,2011,10,2,99,7,3))
if mibBuilder.loadTexts:h3cPortalExtMTSrvTable.setStatus(_A)
_H3cPortalExtMTSrvEntry_Object=MibTableRow
h3cPortalExtMTSrvEntry=_H3cPortalExtMTSrvEntry_Object((1,3,6,1,4,1,2011,10,2,99,7,3,1))
h3cPortalExtMTSrvEntry.setIndexNames((0,_D,_e))
if mibBuilder.loadTexts:h3cPortalExtMTSrvEntry.setStatus(_A)
class _H3cPortalExtMTSrvName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_H3cPortalExtMTSrvName_Type.__name__=_H
_H3cPortalExtMTSrvName_Object=MibTableColumn
h3cPortalExtMTSrvName=_H3cPortalExtMTSrvName_Object((1,3,6,1,4,1,2011,10,2,99,7,3,1,1),_H3cPortalExtMTSrvName_Type())
h3cPortalExtMTSrvName.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cPortalExtMTSrvName.setStatus(_A)
_H3cPortalExtMTSrvIPAddrType_Type=InetAddressType
_H3cPortalExtMTSrvIPAddrType_Object=MibTableColumn
h3cPortalExtMTSrvIPAddrType=_H3cPortalExtMTSrvIPAddrType_Object((1,3,6,1,4,1,2011,10,2,99,7,3,1,2),_H3cPortalExtMTSrvIPAddrType_Type())
h3cPortalExtMTSrvIPAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPortalExtMTSrvIPAddrType.setStatus(_A)
_H3cPortalExtMTSrvIP_Type=InetAddress
_H3cPortalExtMTSrvIP_Object=MibTableColumn
h3cPortalExtMTSrvIP=_H3cPortalExtMTSrvIP_Object((1,3,6,1,4,1,2011,10,2,99,7,3,1,3),_H3cPortalExtMTSrvIP_Type())
h3cPortalExtMTSrvIP.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPortalExtMTSrvIP.setStatus(_A)
class _H3cPortalExtMTSrvPort_Type(Integer32):defaultValue=50100
_H3cPortalExtMTSrvPort_Type.__name__=_F
_H3cPortalExtMTSrvPort_Object=MibTableColumn
h3cPortalExtMTSrvPort=_H3cPortalExtMTSrvPort_Object((1,3,6,1,4,1,2011,10,2,99,7,3,1,4),_H3cPortalExtMTSrvPort_Type())
h3cPortalExtMTSrvPort.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPortalExtMTSrvPort.setStatus(_A)
class _H3cPortalExtMTDetctFlowPeriod_Type(Integer32):defaultValue=300
_H3cPortalExtMTDetctFlowPeriod_Type.__name__=_F
_H3cPortalExtMTDetctFlowPeriod_Object=MibTableColumn
h3cPortalExtMTDetctFlowPeriod=_H3cPortalExtMTDetctFlowPeriod_Object((1,3,6,1,4,1,2011,10,2,99,7,3,1,5),_H3cPortalExtMTDetctFlowPeriod_Type())
h3cPortalExtMTDetctFlowPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPortalExtMTDetctFlowPeriod.setStatus(_A)
if mibBuilder.loadTexts:h3cPortalExtMTDetctFlowPeriod.setUnits(_Z)
class _H3cPortalExtMTThresholdFlow_Type(Unsigned32):defaultValue=0
_H3cPortalExtMTThresholdFlow_Type.__name__=_J
_H3cPortalExtMTThresholdFlow_Object=MibTableColumn
h3cPortalExtMTThresholdFlow=_H3cPortalExtMTThresholdFlow_Object((1,3,6,1,4,1,2011,10,2,99,7,3,1,6),_H3cPortalExtMTThresholdFlow_Type())
h3cPortalExtMTThresholdFlow.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPortalExtMTThresholdFlow.setStatus(_A)
if mibBuilder.loadTexts:h3cPortalExtMTThresholdFlow.setUnits('bytes')
_H3cPortalExtMTSrvRowStatus_Type=RowStatus
_H3cPortalExtMTSrvRowStatus_Object=MibTableColumn
h3cPortalExtMTSrvRowStatus=_H3cPortalExtMTSrvRowStatus_Object((1,3,6,1,4,1,2011,10,2,99,7,3,1,7),_H3cPortalExtMTSrvRowStatus_Type())
h3cPortalExtMTSrvRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPortalExtMTSrvRowStatus.setStatus(_A)
_H3cPortalExtIfConfigTable_Object=MibTable
h3cPortalExtIfConfigTable=_H3cPortalExtIfConfigTable_Object((1,3,6,1,4,1,2011,10,2,99,7,4))
if mibBuilder.loadTexts:h3cPortalExtIfConfigTable.setStatus(_A)
_H3cPortalExtIfConfigEntry_Object=MibTableRow
h3cPortalExtIfConfigEntry=_H3cPortalExtIfConfigEntry_Object((1,3,6,1,4,1,2011,10,2,99,7,4,1))
h3cPortalExtIfConfigEntry.setIndexNames((0,_D,_f))
if mibBuilder.loadTexts:h3cPortalExtIfConfigEntry.setStatus(_A)
_H3cPortalExtIfIndex_Type=InterfaceIndex
_H3cPortalExtIfIndex_Object=MibTableColumn
h3cPortalExtIfIndex=_H3cPortalExtIfIndex_Object((1,3,6,1,4,1,2011,10,2,99,7,4,1,1),_H3cPortalExtIfIndex_Type())
h3cPortalExtIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cPortalExtIfIndex.setStatus(_A)
_H3cPortalExtIfWebSrvName_Type=OctetString
_H3cPortalExtIfWebSrvName_Object=MibTableColumn
h3cPortalExtIfWebSrvName=_H3cPortalExtIfWebSrvName_Object((1,3,6,1,4,1,2011,10,2,99,7,4,1,2),_H3cPortalExtIfWebSrvName_Type())
h3cPortalExtIfWebSrvName.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPortalExtIfWebSrvName.setStatus(_A)
_H3cPortalExtIfDomainName_Type=OctetString
_H3cPortalExtIfDomainName_Object=MibTableColumn
h3cPortalExtIfDomainName=_H3cPortalExtIfDomainName_Object((1,3,6,1,4,1,2011,10,2,99,7,4,1,3),_H3cPortalExtIfDomainName_Type())
h3cPortalExtIfDomainName.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPortalExtIfDomainName.setStatus(_A)
_H3cPortalExtIfAuthMethod_Type=H3cPortalAuthMethod
_H3cPortalExtIfAuthMethod_Object=MibTableColumn
h3cPortalExtIfAuthMethod=_H3cPortalExtIfAuthMethod_Object((1,3,6,1,4,1,2011,10,2,99,7,4,1,4),_H3cPortalExtIfAuthMethod_Type())
h3cPortalExtIfAuthMethod.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPortalExtIfAuthMethod.setStatus(_A)
_H3cPortalExtIfMTSrvName_Type=OctetString
_H3cPortalExtIfMTSrvName_Object=MibTableColumn
h3cPortalExtIfMTSrvName=_H3cPortalExtIfMTSrvName_Object((1,3,6,1,4,1,2011,10,2,99,7,4,1,5),_H3cPortalExtIfMTSrvName_Type())
h3cPortalExtIfMTSrvName.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPortalExtIfMTSrvName.setStatus(_A)
_H3cPortalExtIfMaxUser_Type=Unsigned32
_H3cPortalExtIfMaxUser_Object=MibTableColumn
h3cPortalExtIfMaxUser=_H3cPortalExtIfMaxUser_Object((1,3,6,1,4,1,2011,10,2,99,7,4,1,6),_H3cPortalExtIfMaxUser_Type())
h3cPortalExtIfMaxUser.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPortalExtIfMaxUser.setStatus(_A)
_H3cPortalExtIfIpv6ConfigTable_Object=MibTable
h3cPortalExtIfIpv6ConfigTable=_H3cPortalExtIfIpv6ConfigTable_Object((1,3,6,1,4,1,2011,10,2,99,7,5))
if mibBuilder.loadTexts:h3cPortalExtIfIpv6ConfigTable.setStatus(_A)
_H3cPortalExtIfIpv6ConfigEntry_Object=MibTableRow
h3cPortalExtIfIpv6ConfigEntry=_H3cPortalExtIfIpv6ConfigEntry_Object((1,3,6,1,4,1,2011,10,2,99,7,5,1))
h3cPortalExtIfIpv6ConfigEntry.setIndexNames((0,_D,_g))
if mibBuilder.loadTexts:h3cPortalExtIfIpv6ConfigEntry.setStatus(_A)
_H3cPortalExtIfIpv6Index_Type=InterfaceIndex
_H3cPortalExtIfIpv6Index_Object=MibTableColumn
h3cPortalExtIfIpv6Index=_H3cPortalExtIfIpv6Index_Object((1,3,6,1,4,1,2011,10,2,99,7,5,1,1),_H3cPortalExtIfIpv6Index_Type())
h3cPortalExtIfIpv6Index.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cPortalExtIfIpv6Index.setStatus(_A)
_H3cPortalExtIfIpv6WebSrvName_Type=OctetString
_H3cPortalExtIfIpv6WebSrvName_Object=MibTableColumn
h3cPortalExtIfIpv6WebSrvName=_H3cPortalExtIfIpv6WebSrvName_Object((1,3,6,1,4,1,2011,10,2,99,7,5,1,2),_H3cPortalExtIfIpv6WebSrvName_Type())
h3cPortalExtIfIpv6WebSrvName.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPortalExtIfIpv6WebSrvName.setStatus(_A)
_H3cPortalExtIfIpv6DomainName_Type=OctetString
_H3cPortalExtIfIpv6DomainName_Object=MibTableColumn
h3cPortalExtIfIpv6DomainName=_H3cPortalExtIfIpv6DomainName_Object((1,3,6,1,4,1,2011,10,2,99,7,5,1,3),_H3cPortalExtIfIpv6DomainName_Type())
h3cPortalExtIfIpv6DomainName.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPortalExtIfIpv6DomainName.setStatus(_A)
_H3cPortalExtIfIpv6AuthMethod_Type=H3cPortalAuthMethod
_H3cPortalExtIfIpv6AuthMethod_Object=MibTableColumn
h3cPortalExtIfIpv6AuthMethod=_H3cPortalExtIfIpv6AuthMethod_Object((1,3,6,1,4,1,2011,10,2,99,7,5,1,4),_H3cPortalExtIfIpv6AuthMethod_Type())
h3cPortalExtIfIpv6AuthMethod.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPortalExtIfIpv6AuthMethod.setStatus(_A)
_H3cPortalExtIfIpv6MaxUser_Type=Unsigned32
_H3cPortalExtIfIpv6MaxUser_Object=MibTableColumn
h3cPortalExtIfIpv6MaxUser=_H3cPortalExtIfIpv6MaxUser_Object((1,3,6,1,4,1,2011,10,2,99,7,5,1,5),_H3cPortalExtIfIpv6MaxUser_Type())
h3cPortalExtIfIpv6MaxUser.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPortalExtIfIpv6MaxUser.setStatus(_A)
_H3cPortalDot11SrvTable_Object=MibTable
h3cPortalDot11SrvTable=_H3cPortalDot11SrvTable_Object((1,3,6,1,4,1,2011,10,2,99,7,6))
if mibBuilder.loadTexts:h3cPortalDot11SrvTable.setStatus(_A)
_H3cPortalDot11SrvEntry_Object=MibTableRow
h3cPortalDot11SrvEntry=_H3cPortalDot11SrvEntry_Object((1,3,6,1,4,1,2011,10,2,99,7,6,1))
h3cPortalDot11SrvEntry.setIndexNames((0,_D,_h))
if mibBuilder.loadTexts:h3cPortalDot11SrvEntry.setStatus(_A)
class _H3cPortalDot11SrvTemName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,63))
_H3cPortalDot11SrvTemName_Type.__name__=_H
_H3cPortalDot11SrvTemName_Object=MibTableColumn
h3cPortalDot11SrvTemName=_H3cPortalDot11SrvTemName_Object((1,3,6,1,4,1,2011,10,2,99,7,6,1,1),_H3cPortalDot11SrvTemName_Type())
h3cPortalDot11SrvTemName.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cPortalDot11SrvTemName.setStatus(_A)
_H3cPortalDot11WebSrvName_Type=OctetString
_H3cPortalDot11WebSrvName_Object=MibTableColumn
h3cPortalDot11WebSrvName=_H3cPortalDot11WebSrvName_Object((1,3,6,1,4,1,2011,10,2,99,7,6,1,2),_H3cPortalDot11WebSrvName_Type())
h3cPortalDot11WebSrvName.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPortalDot11WebSrvName.setStatus(_A)
_H3cPortalDot11DomainName_Type=OctetString
_H3cPortalDot11DomainName_Object=MibTableColumn
h3cPortalDot11DomainName=_H3cPortalDot11DomainName_Object((1,3,6,1,4,1,2011,10,2,99,7,6,1,3),_H3cPortalDot11DomainName_Type())
h3cPortalDot11DomainName.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPortalDot11DomainName.setStatus(_A)
_H3cPortalDot11AuthMethod_Type=H3cPortalAuthMethod
_H3cPortalDot11AuthMethod_Object=MibTableColumn
h3cPortalDot11AuthMethod=_H3cPortalDot11AuthMethod_Object((1,3,6,1,4,1,2011,10,2,99,7,6,1,4),_H3cPortalDot11AuthMethod_Type())
h3cPortalDot11AuthMethod.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPortalDot11AuthMethod.setStatus(_A)
_H3cPortalDot11MTSrvName_Type=OctetString
_H3cPortalDot11MTSrvName_Object=MibTableColumn
h3cPortalDot11MTSrvName=_H3cPortalDot11MTSrvName_Object((1,3,6,1,4,1,2011,10,2,99,7,6,1,5),_H3cPortalDot11MTSrvName_Type())
h3cPortalDot11MTSrvName.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPortalDot11MTSrvName.setStatus(_A)
_H3cPortalDot11MaxUser_Type=Unsigned32
_H3cPortalDot11MaxUser_Object=MibTableColumn
h3cPortalDot11MaxUser=_H3cPortalDot11MaxUser_Object((1,3,6,1,4,1,2011,10,2,99,7,6,1,6),_H3cPortalDot11MaxUser_Type())
h3cPortalDot11MaxUser.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPortalDot11MaxUser.setStatus(_A)
_H3cPortalDot11Ipv6SrvTable_Object=MibTable
h3cPortalDot11Ipv6SrvTable=_H3cPortalDot11Ipv6SrvTable_Object((1,3,6,1,4,1,2011,10,2,99,7,7))
if mibBuilder.loadTexts:h3cPortalDot11Ipv6SrvTable.setStatus(_A)
_H3cPortalDot11Ipv6SrvEntry_Object=MibTableRow
h3cPortalDot11Ipv6SrvEntry=_H3cPortalDot11Ipv6SrvEntry_Object((1,3,6,1,4,1,2011,10,2,99,7,7,1))
h3cPortalDot11Ipv6SrvEntry.setIndexNames((0,_D,_i))
if mibBuilder.loadTexts:h3cPortalDot11Ipv6SrvEntry.setStatus(_A)
class _H3cPortalDot11Ipv6SrvTemName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,63))
_H3cPortalDot11Ipv6SrvTemName_Type.__name__=_H
_H3cPortalDot11Ipv6SrvTemName_Object=MibTableColumn
h3cPortalDot11Ipv6SrvTemName=_H3cPortalDot11Ipv6SrvTemName_Object((1,3,6,1,4,1,2011,10,2,99,7,7,1,1),_H3cPortalDot11Ipv6SrvTemName_Type())
h3cPortalDot11Ipv6SrvTemName.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cPortalDot11Ipv6SrvTemName.setStatus(_A)
_H3cPortalDot11Ipv6WebSrvName_Type=OctetString
_H3cPortalDot11Ipv6WebSrvName_Object=MibTableColumn
h3cPortalDot11Ipv6WebSrvName=_H3cPortalDot11Ipv6WebSrvName_Object((1,3,6,1,4,1,2011,10,2,99,7,7,1,2),_H3cPortalDot11Ipv6WebSrvName_Type())
h3cPortalDot11Ipv6WebSrvName.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPortalDot11Ipv6WebSrvName.setStatus(_A)
_H3cPortalDot11Ipv6DomainName_Type=OctetString
_H3cPortalDot11Ipv6DomainName_Object=MibTableColumn
h3cPortalDot11Ipv6DomainName=_H3cPortalDot11Ipv6DomainName_Object((1,3,6,1,4,1,2011,10,2,99,7,7,1,3),_H3cPortalDot11Ipv6DomainName_Type())
h3cPortalDot11Ipv6DomainName.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPortalDot11Ipv6DomainName.setStatus(_A)
_H3cPortalDot11Ipv6AuthMethod_Type=H3cPortalAuthMethod
_H3cPortalDot11Ipv6AuthMethod_Object=MibTableColumn
h3cPortalDot11Ipv6AuthMethod=_H3cPortalDot11Ipv6AuthMethod_Object((1,3,6,1,4,1,2011,10,2,99,7,7,1,4),_H3cPortalDot11Ipv6AuthMethod_Type())
h3cPortalDot11Ipv6AuthMethod.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPortalDot11Ipv6AuthMethod.setStatus(_A)
_H3cPortalDot11Ipv6MaxUser_Type=Unsigned32
_H3cPortalDot11Ipv6MaxUser_Object=MibTableColumn
h3cPortalDot11Ipv6MaxUser=_H3cPortalDot11Ipv6MaxUser_Object((1,3,6,1,4,1,2011,10,2,99,7,7,1,5),_H3cPortalDot11Ipv6MaxUser_Type())
h3cPortalDot11Ipv6MaxUser.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPortalDot11Ipv6MaxUser.setStatus(_A)
h3cPortalServerLost=NotificationType((1,3,6,1,4,1,2011,10,2,99,3,0,1))
h3cPortalServerLost.setObjects(*((_D,_I),(_D,_M),(_D,_N),(_D,_O)))
if mibBuilder.loadTexts:h3cPortalServerLost.setStatus(_A)
h3cPortalServerGet=NotificationType((1,3,6,1,4,1,2011,10,2,99,3,0,2))
h3cPortalServerGet.setObjects(*((_D,_I),(_D,_M),(_D,_N),(_D,_O)))
if mibBuilder.loadTexts:h3cPortalServerGet.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'H3cPortalAuthMethod':H3cPortalAuthMethod,'h3cPortal':h3cPortal,'h3cPortalConfig':h3cPortalConfig,'h3cPortalMaxUserNumber':h3cPortalMaxUserNumber,'h3cPortalCurrentUserNumber':h3cPortalCurrentUserNumber,'h3cPortalStatus':h3cPortalStatus,'h3cPortalUserNumberUpperLimit':h3cPortalUserNumberUpperLimit,'h3cPortalNasId':h3cPortalNasId,'h3cPortalTables':h3cPortalTables,'h3cPortalServerTable':h3cPortalServerTable,'h3cPortalServerEntry':h3cPortalServerEntry,_I:h3cPortalServerName,'h3cPortalServerUrl':h3cPortalServerUrl,_O:h3cPortalServerPort,'h3cPortalIfInfoTable':h3cPortalIfInfoTable,'h3cPortalIfInfoEntry':h3cPortalIfInfoEntry,'h3cPortalAuthReqNumber':h3cPortalAuthReqNumber,'h3cPortalAuthSuccNumber':h3cPortalAuthSuccNumber,'h3cPortalAuthFailNumber':h3cPortalAuthFailNumber,'h3cPortalIfServerTable':h3cPortalIfServerTable,'h3cPortalIfServerEntry':h3cPortalIfServerEntry,_T:h3cPortalIfServerIndex,'h3cPortalIfServerUrl':h3cPortalIfServerUrl,'h3cPortalIfServerRowStatus':h3cPortalIfServerRowStatus,'h3cPortalIfVlanNasIDTable':h3cPortalIfVlanNasIDTable,'h3cPortalIfVlanNasIDEntry':h3cPortalIfVlanNasIDEntry,_U:h3cPortalIfVlanNasIDIfIndex,_V:h3cPortalIfVlanNasIDVlanID,'h3cPortalIfVlanNasIDNasID':h3cPortalIfVlanNasIDNasID,'h3cPortalSSIDFreeRuleTable':h3cPortalSSIDFreeRuleTable,'h3cPortalSSIDFreeRuleEntry':h3cPortalSSIDFreeRuleEntry,_W:h3cPortalSSIDFreeRuleIndex,'h3cPortalSSIDFreeRuleSrcSSID':h3cPortalSSIDFreeRuleSrcSSID,'h3cPortalSSIDFreeRuleRowStatus':h3cPortalSSIDFreeRuleRowStatus,'h3cPortalSSIDFreeRuleSrcSpot':h3cPortalSSIDFreeRuleSrcSpot,'h3cPortalMacTriggerSrvTable':h3cPortalMacTriggerSrvTable,'h3cPortalMacTriggerSrvEntry':h3cPortalMacTriggerSrvEntry,_X:h3cPortalMacTriggerSrvIndex,'h3cPortalMacTriggerSrvIPAddrType':h3cPortalMacTriggerSrvIPAddrType,'h3cPortalMacTriggerSrvIP':h3cPortalMacTriggerSrvIP,'h3cPortalMacTriggerSrvPort':h3cPortalMacTriggerSrvPort,'h3cPortalMacTriggerSrvRowStatus':h3cPortalMacTriggerSrvRowStatus,'h3cPortalMacTriggerOnIfTable':h3cPortalMacTriggerOnIfTable,'h3cPortalMacTriggerOnIfEntry':h3cPortalMacTriggerOnIfEntry,_Y:h3cPortalMacTriggerOnIfIfIndex,'h3cPortalMacTriggerOnIfDetctFlowPeriod':h3cPortalMacTriggerOnIfDetctFlowPeriod,'h3cPortalMacTriggerOnIfThresholdFlow':h3cPortalMacTriggerOnIfThresholdFlow,'h3cPortalMacTriggerOnIfRowStatus':h3cPortalMacTriggerOnIfRowStatus,'h3cPortalFreeRuleTable':h3cPortalFreeRuleTable,'h3cPortalFreeRuleEntry':h3cPortalFreeRuleEntry,_a:h3cPortalFreeRuleIndex,'h3cPortalFreeRuleSrcIfIndex':h3cPortalFreeRuleSrcIfIndex,'h3cPortalFreeRuleSrcVlanID':h3cPortalFreeRuleSrcVlanID,'h3cPortalFreeRuleSrcMac':h3cPortalFreeRuleSrcMac,'h3cPortalFreeRuleAddrType':h3cPortalFreeRuleAddrType,'h3cPortalFreeRuleSrcAddr':h3cPortalFreeRuleSrcAddr,'h3cPortalFreeRuleSrcPrefix':h3cPortalFreeRuleSrcPrefix,'h3cPortalFreeRuleDstAddr':h3cPortalFreeRuleDstAddr,'h3cPortalFreeRuleDstPrefix':h3cPortalFreeRuleDstPrefix,'h3cPortalFreeRuleProtocol':h3cPortalFreeRuleProtocol,'h3cPortalFreeRuleSrcPort':h3cPortalFreeRuleSrcPort,'h3cPortalFreeRuleDstPort':h3cPortalFreeRuleDstPort,'h3cPortalFreeRuleRowStatus':h3cPortalFreeRuleRowStatus,'h3cPortalForbiddenRuleTable':h3cPortalForbiddenRuleTable,'h3cPortalForbiddenRuleEntry':h3cPortalForbiddenRuleEntry,_b:h3cPortalForbiddenRuleIndex,'h3cPortalForbiddenRuleSrcIfIndex':h3cPortalForbiddenRuleSrcIfIndex,'h3cPortalForbiddenRuleSrcVlanID':h3cPortalForbiddenRuleSrcVlanID,'h3cPortalForbiddenRuleSrcMac':h3cPortalForbiddenRuleSrcMac,'h3cPortalForbiddenRuleAddrType':h3cPortalForbiddenRuleAddrType,'h3cPortalForbiddenRuleSrcAddr':h3cPortalForbiddenRuleSrcAddr,'h3cPortalForbiddenRuleSrcPrefix':h3cPortalForbiddenRuleSrcPrefix,'h3cPortalForbiddenRuleDstAddr':h3cPortalForbiddenRuleDstAddr,'h3cPortalForbiddenRuleDstPrefix':h3cPortalForbiddenRuleDstPrefix,'h3cPortalForbiddenRuleProtocol':h3cPortalForbiddenRuleProtocol,'h3cPortalForbiddenRuleSrcPort':h3cPortalForbiddenRuleSrcPort,'h3cPortalForbiddenRuleDstPort':h3cPortalForbiddenRuleDstPort,'h3cPortalForbiddenRuleRowStatus':h3cPortalForbiddenRuleRowStatus,'h3cPortalForbiddenRuleSsidName':h3cPortalForbiddenRuleSsidName,'h3cPortalTraps':h3cPortalTraps,'h3cPortalTrapPrefix':h3cPortalTrapPrefix,'h3cPortalServerLost':h3cPortalServerLost,'h3cPortalServerGet':h3cPortalServerGet,'h3cPortalTrapVarObjects':h3cPortalTrapVarObjects,_M:h3cPortalFirstTrapTime,_N:h3cPortalServerIP,'h3cPortalStatistic':h3cPortalStatistic,'h3cPortalStatAuthReq':h3cPortalStatAuthReq,'h3cPortalStatAckLogout':h3cPortalStatAckLogout,'h3cPortalStatNotifyLogout':h3cPortalStatNotifyLogout,'h3cPortalStatChallengeTimeout':h3cPortalStatChallengeTimeout,'h3cPortalStatChallengeBusy':h3cPortalStatChallengeBusy,'h3cPortalStatChallengeFail':h3cPortalStatChallengeFail,'h3cPortalStatAuthTimeout':h3cPortalStatAuthTimeout,'h3cPortalStatAuthFail':h3cPortalStatAuthFail,'h3cPortalStatPwdError':h3cPortalStatPwdError,'h3cPortalStatAuthBusy':h3cPortalStatAuthBusy,'h3cPortalStatAuthDisordered':h3cPortalStatAuthDisordered,'h3cPortalStatAuthUnknownError':h3cPortalStatAuthUnknownError,'h3cPortalStatAuthResp':h3cPortalStatAuthResp,'h3cPortalStatChallengeReq':h3cPortalStatChallengeReq,'h3cPortalStatChallengeResp':h3cPortalStatChallengeResp,'h3cPortalStatHttpReq':h3cPortalStatHttpReq,'h3cPortalStatHttpResp':h3cPortalStatHttpResp,'h3cPortalStatHttpsReq':h3cPortalStatHttpsReq,'h3cPortalStatHttpsResp':h3cPortalStatHttpsResp,'h3cPortalPktStatistic':h3cPortalPktStatistic,'h3cPortalPktStaReqAuthNum':h3cPortalPktStaReqAuthNum,'h3cPortalPktStaAckAuthSuccess':h3cPortalPktStaAckAuthSuccess,'h3cPortalPktStaAckAuthReject':h3cPortalPktStaAckAuthReject,'h3cPortalPktStaAckAuthEstablish':h3cPortalPktStaAckAuthEstablish,'h3cPortalPktStaAckAuthBusy':h3cPortalPktStaAckAuthBusy,'h3cPortalPktStaAckAuthAuthFail':h3cPortalPktStaAckAuthAuthFail,'h3cPortalPktStaReqChallengeNum':h3cPortalPktStaReqChallengeNum,'h3cPortalPktStaAckChallengeSuccess':h3cPortalPktStaAckChallengeSuccess,'h3cPortalPktStaAckChallengeReject':h3cPortalPktStaAckChallengeReject,'h3cPortalPktStaAckChallengeEstablish':h3cPortalPktStaAckChallengeEstablish,'h3cPortalPktStaAckChallengeBusy':h3cPortalPktStaAckChallengeBusy,'h3cPortalPktStaAckChallengeAuthFail':h3cPortalPktStaAckChallengeAuthFail,'h3cPortalExtConfig':h3cPortalExtConfig,'h3cPortalExtMaxUserNumber':h3cPortalExtMaxUserNumber,'h3cPortalExtCurrentUserNumber':h3cPortalExtCurrentUserNumber,'h3cPortalExtStatus':h3cPortalExtStatus,'h3cPortalExtTables':h3cPortalExtTables,'h3cPortalExtSrvTable':h3cPortalExtSrvTable,'h3cPortalExtSrvEntry':h3cPortalExtSrvEntry,_c:h3cPortalExtSrvName,'h3cPortalExtSrvIPAddrType':h3cPortalExtSrvIPAddrType,'h3cPortalExtSrvIP':h3cPortalExtSrvIP,'h3cPortalExtSrvPort':h3cPortalExtSrvPort,'h3cPortalExtSrvRowStatus':h3cPortalExtSrvRowStatus,'h3cPortalExtWebSrvTable':h3cPortalExtWebSrvTable,'h3cPortalExtWebSrvEntry':h3cPortalExtWebSrvEntry,_d:h3cPortalExtWebSrvName,'h3cPortalExtWebSrvUrl':h3cPortalExtWebSrvUrl,'h3cPortalExtWebSrvRowStatus':h3cPortalExtWebSrvRowStatus,'h3cPortalExtMTSrvTable':h3cPortalExtMTSrvTable,'h3cPortalExtMTSrvEntry':h3cPortalExtMTSrvEntry,_e:h3cPortalExtMTSrvName,'h3cPortalExtMTSrvIPAddrType':h3cPortalExtMTSrvIPAddrType,'h3cPortalExtMTSrvIP':h3cPortalExtMTSrvIP,'h3cPortalExtMTSrvPort':h3cPortalExtMTSrvPort,'h3cPortalExtMTDetctFlowPeriod':h3cPortalExtMTDetctFlowPeriod,'h3cPortalExtMTThresholdFlow':h3cPortalExtMTThresholdFlow,'h3cPortalExtMTSrvRowStatus':h3cPortalExtMTSrvRowStatus,'h3cPortalExtIfConfigTable':h3cPortalExtIfConfigTable,'h3cPortalExtIfConfigEntry':h3cPortalExtIfConfigEntry,_f:h3cPortalExtIfIndex,'h3cPortalExtIfWebSrvName':h3cPortalExtIfWebSrvName,'h3cPortalExtIfDomainName':h3cPortalExtIfDomainName,'h3cPortalExtIfAuthMethod':h3cPortalExtIfAuthMethod,'h3cPortalExtIfMTSrvName':h3cPortalExtIfMTSrvName,'h3cPortalExtIfMaxUser':h3cPortalExtIfMaxUser,'h3cPortalExtIfIpv6ConfigTable':h3cPortalExtIfIpv6ConfigTable,'h3cPortalExtIfIpv6ConfigEntry':h3cPortalExtIfIpv6ConfigEntry,_g:h3cPortalExtIfIpv6Index,'h3cPortalExtIfIpv6WebSrvName':h3cPortalExtIfIpv6WebSrvName,'h3cPortalExtIfIpv6DomainName':h3cPortalExtIfIpv6DomainName,'h3cPortalExtIfIpv6AuthMethod':h3cPortalExtIfIpv6AuthMethod,'h3cPortalExtIfIpv6MaxUser':h3cPortalExtIfIpv6MaxUser,'h3cPortalDot11SrvTable':h3cPortalDot11SrvTable,'h3cPortalDot11SrvEntry':h3cPortalDot11SrvEntry,_h:h3cPortalDot11SrvTemName,'h3cPortalDot11WebSrvName':h3cPortalDot11WebSrvName,'h3cPortalDot11DomainName':h3cPortalDot11DomainName,'h3cPortalDot11AuthMethod':h3cPortalDot11AuthMethod,'h3cPortalDot11MTSrvName':h3cPortalDot11MTSrvName,'h3cPortalDot11MaxUser':h3cPortalDot11MaxUser,'h3cPortalDot11Ipv6SrvTable':h3cPortalDot11Ipv6SrvTable,'h3cPortalDot11Ipv6SrvEntry':h3cPortalDot11Ipv6SrvEntry,_i:h3cPortalDot11Ipv6SrvTemName,'h3cPortalDot11Ipv6WebSrvName':h3cPortalDot11Ipv6WebSrvName,'h3cPortalDot11Ipv6DomainName':h3cPortalDot11Ipv6DomainName,'h3cPortalDot11Ipv6AuthMethod':h3cPortalDot11Ipv6AuthMethod,'h3cPortalDot11Ipv6MaxUser':h3cPortalDot11Ipv6MaxUser})