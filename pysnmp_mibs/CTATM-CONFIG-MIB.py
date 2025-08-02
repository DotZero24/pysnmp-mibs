_a='ctATMLANEInfoExtTMIndex'
_Z='restart'
_Y='manual'
_X='automatic'
_W='ctATMDiscoveryElanIndex'
_V='leArpMacAddress'
_U='atmVclVpi'
_T='atmVclVci'
_S='atmTrafficDescrParamIndex'
_R='OctetString'
_Q='down'
_P='unknown'
_O='CTATM-CONFIG-MIB'
_N='off'
_M='disable'
_L='enable'
_K='lecIndex'
_J='ATM-MIB'
_I='LAN-EMULATION-CLIENT-MIB'
_H='DisplayString'
_G='ifIndex'
_F='IF-MIB'
_E='obsolete'
_D='read-write'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_R,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
atmTrafficDescrParamIndex,atmVclVci,atmVclVpi=mibBuilder.importSymbols(_J,_S,_T,_U)
AtmTrafficDescrParamIndex,=mibBuilder.importSymbols('ATM-TC-MIB','AtmTrafficDescrParamIndex')
ctATMConfig,=mibBuilder.importSymbols('CTRON-MIB-NAMES','ctATMConfig')
ifIndex,=mibBuilder.importSymbols(_F,_G)
leArpMacAddress,lecIndex=mibBuilder.importSymbols(_I,_V,_K)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','TextualConvention')
class AtmAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(20,20));fixedLength=20
_CtATMBaseConfig_ObjectIdentity=ObjectIdentity
ctATMBaseConfig=_CtATMBaseConfig_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,10,1,1))
class _CtATMPvcIfDef_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,512))
_CtATMPvcIfDef_Type.__name__=_B
_CtATMPvcIfDef_Object=MibScalar
ctATMPvcIfDef=_CtATMPvcIfDef_Object((1,3,6,1,4,1,52,4,1,2,10,1,1,1),_CtATMPvcIfDef_Type())
ctATMPvcIfDef.setMaxAccess(_D)
if mibBuilder.loadTexts:ctATMPvcIfDef.setStatus('deprecated')
class _CtATMLecIfDef_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,512))
_CtATMLecIfDef_Type.__name__=_B
_CtATMLecIfDef_Object=MibScalar
ctATMLecIfDef=_CtATMLecIfDef_Object((1,3,6,1,4,1,52,4,1,2,10,1,1,2),_CtATMLecIfDef_Type())
ctATMLecIfDef.setMaxAccess(_D)
if mibBuilder.loadTexts:ctATMLecIfDef.setStatus(_E)
_CtATMDefApplicationTable_Object=MibTable
ctATMDefApplicationTable=_CtATMDefApplicationTable_Object((1,3,6,1,4,1,52,4,1,2,10,1,1,3))
if mibBuilder.loadTexts:ctATMDefApplicationTable.setStatus(_E)
_CtATMDefApplicationEntry_Object=MibTableRow
ctATMDefApplicationEntry=_CtATMDefApplicationEntry_Object((1,3,6,1,4,1,52,4,1,2,10,1,1,3,1))
ctATMDefApplicationEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:ctATMDefApplicationEntry.setStatus(_E)
class _CtATMDefApplicationIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,512))
_CtATMDefApplicationIfIndex_Type.__name__=_B
_CtATMDefApplicationIfIndex_Object=MibTableColumn
ctATMDefApplicationIfIndex=_CtATMDefApplicationIfIndex_Object((1,3,6,1,4,1,52,4,1,2,10,1,1,3,1,1),_CtATMDefApplicationIfIndex_Type())
ctATMDefApplicationIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ctATMDefApplicationIfIndex.setStatus(_E)
class _CtATMDefApplication_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('lane04',1),('lane',2)))
_CtATMDefApplication_Type.__name__=_B
_CtATMDefApplication_Object=MibTableColumn
ctATMDefApplication=_CtATMDefApplication_Object((1,3,6,1,4,1,52,4,1,2,10,1,1,3,1,2),_CtATMDefApplication_Type())
ctATMDefApplication.setMaxAccess(_D)
if mibBuilder.loadTexts:ctATMDefApplication.setStatus(_E)
_CtATMFramerStatusTable_Object=MibTable
ctATMFramerStatusTable=_CtATMFramerStatusTable_Object((1,3,6,1,4,1,52,4,1,2,10,1,1,4))
if mibBuilder.loadTexts:ctATMFramerStatusTable.setStatus(_E)
_CtATMFramerStatusEntry_Object=MibTableRow
ctATMFramerStatusEntry=_CtATMFramerStatusEntry_Object((1,3,6,1,4,1,52,4,1,2,10,1,1,4,1))
ctATMFramerStatusEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:ctATMFramerStatusEntry.setStatus(_E)
class _CtATMFramerStatusIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,512))
_CtATMFramerStatusIfIndex_Type.__name__=_B
_CtATMFramerStatusIfIndex_Object=MibTableColumn
ctATMFramerStatusIfIndex=_CtATMFramerStatusIfIndex_Object((1,3,6,1,4,1,52,4,1,2,10,1,1,4,1,1),_CtATMFramerStatusIfIndex_Type())
ctATMFramerStatusIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ctATMFramerStatusIfIndex.setStatus(_E)
class _CtATMFramerStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),(_N,2)))
_CtATMFramerStatus_Type.__name__=_B
_CtATMFramerStatus_Object=MibTableColumn
ctATMFramerStatus=_CtATMFramerStatus_Object((1,3,6,1,4,1,52,4,1,2,10,1,1,4,1,2),_CtATMFramerStatus_Type())
ctATMFramerStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ctATMFramerStatus.setStatus(_E)
_CtATMLecArpMacTable_Object=MibTable
ctATMLecArpMacTable=_CtATMLecArpMacTable_Object((1,3,6,1,4,1,52,4,1,2,10,1,1,5))
if mibBuilder.loadTexts:ctATMLecArpMacTable.setStatus(_A)
_CtATMLecArpMacEntry_Object=MibTableRow
ctATMLecArpMacEntry=_CtATMLecArpMacEntry_Object((1,3,6,1,4,1,52,4,1,2,10,1,1,5,1))
ctATMLecArpMacEntry.setIndexNames((0,_I,_K),(0,_I,_V))
if mibBuilder.loadTexts:ctATMLecArpMacEntry.setStatus(_A)
class _CtATMLecArpMacLecIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CtATMLecArpMacLecIndex_Type.__name__=_B
_CtATMLecArpMacLecIndex_Object=MibTableColumn
ctATMLecArpMacLecIndex=_CtATMLecArpMacLecIndex_Object((1,3,6,1,4,1,52,4,1,2,10,1,1,5,1,1),_CtATMLecArpMacLecIndex_Type())
ctATMLecArpMacLecIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ctATMLecArpMacLecIndex.setStatus(_E)
class _CtATMLecArpMacAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_CtATMLecArpMacAddress_Type.__name__=_R
_CtATMLecArpMacAddress_Object=MibTableColumn
ctATMLecArpMacAddress=_CtATMLecArpMacAddress_Object((1,3,6,1,4,1,52,4,1,2,10,1,1,5,1,2),_CtATMLecArpMacAddress_Type())
ctATMLecArpMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ctATMLecArpMacAddress.setStatus(_E)
_CtATMLecArpMacElanName_Type=DisplayString
_CtATMLecArpMacElanName_Object=MibTableColumn
ctATMLecArpMacElanName=_CtATMLecArpMacElanName_Object((1,3,6,1,4,1,52,4,1,2,10,1,1,5,1,3),_CtATMLecArpMacElanName_Type())
ctATMLecArpMacElanName.setMaxAccess(_C)
if mibBuilder.loadTexts:ctATMLecArpMacElanName.setStatus(_A)
class _CtATMLecArpMacVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_CtATMLecArpMacVpi_Type.__name__=_B
_CtATMLecArpMacVpi_Object=MibTableColumn
ctATMLecArpMacVpi=_CtATMLecArpMacVpi_Object((1,3,6,1,4,1,52,4,1,2,10,1,1,5,1,4),_CtATMLecArpMacVpi_Type())
ctATMLecArpMacVpi.setMaxAccess(_C)
if mibBuilder.loadTexts:ctATMLecArpMacVpi.setStatus(_A)
class _CtATMLecArpMacVci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CtATMLecArpMacVci_Type.__name__=_B
_CtATMLecArpMacVci_Object=MibTableColumn
ctATMLecArpMacVci=_CtATMLecArpMacVci_Object((1,3,6,1,4,1,52,4,1,2,10,1,1,5,1,5),_CtATMLecArpMacVci_Type())
ctATMLecArpMacVci.setMaxAccess(_C)
if mibBuilder.loadTexts:ctATMLecArpMacVci.setStatus(_A)
class _CtATMLecArpMacATMAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_CtATMLecArpMacATMAddress_Type.__name__=_H
_CtATMLecArpMacATMAddress_Object=MibTableColumn
ctATMLecArpMacATMAddress=_CtATMLecArpMacATMAddress_Object((1,3,6,1,4,1,52,4,1,2,10,1,1,5,1,6),_CtATMLecArpMacATMAddress_Type())
ctATMLecArpMacATMAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ctATMLecArpMacATMAddress.setStatus(_A)
_CtATMPvcBwAllocTable_Object=MibTable
ctATMPvcBwAllocTable=_CtATMPvcBwAllocTable_Object((1,3,6,1,4,1,52,4,1,2,10,1,1,6))
if mibBuilder.loadTexts:ctATMPvcBwAllocTable.setStatus(_A)
_CtATMPvcBwAllocEntry_Object=MibTableRow
ctATMPvcBwAllocEntry=_CtATMPvcBwAllocEntry_Object((1,3,6,1,4,1,52,4,1,2,10,1,1,6,1))
ctATMPvcBwAllocEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:ctATMPvcBwAllocEntry.setStatus(_A)
class _CtATMPvcBwAllocPhysIface_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,512))
_CtATMPvcBwAllocPhysIface_Type.__name__=_B
_CtATMPvcBwAllocPhysIface_Object=MibTableColumn
ctATMPvcBwAllocPhysIface=_CtATMPvcBwAllocPhysIface_Object((1,3,6,1,4,1,52,4,1,2,10,1,1,6,1,1),_CtATMPvcBwAllocPhysIface_Type())
ctATMPvcBwAllocPhysIface.setMaxAccess(_C)
if mibBuilder.loadTexts:ctATMPvcBwAllocPhysIface.setStatus(_E)
class _CtATMPvcBwAllocStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('on',1),(_N,2),('notSupported',3)))
_CtATMPvcBwAllocStatus_Type.__name__=_B
_CtATMPvcBwAllocStatus_Object=MibTableColumn
ctATMPvcBwAllocStatus=_CtATMPvcBwAllocStatus_Object((1,3,6,1,4,1,52,4,1,2,10,1,1,6,1,2),_CtATMPvcBwAllocStatus_Type())
ctATMPvcBwAllocStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ctATMPvcBwAllocStatus.setStatus(_A)
class _CtATMPvcBwAllocBandwidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CtATMPvcBwAllocBandwidth_Type.__name__=_B
_CtATMPvcBwAllocBandwidth_Object=MibTableColumn
ctATMPvcBwAllocBandwidth=_CtATMPvcBwAllocBandwidth_Object((1,3,6,1,4,1,52,4,1,2,10,1,1,6,1,3),_CtATMPvcBwAllocBandwidth_Type())
ctATMPvcBwAllocBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:ctATMPvcBwAllocBandwidth.setStatus(_E)
_CtATMDiscoveryElanTable_Object=MibTable
ctATMDiscoveryElanTable=_CtATMDiscoveryElanTable_Object((1,3,6,1,4,1,52,4,1,2,10,1,1,7))
if mibBuilder.loadTexts:ctATMDiscoveryElanTable.setStatus(_A)
_CtATMDiscoveryElanEntry_Object=MibTableRow
ctATMDiscoveryElanEntry=_CtATMDiscoveryElanEntry_Object((1,3,6,1,4,1,52,4,1,2,10,1,1,7,1))
ctATMDiscoveryElanEntry.setIndexNames((0,_F,_G),(0,_O,_W))
if mibBuilder.loadTexts:ctATMDiscoveryElanEntry.setStatus(_A)
class _CtATMDiscoveryElanIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_CtATMDiscoveryElanIndex_Type.__name__=_B
_CtATMDiscoveryElanIndex_Object=MibTableColumn
ctATMDiscoveryElanIndex=_CtATMDiscoveryElanIndex_Object((1,3,6,1,4,1,52,4,1,2,10,1,1,7,1,1),_CtATMDiscoveryElanIndex_Type())
ctATMDiscoveryElanIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ctATMDiscoveryElanIndex.setStatus(_A)
class _CtATMDiscoveryElanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_CtATMDiscoveryElanName_Type.__name__=_H
_CtATMDiscoveryElanName_Object=MibTableColumn
ctATMDiscoveryElanName=_CtATMDiscoveryElanName_Object((1,3,6,1,4,1,52,4,1,2,10,1,1,7,1,2),_CtATMDiscoveryElanName_Type())
ctATMDiscoveryElanName.setMaxAccess(_D)
if mibBuilder.loadTexts:ctATMDiscoveryElanName.setStatus(_A)
class _CtATMDiscoveryElanMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ctATMDiscoveryElanMaster',1),('ctATMDiscoveryElanSlave',2)))
_CtATMDiscoveryElanMode_Type.__name__=_B
_CtATMDiscoveryElanMode_Object=MibTableColumn
ctATMDiscoveryElanMode=_CtATMDiscoveryElanMode_Object((1,3,6,1,4,1,52,4,1,2,10,1,1,7,1,3),_CtATMDiscoveryElanMode_Type())
ctATMDiscoveryElanMode.setMaxAccess(_D)
if mibBuilder.loadTexts:ctATMDiscoveryElanMode.setStatus(_A)
class _CtATMDiscoveryElanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ctATMDiscoveryElanEnabled',1),('ctATmDiscoveryElanDisabled',2)))
_CtATMDiscoveryElanStatus_Type.__name__=_B
_CtATMDiscoveryElanStatus_Object=MibTableColumn
ctATMDiscoveryElanStatus=_CtATMDiscoveryElanStatus_Object((1,3,6,1,4,1,52,4,1,2,10,1,1,7,1,4),_CtATMDiscoveryElanStatus_Type())
ctATMDiscoveryElanStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ctATMDiscoveryElanStatus.setStatus(_A)
class _CtATMDiscoveryElanPhysIface_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,512))
_CtATMDiscoveryElanPhysIface_Type.__name__=_B
_CtATMDiscoveryElanPhysIface_Object=MibTableColumn
ctATMDiscoveryElanPhysIface=_CtATMDiscoveryElanPhysIface_Object((1,3,6,1,4,1,52,4,1,2,10,1,1,7,1,5),_CtATMDiscoveryElanPhysIface_Type())
ctATMDiscoveryElanPhysIface.setMaxAccess(_C)
if mibBuilder.loadTexts:ctATMDiscoveryElanPhysIface.setStatus(_E)
_CtATMVclTable_Object=MibTable
ctATMVclTable=_CtATMVclTable_Object((1,3,6,1,4,1,52,4,1,2,10,1,1,8))
if mibBuilder.loadTexts:ctATMVclTable.setStatus(_A)
_CtATMVclEntry_Object=MibTableRow
ctATMVclEntry=_CtATMVclEntry_Object((1,3,6,1,4,1,52,4,1,2,10,1,1,8,1))
ctATMVclEntry.setIndexNames((0,_F,_G),(0,_J,_U),(0,_J,_T))
if mibBuilder.loadTexts:ctATMVclEntry.setStatus(_A)
class _CtATMVclIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,512))
_CtATMVclIfIndex_Type.__name__=_B
_CtATMVclIfIndex_Object=MibTableColumn
ctATMVclIfIndex=_CtATMVclIfIndex_Object((1,3,6,1,4,1,52,4,1,2,10,1,1,8,1,1),_CtATMVclIfIndex_Type())
ctATMVclIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ctATMVclIfIndex.setStatus(_E)
class _CtATMVclVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_CtATMVclVpi_Type.__name__=_B
_CtATMVclVpi_Object=MibTableColumn
ctATMVclVpi=_CtATMVclVpi_Object((1,3,6,1,4,1,52,4,1,2,10,1,1,8,1,2),_CtATMVclVpi_Type())
ctATMVclVpi.setMaxAccess(_C)
if mibBuilder.loadTexts:ctATMVclVpi.setStatus(_E)
class _CtATMVclVci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CtATMVclVci_Type.__name__=_B
_CtATMVclVci_Object=MibTableColumn
ctATMVclVci=_CtATMVclVci_Object((1,3,6,1,4,1,52,4,1,2,10,1,1,8,1,3),_CtATMVclVci_Type())
ctATMVclVci.setMaxAccess(_C)
if mibBuilder.loadTexts:ctATMVclVci.setStatus(_E)
class _CtATMVclVirtualIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,512))
_CtATMVclVirtualIfIndex_Type.__name__=_B
_CtATMVclVirtualIfIndex_Object=MibTableColumn
ctATMVclVirtualIfIndex=_CtATMVclVirtualIfIndex_Object((1,3,6,1,4,1,52,4,1,2,10,1,1,8,1,4),_CtATMVclVirtualIfIndex_Type())
ctATMVclVirtualIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ctATMVclVirtualIfIndex.setStatus(_A)
class _CtATMVclApplicationPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,512))
_CtATMVclApplicationPort_Type.__name__=_B
_CtATMVclApplicationPort_Object=MibTableColumn
ctATMVclApplicationPort=_CtATMVclApplicationPort_Object((1,3,6,1,4,1,52,4,1,2,10,1,1,8,1,5),_CtATMVclApplicationPort_Type())
ctATMVclApplicationPort.setMaxAccess(_C)
if mibBuilder.loadTexts:ctATMVclApplicationPort.setStatus(_A)
_CtATMVclATMAddress_Type=AtmAddress
_CtATMVclATMAddress_Object=MibTableColumn
ctATMVclATMAddress=_CtATMVclATMAddress_Object((1,3,6,1,4,1,52,4,1,2,10,1,1,8,1,6),_CtATMVclATMAddress_Type())
ctATMVclATMAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ctATMVclATMAddress.setStatus(_A)
class _CtATMVclEncapsulationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)));namedValues=NamedValues(*(('vcMultiplexRoutedProtocol',1),('vcMultiplexBridgedProtocol8023',2),('vcMultiplexBridgedProtocol8025',3),('vcMultiplexBridgedProtocol8026',4),('vcMultiplexLANemulation8023',5),('vcMultiplexLANemulation8025',6),('llcEncapsulation',7),('multiprotocolFrameRelaySscs',8),('other',9),(_P,10),('ilmi',11),('uni',12),('lanEmulationData',13),('lanEmulationControl',14),('atmVcSvcApp',15),('multiProtocolOverATMData',16),('multiProtocolOverATMControl',17)))
_CtATMVclEncapsulationType_Type.__name__=_B
_CtATMVclEncapsulationType_Object=MibTableColumn
ctATMVclEncapsulationType=_CtATMVclEncapsulationType_Object((1,3,6,1,4,1,52,4,1,2,10,1,1,8,1,7),_CtATMVclEncapsulationType_Type())
ctATMVclEncapsulationType.setMaxAccess(_C)
if mibBuilder.loadTexts:ctATMVclEncapsulationType.setStatus(_A)
_CtATMPhysicalRedundancy_ObjectIdentity=ObjectIdentity
ctATMPhysicalRedundancy=_CtATMPhysicalRedundancy_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,10,1,2))
_CtATMPhysicalRedundancyInterface_ObjectIdentity=ObjectIdentity
ctATMPhysicalRedundancyInterface=_CtATMPhysicalRedundancyInterface_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,10,1,2,1))
_CtATMPhyRedundTable_Object=MibTable
ctATMPhyRedundTable=_CtATMPhyRedundTable_Object((1,3,6,1,4,1,52,4,1,2,10,1,2,1,1))
if mibBuilder.loadTexts:ctATMPhyRedundTable.setStatus(_A)
_CtATMPhyRedundEntry_Object=MibTableRow
ctATMPhyRedundEntry=_CtATMPhyRedundEntry_Object((1,3,6,1,4,1,52,4,1,2,10,1,2,1,1,1))
ctATMPhyRedundEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:ctATMPhyRedundEntry.setStatus(_A)
class _CtATMPhyRedundIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,512))
_CtATMPhyRedundIfIndex_Type.__name__=_B
_CtATMPhyRedundIfIndex_Object=MibTableColumn
ctATMPhyRedundIfIndex=_CtATMPhyRedundIfIndex_Object((1,3,6,1,4,1,52,4,1,2,10,1,2,1,1,1,1),_CtATMPhyRedundIfIndex_Type())
ctATMPhyRedundIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ctATMPhyRedundIfIndex.setStatus(_E)
class _CtATMPhyRedundPrimaryPort_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_CtATMPhyRedundPrimaryPort_Type.__name__=_B
_CtATMPhyRedundPrimaryPort_Object=MibTableColumn
ctATMPhyRedundPrimaryPort=_CtATMPhyRedundPrimaryPort_Object((1,3,6,1,4,1,52,4,1,2,10,1,2,1,1,1,2),_CtATMPhyRedundPrimaryPort_Type())
ctATMPhyRedundPrimaryPort.setMaxAccess(_D)
if mibBuilder.loadTexts:ctATMPhyRedundPrimaryPort.setStatus(_A)
class _CtATMPhyRedundActivePort_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_CtATMPhyRedundActivePort_Type.__name__=_B
_CtATMPhyRedundActivePort_Object=MibTableColumn
ctATMPhyRedundActivePort=_CtATMPhyRedundActivePort_Object((1,3,6,1,4,1,52,4,1,2,10,1,2,1,1,1,3),_CtATMPhyRedundActivePort_Type())
ctATMPhyRedundActivePort.setMaxAccess(_D)
if mibBuilder.loadTexts:ctATMPhyRedundActivePort.setStatus(_A)
class _CtATMPhyRedundStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_CtATMPhyRedundStatus_Type.__name__=_B
_CtATMPhyRedundStatus_Object=MibTableColumn
ctATMPhyRedundStatus=_CtATMPhyRedundStatus_Object((1,3,6,1,4,1,52,4,1,2,10,1,2,1,1,1,4),_CtATMPhyRedundStatus_Type())
ctATMPhyRedundStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ctATMPhyRedundStatus.setStatus(_A)
class _CtATMPhyRedundActivation_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_X,1),(_Y,2)))
_CtATMPhyRedundActivation_Type.__name__=_B
_CtATMPhyRedundActivation_Object=MibTableColumn
ctATMPhyRedundActivation=_CtATMPhyRedundActivation_Object((1,3,6,1,4,1,52,4,1,2,10,1,2,1,1,1,5),_CtATMPhyRedundActivation_Type())
ctATMPhyRedundActivation.setMaxAccess(_D)
if mibBuilder.loadTexts:ctATMPhyRedundActivation.setStatus(_A)
class _CtATMPhyRedundPrimaryRevert_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_X,1),(_Y,2)))
_CtATMPhyRedundPrimaryRevert_Type.__name__=_B
_CtATMPhyRedundPrimaryRevert_Object=MibTableColumn
ctATMPhyRedundPrimaryRevert=_CtATMPhyRedundPrimaryRevert_Object((1,3,6,1,4,1,52,4,1,2,10,1,2,1,1,1,6),_CtATMPhyRedundPrimaryRevert_Type())
ctATMPhyRedundPrimaryRevert.setMaxAccess(_D)
if mibBuilder.loadTexts:ctATMPhyRedundPrimaryRevert.setStatus(_A)
class _CtATMPhyRedundPerformTest_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),(_M,2),('immediate',3)))
_CtATMPhyRedundPerformTest_Type.__name__=_B
_CtATMPhyRedundPerformTest_Object=MibTableColumn
ctATMPhyRedundPerformTest=_CtATMPhyRedundPerformTest_Object((1,3,6,1,4,1,52,4,1,2,10,1,2,1,1,1,7),_CtATMPhyRedundPerformTest_Type())
ctATMPhyRedundPerformTest.setMaxAccess(_D)
if mibBuilder.loadTexts:ctATMPhyRedundPerformTest.setStatus(_A)
class _CtATMPhyRedundTestTOD_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(9,9));fixedLength=9
_CtATMPhyRedundTestTOD_Type.__name__=_H
_CtATMPhyRedundTestTOD_Object=MibTableColumn
ctATMPhyRedundTestTOD=_CtATMPhyRedundTestTOD_Object((1,3,6,1,4,1,52,4,1,2,10,1,2,1,1,1,8),_CtATMPhyRedundTestTOD_Type())
ctATMPhyRedundTestTOD.setMaxAccess(_D)
if mibBuilder.loadTexts:ctATMPhyRedundTestTOD.setStatus(_A)
class _CtATMPhyRedundTestResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,101,102,103,200,201,202,203)));namedValues=NamedValues(*(('manualAllPortsGood',100),('manualPrimaryBadOthersGood',101),('manualPrimaryGoodOthersBad',102),('manualPrimaryBadOthersBad',103),('automaticAllPortsGood',200),('automaticPrimaryBadOthersGood',201),('automaticPrimaryGoodOthersBad',202),('automaticPrimaryBadOthersBad',203)))
_CtATMPhyRedundTestResult_Type.__name__=_B
_CtATMPhyRedundTestResult_Object=MibTableColumn
ctATMPhyRedundTestResult=_CtATMPhyRedundTestResult_Object((1,3,6,1,4,1,52,4,1,2,10,1,2,1,1,1,9),_CtATMPhyRedundTestResult_Type())
ctATMPhyRedundTestResult.setMaxAccess(_C)
if mibBuilder.loadTexts:ctATMPhyRedundTestResult.setStatus(_A)
class _CtATMPhyRedundReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('reset',1))
_CtATMPhyRedundReset_Type.__name__=_B
_CtATMPhyRedundReset_Object=MibTableColumn
ctATMPhyRedundReset=_CtATMPhyRedundReset_Object((1,3,6,1,4,1,52,4,1,2,10,1,2,1,1,1,10),_CtATMPhyRedundReset_Type())
ctATMPhyRedundReset.setMaxAccess(_D)
if mibBuilder.loadTexts:ctATMPhyRedundReset.setStatus(_A)
_CtATMIlmi_ObjectIdentity=ObjectIdentity
ctATMIlmi=_CtATMIlmi_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,10,1,3))
_CtATMIlmiTable_Object=MibTable
ctATMIlmiTable=_CtATMIlmiTable_Object((1,3,6,1,4,1,52,4,1,2,10,1,3,1))
if mibBuilder.loadTexts:ctATMIlmiTable.setStatus(_A)
_CtATMIlmiEntry_Object=MibTableRow
ctATMIlmiEntry=_CtATMIlmiEntry_Object((1,3,6,1,4,1,52,4,1,2,10,1,3,1,1))
ctATMIlmiEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:ctATMIlmiEntry.setStatus(_A)
class _CtATMIlmiIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,512))
_CtATMIlmiIfIndex_Type.__name__=_B
_CtATMIlmiIfIndex_Object=MibTableColumn
ctATMIlmiIfIndex=_CtATMIlmiIfIndex_Object((1,3,6,1,4,1,52,4,1,2,10,1,3,1,1,1),_CtATMIlmiIfIndex_Type())
ctATMIlmiIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ctATMIlmiIfIndex.setStatus(_E)
class _CtATMIlmiStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('enableAutoConfigure',1),(_L,2),(_M,3)))
_CtATMIlmiStatus_Type.__name__=_B
_CtATMIlmiStatus_Object=MibTableColumn
ctATMIlmiStatus=_CtATMIlmiStatus_Object((1,3,6,1,4,1,52,4,1,2,10,1,3,1,1,2),_CtATMIlmiStatus_Type())
ctATMIlmiStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ctATMIlmiStatus.setStatus(_A)
_CtATMIlmiAtmAddress_Type=AtmAddress
_CtATMIlmiAtmAddress_Object=MibTableColumn
ctATMIlmiAtmAddress=_CtATMIlmiAtmAddress_Object((1,3,6,1,4,1,52,4,1,2,10,1,3,1,1,3),_CtATMIlmiAtmAddress_Type())
ctATMIlmiAtmAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:ctATMIlmiAtmAddress.setStatus(_A)
class _CtATMIlmiState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_P,1),('up',2),('addressRegistration',3),('autoconfigure',4),(_Q,5),('estabConnectivity',6),('noLink',7),('obtainLECS',8)))
_CtATMIlmiState_Type.__name__=_B
_CtATMIlmiState_Object=MibTableColumn
ctATMIlmiState=_CtATMIlmiState_Object((1,3,6,1,4,1,52,4,1,2,10,1,3,1,1,4),_CtATMIlmiState_Type())
ctATMIlmiState.setMaxAccess(_C)
if mibBuilder.loadTexts:ctATMIlmiState.setStatus(_A)
class _CtATMIlmiRestart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_Z,1))
_CtATMIlmiRestart_Type.__name__=_B
_CtATMIlmiRestart_Object=MibTableColumn
ctATMIlmiRestart=_CtATMIlmiRestart_Object((1,3,6,1,4,1,52,4,1,2,10,1,3,1,1,5),_CtATMIlmiRestart_Type())
ctATMIlmiRestart.setMaxAccess(_D)
if mibBuilder.loadTexts:ctATMIlmiRestart.setStatus(_A)
_CtATMSignalConfig_ObjectIdentity=ObjectIdentity
ctATMSignalConfig=_CtATMSignalConfig_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,10,1,4))
_CtATMSignalTable_Object=MibTable
ctATMSignalTable=_CtATMSignalTable_Object((1,3,6,1,4,1,52,4,1,2,10,1,4,1))
if mibBuilder.loadTexts:ctATMSignalTable.setStatus(_A)
_CtATMSignalEntry_Object=MibTableRow
ctATMSignalEntry=_CtATMSignalEntry_Object((1,3,6,1,4,1,52,4,1,2,10,1,4,1,1))
ctATMSignalEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:ctATMSignalEntry.setStatus(_A)
class _CtATMSignalIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,512))
_CtATMSignalIfIndex_Type.__name__=_B
_CtATMSignalIfIndex_Object=MibTableColumn
ctATMSignalIfIndex=_CtATMSignalIfIndex_Object((1,3,6,1,4,1,52,4,1,2,10,1,4,1,1,1),_CtATMSignalIfIndex_Type())
ctATMSignalIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ctATMSignalIfIndex.setStatus(_E)
class _CtATMSignalStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_CtATMSignalStatus_Type.__name__=_B
_CtATMSignalStatus_Object=MibTableColumn
ctATMSignalStatus=_CtATMSignalStatus_Object((1,3,6,1,4,1,52,4,1,2,10,1,4,1,1,2),_CtATMSignalStatus_Type())
ctATMSignalStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ctATMSignalStatus.setStatus(_A)
class _CtATMSignalType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_P,1),('spans',2),('uni30',3),('uni31',4),('uni40',5)))
_CtATMSignalType_Type.__name__=_B
_CtATMSignalType_Object=MibTableColumn
ctATMSignalType=_CtATMSignalType_Object((1,3,6,1,4,1,52,4,1,2,10,1,4,1,1,3),_CtATMSignalType_Type())
ctATMSignalType.setMaxAccess(_D)
if mibBuilder.loadTexts:ctATMSignalType.setStatus(_A)
class _CtATMSignalQ93Status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),(_Q,2)))
_CtATMSignalQ93Status_Type.__name__=_B
_CtATMSignalQ93Status_Object=MibTableColumn
ctATMSignalQ93Status=_CtATMSignalQ93Status_Object((1,3,6,1,4,1,52,4,1,2,10,1,4,1,1,4),_CtATMSignalQ93Status_Type())
ctATMSignalQ93Status.setMaxAccess(_C)
if mibBuilder.loadTexts:ctATMSignalQ93Status.setStatus(_A)
class _CtATMSignalQsaalStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),(_Q,2)))
_CtATMSignalQsaalStatus_Type.__name__=_B
_CtATMSignalQsaalStatus_Object=MibTableColumn
ctATMSignalQsaalStatus=_CtATMSignalQsaalStatus_Object((1,3,6,1,4,1,52,4,1,2,10,1,4,1,1,5),_CtATMSignalQsaalStatus_Type())
ctATMSignalQsaalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ctATMSignalQsaalStatus.setStatus(_A)
class _CtATMSignalRestart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_Z,1))
_CtATMSignalRestart_Type.__name__=_B
_CtATMSignalRestart_Object=MibTableColumn
ctATMSignalRestart=_CtATMSignalRestart_Object((1,3,6,1,4,1,52,4,1,2,10,1,4,1,1,6),_CtATMSignalRestart_Type())
ctATMSignalRestart.setMaxAccess(_D)
if mibBuilder.loadTexts:ctATMSignalRestart.setStatus(_A)
_CtATMLANEServices_ObjectIdentity=ObjectIdentity
ctATMLANEServices=_CtATMLANEServices_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,10,1,5))
_CtATMLANEInfoExtGroup_ObjectIdentity=ObjectIdentity
ctATMLANEInfoExtGroup=_CtATMLANEInfoExtGroup_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,10,1,6))
_CtATMLANEInfoExtStatusTable_Object=MibTable
ctATMLANEInfoExtStatusTable=_CtATMLANEInfoExtStatusTable_Object((1,3,6,1,4,1,52,4,1,2,10,1,6,1))
if mibBuilder.loadTexts:ctATMLANEInfoExtStatusTable.setStatus(_A)
_CtATMLANEInfoExtStatusEntry_Object=MibTableRow
ctATMLANEInfoExtStatusEntry=_CtATMLANEInfoExtStatusEntry_Object((1,3,6,1,4,1,52,4,1,2,10,1,6,1,1))
ctATMLANEInfoExtStatusEntry.setIndexNames((0,_I,_K))
if mibBuilder.loadTexts:ctATMLANEInfoExtStatusEntry.setStatus(_A)
class _CtATMLANEInfoExtStatusUpTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CtATMLANEInfoExtStatusUpTime_Type.__name__=_B
_CtATMLANEInfoExtStatusUpTime_Object=MibTableColumn
ctATMLANEInfoExtStatusUpTime=_CtATMLANEInfoExtStatusUpTime_Object((1,3,6,1,4,1,52,4,1,2,10,1,6,1,1,1),_CtATMLANEInfoExtStatusUpTime_Type())
ctATMLANEInfoExtStatusUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ctATMLANEInfoExtStatusUpTime.setStatus(_A)
class _CtATMLANEInfoExtStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('lecactive',1),('lecnotInService',2),('lecnoLink',3),('lecnoATMaddrnoUNI',4),('lecnoATMaddr',5),('lecnoUNI',6),('lecmemError',7)))
_CtATMLANEInfoExtStatus_Type.__name__=_B
_CtATMLANEInfoExtStatus_Object=MibTableColumn
ctATMLANEInfoExtStatus=_CtATMLANEInfoExtStatus_Object((1,3,6,1,4,1,52,4,1,2,10,1,6,1,1,2),_CtATMLANEInfoExtStatus_Type())
ctATMLANEInfoExtStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ctATMLANEInfoExtStatus.setStatus(_A)
class _CtATMLANEInfoExtStatusSendTopo_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),(_N,2)))
_CtATMLANEInfoExtStatusSendTopo_Type.__name__=_B
_CtATMLANEInfoExtStatusSendTopo_Object=MibTableColumn
ctATMLANEInfoExtStatusSendTopo=_CtATMLANEInfoExtStatusSendTopo_Object((1,3,6,1,4,1,52,4,1,2,10,1,6,1,1,3),_CtATMLANEInfoExtStatusSendTopo_Type())
ctATMLANEInfoExtStatusSendTopo.setMaxAccess(_D)
if mibBuilder.loadTexts:ctATMLANEInfoExtStatusSendTopo.setStatus(_A)
class _CtATMLANEInfoExtStatusTimeLeft_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_CtATMLANEInfoExtStatusTimeLeft_Type.__name__=_H
_CtATMLANEInfoExtStatusTimeLeft_Object=MibTableColumn
ctATMLANEInfoExtStatusTimeLeft=_CtATMLANEInfoExtStatusTimeLeft_Object((1,3,6,1,4,1,52,4,1,2,10,1,6,1,1,4),_CtATMLANEInfoExtStatusTimeLeft_Type())
ctATMLANEInfoExtStatusTimeLeft.setMaxAccess(_C)
if mibBuilder.loadTexts:ctATMLANEInfoExtStatusTimeLeft.setStatus(_A)
class _CtATMLANEInfoExtStatusNumQueues_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_CtATMLANEInfoExtStatusNumQueues_Type.__name__=_B
_CtATMLANEInfoExtStatusNumQueues_Object=MibTableColumn
ctATMLANEInfoExtStatusNumQueues=_CtATMLANEInfoExtStatusNumQueues_Object((1,3,6,1,4,1,52,4,1,2,10,1,6,1,1,5),_CtATMLANEInfoExtStatusNumQueues_Type())
ctATMLANEInfoExtStatusNumQueues.setMaxAccess(_D)
if mibBuilder.loadTexts:ctATMLANEInfoExtStatusNumQueues.setStatus(_A)
class _CtATMLANEInfoExtStatusMaxNumQueues_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_CtATMLANEInfoExtStatusMaxNumQueues_Type.__name__=_B
_CtATMLANEInfoExtStatusMaxNumQueues_Object=MibTableColumn
ctATMLANEInfoExtStatusMaxNumQueues=_CtATMLANEInfoExtStatusMaxNumQueues_Object((1,3,6,1,4,1,52,4,1,2,10,1,6,1,1,6),_CtATMLANEInfoExtStatusMaxNumQueues_Type())
ctATMLANEInfoExtStatusMaxNumQueues.setMaxAccess(_C)
if mibBuilder.loadTexts:ctATMLANEInfoExtStatusMaxNumQueues.setStatus(_A)
_CtATMLANEInfoExtTMTable_Object=MibTable
ctATMLANEInfoExtTMTable=_CtATMLANEInfoExtTMTable_Object((1,3,6,1,4,1,52,4,1,2,10,1,6,2))
if mibBuilder.loadTexts:ctATMLANEInfoExtTMTable.setStatus(_A)
_CtATMLANEInfoExtTMEntry_Object=MibTableRow
ctATMLANEInfoExtTMEntry=_CtATMLANEInfoExtTMEntry_Object((1,3,6,1,4,1,52,4,1,2,10,1,6,2,1))
ctATMLANEInfoExtTMEntry.setIndexNames((0,_I,_K),(0,_O,_a))
if mibBuilder.loadTexts:ctATMLANEInfoExtTMEntry.setStatus(_A)
_CtATMLANEInfoExtTMIndex_Type=Integer32
_CtATMLANEInfoExtTMIndex_Object=MibTableColumn
ctATMLANEInfoExtTMIndex=_CtATMLANEInfoExtTMIndex_Object((1,3,6,1,4,1,52,4,1,2,10,1,6,2,1,1),_CtATMLANEInfoExtTMIndex_Type())
ctATMLANEInfoExtTMIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ctATMLANEInfoExtTMIndex.setStatus(_A)
_CtATMLANEInfoExtTMTrafficDescrIndex_Type=AtmTrafficDescrParamIndex
_CtATMLANEInfoExtTMTrafficDescrIndex_Object=MibTableColumn
ctATMLANEInfoExtTMTrafficDescrIndex=_CtATMLANEInfoExtTMTrafficDescrIndex_Object((1,3,6,1,4,1,52,4,1,2,10,1,6,2,1,2),_CtATMLANEInfoExtTMTrafficDescrIndex_Type())
ctATMLANEInfoExtTMTrafficDescrIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ctATMLANEInfoExtTMTrafficDescrIndex.setStatus(_A)
_CtATMTrafficManagementGroup_ObjectIdentity=ObjectIdentity
ctATMTrafficManagementGroup=_CtATMTrafficManagementGroup_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,10,1,7))
_CtATMTrafficDescrNameTable_Object=MibTable
ctATMTrafficDescrNameTable=_CtATMTrafficDescrNameTable_Object((1,3,6,1,4,1,52,4,1,2,10,1,7,1))
if mibBuilder.loadTexts:ctATMTrafficDescrNameTable.setStatus(_A)
_CtATMTrafficDescrNameEntry_Object=MibTableRow
ctATMTrafficDescrNameEntry=_CtATMTrafficDescrNameEntry_Object((1,3,6,1,4,1,52,4,1,2,10,1,7,1,1))
ctATMTrafficDescrNameEntry.setIndexNames((0,_J,_S))
if mibBuilder.loadTexts:ctATMTrafficDescrNameEntry.setStatus(_A)
class _CtATMTrafficDescrName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_CtATMTrafficDescrName_Type.__name__=_H
_CtATMTrafficDescrName_Object=MibTableColumn
ctATMTrafficDescrName=_CtATMTrafficDescrName_Object((1,3,6,1,4,1,52,4,1,2,10,1,7,1,1,1),_CtATMTrafficDescrName_Type())
ctATMTrafficDescrName.setMaxAccess(_D)
if mibBuilder.loadTexts:ctATMTrafficDescrName.setStatus(_A)
_CtATMTrafficServiceCategoriesSupportedTable_Object=MibTable
ctATMTrafficServiceCategoriesSupportedTable=_CtATMTrafficServiceCategoriesSupportedTable_Object((1,3,6,1,4,1,52,4,1,2,10,1,7,2))
if mibBuilder.loadTexts:ctATMTrafficServiceCategoriesSupportedTable.setStatus(_A)
_CtATMTrafficServiceCategoriesSupportedEntry_Object=MibTableRow
ctATMTrafficServiceCategoriesSupportedEntry=_CtATMTrafficServiceCategoriesSupportedEntry_Object((1,3,6,1,4,1,52,4,1,2,10,1,7,2,1))
ctATMTrafficServiceCategoriesSupportedEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:ctATMTrafficServiceCategoriesSupportedEntry.setStatus(_A)
class _CtATMTrafficServiceCategoriesSupportedBitMask_Type(Bits):namedValues=NamedValues(*(('other',0),('pvcBandwidthAllocation',1),('cbr',2),('vbrnrt',3),('ubr',4),('abr',5),('vbrrt',6)))
_CtATMTrafficServiceCategoriesSupportedBitMask_Type.__name__='Bits'
_CtATMTrafficServiceCategoriesSupportedBitMask_Object=MibTableColumn
ctATMTrafficServiceCategoriesSupportedBitMask=_CtATMTrafficServiceCategoriesSupportedBitMask_Object((1,3,6,1,4,1,52,4,1,2,10,1,7,2,1,1),_CtATMTrafficServiceCategoriesSupportedBitMask_Type())
ctATMTrafficServiceCategoriesSupportedBitMask.setMaxAccess(_C)
if mibBuilder.loadTexts:ctATMTrafficServiceCategoriesSupportedBitMask.setStatus(_A)
class _CtATMTrafficManagementAllocBandwidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CtATMTrafficManagementAllocBandwidth_Type.__name__=_B
_CtATMTrafficManagementAllocBandwidth_Object=MibTableColumn
ctATMTrafficManagementAllocBandwidth=_CtATMTrafficManagementAllocBandwidth_Object((1,3,6,1,4,1,52,4,1,2,10,1,7,2,1,2),_CtATMTrafficManagementAllocBandwidth_Type())
ctATMTrafficManagementAllocBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:ctATMTrafficManagementAllocBandwidth.setStatus(_A)
mibBuilder.exportSymbols(_O,**{'AtmAddress':AtmAddress,'ctATMBaseConfig':ctATMBaseConfig,'ctATMPvcIfDef':ctATMPvcIfDef,'ctATMLecIfDef':ctATMLecIfDef,'ctATMDefApplicationTable':ctATMDefApplicationTable,'ctATMDefApplicationEntry':ctATMDefApplicationEntry,'ctATMDefApplicationIfIndex':ctATMDefApplicationIfIndex,'ctATMDefApplication':ctATMDefApplication,'ctATMFramerStatusTable':ctATMFramerStatusTable,'ctATMFramerStatusEntry':ctATMFramerStatusEntry,'ctATMFramerStatusIfIndex':ctATMFramerStatusIfIndex,'ctATMFramerStatus':ctATMFramerStatus,'ctATMLecArpMacTable':ctATMLecArpMacTable,'ctATMLecArpMacEntry':ctATMLecArpMacEntry,'ctATMLecArpMacLecIndex':ctATMLecArpMacLecIndex,'ctATMLecArpMacAddress':ctATMLecArpMacAddress,'ctATMLecArpMacElanName':ctATMLecArpMacElanName,'ctATMLecArpMacVpi':ctATMLecArpMacVpi,'ctATMLecArpMacVci':ctATMLecArpMacVci,'ctATMLecArpMacATMAddress':ctATMLecArpMacATMAddress,'ctATMPvcBwAllocTable':ctATMPvcBwAllocTable,'ctATMPvcBwAllocEntry':ctATMPvcBwAllocEntry,'ctATMPvcBwAllocPhysIface':ctATMPvcBwAllocPhysIface,'ctATMPvcBwAllocStatus':ctATMPvcBwAllocStatus,'ctATMPvcBwAllocBandwidth':ctATMPvcBwAllocBandwidth,'ctATMDiscoveryElanTable':ctATMDiscoveryElanTable,'ctATMDiscoveryElanEntry':ctATMDiscoveryElanEntry,_W:ctATMDiscoveryElanIndex,'ctATMDiscoveryElanName':ctATMDiscoveryElanName,'ctATMDiscoveryElanMode':ctATMDiscoveryElanMode,'ctATMDiscoveryElanStatus':ctATMDiscoveryElanStatus,'ctATMDiscoveryElanPhysIface':ctATMDiscoveryElanPhysIface,'ctATMVclTable':ctATMVclTable,'ctATMVclEntry':ctATMVclEntry,'ctATMVclIfIndex':ctATMVclIfIndex,'ctATMVclVpi':ctATMVclVpi,'ctATMVclVci':ctATMVclVci,'ctATMVclVirtualIfIndex':ctATMVclVirtualIfIndex,'ctATMVclApplicationPort':ctATMVclApplicationPort,'ctATMVclATMAddress':ctATMVclATMAddress,'ctATMVclEncapsulationType':ctATMVclEncapsulationType,'ctATMPhysicalRedundancy':ctATMPhysicalRedundancy,'ctATMPhysicalRedundancyInterface':ctATMPhysicalRedundancyInterface,'ctATMPhyRedundTable':ctATMPhyRedundTable,'ctATMPhyRedundEntry':ctATMPhyRedundEntry,'ctATMPhyRedundIfIndex':ctATMPhyRedundIfIndex,'ctATMPhyRedundPrimaryPort':ctATMPhyRedundPrimaryPort,'ctATMPhyRedundActivePort':ctATMPhyRedundActivePort,'ctATMPhyRedundStatus':ctATMPhyRedundStatus,'ctATMPhyRedundActivation':ctATMPhyRedundActivation,'ctATMPhyRedundPrimaryRevert':ctATMPhyRedundPrimaryRevert,'ctATMPhyRedundPerformTest':ctATMPhyRedundPerformTest,'ctATMPhyRedundTestTOD':ctATMPhyRedundTestTOD,'ctATMPhyRedundTestResult':ctATMPhyRedundTestResult,'ctATMPhyRedundReset':ctATMPhyRedundReset,'ctATMIlmi':ctATMIlmi,'ctATMIlmiTable':ctATMIlmiTable,'ctATMIlmiEntry':ctATMIlmiEntry,'ctATMIlmiIfIndex':ctATMIlmiIfIndex,'ctATMIlmiStatus':ctATMIlmiStatus,'ctATMIlmiAtmAddress':ctATMIlmiAtmAddress,'ctATMIlmiState':ctATMIlmiState,'ctATMIlmiRestart':ctATMIlmiRestart,'ctATMSignalConfig':ctATMSignalConfig,'ctATMSignalTable':ctATMSignalTable,'ctATMSignalEntry':ctATMSignalEntry,'ctATMSignalIfIndex':ctATMSignalIfIndex,'ctATMSignalStatus':ctATMSignalStatus,'ctATMSignalType':ctATMSignalType,'ctATMSignalQ93Status':ctATMSignalQ93Status,'ctATMSignalQsaalStatus':ctATMSignalQsaalStatus,'ctATMSignalRestart':ctATMSignalRestart,'ctATMLANEServices':ctATMLANEServices,'ctATMLANEInfoExtGroup':ctATMLANEInfoExtGroup,'ctATMLANEInfoExtStatusTable':ctATMLANEInfoExtStatusTable,'ctATMLANEInfoExtStatusEntry':ctATMLANEInfoExtStatusEntry,'ctATMLANEInfoExtStatusUpTime':ctATMLANEInfoExtStatusUpTime,'ctATMLANEInfoExtStatus':ctATMLANEInfoExtStatus,'ctATMLANEInfoExtStatusSendTopo':ctATMLANEInfoExtStatusSendTopo,'ctATMLANEInfoExtStatusTimeLeft':ctATMLANEInfoExtStatusTimeLeft,'ctATMLANEInfoExtStatusNumQueues':ctATMLANEInfoExtStatusNumQueues,'ctATMLANEInfoExtStatusMaxNumQueues':ctATMLANEInfoExtStatusMaxNumQueues,'ctATMLANEInfoExtTMTable':ctATMLANEInfoExtTMTable,'ctATMLANEInfoExtTMEntry':ctATMLANEInfoExtTMEntry,_a:ctATMLANEInfoExtTMIndex,'ctATMLANEInfoExtTMTrafficDescrIndex':ctATMLANEInfoExtTMTrafficDescrIndex,'ctATMTrafficManagementGroup':ctATMTrafficManagementGroup,'ctATMTrafficDescrNameTable':ctATMTrafficDescrNameTable,'ctATMTrafficDescrNameEntry':ctATMTrafficDescrNameEntry,'ctATMTrafficDescrName':ctATMTrafficDescrName,'ctATMTrafficServiceCategoriesSupportedTable':ctATMTrafficServiceCategoriesSupportedTable,'ctATMTrafficServiceCategoriesSupportedEntry':ctATMTrafficServiceCategoriesSupportedEntry,'ctATMTrafficServiceCategoriesSupportedBitMask':ctATMTrafficServiceCategoriesSupportedBitMask,'ctATMTrafficManagementAllocBandwidth':ctATMTrafficManagementAllocBandwidth})