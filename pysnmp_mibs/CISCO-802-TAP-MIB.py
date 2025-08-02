_V='cisco802TapStreamGroup'
_U='c802tapStreamStatus'
_T='c802tapStreamDestinationLlcSap'
_S='c802tapStreamSourceLlcSap'
_R='c802tapStreamEthernetPid'
_Q='c802tapStreamSourceAddress'
_P='c802tapStreamDestinationAddress'
_O='c802tapStreamInterface'
_N='c802tapStreamFields'
_M='c802tapStreamCapabilities'
_L='srcLlcSap'
_K='dstLlcSap'
_J='ethernetPid'
_I='interface'
_H='Integer32'
_G='cTap2StreamIndex'
_F='cTap2MediationContentId'
_E='Bits'
_D='CISCO-TAP2-MIB'
_C='read-create'
_B='CISCO-802-TAP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
cTap2MediationContentId,cTap2StreamIndex=mibBuilder.importSymbols(_D,_F,_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_E,'Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
cisco802TapMIB=ModuleIdentity((1,3,6,1,4,1,9,9,395))
if mibBuilder.loadTexts:cisco802TapMIB.setRevisions(('2004-03-11 00:00',))
_Cisco802TapMIBNotifs_ObjectIdentity=ObjectIdentity
cisco802TapMIBNotifs=_Cisco802TapMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,395,0))
_Cisco802TapMIBObjects_ObjectIdentity=ObjectIdentity
cisco802TapMIBObjects=_Cisco802TapMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,395,1))
_C802tapStreamEncodePacket_ObjectIdentity=ObjectIdentity
c802tapStreamEncodePacket=_C802tapStreamEncodePacket_ObjectIdentity((1,3,6,1,4,1,9,9,395,1,1))
class _C802tapStreamCapabilities_Type(Bits):namedValues=NamedValues(*(('tapEnable',0),(_I,1),('dstMacAddr',2),('srcMacAddr',3),(_J,4),(_K,5),(_L,6)))
_C802tapStreamCapabilities_Type.__name__=_E
_C802tapStreamCapabilities_Object=MibScalar
c802tapStreamCapabilities=_C802tapStreamCapabilities_Object((1,3,6,1,4,1,9,9,395,1,1,1),_C802tapStreamCapabilities_Type())
c802tapStreamCapabilities.setMaxAccess('read-only')
if mibBuilder.loadTexts:c802tapStreamCapabilities.setStatus(_A)
_C802tapStreamTable_Object=MibTable
c802tapStreamTable=_C802tapStreamTable_Object((1,3,6,1,4,1,9,9,395,1,1,2))
if mibBuilder.loadTexts:c802tapStreamTable.setStatus(_A)
_C802tapStreamEntry_Object=MibTableRow
c802tapStreamEntry=_C802tapStreamEntry_Object((1,3,6,1,4,1,9,9,395,1,1,2,1))
c802tapStreamEntry.setIndexNames((0,_D,_F),(0,_D,_G))
if mibBuilder.loadTexts:c802tapStreamEntry.setStatus(_A)
class _C802tapStreamFields_Type(Bits):namedValues=NamedValues(*((_I,0),('dstMacAddress',1),('srcMacAddress',2),(_J,3),(_K,4),(_L,5)))
_C802tapStreamFields_Type.__name__=_E
_C802tapStreamFields_Object=MibTableColumn
c802tapStreamFields=_C802tapStreamFields_Object((1,3,6,1,4,1,9,9,395,1,1,2,1,1),_C802tapStreamFields_Type())
c802tapStreamFields.setMaxAccess(_C)
if mibBuilder.loadTexts:c802tapStreamFields.setStatus(_A)
class _C802tapStreamInterface_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,0),ValueRangeConstraint(1,2147483647))
_C802tapStreamInterface_Type.__name__=_H
_C802tapStreamInterface_Object=MibTableColumn
c802tapStreamInterface=_C802tapStreamInterface_Object((1,3,6,1,4,1,9,9,395,1,1,2,1,2),_C802tapStreamInterface_Type())
c802tapStreamInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:c802tapStreamInterface.setStatus(_A)
_C802tapStreamDestinationAddress_Type=MacAddress
_C802tapStreamDestinationAddress_Object=MibTableColumn
c802tapStreamDestinationAddress=_C802tapStreamDestinationAddress_Object((1,3,6,1,4,1,9,9,395,1,1,2,1,3),_C802tapStreamDestinationAddress_Type())
c802tapStreamDestinationAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:c802tapStreamDestinationAddress.setStatus(_A)
_C802tapStreamSourceAddress_Type=MacAddress
_C802tapStreamSourceAddress_Object=MibTableColumn
c802tapStreamSourceAddress=_C802tapStreamSourceAddress_Object((1,3,6,1,4,1,9,9,395,1,1,2,1,4),_C802tapStreamSourceAddress_Type())
c802tapStreamSourceAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:c802tapStreamSourceAddress.setStatus(_A)
_C802tapStreamEthernetPid_Type=Unsigned32
_C802tapStreamEthernetPid_Object=MibTableColumn
c802tapStreamEthernetPid=_C802tapStreamEthernetPid_Object((1,3,6,1,4,1,9,9,395,1,1,2,1,5),_C802tapStreamEthernetPid_Type())
c802tapStreamEthernetPid.setMaxAccess(_C)
if mibBuilder.loadTexts:c802tapStreamEthernetPid.setStatus(_A)
_C802tapStreamDestinationLlcSap_Type=Unsigned32
_C802tapStreamDestinationLlcSap_Object=MibTableColumn
c802tapStreamDestinationLlcSap=_C802tapStreamDestinationLlcSap_Object((1,3,6,1,4,1,9,9,395,1,1,2,1,6),_C802tapStreamDestinationLlcSap_Type())
c802tapStreamDestinationLlcSap.setMaxAccess(_C)
if mibBuilder.loadTexts:c802tapStreamDestinationLlcSap.setStatus(_A)
_C802tapStreamSourceLlcSap_Type=Unsigned32
_C802tapStreamSourceLlcSap_Object=MibTableColumn
c802tapStreamSourceLlcSap=_C802tapStreamSourceLlcSap_Object((1,3,6,1,4,1,9,9,395,1,1,2,1,7),_C802tapStreamSourceLlcSap_Type())
c802tapStreamSourceLlcSap.setMaxAccess(_C)
if mibBuilder.loadTexts:c802tapStreamSourceLlcSap.setStatus(_A)
_C802tapStreamStatus_Type=RowStatus
_C802tapStreamStatus_Object=MibTableColumn
c802tapStreamStatus=_C802tapStreamStatus_Object((1,3,6,1,4,1,9,9,395,1,1,2,1,8),_C802tapStreamStatus_Type())
c802tapStreamStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:c802tapStreamStatus.setStatus(_A)
_Cisco802TapMIBConform_ObjectIdentity=ObjectIdentity
cisco802TapMIBConform=_Cisco802TapMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,395,2))
_Cisco802TapMIBCompliances_ObjectIdentity=ObjectIdentity
cisco802TapMIBCompliances=_Cisco802TapMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,395,2,1))
_Cisco802TapMIBGroups_ObjectIdentity=ObjectIdentity
cisco802TapMIBGroups=_Cisco802TapMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,395,2,2))
cisco802TapStreamGroup=ObjectGroup((1,3,6,1,4,1,9,9,395,2,2,1))
cisco802TapStreamGroup.setObjects(*((_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:cisco802TapStreamGroup.setStatus(_A)
cisco802TapMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,395,2,1,1))
cisco802TapMIBCompliance.setObjects((_B,_V))
if mibBuilder.loadTexts:cisco802TapMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'cisco802TapMIB':cisco802TapMIB,'cisco802TapMIBNotifs':cisco802TapMIBNotifs,'cisco802TapMIBObjects':cisco802TapMIBObjects,'c802tapStreamEncodePacket':c802tapStreamEncodePacket,_M:c802tapStreamCapabilities,'c802tapStreamTable':c802tapStreamTable,'c802tapStreamEntry':c802tapStreamEntry,_N:c802tapStreamFields,_O:c802tapStreamInterface,_P:c802tapStreamDestinationAddress,_Q:c802tapStreamSourceAddress,_R:c802tapStreamEthernetPid,_T:c802tapStreamDestinationLlcSap,_S:c802tapStreamSourceLlcSap,_U:c802tapStreamStatus,'cisco802TapMIBConform':cisco802TapMIBConform,'cisco802TapMIBCompliances':cisco802TapMIBCompliances,'cisco802TapMIBCompliance':cisco802TapMIBCompliance,'cisco802TapMIBGroups':cisco802TapMIBGroups,_V:cisco802TapStreamGroup})