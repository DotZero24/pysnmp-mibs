_o='h3cRprTrapIpAddress'
_n='h3cRprTrapTopoMacAddress'
_m='h3cRprTopoImageXEntry'
_l='h3cRprMacLearnRprMac'
_k='h3cRprMacLearnIfIndex'
_j='h3cRprRateLimitConfigServiceClass'
_i='h3cRprRateLimitConfigRingletId'
_h='h3cRprRateLimitConfigIfIndex'
_g='h3cRprPriorityValue'
_f='h3cRprPriority2ClassMapType'
_e='h3cRprPriority2ClassMapIfIndex'
_d='h3cRprDefectIfIndex'
_c='h3cRprDefaultRingIDIfIndex'
_b='h3cRprVrrpRSVirtualMacAddress'
_a='h3cRprVrrpRSIfIndex'
_Z='h3cRprIpv4OverallRSMacAddress'
_Y='h3cRprIpv4OverallRSIfIndex'
_X='h3cRprIpv6DynamicRSMacAddress'
_W='h3cRprIpv6DynamicRSIfIndex'
_V='h3cRprIpv4DynamicRSMacAddress'
_U='h3cRprIpv4DynamicRSIfIndex'
_T='h3cRprStaticRSMacAddress'
_S='h3cRprStaticRSIfIndex'
_R='h3cRprPktDropCntRingletID'
_Q='h3cRprPktDropCntIfIndex'
_P='h3cRprDestMacCountByDestAddress'
_O='h3cRprDestMacCountIfIndex'
_N='h3cRprSrcMacCountBySrcAddress'
_M='h3cRprSrcMacCountIfIndex'
_L='h3cRprMaxMumIfIndex'
_K='h3cRprPriority2ClassMap'
_J='accessible-for-notify'
_I='read-write'
_H='Integer32'
_G='h3cRprTrapRinglet'
_F='read-create'
_E='h3cRprTrapIfIndex'
_D='not-accessible'
_C='read-only'
_B='H3C-RPR-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
rprTopoImageEntry,rprTopoImageInetAddress,rprTopoImageMacAddress=mibBuilder.importSymbols('IEEE-802DOT17-RPR-MIB','rprTopoImageEntry','rprTopoImageInetAddress','rprTopoImageMacAddress')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddress,=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
h3cRpr=ModuleIdentity((1,3,6,1,4,1,2011,10,2,60))
if mibBuilder.loadTexts:h3cRpr.setRevisions(('2005-03-16 10:00',))
class H3cRprRingletID(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ringlet0',1),('ringlet1',2)))
class H3cRprServiceClass(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('classC',1),('classB',2),('classA1',3),('classA0',4)))
_H3cRprObjects_ObjectIdentity=ObjectIdentity
h3cRprObjects=_H3cRprObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,60,1))
_H3cRprMaxmumDefine_ObjectIdentity=ObjectIdentity
h3cRprMaxmumDefine=_H3cRprMaxmumDefine_ObjectIdentity((1,3,6,1,4,1,2011,10,2,60,1,1))
_H3cRprMaxmumDefineTable_Object=MibTable
h3cRprMaxmumDefineTable=_H3cRprMaxmumDefineTable_Object((1,3,6,1,4,1,2011,10,2,60,1,1,1))
if mibBuilder.loadTexts:h3cRprMaxmumDefineTable.setStatus(_A)
_H3cRprMaxmumDefineEntry_Object=MibTableRow
h3cRprMaxmumDefineEntry=_H3cRprMaxmumDefineEntry_Object((1,3,6,1,4,1,2011,10,2,60,1,1,1,1))
h3cRprMaxmumDefineEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:h3cRprMaxmumDefineEntry.setStatus(_A)
_H3cRprMaxMumIfIndex_Type=InterfaceIndex
_H3cRprMaxMumIfIndex_Object=MibTableColumn
h3cRprMaxMumIfIndex=_H3cRprMaxMumIfIndex_Object((1,3,6,1,4,1,2011,10,2,60,1,1,1,1,1),_H3cRprMaxMumIfIndex_Type())
h3cRprMaxMumIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cRprMaxMumIfIndex.setStatus(_A)
_H3cRprMaxStationNumDefine_Type=Integer32
_H3cRprMaxStationNumDefine_Object=MibTableColumn
h3cRprMaxStationNumDefine=_H3cRprMaxStationNumDefine_Object((1,3,6,1,4,1,2011,10,2,60,1,1,1,1,2),_H3cRprMaxStationNumDefine_Type())
h3cRprMaxStationNumDefine.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cRprMaxStationNumDefine.setStatus(_A)
_H3cRprMaxReservedRateDefine_Type=Gauge32
_H3cRprMaxReservedRateDefine_Object=MibTableColumn
h3cRprMaxReservedRateDefine=_H3cRprMaxReservedRateDefine_Object((1,3,6,1,4,1,2011,10,2,60,1,1,1,1,3),_H3cRprMaxReservedRateDefine_Type())
h3cRprMaxReservedRateDefine.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cRprMaxReservedRateDefine.setStatus(_A)
_H3cRprTopoImage_ObjectIdentity=ObjectIdentity
h3cRprTopoImage=_H3cRprTopoImage_ObjectIdentity((1,3,6,1,4,1,2011,10,2,60,1,2))
_H3cRprTopoImageXTable_Object=MibTable
h3cRprTopoImageXTable=_H3cRprTopoImageXTable_Object((1,3,6,1,4,1,2011,10,2,60,1,2,1))
if mibBuilder.loadTexts:h3cRprTopoImageXTable.setStatus(_A)
_H3cRprTopoImageXEntry_Object=MibTableRow
h3cRprTopoImageXEntry=_H3cRprTopoImageXEntry_Object((1,3,6,1,4,1,2011,10,2,60,1,2,1,1))
if mibBuilder.loadTexts:h3cRprTopoImageXEntry.setStatus(_A)
_H3cRprTopoImageXWestEdgeStatus_Type=TruthValue
_H3cRprTopoImageXWestEdgeStatus_Object=MibTableColumn
h3cRprTopoImageXWestEdgeStatus=_H3cRprTopoImageXWestEdgeStatus_Object((1,3,6,1,4,1,2011,10,2,60,1,2,1,1,3),_H3cRprTopoImageXWestEdgeStatus_Type())
h3cRprTopoImageXWestEdgeStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cRprTopoImageXWestEdgeStatus.setStatus(_A)
_H3cRprTopoImageXEastEdgeStatus_Type=TruthValue
_H3cRprTopoImageXEastEdgeStatus_Object=MibTableColumn
h3cRprTopoImageXEastEdgeStatus=_H3cRprTopoImageXEastEdgeStatus_Object((1,3,6,1,4,1,2011,10,2,60,1,2,1,1,4),_H3cRprTopoImageXEastEdgeStatus_Type())
h3cRprTopoImageXEastEdgeStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cRprTopoImageXEastEdgeStatus.setStatus(_A)
_H3cRprTopoImageXStationName_Type=SnmpAdminString
_H3cRprTopoImageXStationName_Object=MibTableColumn
h3cRprTopoImageXStationName=_H3cRprTopoImageXStationName_Object((1,3,6,1,4,1,2011,10,2,60,1,2,1,1,5),_H3cRprTopoImageXStationName_Type())
h3cRprTopoImageXStationName.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cRprTopoImageXStationName.setStatus(_A)
_H3cRprSpanCounters_ObjectIdentity=ObjectIdentity
h3cRprSpanCounters=_H3cRprSpanCounters_ObjectIdentity((1,3,6,1,4,1,2011,10,2,60,1,3))
_H3cRprSrcMacCountTable_Object=MibTable
h3cRprSrcMacCountTable=_H3cRprSrcMacCountTable_Object((1,3,6,1,4,1,2011,10,2,60,1,3,1))
if mibBuilder.loadTexts:h3cRprSrcMacCountTable.setStatus(_A)
_H3cRprSrcMacCountEntry_Object=MibTableRow
h3cRprSrcMacCountEntry=_H3cRprSrcMacCountEntry_Object((1,3,6,1,4,1,2011,10,2,60,1,3,1,1))
h3cRprSrcMacCountEntry.setIndexNames((0,_B,_M),(0,_B,_N))
if mibBuilder.loadTexts:h3cRprSrcMacCountEntry.setStatus(_A)
_H3cRprSrcMacCountIfIndex_Type=InterfaceIndex
_H3cRprSrcMacCountIfIndex_Object=MibTableColumn
h3cRprSrcMacCountIfIndex=_H3cRprSrcMacCountIfIndex_Object((1,3,6,1,4,1,2011,10,2,60,1,3,1,1,1),_H3cRprSrcMacCountIfIndex_Type())
h3cRprSrcMacCountIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cRprSrcMacCountIfIndex.setStatus(_A)
_H3cRprSrcMacCountBySrcAddress_Type=MacAddress
_H3cRprSrcMacCountBySrcAddress_Object=MibTableColumn
h3cRprSrcMacCountBySrcAddress=_H3cRprSrcMacCountBySrcAddress_Object((1,3,6,1,4,1,2011,10,2,60,1,3,1,1,2),_H3cRprSrcMacCountBySrcAddress_Type())
h3cRprSrcMacCountBySrcAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cRprSrcMacCountBySrcAddress.setStatus(_A)
_H3cRprSrcMacCountReceivedFrames_Type=Counter64
_H3cRprSrcMacCountReceivedFrames_Object=MibTableColumn
h3cRprSrcMacCountReceivedFrames=_H3cRprSrcMacCountReceivedFrames_Object((1,3,6,1,4,1,2011,10,2,60,1,3,1,1,3),_H3cRprSrcMacCountReceivedFrames_Type())
h3cRprSrcMacCountReceivedFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cRprSrcMacCountReceivedFrames.setStatus(_A)
_H3cRprSrcMacCountReceivedOctets_Type=Counter64
_H3cRprSrcMacCountReceivedOctets_Object=MibTableColumn
h3cRprSrcMacCountReceivedOctets=_H3cRprSrcMacCountReceivedOctets_Object((1,3,6,1,4,1,2011,10,2,60,1,3,1,1,4),_H3cRprSrcMacCountReceivedOctets_Type())
h3cRprSrcMacCountReceivedOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cRprSrcMacCountReceivedOctets.setStatus(_A)
_H3cRprDestMacCountTable_Object=MibTable
h3cRprDestMacCountTable=_H3cRprDestMacCountTable_Object((1,3,6,1,4,1,2011,10,2,60,1,3,2))
if mibBuilder.loadTexts:h3cRprDestMacCountTable.setStatus(_A)
_H3cRprDestMacCountEntry_Object=MibTableRow
h3cRprDestMacCountEntry=_H3cRprDestMacCountEntry_Object((1,3,6,1,4,1,2011,10,2,60,1,3,2,1))
h3cRprDestMacCountEntry.setIndexNames((0,_B,_O),(0,_B,_P))
if mibBuilder.loadTexts:h3cRprDestMacCountEntry.setStatus(_A)
_H3cRprDestMacCountIfIndex_Type=InterfaceIndex
_H3cRprDestMacCountIfIndex_Object=MibTableColumn
h3cRprDestMacCountIfIndex=_H3cRprDestMacCountIfIndex_Object((1,3,6,1,4,1,2011,10,2,60,1,3,2,1,1),_H3cRprDestMacCountIfIndex_Type())
h3cRprDestMacCountIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cRprDestMacCountIfIndex.setStatus(_A)
_H3cRprDestMacCountByDestAddress_Type=MacAddress
_H3cRprDestMacCountByDestAddress_Object=MibTableColumn
h3cRprDestMacCountByDestAddress=_H3cRprDestMacCountByDestAddress_Object((1,3,6,1,4,1,2011,10,2,60,1,3,2,1,2),_H3cRprDestMacCountByDestAddress_Type())
h3cRprDestMacCountByDestAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cRprDestMacCountByDestAddress.setStatus(_A)
_H3cRprDestMacCountReceivedFrames_Type=Counter64
_H3cRprDestMacCountReceivedFrames_Object=MibTableColumn
h3cRprDestMacCountReceivedFrames=_H3cRprDestMacCountReceivedFrames_Object((1,3,6,1,4,1,2011,10,2,60,1,3,2,1,3),_H3cRprDestMacCountReceivedFrames_Type())
h3cRprDestMacCountReceivedFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cRprDestMacCountReceivedFrames.setStatus(_A)
_H3cRprDestMacCountReceivedOctets_Type=Counter64
_H3cRprDestMacCountReceivedOctets_Object=MibTableColumn
h3cRprDestMacCountReceivedOctets=_H3cRprDestMacCountReceivedOctets_Object((1,3,6,1,4,1,2011,10,2,60,1,3,2,1,4),_H3cRprDestMacCountReceivedOctets_Type())
h3cRprDestMacCountReceivedOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cRprDestMacCountReceivedOctets.setStatus(_A)
_H3cRprPktDropCountTable_Object=MibTable
h3cRprPktDropCountTable=_H3cRprPktDropCountTable_Object((1,3,6,1,4,1,2011,10,2,60,1,3,3))
if mibBuilder.loadTexts:h3cRprPktDropCountTable.setStatus(_A)
_H3cRprPktDropCountEntry_Object=MibTableRow
h3cRprPktDropCountEntry=_H3cRprPktDropCountEntry_Object((1,3,6,1,4,1,2011,10,2,60,1,3,3,1))
h3cRprPktDropCountEntry.setIndexNames((0,_B,_Q),(0,_B,_R))
if mibBuilder.loadTexts:h3cRprPktDropCountEntry.setStatus(_A)
_H3cRprPktDropCntIfIndex_Type=InterfaceIndex
_H3cRprPktDropCntIfIndex_Object=MibTableColumn
h3cRprPktDropCntIfIndex=_H3cRprPktDropCntIfIndex_Object((1,3,6,1,4,1,2011,10,2,60,1,3,3,1,1),_H3cRprPktDropCntIfIndex_Type())
h3cRprPktDropCntIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cRprPktDropCntIfIndex.setStatus(_A)
_H3cRprPktDropCntRingletID_Type=H3cRprRingletID
_H3cRprPktDropCntRingletID_Object=MibTableColumn
h3cRprPktDropCntRingletID=_H3cRprPktDropCntRingletID_Object((1,3,6,1,4,1,2011,10,2,60,1,3,3,1,2),_H3cRprPktDropCntRingletID_Type())
h3cRprPktDropCntRingletID.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cRprPktDropCntRingletID.setStatus(_A)
_H3cRprDownFlowClassAPktDrops_Type=Counter64
_H3cRprDownFlowClassAPktDrops_Object=MibTableColumn
h3cRprDownFlowClassAPktDrops=_H3cRprDownFlowClassAPktDrops_Object((1,3,6,1,4,1,2011,10,2,60,1,3,3,1,3),_H3cRprDownFlowClassAPktDrops_Type())
h3cRprDownFlowClassAPktDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cRprDownFlowClassAPktDrops.setStatus(_A)
_H3cRprUpFlowClassAPktDrops_Type=Counter64
_H3cRprUpFlowClassAPktDrops_Object=MibTableColumn
h3cRprUpFlowClassAPktDrops=_H3cRprUpFlowClassAPktDrops_Object((1,3,6,1,4,1,2011,10,2,60,1,3,3,1,4),_H3cRprUpFlowClassAPktDrops_Type())
h3cRprUpFlowClassAPktDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cRprUpFlowClassAPktDrops.setStatus(_A)
_H3cRprDownFlowClassBPktDrops_Type=Counter64
_H3cRprDownFlowClassBPktDrops_Object=MibTableColumn
h3cRprDownFlowClassBPktDrops=_H3cRprDownFlowClassBPktDrops_Object((1,3,6,1,4,1,2011,10,2,60,1,3,3,1,5),_H3cRprDownFlowClassBPktDrops_Type())
h3cRprDownFlowClassBPktDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cRprDownFlowClassBPktDrops.setStatus(_A)
_H3cRprUpFlowClassBPktDrops_Type=Counter64
_H3cRprUpFlowClassBPktDrops_Object=MibTableColumn
h3cRprUpFlowClassBPktDrops=_H3cRprUpFlowClassBPktDrops_Object((1,3,6,1,4,1,2011,10,2,60,1,3,3,1,6),_H3cRprUpFlowClassBPktDrops_Type())
h3cRprUpFlowClassBPktDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cRprUpFlowClassBPktDrops.setStatus(_A)
_H3cRprDownFlowClassCPktDrops_Type=Counter64
_H3cRprDownFlowClassCPktDrops_Object=MibTableColumn
h3cRprDownFlowClassCPktDrops=_H3cRprDownFlowClassCPktDrops_Object((1,3,6,1,4,1,2011,10,2,60,1,3,3,1,7),_H3cRprDownFlowClassCPktDrops_Type())
h3cRprDownFlowClassCPktDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cRprDownFlowClassCPktDrops.setStatus(_A)
_H3cRprUpFlowClassCPktDrops_Type=Counter64
_H3cRprUpFlowClassCPktDrops_Object=MibTableColumn
h3cRprUpFlowClassCPktDrops=_H3cRprUpFlowClassCPktDrops_Object((1,3,6,1,4,1,2011,10,2,60,1,3,3,1,8),_H3cRprUpFlowClassCPktDrops_Type())
h3cRprUpFlowClassCPktDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cRprUpFlowClassCPktDrops.setStatus(_A)
_H3cRprRS_ObjectIdentity=ObjectIdentity
h3cRprRS=_H3cRprRS_ObjectIdentity((1,3,6,1,4,1,2011,10,2,60,1,4))
_H3cRprStaticRSTable_Object=MibTable
h3cRprStaticRSTable=_H3cRprStaticRSTable_Object((1,3,6,1,4,1,2011,10,2,60,1,4,1))
if mibBuilder.loadTexts:h3cRprStaticRSTable.setStatus(_A)
_H3cRprStaticRSEntry_Object=MibTableRow
h3cRprStaticRSEntry=_H3cRprStaticRSEntry_Object((1,3,6,1,4,1,2011,10,2,60,1,4,1,1))
h3cRprStaticRSEntry.setIndexNames((0,_B,_S),(0,_B,_T))
if mibBuilder.loadTexts:h3cRprStaticRSEntry.setStatus(_A)
_H3cRprStaticRSIfIndex_Type=InterfaceIndex
_H3cRprStaticRSIfIndex_Object=MibTableColumn
h3cRprStaticRSIfIndex=_H3cRprStaticRSIfIndex_Object((1,3,6,1,4,1,2011,10,2,60,1,4,1,1,1),_H3cRprStaticRSIfIndex_Type())
h3cRprStaticRSIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cRprStaticRSIfIndex.setStatus(_A)
_H3cRprStaticRSMacAddress_Type=MacAddress
_H3cRprStaticRSMacAddress_Object=MibTableColumn
h3cRprStaticRSMacAddress=_H3cRprStaticRSMacAddress_Object((1,3,6,1,4,1,2011,10,2,60,1,4,1,1,2),_H3cRprStaticRSMacAddress_Type())
h3cRprStaticRSMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cRprStaticRSMacAddress.setStatus(_A)
_H3cRprStaticRSRingletID_Type=H3cRprRingletID
_H3cRprStaticRSRingletID_Object=MibTableColumn
h3cRprStaticRSRingletID=_H3cRprStaticRSRingletID_Object((1,3,6,1,4,1,2011,10,2,60,1,4,1,1,3),_H3cRprStaticRSRingletID_Type())
h3cRprStaticRSRingletID.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cRprStaticRSRingletID.setStatus(_A)
_H3cRprStaticRSTtl_Type=Integer32
_H3cRprStaticRSTtl_Object=MibTableColumn
h3cRprStaticRSTtl=_H3cRprStaticRSTtl_Object((1,3,6,1,4,1,2011,10,2,60,1,4,1,1,4),_H3cRprStaticRSTtl_Type())
h3cRprStaticRSTtl.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cRprStaticRSTtl.setStatus(_A)
_H3cRprStaticRSValid_Type=TruthValue
_H3cRprStaticRSValid_Object=MibTableColumn
h3cRprStaticRSValid=_H3cRprStaticRSValid_Object((1,3,6,1,4,1,2011,10,2,60,1,4,1,1,5),_H3cRprStaticRSValid_Type())
h3cRprStaticRSValid.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cRprStaticRSValid.setStatus(_A)
_H3cRprStaticRSRowStatus_Type=RowStatus
_H3cRprStaticRSRowStatus_Object=MibTableColumn
h3cRprStaticRSRowStatus=_H3cRprStaticRSRowStatus_Object((1,3,6,1,4,1,2011,10,2,60,1,4,1,1,6),_H3cRprStaticRSRowStatus_Type())
h3cRprStaticRSRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cRprStaticRSRowStatus.setStatus(_A)
_H3cRprIpv4DynamicRSTable_Object=MibTable
h3cRprIpv4DynamicRSTable=_H3cRprIpv4DynamicRSTable_Object((1,3,6,1,4,1,2011,10,2,60,1,4,2))
if mibBuilder.loadTexts:h3cRprIpv4DynamicRSTable.setStatus(_A)
_H3cRprIpv4DynamicRSEntry_Object=MibTableRow
h3cRprIpv4DynamicRSEntry=_H3cRprIpv4DynamicRSEntry_Object((1,3,6,1,4,1,2011,10,2,60,1,4,2,1))
h3cRprIpv4DynamicRSEntry.setIndexNames((0,_B,_U),(0,_B,_V))
if mibBuilder.loadTexts:h3cRprIpv4DynamicRSEntry.setStatus(_A)
_H3cRprIpv4DynamicRSIfIndex_Type=InterfaceIndex
_H3cRprIpv4DynamicRSIfIndex_Object=MibTableColumn
h3cRprIpv4DynamicRSIfIndex=_H3cRprIpv4DynamicRSIfIndex_Object((1,3,6,1,4,1,2011,10,2,60,1,4,2,1,1),_H3cRprIpv4DynamicRSIfIndex_Type())
h3cRprIpv4DynamicRSIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cRprIpv4DynamicRSIfIndex.setStatus(_A)
_H3cRprIpv4DynamicRSMacAddress_Type=MacAddress
_H3cRprIpv4DynamicRSMacAddress_Object=MibTableColumn
h3cRprIpv4DynamicRSMacAddress=_H3cRprIpv4DynamicRSMacAddress_Object((1,3,6,1,4,1,2011,10,2,60,1,4,2,1,2),_H3cRprIpv4DynamicRSMacAddress_Type())
h3cRprIpv4DynamicRSMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cRprIpv4DynamicRSMacAddress.setStatus(_A)
_H3cRprIpv4DynamicRSRingletID_Type=H3cRprRingletID
_H3cRprIpv4DynamicRSRingletID_Object=MibTableColumn
h3cRprIpv4DynamicRSRingletID=_H3cRprIpv4DynamicRSRingletID_Object((1,3,6,1,4,1,2011,10,2,60,1,4,2,1,3),_H3cRprIpv4DynamicRSRingletID_Type())
h3cRprIpv4DynamicRSRingletID.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cRprIpv4DynamicRSRingletID.setStatus(_A)
_H3cRprIpv4DynamicRSTtl_Type=Integer32
_H3cRprIpv4DynamicRSTtl_Object=MibTableColumn
h3cRprIpv4DynamicRSTtl=_H3cRprIpv4DynamicRSTtl_Object((1,3,6,1,4,1,2011,10,2,60,1,4,2,1,4),_H3cRprIpv4DynamicRSTtl_Type())
h3cRprIpv4DynamicRSTtl.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cRprIpv4DynamicRSTtl.setStatus(_A)
_H3cRprIpv6DynamicRSTable_Object=MibTable
h3cRprIpv6DynamicRSTable=_H3cRprIpv6DynamicRSTable_Object((1,3,6,1,4,1,2011,10,2,60,1,4,3))
if mibBuilder.loadTexts:h3cRprIpv6DynamicRSTable.setStatus(_A)
_H3cRprIpv6DynamicRSEntry_Object=MibTableRow
h3cRprIpv6DynamicRSEntry=_H3cRprIpv6DynamicRSEntry_Object((1,3,6,1,4,1,2011,10,2,60,1,4,3,1))
h3cRprIpv6DynamicRSEntry.setIndexNames((0,_B,_W),(0,_B,_X))
if mibBuilder.loadTexts:h3cRprIpv6DynamicRSEntry.setStatus(_A)
_H3cRprIpv6DynamicRSIfIndex_Type=InterfaceIndex
_H3cRprIpv6DynamicRSIfIndex_Object=MibTableColumn
h3cRprIpv6DynamicRSIfIndex=_H3cRprIpv6DynamicRSIfIndex_Object((1,3,6,1,4,1,2011,10,2,60,1,4,3,1,1),_H3cRprIpv6DynamicRSIfIndex_Type())
h3cRprIpv6DynamicRSIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cRprIpv6DynamicRSIfIndex.setStatus(_A)
_H3cRprIpv6DynamicRSMacAddress_Type=MacAddress
_H3cRprIpv6DynamicRSMacAddress_Object=MibTableColumn
h3cRprIpv6DynamicRSMacAddress=_H3cRprIpv6DynamicRSMacAddress_Object((1,3,6,1,4,1,2011,10,2,60,1,4,3,1,2),_H3cRprIpv6DynamicRSMacAddress_Type())
h3cRprIpv6DynamicRSMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cRprIpv6DynamicRSMacAddress.setStatus(_A)
_H3cRprIpv6DynamicRSRingletID_Type=H3cRprRingletID
_H3cRprIpv6DynamicRSRingletID_Object=MibTableColumn
h3cRprIpv6DynamicRSRingletID=_H3cRprIpv6DynamicRSRingletID_Object((1,3,6,1,4,1,2011,10,2,60,1,4,3,1,3),_H3cRprIpv6DynamicRSRingletID_Type())
h3cRprIpv6DynamicRSRingletID.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cRprIpv6DynamicRSRingletID.setStatus(_A)
_H3cRprIpv6DynamicRSTtl_Type=Integer32
_H3cRprIpv6DynamicRSTtl_Object=MibTableColumn
h3cRprIpv6DynamicRSTtl=_H3cRprIpv6DynamicRSTtl_Object((1,3,6,1,4,1,2011,10,2,60,1,4,3,1,4),_H3cRprIpv6DynamicRSTtl_Type())
h3cRprIpv6DynamicRSTtl.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cRprIpv6DynamicRSTtl.setStatus(_A)
_H3cRprIpv4OverallRSTable_Object=MibTable
h3cRprIpv4OverallRSTable=_H3cRprIpv4OverallRSTable_Object((1,3,6,1,4,1,2011,10,2,60,1,4,4))
if mibBuilder.loadTexts:h3cRprIpv4OverallRSTable.setStatus(_A)
_H3cRprIpv4OverallRSEntry_Object=MibTableRow
h3cRprIpv4OverallRSEntry=_H3cRprIpv4OverallRSEntry_Object((1,3,6,1,4,1,2011,10,2,60,1,4,4,1))
h3cRprIpv4OverallRSEntry.setIndexNames((0,_B,_Y),(0,_B,_Z))
if mibBuilder.loadTexts:h3cRprIpv4OverallRSEntry.setStatus(_A)
_H3cRprIpv4OverallRSIfIndex_Type=InterfaceIndex
_H3cRprIpv4OverallRSIfIndex_Object=MibTableColumn
h3cRprIpv4OverallRSIfIndex=_H3cRprIpv4OverallRSIfIndex_Object((1,3,6,1,4,1,2011,10,2,60,1,4,4,1,1),_H3cRprIpv4OverallRSIfIndex_Type())
h3cRprIpv4OverallRSIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cRprIpv4OverallRSIfIndex.setStatus(_A)
_H3cRprIpv4OverallRSMacAddress_Type=MacAddress
_H3cRprIpv4OverallRSMacAddress_Object=MibTableColumn
h3cRprIpv4OverallRSMacAddress=_H3cRprIpv4OverallRSMacAddress_Object((1,3,6,1,4,1,2011,10,2,60,1,4,4,1,2),_H3cRprIpv4OverallRSMacAddress_Type())
h3cRprIpv4OverallRSMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cRprIpv4OverallRSMacAddress.setStatus(_A)
class _H3cRprIpv4OverallRSType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('static',1),('dynamic',2)))
_H3cRprIpv4OverallRSType_Type.__name__=_H
_H3cRprIpv4OverallRSType_Object=MibTableColumn
h3cRprIpv4OverallRSType=_H3cRprIpv4OverallRSType_Object((1,3,6,1,4,1,2011,10,2,60,1,4,4,1,3),_H3cRprIpv4OverallRSType_Type())
h3cRprIpv4OverallRSType.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cRprIpv4OverallRSType.setStatus(_A)
_H3cRprIpv4OverallRSRingletID_Type=H3cRprRingletID
_H3cRprIpv4OverallRSRingletID_Object=MibTableColumn
h3cRprIpv4OverallRSRingletID=_H3cRprIpv4OverallRSRingletID_Object((1,3,6,1,4,1,2011,10,2,60,1,4,4,1,4),_H3cRprIpv4OverallRSRingletID_Type())
h3cRprIpv4OverallRSRingletID.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cRprIpv4OverallRSRingletID.setStatus(_A)
_H3cRprIpv4OverallRSTtl_Type=Integer32
_H3cRprIpv4OverallRSTtl_Object=MibTableColumn
h3cRprIpv4OverallRSTtl=_H3cRprIpv4OverallRSTtl_Object((1,3,6,1,4,1,2011,10,2,60,1,4,4,1,5),_H3cRprIpv4OverallRSTtl_Type())
h3cRprIpv4OverallRSTtl.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cRprIpv4OverallRSTtl.setStatus(_A)
_H3cRprVrrpRSTable_Object=MibTable
h3cRprVrrpRSTable=_H3cRprVrrpRSTable_Object((1,3,6,1,4,1,2011,10,2,60,1,4,5))
if mibBuilder.loadTexts:h3cRprVrrpRSTable.setStatus(_A)
_H3cRprVrrpRSEntry_Object=MibTableRow
h3cRprVrrpRSEntry=_H3cRprVrrpRSEntry_Object((1,3,6,1,4,1,2011,10,2,60,1,4,5,1))
h3cRprVrrpRSEntry.setIndexNames((0,_B,_a),(0,_B,_b))
if mibBuilder.loadTexts:h3cRprVrrpRSEntry.setStatus(_A)
_H3cRprVrrpRSIfIndex_Type=InterfaceIndex
_H3cRprVrrpRSIfIndex_Object=MibTableColumn
h3cRprVrrpRSIfIndex=_H3cRprVrrpRSIfIndex_Object((1,3,6,1,4,1,2011,10,2,60,1,4,5,1,1),_H3cRprVrrpRSIfIndex_Type())
h3cRprVrrpRSIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cRprVrrpRSIfIndex.setStatus(_A)
_H3cRprVrrpRSVirtualMacAddress_Type=MacAddress
_H3cRprVrrpRSVirtualMacAddress_Object=MibTableColumn
h3cRprVrrpRSVirtualMacAddress=_H3cRprVrrpRSVirtualMacAddress_Object((1,3,6,1,4,1,2011,10,2,60,1,4,5,1,2),_H3cRprVrrpRSVirtualMacAddress_Type())
h3cRprVrrpRSVirtualMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cRprVrrpRSVirtualMacAddress.setStatus(_A)
_H3cRprVrrpRSMacAddress_Type=MacAddress
_H3cRprVrrpRSMacAddress_Object=MibTableColumn
h3cRprVrrpRSMacAddress=_H3cRprVrrpRSMacAddress_Object((1,3,6,1,4,1,2011,10,2,60,1,4,5,1,3),_H3cRprVrrpRSMacAddress_Type())
h3cRprVrrpRSMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cRprVrrpRSMacAddress.setStatus(_A)
_H3cRprVrrpRSRingletID_Type=H3cRprRingletID
_H3cRprVrrpRSRingletID_Object=MibTableColumn
h3cRprVrrpRSRingletID=_H3cRprVrrpRSRingletID_Object((1,3,6,1,4,1,2011,10,2,60,1,4,5,1,4),_H3cRprVrrpRSRingletID_Type())
h3cRprVrrpRSRingletID.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cRprVrrpRSRingletID.setStatus(_A)
_H3cRprVrrpRSTtl_Type=Integer32
_H3cRprVrrpRSTtl_Object=MibTableColumn
h3cRprVrrpRSTtl=_H3cRprVrrpRSTtl_Object((1,3,6,1,4,1,2011,10,2,60,1,4,5,1,5),_H3cRprVrrpRSTtl_Type())
h3cRprVrrpRSTtl.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cRprVrrpRSTtl.setStatus(_A)
_H3cRprDefaultRingIDTable_Object=MibTable
h3cRprDefaultRingIDTable=_H3cRprDefaultRingIDTable_Object((1,3,6,1,4,1,2011,10,2,60,1,4,6))
if mibBuilder.loadTexts:h3cRprDefaultRingIDTable.setStatus(_A)
_H3cRprDefaultRingIDEntry_Object=MibTableRow
h3cRprDefaultRingIDEntry=_H3cRprDefaultRingIDEntry_Object((1,3,6,1,4,1,2011,10,2,60,1,4,6,1))
h3cRprDefaultRingIDEntry.setIndexNames((0,_B,_c))
if mibBuilder.loadTexts:h3cRprDefaultRingIDEntry.setStatus(_A)
_H3cRprDefaultRingIDIfIndex_Type=InterfaceIndex
_H3cRprDefaultRingIDIfIndex_Object=MibTableColumn
h3cRprDefaultRingIDIfIndex=_H3cRprDefaultRingIDIfIndex_Object((1,3,6,1,4,1,2011,10,2,60,1,4,6,1,1),_H3cRprDefaultRingIDIfIndex_Type())
h3cRprDefaultRingIDIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cRprDefaultRingIDIfIndex.setStatus(_A)
_H3cRprDefaultConfigRingletID_Type=H3cRprRingletID
_H3cRprDefaultConfigRingletID_Object=MibTableColumn
h3cRprDefaultConfigRingletID=_H3cRprDefaultConfigRingletID_Object((1,3,6,1,4,1,2011,10,2,60,1,4,6,1,2),_H3cRprDefaultConfigRingletID_Type())
h3cRprDefaultConfigRingletID.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cRprDefaultConfigRingletID.setStatus(_A)
_H3cRprDefaultActiveRingID_Type=H3cRprRingletID
_H3cRprDefaultActiveRingID_Object=MibTableColumn
h3cRprDefaultActiveRingID=_H3cRprDefaultActiveRingID_Object((1,3,6,1,4,1,2011,10,2,60,1,4,6,1,3),_H3cRprDefaultActiveRingID_Type())
h3cRprDefaultActiveRingID.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cRprDefaultActiveRingID.setStatus(_A)
_H3cRprDefect_ObjectIdentity=ObjectIdentity
h3cRprDefect=_H3cRprDefect_ObjectIdentity((1,3,6,1,4,1,2011,10,2,60,1,5))
_H3cRprDefectReportTable_Object=MibTable
h3cRprDefectReportTable=_H3cRprDefectReportTable_Object((1,3,6,1,4,1,2011,10,2,60,1,5,1))
if mibBuilder.loadTexts:h3cRprDefectReportTable.setStatus(_A)
_H3cRprDefectReportEntry_Object=MibTableRow
h3cRprDefectReportEntry=_H3cRprDefectReportEntry_Object((1,3,6,1,4,1,2011,10,2,60,1,5,1,1))
h3cRprDefectReportEntry.setIndexNames((0,_B,_d))
if mibBuilder.loadTexts:h3cRprDefectReportEntry.setStatus(_A)
_H3cRprDefectIfIndex_Type=InterfaceIndex
_H3cRprDefectIfIndex_Object=MibTableColumn
h3cRprDefectIfIndex=_H3cRprDefectIfIndex_Object((1,3,6,1,4,1,2011,10,2,60,1,5,1,1,1),_H3cRprDefectIfIndex_Type())
h3cRprDefectIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cRprDefectIfIndex.setStatus(_A)
class _H3cRprDefectCurrentStatus_Type(Bits):namedValues=NamedValues(*(('topologyOpenRing',0),('topoInstability',1),('topoInconsistent',2),('dulpMacAddress',3),('dulpIPAddress',4),('lrttDefect',5),('protCfgDefect',6),('jumboCfgDefect',7),('excessReservedRateDefect',8),('excessMaxStationNum',9),('miscabling',10),('backPressure',11)))
_H3cRprDefectCurrentStatus_Type.__name__='Bits'
_H3cRprDefectCurrentStatus_Object=MibTableColumn
h3cRprDefectCurrentStatus=_H3cRprDefectCurrentStatus_Object((1,3,6,1,4,1,2011,10,2,60,1,5,1,1,2),_H3cRprDefectCurrentStatus_Type())
h3cRprDefectCurrentStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cRprDefectCurrentStatus.setStatus(_A)
_H3cRprPriorityMap_ObjectIdentity=ObjectIdentity
h3cRprPriorityMap=_H3cRprPriorityMap_ObjectIdentity((1,3,6,1,4,1,2011,10,2,60,1,6))
_H3cRprPriority2ClassMapTable_Object=MibTable
h3cRprPriority2ClassMapTable=_H3cRprPriority2ClassMapTable_Object((1,3,6,1,4,1,2011,10,2,60,1,6,1))
if mibBuilder.loadTexts:h3cRprPriority2ClassMapTable.setStatus(_A)
_H3cRprPriority2ClassMapEntry_Object=MibTableRow
h3cRprPriority2ClassMapEntry=_H3cRprPriority2ClassMapEntry_Object((1,3,6,1,4,1,2011,10,2,60,1,6,1,1))
h3cRprPriority2ClassMapEntry.setIndexNames((0,_B,_e),(0,_B,_f),(0,_B,_g))
if mibBuilder.loadTexts:h3cRprPriority2ClassMapEntry.setStatus(_A)
_H3cRprPriority2ClassMapIfIndex_Type=InterfaceIndex
_H3cRprPriority2ClassMapIfIndex_Object=MibTableColumn
h3cRprPriority2ClassMapIfIndex=_H3cRprPriority2ClassMapIfIndex_Object((1,3,6,1,4,1,2011,10,2,60,1,6,1,1,1),_H3cRprPriority2ClassMapIfIndex_Type())
h3cRprPriority2ClassMapIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cRprPriority2ClassMapIfIndex.setStatus(_A)
class _H3cRprPriority2ClassMapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('tag',1),('mpls',2),('ip',3)))
_H3cRprPriority2ClassMapType_Type.__name__=_H
_H3cRprPriority2ClassMapType_Object=MibTableColumn
h3cRprPriority2ClassMapType=_H3cRprPriority2ClassMapType_Object((1,3,6,1,4,1,2011,10,2,60,1,6,1,1,2),_H3cRprPriority2ClassMapType_Type())
h3cRprPriority2ClassMapType.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cRprPriority2ClassMapType.setStatus(_A)
class _H3cRprPriorityValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('pri0',1),('pri1',2),('pri2',3),('pri3',4),('pri4',5),('pri5',6),('pri6',7),('pri7',8)))
_H3cRprPriorityValue_Type.__name__=_H
_H3cRprPriorityValue_Object=MibTableColumn
h3cRprPriorityValue=_H3cRprPriorityValue_Object((1,3,6,1,4,1,2011,10,2,60,1,6,1,1,3),_H3cRprPriorityValue_Type())
h3cRprPriorityValue.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cRprPriorityValue.setStatus(_A)
_H3cRprPriority2ClassMap_Type=H3cRprServiceClass
_H3cRprPriority2ClassMap_Object=MibTableColumn
h3cRprPriority2ClassMap=_H3cRprPriority2ClassMap_Object((1,3,6,1,4,1,2011,10,2,60,1,6,1,1,4),_H3cRprPriority2ClassMap_Type())
h3cRprPriority2ClassMap.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cRprPriority2ClassMap.setStatus(_A)
_H3cRprRateLimitConfig_ObjectIdentity=ObjectIdentity
h3cRprRateLimitConfig=_H3cRprRateLimitConfig_ObjectIdentity((1,3,6,1,4,1,2011,10,2,60,1,7))
_H3cRprRateLimitConfigTable_Object=MibTable
h3cRprRateLimitConfigTable=_H3cRprRateLimitConfigTable_Object((1,3,6,1,4,1,2011,10,2,60,1,7,1))
if mibBuilder.loadTexts:h3cRprRateLimitConfigTable.setStatus(_A)
_H3cRprRateLimitConfigEntry_Object=MibTableRow
h3cRprRateLimitConfigEntry=_H3cRprRateLimitConfigEntry_Object((1,3,6,1,4,1,2011,10,2,60,1,7,1,1))
h3cRprRateLimitConfigEntry.setIndexNames((0,_B,_h),(0,_B,_i),(0,_B,_j))
if mibBuilder.loadTexts:h3cRprRateLimitConfigEntry.setStatus(_A)
_H3cRprRateLimitConfigIfIndex_Type=InterfaceIndex
_H3cRprRateLimitConfigIfIndex_Object=MibTableColumn
h3cRprRateLimitConfigIfIndex=_H3cRprRateLimitConfigIfIndex_Object((1,3,6,1,4,1,2011,10,2,60,1,7,1,1,1),_H3cRprRateLimitConfigIfIndex_Type())
h3cRprRateLimitConfigIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cRprRateLimitConfigIfIndex.setStatus(_A)
_H3cRprRateLimitConfigRingletId_Type=H3cRprRingletID
_H3cRprRateLimitConfigRingletId_Object=MibTableColumn
h3cRprRateLimitConfigRingletId=_H3cRprRateLimitConfigRingletId_Object((1,3,6,1,4,1,2011,10,2,60,1,7,1,1,2),_H3cRprRateLimitConfigRingletId_Type())
h3cRprRateLimitConfigRingletId.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cRprRateLimitConfigRingletId.setStatus(_A)
_H3cRprRateLimitConfigServiceClass_Type=H3cRprServiceClass
_H3cRprRateLimitConfigServiceClass_Object=MibTableColumn
h3cRprRateLimitConfigServiceClass=_H3cRprRateLimitConfigServiceClass_Object((1,3,6,1,4,1,2011,10,2,60,1,7,1,1,3),_H3cRprRateLimitConfigServiceClass_Type())
h3cRprRateLimitConfigServiceClass.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cRprRateLimitConfigServiceClass.setStatus(_A)
_H3cRprRateLimitConfigValue_Type=Integer32
_H3cRprRateLimitConfigValue_Object=MibTableColumn
h3cRprRateLimitConfigValue=_H3cRprRateLimitConfigValue_Object((1,3,6,1,4,1,2011,10,2,60,1,7,1,1,4),_H3cRprRateLimitConfigValue_Type())
h3cRprRateLimitConfigValue.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cRprRateLimitConfigValue.setStatus(_A)
_H3cRprMacAddrLearn_ObjectIdentity=ObjectIdentity
h3cRprMacAddrLearn=_H3cRprMacAddrLearn_ObjectIdentity((1,3,6,1,4,1,2011,10,2,60,1,8))
_H3cRprMacLearnCfgTable_Object=MibTable
h3cRprMacLearnCfgTable=_H3cRprMacLearnCfgTable_Object((1,3,6,1,4,1,2011,10,2,60,1,8,1))
if mibBuilder.loadTexts:h3cRprMacLearnCfgTable.setStatus(_A)
_H3cRprMacLearnCfgEntry_Object=MibTableRow
h3cRprMacLearnCfgEntry=_H3cRprMacLearnCfgEntry_Object((1,3,6,1,4,1,2011,10,2,60,1,8,1,1))
h3cRprMacLearnCfgEntry.setIndexNames((0,_B,_k),(0,_B,_l))
if mibBuilder.loadTexts:h3cRprMacLearnCfgEntry.setStatus(_A)
_H3cRprMacLearnIfIndex_Type=InterfaceIndex
_H3cRprMacLearnIfIndex_Object=MibTableColumn
h3cRprMacLearnIfIndex=_H3cRprMacLearnIfIndex_Object((1,3,6,1,4,1,2011,10,2,60,1,8,1,1,1),_H3cRprMacLearnIfIndex_Type())
h3cRprMacLearnIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cRprMacLearnIfIndex.setStatus(_A)
_H3cRprMacLearnRprMac_Type=MacAddress
_H3cRprMacLearnRprMac_Object=MibTableColumn
h3cRprMacLearnRprMac=_H3cRprMacLearnRprMac_Object((1,3,6,1,4,1,2011,10,2,60,1,8,1,1,2),_H3cRprMacLearnRprMac_Type())
h3cRprMacLearnRprMac.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cRprMacLearnRprMac.setStatus(_A)
_H3cRprMacLearnType_Type=Integer32
_H3cRprMacLearnType_Object=MibTableColumn
h3cRprMacLearnType=_H3cRprMacLearnType_Object((1,3,6,1,4,1,2011,10,2,60,1,8,1,1,3),_H3cRprMacLearnType_Type())
h3cRprMacLearnType.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cRprMacLearnType.setStatus(_A)
_H3cRprMacLearnDestMac_Type=MacAddress
_H3cRprMacLearnDestMac_Object=MibTableColumn
h3cRprMacLearnDestMac=_H3cRprMacLearnDestMac_Object((1,3,6,1,4,1,2011,10,2,60,1,8,1,1,4),_H3cRprMacLearnDestMac_Type())
h3cRprMacLearnDestMac.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cRprMacLearnDestMac.setStatus(_A)
class _H3cRprMacLearnVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_H3cRprMacLearnVlanId_Type.__name__=_H
_H3cRprMacLearnVlanId_Object=MibTableColumn
h3cRprMacLearnVlanId=_H3cRprMacLearnVlanId_Object((1,3,6,1,4,1,2011,10,2,60,1,8,1,1,5),_H3cRprMacLearnVlanId_Type())
h3cRprMacLearnVlanId.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cRprMacLearnVlanId.setStatus(_A)
_H3cRprMacLearnRinglet_Type=H3cRprRingletID
_H3cRprMacLearnRinglet_Object=MibTableColumn
h3cRprMacLearnRinglet=_H3cRprMacLearnRinglet_Object((1,3,6,1,4,1,2011,10,2,60,1,8,1,1,6),_H3cRprMacLearnRinglet_Type())
h3cRprMacLearnRinglet.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cRprMacLearnRinglet.setStatus(_A)
_H3cRprMacLearnTtl_Type=Integer32
_H3cRprMacLearnTtl_Object=MibTableColumn
h3cRprMacLearnTtl=_H3cRprMacLearnTtl_Object((1,3,6,1,4,1,2011,10,2,60,1,8,1,1,7),_H3cRprMacLearnTtl_Type())
h3cRprMacLearnTtl.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cRprMacLearnTtl.setStatus(_A)
_H3cRprMacLearnIsValid_Type=TruthValue
_H3cRprMacLearnIsValid_Object=MibTableColumn
h3cRprMacLearnIsValid=_H3cRprMacLearnIsValid_Object((1,3,6,1,4,1,2011,10,2,60,1,8,1,1,8),_H3cRprMacLearnIsValid_Type())
h3cRprMacLearnIsValid.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cRprMacLearnIsValid.setStatus(_A)
_H3cRprMacLearnRowStatus_Type=RowStatus
_H3cRprMacLearnRowStatus_Object=MibTableColumn
h3cRprMacLearnRowStatus=_H3cRprMacLearnRowStatus_Object((1,3,6,1,4,1,2011,10,2,60,1,8,1,1,9),_H3cRprMacLearnRowStatus_Type())
h3cRprMacLearnRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cRprMacLearnRowStatus.setStatus(_A)
_H3cRprTrapVar_ObjectIdentity=ObjectIdentity
h3cRprTrapVar=_H3cRprTrapVar_ObjectIdentity((1,3,6,1,4,1,2011,10,2,60,1,9))
_H3cRprTrapVarTable_Object=MibTable
h3cRprTrapVarTable=_H3cRprTrapVarTable_Object((1,3,6,1,4,1,2011,10,2,60,1,9,1))
if mibBuilder.loadTexts:h3cRprTrapVarTable.setStatus(_A)
_H3cRprTrapVarEntry_Object=MibTableRow
h3cRprTrapVarEntry=_H3cRprTrapVarEntry_Object((1,3,6,1,4,1,2011,10,2,60,1,9,1,1))
h3cRprTrapVarEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:h3cRprTrapVarEntry.setStatus(_A)
_H3cRprTrapIfIndex_Type=InterfaceIndex
_H3cRprTrapIfIndex_Object=MibTableColumn
h3cRprTrapIfIndex=_H3cRprTrapIfIndex_Object((1,3,6,1,4,1,2011,10,2,60,1,9,1,1,1),_H3cRprTrapIfIndex_Type())
h3cRprTrapIfIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cRprTrapIfIndex.setStatus(_A)
_H3cRprTrapRinglet_Type=H3cRprRingletID
_H3cRprTrapRinglet_Object=MibTableColumn
h3cRprTrapRinglet=_H3cRprTrapRinglet_Object((1,3,6,1,4,1,2011,10,2,60,1,9,1,1,2),_H3cRprTrapRinglet_Type())
h3cRprTrapRinglet.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cRprTrapRinglet.setStatus(_A)
_H3cRprTrapTopoMacAddress_Type=MacAddress
_H3cRprTrapTopoMacAddress_Object=MibTableColumn
h3cRprTrapTopoMacAddress=_H3cRprTrapTopoMacAddress_Object((1,3,6,1,4,1,2011,10,2,60,1,9,1,1,3),_H3cRprTrapTopoMacAddress_Type())
h3cRprTrapTopoMacAddress.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cRprTrapTopoMacAddress.setStatus(_A)
_H3cRprTrapIpAddress_Type=InetAddress
_H3cRprTrapIpAddress_Object=MibTableColumn
h3cRprTrapIpAddress=_H3cRprTrapIpAddress_Object((1,3,6,1,4,1,2011,10,2,60,1,9,1,1,4),_H3cRprTrapIpAddress_Type())
h3cRprTrapIpAddress.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cRprTrapIpAddress.setStatus(_A)
_H3cRprTrap_ObjectIdentity=ObjectIdentity
h3cRprTrap=_H3cRprTrap_ObjectIdentity((1,3,6,1,4,1,2011,10,2,60,1,10))
rprTopoImageEntry.registerAugmentions((_B,_m))
h3cRprTopoImageXEntry.setIndexNames(*rprTopoImageEntry.getIndexNames())
h3cRprTopologyOpenRing=NotificationType((1,3,6,1,4,1,2011,10,2,60,1,10,1))
h3cRprTopologyOpenRing.setObjects(*((_B,_E),(_B,_G)))
if mibBuilder.loadTexts:h3cRprTopologyOpenRing.setStatus(_A)
h3cRprTopologyCloseRing=NotificationType((1,3,6,1,4,1,2011,10,2,60,1,10,2))
h3cRprTopologyCloseRing.setObjects(*((_B,_E),(_B,_G)))
if mibBuilder.loadTexts:h3cRprTopologyCloseRing.setStatus(_A)
h3cRprTopologyInconsistent=NotificationType((1,3,6,1,4,1,2011,10,2,60,1,10,3))
h3cRprTopologyInconsistent.setObjects((_B,_E))
if mibBuilder.loadTexts:h3cRprTopologyInconsistent.setStatus(_A)
h3cRprTopologyInstability=NotificationType((1,3,6,1,4,1,2011,10,2,60,1,10,4))
h3cRprTopologyInstability.setObjects((_B,_E))
if mibBuilder.loadTexts:h3cRprTopologyInstability.setStatus(_A)
h3cRprDuplicateMacAddress=NotificationType((1,3,6,1,4,1,2011,10,2,60,1,10,5))
h3cRprDuplicateMacAddress.setObjects(*((_B,_E),(_B,_n)))
if mibBuilder.loadTexts:h3cRprDuplicateMacAddress.setStatus(_A)
h3cRprDulplicateIPAddress=NotificationType((1,3,6,1,4,1,2011,10,2,60,1,10,6))
h3cRprDulplicateIPAddress.setObjects(*((_B,_E),(_B,_o)))
if mibBuilder.loadTexts:h3cRprDulplicateIPAddress.setStatus(_A)
h3cRprIncompleteLRTT=NotificationType((1,3,6,1,4,1,2011,10,2,60,1,10,7))
h3cRprIncompleteLRTT.setObjects((_B,_E))
if mibBuilder.loadTexts:h3cRprIncompleteLRTT.setStatus(_A)
h3cRprProtecConfigInconsistent=NotificationType((1,3,6,1,4,1,2011,10,2,60,1,10,8))
h3cRprProtecConfigInconsistent.setObjects((_B,_E))
if mibBuilder.loadTexts:h3cRprProtecConfigInconsistent.setStatus(_A)
h3cRprJumboConfigInconsistent=NotificationType((1,3,6,1,4,1,2011,10,2,60,1,10,9))
h3cRprJumboConfigInconsistent.setObjects((_B,_E))
if mibBuilder.loadTexts:h3cRprJumboConfigInconsistent.setStatus(_A)
h3cRprExceedMaxReservRate=NotificationType((1,3,6,1,4,1,2011,10,2,60,1,10,10))
h3cRprExceedMaxReservRate.setObjects(*((_B,_E),(_B,_G)))
if mibBuilder.loadTexts:h3cRprExceedMaxReservRate.setStatus(_A)
h3cRprExceedMaxStationNum=NotificationType((1,3,6,1,4,1,2011,10,2,60,1,10,11))
h3cRprExceedMaxStationNum.setObjects((_B,_E))
if mibBuilder.loadTexts:h3cRprExceedMaxStationNum.setStatus(_A)
h3cRprMiscabling=NotificationType((1,3,6,1,4,1,2011,10,2,60,1,10,12))
h3cRprMiscabling.setObjects(*((_B,_E),(_B,_G)))
if mibBuilder.loadTexts:h3cRprMiscabling.setStatus(_A)
h3cRprBackPressure=NotificationType((1,3,6,1,4,1,2011,10,2,60,1,10,13))
h3cRprBackPressure.setObjects(*((_B,_E),(_B,_G),(_B,_K)))
if mibBuilder.loadTexts:h3cRprBackPressure.setStatus(_A)
h3cRprBackPressureOver=NotificationType((1,3,6,1,4,1,2011,10,2,60,1,10,14))
h3cRprBackPressureOver.setObjects(*((_B,_E),(_B,_G),(_B,_K)))
if mibBuilder.loadTexts:h3cRprBackPressureOver.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'H3cRprRingletID':H3cRprRingletID,'H3cRprServiceClass':H3cRprServiceClass,'h3cRpr':h3cRpr,'h3cRprObjects':h3cRprObjects,'h3cRprMaxmumDefine':h3cRprMaxmumDefine,'h3cRprMaxmumDefineTable':h3cRprMaxmumDefineTable,'h3cRprMaxmumDefineEntry':h3cRprMaxmumDefineEntry,_L:h3cRprMaxMumIfIndex,'h3cRprMaxStationNumDefine':h3cRprMaxStationNumDefine,'h3cRprMaxReservedRateDefine':h3cRprMaxReservedRateDefine,'h3cRprTopoImage':h3cRprTopoImage,'h3cRprTopoImageXTable':h3cRprTopoImageXTable,_m:h3cRprTopoImageXEntry,'h3cRprTopoImageXWestEdgeStatus':h3cRprTopoImageXWestEdgeStatus,'h3cRprTopoImageXEastEdgeStatus':h3cRprTopoImageXEastEdgeStatus,'h3cRprTopoImageXStationName':h3cRprTopoImageXStationName,'h3cRprSpanCounters':h3cRprSpanCounters,'h3cRprSrcMacCountTable':h3cRprSrcMacCountTable,'h3cRprSrcMacCountEntry':h3cRprSrcMacCountEntry,_M:h3cRprSrcMacCountIfIndex,_N:h3cRprSrcMacCountBySrcAddress,'h3cRprSrcMacCountReceivedFrames':h3cRprSrcMacCountReceivedFrames,'h3cRprSrcMacCountReceivedOctets':h3cRprSrcMacCountReceivedOctets,'h3cRprDestMacCountTable':h3cRprDestMacCountTable,'h3cRprDestMacCountEntry':h3cRprDestMacCountEntry,_O:h3cRprDestMacCountIfIndex,_P:h3cRprDestMacCountByDestAddress,'h3cRprDestMacCountReceivedFrames':h3cRprDestMacCountReceivedFrames,'h3cRprDestMacCountReceivedOctets':h3cRprDestMacCountReceivedOctets,'h3cRprPktDropCountTable':h3cRprPktDropCountTable,'h3cRprPktDropCountEntry':h3cRprPktDropCountEntry,_Q:h3cRprPktDropCntIfIndex,_R:h3cRprPktDropCntRingletID,'h3cRprDownFlowClassAPktDrops':h3cRprDownFlowClassAPktDrops,'h3cRprUpFlowClassAPktDrops':h3cRprUpFlowClassAPktDrops,'h3cRprDownFlowClassBPktDrops':h3cRprDownFlowClassBPktDrops,'h3cRprUpFlowClassBPktDrops':h3cRprUpFlowClassBPktDrops,'h3cRprDownFlowClassCPktDrops':h3cRprDownFlowClassCPktDrops,'h3cRprUpFlowClassCPktDrops':h3cRprUpFlowClassCPktDrops,'h3cRprRS':h3cRprRS,'h3cRprStaticRSTable':h3cRprStaticRSTable,'h3cRprStaticRSEntry':h3cRprStaticRSEntry,_S:h3cRprStaticRSIfIndex,_T:h3cRprStaticRSMacAddress,'h3cRprStaticRSRingletID':h3cRprStaticRSRingletID,'h3cRprStaticRSTtl':h3cRprStaticRSTtl,'h3cRprStaticRSValid':h3cRprStaticRSValid,'h3cRprStaticRSRowStatus':h3cRprStaticRSRowStatus,'h3cRprIpv4DynamicRSTable':h3cRprIpv4DynamicRSTable,'h3cRprIpv4DynamicRSEntry':h3cRprIpv4DynamicRSEntry,_U:h3cRprIpv4DynamicRSIfIndex,_V:h3cRprIpv4DynamicRSMacAddress,'h3cRprIpv4DynamicRSRingletID':h3cRprIpv4DynamicRSRingletID,'h3cRprIpv4DynamicRSTtl':h3cRprIpv4DynamicRSTtl,'h3cRprIpv6DynamicRSTable':h3cRprIpv6DynamicRSTable,'h3cRprIpv6DynamicRSEntry':h3cRprIpv6DynamicRSEntry,_W:h3cRprIpv6DynamicRSIfIndex,_X:h3cRprIpv6DynamicRSMacAddress,'h3cRprIpv6DynamicRSRingletID':h3cRprIpv6DynamicRSRingletID,'h3cRprIpv6DynamicRSTtl':h3cRprIpv6DynamicRSTtl,'h3cRprIpv4OverallRSTable':h3cRprIpv4OverallRSTable,'h3cRprIpv4OverallRSEntry':h3cRprIpv4OverallRSEntry,_Y:h3cRprIpv4OverallRSIfIndex,_Z:h3cRprIpv4OverallRSMacAddress,'h3cRprIpv4OverallRSType':h3cRprIpv4OverallRSType,'h3cRprIpv4OverallRSRingletID':h3cRprIpv4OverallRSRingletID,'h3cRprIpv4OverallRSTtl':h3cRprIpv4OverallRSTtl,'h3cRprVrrpRSTable':h3cRprVrrpRSTable,'h3cRprVrrpRSEntry':h3cRprVrrpRSEntry,_a:h3cRprVrrpRSIfIndex,_b:h3cRprVrrpRSVirtualMacAddress,'h3cRprVrrpRSMacAddress':h3cRprVrrpRSMacAddress,'h3cRprVrrpRSRingletID':h3cRprVrrpRSRingletID,'h3cRprVrrpRSTtl':h3cRprVrrpRSTtl,'h3cRprDefaultRingIDTable':h3cRprDefaultRingIDTable,'h3cRprDefaultRingIDEntry':h3cRprDefaultRingIDEntry,_c:h3cRprDefaultRingIDIfIndex,'h3cRprDefaultConfigRingletID':h3cRprDefaultConfigRingletID,'h3cRprDefaultActiveRingID':h3cRprDefaultActiveRingID,'h3cRprDefect':h3cRprDefect,'h3cRprDefectReportTable':h3cRprDefectReportTable,'h3cRprDefectReportEntry':h3cRprDefectReportEntry,_d:h3cRprDefectIfIndex,'h3cRprDefectCurrentStatus':h3cRprDefectCurrentStatus,'h3cRprPriorityMap':h3cRprPriorityMap,'h3cRprPriority2ClassMapTable':h3cRprPriority2ClassMapTable,'h3cRprPriority2ClassMapEntry':h3cRprPriority2ClassMapEntry,_e:h3cRprPriority2ClassMapIfIndex,_f:h3cRprPriority2ClassMapType,_g:h3cRprPriorityValue,_K:h3cRprPriority2ClassMap,'h3cRprRateLimitConfig':h3cRprRateLimitConfig,'h3cRprRateLimitConfigTable':h3cRprRateLimitConfigTable,'h3cRprRateLimitConfigEntry':h3cRprRateLimitConfigEntry,_h:h3cRprRateLimitConfigIfIndex,_i:h3cRprRateLimitConfigRingletId,_j:h3cRprRateLimitConfigServiceClass,'h3cRprRateLimitConfigValue':h3cRprRateLimitConfigValue,'h3cRprMacAddrLearn':h3cRprMacAddrLearn,'h3cRprMacLearnCfgTable':h3cRprMacLearnCfgTable,'h3cRprMacLearnCfgEntry':h3cRprMacLearnCfgEntry,_k:h3cRprMacLearnIfIndex,_l:h3cRprMacLearnRprMac,'h3cRprMacLearnType':h3cRprMacLearnType,'h3cRprMacLearnDestMac':h3cRprMacLearnDestMac,'h3cRprMacLearnVlanId':h3cRprMacLearnVlanId,'h3cRprMacLearnRinglet':h3cRprMacLearnRinglet,'h3cRprMacLearnTtl':h3cRprMacLearnTtl,'h3cRprMacLearnIsValid':h3cRprMacLearnIsValid,'h3cRprMacLearnRowStatus':h3cRprMacLearnRowStatus,'h3cRprTrapVar':h3cRprTrapVar,'h3cRprTrapVarTable':h3cRprTrapVarTable,'h3cRprTrapVarEntry':h3cRprTrapVarEntry,_E:h3cRprTrapIfIndex,_G:h3cRprTrapRinglet,_n:h3cRprTrapTopoMacAddress,_o:h3cRprTrapIpAddress,'h3cRprTrap':h3cRprTrap,'h3cRprTopologyOpenRing':h3cRprTopologyOpenRing,'h3cRprTopologyCloseRing':h3cRprTopologyCloseRing,'h3cRprTopologyInconsistent':h3cRprTopologyInconsistent,'h3cRprTopologyInstability':h3cRprTopologyInstability,'h3cRprDuplicateMacAddress':h3cRprDuplicateMacAddress,'h3cRprDulplicateIPAddress':h3cRprDulplicateIPAddress,'h3cRprIncompleteLRTT':h3cRprIncompleteLRTT,'h3cRprProtecConfigInconsistent':h3cRprProtecConfigInconsistent,'h3cRprJumboConfigInconsistent':h3cRprJumboConfigInconsistent,'h3cRprExceedMaxReservRate':h3cRprExceedMaxReservRate,'h3cRprExceedMaxStationNum':h3cRprExceedMaxStationNum,'h3cRprMiscabling':h3cRprMiscabling,'h3cRprBackPressure':h3cRprBackPressure,'h3cRprBackPressureOver':h3cRprBackPressureOver})