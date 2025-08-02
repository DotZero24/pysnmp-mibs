_Y='cfmMetadateFlowInfoGroupV2'
_X='cfmMetadateFlowInfoGroup'
_W='cfmMetadataFlowAllAttrPen'
_V='cfmMetadataFlowAllAttrValue'
_U='cfmMetadataFlowAttrValue'
_T='cfmMetadataFlowAllAttrInstanceId'
_S='cfmMetadataIpFixIeId'
_R='Integer32'
_Q='OctetString'
_P='cfmMetadataFlowSSRC'
_O='cfmMetadataFlowSrcPort'
_N='cfmMetadataFlowSrcAddr'
_M='cfmMetadataFlowSrcAddrType'
_L='cfmMetadataFlowDestPort'
_K='cfmMetadataFlowDestAddr'
_J='cfmMetadataFlowDestAddrType'
_I='cfmMetadataFlowProtocolType'
_H='cfmMetadataFlowAttrType'
_G='not-accessible'
_F='cfmMetadataFlowId'
_E='Unsigned32'
_D='deprecated'
_C='read-only'
_B='current'
_A='CISCO-FLOW-METADATA-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_Q,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType','InetPortNumber')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_R,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoFlowMetadataMIB=ModuleIdentity((1,3,6,1,4,1,9,9,789))
if mibBuilder.loadTexts:ciscoFlowMetadataMIB.setRevisions(('2012-12-17 00:00','2011-03-20 00:00'))
class CfmMetadataFlowAttributeType(TextualConvention,Integer32):status=_D;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,94,95,96,97,98,100,101,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,134,135,136,137,138,139)));namedValues=NamedValues(*(('other',0),('appDescription',94),('appTag',95),('appName',96),('appVersion',97),('appVendor',98),('vmFlowTimeout',100),('vmRTPClockFrequency',101),('pakRate',103),('l3Bitrate',104),('mediaBitrate',105),('mediaVideoPaksize',106),('globalSessionID',107),('multipartySessionID',108),('rtpMediaFlow',109),('mediaEncryptionStatus',110),('syntheticTraffic',111),('meteringPriority',112),('endpointModel',113),('endpointVendor',114),('endpointVersion',115),('ssrc',116),('endpointIPAddressType',117),('endpointIPAddressLength',118),('endpointIPAddressValue',119),('sipProxyServerType',120),('sipProxyServerLength',121),('sipProxyServerValue',122),('bandwidth',123),('deviceName',124),('deviceClass',125),('sipUserName',126),('sipEmail',127),('audioCodec',128),('bandwidthConsumed',129),('payloadType',130),('mimeType',131),('extrapolatedBandwidth',132),('cname',134),('videoCodec',135),('sdpSessionID',136),('domainName',137),('endpointSwVersion',138),('tosDscp',139)))
class CfmMetadataFlowAttrVal(TextualConvention,OctetString):status=_D;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_CFlowMetadataMIBNotifs_ObjectIdentity=ObjectIdentity
cFlowMetadataMIBNotifs=_CFlowMetadataMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,789,0))
_CFlowMetadataMIBObjects_ObjectIdentity=ObjectIdentity
cFlowMetadataMIBObjects=_CFlowMetadataMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,789,1))
_CfmMetadataFlowTable_Object=MibTable
cfmMetadataFlowTable=_CfmMetadataFlowTable_Object((1,3,6,1,4,1,9,9,789,1,1))
if mibBuilder.loadTexts:cfmMetadataFlowTable.setStatus(_B)
_CfmMetadataFlowEntry_Object=MibTableRow
cfmMetadataFlowEntry=_CfmMetadataFlowEntry_Object((1,3,6,1,4,1,9,9,789,1,1,1))
cfmMetadataFlowEntry.setIndexNames((0,_A,_F))
if mibBuilder.loadTexts:cfmMetadataFlowEntry.setStatus(_B)
_CfmMetadataFlowId_Type=Unsigned32
_CfmMetadataFlowId_Object=MibTableColumn
cfmMetadataFlowId=_CfmMetadataFlowId_Object((1,3,6,1,4,1,9,9,789,1,1,1,1),_CfmMetadataFlowId_Type())
cfmMetadataFlowId.setMaxAccess(_G)
if mibBuilder.loadTexts:cfmMetadataFlowId.setStatus(_B)
class _CfmMetadataFlowProtocolType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('tcp',1),('udp',2)))
_CfmMetadataFlowProtocolType_Type.__name__=_R
_CfmMetadataFlowProtocolType_Object=MibTableColumn
cfmMetadataFlowProtocolType=_CfmMetadataFlowProtocolType_Object((1,3,6,1,4,1,9,9,789,1,1,1,2),_CfmMetadataFlowProtocolType_Type())
cfmMetadataFlowProtocolType.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmMetadataFlowProtocolType.setStatus(_B)
_CfmMetadataFlowDestAddrType_Type=InetAddressType
_CfmMetadataFlowDestAddrType_Object=MibTableColumn
cfmMetadataFlowDestAddrType=_CfmMetadataFlowDestAddrType_Object((1,3,6,1,4,1,9,9,789,1,1,1,3),_CfmMetadataFlowDestAddrType_Type())
cfmMetadataFlowDestAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmMetadataFlowDestAddrType.setStatus(_B)
_CfmMetadataFlowDestAddr_Type=InetAddress
_CfmMetadataFlowDestAddr_Object=MibTableColumn
cfmMetadataFlowDestAddr=_CfmMetadataFlowDestAddr_Object((1,3,6,1,4,1,9,9,789,1,1,1,4),_CfmMetadataFlowDestAddr_Type())
cfmMetadataFlowDestAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmMetadataFlowDestAddr.setStatus(_B)
_CfmMetadataFlowDestPort_Type=InetPortNumber
_CfmMetadataFlowDestPort_Object=MibTableColumn
cfmMetadataFlowDestPort=_CfmMetadataFlowDestPort_Object((1,3,6,1,4,1,9,9,789,1,1,1,5),_CfmMetadataFlowDestPort_Type())
cfmMetadataFlowDestPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmMetadataFlowDestPort.setStatus(_B)
_CfmMetadataFlowSrcAddrType_Type=InetAddressType
_CfmMetadataFlowSrcAddrType_Object=MibTableColumn
cfmMetadataFlowSrcAddrType=_CfmMetadataFlowSrcAddrType_Object((1,3,6,1,4,1,9,9,789,1,1,1,6),_CfmMetadataFlowSrcAddrType_Type())
cfmMetadataFlowSrcAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmMetadataFlowSrcAddrType.setStatus(_B)
_CfmMetadataFlowSrcAddr_Type=InetAddress
_CfmMetadataFlowSrcAddr_Object=MibTableColumn
cfmMetadataFlowSrcAddr=_CfmMetadataFlowSrcAddr_Object((1,3,6,1,4,1,9,9,789,1,1,1,7),_CfmMetadataFlowSrcAddr_Type())
cfmMetadataFlowSrcAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmMetadataFlowSrcAddr.setStatus(_B)
_CfmMetadataFlowSrcPort_Type=InetPortNumber
_CfmMetadataFlowSrcPort_Object=MibTableColumn
cfmMetadataFlowSrcPort=_CfmMetadataFlowSrcPort_Object((1,3,6,1,4,1,9,9,789,1,1,1,8),_CfmMetadataFlowSrcPort_Type())
cfmMetadataFlowSrcPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmMetadataFlowSrcPort.setStatus(_B)
class _CfmMetadataFlowSSRC_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CfmMetadataFlowSSRC_Type.__name__=_E
_CfmMetadataFlowSSRC_Object=MibTableColumn
cfmMetadataFlowSSRC=_CfmMetadataFlowSSRC_Object((1,3,6,1,4,1,9,9,789,1,1,1,9),_CfmMetadataFlowSSRC_Type())
cfmMetadataFlowSSRC.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmMetadataFlowSSRC.setStatus(_B)
_CfmMetadataFlowAttrTable_Object=MibTable
cfmMetadataFlowAttrTable=_CfmMetadataFlowAttrTable_Object((1,3,6,1,4,1,9,9,789,1,2))
if mibBuilder.loadTexts:cfmMetadataFlowAttrTable.setStatus(_D)
_CfmMetadataFlowAttrEntry_Object=MibTableRow
cfmMetadataFlowAttrEntry=_CfmMetadataFlowAttrEntry_Object((1,3,6,1,4,1,9,9,789,1,2,1))
cfmMetadataFlowAttrEntry.setIndexNames((0,_A,_F),(0,_A,_H))
if mibBuilder.loadTexts:cfmMetadataFlowAttrEntry.setStatus(_D)
_CfmMetadataFlowAttrType_Type=CfmMetadataFlowAttributeType
_CfmMetadataFlowAttrType_Object=MibTableColumn
cfmMetadataFlowAttrType=_CfmMetadataFlowAttrType_Object((1,3,6,1,4,1,9,9,789,1,2,1,1),_CfmMetadataFlowAttrType_Type())
cfmMetadataFlowAttrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmMetadataFlowAttrType.setStatus(_D)
_CfmMetadataFlowAttrValue_Type=CfmMetadataFlowAttrVal
_CfmMetadataFlowAttrValue_Object=MibTableColumn
cfmMetadataFlowAttrValue=_CfmMetadataFlowAttrValue_Object((1,3,6,1,4,1,9,9,789,1,2,1,2),_CfmMetadataFlowAttrValue_Type())
cfmMetadataFlowAttrValue.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmMetadataFlowAttrValue.setStatus(_D)
_CfmMetadataFlowAllAttrTable_Object=MibTable
cfmMetadataFlowAllAttrTable=_CfmMetadataFlowAllAttrTable_Object((1,3,6,1,4,1,9,9,789,1,3))
if mibBuilder.loadTexts:cfmMetadataFlowAllAttrTable.setStatus(_B)
_CfmMetadataFlowAllAttrEntry_Object=MibTableRow
cfmMetadataFlowAllAttrEntry=_CfmMetadataFlowAllAttrEntry_Object((1,3,6,1,4,1,9,9,789,1,3,1))
cfmMetadataFlowAllAttrEntry.setIndexNames((0,_A,_F),(0,_A,_S),(0,_A,_T))
if mibBuilder.loadTexts:cfmMetadataFlowAllAttrEntry.setStatus(_B)
class _CfmMetadataIpFixIeId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CfmMetadataIpFixIeId_Type.__name__=_E
_CfmMetadataIpFixIeId_Object=MibTableColumn
cfmMetadataIpFixIeId=_CfmMetadataIpFixIeId_Object((1,3,6,1,4,1,9,9,789,1,3,1,1),_CfmMetadataIpFixIeId_Type())
cfmMetadataIpFixIeId.setMaxAccess(_G)
if mibBuilder.loadTexts:cfmMetadataIpFixIeId.setStatus(_B)
class _CfmMetadataFlowAllAttrInstanceId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CfmMetadataFlowAllAttrInstanceId_Type.__name__=_E
_CfmMetadataFlowAllAttrInstanceId_Object=MibTableColumn
cfmMetadataFlowAllAttrInstanceId=_CfmMetadataFlowAllAttrInstanceId_Object((1,3,6,1,4,1,9,9,789,1,3,1,2),_CfmMetadataFlowAllAttrInstanceId_Type())
cfmMetadataFlowAllAttrInstanceId.setMaxAccess(_G)
if mibBuilder.loadTexts:cfmMetadataFlowAllAttrInstanceId.setStatus(_B)
class _CfmMetadataFlowAllAttrValue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CfmMetadataFlowAllAttrValue_Type.__name__=_Q
_CfmMetadataFlowAllAttrValue_Object=MibTableColumn
cfmMetadataFlowAllAttrValue=_CfmMetadataFlowAllAttrValue_Object((1,3,6,1,4,1,9,9,789,1,3,1,3),_CfmMetadataFlowAllAttrValue_Type())
cfmMetadataFlowAllAttrValue.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmMetadataFlowAllAttrValue.setStatus(_B)
class _CfmMetadataFlowAllAttrPen_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CfmMetadataFlowAllAttrPen_Type.__name__=_E
_CfmMetadataFlowAllAttrPen_Object=MibTableColumn
cfmMetadataFlowAllAttrPen=_CfmMetadataFlowAllAttrPen_Object((1,3,6,1,4,1,9,9,789,1,3,1,4),_CfmMetadataFlowAllAttrPen_Type())
cfmMetadataFlowAllAttrPen.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmMetadataFlowAllAttrPen.setStatus(_B)
_CFlowMetadataMIBConform_ObjectIdentity=ObjectIdentity
cFlowMetadataMIBConform=_CFlowMetadataMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,789,2))
_CfmMetadataMIBCompliances_ObjectIdentity=ObjectIdentity
cfmMetadataMIBCompliances=_CfmMetadataMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,789,2,1))
_CfmMetadataMIBGroups_ObjectIdentity=ObjectIdentity
cfmMetadataMIBGroups=_CfmMetadataMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,789,2,2))
cfmMetadateFlowInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,789,2,2,1))
cfmMetadateFlowInfoGroup.setObjects(*((_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_H),(_A,_U)))
if mibBuilder.loadTexts:cfmMetadateFlowInfoGroup.setStatus(_D)
cfmMetadateFlowInfoGroupV2=ObjectGroup((1,3,6,1,4,1,9,9,789,2,2,2))
cfmMetadateFlowInfoGroupV2.setObjects(*((_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_V),(_A,_W)))
if mibBuilder.loadTexts:cfmMetadateFlowInfoGroupV2.setStatus(_B)
cfmMetadataMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,789,2,1,1))
cfmMetadataMIBCompliance.setObjects((_A,_X))
if mibBuilder.loadTexts:cfmMetadataMIBCompliance.setStatus(_D)
cfmMetadataMIBComplianceV2=ModuleCompliance((1,3,6,1,4,1,9,9,789,2,1,2))
cfmMetadataMIBComplianceV2.setObjects((_A,_Y))
if mibBuilder.loadTexts:cfmMetadataMIBComplianceV2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'CfmMetadataFlowAttributeType':CfmMetadataFlowAttributeType,'CfmMetadataFlowAttrVal':CfmMetadataFlowAttrVal,'ciscoFlowMetadataMIB':ciscoFlowMetadataMIB,'cFlowMetadataMIBNotifs':cFlowMetadataMIBNotifs,'cFlowMetadataMIBObjects':cFlowMetadataMIBObjects,'cfmMetadataFlowTable':cfmMetadataFlowTable,'cfmMetadataFlowEntry':cfmMetadataFlowEntry,_F:cfmMetadataFlowId,_I:cfmMetadataFlowProtocolType,_J:cfmMetadataFlowDestAddrType,_K:cfmMetadataFlowDestAddr,_L:cfmMetadataFlowDestPort,_M:cfmMetadataFlowSrcAddrType,_N:cfmMetadataFlowSrcAddr,_O:cfmMetadataFlowSrcPort,_P:cfmMetadataFlowSSRC,'cfmMetadataFlowAttrTable':cfmMetadataFlowAttrTable,'cfmMetadataFlowAttrEntry':cfmMetadataFlowAttrEntry,_H:cfmMetadataFlowAttrType,_U:cfmMetadataFlowAttrValue,'cfmMetadataFlowAllAttrTable':cfmMetadataFlowAllAttrTable,'cfmMetadataFlowAllAttrEntry':cfmMetadataFlowAllAttrEntry,_S:cfmMetadataIpFixIeId,_T:cfmMetadataFlowAllAttrInstanceId,_V:cfmMetadataFlowAllAttrValue,_W:cfmMetadataFlowAllAttrPen,'cFlowMetadataMIBConform':cFlowMetadataMIBConform,'cfmMetadataMIBCompliances':cfmMetadataMIBCompliances,'cfmMetadataMIBCompliance':cfmMetadataMIBCompliance,'cfmMetadataMIBComplianceV2':cfmMetadataMIBComplianceV2,'cfmMetadataMIBGroups':cfmMetadataMIBGroups,_X:cfmMetadateFlowInfoGroup,_Y:cfmMetadateFlowInfoGroupV2})