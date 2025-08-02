_AE='ciscoCdpV2IfExtGroup'
_AD='ciscoCdpV2MIBGroup'
_AC='ciscoCdpCtAddressGroup'
_AB='ciscoCdpMIBGroupV12R03'
_AA='ciscoCdpMIBGroupV11R02'
_A9='ciscoCdpMIBGroupV11R01'
_A8='ciscoCdpMIBGroup'
_A7='cdpInterfaceName'
_A6='cdpCtAddress'
_A5='cdpCtAddressType'
_A4='cdpInterfaceCosForUntrustedPort'
_A3='cdpInterfaceExtendedTrust'
_A2='cdpGlobalDeviceIdFormat'
_A1='cdpGlobalDeviceIdFormatCpb'
_A0='cdpGlobalLastChange'
_z='cdpCacheSecondaryMgmtAddr'
_y='cdpCacheSecondaryMgmtAddrType'
_x='cdpCachePrimaryMgmtAddr'
_w='cdpCachePrimaryMgmtAddrType'
_v='cdpCachePhysLocation'
_u='cdpCacheLastChange'
_t='cdpCacheSysObjectID'
_s='cdpCacheSysName'
_r='cdpCacheMTU'
_q='cdpCachePowerConsumption'
_p='cdpCacheVlanID'
_o='cdpCacheApplianceID'
_n='deprecated'
_m='macAddress'
_l='serialNumber'
_k='cdpCtAddressIndex'
_j='cdpInterfaceIfIndex'
_i='TruthValue'
_h='ifIndex'
_g='IF-MIB'
_f='OctetString'
_e='ciscoCdpMIBGroupV12R02'
_d='cdpGlobalDeviceId'
_c='cdpCacheDuplex'
_b='cdpCacheNativeVLAN'
_a='cdpCacheVTPMgmtDomain'
_Z='cdpInterfaceMessageInterval'
_Y='cdpCacheDeviceIndex'
_X='cdpCacheIfIndex'
_W='seconds'
_V='DisplayString'
_U='cdpGlobalHoldTime'
_T='cdpGlobalMessageInterval'
_S='cdpGlobalRun'
_R='not-accessible'
_Q='Unsigned32'
_P='cdpInterfacePort'
_O='cdpInterfaceGroup'
_N='cdpCachePlatform'
_M='cdpCacheCapabilities'
_L='cdpCacheDevicePort'
_K='cdpCacheDeviceId'
_J='cdpCacheVersion'
_I='cdpCacheAddress'
_H='cdpCacheAddressType'
_G='cdpInterfaceEnable'
_F='obsolete'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='current'
_A='CISCO-CDP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_f,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoNetworkAddress,CiscoNetworkProtocol=mibBuilder.importSymbols('CISCO-TC','CiscoNetworkAddress','CiscoNetworkProtocol')
VlanIndex,=mibBuilder.importSymbols('CISCO-VTP-MIB','VlanIndex')
ifIndex,=mibBuilder.importSymbols(_g,_h)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_Q,'iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_V,'PhysAddress','TextualConvention','TimeStamp',_i)
ciscoCdpMIB=ModuleIdentity((1,3,6,1,4,1,9,9,23))
if mibBuilder.loadTexts:ciscoCdpMIB.setRevisions(('2005-03-21 00:00','2005-03-14 00:00','2001-11-23 00:00','2001-04-23 00:00','2000-11-22 00:00','1998-12-10 00:00','1998-09-16 00:00','1996-07-08 00:00','1995-08-15 00:00','1995-07-27 00:00','1995-01-25 00:00'))
_CiscoCdpMIBObjects_ObjectIdentity=ObjectIdentity
ciscoCdpMIBObjects=_CiscoCdpMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,23,1))
_CdpInterface_ObjectIdentity=ObjectIdentity
cdpInterface=_CdpInterface_ObjectIdentity((1,3,6,1,4,1,9,9,23,1,1))
_CdpInterfaceTable_Object=MibTable
cdpInterfaceTable=_CdpInterfaceTable_Object((1,3,6,1,4,1,9,9,23,1,1,1))
if mibBuilder.loadTexts:cdpInterfaceTable.setStatus(_B)
_CdpInterfaceEntry_Object=MibTableRow
cdpInterfaceEntry=_CdpInterfaceEntry_Object((1,3,6,1,4,1,9,9,23,1,1,1,1))
cdpInterfaceEntry.setIndexNames((0,_A,_j))
if mibBuilder.loadTexts:cdpInterfaceEntry.setStatus(_B)
class _CdpInterfaceIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CdpInterfaceIfIndex_Type.__name__=_D
_CdpInterfaceIfIndex_Object=MibTableColumn
cdpInterfaceIfIndex=_CdpInterfaceIfIndex_Object((1,3,6,1,4,1,9,9,23,1,1,1,1,1),_CdpInterfaceIfIndex_Type())
cdpInterfaceIfIndex.setMaxAccess(_R)
if mibBuilder.loadTexts:cdpInterfaceIfIndex.setStatus(_B)
_CdpInterfaceEnable_Type=TruthValue
_CdpInterfaceEnable_Object=MibTableColumn
cdpInterfaceEnable=_CdpInterfaceEnable_Object((1,3,6,1,4,1,9,9,23,1,1,1,1,2),_CdpInterfaceEnable_Type())
cdpInterfaceEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:cdpInterfaceEnable.setStatus(_B)
class _CdpInterfaceMessageInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,254))
_CdpInterfaceMessageInterval_Type.__name__=_D
_CdpInterfaceMessageInterval_Object=MibTableColumn
cdpInterfaceMessageInterval=_CdpInterfaceMessageInterval_Object((1,3,6,1,4,1,9,9,23,1,1,1,1,3),_CdpInterfaceMessageInterval_Type())
cdpInterfaceMessageInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:cdpInterfaceMessageInterval.setStatus(_F)
if mibBuilder.loadTexts:cdpInterfaceMessageInterval.setUnits(_W)
_CdpInterfaceGroup_Type=Integer32
_CdpInterfaceGroup_Object=MibTableColumn
cdpInterfaceGroup=_CdpInterfaceGroup_Object((1,3,6,1,4,1,9,9,23,1,1,1,1,4),_CdpInterfaceGroup_Type())
cdpInterfaceGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:cdpInterfaceGroup.setStatus(_B)
_CdpInterfacePort_Type=Integer32
_CdpInterfacePort_Object=MibTableColumn
cdpInterfacePort=_CdpInterfacePort_Object((1,3,6,1,4,1,9,9,23,1,1,1,1,5),_CdpInterfacePort_Type())
cdpInterfacePort.setMaxAccess(_C)
if mibBuilder.loadTexts:cdpInterfacePort.setStatus(_B)
_CdpInterfaceName_Type=DisplayString
_CdpInterfaceName_Object=MibTableColumn
cdpInterfaceName=_CdpInterfaceName_Object((1,3,6,1,4,1,9,9,23,1,1,1,1,6),_CdpInterfaceName_Type())
cdpInterfaceName.setMaxAccess(_C)
if mibBuilder.loadTexts:cdpInterfaceName.setStatus(_B)
_CdpInterfaceExtTable_Object=MibTable
cdpInterfaceExtTable=_CdpInterfaceExtTable_Object((1,3,6,1,4,1,9,9,23,1,1,2))
if mibBuilder.loadTexts:cdpInterfaceExtTable.setStatus(_B)
_CdpInterfaceExtEntry_Object=MibTableRow
cdpInterfaceExtEntry=_CdpInterfaceExtEntry_Object((1,3,6,1,4,1,9,9,23,1,1,2,1))
cdpInterfaceExtEntry.setIndexNames((0,_g,_h))
if mibBuilder.loadTexts:cdpInterfaceExtEntry.setStatus(_B)
class _CdpInterfaceExtendedTrust_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('trusted',1),('noTrust',2)))
_CdpInterfaceExtendedTrust_Type.__name__=_D
_CdpInterfaceExtendedTrust_Object=MibTableColumn
cdpInterfaceExtendedTrust=_CdpInterfaceExtendedTrust_Object((1,3,6,1,4,1,9,9,23,1,1,2,1,1),_CdpInterfaceExtendedTrust_Type())
cdpInterfaceExtendedTrust.setMaxAccess(_E)
if mibBuilder.loadTexts:cdpInterfaceExtendedTrust.setStatus(_B)
class _CdpInterfaceCosForUntrustedPort_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_CdpInterfaceCosForUntrustedPort_Type.__name__=_Q
_CdpInterfaceCosForUntrustedPort_Object=MibTableColumn
cdpInterfaceCosForUntrustedPort=_CdpInterfaceCosForUntrustedPort_Object((1,3,6,1,4,1,9,9,23,1,1,2,1,2),_CdpInterfaceCosForUntrustedPort_Type())
cdpInterfaceCosForUntrustedPort.setMaxAccess(_E)
if mibBuilder.loadTexts:cdpInterfaceCosForUntrustedPort.setStatus(_B)
_CdpCache_ObjectIdentity=ObjectIdentity
cdpCache=_CdpCache_ObjectIdentity((1,3,6,1,4,1,9,9,23,1,2))
_CdpCacheTable_Object=MibTable
cdpCacheTable=_CdpCacheTable_Object((1,3,6,1,4,1,9,9,23,1,2,1))
if mibBuilder.loadTexts:cdpCacheTable.setStatus(_B)
_CdpCacheEntry_Object=MibTableRow
cdpCacheEntry=_CdpCacheEntry_Object((1,3,6,1,4,1,9,9,23,1,2,1,1))
cdpCacheEntry.setIndexNames((0,_A,_X),(0,_A,_Y))
if mibBuilder.loadTexts:cdpCacheEntry.setStatus(_B)
class _CdpCacheIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CdpCacheIfIndex_Type.__name__=_D
_CdpCacheIfIndex_Object=MibTableColumn
cdpCacheIfIndex=_CdpCacheIfIndex_Object((1,3,6,1,4,1,9,9,23,1,2,1,1,1),_CdpCacheIfIndex_Type())
cdpCacheIfIndex.setMaxAccess(_R)
if mibBuilder.loadTexts:cdpCacheIfIndex.setStatus(_B)
class _CdpCacheDeviceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CdpCacheDeviceIndex_Type.__name__=_D
_CdpCacheDeviceIndex_Object=MibTableColumn
cdpCacheDeviceIndex=_CdpCacheDeviceIndex_Object((1,3,6,1,4,1,9,9,23,1,2,1,1,2),_CdpCacheDeviceIndex_Type())
cdpCacheDeviceIndex.setMaxAccess(_R)
if mibBuilder.loadTexts:cdpCacheDeviceIndex.setStatus(_B)
_CdpCacheAddressType_Type=CiscoNetworkProtocol
_CdpCacheAddressType_Object=MibTableColumn
cdpCacheAddressType=_CdpCacheAddressType_Object((1,3,6,1,4,1,9,9,23,1,2,1,1,3),_CdpCacheAddressType_Type())
cdpCacheAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:cdpCacheAddressType.setStatus(_B)
_CdpCacheAddress_Type=CiscoNetworkAddress
_CdpCacheAddress_Object=MibTableColumn
cdpCacheAddress=_CdpCacheAddress_Object((1,3,6,1,4,1,9,9,23,1,2,1,1,4),_CdpCacheAddress_Type())
cdpCacheAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cdpCacheAddress.setStatus(_B)
_CdpCacheVersion_Type=DisplayString
_CdpCacheVersion_Object=MibTableColumn
cdpCacheVersion=_CdpCacheVersion_Object((1,3,6,1,4,1,9,9,23,1,2,1,1,5),_CdpCacheVersion_Type())
cdpCacheVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:cdpCacheVersion.setStatus(_B)
_CdpCacheDeviceId_Type=DisplayString
_CdpCacheDeviceId_Object=MibTableColumn
cdpCacheDeviceId=_CdpCacheDeviceId_Object((1,3,6,1,4,1,9,9,23,1,2,1,1,6),_CdpCacheDeviceId_Type())
cdpCacheDeviceId.setMaxAccess(_C)
if mibBuilder.loadTexts:cdpCacheDeviceId.setStatus(_B)
_CdpCacheDevicePort_Type=DisplayString
_CdpCacheDevicePort_Object=MibTableColumn
cdpCacheDevicePort=_CdpCacheDevicePort_Object((1,3,6,1,4,1,9,9,23,1,2,1,1,7),_CdpCacheDevicePort_Type())
cdpCacheDevicePort.setMaxAccess(_C)
if mibBuilder.loadTexts:cdpCacheDevicePort.setStatus(_B)
_CdpCachePlatform_Type=DisplayString
_CdpCachePlatform_Object=MibTableColumn
cdpCachePlatform=_CdpCachePlatform_Object((1,3,6,1,4,1,9,9,23,1,2,1,1,8),_CdpCachePlatform_Type())
cdpCachePlatform.setMaxAccess(_C)
if mibBuilder.loadTexts:cdpCachePlatform.setStatus(_B)
class _CdpCacheCapabilities_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_CdpCacheCapabilities_Type.__name__=_f
_CdpCacheCapabilities_Object=MibTableColumn
cdpCacheCapabilities=_CdpCacheCapabilities_Object((1,3,6,1,4,1,9,9,23,1,2,1,1,9),_CdpCacheCapabilities_Type())
cdpCacheCapabilities.setMaxAccess(_C)
if mibBuilder.loadTexts:cdpCacheCapabilities.setStatus(_B)
class _CdpCacheVTPMgmtDomain_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CdpCacheVTPMgmtDomain_Type.__name__=_V
_CdpCacheVTPMgmtDomain_Object=MibTableColumn
cdpCacheVTPMgmtDomain=_CdpCacheVTPMgmtDomain_Object((1,3,6,1,4,1,9,9,23,1,2,1,1,10),_CdpCacheVTPMgmtDomain_Type())
cdpCacheVTPMgmtDomain.setMaxAccess(_C)
if mibBuilder.loadTexts:cdpCacheVTPMgmtDomain.setStatus(_B)
_CdpCacheNativeVLAN_Type=VlanIndex
_CdpCacheNativeVLAN_Object=MibTableColumn
cdpCacheNativeVLAN=_CdpCacheNativeVLAN_Object((1,3,6,1,4,1,9,9,23,1,2,1,1,11),_CdpCacheNativeVLAN_Type())
cdpCacheNativeVLAN.setMaxAccess(_C)
if mibBuilder.loadTexts:cdpCacheNativeVLAN.setStatus(_B)
class _CdpCacheDuplex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unknown',1),('halfduplex',2),('fullduplex',3)))
_CdpCacheDuplex_Type.__name__=_D
_CdpCacheDuplex_Object=MibTableColumn
cdpCacheDuplex=_CdpCacheDuplex_Object((1,3,6,1,4,1,9,9,23,1,2,1,1,12),_CdpCacheDuplex_Type())
cdpCacheDuplex.setMaxAccess(_C)
if mibBuilder.loadTexts:cdpCacheDuplex.setStatus(_B)
class _CdpCacheApplianceID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CdpCacheApplianceID_Type.__name__=_Q
_CdpCacheApplianceID_Object=MibTableColumn
cdpCacheApplianceID=_CdpCacheApplianceID_Object((1,3,6,1,4,1,9,9,23,1,2,1,1,13),_CdpCacheApplianceID_Type())
cdpCacheApplianceID.setMaxAccess(_C)
if mibBuilder.loadTexts:cdpCacheApplianceID.setStatus(_B)
class _CdpCacheVlanID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_CdpCacheVlanID_Type.__name__=_Q
_CdpCacheVlanID_Object=MibTableColumn
cdpCacheVlanID=_CdpCacheVlanID_Object((1,3,6,1,4,1,9,9,23,1,2,1,1,14),_CdpCacheVlanID_Type())
cdpCacheVlanID.setMaxAccess(_C)
if mibBuilder.loadTexts:cdpCacheVlanID.setStatus(_B)
_CdpCachePowerConsumption_Type=Unsigned32
_CdpCachePowerConsumption_Object=MibTableColumn
cdpCachePowerConsumption=_CdpCachePowerConsumption_Object((1,3,6,1,4,1,9,9,23,1,2,1,1,15),_CdpCachePowerConsumption_Type())
cdpCachePowerConsumption.setMaxAccess(_C)
if mibBuilder.loadTexts:cdpCachePowerConsumption.setStatus(_B)
if mibBuilder.loadTexts:cdpCachePowerConsumption.setUnits('milliwatts')
_CdpCacheMTU_Type=Unsigned32
_CdpCacheMTU_Object=MibTableColumn
cdpCacheMTU=_CdpCacheMTU_Object((1,3,6,1,4,1,9,9,23,1,2,1,1,16),_CdpCacheMTU_Type())
cdpCacheMTU.setMaxAccess(_C)
if mibBuilder.loadTexts:cdpCacheMTU.setStatus(_B)
class _CdpCacheSysName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CdpCacheSysName_Type.__name__=_V
_CdpCacheSysName_Object=MibTableColumn
cdpCacheSysName=_CdpCacheSysName_Object((1,3,6,1,4,1,9,9,23,1,2,1,1,17),_CdpCacheSysName_Type())
cdpCacheSysName.setMaxAccess(_C)
if mibBuilder.loadTexts:cdpCacheSysName.setStatus(_B)
_CdpCacheSysObjectID_Type=ObjectIdentifier
_CdpCacheSysObjectID_Object=MibTableColumn
cdpCacheSysObjectID=_CdpCacheSysObjectID_Object((1,3,6,1,4,1,9,9,23,1,2,1,1,18),_CdpCacheSysObjectID_Type())
cdpCacheSysObjectID.setMaxAccess(_C)
if mibBuilder.loadTexts:cdpCacheSysObjectID.setStatus(_B)
_CdpCachePrimaryMgmtAddrType_Type=CiscoNetworkProtocol
_CdpCachePrimaryMgmtAddrType_Object=MibTableColumn
cdpCachePrimaryMgmtAddrType=_CdpCachePrimaryMgmtAddrType_Object((1,3,6,1,4,1,9,9,23,1,2,1,1,19),_CdpCachePrimaryMgmtAddrType_Type())
cdpCachePrimaryMgmtAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cdpCachePrimaryMgmtAddrType.setStatus(_B)
_CdpCachePrimaryMgmtAddr_Type=CiscoNetworkAddress
_CdpCachePrimaryMgmtAddr_Object=MibTableColumn
cdpCachePrimaryMgmtAddr=_CdpCachePrimaryMgmtAddr_Object((1,3,6,1,4,1,9,9,23,1,2,1,1,20),_CdpCachePrimaryMgmtAddr_Type())
cdpCachePrimaryMgmtAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cdpCachePrimaryMgmtAddr.setStatus(_B)
_CdpCacheSecondaryMgmtAddrType_Type=CiscoNetworkProtocol
_CdpCacheSecondaryMgmtAddrType_Object=MibTableColumn
cdpCacheSecondaryMgmtAddrType=_CdpCacheSecondaryMgmtAddrType_Object((1,3,6,1,4,1,9,9,23,1,2,1,1,21),_CdpCacheSecondaryMgmtAddrType_Type())
cdpCacheSecondaryMgmtAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cdpCacheSecondaryMgmtAddrType.setStatus(_B)
_CdpCacheSecondaryMgmtAddr_Type=CiscoNetworkAddress
_CdpCacheSecondaryMgmtAddr_Object=MibTableColumn
cdpCacheSecondaryMgmtAddr=_CdpCacheSecondaryMgmtAddr_Object((1,3,6,1,4,1,9,9,23,1,2,1,1,22),_CdpCacheSecondaryMgmtAddr_Type())
cdpCacheSecondaryMgmtAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cdpCacheSecondaryMgmtAddr.setStatus(_B)
_CdpCachePhysLocation_Type=DisplayString
_CdpCachePhysLocation_Object=MibTableColumn
cdpCachePhysLocation=_CdpCachePhysLocation_Object((1,3,6,1,4,1,9,9,23,1,2,1,1,23),_CdpCachePhysLocation_Type())
cdpCachePhysLocation.setMaxAccess(_C)
if mibBuilder.loadTexts:cdpCachePhysLocation.setStatus(_B)
_CdpCacheLastChange_Type=TimeStamp
_CdpCacheLastChange_Object=MibTableColumn
cdpCacheLastChange=_CdpCacheLastChange_Object((1,3,6,1,4,1,9,9,23,1,2,1,1,24),_CdpCacheLastChange_Type())
cdpCacheLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:cdpCacheLastChange.setStatus(_B)
_CdpCtAddressTable_Object=MibTable
cdpCtAddressTable=_CdpCtAddressTable_Object((1,3,6,1,4,1,9,9,23,1,2,2))
if mibBuilder.loadTexts:cdpCtAddressTable.setStatus(_B)
_CdpCtAddressEntry_Object=MibTableRow
cdpCtAddressEntry=_CdpCtAddressEntry_Object((1,3,6,1,4,1,9,9,23,1,2,2,1))
cdpCtAddressEntry.setIndexNames((0,_A,_X),(0,_A,_Y),(0,_A,_k))
if mibBuilder.loadTexts:cdpCtAddressEntry.setStatus(_B)
class _CdpCtAddressIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CdpCtAddressIndex_Type.__name__=_D
_CdpCtAddressIndex_Object=MibTableColumn
cdpCtAddressIndex=_CdpCtAddressIndex_Object((1,3,6,1,4,1,9,9,23,1,2,2,1,3),_CdpCtAddressIndex_Type())
cdpCtAddressIndex.setMaxAccess(_R)
if mibBuilder.loadTexts:cdpCtAddressIndex.setStatus(_B)
_CdpCtAddressType_Type=CiscoNetworkProtocol
_CdpCtAddressType_Object=MibTableColumn
cdpCtAddressType=_CdpCtAddressType_Object((1,3,6,1,4,1,9,9,23,1,2,2,1,4),_CdpCtAddressType_Type())
cdpCtAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:cdpCtAddressType.setStatus(_B)
_CdpCtAddress_Type=CiscoNetworkAddress
_CdpCtAddress_Object=MibTableColumn
cdpCtAddress=_CdpCtAddress_Object((1,3,6,1,4,1,9,9,23,1,2,2,1,5),_CdpCtAddress_Type())
cdpCtAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cdpCtAddress.setStatus(_B)
_CdpGlobal_ObjectIdentity=ObjectIdentity
cdpGlobal=_CdpGlobal_ObjectIdentity((1,3,6,1,4,1,9,9,23,1,3))
class _CdpGlobalRun_Type(TruthValue):defaultValue=1
_CdpGlobalRun_Type.__name__=_i
_CdpGlobalRun_Object=MibScalar
cdpGlobalRun=_CdpGlobalRun_Object((1,3,6,1,4,1,9,9,23,1,3,1),_CdpGlobalRun_Type())
cdpGlobalRun.setMaxAccess(_E)
if mibBuilder.loadTexts:cdpGlobalRun.setStatus(_B)
class _CdpGlobalMessageInterval_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,254))
_CdpGlobalMessageInterval_Type.__name__=_D
_CdpGlobalMessageInterval_Object=MibScalar
cdpGlobalMessageInterval=_CdpGlobalMessageInterval_Object((1,3,6,1,4,1,9,9,23,1,3,2),_CdpGlobalMessageInterval_Type())
cdpGlobalMessageInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:cdpGlobalMessageInterval.setStatus(_B)
if mibBuilder.loadTexts:cdpGlobalMessageInterval.setUnits(_W)
class _CdpGlobalHoldTime_Type(Integer32):defaultValue=180;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,255))
_CdpGlobalHoldTime_Type.__name__=_D
_CdpGlobalHoldTime_Object=MibScalar
cdpGlobalHoldTime=_CdpGlobalHoldTime_Object((1,3,6,1,4,1,9,9,23,1,3,3),_CdpGlobalHoldTime_Type())
cdpGlobalHoldTime.setMaxAccess(_E)
if mibBuilder.loadTexts:cdpGlobalHoldTime.setStatus(_B)
if mibBuilder.loadTexts:cdpGlobalHoldTime.setUnits(_W)
_CdpGlobalDeviceId_Type=DisplayString
_CdpGlobalDeviceId_Object=MibScalar
cdpGlobalDeviceId=_CdpGlobalDeviceId_Object((1,3,6,1,4,1,9,9,23,1,3,4),_CdpGlobalDeviceId_Type())
cdpGlobalDeviceId.setMaxAccess(_C)
if mibBuilder.loadTexts:cdpGlobalDeviceId.setStatus(_B)
_CdpGlobalLastChange_Type=TimeStamp
_CdpGlobalLastChange_Object=MibScalar
cdpGlobalLastChange=_CdpGlobalLastChange_Object((1,3,6,1,4,1,9,9,23,1,3,5),_CdpGlobalLastChange_Type())
cdpGlobalLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:cdpGlobalLastChange.setStatus(_B)
class _CdpGlobalDeviceIdFormatCpb_Type(Bits):namedValues=NamedValues(*((_l,0),(_m,1),('other',2)))
_CdpGlobalDeviceIdFormatCpb_Type.__name__='Bits'
_CdpGlobalDeviceIdFormatCpb_Object=MibScalar
cdpGlobalDeviceIdFormatCpb=_CdpGlobalDeviceIdFormatCpb_Object((1,3,6,1,4,1,9,9,23,1,3,6),_CdpGlobalDeviceIdFormatCpb_Type())
cdpGlobalDeviceIdFormatCpb.setMaxAccess(_C)
if mibBuilder.loadTexts:cdpGlobalDeviceIdFormatCpb.setStatus(_B)
class _CdpGlobalDeviceIdFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_l,1),(_m,2),('other',3)))
_CdpGlobalDeviceIdFormat_Type.__name__=_D
_CdpGlobalDeviceIdFormat_Object=MibScalar
cdpGlobalDeviceIdFormat=_CdpGlobalDeviceIdFormat_Object((1,3,6,1,4,1,9,9,23,1,3,7),_CdpGlobalDeviceIdFormat_Type())
cdpGlobalDeviceIdFormat.setMaxAccess(_E)
if mibBuilder.loadTexts:cdpGlobalDeviceIdFormat.setStatus(_B)
_CiscoCdpMIBConformance_ObjectIdentity=ObjectIdentity
ciscoCdpMIBConformance=_CiscoCdpMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,23,2))
_CiscoCdpMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoCdpMIBCompliances=_CiscoCdpMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,23,2,1))
_CiscoCdpMIBGroups_ObjectIdentity=ObjectIdentity
ciscoCdpMIBGroups=_CiscoCdpMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,23,2,2))
ciscoCdpMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,23,2,2,1))
ciscoCdpMIBGroup.setObjects(*((_A,_G),(_A,_Z),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ciscoCdpMIBGroup.setStatus(_F)
ciscoCdpMIBGroupV11R01=ObjectGroup((1,3,6,1,4,1,9,9,23,2,2,2))
ciscoCdpMIBGroupV11R01.setObjects(*((_A,_G),(_A,_Z),(_A,_O),(_A,_P),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ciscoCdpMIBGroupV11R01.setStatus(_F)
ciscoCdpMIBGroupV11R02=ObjectGroup((1,3,6,1,4,1,9,9,23,2,2,3))
ciscoCdpMIBGroupV11R02.setObjects(*((_A,_G),(_A,_O),(_A,_P),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_S),(_A,_T),(_A,_U)))
if mibBuilder.loadTexts:ciscoCdpMIBGroupV11R02.setStatus(_F)
ciscoCdpMIBGroupV12R02=ObjectGroup((1,3,6,1,4,1,9,9,23,2,2,5))
ciscoCdpMIBGroupV12R02.setObjects(*((_A,_G),(_A,_O),(_A,_P),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_a),(_A,_b),(_A,_c),(_A,_S),(_A,_T),(_A,_U),(_A,_d)))
if mibBuilder.loadTexts:ciscoCdpMIBGroupV12R02.setStatus(_n)
ciscoCdpV2MIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,23,2,2,6))
ciscoCdpV2MIBGroup.setObjects(*((_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2)))
if mibBuilder.loadTexts:ciscoCdpV2MIBGroup.setStatus(_B)
ciscoCdpV2IfExtGroup=ObjectGroup((1,3,6,1,4,1,9,9,23,2,2,7))
ciscoCdpV2IfExtGroup.setObjects(*((_A,_A3),(_A,_A4)))
if mibBuilder.loadTexts:ciscoCdpV2IfExtGroup.setStatus(_B)
ciscoCdpCtAddressGroup=ObjectGroup((1,3,6,1,4,1,9,9,23,2,2,8))
ciscoCdpCtAddressGroup.setObjects(*((_A,_A5),(_A,_A6)))
if mibBuilder.loadTexts:ciscoCdpCtAddressGroup.setStatus(_B)
ciscoCdpMIBGroupV12R03=ObjectGroup((1,3,6,1,4,1,9,9,23,2,2,9))
ciscoCdpMIBGroupV12R03.setObjects(*((_A,_G),(_A,_O),(_A,_P),(_A,_A7),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_a),(_A,_b),(_A,_c),(_A,_S),(_A,_T),(_A,_U),(_A,_d)))
if mibBuilder.loadTexts:ciscoCdpMIBGroupV12R03.setStatus(_B)
ciscoCdpMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,23,2,1,1))
ciscoCdpMIBCompliance.setObjects((_A,_A8))
if mibBuilder.loadTexts:ciscoCdpMIBCompliance.setStatus(_F)
ciscoCdpMIBComplianceV11R01=ModuleCompliance((1,3,6,1,4,1,9,9,23,2,1,2))
ciscoCdpMIBComplianceV11R01.setObjects((_A,_A9))
if mibBuilder.loadTexts:ciscoCdpMIBComplianceV11R01.setStatus(_F)
ciscoCdpMIBComplianceV11R02=ModuleCompliance((1,3,6,1,4,1,9,9,23,2,1,3))
ciscoCdpMIBComplianceV11R02.setObjects((_A,_AA))
if mibBuilder.loadTexts:ciscoCdpMIBComplianceV11R02.setStatus(_F)
ciscoCdpMIBComplianceV12R02=ModuleCompliance((1,3,6,1,4,1,9,9,23,2,1,4))
ciscoCdpMIBComplianceV12R02.setObjects((_A,_e))
if mibBuilder.loadTexts:ciscoCdpMIBComplianceV12R02.setStatus(_F)
ciscoCdpMIBCompliance5=ModuleCompliance((1,3,6,1,4,1,9,9,23,2,1,5))
ciscoCdpMIBCompliance5.setObjects((_A,_e))
if mibBuilder.loadTexts:ciscoCdpMIBCompliance5.setStatus(_n)
ciscoCdpMIBComplianceV12R03=ModuleCompliance((1,3,6,1,4,1,9,9,23,2,1,6))
ciscoCdpMIBComplianceV12R03.setObjects(*((_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE)))
if mibBuilder.loadTexts:ciscoCdpMIBComplianceV12R03.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoCdpMIB':ciscoCdpMIB,'ciscoCdpMIBObjects':ciscoCdpMIBObjects,'cdpInterface':cdpInterface,'cdpInterfaceTable':cdpInterfaceTable,'cdpInterfaceEntry':cdpInterfaceEntry,_j:cdpInterfaceIfIndex,_G:cdpInterfaceEnable,_Z:cdpInterfaceMessageInterval,_O:cdpInterfaceGroup,_P:cdpInterfacePort,_A7:cdpInterfaceName,'cdpInterfaceExtTable':cdpInterfaceExtTable,'cdpInterfaceExtEntry':cdpInterfaceExtEntry,_A3:cdpInterfaceExtendedTrust,_A4:cdpInterfaceCosForUntrustedPort,'cdpCache':cdpCache,'cdpCacheTable':cdpCacheTable,'cdpCacheEntry':cdpCacheEntry,_X:cdpCacheIfIndex,_Y:cdpCacheDeviceIndex,_H:cdpCacheAddressType,_I:cdpCacheAddress,_J:cdpCacheVersion,_K:cdpCacheDeviceId,_L:cdpCacheDevicePort,_N:cdpCachePlatform,_M:cdpCacheCapabilities,_a:cdpCacheVTPMgmtDomain,_b:cdpCacheNativeVLAN,_c:cdpCacheDuplex,_o:cdpCacheApplianceID,_p:cdpCacheVlanID,_q:cdpCachePowerConsumption,_r:cdpCacheMTU,_s:cdpCacheSysName,_t:cdpCacheSysObjectID,_w:cdpCachePrimaryMgmtAddrType,_x:cdpCachePrimaryMgmtAddr,_y:cdpCacheSecondaryMgmtAddrType,_z:cdpCacheSecondaryMgmtAddr,_v:cdpCachePhysLocation,_u:cdpCacheLastChange,'cdpCtAddressTable':cdpCtAddressTable,'cdpCtAddressEntry':cdpCtAddressEntry,_k:cdpCtAddressIndex,_A5:cdpCtAddressType,_A6:cdpCtAddress,'cdpGlobal':cdpGlobal,_S:cdpGlobalRun,_T:cdpGlobalMessageInterval,_U:cdpGlobalHoldTime,_d:cdpGlobalDeviceId,_A0:cdpGlobalLastChange,_A1:cdpGlobalDeviceIdFormatCpb,_A2:cdpGlobalDeviceIdFormat,'ciscoCdpMIBConformance':ciscoCdpMIBConformance,'ciscoCdpMIBCompliances':ciscoCdpMIBCompliances,'ciscoCdpMIBCompliance':ciscoCdpMIBCompliance,'ciscoCdpMIBComplianceV11R01':ciscoCdpMIBComplianceV11R01,'ciscoCdpMIBComplianceV11R02':ciscoCdpMIBComplianceV11R02,'ciscoCdpMIBComplianceV12R02':ciscoCdpMIBComplianceV12R02,'ciscoCdpMIBCompliance5':ciscoCdpMIBCompliance5,'ciscoCdpMIBComplianceV12R03':ciscoCdpMIBComplianceV12R03,'ciscoCdpMIBGroups':ciscoCdpMIBGroups,_A8:ciscoCdpMIBGroup,_A9:ciscoCdpMIBGroupV11R01,_AA:ciscoCdpMIBGroupV11R02,_e:ciscoCdpMIBGroupV12R02,_AD:ciscoCdpV2MIBGroup,_AE:ciscoCdpV2IfExtGroup,_AC:ciscoCdpCtAddressGroup,_AB:ciscoCdpMIBGroupV12R03})