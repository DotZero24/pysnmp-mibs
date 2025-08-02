_J='active'
_I='passive'
_H='ifIndex'
_G='IF-MIB'
_F='OctetString'
_E='supported'
_D='not-supported'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_G,_H)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ethernetOamDiscoveryInfo,=mibBuilder.importSymbols('TPLINK-ETHERNETOAM-MIB','ethernetOamDiscoveryInfo')
_EthernetOamDiscInfoTable_Object=MibTable
ethernetOamDiscInfoTable=_EthernetOamDiscInfoTable_Object((1,3,6,1,4,1,11863,6,60,1,5,1))
if mibBuilder.loadTexts:ethernetOamDiscInfoTable.setStatus(_A)
_EthernetOamDiscInfoEntry_Object=MibTableRow
ethernetOamDiscInfoEntry=_EthernetOamDiscInfoEntry_Object((1,3,6,1,4,1,11863,6,60,1,5,1,1))
ethernetOamDiscInfoEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:ethernetOamDiscInfoEntry.setStatus(_A)
_EthernetOamDiscInfoPort_Type=DisplayString
_EthernetOamDiscInfoPort_Object=MibTableColumn
ethernetOamDiscInfoPort=_EthernetOamDiscInfoPort_Object((1,3,6,1,4,1,11863,6,60,1,5,1,1,1),_EthernetOamDiscInfoPort_Type())
ethernetOamDiscInfoPort.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetOamDiscInfoPort.setStatus(_A)
class _EthernetOamDiscInfoLocOAM_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disabled',0),('enabled',1)))
_EthernetOamDiscInfoLocOAM_Type.__name__=_C
_EthernetOamDiscInfoLocOAM_Object=MibTableColumn
ethernetOamDiscInfoLocOAM=_EthernetOamDiscInfoLocOAM_Object((1,3,6,1,4,1,11863,6,60,1,5,1,1,2),_EthernetOamDiscInfoLocOAM_Type())
ethernetOamDiscInfoLocOAM.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetOamDiscInfoLocOAM.setStatus(_A)
class _EthernetOamDiscInfoLocMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_EthernetOamDiscInfoLocMode_Type.__name__=_C
_EthernetOamDiscInfoLocMode_Object=MibTableColumn
ethernetOamDiscInfoLocMode=_EthernetOamDiscInfoLocMode_Object((1,3,6,1,4,1,11863,6,60,1,5,1,1,3),_EthernetOamDiscInfoLocMode_Type())
ethernetOamDiscInfoLocMode.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetOamDiscInfoLocMode.setStatus(_A)
_EthernetOamDiscInfoLocMaxOAMPDU_Type=Integer32
_EthernetOamDiscInfoLocMaxOAMPDU_Object=MibTableColumn
ethernetOamDiscInfoLocMaxOAMPDU=_EthernetOamDiscInfoLocMaxOAMPDU_Object((1,3,6,1,4,1,11863,6,60,1,5,1,1,4),_EthernetOamDiscInfoLocMaxOAMPDU_Type())
ethernetOamDiscInfoLocMaxOAMPDU.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetOamDiscInfoLocMaxOAMPDU.setStatus(_A)
class _EthernetOamDiscInfoLocRemoteLoopback_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_EthernetOamDiscInfoLocRemoteLoopback_Type.__name__=_C
_EthernetOamDiscInfoLocRemoteLoopback_Object=MibTableColumn
ethernetOamDiscInfoLocRemoteLoopback=_EthernetOamDiscInfoLocRemoteLoopback_Object((1,3,6,1,4,1,11863,6,60,1,5,1,1,5),_EthernetOamDiscInfoLocRemoteLoopback_Type())
ethernetOamDiscInfoLocRemoteLoopback.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetOamDiscInfoLocRemoteLoopback.setStatus(_A)
class _EthernetOamDiscInfoLocUnidirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_EthernetOamDiscInfoLocUnidirection_Type.__name__=_C
_EthernetOamDiscInfoLocUnidirection_Object=MibTableColumn
ethernetOamDiscInfoLocUnidirection=_EthernetOamDiscInfoLocUnidirection_Object((1,3,6,1,4,1,11863,6,60,1,5,1,1,6),_EthernetOamDiscInfoLocUnidirection_Type())
ethernetOamDiscInfoLocUnidirection.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetOamDiscInfoLocUnidirection.setStatus(_A)
class _EthernetOamDiscInfoLocLinkMonitoring_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_EthernetOamDiscInfoLocLinkMonitoring_Type.__name__=_C
_EthernetOamDiscInfoLocLinkMonitoring_Object=MibTableColumn
ethernetOamDiscInfoLocLinkMonitoring=_EthernetOamDiscInfoLocLinkMonitoring_Object((1,3,6,1,4,1,11863,6,60,1,5,1,1,7),_EthernetOamDiscInfoLocLinkMonitoring_Type())
ethernetOamDiscInfoLocLinkMonitoring.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetOamDiscInfoLocLinkMonitoring.setStatus(_A)
class _EthernetOamDiscInfoLocVariableRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_EthernetOamDiscInfoLocVariableRequest_Type.__name__=_C
_EthernetOamDiscInfoLocVariableRequest_Object=MibTableColumn
ethernetOamDiscInfoLocVariableRequest=_EthernetOamDiscInfoLocVariableRequest_Object((1,3,6,1,4,1,11863,6,60,1,5,1,1,8),_EthernetOamDiscInfoLocVariableRequest_Type())
ethernetOamDiscInfoLocVariableRequest.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetOamDiscInfoLocVariableRequest.setStatus(_A)
_EthernetOamDiscInfoLocPduRevision_Type=Integer32
_EthernetOamDiscInfoLocPduRevision_Object=MibTableColumn
ethernetOamDiscInfoLocPduRevision=_EthernetOamDiscInfoLocPduRevision_Object((1,3,6,1,4,1,11863,6,60,1,5,1,1,9),_EthernetOamDiscInfoLocPduRevision_Type())
ethernetOamDiscInfoLocPduRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetOamDiscInfoLocPduRevision.setStatus(_A)
class _EthernetOamDiscInfoLocOperationStatus_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,25))
_EthernetOamDiscInfoLocOperationStatus_Type.__name__=_F
_EthernetOamDiscInfoLocOperationStatus_Object=MibTableColumn
ethernetOamDiscInfoLocOperationStatus=_EthernetOamDiscInfoLocOperationStatus_Object((1,3,6,1,4,1,11863,6,60,1,5,1,1,10),_EthernetOamDiscInfoLocOperationStatus_Type())
ethernetOamDiscInfoLocOperationStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetOamDiscInfoLocOperationStatus.setStatus(_A)
class _EthernetOamDiscInfoLocLoopbackStatus_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_EthernetOamDiscInfoLocLoopbackStatus_Type.__name__=_F
_EthernetOamDiscInfoLocLoopbackStatus_Object=MibTableColumn
ethernetOamDiscInfoLocLoopbackStatus=_EthernetOamDiscInfoLocLoopbackStatus_Object((1,3,6,1,4,1,11863,6,60,1,5,1,1,11),_EthernetOamDiscInfoLocLoopbackStatus_Type())
ethernetOamDiscInfoLocLoopbackStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetOamDiscInfoLocLoopbackStatus.setStatus(_A)
class _EthernetOamDiscInfoRmtMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_EthernetOamDiscInfoRmtMode_Type.__name__=_C
_EthernetOamDiscInfoRmtMode_Object=MibTableColumn
ethernetOamDiscInfoRmtMode=_EthernetOamDiscInfoRmtMode_Object((1,3,6,1,4,1,11863,6,60,1,5,1,1,12),_EthernetOamDiscInfoRmtMode_Type())
ethernetOamDiscInfoRmtMode.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetOamDiscInfoRmtMode.setStatus(_A)
class _EthernetOamDiscInfoRmtMacAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,18))
_EthernetOamDiscInfoRmtMacAddress_Type.__name__=_F
_EthernetOamDiscInfoRmtMacAddress_Object=MibTableColumn
ethernetOamDiscInfoRmtMacAddress=_EthernetOamDiscInfoRmtMacAddress_Object((1,3,6,1,4,1,11863,6,60,1,5,1,1,13),_EthernetOamDiscInfoRmtMacAddress_Type())
ethernetOamDiscInfoRmtMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetOamDiscInfoRmtMacAddress.setStatus(_A)
class _EthernetOamDiscInfoRmtVendorOUI_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,7))
_EthernetOamDiscInfoRmtVendorOUI_Type.__name__=_F
_EthernetOamDiscInfoRmtVendorOUI_Object=MibTableColumn
ethernetOamDiscInfoRmtVendorOUI=_EthernetOamDiscInfoRmtVendorOUI_Object((1,3,6,1,4,1,11863,6,60,1,5,1,1,14),_EthernetOamDiscInfoRmtVendorOUI_Type())
ethernetOamDiscInfoRmtVendorOUI.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetOamDiscInfoRmtVendorOUI.setStatus(_A)
_EthernetOamDiscInfoRmtMaxOAMPDU_Type=Integer32
_EthernetOamDiscInfoRmtMaxOAMPDU_Object=MibTableColumn
ethernetOamDiscInfoRmtMaxOAMPDU=_EthernetOamDiscInfoRmtMaxOAMPDU_Object((1,3,6,1,4,1,11863,6,60,1,5,1,1,15),_EthernetOamDiscInfoRmtMaxOAMPDU_Type())
ethernetOamDiscInfoRmtMaxOAMPDU.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetOamDiscInfoRmtMaxOAMPDU.setStatus(_A)
class _EthernetOamDiscInfoRmtRemoteLoopback_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_EthernetOamDiscInfoRmtRemoteLoopback_Type.__name__=_C
_EthernetOamDiscInfoRmtRemoteLoopback_Object=MibTableColumn
ethernetOamDiscInfoRmtRemoteLoopback=_EthernetOamDiscInfoRmtRemoteLoopback_Object((1,3,6,1,4,1,11863,6,60,1,5,1,1,16),_EthernetOamDiscInfoRmtRemoteLoopback_Type())
ethernetOamDiscInfoRmtRemoteLoopback.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetOamDiscInfoRmtRemoteLoopback.setStatus(_A)
class _EthernetOamDiscInfoRmtUnidirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_EthernetOamDiscInfoRmtUnidirection_Type.__name__=_C
_EthernetOamDiscInfoRmtUnidirection_Object=MibTableColumn
ethernetOamDiscInfoRmtUnidirection=_EthernetOamDiscInfoRmtUnidirection_Object((1,3,6,1,4,1,11863,6,60,1,5,1,1,17),_EthernetOamDiscInfoRmtUnidirection_Type())
ethernetOamDiscInfoRmtUnidirection.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetOamDiscInfoRmtUnidirection.setStatus(_A)
class _EthernetOamDiscInfoRmtLinkMonitoring_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_EthernetOamDiscInfoRmtLinkMonitoring_Type.__name__=_C
_EthernetOamDiscInfoRmtLinkMonitoring_Object=MibTableColumn
ethernetOamDiscInfoRmtLinkMonitoring=_EthernetOamDiscInfoRmtLinkMonitoring_Object((1,3,6,1,4,1,11863,6,60,1,5,1,1,18),_EthernetOamDiscInfoRmtLinkMonitoring_Type())
ethernetOamDiscInfoRmtLinkMonitoring.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetOamDiscInfoRmtLinkMonitoring.setStatus(_A)
class _EthernetOamDiscInfoRmtVariableRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_EthernetOamDiscInfoRmtVariableRequest_Type.__name__=_C
_EthernetOamDiscInfoRmtVariableRequest_Object=MibTableColumn
ethernetOamDiscInfoRmtVariableRequest=_EthernetOamDiscInfoRmtVariableRequest_Object((1,3,6,1,4,1,11863,6,60,1,5,1,1,19),_EthernetOamDiscInfoRmtVariableRequest_Type())
ethernetOamDiscInfoRmtVariableRequest.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetOamDiscInfoRmtVariableRequest.setStatus(_A)
_EthernetOamDiscInfoRmtPduRevision_Type=Integer32
_EthernetOamDiscInfoRmtPduRevision_Object=MibTableColumn
ethernetOamDiscInfoRmtPduRevision=_EthernetOamDiscInfoRmtPduRevision_Object((1,3,6,1,4,1,11863,6,60,1,5,1,1,20),_EthernetOamDiscInfoRmtPduRevision_Type())
ethernetOamDiscInfoRmtPduRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetOamDiscInfoRmtPduRevision.setStatus(_A)
class _EthernetOamDiscInfoRmtVendorInfo_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,9))
_EthernetOamDiscInfoRmtVendorInfo_Type.__name__=_F
_EthernetOamDiscInfoRmtVendorInfo_Object=MibTableColumn
ethernetOamDiscInfoRmtVendorInfo=_EthernetOamDiscInfoRmtVendorInfo_Object((1,3,6,1,4,1,11863,6,60,1,5,1,1,21),_EthernetOamDiscInfoRmtVendorInfo_Type())
ethernetOamDiscInfoRmtVendorInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetOamDiscInfoRmtVendorInfo.setStatus(_A)
mibBuilder.exportSymbols('TPLINK-ETHERNETOAMDISCINFO-MIB',**{'ethernetOamDiscInfoTable':ethernetOamDiscInfoTable,'ethernetOamDiscInfoEntry':ethernetOamDiscInfoEntry,'ethernetOamDiscInfoPort':ethernetOamDiscInfoPort,'ethernetOamDiscInfoLocOAM':ethernetOamDiscInfoLocOAM,'ethernetOamDiscInfoLocMode':ethernetOamDiscInfoLocMode,'ethernetOamDiscInfoLocMaxOAMPDU':ethernetOamDiscInfoLocMaxOAMPDU,'ethernetOamDiscInfoLocRemoteLoopback':ethernetOamDiscInfoLocRemoteLoopback,'ethernetOamDiscInfoLocUnidirection':ethernetOamDiscInfoLocUnidirection,'ethernetOamDiscInfoLocLinkMonitoring':ethernetOamDiscInfoLocLinkMonitoring,'ethernetOamDiscInfoLocVariableRequest':ethernetOamDiscInfoLocVariableRequest,'ethernetOamDiscInfoLocPduRevision':ethernetOamDiscInfoLocPduRevision,'ethernetOamDiscInfoLocOperationStatus':ethernetOamDiscInfoLocOperationStatus,'ethernetOamDiscInfoLocLoopbackStatus':ethernetOamDiscInfoLocLoopbackStatus,'ethernetOamDiscInfoRmtMode':ethernetOamDiscInfoRmtMode,'ethernetOamDiscInfoRmtMacAddress':ethernetOamDiscInfoRmtMacAddress,'ethernetOamDiscInfoRmtVendorOUI':ethernetOamDiscInfoRmtVendorOUI,'ethernetOamDiscInfoRmtMaxOAMPDU':ethernetOamDiscInfoRmtMaxOAMPDU,'ethernetOamDiscInfoRmtRemoteLoopback':ethernetOamDiscInfoRmtRemoteLoopback,'ethernetOamDiscInfoRmtUnidirection':ethernetOamDiscInfoRmtUnidirection,'ethernetOamDiscInfoRmtLinkMonitoring':ethernetOamDiscInfoRmtLinkMonitoring,'ethernetOamDiscInfoRmtVariableRequest':ethernetOamDiscInfoRmtVariableRequest,'ethernetOamDiscInfoRmtPduRevision':ethernetOamDiscInfoRmtPduRevision,'ethernetOamDiscInfoRmtVendorInfo':ethernetOamDiscInfoRmtVendorInfo})