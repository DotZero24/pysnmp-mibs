_V='casa802TapStreamGroup'
_U='casa802tapStreamStatus'
_T='casa802tapStreamDestinationLlcSap'
_S='casa802tapStreamSourceLlcSap'
_R='casa802tapStreamEthernetPid'
_Q='casa802tapStreamSourceAddress'
_P='casa802tapStreamDestinationAddress'
_O='casa802tapStreamInterface'
_N='casa802tapStreamFields'
_M='casa802tapStreamCapabilities'
_L='casa802tapStreamIndex'
_K='srcLlcSap'
_J='dstLlcSap'
_I='ethernetPid'
_H='interface'
_G='pktcEScTapMediationContentId'
_F='PKTC-ES-TAP-MIB'
_E='Bits'
_D='Integer32'
_C='read-create'
_B='CASA-802-TAP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
casa,=mibBuilder.importSymbols('CASA-MIB','casa')
pktcEScTapMediationContentId,=mibBuilder.importSymbols(_F,_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_E,'Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
casa802TapMIB=ModuleIdentity((1,3,6,1,4,1,20858,10,19))
if mibBuilder.loadTexts:casa802TapMIB.setRevisions(('2008-11-19 11:11',))
_CasaMgmt_ObjectIdentity=ObjectIdentity
casaMgmt=_CasaMgmt_ObjectIdentity((1,3,6,1,4,1,20858,10))
_Casa802TapMIBNotifs_ObjectIdentity=ObjectIdentity
casa802TapMIBNotifs=_Casa802TapMIBNotifs_ObjectIdentity((1,3,6,1,4,1,20858,10,19,0))
_Casa802TapMIBObjects_ObjectIdentity=ObjectIdentity
casa802TapMIBObjects=_Casa802TapMIBObjects_ObjectIdentity((1,3,6,1,4,1,20858,10,19,1))
_Casa802tapStreamEncodePacket_ObjectIdentity=ObjectIdentity
casa802tapStreamEncodePacket=_Casa802tapStreamEncodePacket_ObjectIdentity((1,3,6,1,4,1,20858,10,19,1,1))
class _Casa802tapStreamCapabilities_Type(Bits):namedValues=NamedValues(*(('tapEnable',0),(_H,1),('dstMacAddr',2),('srcMacAddr',3),(_I,4),(_J,5),(_K,6)))
_Casa802tapStreamCapabilities_Type.__name__=_E
_Casa802tapStreamCapabilities_Object=MibScalar
casa802tapStreamCapabilities=_Casa802tapStreamCapabilities_Object((1,3,6,1,4,1,20858,10,19,1,1,1),_Casa802tapStreamCapabilities_Type())
casa802tapStreamCapabilities.setMaxAccess('read-only')
if mibBuilder.loadTexts:casa802tapStreamCapabilities.setStatus(_A)
_Casa802tapStreamTable_Object=MibTable
casa802tapStreamTable=_Casa802tapStreamTable_Object((1,3,6,1,4,1,20858,10,19,1,1,2))
if mibBuilder.loadTexts:casa802tapStreamTable.setStatus(_A)
_Casa802tapStreamEntry_Object=MibTableRow
casa802tapStreamEntry=_Casa802tapStreamEntry_Object((1,3,6,1,4,1,20858,10,19,1,1,2,1))
casa802tapStreamEntry.setIndexNames((0,_F,_G),(0,_B,_L))
if mibBuilder.loadTexts:casa802tapStreamEntry.setStatus(_A)
class _Casa802tapStreamIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_Casa802tapStreamIndex_Type.__name__=_D
_Casa802tapStreamIndex_Object=MibTableColumn
casa802tapStreamIndex=_Casa802tapStreamIndex_Object((1,3,6,1,4,1,20858,10,19,1,1,2,1,1),_Casa802tapStreamIndex_Type())
casa802tapStreamIndex.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:casa802tapStreamIndex.setStatus(_A)
class _Casa802tapStreamFields_Type(Bits):namedValues=NamedValues(*((_H,0),('dstMacAddress',1),('srcMacAddress',2),(_I,3),(_J,4),(_K,5)))
_Casa802tapStreamFields_Type.__name__=_E
_Casa802tapStreamFields_Object=MibTableColumn
casa802tapStreamFields=_Casa802tapStreamFields_Object((1,3,6,1,4,1,20858,10,19,1,1,2,1,2),_Casa802tapStreamFields_Type())
casa802tapStreamFields.setMaxAccess(_C)
if mibBuilder.loadTexts:casa802tapStreamFields.setStatus(_A)
class _Casa802tapStreamInterface_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,0),ValueRangeConstraint(1,2147483647))
_Casa802tapStreamInterface_Type.__name__=_D
_Casa802tapStreamInterface_Object=MibTableColumn
casa802tapStreamInterface=_Casa802tapStreamInterface_Object((1,3,6,1,4,1,20858,10,19,1,1,2,1,3),_Casa802tapStreamInterface_Type())
casa802tapStreamInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:casa802tapStreamInterface.setStatus(_A)
_Casa802tapStreamDestinationAddress_Type=MacAddress
_Casa802tapStreamDestinationAddress_Object=MibTableColumn
casa802tapStreamDestinationAddress=_Casa802tapStreamDestinationAddress_Object((1,3,6,1,4,1,20858,10,19,1,1,2,1,4),_Casa802tapStreamDestinationAddress_Type())
casa802tapStreamDestinationAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:casa802tapStreamDestinationAddress.setStatus(_A)
_Casa802tapStreamSourceAddress_Type=MacAddress
_Casa802tapStreamSourceAddress_Object=MibTableColumn
casa802tapStreamSourceAddress=_Casa802tapStreamSourceAddress_Object((1,3,6,1,4,1,20858,10,19,1,1,2,1,5),_Casa802tapStreamSourceAddress_Type())
casa802tapStreamSourceAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:casa802tapStreamSourceAddress.setStatus(_A)
_Casa802tapStreamEthernetPid_Type=Unsigned32
_Casa802tapStreamEthernetPid_Object=MibTableColumn
casa802tapStreamEthernetPid=_Casa802tapStreamEthernetPid_Object((1,3,6,1,4,1,20858,10,19,1,1,2,1,6),_Casa802tapStreamEthernetPid_Type())
casa802tapStreamEthernetPid.setMaxAccess(_C)
if mibBuilder.loadTexts:casa802tapStreamEthernetPid.setStatus(_A)
_Casa802tapStreamDestinationLlcSap_Type=Unsigned32
_Casa802tapStreamDestinationLlcSap_Object=MibTableColumn
casa802tapStreamDestinationLlcSap=_Casa802tapStreamDestinationLlcSap_Object((1,3,6,1,4,1,20858,10,19,1,1,2,1,7),_Casa802tapStreamDestinationLlcSap_Type())
casa802tapStreamDestinationLlcSap.setMaxAccess(_C)
if mibBuilder.loadTexts:casa802tapStreamDestinationLlcSap.setStatus(_A)
_Casa802tapStreamSourceLlcSap_Type=Unsigned32
_Casa802tapStreamSourceLlcSap_Object=MibTableColumn
casa802tapStreamSourceLlcSap=_Casa802tapStreamSourceLlcSap_Object((1,3,6,1,4,1,20858,10,19,1,1,2,1,8),_Casa802tapStreamSourceLlcSap_Type())
casa802tapStreamSourceLlcSap.setMaxAccess(_C)
if mibBuilder.loadTexts:casa802tapStreamSourceLlcSap.setStatus(_A)
class _Casa802tapStreamInterceptEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_Casa802tapStreamInterceptEnable_Type.__name__=_D
_Casa802tapStreamInterceptEnable_Object=MibTableColumn
casa802tapStreamInterceptEnable=_Casa802tapStreamInterceptEnable_Object((1,3,6,1,4,1,20858,10,19,1,1,2,1,9),_Casa802tapStreamInterceptEnable_Type())
casa802tapStreamInterceptEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:casa802tapStreamInterceptEnable.setStatus(_A)
_Casa802tapStreamStatus_Type=RowStatus
_Casa802tapStreamStatus_Object=MibTableColumn
casa802tapStreamStatus=_Casa802tapStreamStatus_Object((1,3,6,1,4,1,20858,10,19,1,1,2,1,10),_Casa802tapStreamStatus_Type())
casa802tapStreamStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:casa802tapStreamStatus.setStatus(_A)
_Casa802TapMIBConform_ObjectIdentity=ObjectIdentity
casa802TapMIBConform=_Casa802TapMIBConform_ObjectIdentity((1,3,6,1,4,1,20858,10,19,2))
_Casa802TapMIBCompliances_ObjectIdentity=ObjectIdentity
casa802TapMIBCompliances=_Casa802TapMIBCompliances_ObjectIdentity((1,3,6,1,4,1,20858,10,19,2,1))
_Casa802TapMIBGroups_ObjectIdentity=ObjectIdentity
casa802TapMIBGroups=_Casa802TapMIBGroups_ObjectIdentity((1,3,6,1,4,1,20858,10,19,2,2))
casa802TapStreamGroup=ObjectGroup((1,3,6,1,4,1,20858,10,19,2,2,1))
casa802TapStreamGroup.setObjects(*((_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:casa802TapStreamGroup.setStatus(_A)
casa802TapMIBCompliance=ModuleCompliance((1,3,6,1,4,1,20858,10,19,2,1,1))
casa802TapMIBCompliance.setObjects((_B,_V))
if mibBuilder.loadTexts:casa802TapMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'casaMgmt':casaMgmt,'casa802TapMIB':casa802TapMIB,'casa802TapMIBNotifs':casa802TapMIBNotifs,'casa802TapMIBObjects':casa802TapMIBObjects,'casa802tapStreamEncodePacket':casa802tapStreamEncodePacket,_M:casa802tapStreamCapabilities,'casa802tapStreamTable':casa802tapStreamTable,'casa802tapStreamEntry':casa802tapStreamEntry,_L:casa802tapStreamIndex,_N:casa802tapStreamFields,_O:casa802tapStreamInterface,_P:casa802tapStreamDestinationAddress,_Q:casa802tapStreamSourceAddress,_R:casa802tapStreamEthernetPid,_T:casa802tapStreamDestinationLlcSap,_S:casa802tapStreamSourceLlcSap,'casa802tapStreamInterceptEnable':casa802tapStreamInterceptEnable,_U:casa802tapStreamStatus,'casa802TapMIBConform':casa802TapMIBConform,'casa802TapMIBCompliances':casa802TapMIBCompliances,'casa802TapMIBCompliance':casa802TapMIBCompliance,'casa802TapMIBGroups':casa802TapMIBGroups,_V:casa802TapStreamGroup})