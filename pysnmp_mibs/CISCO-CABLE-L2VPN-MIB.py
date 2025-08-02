_U='ccl2vpnPWMappingGroup'
_T='ccl2vpnPWToL2vpnIndex'
_S='ccl2vpnMacVpnIdToL2vpnIndex'
_R='ccl2vpnPWVCID'
_Q='ccl2vpnPWType'
_P='ccl2vpnPWPeerIPAddress'
_O='ccl2vpnPWPeerIPAddressType'
_N='ccl2vpnPWVpnId'
_M='ccl2vpnPWMAC'
_L='ccl2vpnL2vpnIndex'
_K='ccl2vpnVCID'
_J='ccl2vpnPeerIPAddress'
_I='ccl2vpnPeerIPAddressType'
_H='ccl2vpnPseudoWireType'
_G='ccl2vpnVpnId'
_F='ccl2vpnMac'
_E='OctetString'
_D='not-accessible'
_C='read-only'
_B='CISCO-CABLE-L2VPN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CpwVcIDType,CpwVcType=mibBuilder.importSymbols('CISCO-IETF-PW-TC-MIB','CpwVcIDType','CpwVcType')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
ciscoCableL2vpnMIB=ModuleIdentity((1,3,6,1,4,1,9,9,700))
if mibBuilder.loadTexts:ciscoCableL2vpnMIB.setRevisions(('2009-06-17 00:00',))
class CiscoCableL2vpnIndex(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CiscoCableL2vpnMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoCableL2vpnMIBNotifs=_CiscoCableL2vpnMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,700,0))
_CiscoCableL2vpnMIBObjects_ObjectIdentity=ObjectIdentity
ciscoCableL2vpnMIBObjects=_CiscoCableL2vpnMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,700,1))
_Ccl2vpnMacVpnIdL2vpnIndexTable_Object=MibTable
ccl2vpnMacVpnIdL2vpnIndexTable=_Ccl2vpnMacVpnIdL2vpnIndexTable_Object((1,3,6,1,4,1,9,9,700,1,1))
if mibBuilder.loadTexts:ccl2vpnMacVpnIdL2vpnIndexTable.setStatus(_A)
_Ccl2vpnMacVpnIdL2vpnIndexEntry_Object=MibTableRow
ccl2vpnMacVpnIdL2vpnIndexEntry=_Ccl2vpnMacVpnIdL2vpnIndexEntry_Object((1,3,6,1,4,1,9,9,700,1,1,1))
ccl2vpnMacVpnIdL2vpnIndexEntry.setIndexNames((0,_B,_F),(1,_B,_G))
if mibBuilder.loadTexts:ccl2vpnMacVpnIdL2vpnIndexEntry.setStatus(_A)
_Ccl2vpnMac_Type=MacAddress
_Ccl2vpnMac_Object=MibTableColumn
ccl2vpnMac=_Ccl2vpnMac_Object((1,3,6,1,4,1,9,9,700,1,1,1,1),_Ccl2vpnMac_Type())
ccl2vpnMac.setMaxAccess(_D)
if mibBuilder.loadTexts:ccl2vpnMac.setStatus(_A)
class _Ccl2vpnVpnId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_Ccl2vpnVpnId_Type.__name__=_E
_Ccl2vpnVpnId_Object=MibTableColumn
ccl2vpnVpnId=_Ccl2vpnVpnId_Object((1,3,6,1,4,1,9,9,700,1,1,1,2),_Ccl2vpnVpnId_Type())
ccl2vpnVpnId.setMaxAccess(_D)
if mibBuilder.loadTexts:ccl2vpnVpnId.setStatus(_A)
_Ccl2vpnMacVpnIdToL2vpnIndex_Type=CiscoCableL2vpnIndex
_Ccl2vpnMacVpnIdToL2vpnIndex_Object=MibTableColumn
ccl2vpnMacVpnIdToL2vpnIndex=_Ccl2vpnMacVpnIdToL2vpnIndex_Object((1,3,6,1,4,1,9,9,700,1,1,1,3),_Ccl2vpnMacVpnIdToL2vpnIndex_Type())
ccl2vpnMacVpnIdToL2vpnIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ccl2vpnMacVpnIdToL2vpnIndex.setStatus(_A)
_Ccl2vpnPWL2vpnIndexTable_Object=MibTable
ccl2vpnPWL2vpnIndexTable=_Ccl2vpnPWL2vpnIndexTable_Object((1,3,6,1,4,1,9,9,700,1,2))
if mibBuilder.loadTexts:ccl2vpnPWL2vpnIndexTable.setStatus(_A)
_Ccl2vpnPWL2vpnIndexEntry_Object=MibTableRow
ccl2vpnPWL2vpnIndexEntry=_Ccl2vpnPWL2vpnIndexEntry_Object((1,3,6,1,4,1,9,9,700,1,2,1))
ccl2vpnPWL2vpnIndexEntry.setIndexNames((0,_B,_H),(0,_B,_I),(0,_B,_J),(0,_B,_K))
if mibBuilder.loadTexts:ccl2vpnPWL2vpnIndexEntry.setStatus(_A)
_Ccl2vpnPseudoWireType_Type=CpwVcType
_Ccl2vpnPseudoWireType_Object=MibTableColumn
ccl2vpnPseudoWireType=_Ccl2vpnPseudoWireType_Object((1,3,6,1,4,1,9,9,700,1,2,1,1),_Ccl2vpnPseudoWireType_Type())
ccl2vpnPseudoWireType.setMaxAccess(_D)
if mibBuilder.loadTexts:ccl2vpnPseudoWireType.setStatus(_A)
_Ccl2vpnPeerIPAddressType_Type=InetAddressType
_Ccl2vpnPeerIPAddressType_Object=MibTableColumn
ccl2vpnPeerIPAddressType=_Ccl2vpnPeerIPAddressType_Object((1,3,6,1,4,1,9,9,700,1,2,1,2),_Ccl2vpnPeerIPAddressType_Type())
ccl2vpnPeerIPAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:ccl2vpnPeerIPAddressType.setStatus(_A)
_Ccl2vpnPeerIPAddress_Type=InetAddress
_Ccl2vpnPeerIPAddress_Object=MibTableColumn
ccl2vpnPeerIPAddress=_Ccl2vpnPeerIPAddress_Object((1,3,6,1,4,1,9,9,700,1,2,1,3),_Ccl2vpnPeerIPAddress_Type())
ccl2vpnPeerIPAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:ccl2vpnPeerIPAddress.setStatus(_A)
_Ccl2vpnVCID_Type=CpwVcIDType
_Ccl2vpnVCID_Object=MibTableColumn
ccl2vpnVCID=_Ccl2vpnVCID_Object((1,3,6,1,4,1,9,9,700,1,2,1,4),_Ccl2vpnVCID_Type())
ccl2vpnVCID.setMaxAccess(_D)
if mibBuilder.loadTexts:ccl2vpnVCID.setStatus(_A)
_Ccl2vpnPWToL2vpnIndex_Type=CiscoCableL2vpnIndex
_Ccl2vpnPWToL2vpnIndex_Object=MibTableColumn
ccl2vpnPWToL2vpnIndex=_Ccl2vpnPWToL2vpnIndex_Object((1,3,6,1,4,1,9,9,700,1,2,1,5),_Ccl2vpnPWToL2vpnIndex_Type())
ccl2vpnPWToL2vpnIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ccl2vpnPWToL2vpnIndex.setStatus(_A)
_Ccl2vpnL2vpnIndexPWTable_Object=MibTable
ccl2vpnL2vpnIndexPWTable=_Ccl2vpnL2vpnIndexPWTable_Object((1,3,6,1,4,1,9,9,700,1,3))
if mibBuilder.loadTexts:ccl2vpnL2vpnIndexPWTable.setStatus(_A)
_Ccl2vpnL2vpnIndexPWEntry_Object=MibTableRow
ccl2vpnL2vpnIndexPWEntry=_Ccl2vpnL2vpnIndexPWEntry_Object((1,3,6,1,4,1,9,9,700,1,3,1))
ccl2vpnL2vpnIndexPWEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:ccl2vpnL2vpnIndexPWEntry.setStatus(_A)
_Ccl2vpnL2vpnIndex_Type=CiscoCableL2vpnIndex
_Ccl2vpnL2vpnIndex_Object=MibTableColumn
ccl2vpnL2vpnIndex=_Ccl2vpnL2vpnIndex_Object((1,3,6,1,4,1,9,9,700,1,3,1,1),_Ccl2vpnL2vpnIndex_Type())
ccl2vpnL2vpnIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ccl2vpnL2vpnIndex.setStatus(_A)
_Ccl2vpnPWMAC_Type=MacAddress
_Ccl2vpnPWMAC_Object=MibTableColumn
ccl2vpnPWMAC=_Ccl2vpnPWMAC_Object((1,3,6,1,4,1,9,9,700,1,3,1,2),_Ccl2vpnPWMAC_Type())
ccl2vpnPWMAC.setMaxAccess(_C)
if mibBuilder.loadTexts:ccl2vpnPWMAC.setStatus(_A)
class _Ccl2vpnPWVpnId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_Ccl2vpnPWVpnId_Type.__name__=_E
_Ccl2vpnPWVpnId_Object=MibTableColumn
ccl2vpnPWVpnId=_Ccl2vpnPWVpnId_Object((1,3,6,1,4,1,9,9,700,1,3,1,3),_Ccl2vpnPWVpnId_Type())
ccl2vpnPWVpnId.setMaxAccess(_C)
if mibBuilder.loadTexts:ccl2vpnPWVpnId.setStatus(_A)
_Ccl2vpnPWPeerIPAddressType_Type=InetAddressType
_Ccl2vpnPWPeerIPAddressType_Object=MibTableColumn
ccl2vpnPWPeerIPAddressType=_Ccl2vpnPWPeerIPAddressType_Object((1,3,6,1,4,1,9,9,700,1,3,1,4),_Ccl2vpnPWPeerIPAddressType_Type())
ccl2vpnPWPeerIPAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:ccl2vpnPWPeerIPAddressType.setStatus(_A)
_Ccl2vpnPWPeerIPAddress_Type=InetAddress
_Ccl2vpnPWPeerIPAddress_Object=MibTableColumn
ccl2vpnPWPeerIPAddress=_Ccl2vpnPWPeerIPAddress_Object((1,3,6,1,4,1,9,9,700,1,3,1,5),_Ccl2vpnPWPeerIPAddress_Type())
ccl2vpnPWPeerIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ccl2vpnPWPeerIPAddress.setStatus(_A)
_Ccl2vpnPWType_Type=CpwVcType
_Ccl2vpnPWType_Object=MibTableColumn
ccl2vpnPWType=_Ccl2vpnPWType_Object((1,3,6,1,4,1,9,9,700,1,3,1,6),_Ccl2vpnPWType_Type())
ccl2vpnPWType.setMaxAccess(_C)
if mibBuilder.loadTexts:ccl2vpnPWType.setStatus(_A)
_Ccl2vpnPWVCID_Type=CpwVcIDType
_Ccl2vpnPWVCID_Object=MibTableColumn
ccl2vpnPWVCID=_Ccl2vpnPWVCID_Object((1,3,6,1,4,1,9,9,700,1,3,1,7),_Ccl2vpnPWVCID_Type())
ccl2vpnPWVCID.setMaxAccess(_C)
if mibBuilder.loadTexts:ccl2vpnPWVCID.setStatus(_A)
_CiscoCableL2vpnMIBConform_ObjectIdentity=ObjectIdentity
ciscoCableL2vpnMIBConform=_CiscoCableL2vpnMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,700,2))
_Ccl2vpnMIBCompliances_ObjectIdentity=ObjectIdentity
ccl2vpnMIBCompliances=_Ccl2vpnMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,700,2,1))
_Ccl2vpnMIBGroups_ObjectIdentity=ObjectIdentity
ccl2vpnMIBGroups=_Ccl2vpnMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,700,2,2))
ccl2vpnPWMappingGroup=ObjectGroup((1,3,6,1,4,1,9,9,700,2,2,1))
ccl2vpnPWMappingGroup.setObjects(*((_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:ccl2vpnPWMappingGroup.setStatus(_A)
ccl2vpnMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,700,2,1,1))
ccl2vpnMIBCompliance.setObjects((_B,_U))
if mibBuilder.loadTexts:ccl2vpnMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CiscoCableL2vpnIndex':CiscoCableL2vpnIndex,'ciscoCableL2vpnMIB':ciscoCableL2vpnMIB,'ciscoCableL2vpnMIBNotifs':ciscoCableL2vpnMIBNotifs,'ciscoCableL2vpnMIBObjects':ciscoCableL2vpnMIBObjects,'ccl2vpnMacVpnIdL2vpnIndexTable':ccl2vpnMacVpnIdL2vpnIndexTable,'ccl2vpnMacVpnIdL2vpnIndexEntry':ccl2vpnMacVpnIdL2vpnIndexEntry,_F:ccl2vpnMac,_G:ccl2vpnVpnId,_S:ccl2vpnMacVpnIdToL2vpnIndex,'ccl2vpnPWL2vpnIndexTable':ccl2vpnPWL2vpnIndexTable,'ccl2vpnPWL2vpnIndexEntry':ccl2vpnPWL2vpnIndexEntry,_H:ccl2vpnPseudoWireType,_I:ccl2vpnPeerIPAddressType,_J:ccl2vpnPeerIPAddress,_K:ccl2vpnVCID,_T:ccl2vpnPWToL2vpnIndex,'ccl2vpnL2vpnIndexPWTable':ccl2vpnL2vpnIndexPWTable,'ccl2vpnL2vpnIndexPWEntry':ccl2vpnL2vpnIndexPWEntry,_L:ccl2vpnL2vpnIndex,_M:ccl2vpnPWMAC,_N:ccl2vpnPWVpnId,_O:ccl2vpnPWPeerIPAddressType,_P:ccl2vpnPWPeerIPAddress,_Q:ccl2vpnPWType,_R:ccl2vpnPWVCID,'ciscoCableL2vpnMIBConform':ciscoCableL2vpnMIBConform,'ccl2vpnMIBCompliances':ccl2vpnMIBCompliances,'ccl2vpnMIBCompliance':ccl2vpnMIBCompliance,'ccl2vpnMIBGroups':ccl2vpnMIBGroups,_U:ccl2vpnPWMappingGroup})