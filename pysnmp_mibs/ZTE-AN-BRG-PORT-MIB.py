_b='zxAnBrgVirtualMacVid'
_a='zxAnBrgPortIpv6IpBindIp'
_Z='zxAnBrgPortFilterMac'
_Y='zxAnBrgPortStaticMac'
_X='zxAnBrgPortStaticHostIp'
_W='aoeAal0'
_V='modemMgmt'
_U='ipoaVcmux'
_T='ipoaLlc'
_S='pppoaVcmux'
_R='pppoaLlc'
_Q='eoaVcmux'
_P='eoaLlc'
_O='disabled'
_N='enabled'
_M='read-write'
_L='read-only'
_K='not-accessible'
_J='zxAnBrgUsrPortId'
_I='ifIndex'
_H='IF-MIB'
_G='pps'
_F='disable'
_E='enable'
_D='ZTE-AN-BRG-PORT-MIB'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifAdminStatus,ifIndex,ifOperStatus,ifType=mibBuilder.importSymbols(_H,'ifAdminStatus',_I,'ifOperStatus','ifType')
InetAddress,InetAddressPrefixLength=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressPrefixLength')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
ZxAnIdList,ZxAnIfindex,ZxAnPortList,zxAn=mibBuilder.importSymbols('ZTE-AN-TC-MIB','ZxAnIdList','ZxAnIfindex','ZxAnPortList','zxAn')
zxAnBrgPortMib=ModuleIdentity((1,3,6,1,4,1,3902,1015,5))
_ZxAnBrgPortObjects_ObjectIdentity=ObjectIdentity
zxAnBrgPortObjects=_ZxAnBrgPortObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,5,1))
_ZxAnBrgUsrSidePortTable_Object=MibTable
zxAnBrgUsrSidePortTable=_ZxAnBrgUsrSidePortTable_Object((1,3,6,1,4,1,3902,1015,5,1,1))
if mibBuilder.loadTexts:zxAnBrgUsrSidePortTable.setStatus(_A)
_ZxAnBrgUsrSidePortEntry_Object=MibTableRow
zxAnBrgUsrSidePortEntry=_ZxAnBrgUsrSidePortEntry_Object((1,3,6,1,4,1,3902,1015,5,1,1,1))
zxAnBrgUsrSidePortEntry.setIndexNames((0,_H,_I),(0,_D,_J))
if mibBuilder.loadTexts:zxAnBrgUsrSidePortEntry.setStatus(_A)
_ZxAnBrgUsrPortId_Type=Integer32
_ZxAnBrgUsrPortId_Object=MibTableColumn
zxAnBrgUsrPortId=_ZxAnBrgUsrPortId_Object((1,3,6,1,4,1,3902,1015,5,1,1,1,1),_ZxAnBrgUsrPortId_Type())
zxAnBrgUsrPortId.setMaxAccess(_K)
if mibBuilder.loadTexts:zxAnBrgUsrPortId.setStatus(_A)
class _ZxAnBrgUsrPortAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_ZxAnBrgUsrPortAdminStatus_Type.__name__=_C
_ZxAnBrgUsrPortAdminStatus_Object=MibTableColumn
zxAnBrgUsrPortAdminStatus=_ZxAnBrgUsrPortAdminStatus_Object((1,3,6,1,4,1,3902,1015,5,1,1,1,2),_ZxAnBrgUsrPortAdminStatus_Type())
zxAnBrgUsrPortAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBrgUsrPortAdminStatus.setStatus(_A)
_ZxAnBrgUsrPortPvcVpi_Type=Integer32
_ZxAnBrgUsrPortPvcVpi_Object=MibTableColumn
zxAnBrgUsrPortPvcVpi=_ZxAnBrgUsrPortPvcVpi_Object((1,3,6,1,4,1,3902,1015,5,1,1,1,3),_ZxAnBrgUsrPortPvcVpi_Type())
zxAnBrgUsrPortPvcVpi.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBrgUsrPortPvcVpi.setStatus(_A)
_ZxAnBrgUsrPortPvcVci_Type=Integer32
_ZxAnBrgUsrPortPvcVci_Object=MibTableColumn
zxAnBrgUsrPortPvcVci=_ZxAnBrgUsrPortPvcVci_Object((1,3,6,1,4,1,3902,1015,5,1,1,1,4),_ZxAnBrgUsrPortPvcVci_Type())
zxAnBrgUsrPortPvcVci.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBrgUsrPortPvcVci.setStatus(_A)
class _ZxAnBrgUsrPortBindIpEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_ZxAnBrgUsrPortBindIpEnable_Type.__name__=_C
_ZxAnBrgUsrPortBindIpEnable_Object=MibTableColumn
zxAnBrgUsrPortBindIpEnable=_ZxAnBrgUsrPortBindIpEnable_Object((1,3,6,1,4,1,3902,1015,5,1,1,1,5),_ZxAnBrgUsrPortBindIpEnable_Type())
zxAnBrgUsrPortBindIpEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBrgUsrPortBindIpEnable.setStatus(_A)
class _ZxAnBrgUsrPortBindMacEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_ZxAnBrgUsrPortBindMacEnable_Type.__name__=_C
_ZxAnBrgUsrPortBindMacEnable_Object=MibTableColumn
zxAnBrgUsrPortBindMacEnable=_ZxAnBrgUsrPortBindMacEnable_Object((1,3,6,1,4,1,3902,1015,5,1,1,1,6),_ZxAnBrgUsrPortBindMacEnable_Type())
zxAnBrgUsrPortBindMacEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBrgUsrPortBindMacEnable.setStatus(_A)
class _ZxAnBrgUsrPortMacLearnLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_ZxAnBrgUsrPortMacLearnLimit_Type.__name__=_C
_ZxAnBrgUsrPortMacLearnLimit_Object=MibTableColumn
zxAnBrgUsrPortMacLearnLimit=_ZxAnBrgUsrPortMacLearnLimit_Object((1,3,6,1,4,1,3902,1015,5,1,1,1,7),_ZxAnBrgUsrPortMacLearnLimit_Type())
zxAnBrgUsrPortMacLearnLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBrgUsrPortMacLearnLimit.setStatus(_A)
_ZxAnBrgUsrPortMaxMacLearn_Type=Integer32
_ZxAnBrgUsrPortMaxMacLearn_Object=MibTableColumn
zxAnBrgUsrPortMaxMacLearn=_ZxAnBrgUsrPortMaxMacLearn_Object((1,3,6,1,4,1,3902,1015,5,1,1,1,8),_ZxAnBrgUsrPortMaxMacLearn_Type())
zxAnBrgUsrPortMaxMacLearn.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBrgUsrPortMaxMacLearn.setStatus(_A)
if mibBuilder.loadTexts:zxAnBrgUsrPortMaxMacLearn.setUnits('package')
class _ZxAnBrgUsrPortBrdcastRateLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_ZxAnBrgUsrPortBrdcastRateLimit_Type.__name__=_C
_ZxAnBrgUsrPortBrdcastRateLimit_Object=MibTableColumn
zxAnBrgUsrPortBrdcastRateLimit=_ZxAnBrgUsrPortBrdcastRateLimit_Object((1,3,6,1,4,1,3902,1015,5,1,1,1,9),_ZxAnBrgUsrPortBrdcastRateLimit_Type())
zxAnBrgUsrPortBrdcastRateLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBrgUsrPortBrdcastRateLimit.setStatus(_A)
_ZxAnBrgUsrPortMaxBroadcastRate_Type=Integer32
_ZxAnBrgUsrPortMaxBroadcastRate_Object=MibTableColumn
zxAnBrgUsrPortMaxBroadcastRate=_ZxAnBrgUsrPortMaxBroadcastRate_Object((1,3,6,1,4,1,3902,1015,5,1,1,1,10),_ZxAnBrgUsrPortMaxBroadcastRate_Type())
zxAnBrgUsrPortMaxBroadcastRate.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBrgUsrPortMaxBroadcastRate.setStatus(_A)
if mibBuilder.loadTexts:zxAnBrgUsrPortMaxBroadcastRate.setUnits(_G)
class _ZxAnBrgUsrPortDhcpRateLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_ZxAnBrgUsrPortDhcpRateLimit_Type.__name__=_C
_ZxAnBrgUsrPortDhcpRateLimit_Object=MibTableColumn
zxAnBrgUsrPortDhcpRateLimit=_ZxAnBrgUsrPortDhcpRateLimit_Object((1,3,6,1,4,1,3902,1015,5,1,1,1,11),_ZxAnBrgUsrPortDhcpRateLimit_Type())
zxAnBrgUsrPortDhcpRateLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBrgUsrPortDhcpRateLimit.setStatus(_A)
_ZxAnBrgUsrPortMaxDhcpRate_Type=Integer32
_ZxAnBrgUsrPortMaxDhcpRate_Object=MibTableColumn
zxAnBrgUsrPortMaxDhcpRate=_ZxAnBrgUsrPortMaxDhcpRate_Object((1,3,6,1,4,1,3902,1015,5,1,1,1,12),_ZxAnBrgUsrPortMaxDhcpRate_Type())
zxAnBrgUsrPortMaxDhcpRate.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBrgUsrPortMaxDhcpRate.setStatus(_A)
if mibBuilder.loadTexts:zxAnBrgUsrPortMaxDhcpRate.setUnits(_G)
class _ZxAnBrgUsrPortIgmpRateLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_ZxAnBrgUsrPortIgmpRateLimit_Type.__name__=_C
_ZxAnBrgUsrPortIgmpRateLimit_Object=MibTableColumn
zxAnBrgUsrPortIgmpRateLimit=_ZxAnBrgUsrPortIgmpRateLimit_Object((1,3,6,1,4,1,3902,1015,5,1,1,1,13),_ZxAnBrgUsrPortIgmpRateLimit_Type())
zxAnBrgUsrPortIgmpRateLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBrgUsrPortIgmpRateLimit.setStatus(_A)
_ZxAnBrgUsrPortMaxIgmpRate_Type=Integer32
_ZxAnBrgUsrPortMaxIgmpRate_Object=MibTableColumn
zxAnBrgUsrPortMaxIgmpRate=_ZxAnBrgUsrPortMaxIgmpRate_Object((1,3,6,1,4,1,3902,1015,5,1,1,1,14),_ZxAnBrgUsrPortMaxIgmpRate_Type())
zxAnBrgUsrPortMaxIgmpRate.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBrgUsrPortMaxIgmpRate.setStatus(_A)
if mibBuilder.loadTexts:zxAnBrgUsrPortMaxIgmpRate.setUnits(_G)
class _ZxAnBrgUsrPortEncapsType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_P,1),(_Q,2),(_R,3),(_S,4),(_T,5),(_U,6),('aoe',7),(_V,8),('auto',9),(_W,10)))
_ZxAnBrgUsrPortEncapsType_Type.__name__=_C
_ZxAnBrgUsrPortEncapsType_Object=MibTableColumn
zxAnBrgUsrPortEncapsType=_ZxAnBrgUsrPortEncapsType_Object((1,3,6,1,4,1,3902,1015,5,1,1,1,15),_ZxAnBrgUsrPortEncapsType_Type())
zxAnBrgUsrPortEncapsType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBrgUsrPortEncapsType.setStatus(_A)
class _ZxAnBrgUserPortBrdcastEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_ZxAnBrgUserPortBrdcastEnable_Type.__name__=_C
_ZxAnBrgUserPortBrdcastEnable_Object=MibTableColumn
zxAnBrgUserPortBrdcastEnable=_ZxAnBrgUserPortBrdcastEnable_Object((1,3,6,1,4,1,3902,1015,5,1,1,1,16),_ZxAnBrgUserPortBrdcastEnable_Type())
zxAnBrgUserPortBrdcastEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBrgUserPortBrdcastEnable.setStatus(_A)
class _ZxAnBrgUserPortFloodEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_ZxAnBrgUserPortFloodEnable_Type.__name__=_C
_ZxAnBrgUserPortFloodEnable_Object=MibTableColumn
zxAnBrgUserPortFloodEnable=_ZxAnBrgUserPortFloodEnable_Object((1,3,6,1,4,1,3902,1015,5,1,1,1,17),_ZxAnBrgUserPortFloodEnable_Type())
zxAnBrgUserPortFloodEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBrgUserPortFloodEnable.setStatus(_A)
class _ZxAnBrgUserPortActualEncapsType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_P,1),(_Q,2),(_R,3),(_S,4),(_T,5),(_U,6),('aoe',7),(_V,8),('unknown',9),(_W,10)))
_ZxAnBrgUserPortActualEncapsType_Type.__name__=_C
_ZxAnBrgUserPortActualEncapsType_Object=MibTableColumn
zxAnBrgUserPortActualEncapsType=_ZxAnBrgUserPortActualEncapsType_Object((1,3,6,1,4,1,3902,1015,5,1,1,1,18),_ZxAnBrgUserPortActualEncapsType_Type())
zxAnBrgUserPortActualEncapsType.setMaxAccess(_L)
if mibBuilder.loadTexts:zxAnBrgUserPortActualEncapsType.setStatus(_A)
class _ZxAnBrgUserPortVirtualMacEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_ZxAnBrgUserPortVirtualMacEnable_Type.__name__=_C
_ZxAnBrgUserPortVirtualMacEnable_Object=MibTableColumn
zxAnBrgUserPortVirtualMacEnable=_ZxAnBrgUserPortVirtualMacEnable_Object((1,3,6,1,4,1,3902,1015,5,1,1,1,19),_ZxAnBrgUserPortVirtualMacEnable_Type())
zxAnBrgUserPortVirtualMacEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBrgUserPortVirtualMacEnable.setStatus(_A)
_ZxAnBrgUserPortTxNetDataRate_Type=Integer32
_ZxAnBrgUserPortTxNetDataRate_Object=MibTableColumn
zxAnBrgUserPortTxNetDataRate=_ZxAnBrgUserPortTxNetDataRate_Object((1,3,6,1,4,1,3902,1015,5,1,1,1,20),_ZxAnBrgUserPortTxNetDataRate_Type())
zxAnBrgUserPortTxNetDataRate.setMaxAccess(_L)
if mibBuilder.loadTexts:zxAnBrgUserPortTxNetDataRate.setStatus(_A)
if mibBuilder.loadTexts:zxAnBrgUserPortTxNetDataRate.setUnits('kbps')
_ZxAnBrgUserPortRxNetDataRate_Type=Integer32
_ZxAnBrgUserPortRxNetDataRate_Object=MibTableColumn
zxAnBrgUserPortRxNetDataRate=_ZxAnBrgUserPortRxNetDataRate_Object((1,3,6,1,4,1,3902,1015,5,1,1,1,21),_ZxAnBrgUserPortRxNetDataRate_Type())
zxAnBrgUserPortRxNetDataRate.setMaxAccess(_L)
if mibBuilder.loadTexts:zxAnBrgUserPortRxNetDataRate.setStatus(_A)
if mibBuilder.loadTexts:zxAnBrgUserPortRxNetDataRate.setUnits('kbps')
class _ZxAnBrgUsrPortPppoeRateLimit_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_ZxAnBrgUsrPortPppoeRateLimit_Type.__name__=_C
_ZxAnBrgUsrPortPppoeRateLimit_Object=MibTableColumn
zxAnBrgUsrPortPppoeRateLimit=_ZxAnBrgUsrPortPppoeRateLimit_Object((1,3,6,1,4,1,3902,1015,5,1,1,1,22),_ZxAnBrgUsrPortPppoeRateLimit_Type())
zxAnBrgUsrPortPppoeRateLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBrgUsrPortPppoeRateLimit.setStatus(_A)
class _ZxAnBrgUsrPortMaxPppoeRate_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ZxAnBrgUsrPortMaxPppoeRate_Type.__name__=_C
_ZxAnBrgUsrPortMaxPppoeRate_Object=MibTableColumn
zxAnBrgUsrPortMaxPppoeRate=_ZxAnBrgUsrPortMaxPppoeRate_Object((1,3,6,1,4,1,3902,1015,5,1,1,1,23),_ZxAnBrgUsrPortMaxPppoeRate_Type())
zxAnBrgUsrPortMaxPppoeRate.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBrgUsrPortMaxPppoeRate.setStatus(_A)
if mibBuilder.loadTexts:zxAnBrgUsrPortMaxPppoeRate.setUnits(_G)
_ZxAnBrgUsrPortRowStatus_Type=RowStatus
_ZxAnBrgUsrPortRowStatus_Object=MibTableColumn
zxAnBrgUsrPortRowStatus=_ZxAnBrgUsrPortRowStatus_Object((1,3,6,1,4,1,3902,1015,5,1,1,1,50),_ZxAnBrgUsrPortRowStatus_Type())
zxAnBrgUsrPortRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBrgUsrPortRowStatus.setStatus(_A)
_ZxAnBrgPortStaticHostTable_Object=MibTable
zxAnBrgPortStaticHostTable=_ZxAnBrgPortStaticHostTable_Object((1,3,6,1,4,1,3902,1015,5,1,2))
if mibBuilder.loadTexts:zxAnBrgPortStaticHostTable.setStatus(_A)
_ZxAnBrgPortStaticHostEntry_Object=MibTableRow
zxAnBrgPortStaticHostEntry=_ZxAnBrgPortStaticHostEntry_Object((1,3,6,1,4,1,3902,1015,5,1,2,1))
zxAnBrgPortStaticHostEntry.setIndexNames((0,_H,_I),(0,_D,_J),(0,_D,_X))
if mibBuilder.loadTexts:zxAnBrgPortStaticHostEntry.setStatus(_A)
_ZxAnBrgPortStaticHostIp_Type=IpAddress
_ZxAnBrgPortStaticHostIp_Object=MibTableColumn
zxAnBrgPortStaticHostIp=_ZxAnBrgPortStaticHostIp_Object((1,3,6,1,4,1,3902,1015,5,1,2,1,1),_ZxAnBrgPortStaticHostIp_Type())
zxAnBrgPortStaticHostIp.setMaxAccess(_K)
if mibBuilder.loadTexts:zxAnBrgPortStaticHostIp.setStatus(_A)
_ZxAnBrgPortStaticHostRowStatus_Type=RowStatus
_ZxAnBrgPortStaticHostRowStatus_Object=MibTableColumn
zxAnBrgPortStaticHostRowStatus=_ZxAnBrgPortStaticHostRowStatus_Object((1,3,6,1,4,1,3902,1015,5,1,2,1,2),_ZxAnBrgPortStaticHostRowStatus_Type())
zxAnBrgPortStaticHostRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBrgPortStaticHostRowStatus.setStatus(_A)
_ZxAnBrgPortStaticMacTable_Object=MibTable
zxAnBrgPortStaticMacTable=_ZxAnBrgPortStaticMacTable_Object((1,3,6,1,4,1,3902,1015,5,1,3))
if mibBuilder.loadTexts:zxAnBrgPortStaticMacTable.setStatus(_A)
_ZxAnBrgPortStaticMacEntry_Object=MibTableRow
zxAnBrgPortStaticMacEntry=_ZxAnBrgPortStaticMacEntry_Object((1,3,6,1,4,1,3902,1015,5,1,3,1))
zxAnBrgPortStaticMacEntry.setIndexNames((0,_H,_I),(0,_D,_J),(0,_D,_Y))
if mibBuilder.loadTexts:zxAnBrgPortStaticMacEntry.setStatus(_A)
_ZxAnBrgPortStaticMac_Type=MacAddress
_ZxAnBrgPortStaticMac_Object=MibTableColumn
zxAnBrgPortStaticMac=_ZxAnBrgPortStaticMac_Object((1,3,6,1,4,1,3902,1015,5,1,3,1,1),_ZxAnBrgPortStaticMac_Type())
zxAnBrgPortStaticMac.setMaxAccess(_K)
if mibBuilder.loadTexts:zxAnBrgPortStaticMac.setStatus(_A)
_ZxAnSecIfMacBindingRowStatus_Type=RowStatus
_ZxAnSecIfMacBindingRowStatus_Object=MibTableColumn
zxAnSecIfMacBindingRowStatus=_ZxAnSecIfMacBindingRowStatus_Object((1,3,6,1,4,1,3902,1015,5,1,3,1,2),_ZxAnSecIfMacBindingRowStatus_Type())
zxAnSecIfMacBindingRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnSecIfMacBindingRowStatus.setStatus(_A)
_ZxAnBrgPortFilterMacTable_Object=MibTable
zxAnBrgPortFilterMacTable=_ZxAnBrgPortFilterMacTable_Object((1,3,6,1,4,1,3902,1015,5,1,4))
if mibBuilder.loadTexts:zxAnBrgPortFilterMacTable.setStatus(_A)
_ZxAnBrgPortFilterMacEntry_Object=MibTableRow
zxAnBrgPortFilterMacEntry=_ZxAnBrgPortFilterMacEntry_Object((1,3,6,1,4,1,3902,1015,5,1,4,1))
zxAnBrgPortFilterMacEntry.setIndexNames((0,_H,_I),(0,_D,_J),(0,_D,_Z))
if mibBuilder.loadTexts:zxAnBrgPortFilterMacEntry.setStatus(_A)
_ZxAnBrgPortFilterMac_Type=MacAddress
_ZxAnBrgPortFilterMac_Object=MibTableColumn
zxAnBrgPortFilterMac=_ZxAnBrgPortFilterMac_Object((1,3,6,1,4,1,3902,1015,5,1,4,1,1),_ZxAnBrgPortFilterMac_Type())
zxAnBrgPortFilterMac.setMaxAccess(_K)
if mibBuilder.loadTexts:zxAnBrgPortFilterMac.setStatus(_A)
_ZxAnSecIfMacFilterRowStatus_Type=RowStatus
_ZxAnSecIfMacFilterRowStatus_Object=MibTableColumn
zxAnSecIfMacFilterRowStatus=_ZxAnSecIfMacFilterRowStatus_Object((1,3,6,1,4,1,3902,1015,5,1,4,1,2),_ZxAnSecIfMacFilterRowStatus_Type())
zxAnSecIfMacFilterRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnSecIfMacFilterRowStatus.setStatus(_A)
_ZxAnBrgPortIpv6Objects_ObjectIdentity=ObjectIdentity
zxAnBrgPortIpv6Objects=_ZxAnBrgPortIpv6Objects_ObjectIdentity((1,3,6,1,4,1,3902,1015,5,1,10))
_ZxAnBrgPortIpv6IpBindTable_Object=MibTable
zxAnBrgPortIpv6IpBindTable=_ZxAnBrgPortIpv6IpBindTable_Object((1,3,6,1,4,1,3902,1015,5,1,10,1))
if mibBuilder.loadTexts:zxAnBrgPortIpv6IpBindTable.setStatus(_A)
_ZxAnBrgPortIpv6IpBindEntry_Object=MibTableRow
zxAnBrgPortIpv6IpBindEntry=_ZxAnBrgPortIpv6IpBindEntry_Object((1,3,6,1,4,1,3902,1015,5,1,10,1,1))
zxAnBrgPortIpv6IpBindEntry.setIndexNames((0,_H,_I),(0,_D,_J),(0,_D,_a))
if mibBuilder.loadTexts:zxAnBrgPortIpv6IpBindEntry.setStatus(_A)
_ZxAnBrgPortIpv6IpBindIp_Type=InetAddress
_ZxAnBrgPortIpv6IpBindIp_Object=MibTableColumn
zxAnBrgPortIpv6IpBindIp=_ZxAnBrgPortIpv6IpBindIp_Object((1,3,6,1,4,1,3902,1015,5,1,10,1,1,1),_ZxAnBrgPortIpv6IpBindIp_Type())
zxAnBrgPortIpv6IpBindIp.setMaxAccess(_K)
if mibBuilder.loadTexts:zxAnBrgPortIpv6IpBindIp.setStatus(_A)
_ZxAnBrgPortIpv6IpBindIpPfxLen_Type=InetAddressPrefixLength
_ZxAnBrgPortIpv6IpBindIpPfxLen_Object=MibTableColumn
zxAnBrgPortIpv6IpBindIpPfxLen=_ZxAnBrgPortIpv6IpBindIpPfxLen_Object((1,3,6,1,4,1,3902,1015,5,1,10,1,1,2),_ZxAnBrgPortIpv6IpBindIpPfxLen_Type())
zxAnBrgPortIpv6IpBindIpPfxLen.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBrgPortIpv6IpBindIpPfxLen.setStatus(_A)
_ZxAnBrgPortIpv6IpBindRowStatus_Type=RowStatus
_ZxAnBrgPortIpv6IpBindRowStatus_Object=MibTableColumn
zxAnBrgPortIpv6IpBindRowStatus=_ZxAnBrgPortIpv6IpBindRowStatus_Object((1,3,6,1,4,1,3902,1015,5,1,10,1,1,10),_ZxAnBrgPortIpv6IpBindRowStatus_Type())
zxAnBrgPortIpv6IpBindRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBrgPortIpv6IpBindRowStatus.setStatus(_A)
_ZxAnBrgPortStatsObjects_ObjectIdentity=ObjectIdentity
zxAnBrgPortStatsObjects=_ZxAnBrgPortStatsObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,5,1,11))
_ZxAnBrgPortStatsTable_Object=MibTable
zxAnBrgPortStatsTable=_ZxAnBrgPortStatsTable_Object((1,3,6,1,4,1,3902,1015,5,1,11,2))
if mibBuilder.loadTexts:zxAnBrgPortStatsTable.setStatus(_A)
_ZxAnBrgPortStatsEntry_Object=MibTableRow
zxAnBrgPortStatsEntry=_ZxAnBrgPortStatsEntry_Object((1,3,6,1,4,1,3902,1015,5,1,11,2,1))
zxAnBrgPortStatsEntry.setIndexNames((0,_H,_I),(0,_D,_J))
if mibBuilder.loadTexts:zxAnBrgPortStatsEntry.setStatus(_A)
_ZxAnBrgPortInDiscards_Type=Counter64
_ZxAnBrgPortInDiscards_Object=MibTableColumn
zxAnBrgPortInDiscards=_ZxAnBrgPortInDiscards_Object((1,3,6,1,4,1,3902,1015,5,1,11,2,1,1),_ZxAnBrgPortInDiscards_Type())
zxAnBrgPortInDiscards.setMaxAccess(_L)
if mibBuilder.loadTexts:zxAnBrgPortInDiscards.setStatus(_A)
_ZxAnBrgPortOutDiscards_Type=Counter64
_ZxAnBrgPortOutDiscards_Object=MibTableColumn
zxAnBrgPortOutDiscards=_ZxAnBrgPortOutDiscards_Object((1,3,6,1,4,1,3902,1015,5,1,11,2,1,2),_ZxAnBrgPortOutDiscards_Type())
zxAnBrgPortOutDiscards.setMaxAccess(_L)
if mibBuilder.loadTexts:zxAnBrgPortOutDiscards.setStatus(_A)
_ZxAnBrgVirtualMacObjects_ObjectIdentity=ObjectIdentity
zxAnBrgVirtualMacObjects=_ZxAnBrgVirtualMacObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,5,1,12))
_ZxAnBrgVirtualMacVlanTable_Object=MibTable
zxAnBrgVirtualMacVlanTable=_ZxAnBrgVirtualMacVlanTable_Object((1,3,6,1,4,1,3902,1015,5,1,12,2))
if mibBuilder.loadTexts:zxAnBrgVirtualMacVlanTable.setStatus(_A)
_ZxAnBrgVirtualMacVlanEntry_Object=MibTableRow
zxAnBrgVirtualMacVlanEntry=_ZxAnBrgVirtualMacVlanEntry_Object((1,3,6,1,4,1,3902,1015,5,1,12,2,1))
zxAnBrgVirtualMacVlanEntry.setIndexNames((0,_D,_b))
if mibBuilder.loadTexts:zxAnBrgVirtualMacVlanEntry.setStatus(_A)
class _ZxAnBrgVirtualMacVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_ZxAnBrgVirtualMacVid_Type.__name__=_C
_ZxAnBrgVirtualMacVid_Object=MibTableColumn
zxAnBrgVirtualMacVid=_ZxAnBrgVirtualMacVid_Object((1,3,6,1,4,1,3902,1015,5,1,12,2,1,1),_ZxAnBrgVirtualMacVid_Type())
zxAnBrgVirtualMacVid.setMaxAccess(_K)
if mibBuilder.loadTexts:zxAnBrgVirtualMacVid.setStatus(_A)
_ZxAnBrgVirtualMacVlanRowStatus_Type=RowStatus
_ZxAnBrgVirtualMacVlanRowStatus_Object=MibTableColumn
zxAnBrgVirtualMacVlanRowStatus=_ZxAnBrgVirtualMacVlanRowStatus_Object((1,3,6,1,4,1,3902,1015,5,1,12,2,1,50),_ZxAnBrgVirtualMacVlanRowStatus_Type())
zxAnBrgVirtualMacVlanRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBrgVirtualMacVlanRowStatus.setStatus(_A)
_ZxAnBrgPortGlobalObjects_ObjectIdentity=ObjectIdentity
zxAnBrgPortGlobalObjects=_ZxAnBrgPortGlobalObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,5,2))
_ZxAnBrgPktRateLimit_ObjectIdentity=ObjectIdentity
zxAnBrgPktRateLimit=_ZxAnBrgPktRateLimit_ObjectIdentity((1,3,6,1,4,1,3902,1015,5,2,1))
class _ZxAnBrgBroadcastRateLimit_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ZxAnBrgBroadcastRateLimit_Type.__name__=_C
_ZxAnBrgBroadcastRateLimit_Object=MibScalar
zxAnBrgBroadcastRateLimit=_ZxAnBrgBroadcastRateLimit_Object((1,3,6,1,4,1,3902,1015,5,2,1,1),_ZxAnBrgBroadcastRateLimit_Type())
zxAnBrgBroadcastRateLimit.setMaxAccess(_M)
if mibBuilder.loadTexts:zxAnBrgBroadcastRateLimit.setStatus(_A)
if mibBuilder.loadTexts:zxAnBrgBroadcastRateLimit.setUnits(_G)
class _ZxAnBrgMulticastRateLimit_Type(Integer32):defaultValue=65535;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ZxAnBrgMulticastRateLimit_Type.__name__=_C
_ZxAnBrgMulticastRateLimit_Object=MibScalar
zxAnBrgMulticastRateLimit=_ZxAnBrgMulticastRateLimit_Object((1,3,6,1,4,1,3902,1015,5,2,1,2),_ZxAnBrgMulticastRateLimit_Type())
zxAnBrgMulticastRateLimit.setMaxAccess(_M)
if mibBuilder.loadTexts:zxAnBrgMulticastRateLimit.setStatus(_A)
if mibBuilder.loadTexts:zxAnBrgMulticastRateLimit.setUnits(_G)
class _ZxAnBrgFloodingRateLimit_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ZxAnBrgFloodingRateLimit_Type.__name__=_C
_ZxAnBrgFloodingRateLimit_Object=MibScalar
zxAnBrgFloodingRateLimit=_ZxAnBrgFloodingRateLimit_Object((1,3,6,1,4,1,3902,1015,5,2,1,3),_ZxAnBrgFloodingRateLimit_Type())
zxAnBrgFloodingRateLimit.setMaxAccess(_M)
if mibBuilder.loadTexts:zxAnBrgFloodingRateLimit.setStatus(_A)
if mibBuilder.loadTexts:zxAnBrgFloodingRateLimit.setUnits(_G)
class _ZxAnBrgBpduFloodingRateLimit_Type(Integer32):defaultValue=65535;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ZxAnBrgBpduFloodingRateLimit_Type.__name__=_C
_ZxAnBrgBpduFloodingRateLimit_Object=MibScalar
zxAnBrgBpduFloodingRateLimit=_ZxAnBrgBpduFloodingRateLimit_Object((1,3,6,1,4,1,3902,1015,5,2,1,4),_ZxAnBrgBpduFloodingRateLimit_Type())
zxAnBrgBpduFloodingRateLimit.setMaxAccess(_M)
if mibBuilder.loadTexts:zxAnBrgBpduFloodingRateLimit.setStatus(_A)
if mibBuilder.loadTexts:zxAnBrgBpduFloodingRateLimit.setUnits(_G)
class _ZxAnBrgUnknownUcastFloodingEn_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_ZxAnBrgUnknownUcastFloodingEn_Type.__name__=_C
_ZxAnBrgUnknownUcastFloodingEn_Object=MibScalar
zxAnBrgUnknownUcastFloodingEn=_ZxAnBrgUnknownUcastFloodingEn_Object((1,3,6,1,4,1,3902,1015,5,2,1,5),_ZxAnBrgUnknownUcastFloodingEn_Type())
zxAnBrgUnknownUcastFloodingEn.setMaxAccess(_M)
if mibBuilder.loadTexts:zxAnBrgUnknownUcastFloodingEn.setStatus(_A)
class _ZxAnBrgUnknownMcastFloodingEn_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_ZxAnBrgUnknownMcastFloodingEn_Type.__name__=_C
_ZxAnBrgUnknownMcastFloodingEn_Object=MibScalar
zxAnBrgUnknownMcastFloodingEn=_ZxAnBrgUnknownMcastFloodingEn_Object((1,3,6,1,4,1,3902,1015,5,2,1,6),_ZxAnBrgUnknownMcastFloodingEn_Type())
zxAnBrgUnknownMcastFloodingEn.setMaxAccess(_M)
if mibBuilder.loadTexts:zxAnBrgUnknownMcastFloodingEn.setStatus(_A)
_ZxAnBrgVirtualMac_ObjectIdentity=ObjectIdentity
zxAnBrgVirtualMac=_ZxAnBrgVirtualMac_ObjectIdentity((1,3,6,1,4,1,3902,1015,5,2,2))
class _ZxAnBrgVirtualMacKey_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ZxAnBrgVirtualMacKey_Type.__name__=_C
_ZxAnBrgVirtualMacKey_Object=MibScalar
zxAnBrgVirtualMacKey=_ZxAnBrgVirtualMacKey_Object((1,3,6,1,4,1,3902,1015,5,2,2,1),_ZxAnBrgVirtualMacKey_Type())
zxAnBrgVirtualMacKey.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBrgVirtualMacKey.setStatus(_A)
class _ZxAnBrgVirtualMacFormat_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('tpsa',1),('magyarTel',2)))
_ZxAnBrgVirtualMacFormat_Type.__name__=_C
_ZxAnBrgVirtualMacFormat_Object=MibScalar
zxAnBrgVirtualMacFormat=_ZxAnBrgVirtualMacFormat_Object((1,3,6,1,4,1,3902,1015,5,2,2,2),_ZxAnBrgVirtualMacFormat_Type())
zxAnBrgVirtualMacFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBrgVirtualMacFormat.setStatus(_A)
class _ZxAnBrgVirtualMacUserDefined_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_ZxAnBrgVirtualMacUserDefined_Type.__name__=_C
_ZxAnBrgVirtualMacUserDefined_Object=MibScalar
zxAnBrgVirtualMacUserDefined=_ZxAnBrgVirtualMacUserDefined_Object((1,3,6,1,4,1,3902,1015,5,2,2,3),_ZxAnBrgVirtualMacUserDefined_Type())
zxAnBrgVirtualMacUserDefined.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBrgVirtualMacUserDefined.setStatus(_A)
class _ZxAnBrgPortCapabilities_Type(Bits):namedValues=NamedValues(*(('vdslAtmPtmCoexist',0),('shdslAtmEfmCoexist',1),('supportPppoeRateLimit',2)))
_ZxAnBrgPortCapabilities_Type.__name__='Bits'
_ZxAnBrgPortCapabilities_Object=MibScalar
zxAnBrgPortCapabilities=_ZxAnBrgPortCapabilities_Object((1,3,6,1,4,1,3902,1015,5,2,50),_ZxAnBrgPortCapabilities_Type())
zxAnBrgPortCapabilities.setMaxAccess(_L)
if mibBuilder.loadTexts:zxAnBrgPortCapabilities.setStatus(_A)
_ZxAnBrgPortTrapObjects_ObjectIdentity=ObjectIdentity
zxAnBrgPortTrapObjects=_ZxAnBrgPortTrapObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,5,3))
mibBuilder.exportSymbols(_D,**{'zxAnBrgPortMib':zxAnBrgPortMib,'zxAnBrgPortObjects':zxAnBrgPortObjects,'zxAnBrgUsrSidePortTable':zxAnBrgUsrSidePortTable,'zxAnBrgUsrSidePortEntry':zxAnBrgUsrSidePortEntry,_J:zxAnBrgUsrPortId,'zxAnBrgUsrPortAdminStatus':zxAnBrgUsrPortAdminStatus,'zxAnBrgUsrPortPvcVpi':zxAnBrgUsrPortPvcVpi,'zxAnBrgUsrPortPvcVci':zxAnBrgUsrPortPvcVci,'zxAnBrgUsrPortBindIpEnable':zxAnBrgUsrPortBindIpEnable,'zxAnBrgUsrPortBindMacEnable':zxAnBrgUsrPortBindMacEnable,'zxAnBrgUsrPortMacLearnLimit':zxAnBrgUsrPortMacLearnLimit,'zxAnBrgUsrPortMaxMacLearn':zxAnBrgUsrPortMaxMacLearn,'zxAnBrgUsrPortBrdcastRateLimit':zxAnBrgUsrPortBrdcastRateLimit,'zxAnBrgUsrPortMaxBroadcastRate':zxAnBrgUsrPortMaxBroadcastRate,'zxAnBrgUsrPortDhcpRateLimit':zxAnBrgUsrPortDhcpRateLimit,'zxAnBrgUsrPortMaxDhcpRate':zxAnBrgUsrPortMaxDhcpRate,'zxAnBrgUsrPortIgmpRateLimit':zxAnBrgUsrPortIgmpRateLimit,'zxAnBrgUsrPortMaxIgmpRate':zxAnBrgUsrPortMaxIgmpRate,'zxAnBrgUsrPortEncapsType':zxAnBrgUsrPortEncapsType,'zxAnBrgUserPortBrdcastEnable':zxAnBrgUserPortBrdcastEnable,'zxAnBrgUserPortFloodEnable':zxAnBrgUserPortFloodEnable,'zxAnBrgUserPortActualEncapsType':zxAnBrgUserPortActualEncapsType,'zxAnBrgUserPortVirtualMacEnable':zxAnBrgUserPortVirtualMacEnable,'zxAnBrgUserPortTxNetDataRate':zxAnBrgUserPortTxNetDataRate,'zxAnBrgUserPortRxNetDataRate':zxAnBrgUserPortRxNetDataRate,'zxAnBrgUsrPortPppoeRateLimit':zxAnBrgUsrPortPppoeRateLimit,'zxAnBrgUsrPortMaxPppoeRate':zxAnBrgUsrPortMaxPppoeRate,'zxAnBrgUsrPortRowStatus':zxAnBrgUsrPortRowStatus,'zxAnBrgPortStaticHostTable':zxAnBrgPortStaticHostTable,'zxAnBrgPortStaticHostEntry':zxAnBrgPortStaticHostEntry,_X:zxAnBrgPortStaticHostIp,'zxAnBrgPortStaticHostRowStatus':zxAnBrgPortStaticHostRowStatus,'zxAnBrgPortStaticMacTable':zxAnBrgPortStaticMacTable,'zxAnBrgPortStaticMacEntry':zxAnBrgPortStaticMacEntry,_Y:zxAnBrgPortStaticMac,'zxAnSecIfMacBindingRowStatus':zxAnSecIfMacBindingRowStatus,'zxAnBrgPortFilterMacTable':zxAnBrgPortFilterMacTable,'zxAnBrgPortFilterMacEntry':zxAnBrgPortFilterMacEntry,_Z:zxAnBrgPortFilterMac,'zxAnSecIfMacFilterRowStatus':zxAnSecIfMacFilterRowStatus,'zxAnBrgPortIpv6Objects':zxAnBrgPortIpv6Objects,'zxAnBrgPortIpv6IpBindTable':zxAnBrgPortIpv6IpBindTable,'zxAnBrgPortIpv6IpBindEntry':zxAnBrgPortIpv6IpBindEntry,_a:zxAnBrgPortIpv6IpBindIp,'zxAnBrgPortIpv6IpBindIpPfxLen':zxAnBrgPortIpv6IpBindIpPfxLen,'zxAnBrgPortIpv6IpBindRowStatus':zxAnBrgPortIpv6IpBindRowStatus,'zxAnBrgPortStatsObjects':zxAnBrgPortStatsObjects,'zxAnBrgPortStatsTable':zxAnBrgPortStatsTable,'zxAnBrgPortStatsEntry':zxAnBrgPortStatsEntry,'zxAnBrgPortInDiscards':zxAnBrgPortInDiscards,'zxAnBrgPortOutDiscards':zxAnBrgPortOutDiscards,'zxAnBrgVirtualMacObjects':zxAnBrgVirtualMacObjects,'zxAnBrgVirtualMacVlanTable':zxAnBrgVirtualMacVlanTable,'zxAnBrgVirtualMacVlanEntry':zxAnBrgVirtualMacVlanEntry,_b:zxAnBrgVirtualMacVid,'zxAnBrgVirtualMacVlanRowStatus':zxAnBrgVirtualMacVlanRowStatus,'zxAnBrgPortGlobalObjects':zxAnBrgPortGlobalObjects,'zxAnBrgPktRateLimit':zxAnBrgPktRateLimit,'zxAnBrgBroadcastRateLimit':zxAnBrgBroadcastRateLimit,'zxAnBrgMulticastRateLimit':zxAnBrgMulticastRateLimit,'zxAnBrgFloodingRateLimit':zxAnBrgFloodingRateLimit,'zxAnBrgBpduFloodingRateLimit':zxAnBrgBpduFloodingRateLimit,'zxAnBrgUnknownUcastFloodingEn':zxAnBrgUnknownUcastFloodingEn,'zxAnBrgUnknownMcastFloodingEn':zxAnBrgUnknownMcastFloodingEn,'zxAnBrgVirtualMac':zxAnBrgVirtualMac,'zxAnBrgVirtualMacKey':zxAnBrgVirtualMacKey,'zxAnBrgVirtualMacFormat':zxAnBrgVirtualMacFormat,'zxAnBrgVirtualMacUserDefined':zxAnBrgVirtualMacUserDefined,'zxAnBrgPortCapabilities':zxAnBrgPortCapabilities,'zxAnBrgPortTrapObjects':zxAnBrgPortTrapObjects})