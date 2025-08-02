_K='nsIfMonIfIdx'
_J='nsIfFlowIfIdx'
_I='nsIfSecondaryIpIndex'
_H='nsIfIndex'
_G='DisplayString'
_F='NETSCREEN-INTERFACE-MIB'
_E='enable'
_D='disable'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
netscreenInterface,=mibBuilder.importSymbols('NETSCREEN-SMI','netscreenInterface')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','TextualConvention')
netscreenInterfaceMibModule=ModuleIdentity((1,3,6,1,4,1,3224,9,0))
if mibBuilder.loadTexts:netscreenInterfaceMibModule.setRevisions(('2004-05-03 00:00','2004-03-03 00:00','2001-09-28 00:00','2001-05-11 00:00'))
_NsIfTable_Object=MibTable
nsIfTable=_NsIfTable_Object((1,3,6,1,4,1,3224,9,1))
if mibBuilder.loadTexts:nsIfTable.setStatus(_A)
_NsIfEntry_Object=MibTableRow
nsIfEntry=_NsIfEntry_Object((1,3,6,1,4,1,3224,9,1,1))
nsIfEntry.setIndexNames((0,_F,_H))
if mibBuilder.loadTexts:nsIfEntry.setStatus(_A)
class _NsIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NsIfIndex_Type.__name__=_C
_NsIfIndex_Object=MibTableColumn
nsIfIndex=_NsIfIndex_Object((1,3,6,1,4,1,3224,9,1,1,1),_NsIfIndex_Type())
nsIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIfIndex.setStatus(_A)
class _NsIfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsIfName_Type.__name__=_G
_NsIfName_Object=MibTableColumn
nsIfName=_NsIfName_Object((1,3,6,1,4,1,3224,9,1,1,2),_NsIfName_Type())
nsIfName.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIfName.setStatus(_A)
_NsIfVsys_Type=Integer32
_NsIfVsys_Object=MibTableColumn
nsIfVsys=_NsIfVsys_Object((1,3,6,1,4,1,3224,9,1,1,3),_NsIfVsys_Type())
nsIfVsys.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIfVsys.setStatus(_A)
_NsIfZone_Type=Integer32
_NsIfZone_Object=MibTableColumn
nsIfZone=_NsIfZone_Object((1,3,6,1,4,1,3224,9,1,1,4),_NsIfZone_Type())
nsIfZone.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIfZone.setStatus(_A)
class _NsIfStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('down',0),('up',1),('ready',2),('inactive',3)))
_NsIfStatus_Type.__name__=_C
_NsIfStatus_Object=MibTableColumn
nsIfStatus=_NsIfStatus_Object((1,3,6,1,4,1,3224,9,1,1,5),_NsIfStatus_Type())
nsIfStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIfStatus.setStatus(_A)
_NsIfIp_Type=IpAddress
_NsIfIp_Object=MibTableColumn
nsIfIp=_NsIfIp_Object((1,3,6,1,4,1,3224,9,1,1,6),_NsIfIp_Type())
nsIfIp.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIfIp.setStatus(_A)
_NsIfNetmask_Type=IpAddress
_NsIfNetmask_Object=MibTableColumn
nsIfNetmask=_NsIfNetmask_Object((1,3,6,1,4,1,3224,9,1,1,7),_NsIfNetmask_Type())
nsIfNetmask.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIfNetmask.setStatus(_A)
_NsIfGateway_Type=IpAddress
_NsIfGateway_Object=MibTableColumn
nsIfGateway=_NsIfGateway_Object((1,3,6,1,4,1,3224,9,1,1,8),_NsIfGateway_Type())
nsIfGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIfGateway.setStatus(_A)
_NsIfMngIp_Type=IpAddress
_NsIfMngIp_Object=MibTableColumn
nsIfMngIp=_NsIfMngIp_Object((1,3,6,1,4,1,3224,9,1,1,9),_NsIfMngIp_Type())
nsIfMngIp.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIfMngIp.setStatus(_A)
class _NsIfMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('transparent',0),('nat',1),('route',2),('not-applicable',3)))
_NsIfMode_Type.__name__=_C
_NsIfMode_Object=MibTableColumn
nsIfMode=_NsIfMode_Object((1,3,6,1,4,1,3224,9,1,1,10),_NsIfMode_Type())
nsIfMode.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIfMode.setStatus(_A)
_NsIfMAC_Type=PhysAddress
_NsIfMAC_Object=MibTableColumn
nsIfMAC=_NsIfMAC_Object((1,3,6,1,4,1,3224,9,1,1,11),_NsIfMAC_Type())
nsIfMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIfMAC.setStatus(_A)
class _NsIfMngTelnet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_NsIfMngTelnet_Type.__name__=_C
_NsIfMngTelnet_Object=MibTableColumn
nsIfMngTelnet=_NsIfMngTelnet_Object((1,3,6,1,4,1,3224,9,1,1,12),_NsIfMngTelnet_Type())
nsIfMngTelnet.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIfMngTelnet.setStatus(_A)
class _NsIfMngSCS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_NsIfMngSCS_Type.__name__=_C
_NsIfMngSCS_Object=MibTableColumn
nsIfMngSCS=_NsIfMngSCS_Object((1,3,6,1,4,1,3224,9,1,1,13),_NsIfMngSCS_Type())
nsIfMngSCS.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIfMngSCS.setStatus(_A)
class _NsIfMngWEB_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_NsIfMngWEB_Type.__name__=_C
_NsIfMngWEB_Object=MibTableColumn
nsIfMngWEB=_NsIfMngWEB_Object((1,3,6,1,4,1,3224,9,1,1,14),_NsIfMngWEB_Type())
nsIfMngWEB.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIfMngWEB.setStatus(_A)
class _NsIfMngSSL_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_NsIfMngSSL_Type.__name__=_C
_NsIfMngSSL_Object=MibTableColumn
nsIfMngSSL=_NsIfMngSSL_Object((1,3,6,1,4,1,3224,9,1,1,15),_NsIfMngSSL_Type())
nsIfMngSSL.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIfMngSSL.setStatus(_A)
class _NsIfMngSNMP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_NsIfMngSNMP_Type.__name__=_C
_NsIfMngSNMP_Object=MibTableColumn
nsIfMngSNMP=_NsIfMngSNMP_Object((1,3,6,1,4,1,3224,9,1,1,16),_NsIfMngSNMP_Type())
nsIfMngSNMP.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIfMngSNMP.setStatus(_A)
class _NsIfMngGlobal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_NsIfMngGlobal_Type.__name__=_C
_NsIfMngGlobal_Object=MibTableColumn
nsIfMngGlobal=_NsIfMngGlobal_Object((1,3,6,1,4,1,3224,9,1,1,17),_NsIfMngGlobal_Type())
nsIfMngGlobal.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIfMngGlobal.setStatus(_A)
class _NsIfMngGlobalPro_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_NsIfMngGlobalPro_Type.__name__=_C
_NsIfMngGlobalPro_Object=MibTableColumn
nsIfMngGlobalPro=_NsIfMngGlobalPro_Object((1,3,6,1,4,1,3224,9,1,1,18),_NsIfMngGlobalPro_Type())
nsIfMngGlobalPro.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIfMngGlobalPro.setStatus(_A)
class _NsIfMngPing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_NsIfMngPing_Type.__name__=_C
_NsIfMngPing_Object=MibTableColumn
nsIfMngPing=_NsIfMngPing_Object((1,3,6,1,4,1,3224,9,1,1,19),_NsIfMngPing_Type())
nsIfMngPing.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIfMngPing.setStatus(_A)
class _NsIfMngIdentReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_NsIfMngIdentReset_Type.__name__=_C
_NsIfMngIdentReset_Object=MibTableColumn
nsIfMngIdentReset=_NsIfMngIdentReset_Object((1,3,6,1,4,1,3224,9,1,1,20),_NsIfMngIdentReset_Type())
nsIfMngIdentReset.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIfMngIdentReset.setStatus(_A)
class _NsIfInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NsIfInfo_Type.__name__=_C
_NsIfInfo_Object=MibTableColumn
nsIfInfo=_NsIfInfo_Object((1,3,6,1,4,1,3224,9,1,1,21),_NsIfInfo_Type())
nsIfInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIfInfo.setStatus(_A)
class _NsIfDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsIfDescr_Type.__name__=_G
_NsIfDescr_Object=MibTableColumn
nsIfDescr=_NsIfDescr_Object((1,3,6,1,4,1,3224,9,1,1,22),_NsIfDescr_Type())
nsIfDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIfDescr.setStatus(_A)
_NsIfSecondaryIpTable_Object=MibTable
nsIfSecondaryIpTable=_NsIfSecondaryIpTable_Object((1,3,6,1,4,1,3224,9,2))
if mibBuilder.loadTexts:nsIfSecondaryIpTable.setStatus(_A)
_NsIfSecondaryIpEntry_Object=MibTableRow
nsIfSecondaryIpEntry=_NsIfSecondaryIpEntry_Object((1,3,6,1,4,1,3224,9,2,1))
nsIfSecondaryIpEntry.setIndexNames((0,_F,_I))
if mibBuilder.loadTexts:nsIfSecondaryIpEntry.setStatus(_A)
class _NsIfSecondaryIpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NsIfSecondaryIpIndex_Type.__name__=_C
_NsIfSecondaryIpIndex_Object=MibTableColumn
nsIfSecondaryIpIndex=_NsIfSecondaryIpIndex_Object((1,3,6,1,4,1,3224,9,2,1,1),_NsIfSecondaryIpIndex_Type())
nsIfSecondaryIpIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIfSecondaryIpIndex.setStatus(_A)
_NsIfSecondaryIpIfIdx_Type=Integer32
_NsIfSecondaryIpIfIdx_Object=MibTableColumn
nsIfSecondaryIpIfIdx=_NsIfSecondaryIpIfIdx_Object((1,3,6,1,4,1,3224,9,2,1,2),_NsIfSecondaryIpIfIdx_Type())
nsIfSecondaryIpIfIdx.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIfSecondaryIpIfIdx.setStatus(_A)
_NsIfSecondaryIpVsys_Type=Integer32
_NsIfSecondaryIpVsys_Object=MibTableColumn
nsIfSecondaryIpVsys=_NsIfSecondaryIpVsys_Object((1,3,6,1,4,1,3224,9,2,1,3),_NsIfSecondaryIpVsys_Type())
nsIfSecondaryIpVsys.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIfSecondaryIpVsys.setStatus(_A)
_NsIfSecondaryIpZone_Type=Integer32
_NsIfSecondaryIpZone_Object=MibTableColumn
nsIfSecondaryIpZone=_NsIfSecondaryIpZone_Object((1,3,6,1,4,1,3224,9,2,1,4),_NsIfSecondaryIpZone_Type())
nsIfSecondaryIpZone.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIfSecondaryIpZone.setStatus(_A)
_NsIfSecondaryIpAddress_Type=IpAddress
_NsIfSecondaryIpAddress_Object=MibTableColumn
nsIfSecondaryIpAddress=_NsIfSecondaryIpAddress_Object((1,3,6,1,4,1,3224,9,2,1,5),_NsIfSecondaryIpAddress_Type())
nsIfSecondaryIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIfSecondaryIpAddress.setStatus(_A)
_NsIfSecondaryIpNetmask_Type=IpAddress
_NsIfSecondaryIpNetmask_Object=MibTableColumn
nsIfSecondaryIpNetmask=_NsIfSecondaryIpNetmask_Object((1,3,6,1,4,1,3224,9,2,1,6),_NsIfSecondaryIpNetmask_Type())
nsIfSecondaryIpNetmask.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIfSecondaryIpNetmask.setStatus(_A)
class _NsIfSecondaryIpIfInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NsIfSecondaryIpIfInfo_Type.__name__=_C
_NsIfSecondaryIpIfInfo_Object=MibTableColumn
nsIfSecondaryIpIfInfo=_NsIfSecondaryIpIfInfo_Object((1,3,6,1,4,1,3224,9,2,1,7),_NsIfSecondaryIpIfInfo_Type())
nsIfSecondaryIpIfInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIfSecondaryIpIfInfo.setStatus(_A)
_NsIfFlowTable_Object=MibTable
nsIfFlowTable=_NsIfFlowTable_Object((1,3,6,1,4,1,3224,9,3))
if mibBuilder.loadTexts:nsIfFlowTable.setStatus(_A)
_NsIfFlowEntry_Object=MibTableRow
nsIfFlowEntry=_NsIfFlowEntry_Object((1,3,6,1,4,1,3224,9,3,1))
nsIfFlowEntry.setIndexNames((0,_F,_J))
if mibBuilder.loadTexts:nsIfFlowEntry.setStatus(_A)
class _NsIfFlowIfIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NsIfFlowIfIdx_Type.__name__=_C
_NsIfFlowIfIdx_Object=MibTableColumn
nsIfFlowIfIdx=_NsIfFlowIfIdx_Object((1,3,6,1,4,1,3224,9,3,1,1),_NsIfFlowIfIdx_Type())
nsIfFlowIfIdx.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIfFlowIfIdx.setStatus(_A)
_NsIfFlowVsys_Type=Integer32
_NsIfFlowVsys_Object=MibTableColumn
nsIfFlowVsys=_NsIfFlowVsys_Object((1,3,6,1,4,1,3224,9,3,1,2),_NsIfFlowVsys_Type())
nsIfFlowVsys.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIfFlowVsys.setStatus(_A)
_NsIfFlowInByte_Type=Counter32
_NsIfFlowInByte_Object=MibTableColumn
nsIfFlowInByte=_NsIfFlowInByte_Object((1,3,6,1,4,1,3224,9,3,1,3),_NsIfFlowInByte_Type())
nsIfFlowInByte.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIfFlowInByte.setStatus(_A)
_NsIfFlowInPacket_Type=Counter32
_NsIfFlowInPacket_Object=MibTableColumn
nsIfFlowInPacket=_NsIfFlowInPacket_Object((1,3,6,1,4,1,3224,9,3,1,4),_NsIfFlowInPacket_Type())
nsIfFlowInPacket.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIfFlowInPacket.setStatus(_A)
_NsIfFlowOutByte_Type=Counter32
_NsIfFlowOutByte_Object=MibTableColumn
nsIfFlowOutByte=_NsIfFlowOutByte_Object((1,3,6,1,4,1,3224,9,3,1,5),_NsIfFlowOutByte_Type())
nsIfFlowOutByte.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIfFlowOutByte.setStatus(_A)
_NsIfFlowOutPacket_Type=Counter32
_NsIfFlowOutPacket_Object=MibTableColumn
nsIfFlowOutPacket=_NsIfFlowOutPacket_Object((1,3,6,1,4,1,3224,9,3,1,6),_NsIfFlowOutPacket_Type())
nsIfFlowOutPacket.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIfFlowOutPacket.setStatus(_A)
_NsIfFlowInVpn_Type=Counter32
_NsIfFlowInVpn_Object=MibTableColumn
nsIfFlowInVpn=_NsIfFlowInVpn_Object((1,3,6,1,4,1,3224,9,3,1,7),_NsIfFlowInVpn_Type())
nsIfFlowInVpn.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIfFlowInVpn.setStatus(_A)
_NsIfInVlan_Type=Counter32
_NsIfInVlan_Object=MibTableColumn
nsIfInVlan=_NsIfInVlan_Object((1,3,6,1,4,1,3224,9,3,1,8),_NsIfInVlan_Type())
nsIfInVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIfInVlan.setStatus(_A)
_NsIfOutVlan_Type=Counter32
_NsIfOutVlan_Object=MibTableColumn
nsIfOutVlan=_NsIfOutVlan_Object((1,3,6,1,4,1,3224,9,3,1,9),_NsIfOutVlan_Type())
nsIfOutVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIfOutVlan.setStatus(_A)
class _NsIfFlowIfInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NsIfFlowIfInfo_Type.__name__=_C
_NsIfFlowIfInfo_Object=MibTableColumn
nsIfFlowIfInfo=_NsIfFlowIfInfo_Object((1,3,6,1,4,1,3224,9,3,1,10),_NsIfFlowIfInfo_Type())
nsIfFlowIfInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIfFlowIfInfo.setStatus(_A)
_NsIfMonTable_Object=MibTable
nsIfMonTable=_NsIfMonTable_Object((1,3,6,1,4,1,3224,9,4))
if mibBuilder.loadTexts:nsIfMonTable.setStatus(_A)
_NsIfMonEntry_Object=MibTableRow
nsIfMonEntry=_NsIfMonEntry_Object((1,3,6,1,4,1,3224,9,4,1))
nsIfMonEntry.setIndexNames((0,_F,_K))
if mibBuilder.loadTexts:nsIfMonEntry.setStatus(_A)
class _NsIfMonIfIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NsIfMonIfIdx_Type.__name__=_C
_NsIfMonIfIdx_Object=MibTableColumn
nsIfMonIfIdx=_NsIfMonIfIdx_Object((1,3,6,1,4,1,3224,9,4,1,1),_NsIfMonIfIdx_Type())
nsIfMonIfIdx.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIfMonIfIdx.setStatus(_A)
_NsIfMonVsys_Type=Integer32
_NsIfMonVsys_Object=MibTableColumn
nsIfMonVsys=_NsIfMonVsys_Object((1,3,6,1,4,1,3224,9,4,1,2),_NsIfMonVsys_Type())
nsIfMonVsys.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIfMonVsys.setStatus(_A)
_NsIfMonPlyDeny_Type=Counter32
_NsIfMonPlyDeny_Object=MibTableColumn
nsIfMonPlyDeny=_NsIfMonPlyDeny_Object((1,3,6,1,4,1,3224,9,4,1,3),_NsIfMonPlyDeny_Type())
nsIfMonPlyDeny.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIfMonPlyDeny.setStatus(_A)
_NsIfMonAuthFail_Type=Counter32
_NsIfMonAuthFail_Object=MibTableColumn
nsIfMonAuthFail=_NsIfMonAuthFail_Object((1,3,6,1,4,1,3224,9,4,1,4),_NsIfMonAuthFail_Type())
nsIfMonAuthFail.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIfMonAuthFail.setStatus(_A)
_NsIfMonUrlBlock_Type=Counter32
_NsIfMonUrlBlock_Object=MibTableColumn
nsIfMonUrlBlock=_NsIfMonUrlBlock_Object((1,3,6,1,4,1,3224,9,4,1,5),_NsIfMonUrlBlock_Type())
nsIfMonUrlBlock.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIfMonUrlBlock.setStatus(_A)
_NsIfMonTrMngQueue_Type=Counter32
_NsIfMonTrMngQueue_Object=MibTableColumn
nsIfMonTrMngQueue=_NsIfMonTrMngQueue_Object((1,3,6,1,4,1,3224,9,4,1,6),_NsIfMonTrMngQueue_Type())
nsIfMonTrMngQueue.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIfMonTrMngQueue.setStatus(_A)
_NsIfMonTrMngDrop_Type=Counter32
_NsIfMonTrMngDrop_Object=MibTableColumn
nsIfMonTrMngDrop=_NsIfMonTrMngDrop_Object((1,3,6,1,4,1,3224,9,4,1,7),_NsIfMonTrMngDrop_Type())
nsIfMonTrMngDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIfMonTrMngDrop.setStatus(_A)
_NsIfMonEncFail_Type=Counter32
_NsIfMonEncFail_Object=MibTableColumn
nsIfMonEncFail=_NsIfMonEncFail_Object((1,3,6,1,4,1,3224,9,4,1,8),_NsIfMonEncFail_Type())
nsIfMonEncFail.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIfMonEncFail.setStatus(_A)
_NsIfMonNoSa_Type=Counter32
_NsIfMonNoSa_Object=MibTableColumn
nsIfMonNoSa=_NsIfMonNoSa_Object((1,3,6,1,4,1,3224,9,4,1,9),_NsIfMonNoSa_Type())
nsIfMonNoSa.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIfMonNoSa.setStatus(_A)
_NsIfMonNoSaPly_Type=Counter32
_NsIfMonNoSaPly_Object=MibTableColumn
nsIfMonNoSaPly=_NsIfMonNoSaPly_Object((1,3,6,1,4,1,3224,9,4,1,10),_NsIfMonNoSaPly_Type())
nsIfMonNoSaPly.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIfMonNoSaPly.setStatus(_A)
_NsIfMonSaInactive_Type=Counter32
_NsIfMonSaInactive_Object=MibTableColumn
nsIfMonSaInactive=_NsIfMonSaInactive_Object((1,3,6,1,4,1,3224,9,4,1,11),_NsIfMonSaInactive_Type())
nsIfMonSaInactive.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIfMonSaInactive.setStatus(_A)
_NsIfMonSaPolicyDeny_Type=Counter32
_NsIfMonSaPolicyDeny_Object=MibTableColumn
nsIfMonSaPolicyDeny=_NsIfMonSaPolicyDeny_Object((1,3,6,1,4,1,3224,9,4,1,12),_NsIfMonSaPolicyDeny_Type())
nsIfMonSaPolicyDeny.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIfMonSaPolicyDeny.setStatus(_A)
class _NsIfMonIfInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NsIfMonIfInfo_Type.__name__=_C
_NsIfMonIfInfo_Object=MibTableColumn
nsIfMonIfInfo=_NsIfMonIfInfo_Object((1,3,6,1,4,1,3224,9,4,1,13),_NsIfMonIfInfo_Type())
nsIfMonIfInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIfMonIfInfo.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'netscreenInterfaceMibModule':netscreenInterfaceMibModule,'nsIfTable':nsIfTable,'nsIfEntry':nsIfEntry,_H:nsIfIndex,'nsIfName':nsIfName,'nsIfVsys':nsIfVsys,'nsIfZone':nsIfZone,'nsIfStatus':nsIfStatus,'nsIfIp':nsIfIp,'nsIfNetmask':nsIfNetmask,'nsIfGateway':nsIfGateway,'nsIfMngIp':nsIfMngIp,'nsIfMode':nsIfMode,'nsIfMAC':nsIfMAC,'nsIfMngTelnet':nsIfMngTelnet,'nsIfMngSCS':nsIfMngSCS,'nsIfMngWEB':nsIfMngWEB,'nsIfMngSSL':nsIfMngSSL,'nsIfMngSNMP':nsIfMngSNMP,'nsIfMngGlobal':nsIfMngGlobal,'nsIfMngGlobalPro':nsIfMngGlobalPro,'nsIfMngPing':nsIfMngPing,'nsIfMngIdentReset':nsIfMngIdentReset,'nsIfInfo':nsIfInfo,'nsIfDescr':nsIfDescr,'nsIfSecondaryIpTable':nsIfSecondaryIpTable,'nsIfSecondaryIpEntry':nsIfSecondaryIpEntry,_I:nsIfSecondaryIpIndex,'nsIfSecondaryIpIfIdx':nsIfSecondaryIpIfIdx,'nsIfSecondaryIpVsys':nsIfSecondaryIpVsys,'nsIfSecondaryIpZone':nsIfSecondaryIpZone,'nsIfSecondaryIpAddress':nsIfSecondaryIpAddress,'nsIfSecondaryIpNetmask':nsIfSecondaryIpNetmask,'nsIfSecondaryIpIfInfo':nsIfSecondaryIpIfInfo,'nsIfFlowTable':nsIfFlowTable,'nsIfFlowEntry':nsIfFlowEntry,_J:nsIfFlowIfIdx,'nsIfFlowVsys':nsIfFlowVsys,'nsIfFlowInByte':nsIfFlowInByte,'nsIfFlowInPacket':nsIfFlowInPacket,'nsIfFlowOutByte':nsIfFlowOutByte,'nsIfFlowOutPacket':nsIfFlowOutPacket,'nsIfFlowInVpn':nsIfFlowInVpn,'nsIfInVlan':nsIfInVlan,'nsIfOutVlan':nsIfOutVlan,'nsIfFlowIfInfo':nsIfFlowIfInfo,'nsIfMonTable':nsIfMonTable,'nsIfMonEntry':nsIfMonEntry,_K:nsIfMonIfIdx,'nsIfMonVsys':nsIfMonVsys,'nsIfMonPlyDeny':nsIfMonPlyDeny,'nsIfMonAuthFail':nsIfMonAuthFail,'nsIfMonUrlBlock':nsIfMonUrlBlock,'nsIfMonTrMngQueue':nsIfMonTrMngQueue,'nsIfMonTrMngDrop':nsIfMonTrMngDrop,'nsIfMonEncFail':nsIfMonEncFail,'nsIfMonNoSa':nsIfMonNoSa,'nsIfMonNoSaPly':nsIfMonNoSaPly,'nsIfMonSaInactive':nsIfMonSaInactive,'nsIfMonSaPolicyDeny':nsIfMonSaPolicyDeny,'nsIfMonIfInfo':nsIfMonIfInfo})