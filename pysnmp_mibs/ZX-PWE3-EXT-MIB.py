_N='kbytes'
_M='not-accessible'
_L='zxPwe3ExtPwLabelIndex'
_K='zxPwe3ExtPwPsnType'
_J='read-only'
_I='ZX-PWE3-EXT-MIB'
_H='TruthValue'
_G='InetAddressType'
_F='zxPwIndex'
_E='ZXPW-STD-MIB'
_D='read-write'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress',_G)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_H)
zxAnCesMib,=mibBuilder.importSymbols('ZTE-MASTER-MIB','zxAnCesMib')
IANAPwPsnTypeTC,=mibBuilder.importSymbols('ZX-PWE3-MIB','IANAPwPsnTypeTC')
zxPwIndex,=mibBuilder.importSymbols(_E,_F)
zxPwe3ExtMib=ModuleIdentity((1,3,6,1,4,1,3902,1015,1013,21))
class PwVcIDType(TextualConvention,Unsigned32):status=_A
_ZxPwe3ExtObjects_ObjectIdentity=ObjectIdentity
zxPwe3ExtObjects=_ZxPwe3ExtObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,1013,21,1))
_ZxPwe3ExtGlobalObjects_ObjectIdentity=ObjectIdentity
zxPwe3ExtGlobalObjects=_ZxPwe3ExtGlobalObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,1013,21,1,1))
class _ZxPwe3ExtCesMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ces',1),('pwe3',2)))
_ZxPwe3ExtCesMode_Type.__name__=_C
_ZxPwe3ExtCesMode_Object=MibScalar
zxPwe3ExtCesMode=_ZxPwe3ExtCesMode_Object((1,3,6,1,4,1,3902,1015,1013,21,1,1,1),_ZxPwe3ExtCesMode_Type())
zxPwe3ExtCesMode.setMaxAccess(_D)
if mibBuilder.loadTexts:zxPwe3ExtCesMode.setStatus(_A)
class _ZxPwe3ExtCesIp1Type_Type(InetAddressType):defaultValue=1
_ZxPwe3ExtCesIp1Type_Type.__name__=_G
_ZxPwe3ExtCesIp1Type_Object=MibScalar
zxPwe3ExtCesIp1Type=_ZxPwe3ExtCesIp1Type_Object((1,3,6,1,4,1,3902,1015,1013,21,1,1,2),_ZxPwe3ExtCesIp1Type_Type())
zxPwe3ExtCesIp1Type.setMaxAccess(_D)
if mibBuilder.loadTexts:zxPwe3ExtCesIp1Type.setStatus(_A)
_ZxPwe3ExtCesIp1_Type=InetAddress
_ZxPwe3ExtCesIp1_Object=MibScalar
zxPwe3ExtCesIp1=_ZxPwe3ExtCesIp1_Object((1,3,6,1,4,1,3902,1015,1013,21,1,1,3),_ZxPwe3ExtCesIp1_Type())
zxPwe3ExtCesIp1.setMaxAccess(_D)
if mibBuilder.loadTexts:zxPwe3ExtCesIp1.setStatus(_A)
class _ZxPwe3ExtCesIp2Type_Type(InetAddressType):defaultValue=1
_ZxPwe3ExtCesIp2Type_Type.__name__=_G
_ZxPwe3ExtCesIp2Type_Object=MibScalar
zxPwe3ExtCesIp2Type=_ZxPwe3ExtCesIp2Type_Object((1,3,6,1,4,1,3902,1015,1013,21,1,1,4),_ZxPwe3ExtCesIp2Type_Type())
zxPwe3ExtCesIp2Type.setMaxAccess(_D)
if mibBuilder.loadTexts:zxPwe3ExtCesIp2Type.setStatus(_A)
_ZxPwe3ExtCesIp2_Type=InetAddress
_ZxPwe3ExtCesIp2_Object=MibScalar
zxPwe3ExtCesIp2=_ZxPwe3ExtCesIp2_Object((1,3,6,1,4,1,3902,1015,1013,21,1,1,5),_ZxPwe3ExtCesIp2_Type())
zxPwe3ExtCesIp2.setMaxAccess(_D)
if mibBuilder.loadTexts:zxPwe3ExtCesIp2.setStatus(_A)
_ZxPwe3ExtCesMac1_Type=MacAddress
_ZxPwe3ExtCesMac1_Object=MibScalar
zxPwe3ExtCesMac1=_ZxPwe3ExtCesMac1_Object((1,3,6,1,4,1,3902,1015,1013,21,1,1,6),_ZxPwe3ExtCesMac1_Type())
zxPwe3ExtCesMac1.setMaxAccess(_D)
if mibBuilder.loadTexts:zxPwe3ExtCesMac1.setStatus(_A)
_ZxPwe3ExtCesMac2_Type=MacAddress
_ZxPwe3ExtCesMac2_Object=MibScalar
zxPwe3ExtCesMac2=_ZxPwe3ExtCesMac2_Object((1,3,6,1,4,1,3902,1015,1013,21,1,1,7),_ZxPwe3ExtCesMac2_Type())
zxPwe3ExtCesMac2.setMaxAccess(_D)
if mibBuilder.loadTexts:zxPwe3ExtCesMac2.setStatus(_A)
class _ZxPwe3ExtCesMinUdpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ZxPwe3ExtCesMinUdpPort_Type.__name__=_C
_ZxPwe3ExtCesMinUdpPort_Object=MibScalar
zxPwe3ExtCesMinUdpPort=_ZxPwe3ExtCesMinUdpPort_Object((1,3,6,1,4,1,3902,1015,1013,21,1,1,8),_ZxPwe3ExtCesMinUdpPort_Type())
zxPwe3ExtCesMinUdpPort.setMaxAccess(_D)
if mibBuilder.loadTexts:zxPwe3ExtCesMinUdpPort.setStatus(_A)
class _ZxPwe3ExtCesMaxUdpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ZxPwe3ExtCesMaxUdpPort_Type.__name__=_C
_ZxPwe3ExtCesMaxUdpPort_Object=MibScalar
zxPwe3ExtCesMaxUdpPort=_ZxPwe3ExtCesMaxUdpPort_Object((1,3,6,1,4,1,3902,1015,1013,21,1,1,9),_ZxPwe3ExtCesMaxUdpPort_Type())
zxPwe3ExtCesMaxUdpPort.setMaxAccess(_D)
if mibBuilder.loadTexts:zxPwe3ExtCesMaxUdpPort.setStatus(_A)
_ZxPwe3ExtPwTable_Object=MibTable
zxPwe3ExtPwTable=_ZxPwe3ExtPwTable_Object((1,3,6,1,4,1,3902,1015,1013,21,1,2))
if mibBuilder.loadTexts:zxPwe3ExtPwTable.setStatus(_A)
_ZxPwe3ExtPwEntry_Object=MibTableRow
zxPwe3ExtPwEntry=_ZxPwe3ExtPwEntry_Object((1,3,6,1,4,1,3902,1015,1013,21,1,2,1))
zxPwe3ExtPwEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zxPwe3ExtPwEntry.setStatus(_A)
class _ZxPwe3ExtPwSrcIpType_Type(InetAddressType):defaultValue=1
_ZxPwe3ExtPwSrcIpType_Type.__name__=_G
_ZxPwe3ExtPwSrcIpType_Object=MibTableColumn
zxPwe3ExtPwSrcIpType=_ZxPwe3ExtPwSrcIpType_Object((1,3,6,1,4,1,3902,1015,1013,21,1,2,1,1),_ZxPwe3ExtPwSrcIpType_Type())
zxPwe3ExtPwSrcIpType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwe3ExtPwSrcIpType.setStatus(_A)
_ZxPwe3ExtPwSrcIp_Type=InetAddress
_ZxPwe3ExtPwSrcIp_Object=MibTableColumn
zxPwe3ExtPwSrcIp=_ZxPwe3ExtPwSrcIp_Object((1,3,6,1,4,1,3902,1015,1013,21,1,2,1,2),_ZxPwe3ExtPwSrcIp_Type())
zxPwe3ExtPwSrcIp.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwe3ExtPwSrcIp.setStatus(_A)
_ZxPwe3ExtPwSrcMac_Type=MacAddress
_ZxPwe3ExtPwSrcMac_Object=MibTableColumn
zxPwe3ExtPwSrcMac=_ZxPwe3ExtPwSrcMac_Object((1,3,6,1,4,1,3902,1015,1013,21,1,2,1,3),_ZxPwe3ExtPwSrcMac_Type())
zxPwe3ExtPwSrcMac.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwe3ExtPwSrcMac.setStatus(_A)
_ZxPwMplsExtTable_Object=MibTable
zxPwMplsExtTable=_ZxPwMplsExtTable_Object((1,3,6,1,4,1,3902,1015,1013,21,1,3))
if mibBuilder.loadTexts:zxPwMplsExtTable.setStatus(_A)
_ZxPwMplsExtEntry_Object=MibTableRow
zxPwMplsExtEntry=_ZxPwMplsExtEntry_Object((1,3,6,1,4,1,3902,1015,1013,21,1,3,1))
zxPwMplsExtEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zxPwMplsExtEntry.setStatus(_A)
class _ZxPwMplsExtMplsType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('static',1),('dynamic',2),('staticsingle',3)))
_ZxPwMplsExtMplsType_Type.__name__=_C
_ZxPwMplsExtMplsType_Object=MibTableColumn
zxPwMplsExtMplsType=_ZxPwMplsExtMplsType_Object((1,3,6,1,4,1,3902,1015,1013,21,1,3,1,1),_ZxPwMplsExtMplsType_Type())
zxPwMplsExtMplsType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwMplsExtMplsType.setStatus(_A)
_ZxPwMplsExtOutboundTunnelLabel_Type=Unsigned32
_ZxPwMplsExtOutboundTunnelLabel_Object=MibTableColumn
zxPwMplsExtOutboundTunnelLabel=_ZxPwMplsExtOutboundTunnelLabel_Object((1,3,6,1,4,1,3902,1015,1013,21,1,3,1,2),_ZxPwMplsExtOutboundTunnelLabel_Type())
zxPwMplsExtOutboundTunnelLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwMplsExtOutboundTunnelLabel.setStatus(_A)
_ZxPwMplsExtInboundTunnelLabel_Type=Unsigned32
_ZxPwMplsExtInboundTunnelLabel_Object=MibTableColumn
zxPwMplsExtInboundTunnelLabel=_ZxPwMplsExtInboundTunnelLabel_Object((1,3,6,1,4,1,3902,1015,1013,21,1,3,1,3),_ZxPwMplsExtInboundTunnelLabel_Type())
zxPwMplsExtInboundTunnelLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwMplsExtInboundTunnelLabel.setStatus(_A)
_ZxPwMplsExtVcID_Type=PwVcIDType
_ZxPwMplsExtVcID_Object=MibTableColumn
zxPwMplsExtVcID=_ZxPwMplsExtVcID_Object((1,3,6,1,4,1,3902,1015,1013,21,1,3,1,4),_ZxPwMplsExtVcID_Type())
zxPwMplsExtVcID.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwMplsExtVcID.setStatus(_A)
class _ZxPwMplsExtControlWord_Type(TruthValue):defaultValue=2
_ZxPwMplsExtControlWord_Type.__name__=_H
_ZxPwMplsExtControlWord_Object=MibTableColumn
zxPwMplsExtControlWord=_ZxPwMplsExtControlWord_Object((1,3,6,1,4,1,3902,1015,1013,21,1,3,1,5),_ZxPwMplsExtControlWord_Type())
zxPwMplsExtControlWord.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwMplsExtControlWord.setStatus(_A)
class _ZxPwMplsExtWithSequenceNumber_Type(TruthValue):defaultValue=2
_ZxPwMplsExtWithSequenceNumber_Type.__name__=_H
_ZxPwMplsExtWithSequenceNumber_Object=MibTableColumn
zxPwMplsExtWithSequenceNumber=_ZxPwMplsExtWithSequenceNumber_Object((1,3,6,1,4,1,3902,1015,1013,21,1,3,1,6),_ZxPwMplsExtWithSequenceNumber_Type())
zxPwMplsExtWithSequenceNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwMplsExtWithSequenceNumber.setStatus(_A)
_ZxPwe3ExtPwLabelTable_Object=MibTable
zxPwe3ExtPwLabelTable=_ZxPwe3ExtPwLabelTable_Object((1,3,6,1,4,1,3902,1015,1013,21,1,4))
if mibBuilder.loadTexts:zxPwe3ExtPwLabelTable.setStatus(_A)
_ZxPwe3ExtPwLabelEntry_Object=MibTableRow
zxPwe3ExtPwLabelEntry=_ZxPwe3ExtPwLabelEntry_Object((1,3,6,1,4,1,3902,1015,1013,21,1,4,1))
zxPwe3ExtPwLabelEntry.setIndexNames((0,_I,_K),(0,_I,_L))
if mibBuilder.loadTexts:zxPwe3ExtPwLabelEntry.setStatus(_A)
_ZxPwe3ExtPwPsnType_Type=IANAPwPsnTypeTC
_ZxPwe3ExtPwPsnType_Object=MibTableColumn
zxPwe3ExtPwPsnType=_ZxPwe3ExtPwPsnType_Object((1,3,6,1,4,1,3902,1015,1013,21,1,4,1,1),_ZxPwe3ExtPwPsnType_Type())
zxPwe3ExtPwPsnType.setMaxAccess(_M)
if mibBuilder.loadTexts:zxPwe3ExtPwPsnType.setStatus(_A)
_ZxPwe3ExtPwLabelIndex_Type=Integer32
_ZxPwe3ExtPwLabelIndex_Object=MibTableColumn
zxPwe3ExtPwLabelIndex=_ZxPwe3ExtPwLabelIndex_Object((1,3,6,1,4,1,3902,1015,1013,21,1,4,1,2),_ZxPwe3ExtPwLabelIndex_Type())
zxPwe3ExtPwLabelIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:zxPwe3ExtPwLabelIndex.setStatus(_A)
_ZxPwe3ExtPwLabel_Type=DisplayString
_ZxPwe3ExtPwLabel_Object=MibTableColumn
zxPwe3ExtPwLabel=_ZxPwe3ExtPwLabel_Object((1,3,6,1,4,1,3902,1015,1013,21,1,4,1,3),_ZxPwe3ExtPwLabel_Type())
zxPwe3ExtPwLabel.setMaxAccess(_J)
if mibBuilder.loadTexts:zxPwe3ExtPwLabel.setStatus(_A)
_ZxPwExtIpHeadTable_Object=MibTable
zxPwExtIpHeadTable=_ZxPwExtIpHeadTable_Object((1,3,6,1,4,1,3902,1015,1013,21,1,5))
if mibBuilder.loadTexts:zxPwExtIpHeadTable.setStatus(_A)
_ZxPwExtIpHeadEntry_Object=MibTableRow
zxPwExtIpHeadEntry=_ZxPwExtIpHeadEntry_Object((1,3,6,1,4,1,3902,1015,1013,21,1,5,1))
zxPwExtIpHeadEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zxPwExtIpHeadEntry.setStatus(_A)
class _ZxPwExtIpTos_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_ZxPwExtIpTos_Type.__name__=_C
_ZxPwExtIpTos_Object=MibTableColumn
zxPwExtIpTos=_ZxPwExtIpTos_Object((1,3,6,1,4,1,3902,1015,1013,21,1,5,1,1),_ZxPwExtIpTos_Type())
zxPwExtIpTos.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwExtIpTos.setStatus(_A)
class _ZxPwExtIpTtl_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ZxPwExtIpTtl_Type.__name__=_C
_ZxPwExtIpTtl_Object=MibTableColumn
zxPwExtIpTtl=_ZxPwExtIpTtl_Object((1,3,6,1,4,1,3902,1015,1013,21,1,5,1,2),_ZxPwExtIpTtl_Type())
zxPwExtIpTtl.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwExtIpTtl.setStatus(_A)
class _ZxPwExtIpDf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_ZxPwExtIpDf_Type.__name__=_C
_ZxPwExtIpDf_Object=MibTableColumn
zxPwExtIpDf=_ZxPwExtIpDf_Object((1,3,6,1,4,1,3902,1015,1013,21,1,5,1,3),_ZxPwExtIpDf_Type())
zxPwExtIpDf.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwExtIpDf.setStatus(_A)
_ZxAnPwAtmExtCfgTable_Object=MibTable
zxAnPwAtmExtCfgTable=_ZxAnPwAtmExtCfgTable_Object((1,3,6,1,4,1,3902,1015,1013,21,1,6))
if mibBuilder.loadTexts:zxAnPwAtmExtCfgTable.setStatus(_A)
_ZxAnPwAtmExtCfgEntry_Object=MibTableRow
zxAnPwAtmExtCfgEntry=_ZxAnPwAtmExtCfgEntry_Object((1,3,6,1,4,1,3902,1015,1013,21,1,6,1))
zxAnPwAtmExtCfgEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zxAnPwAtmExtCfgEntry.setStatus(_A)
class _ZxAnPwAtmExtTransmitTimeout_Type(Integer32):defaultValue=50;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,4095))
_ZxAnPwAtmExtTransmitTimeout_Type.__name__=_C
_ZxAnPwAtmExtTransmitTimeout_Object=MibTableColumn
zxAnPwAtmExtTransmitTimeout=_ZxAnPwAtmExtTransmitTimeout_Object((1,3,6,1,4,1,3902,1015,1013,21,1,6,1,1),_ZxAnPwAtmExtTransmitTimeout_Type())
zxAnPwAtmExtTransmitTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnPwAtmExtTransmitTimeout.setStatus(_A)
if mibBuilder.loadTexts:zxAnPwAtmExtTransmitTimeout.setUnits('microseconds')
_ZxAnPwQosTable_Object=MibTable
zxAnPwQosTable=_ZxAnPwQosTable_Object((1,3,6,1,4,1,3902,1015,1013,21,1,7))
if mibBuilder.loadTexts:zxAnPwQosTable.setStatus(_A)
_ZxAnPwQosEntry_Object=MibTableRow
zxAnPwQosEntry=_ZxAnPwQosEntry_Object((1,3,6,1,4,1,3902,1015,1013,21,1,7,1))
zxAnPwQosEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zxAnPwQosEntry.setStatus(_A)
class _ZxAnPwQosCir_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,65535))
_ZxAnPwQosCir_Type.__name__=_C
_ZxAnPwQosCir_Object=MibTableColumn
zxAnPwQosCir=_ZxAnPwQosCir_Object((1,3,6,1,4,1,3902,1015,1013,21,1,7,1,1),_ZxAnPwQosCir_Type())
zxAnPwQosCir.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnPwQosCir.setStatus(_A)
if mibBuilder.loadTexts:zxAnPwQosCir.setUnits('kbps')
class _ZxAnPwQosCbs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,65535))
_ZxAnPwQosCbs_Type.__name__=_C
_ZxAnPwQosCbs_Object=MibTableColumn
zxAnPwQosCbs=_ZxAnPwQosCbs_Object((1,3,6,1,4,1,3902,1015,1013,21,1,7,1,2),_ZxAnPwQosCbs_Type())
zxAnPwQosCbs.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnPwQosCbs.setStatus(_A)
if mibBuilder.loadTexts:zxAnPwQosCbs.setUnits(_N)
class _ZxAnPwQosCirRemarkCos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_ZxAnPwQosCirRemarkCos_Type.__name__=_C
_ZxAnPwQosCirRemarkCos_Object=MibTableColumn
zxAnPwQosCirRemarkCos=_ZxAnPwQosCirRemarkCos_Object((1,3,6,1,4,1,3902,1015,1013,21,1,7,1,3),_ZxAnPwQosCirRemarkCos_Type())
zxAnPwQosCirRemarkCos.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnPwQosCirRemarkCos.setStatus(_A)
class _ZxAnPwQosPir_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,65535))
_ZxAnPwQosPir_Type.__name__=_C
_ZxAnPwQosPir_Object=MibTableColumn
zxAnPwQosPir=_ZxAnPwQosPir_Object((1,3,6,1,4,1,3902,1015,1013,21,1,7,1,4),_ZxAnPwQosPir_Type())
zxAnPwQosPir.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnPwQosPir.setStatus(_A)
if mibBuilder.loadTexts:zxAnPwQosPir.setUnits('kbps')
class _ZxAnPwQosPbs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,65535))
_ZxAnPwQosPbs_Type.__name__=_C
_ZxAnPwQosPbs_Object=MibTableColumn
zxAnPwQosPbs=_ZxAnPwQosPbs_Object((1,3,6,1,4,1,3902,1015,1013,21,1,7,1,5),_ZxAnPwQosPbs_Type())
zxAnPwQosPbs.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnPwQosPbs.setStatus(_A)
if mibBuilder.loadTexts:zxAnPwQosPbs.setUnits(_N)
class _ZxAnPwQosPirRemarkCos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_ZxAnPwQosPirRemarkCos_Type.__name__=_C
_ZxAnPwQosPirRemarkCos_Object=MibTableColumn
zxAnPwQosPirRemarkCos=_ZxAnPwQosPirRemarkCos_Object((1,3,6,1,4,1,3902,1015,1013,21,1,7,1,6),_ZxAnPwQosPirRemarkCos_Type())
zxAnPwQosPirRemarkCos.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnPwQosPirRemarkCos.setStatus(_A)
_ZxAnPwQosRowStatus_Type=RowStatus
_ZxAnPwQosRowStatus_Object=MibTableColumn
zxAnPwQosRowStatus=_ZxAnPwQosRowStatus_Object((1,3,6,1,4,1,3902,1015,1013,21,1,7,1,20),_ZxAnPwQosRowStatus_Type())
zxAnPwQosRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnPwQosRowStatus.setStatus(_A)
_ZxAnPwClockTable_Object=MibTable
zxAnPwClockTable=_ZxAnPwClockTable_Object((1,3,6,1,4,1,3902,1015,1013,21,1,8))
if mibBuilder.loadTexts:zxAnPwClockTable.setStatus(_A)
_ZxAnPwClockEntry_Object=MibTableRow
zxAnPwClockEntry=_ZxAnPwClockEntry_Object((1,3,6,1,4,1,3902,1015,1013,21,1,8,1))
zxAnPwClockEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zxAnPwClockEntry.setStatus(_A)
class _ZxAnPwClockStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('freeRun',1),('holdOver',2),('acquiring',3),('acquired',4),('notReady',5)))
_ZxAnPwClockStatus_Type.__name__=_C
_ZxAnPwClockStatus_Object=MibTableColumn
zxAnPwClockStatus=_ZxAnPwClockStatus_Object((1,3,6,1,4,1,3902,1015,1013,21,1,8,1,1),_ZxAnPwClockStatus_Type())
zxAnPwClockStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:zxAnPwClockStatus.setStatus(_A)
_ZxAnPwClockOffset_Type=Integer32
_ZxAnPwClockOffset_Object=MibTableColumn
zxAnPwClockOffset=_ZxAnPwClockOffset_Object((1,3,6,1,4,1,3902,1015,1013,21,1,8,1,2),_ZxAnPwClockOffset_Type())
zxAnPwClockOffset.setMaxAccess(_J)
if mibBuilder.loadTexts:zxAnPwClockOffset.setStatus(_A)
if mibBuilder.loadTexts:zxAnPwClockOffset.setUnits('ppb')
_ZxPwe3ExtTrapObjects_ObjectIdentity=ObjectIdentity
zxPwe3ExtTrapObjects=_ZxPwe3ExtTrapObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,1013,21,2))
mibBuilder.exportSymbols(_I,**{'PwVcIDType':PwVcIDType,'zxPwe3ExtMib':zxPwe3ExtMib,'zxPwe3ExtObjects':zxPwe3ExtObjects,'zxPwe3ExtGlobalObjects':zxPwe3ExtGlobalObjects,'zxPwe3ExtCesMode':zxPwe3ExtCesMode,'zxPwe3ExtCesIp1Type':zxPwe3ExtCesIp1Type,'zxPwe3ExtCesIp1':zxPwe3ExtCesIp1,'zxPwe3ExtCesIp2Type':zxPwe3ExtCesIp2Type,'zxPwe3ExtCesIp2':zxPwe3ExtCesIp2,'zxPwe3ExtCesMac1':zxPwe3ExtCesMac1,'zxPwe3ExtCesMac2':zxPwe3ExtCesMac2,'zxPwe3ExtCesMinUdpPort':zxPwe3ExtCesMinUdpPort,'zxPwe3ExtCesMaxUdpPort':zxPwe3ExtCesMaxUdpPort,'zxPwe3ExtPwTable':zxPwe3ExtPwTable,'zxPwe3ExtPwEntry':zxPwe3ExtPwEntry,'zxPwe3ExtPwSrcIpType':zxPwe3ExtPwSrcIpType,'zxPwe3ExtPwSrcIp':zxPwe3ExtPwSrcIp,'zxPwe3ExtPwSrcMac':zxPwe3ExtPwSrcMac,'zxPwMplsExtTable':zxPwMplsExtTable,'zxPwMplsExtEntry':zxPwMplsExtEntry,'zxPwMplsExtMplsType':zxPwMplsExtMplsType,'zxPwMplsExtOutboundTunnelLabel':zxPwMplsExtOutboundTunnelLabel,'zxPwMplsExtInboundTunnelLabel':zxPwMplsExtInboundTunnelLabel,'zxPwMplsExtVcID':zxPwMplsExtVcID,'zxPwMplsExtControlWord':zxPwMplsExtControlWord,'zxPwMplsExtWithSequenceNumber':zxPwMplsExtWithSequenceNumber,'zxPwe3ExtPwLabelTable':zxPwe3ExtPwLabelTable,'zxPwe3ExtPwLabelEntry':zxPwe3ExtPwLabelEntry,_K:zxPwe3ExtPwPsnType,_L:zxPwe3ExtPwLabelIndex,'zxPwe3ExtPwLabel':zxPwe3ExtPwLabel,'zxPwExtIpHeadTable':zxPwExtIpHeadTable,'zxPwExtIpHeadEntry':zxPwExtIpHeadEntry,'zxPwExtIpTos':zxPwExtIpTos,'zxPwExtIpTtl':zxPwExtIpTtl,'zxPwExtIpDf':zxPwExtIpDf,'zxAnPwAtmExtCfgTable':zxAnPwAtmExtCfgTable,'zxAnPwAtmExtCfgEntry':zxAnPwAtmExtCfgEntry,'zxAnPwAtmExtTransmitTimeout':zxAnPwAtmExtTransmitTimeout,'zxAnPwQosTable':zxAnPwQosTable,'zxAnPwQosEntry':zxAnPwQosEntry,'zxAnPwQosCir':zxAnPwQosCir,'zxAnPwQosCbs':zxAnPwQosCbs,'zxAnPwQosCirRemarkCos':zxAnPwQosCirRemarkCos,'zxAnPwQosPir':zxAnPwQosPir,'zxAnPwQosPbs':zxAnPwQosPbs,'zxAnPwQosPirRemarkCos':zxAnPwQosPirRemarkCos,'zxAnPwQosRowStatus':zxAnPwQosRowStatus,'zxAnPwClockTable':zxAnPwClockTable,'zxAnPwClockEntry':zxAnPwClockEntry,'zxAnPwClockStatus':zxAnPwClockStatus,'zxAnPwClockOffset':zxAnPwClockOffset,'zxPwe3ExtTrapObjects':zxPwe3ExtTrapObjects})