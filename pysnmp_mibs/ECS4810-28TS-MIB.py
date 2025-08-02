_u='switchDevice'
_t='ntpAuthKeyId'
_s='destroy'
_r='active'
_q='create'
_p='ntpServerIpAddress'
_o='sntpServerIndex'
_n='unicast'
_m='vlanPortIndex'
_l='vlanIndex'
_k='config'
_j='opcode'
_i='mstInstanceOperIndex'
_h='mstInstanceEditIndex'
_g='xstInstancePortPort'
_f='xstInstancePortInstance'
_e='xstInstanceCfgIndex'
_d='StaPathCostMode'
_c='staPortIndex'
_b='lacpPortIndex'
_a='trunkIndex'
_Z='dot3xFlowControl'
_Y='backPressure'
_X='fullDuplex1000'
_W='halfDuplex1000'
_V='fullDuplex100'
_U='halfDuplex100'
_T='fullDuplex10'
_S='halfDuplex10'
_R='portIndex'
_Q='master'
_P='swUnitIndex'
_O='MacAddress'
_N='ifIndex'
_M='IF-MIB'
_L='enabled'
_K='EnabledStatus'
_J='disabled'
_I='read-create'
_H='OctetString'
_G='not-accessible'
_F='ECS4810-28TS-MIB'
_E='DisplayString'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
BridgeId,Timeout,dot1dStpPort,dot1dStpPortEntry=mibBuilder.importSymbols('BRIDGE-MIB','BridgeId','Timeout','dot1dStpPort','dot1dStpPortEntry')
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_M,'InterfaceIndex',_N)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB',_K)
PortList,VlanIndex=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList','VlanIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_E,_O,'PhysAddress','RowStatus','TextualConvention','TruthValue')
MacAddress,=mibBuilder.importSymbols('TOKEN-RING-RMON-MIB',_O)
ecs4810_28tsMIB=ModuleIdentity((1,3,6,1,4,1,259,10,1,18))
if mibBuilder.loadTexts:ecs4810_28tsMIB.setRevisions(('2001-09-06 00:00',))
class KeySegment(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
class ValidStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),('invalid',2)))
class StaPathCostMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('short',1),('long',2)))
_Accton_ObjectIdentity=ObjectIdentity
accton=_Accton_ObjectIdentity((1,3,6,1,4,1,259))
_Edgecorenetworks_ObjectIdentity=ObjectIdentity
edgecorenetworks=_Edgecorenetworks_ObjectIdentity((1,3,6,1,4,1,259,10))
_EdgeCoreNetworksMgt_ObjectIdentity=ObjectIdentity
edgeCoreNetworksMgt=_EdgeCoreNetworksMgt_ObjectIdentity((1,3,6,1,4,1,259,10,1))
_Ecs4810_28tsMIBObjects_ObjectIdentity=ObjectIdentity
ecs4810_28tsMIBObjects=_Ecs4810_28tsMIBObjects_ObjectIdentity((1,3,6,1,4,1,259,10,1,18,1))
_SwitchMgt_ObjectIdentity=ObjectIdentity
switchMgt=_SwitchMgt_ObjectIdentity((1,3,6,1,4,1,259,10,1,18,1,1))
class _SwitchManagementVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4092))
_SwitchManagementVlan_Type.__name__=_C
_SwitchManagementVlan_Object=MibScalar
switchManagementVlan=_SwitchManagementVlan_Object((1,3,6,1,4,1,259,10,1,18,1,1,1),_SwitchManagementVlan_Type())
switchManagementVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:switchManagementVlan.setStatus(_A)
_SwitchNumber_Type=Integer32
_SwitchNumber_Object=MibScalar
switchNumber=_SwitchNumber_Object((1,3,6,1,4,1,259,10,1,18,1,1,2),_SwitchNumber_Type())
switchNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:switchNumber.setStatus(_A)
_SwitchInfoTable_Object=MibTable
switchInfoTable=_SwitchInfoTable_Object((1,3,6,1,4,1,259,10,1,18,1,1,3))
if mibBuilder.loadTexts:switchInfoTable.setStatus(_A)
_SwitchInfoEntry_Object=MibTableRow
switchInfoEntry=_SwitchInfoEntry_Object((1,3,6,1,4,1,259,10,1,18,1,1,3,1))
switchInfoEntry.setIndexNames((0,_F,_P))
if mibBuilder.loadTexts:switchInfoEntry.setStatus(_A)
class _SwUnitIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_SwUnitIndex_Type.__name__=_C
_SwUnitIndex_Object=MibTableColumn
swUnitIndex=_SwUnitIndex_Object((1,3,6,1,4,1,259,10,1,18,1,1,3,1,1),_SwUnitIndex_Type())
swUnitIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:swUnitIndex.setStatus(_A)
class _SwHardwareVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_SwHardwareVer_Type.__name__=_E
_SwHardwareVer_Object=MibTableColumn
swHardwareVer=_SwHardwareVer_Object((1,3,6,1,4,1,259,10,1,18,1,1,3,1,2),_SwHardwareVer_Type())
swHardwareVer.setMaxAccess(_B)
if mibBuilder.loadTexts:swHardwareVer.setStatus(_A)
class _SwMicrocodeVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_SwMicrocodeVer_Type.__name__=_E
_SwMicrocodeVer_Object=MibTableColumn
swMicrocodeVer=_SwMicrocodeVer_Object((1,3,6,1,4,1,259,10,1,18,1,1,3,1,3),_SwMicrocodeVer_Type())
swMicrocodeVer.setMaxAccess(_B)
if mibBuilder.loadTexts:swMicrocodeVer.setStatus(_A)
class _SwLoaderVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_SwLoaderVer_Type.__name__=_E
_SwLoaderVer_Object=MibTableColumn
swLoaderVer=_SwLoaderVer_Object((1,3,6,1,4,1,259,10,1,18,1,1,3,1,4),_SwLoaderVer_Type())
swLoaderVer.setMaxAccess(_B)
if mibBuilder.loadTexts:swLoaderVer.setStatus(_A)
class _SwBootRomVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_SwBootRomVer_Type.__name__=_E
_SwBootRomVer_Object=MibTableColumn
swBootRomVer=_SwBootRomVer_Object((1,3,6,1,4,1,259,10,1,18,1,1,3,1,5),_SwBootRomVer_Type())
swBootRomVer.setMaxAccess(_B)
if mibBuilder.loadTexts:swBootRomVer.setStatus(_A)
class _SwOpCodeVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_SwOpCodeVer_Type.__name__=_E
_SwOpCodeVer_Object=MibTableColumn
swOpCodeVer=_SwOpCodeVer_Object((1,3,6,1,4,1,259,10,1,18,1,1,3,1,6),_SwOpCodeVer_Type())
swOpCodeVer.setMaxAccess(_B)
if mibBuilder.loadTexts:swOpCodeVer.setStatus(_A)
_SwPortNumber_Type=Integer32
_SwPortNumber_Object=MibTableColumn
swPortNumber=_SwPortNumber_Object((1,3,6,1,4,1,259,10,1,18,1,1,3,1,7),_SwPortNumber_Type())
swPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:swPortNumber.setStatus(_A)
class _SwPowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('internalPower',1),('redundantPower',2),('internalAndRedundantPower',3)))
_SwPowerStatus_Type.__name__=_C
_SwPowerStatus_Object=MibTableColumn
swPowerStatus=_SwPowerStatus_Object((1,3,6,1,4,1,259,10,1,18,1,1,3,1,8),_SwPowerStatus_Type())
swPowerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:swPowerStatus.setStatus(_A)
class _SwRoleInSystem_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Q,1),('backupMaster',2),('slave',3)))
_SwRoleInSystem_Type.__name__=_C
_SwRoleInSystem_Object=MibTableColumn
swRoleInSystem=_SwRoleInSystem_Object((1,3,6,1,4,1,259,10,1,18,1,1,3,1,9),_SwRoleInSystem_Type())
swRoleInSystem.setMaxAccess(_B)
if mibBuilder.loadTexts:swRoleInSystem.setStatus(_A)
class _SwSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_SwSerialNumber_Type.__name__=_E
_SwSerialNumber_Object=MibTableColumn
swSerialNumber=_SwSerialNumber_Object((1,3,6,1,4,1,259,10,1,18,1,1,3,1,10),_SwSerialNumber_Type())
swSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:swSerialNumber.setStatus(_A)
class _SwServiceTag_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_SwServiceTag_Type.__name__=_E
_SwServiceTag_Object=MibTableColumn
swServiceTag=_SwServiceTag_Object((1,3,6,1,4,1,259,10,1,18,1,1,3,1,13),_SwServiceTag_Type())
swServiceTag.setMaxAccess(_B)
if mibBuilder.loadTexts:swServiceTag.setStatus(_A)
class _SwitchOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('other',1),('unknown',2),('ok',3),('noncritical',4),('critical',5),('nonrecoverable',6)))
_SwitchOperState_Type.__name__=_C
_SwitchOperState_Object=MibScalar
switchOperState=_SwitchOperState_Object((1,3,6,1,4,1,259,10,1,18,1,1,4),_SwitchOperState_Type())
switchOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:switchOperState.setStatus(_A)
_SwitchProductId_ObjectIdentity=ObjectIdentity
switchProductId=_SwitchProductId_ObjectIdentity((1,3,6,1,4,1,259,10,1,18,1,1,5))
class _SwProdName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_SwProdName_Type.__name__=_E
_SwProdName_Object=MibScalar
swProdName=_SwProdName_Object((1,3,6,1,4,1,259,10,1,18,1,1,5,1),_SwProdName_Type())
swProdName.setMaxAccess(_B)
if mibBuilder.loadTexts:swProdName.setStatus(_A)
class _SwProdManufacturer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_SwProdManufacturer_Type.__name__=_E
_SwProdManufacturer_Object=MibScalar
swProdManufacturer=_SwProdManufacturer_Object((1,3,6,1,4,1,259,10,1,18,1,1,5,2),_SwProdManufacturer_Type())
swProdManufacturer.setMaxAccess(_B)
if mibBuilder.loadTexts:swProdManufacturer.setStatus(_A)
class _SwProdDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_SwProdDescription_Type.__name__=_E
_SwProdDescription_Object=MibScalar
swProdDescription=_SwProdDescription_Object((1,3,6,1,4,1,259,10,1,18,1,1,5,3),_SwProdDescription_Type())
swProdDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:swProdDescription.setStatus(_A)
class _SwProdVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_SwProdVersion_Type.__name__=_E
_SwProdVersion_Object=MibScalar
swProdVersion=_SwProdVersion_Object((1,3,6,1,4,1,259,10,1,18,1,1,5,4),_SwProdVersion_Type())
swProdVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:swProdVersion.setStatus(_A)
class _SwProdUrl_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_SwProdUrl_Type.__name__=_E
_SwProdUrl_Object=MibScalar
swProdUrl=_SwProdUrl_Object((1,3,6,1,4,1,259,10,1,18,1,1,5,5),_SwProdUrl_Type())
swProdUrl.setMaxAccess(_B)
if mibBuilder.loadTexts:swProdUrl.setStatus(_A)
_SwIdentifier_Type=Integer32
_SwIdentifier_Object=MibScalar
swIdentifier=_SwIdentifier_Object((1,3,6,1,4,1,259,10,1,18,1,1,5,6),_SwIdentifier_Type())
swIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:swIdentifier.setStatus(_A)
class _SwChassisServiceTag_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_SwChassisServiceTag_Type.__name__=_E
_SwChassisServiceTag_Object=MibScalar
swChassisServiceTag=_SwChassisServiceTag_Object((1,3,6,1,4,1,259,10,1,18,1,1,5,7),_SwChassisServiceTag_Type())
swChassisServiceTag.setMaxAccess(_B)
if mibBuilder.loadTexts:swChassisServiceTag.setStatus(_A)
_AmtrMgt_ObjectIdentity=ObjectIdentity
amtrMgt=_AmtrMgt_ObjectIdentity((1,3,6,1,4,1,259,10,1,18,1,1,8))
_AmtrMacAddrAgingStatus_Type=EnabledStatus
_AmtrMacAddrAgingStatus_Object=MibScalar
amtrMacAddrAgingStatus=_AmtrMacAddrAgingStatus_Object((1,3,6,1,4,1,259,10,1,18,1,1,8,3),_AmtrMacAddrAgingStatus_Type())
amtrMacAddrAgingStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:amtrMacAddrAgingStatus.setStatus(_A)
_PortMgt_ObjectIdentity=ObjectIdentity
portMgt=_PortMgt_ObjectIdentity((1,3,6,1,4,1,259,10,1,18,1,2))
_PortTable_Object=MibTable
portTable=_PortTable_Object((1,3,6,1,4,1,259,10,1,18,1,2,1))
if mibBuilder.loadTexts:portTable.setStatus(_A)
_PortEntry_Object=MibTableRow
portEntry=_PortEntry_Object((1,3,6,1,4,1,259,10,1,18,1,2,1,1))
portEntry.setIndexNames((0,_F,_R))
if mibBuilder.loadTexts:portEntry.setStatus(_A)
_PortIndex_Type=InterfaceIndex
_PortIndex_Object=MibTableColumn
portIndex=_PortIndex_Object((1,3,6,1,4,1,259,10,1,18,1,2,1,1,1),_PortIndex_Type())
portIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:portIndex.setStatus(_A)
class _PortName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_PortName_Type.__name__=_E
_PortName_Object=MibTableColumn
portName=_PortName_Object((1,3,6,1,4,1,259,10,1,18,1,2,1,1,2),_PortName_Type())
portName.setMaxAccess(_B)
if mibBuilder.loadTexts:portName.setStatus(_A)
class _PortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('other',1),('hundredBaseTX',2),('hundredBaseFX',3),('thousandBaseSX',4),('thousandBaseLX',5),('thousandBaseT',6),('thousandBaseGBIC',7),('thousandBaseSfp',8),('hundredBaseFxScSingleMode',9),('hundredBaseFxScMultiMode',10)))
_PortType_Type.__name__=_C
_PortType_Object=MibTableColumn
portType=_PortType_Object((1,3,6,1,4,1,259,10,1,18,1,2,1,1,3),_PortType_Type())
portType.setMaxAccess(_B)
if mibBuilder.loadTexts:portType.setStatus(_A)
class _PortSpeedDpxCfg_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('reserved',1),(_S,2),(_T,3),(_U,4),(_V,5),(_W,6),(_X,7)))
_PortSpeedDpxCfg_Type.__name__=_C
_PortSpeedDpxCfg_Object=MibTableColumn
portSpeedDpxCfg=_PortSpeedDpxCfg_Object((1,3,6,1,4,1,259,10,1,18,1,2,1,1,4),_PortSpeedDpxCfg_Type())
portSpeedDpxCfg.setMaxAccess(_D)
if mibBuilder.loadTexts:portSpeedDpxCfg.setStatus(_A)
class _PortFlowCtrlCfg_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_L,1),(_J,2),(_Y,3),(_Z,4)))
_PortFlowCtrlCfg_Type.__name__=_C
_PortFlowCtrlCfg_Object=MibTableColumn
portFlowCtrlCfg=_PortFlowCtrlCfg_Object((1,3,6,1,4,1,259,10,1,18,1,2,1,1,5),_PortFlowCtrlCfg_Type())
portFlowCtrlCfg.setMaxAccess(_D)
if mibBuilder.loadTexts:portFlowCtrlCfg.setStatus(_A)
class _PortCapabilities_Type(Bits):namedValues=NamedValues(*(('portCap10half',0),('portCap10full',1),('portCap100half',2),('portCap100full',3),('portCap1000half',4),('portCap1000full',5),('reserved6',6),('reserved7',7),('reserved8',8),('reserved9',9),('reserved10',10),('reserved11',11),('reserved12',12),('reserved13',13),('portCapSym',14),('portCapFlowCtrl',15)))
_PortCapabilities_Type.__name__='Bits'
_PortCapabilities_Object=MibTableColumn
portCapabilities=_PortCapabilities_Object((1,3,6,1,4,1,259,10,1,18,1,2,1,1,6),_PortCapabilities_Type())
portCapabilities.setMaxAccess(_B)
if mibBuilder.loadTexts:portCapabilities.setStatus(_A)
class _PortAutonegotiation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_J,2)))
_PortAutonegotiation_Type.__name__=_C
_PortAutonegotiation_Object=MibTableColumn
portAutonegotiation=_PortAutonegotiation_Object((1,3,6,1,4,1,259,10,1,18,1,2,1,1,7),_PortAutonegotiation_Type())
portAutonegotiation.setMaxAccess(_D)
if mibBuilder.loadTexts:portAutonegotiation.setStatus(_A)
class _PortSpeedDpxStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('error',1),(_S,2),(_T,3),(_U,4),(_V,5),(_W,6),(_X,7)))
_PortSpeedDpxStatus_Type.__name__=_C
_PortSpeedDpxStatus_Object=MibTableColumn
portSpeedDpxStatus=_PortSpeedDpxStatus_Object((1,3,6,1,4,1,259,10,1,18,1,2,1,1,8),_PortSpeedDpxStatus_Type())
portSpeedDpxStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:portSpeedDpxStatus.setStatus(_A)
class _PortFlowCtrlStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('error',1),(_Y,2),(_Z,3),('none',4)))
_PortFlowCtrlStatus_Type.__name__=_C
_PortFlowCtrlStatus_Object=MibTableColumn
portFlowCtrlStatus=_PortFlowCtrlStatus_Object((1,3,6,1,4,1,259,10,1,18,1,2,1,1,9),_PortFlowCtrlStatus_Type())
portFlowCtrlStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:portFlowCtrlStatus.setStatus(_A)
_PortTrunkIndex_Type=Integer32
_PortTrunkIndex_Object=MibTableColumn
portTrunkIndex=_PortTrunkIndex_Object((1,3,6,1,4,1,259,10,1,18,1,2,1,1,10),_PortTrunkIndex_Type())
portTrunkIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:portTrunkIndex.setStatus(_A)
_TrunkMgt_ObjectIdentity=ObjectIdentity
trunkMgt=_TrunkMgt_ObjectIdentity((1,3,6,1,4,1,259,10,1,18,1,3))
_TrunkMaxId_Type=Integer32
_TrunkMaxId_Object=MibScalar
trunkMaxId=_TrunkMaxId_Object((1,3,6,1,4,1,259,10,1,18,1,3,1),_TrunkMaxId_Type())
trunkMaxId.setMaxAccess(_B)
if mibBuilder.loadTexts:trunkMaxId.setStatus(_A)
_TrunkValidNumber_Type=Integer32
_TrunkValidNumber_Object=MibScalar
trunkValidNumber=_TrunkValidNumber_Object((1,3,6,1,4,1,259,10,1,18,1,3,2),_TrunkValidNumber_Type())
trunkValidNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:trunkValidNumber.setStatus(_A)
_TrunkTable_Object=MibTable
trunkTable=_TrunkTable_Object((1,3,6,1,4,1,259,10,1,18,1,3,3))
if mibBuilder.loadTexts:trunkTable.setStatus(_A)
_TrunkEntry_Object=MibTableRow
trunkEntry=_TrunkEntry_Object((1,3,6,1,4,1,259,10,1,18,1,3,3,1))
trunkEntry.setIndexNames((0,_F,_a))
if mibBuilder.loadTexts:trunkEntry.setStatus(_A)
class _TrunkIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_TrunkIndex_Type.__name__=_C
_TrunkIndex_Object=MibTableColumn
trunkIndex=_TrunkIndex_Object((1,3,6,1,4,1,259,10,1,18,1,3,3,1,1),_TrunkIndex_Type())
trunkIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:trunkIndex.setStatus(_A)
_TrunkPorts_Type=PortList
_TrunkPorts_Object=MibTableColumn
trunkPorts=_TrunkPorts_Object((1,3,6,1,4,1,259,10,1,18,1,3,3,1,2),_TrunkPorts_Type())
trunkPorts.setMaxAccess(_I)
if mibBuilder.loadTexts:trunkPorts.setStatus(_A)
class _TrunkCreation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('static',1),('lacp',2)))
_TrunkCreation_Type.__name__=_C
_TrunkCreation_Object=MibTableColumn
trunkCreation=_TrunkCreation_Object((1,3,6,1,4,1,259,10,1,18,1,3,3,1,3),_TrunkCreation_Type())
trunkCreation.setMaxAccess(_B)
if mibBuilder.loadTexts:trunkCreation.setStatus(_A)
_TrunkStatus_Type=ValidStatus
_TrunkStatus_Object=MibTableColumn
trunkStatus=_TrunkStatus_Object((1,3,6,1,4,1,259,10,1,18,1,3,3,1,4),_TrunkStatus_Type())
trunkStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:trunkStatus.setStatus(_A)
_LacpMgt_ObjectIdentity=ObjectIdentity
lacpMgt=_LacpMgt_ObjectIdentity((1,3,6,1,4,1,259,10,1,18,1,4))
_LacpPortTable_Object=MibTable
lacpPortTable=_LacpPortTable_Object((1,3,6,1,4,1,259,10,1,18,1,4,1))
if mibBuilder.loadTexts:lacpPortTable.setStatus(_A)
_LacpPortEntry_Object=MibTableRow
lacpPortEntry=_LacpPortEntry_Object((1,3,6,1,4,1,259,10,1,18,1,4,1,1))
lacpPortEntry.setIndexNames((0,_F,_b))
if mibBuilder.loadTexts:lacpPortEntry.setStatus(_A)
_LacpPortIndex_Type=InterfaceIndex
_LacpPortIndex_Object=MibTableColumn
lacpPortIndex=_LacpPortIndex_Object((1,3,6,1,4,1,259,10,1,18,1,4,1,1,1),_LacpPortIndex_Type())
lacpPortIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:lacpPortIndex.setStatus(_A)
class _LacpPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_J,2)))
_LacpPortStatus_Type.__name__=_C
_LacpPortStatus_Object=MibTableColumn
lacpPortStatus=_LacpPortStatus_Object((1,3,6,1,4,1,259,10,1,18,1,4,1,1,2),_LacpPortStatus_Type())
lacpPortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:lacpPortStatus.setStatus(_A)
_StaMgt_ObjectIdentity=ObjectIdentity
staMgt=_StaMgt_ObjectIdentity((1,3,6,1,4,1,259,10,1,18,1,5))
class _StaSystemStatus_Type(EnabledStatus):defaultValue=1
_StaSystemStatus_Type.__name__=_K
_StaSystemStatus_Object=MibScalar
staSystemStatus=_StaSystemStatus_Object((1,3,6,1,4,1,259,10,1,18,1,5,1),_StaSystemStatus_Type())
staSystemStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:staSystemStatus.setStatus(_A)
_StaPortTable_Object=MibTable
staPortTable=_StaPortTable_Object((1,3,6,1,4,1,259,10,1,18,1,5,2))
if mibBuilder.loadTexts:staPortTable.setStatus(_A)
_StaPortEntry_Object=MibTableRow
staPortEntry=_StaPortEntry_Object((1,3,6,1,4,1,259,10,1,18,1,5,2,1))
staPortEntry.setIndexNames((0,_F,_c))
if mibBuilder.loadTexts:staPortEntry.setStatus(_A)
class _StaPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_StaPortIndex_Type.__name__=_C
_StaPortIndex_Object=MibTableColumn
staPortIndex=_StaPortIndex_Object((1,3,6,1,4,1,259,10,1,18,1,5,2,1,1),_StaPortIndex_Type())
staPortIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:staPortIndex.setStatus(_A)
_StaPortFastForward_Type=EnabledStatus
_StaPortFastForward_Object=MibTableColumn
staPortFastForward=_StaPortFastForward_Object((1,3,6,1,4,1,259,10,1,18,1,5,2,1,2),_StaPortFastForward_Type())
staPortFastForward.setMaxAccess(_D)
if mibBuilder.loadTexts:staPortFastForward.setStatus(_A)
_StaPortProtocolMigration_Type=TruthValue
_StaPortProtocolMigration_Object=MibTableColumn
staPortProtocolMigration=_StaPortProtocolMigration_Object((1,3,6,1,4,1,259,10,1,18,1,5,2,1,3),_StaPortProtocolMigration_Type())
staPortProtocolMigration.setMaxAccess(_D)
if mibBuilder.loadTexts:staPortProtocolMigration.setStatus(_A)
_StaPortAdminEdgePort_Type=TruthValue
_StaPortAdminEdgePort_Object=MibTableColumn
staPortAdminEdgePort=_StaPortAdminEdgePort_Object((1,3,6,1,4,1,259,10,1,18,1,5,2,1,4),_StaPortAdminEdgePort_Type())
staPortAdminEdgePort.setMaxAccess(_D)
if mibBuilder.loadTexts:staPortAdminEdgePort.setStatus(_A)
_StaPortOperEdgePort_Type=TruthValue
_StaPortOperEdgePort_Object=MibTableColumn
staPortOperEdgePort=_StaPortOperEdgePort_Object((1,3,6,1,4,1,259,10,1,18,1,5,2,1,5),_StaPortOperEdgePort_Type())
staPortOperEdgePort.setMaxAccess(_B)
if mibBuilder.loadTexts:staPortOperEdgePort.setStatus(_A)
class _StaPortAdminPointToPoint_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('forceTrue',0),('forceFalse',1),('auto',2)))
_StaPortAdminPointToPoint_Type.__name__=_C
_StaPortAdminPointToPoint_Object=MibTableColumn
staPortAdminPointToPoint=_StaPortAdminPointToPoint_Object((1,3,6,1,4,1,259,10,1,18,1,5,2,1,6),_StaPortAdminPointToPoint_Type())
staPortAdminPointToPoint.setMaxAccess(_D)
if mibBuilder.loadTexts:staPortAdminPointToPoint.setStatus(_A)
_StaPortOperPointToPoint_Type=TruthValue
_StaPortOperPointToPoint_Object=MibTableColumn
staPortOperPointToPoint=_StaPortOperPointToPoint_Object((1,3,6,1,4,1,259,10,1,18,1,5,2,1,7),_StaPortOperPointToPoint_Type())
staPortOperPointToPoint.setMaxAccess(_B)
if mibBuilder.loadTexts:staPortOperPointToPoint.setStatus(_A)
class _StaPortLongPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,200000000))
_StaPortLongPathCost_Type.__name__=_C
_StaPortLongPathCost_Object=MibTableColumn
staPortLongPathCost=_StaPortLongPathCost_Object((1,3,6,1,4,1,259,10,1,18,1,5,2,1,8),_StaPortLongPathCost_Type())
staPortLongPathCost.setMaxAccess(_D)
if mibBuilder.loadTexts:staPortLongPathCost.setStatus(_A)
class _StaPortSystemStatus_Type(EnabledStatus):defaultValue=1
_StaPortSystemStatus_Type.__name__=_K
_StaPortSystemStatus_Object=MibTableColumn
staPortSystemStatus=_StaPortSystemStatus_Object((1,3,6,1,4,1,259,10,1,18,1,5,2,1,9),_StaPortSystemStatus_Type())
staPortSystemStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:staPortSystemStatus.setStatus(_A)
class _StaProtocolType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('stp',1),('rstp',2),('mstp',3)))
_StaProtocolType_Type.__name__=_C
_StaProtocolType_Object=MibScalar
staProtocolType=_StaProtocolType_Object((1,3,6,1,4,1,259,10,1,18,1,5,3),_StaProtocolType_Type())
staProtocolType.setMaxAccess(_D)
if mibBuilder.loadTexts:staProtocolType.setStatus(_A)
class _StaTxHoldCount_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_StaTxHoldCount_Type.__name__=_C
_StaTxHoldCount_Object=MibScalar
staTxHoldCount=_StaTxHoldCount_Object((1,3,6,1,4,1,259,10,1,18,1,5,4),_StaTxHoldCount_Type())
staTxHoldCount.setMaxAccess(_D)
if mibBuilder.loadTexts:staTxHoldCount.setStatus(_A)
class _StaPathCostMethod_Type(StaPathCostMode):defaultValue=1
_StaPathCostMethod_Type.__name__=_d
_StaPathCostMethod_Object=MibScalar
staPathCostMethod=_StaPathCostMethod_Object((1,3,6,1,4,1,259,10,1,18,1,5,5),_StaPathCostMethod_Type())
staPathCostMethod.setMaxAccess(_D)
if mibBuilder.loadTexts:staPathCostMethod.setStatus(_A)
_XstMgt_ObjectIdentity=ObjectIdentity
xstMgt=_XstMgt_ObjectIdentity((1,3,6,1,4,1,259,10,1,18,1,5,6))
class _MstName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_MstName_Type.__name__=_E
_MstName_Object=MibScalar
mstName=_MstName_Object((1,3,6,1,4,1,259,10,1,18,1,5,6,1),_MstName_Type())
mstName.setMaxAccess(_D)
if mibBuilder.loadTexts:mstName.setStatus(_A)
_MstRevision_Type=Integer32
_MstRevision_Object=MibScalar
mstRevision=_MstRevision_Object((1,3,6,1,4,1,259,10,1,18,1,5,6,2),_MstRevision_Type())
mstRevision.setMaxAccess(_D)
if mibBuilder.loadTexts:mstRevision.setStatus(_A)
class _MstMaxHops_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,40))
_MstMaxHops_Type.__name__=_C
_MstMaxHops_Object=MibScalar
mstMaxHops=_MstMaxHops_Object((1,3,6,1,4,1,259,10,1,18,1,5,6,3),_MstMaxHops_Type())
mstMaxHops.setMaxAccess(_D)
if mibBuilder.loadTexts:mstMaxHops.setStatus(_A)
_XstInstanceCfgTable_Object=MibTable
xstInstanceCfgTable=_XstInstanceCfgTable_Object((1,3,6,1,4,1,259,10,1,18,1,5,6,4))
if mibBuilder.loadTexts:xstInstanceCfgTable.setStatus(_A)
_XstInstanceCfgEntry_Object=MibTableRow
xstInstanceCfgEntry=_XstInstanceCfgEntry_Object((1,3,6,1,4,1,259,10,1,18,1,5,6,4,1))
xstInstanceCfgEntry.setIndexNames((0,_F,_e))
if mibBuilder.loadTexts:xstInstanceCfgEntry.setStatus(_A)
class _XstInstanceCfgIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_XstInstanceCfgIndex_Type.__name__=_C
_XstInstanceCfgIndex_Object=MibTableColumn
xstInstanceCfgIndex=_XstInstanceCfgIndex_Object((1,3,6,1,4,1,259,10,1,18,1,5,6,4,1,1),_XstInstanceCfgIndex_Type())
xstInstanceCfgIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:xstInstanceCfgIndex.setStatus(_A)
class _XstInstanceCfgPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,61440))
_XstInstanceCfgPriority_Type.__name__=_C
_XstInstanceCfgPriority_Object=MibTableColumn
xstInstanceCfgPriority=_XstInstanceCfgPriority_Object((1,3,6,1,4,1,259,10,1,18,1,5,6,4,1,2),_XstInstanceCfgPriority_Type())
xstInstanceCfgPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:xstInstanceCfgPriority.setStatus(_A)
_XstInstanceCfgTimeSinceTopologyChange_Type=TimeTicks
_XstInstanceCfgTimeSinceTopologyChange_Object=MibTableColumn
xstInstanceCfgTimeSinceTopologyChange=_XstInstanceCfgTimeSinceTopologyChange_Object((1,3,6,1,4,1,259,10,1,18,1,5,6,4,1,3),_XstInstanceCfgTimeSinceTopologyChange_Type())
xstInstanceCfgTimeSinceTopologyChange.setMaxAccess(_B)
if mibBuilder.loadTexts:xstInstanceCfgTimeSinceTopologyChange.setStatus(_A)
_XstInstanceCfgTopChanges_Type=Integer32
_XstInstanceCfgTopChanges_Object=MibTableColumn
xstInstanceCfgTopChanges=_XstInstanceCfgTopChanges_Object((1,3,6,1,4,1,259,10,1,18,1,5,6,4,1,4),_XstInstanceCfgTopChanges_Type())
xstInstanceCfgTopChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:xstInstanceCfgTopChanges.setStatus(_A)
_XstInstanceCfgDesignatedRoot_Type=BridgeId
_XstInstanceCfgDesignatedRoot_Object=MibTableColumn
xstInstanceCfgDesignatedRoot=_XstInstanceCfgDesignatedRoot_Object((1,3,6,1,4,1,259,10,1,18,1,5,6,4,1,5),_XstInstanceCfgDesignatedRoot_Type())
xstInstanceCfgDesignatedRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:xstInstanceCfgDesignatedRoot.setStatus(_A)
_XstInstanceCfgRootCost_Type=Integer32
_XstInstanceCfgRootCost_Object=MibTableColumn
xstInstanceCfgRootCost=_XstInstanceCfgRootCost_Object((1,3,6,1,4,1,259,10,1,18,1,5,6,4,1,6),_XstInstanceCfgRootCost_Type())
xstInstanceCfgRootCost.setMaxAccess(_B)
if mibBuilder.loadTexts:xstInstanceCfgRootCost.setStatus(_A)
_XstInstanceCfgRootPort_Type=Integer32
_XstInstanceCfgRootPort_Object=MibTableColumn
xstInstanceCfgRootPort=_XstInstanceCfgRootPort_Object((1,3,6,1,4,1,259,10,1,18,1,5,6,4,1,7),_XstInstanceCfgRootPort_Type())
xstInstanceCfgRootPort.setMaxAccess(_B)
if mibBuilder.loadTexts:xstInstanceCfgRootPort.setStatus(_A)
_XstInstanceCfgMaxAge_Type=Timeout
_XstInstanceCfgMaxAge_Object=MibTableColumn
xstInstanceCfgMaxAge=_XstInstanceCfgMaxAge_Object((1,3,6,1,4,1,259,10,1,18,1,5,6,4,1,8),_XstInstanceCfgMaxAge_Type())
xstInstanceCfgMaxAge.setMaxAccess(_B)
if mibBuilder.loadTexts:xstInstanceCfgMaxAge.setStatus(_A)
_XstInstanceCfgHelloTime_Type=Timeout
_XstInstanceCfgHelloTime_Object=MibTableColumn
xstInstanceCfgHelloTime=_XstInstanceCfgHelloTime_Object((1,3,6,1,4,1,259,10,1,18,1,5,6,4,1,9),_XstInstanceCfgHelloTime_Type())
xstInstanceCfgHelloTime.setMaxAccess(_B)
if mibBuilder.loadTexts:xstInstanceCfgHelloTime.setStatus(_A)
_XstInstanceCfgHoldTime_Type=Timeout
_XstInstanceCfgHoldTime_Object=MibTableColumn
xstInstanceCfgHoldTime=_XstInstanceCfgHoldTime_Object((1,3,6,1,4,1,259,10,1,18,1,5,6,4,1,10),_XstInstanceCfgHoldTime_Type())
xstInstanceCfgHoldTime.setMaxAccess(_B)
if mibBuilder.loadTexts:xstInstanceCfgHoldTime.setStatus(_A)
_XstInstanceCfgForwardDelay_Type=Timeout
_XstInstanceCfgForwardDelay_Object=MibTableColumn
xstInstanceCfgForwardDelay=_XstInstanceCfgForwardDelay_Object((1,3,6,1,4,1,259,10,1,18,1,5,6,4,1,11),_XstInstanceCfgForwardDelay_Type())
xstInstanceCfgForwardDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:xstInstanceCfgForwardDelay.setStatus(_A)
_XstInstanceCfgBridgeMaxAge_Type=Timeout
_XstInstanceCfgBridgeMaxAge_Object=MibTableColumn
xstInstanceCfgBridgeMaxAge=_XstInstanceCfgBridgeMaxAge_Object((1,3,6,1,4,1,259,10,1,18,1,5,6,4,1,12),_XstInstanceCfgBridgeMaxAge_Type())
xstInstanceCfgBridgeMaxAge.setMaxAccess(_B)
if mibBuilder.loadTexts:xstInstanceCfgBridgeMaxAge.setStatus(_A)
_XstInstanceCfgBridgeHelloTime_Type=Timeout
_XstInstanceCfgBridgeHelloTime_Object=MibTableColumn
xstInstanceCfgBridgeHelloTime=_XstInstanceCfgBridgeHelloTime_Object((1,3,6,1,4,1,259,10,1,18,1,5,6,4,1,13),_XstInstanceCfgBridgeHelloTime_Type())
xstInstanceCfgBridgeHelloTime.setMaxAccess(_B)
if mibBuilder.loadTexts:xstInstanceCfgBridgeHelloTime.setStatus(_A)
_XstInstanceCfgBridgeForwardDelay_Type=Timeout
_XstInstanceCfgBridgeForwardDelay_Object=MibTableColumn
xstInstanceCfgBridgeForwardDelay=_XstInstanceCfgBridgeForwardDelay_Object((1,3,6,1,4,1,259,10,1,18,1,5,6,4,1,14),_XstInstanceCfgBridgeForwardDelay_Type())
xstInstanceCfgBridgeForwardDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:xstInstanceCfgBridgeForwardDelay.setStatus(_A)
_XstInstanceCfgTxHoldCount_Type=Integer32
_XstInstanceCfgTxHoldCount_Object=MibTableColumn
xstInstanceCfgTxHoldCount=_XstInstanceCfgTxHoldCount_Object((1,3,6,1,4,1,259,10,1,18,1,5,6,4,1,15),_XstInstanceCfgTxHoldCount_Type())
xstInstanceCfgTxHoldCount.setMaxAccess(_B)
if mibBuilder.loadTexts:xstInstanceCfgTxHoldCount.setStatus(_A)
_XstInstanceCfgPathCostMethod_Type=StaPathCostMode
_XstInstanceCfgPathCostMethod_Object=MibTableColumn
xstInstanceCfgPathCostMethod=_XstInstanceCfgPathCostMethod_Object((1,3,6,1,4,1,259,10,1,18,1,5,6,4,1,16),_XstInstanceCfgPathCostMethod_Type())
xstInstanceCfgPathCostMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:xstInstanceCfgPathCostMethod.setStatus(_A)
_XstInstancePortTable_Object=MibTable
xstInstancePortTable=_XstInstancePortTable_Object((1,3,6,1,4,1,259,10,1,18,1,5,6,5))
if mibBuilder.loadTexts:xstInstancePortTable.setStatus(_A)
_XstInstancePortEntry_Object=MibTableRow
xstInstancePortEntry=_XstInstancePortEntry_Object((1,3,6,1,4,1,259,10,1,18,1,5,6,5,1))
xstInstancePortEntry.setIndexNames((0,_F,_f),(0,_F,_g))
if mibBuilder.loadTexts:xstInstancePortEntry.setStatus(_A)
class _XstInstancePortInstance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_XstInstancePortInstance_Type.__name__=_C
_XstInstancePortInstance_Object=MibTableColumn
xstInstancePortInstance=_XstInstancePortInstance_Object((1,3,6,1,4,1,259,10,1,18,1,5,6,5,1,1),_XstInstancePortInstance_Type())
xstInstancePortInstance.setMaxAccess(_G)
if mibBuilder.loadTexts:xstInstancePortInstance.setStatus(_A)
class _XstInstancePortPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_XstInstancePortPort_Type.__name__=_C
_XstInstancePortPort_Object=MibTableColumn
xstInstancePortPort=_XstInstancePortPort_Object((1,3,6,1,4,1,259,10,1,18,1,5,6,5,1,2),_XstInstancePortPort_Type())
xstInstancePortPort.setMaxAccess(_G)
if mibBuilder.loadTexts:xstInstancePortPort.setStatus(_A)
class _XstInstancePortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,240))
_XstInstancePortPriority_Type.__name__=_C
_XstInstancePortPriority_Object=MibTableColumn
xstInstancePortPriority=_XstInstancePortPriority_Object((1,3,6,1,4,1,259,10,1,18,1,5,6,5,1,3),_XstInstancePortPriority_Type())
xstInstancePortPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:xstInstancePortPriority.setStatus(_A)
class _XstInstancePortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('discarding',1),('learning',2),('forwarding',3)))
_XstInstancePortState_Type.__name__=_C
_XstInstancePortState_Object=MibTableColumn
xstInstancePortState=_XstInstancePortState_Object((1,3,6,1,4,1,259,10,1,18,1,5,6,5,1,4),_XstInstancePortState_Type())
xstInstancePortState.setMaxAccess(_B)
if mibBuilder.loadTexts:xstInstancePortState.setStatus(_A)
_XstInstancePortEnable_Type=EnabledStatus
_XstInstancePortEnable_Object=MibTableColumn
xstInstancePortEnable=_XstInstancePortEnable_Object((1,3,6,1,4,1,259,10,1,18,1,5,6,5,1,5),_XstInstancePortEnable_Type())
xstInstancePortEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:xstInstancePortEnable.setStatus(_A)
class _XstInstancePortPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,200000000))
_XstInstancePortPathCost_Type.__name__=_C
_XstInstancePortPathCost_Object=MibTableColumn
xstInstancePortPathCost=_XstInstancePortPathCost_Object((1,3,6,1,4,1,259,10,1,18,1,5,6,5,1,6),_XstInstancePortPathCost_Type())
xstInstancePortPathCost.setMaxAccess(_D)
if mibBuilder.loadTexts:xstInstancePortPathCost.setStatus(_A)
_XstInstancePortDesignatedRoot_Type=BridgeId
_XstInstancePortDesignatedRoot_Object=MibTableColumn
xstInstancePortDesignatedRoot=_XstInstancePortDesignatedRoot_Object((1,3,6,1,4,1,259,10,1,18,1,5,6,5,1,7),_XstInstancePortDesignatedRoot_Type())
xstInstancePortDesignatedRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:xstInstancePortDesignatedRoot.setStatus(_A)
_XstInstancePortDesignatedCost_Type=Integer32
_XstInstancePortDesignatedCost_Object=MibTableColumn
xstInstancePortDesignatedCost=_XstInstancePortDesignatedCost_Object((1,3,6,1,4,1,259,10,1,18,1,5,6,5,1,8),_XstInstancePortDesignatedCost_Type())
xstInstancePortDesignatedCost.setMaxAccess(_B)
if mibBuilder.loadTexts:xstInstancePortDesignatedCost.setStatus(_A)
_XstInstancePortDesignatedBridge_Type=BridgeId
_XstInstancePortDesignatedBridge_Object=MibTableColumn
xstInstancePortDesignatedBridge=_XstInstancePortDesignatedBridge_Object((1,3,6,1,4,1,259,10,1,18,1,5,6,5,1,9),_XstInstancePortDesignatedBridge_Type())
xstInstancePortDesignatedBridge.setMaxAccess(_B)
if mibBuilder.loadTexts:xstInstancePortDesignatedBridge.setStatus(_A)
class _XstInstancePortDesignatedPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_XstInstancePortDesignatedPort_Type.__name__=_H
_XstInstancePortDesignatedPort_Object=MibTableColumn
xstInstancePortDesignatedPort=_XstInstancePortDesignatedPort_Object((1,3,6,1,4,1,259,10,1,18,1,5,6,5,1,10),_XstInstancePortDesignatedPort_Type())
xstInstancePortDesignatedPort.setMaxAccess(_B)
if mibBuilder.loadTexts:xstInstancePortDesignatedPort.setStatus(_A)
_XstInstancePortForwardTransitions_Type=Counter32
_XstInstancePortForwardTransitions_Object=MibTableColumn
xstInstancePortForwardTransitions=_XstInstancePortForwardTransitions_Object((1,3,6,1,4,1,259,10,1,18,1,5,6,5,1,11),_XstInstancePortForwardTransitions_Type())
xstInstancePortForwardTransitions.setMaxAccess(_B)
if mibBuilder.loadTexts:xstInstancePortForwardTransitions.setStatus(_A)
class _XstInstancePortPortRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_J,1),('root',2),('designated',3),('alternate',4),('backup',5),(_Q,6)))
_XstInstancePortPortRole_Type.__name__=_C
_XstInstancePortPortRole_Object=MibTableColumn
xstInstancePortPortRole=_XstInstancePortPortRole_Object((1,3,6,1,4,1,259,10,1,18,1,5,6,5,1,12),_XstInstancePortPortRole_Type())
xstInstancePortPortRole.setMaxAccess(_B)
if mibBuilder.loadTexts:xstInstancePortPortRole.setStatus(_A)
_MstInstanceEditTable_Object=MibTable
mstInstanceEditTable=_MstInstanceEditTable_Object((1,3,6,1,4,1,259,10,1,18,1,5,6,6))
if mibBuilder.loadTexts:mstInstanceEditTable.setStatus(_A)
_MstInstanceEditEntry_Object=MibTableRow
mstInstanceEditEntry=_MstInstanceEditEntry_Object((1,3,6,1,4,1,259,10,1,18,1,5,6,6,1))
mstInstanceEditEntry.setIndexNames((0,_F,_h))
if mibBuilder.loadTexts:mstInstanceEditEntry.setStatus(_A)
class _MstInstanceEditIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_MstInstanceEditIndex_Type.__name__=_C
_MstInstanceEditIndex_Object=MibTableColumn
mstInstanceEditIndex=_MstInstanceEditIndex_Object((1,3,6,1,4,1,259,10,1,18,1,5,6,6,1,1),_MstInstanceEditIndex_Type())
mstInstanceEditIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:mstInstanceEditIndex.setStatus(_A)
class _MstInstanceEditVlansMap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_MstInstanceEditVlansMap_Type.__name__=_H
_MstInstanceEditVlansMap_Object=MibTableColumn
mstInstanceEditVlansMap=_MstInstanceEditVlansMap_Object((1,3,6,1,4,1,259,10,1,18,1,5,6,6,1,2),_MstInstanceEditVlansMap_Type())
mstInstanceEditVlansMap.setMaxAccess(_I)
if mibBuilder.loadTexts:mstInstanceEditVlansMap.setStatus(_A)
class _MstInstanceEditVlansMap2k_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_MstInstanceEditVlansMap2k_Type.__name__=_H
_MstInstanceEditVlansMap2k_Object=MibTableColumn
mstInstanceEditVlansMap2k=_MstInstanceEditVlansMap2k_Object((1,3,6,1,4,1,259,10,1,18,1,5,6,6,1,3),_MstInstanceEditVlansMap2k_Type())
mstInstanceEditVlansMap2k.setMaxAccess(_I)
if mibBuilder.loadTexts:mstInstanceEditVlansMap2k.setStatus(_A)
class _MstInstanceEditVlansMap3k_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_MstInstanceEditVlansMap3k_Type.__name__=_H
_MstInstanceEditVlansMap3k_Object=MibTableColumn
mstInstanceEditVlansMap3k=_MstInstanceEditVlansMap3k_Object((1,3,6,1,4,1,259,10,1,18,1,5,6,6,1,4),_MstInstanceEditVlansMap3k_Type())
mstInstanceEditVlansMap3k.setMaxAccess(_I)
if mibBuilder.loadTexts:mstInstanceEditVlansMap3k.setStatus(_A)
class _MstInstanceEditVlansMap4k_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_MstInstanceEditVlansMap4k_Type.__name__=_H
_MstInstanceEditVlansMap4k_Object=MibTableColumn
mstInstanceEditVlansMap4k=_MstInstanceEditVlansMap4k_Object((1,3,6,1,4,1,259,10,1,18,1,5,6,6,1,5),_MstInstanceEditVlansMap4k_Type())
mstInstanceEditVlansMap4k.setMaxAccess(_I)
if mibBuilder.loadTexts:mstInstanceEditVlansMap4k.setStatus(_A)
_MstInstanceEditRemainingHops_Type=Integer32
_MstInstanceEditRemainingHops_Object=MibTableColumn
mstInstanceEditRemainingHops=_MstInstanceEditRemainingHops_Object((1,3,6,1,4,1,259,10,1,18,1,5,6,6,1,6),_MstInstanceEditRemainingHops_Type())
mstInstanceEditRemainingHops.setMaxAccess(_B)
if mibBuilder.loadTexts:mstInstanceEditRemainingHops.setStatus(_A)
_MstInstanceOperTable_Object=MibTable
mstInstanceOperTable=_MstInstanceOperTable_Object((1,3,6,1,4,1,259,10,1,18,1,5,6,7))
if mibBuilder.loadTexts:mstInstanceOperTable.setStatus(_A)
_MstInstanceOperEntry_Object=MibTableRow
mstInstanceOperEntry=_MstInstanceOperEntry_Object((1,3,6,1,4,1,259,10,1,18,1,5,6,7,1))
mstInstanceOperEntry.setIndexNames((0,_F,_i))
if mibBuilder.loadTexts:mstInstanceOperEntry.setStatus(_A)
class _MstInstanceOperIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_MstInstanceOperIndex_Type.__name__=_C
_MstInstanceOperIndex_Object=MibTableColumn
mstInstanceOperIndex=_MstInstanceOperIndex_Object((1,3,6,1,4,1,259,10,1,18,1,5,6,7,1,1),_MstInstanceOperIndex_Type())
mstInstanceOperIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:mstInstanceOperIndex.setStatus(_A)
class _MstInstanceOperVlansMap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_MstInstanceOperVlansMap_Type.__name__=_H
_MstInstanceOperVlansMap_Object=MibTableColumn
mstInstanceOperVlansMap=_MstInstanceOperVlansMap_Object((1,3,6,1,4,1,259,10,1,18,1,5,6,7,1,2),_MstInstanceOperVlansMap_Type())
mstInstanceOperVlansMap.setMaxAccess(_B)
if mibBuilder.loadTexts:mstInstanceOperVlansMap.setStatus(_A)
class _MstInstanceOperVlansMap2k_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_MstInstanceOperVlansMap2k_Type.__name__=_H
_MstInstanceOperVlansMap2k_Object=MibTableColumn
mstInstanceOperVlansMap2k=_MstInstanceOperVlansMap2k_Object((1,3,6,1,4,1,259,10,1,18,1,5,6,7,1,3),_MstInstanceOperVlansMap2k_Type())
mstInstanceOperVlansMap2k.setMaxAccess(_B)
if mibBuilder.loadTexts:mstInstanceOperVlansMap2k.setStatus(_A)
class _MstInstanceOperVlansMap3k_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_MstInstanceOperVlansMap3k_Type.__name__=_H
_MstInstanceOperVlansMap3k_Object=MibTableColumn
mstInstanceOperVlansMap3k=_MstInstanceOperVlansMap3k_Object((1,3,6,1,4,1,259,10,1,18,1,5,6,7,1,4),_MstInstanceOperVlansMap3k_Type())
mstInstanceOperVlansMap3k.setMaxAccess(_B)
if mibBuilder.loadTexts:mstInstanceOperVlansMap3k.setStatus(_A)
class _MstInstanceOperVlansMap4k_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_MstInstanceOperVlansMap4k_Type.__name__=_H
_MstInstanceOperVlansMap4k_Object=MibTableColumn
mstInstanceOperVlansMap4k=_MstInstanceOperVlansMap4k_Object((1,3,6,1,4,1,259,10,1,18,1,5,6,7,1,5),_MstInstanceOperVlansMap4k_Type())
mstInstanceOperVlansMap4k.setMaxAccess(_B)
if mibBuilder.loadTexts:mstInstanceOperVlansMap4k.setStatus(_A)
_TftpMgt_ObjectIdentity=ObjectIdentity
tftpMgt=_TftpMgt_ObjectIdentity((1,3,6,1,4,1,259,10,1,18,1,6))
class _TftpFileType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_j,1),(_k,2)))
_TftpFileType_Type.__name__=_C
_TftpFileType_Object=MibScalar
tftpFileType=_TftpFileType_Object((1,3,6,1,4,1,259,10,1,18,1,6,1),_TftpFileType_Type())
tftpFileType.setMaxAccess(_D)
if mibBuilder.loadTexts:tftpFileType.setStatus(_A)
class _TftpSrcFile_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_TftpSrcFile_Type.__name__=_E
_TftpSrcFile_Object=MibScalar
tftpSrcFile=_TftpSrcFile_Object((1,3,6,1,4,1,259,10,1,18,1,6,2),_TftpSrcFile_Type())
tftpSrcFile.setMaxAccess(_D)
if mibBuilder.loadTexts:tftpSrcFile.setStatus(_A)
class _TftpDestFile_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_TftpDestFile_Type.__name__=_E
_TftpDestFile_Object=MibScalar
tftpDestFile=_TftpDestFile_Object((1,3,6,1,4,1,259,10,1,18,1,6,3),_TftpDestFile_Type())
tftpDestFile.setMaxAccess(_D)
if mibBuilder.loadTexts:tftpDestFile.setStatus(_A)
_TftpServer_Type=IpAddress
_TftpServer_Object=MibScalar
tftpServer=_TftpServer_Object((1,3,6,1,4,1,259,10,1,18,1,6,4),_TftpServer_Type())
tftpServer.setMaxAccess(_D)
if mibBuilder.loadTexts:tftpServer.setStatus(_A)
class _TftpAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('notDownloading',1),('downloadToPROM',2),('downloadToRAM',3),('upload',4)))
_TftpAction_Type.__name__=_C
_TftpAction_Object=MibScalar
tftpAction=_TftpAction_Object((1,3,6,1,4,1,259,10,1,18,1,6,5),_TftpAction_Type())
tftpAction.setMaxAccess(_D)
if mibBuilder.loadTexts:tftpAction.setStatus(_A)
class _TftpStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('tftpSuccess',1),('tftpStatusUnknown',2),('tftpGeneralError',3),('tftpNoResponseFromServer',4),('tftpDownloadChecksumError',5),('tftpDownloadIncompatibleImage',6),('tftpTftpFileNotFound',7),('tftpTftpAccessViolation',8)))
_TftpStatus_Type.__name__=_C
_TftpStatus_Object=MibScalar
tftpStatus=_TftpStatus_Object((1,3,6,1,4,1,259,10,1,18,1,6,6),_TftpStatus_Type())
tftpStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tftpStatus.setStatus(_A)
_RestartMgt_ObjectIdentity=ObjectIdentity
restartMgt=_RestartMgt_ObjectIdentity((1,3,6,1,4,1,259,10,1,18,1,7))
class _RestartControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('running',1),('warmBoot',2),('coldBoot',3)))
_RestartControl_Type.__name__=_C
_RestartControl_Object=MibScalar
restartControl=_RestartControl_Object((1,3,6,1,4,1,259,10,1,18,1,7,3),_RestartControl_Type())
restartControl.setMaxAccess(_D)
if mibBuilder.loadTexts:restartControl.setStatus(_A)
_VlanMgt_ObjectIdentity=ObjectIdentity
vlanMgt=_VlanMgt_ObjectIdentity((1,3,6,1,4,1,259,10,1,18,1,12))
_VlanTable_Object=MibTable
vlanTable=_VlanTable_Object((1,3,6,1,4,1,259,10,1,18,1,12,1))
if mibBuilder.loadTexts:vlanTable.setStatus(_A)
_VlanEntry_Object=MibTableRow
vlanEntry=_VlanEntry_Object((1,3,6,1,4,1,259,10,1,18,1,12,1,1))
vlanEntry.setIndexNames((0,_F,_l))
if mibBuilder.loadTexts:vlanEntry.setStatus(_A)
_VlanIndex_Type=Unsigned32
_VlanIndex_Object=MibTableColumn
vlanIndex=_VlanIndex_Object((1,3,6,1,4,1,259,10,1,18,1,12,1,1,1),_VlanIndex_Type())
vlanIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:vlanIndex.setStatus(_A)
class _VlanAddressMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('user',1),('dhcp',2)))
_VlanAddressMethod_Type.__name__=_C
_VlanAddressMethod_Object=MibTableColumn
vlanAddressMethod=_VlanAddressMethod_Object((1,3,6,1,4,1,259,10,1,18,1,12,1,1,2),_VlanAddressMethod_Type())
vlanAddressMethod.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanAddressMethod.setStatus(_A)
_VlanPortTable_Object=MibTable
vlanPortTable=_VlanPortTable_Object((1,3,6,1,4,1,259,10,1,18,1,12,2))
if mibBuilder.loadTexts:vlanPortTable.setStatus(_A)
_VlanPortEntry_Object=MibTableRow
vlanPortEntry=_VlanPortEntry_Object((1,3,6,1,4,1,259,10,1,18,1,12,2,1))
vlanPortEntry.setIndexNames((0,_F,_m))
if mibBuilder.loadTexts:vlanPortEntry.setStatus(_A)
class _VlanPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,44))
_VlanPortIndex_Type.__name__=_C
_VlanPortIndex_Object=MibTableColumn
vlanPortIndex=_VlanPortIndex_Object((1,3,6,1,4,1,259,10,1,18,1,12,2,1,1),_VlanPortIndex_Type())
vlanPortIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:vlanPortIndex.setStatus(_A)
class _VlanPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('hybrid',1),('dot1qTrunk',2),('access',3),('vlanUnaware',4)))
_VlanPortMode_Type.__name__=_C
_VlanPortMode_Object=MibTableColumn
vlanPortMode=_VlanPortMode_Object((1,3,6,1,4,1,259,10,1,18,1,12,2,1,2),_VlanPortMode_Type())
vlanPortMode.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanPortMode.setStatus(_A)
class _VlanPortPrivateVlanType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('non-isolated',1),('isolated',2)))
_VlanPortPrivateVlanType_Type.__name__=_C
_VlanPortPrivateVlanType_Object=MibTableColumn
vlanPortPrivateVlanType=_VlanPortPrivateVlanType_Object((1,3,6,1,4,1,259,10,1,18,1,12,2,1,3),_VlanPortPrivateVlanType_Type())
vlanPortPrivateVlanType.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanPortPrivateVlanType.setStatus(_A)
_SysTimeMgt_ObjectIdentity=ObjectIdentity
sysTimeMgt=_SysTimeMgt_ObjectIdentity((1,3,6,1,4,1,259,10,1,18,1,23))
_SntpMgt_ObjectIdentity=ObjectIdentity
sntpMgt=_SntpMgt_ObjectIdentity((1,3,6,1,4,1,259,10,1,18,1,23,1))
_SntpStatus_Type=EnabledStatus
_SntpStatus_Object=MibScalar
sntpStatus=_SntpStatus_Object((1,3,6,1,4,1,259,10,1,18,1,23,1,1),_SntpStatus_Type())
sntpStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:sntpStatus.setStatus(_A)
class _SntpServiceMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_n,1))
_SntpServiceMode_Type.__name__=_C
_SntpServiceMode_Object=MibScalar
sntpServiceMode=_SntpServiceMode_Object((1,3,6,1,4,1,259,10,1,18,1,23,1,2),_SntpServiceMode_Type())
sntpServiceMode.setMaxAccess(_D)
if mibBuilder.loadTexts:sntpServiceMode.setStatus(_A)
class _SntpPollInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,16384))
_SntpPollInterval_Type.__name__=_C
_SntpPollInterval_Object=MibScalar
sntpPollInterval=_SntpPollInterval_Object((1,3,6,1,4,1,259,10,1,18,1,23,1,3),_SntpPollInterval_Type())
sntpPollInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:sntpPollInterval.setStatus(_A)
_SntpServerTable_Object=MibTable
sntpServerTable=_SntpServerTable_Object((1,3,6,1,4,1,259,10,1,18,1,23,1,4))
if mibBuilder.loadTexts:sntpServerTable.setStatus(_A)
_SntpServerEntry_Object=MibTableRow
sntpServerEntry=_SntpServerEntry_Object((1,3,6,1,4,1,259,10,1,18,1,23,1,4,1))
sntpServerEntry.setIndexNames((0,_F,_o))
if mibBuilder.loadTexts:sntpServerEntry.setStatus(_A)
class _SntpServerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_SntpServerIndex_Type.__name__=_C
_SntpServerIndex_Object=MibTableColumn
sntpServerIndex=_SntpServerIndex_Object((1,3,6,1,4,1,259,10,1,18,1,23,1,4,1,1),_SntpServerIndex_Type())
sntpServerIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:sntpServerIndex.setStatus(_A)
_SntpServerIpAddress_Type=IpAddress
_SntpServerIpAddress_Object=MibTableColumn
sntpServerIpAddress=_SntpServerIpAddress_Object((1,3,6,1,4,1,259,10,1,18,1,23,1,4,1,2),_SntpServerIpAddress_Type())
sntpServerIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:sntpServerIpAddress.setStatus(_A)
class _SysCurrentTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(20,20));fixedLength=20
_SysCurrentTime_Type.__name__=_E
_SysCurrentTime_Object=MibScalar
sysCurrentTime=_SysCurrentTime_Object((1,3,6,1,4,1,259,10,1,18,1,23,2),_SysCurrentTime_Type())
sysCurrentTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sysCurrentTime.setStatus(_A)
class _SysTimeZone_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_SysTimeZone_Type.__name__=_E
_SysTimeZone_Object=MibScalar
sysTimeZone=_SysTimeZone_Object((1,3,6,1,4,1,259,10,1,18,1,23,3),_SysTimeZone_Type())
sysTimeZone.setMaxAccess(_D)
if mibBuilder.loadTexts:sysTimeZone.setStatus(_A)
_NtpMgt_ObjectIdentity=ObjectIdentity
ntpMgt=_NtpMgt_ObjectIdentity((1,3,6,1,4,1,259,10,1,18,1,23,5))
_NtpStatus_Type=EnabledStatus
_NtpStatus_Object=MibScalar
ntpStatus=_NtpStatus_Object((1,3,6,1,4,1,259,10,1,18,1,23,5,1),_NtpStatus_Type())
ntpStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ntpStatus.setStatus(_A)
class _NtpServiceMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_n,1))
_NtpServiceMode_Type.__name__=_C
_NtpServiceMode_Object=MibScalar
ntpServiceMode=_NtpServiceMode_Object((1,3,6,1,4,1,259,10,1,18,1,23,5,2),_NtpServiceMode_Type())
ntpServiceMode.setMaxAccess(_D)
if mibBuilder.loadTexts:ntpServiceMode.setStatus(_A)
class _NtpPollInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,16384))
_NtpPollInterval_Type.__name__=_C
_NtpPollInterval_Object=MibScalar
ntpPollInterval=_NtpPollInterval_Object((1,3,6,1,4,1,259,10,1,18,1,23,5,3),_NtpPollInterval_Type())
ntpPollInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:ntpPollInterval.setStatus(_A)
_NtpAuthenticateStatus_Type=EnabledStatus
_NtpAuthenticateStatus_Object=MibScalar
ntpAuthenticateStatus=_NtpAuthenticateStatus_Object((1,3,6,1,4,1,259,10,1,18,1,23,5,4),_NtpAuthenticateStatus_Type())
ntpAuthenticateStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ntpAuthenticateStatus.setStatus(_A)
_NtpServerTable_Object=MibTable
ntpServerTable=_NtpServerTable_Object((1,3,6,1,4,1,259,10,1,18,1,23,5,5))
if mibBuilder.loadTexts:ntpServerTable.setStatus(_A)
_NtpServerEntry_Object=MibTableRow
ntpServerEntry=_NtpServerEntry_Object((1,3,6,1,4,1,259,10,1,18,1,23,5,5,1))
ntpServerEntry.setIndexNames((0,_F,_p))
if mibBuilder.loadTexts:ntpServerEntry.setStatus(_A)
_NtpServerIpAddress_Type=IpAddress
_NtpServerIpAddress_Object=MibTableColumn
ntpServerIpAddress=_NtpServerIpAddress_Object((1,3,6,1,4,1,259,10,1,18,1,23,5,5,1,1),_NtpServerIpAddress_Type())
ntpServerIpAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:ntpServerIpAddress.setStatus(_A)
class _NtpServerVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_NtpServerVersion_Type.__name__=_C
_NtpServerVersion_Object=MibTableColumn
ntpServerVersion=_NtpServerVersion_Object((1,3,6,1,4,1,259,10,1,18,1,23,5,5,1,2),_NtpServerVersion_Type())
ntpServerVersion.setMaxAccess(_I)
if mibBuilder.loadTexts:ntpServerVersion.setStatus(_A)
class _NtpServerKeyId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_NtpServerKeyId_Type.__name__=_C
_NtpServerKeyId_Object=MibTableColumn
ntpServerKeyId=_NtpServerKeyId_Object((1,3,6,1,4,1,259,10,1,18,1,23,5,5,1,3),_NtpServerKeyId_Type())
ntpServerKeyId.setMaxAccess(_D)
if mibBuilder.loadTexts:ntpServerKeyId.setStatus(_A)
class _NtpServerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_q,1),(_r,2),(_s,3)))
_NtpServerStatus_Type.__name__=_C
_NtpServerStatus_Object=MibTableColumn
ntpServerStatus=_NtpServerStatus_Object((1,3,6,1,4,1,259,10,1,18,1,23,5,5,1,4),_NtpServerStatus_Type())
ntpServerStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:ntpServerStatus.setStatus(_A)
_NtpAuthKeyTable_Object=MibTable
ntpAuthKeyTable=_NtpAuthKeyTable_Object((1,3,6,1,4,1,259,10,1,18,1,23,5,6))
if mibBuilder.loadTexts:ntpAuthKeyTable.setStatus(_A)
_NtpAuthKeyEntry_Object=MibTableRow
ntpAuthKeyEntry=_NtpAuthKeyEntry_Object((1,3,6,1,4,1,259,10,1,18,1,23,5,6,1))
ntpAuthKeyEntry.setIndexNames((0,_F,_t))
if mibBuilder.loadTexts:ntpAuthKeyEntry.setStatus(_A)
class _NtpAuthKeyId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65536))
_NtpAuthKeyId_Type.__name__=_C
_NtpAuthKeyId_Object=MibTableColumn
ntpAuthKeyId=_NtpAuthKeyId_Object((1,3,6,1,4,1,259,10,1,18,1,23,5,6,1,1),_NtpAuthKeyId_Type())
ntpAuthKeyId.setMaxAccess(_G)
if mibBuilder.loadTexts:ntpAuthKeyId.setStatus(_A)
class _NtpAuthKeyWord_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_NtpAuthKeyWord_Type.__name__=_H
_NtpAuthKeyWord_Object=MibTableColumn
ntpAuthKeyWord=_NtpAuthKeyWord_Object((1,3,6,1,4,1,259,10,1,18,1,23,5,6,1,2),_NtpAuthKeyWord_Type())
ntpAuthKeyWord.setMaxAccess(_I)
if mibBuilder.loadTexts:ntpAuthKeyWord.setStatus(_A)
class _NtpAuthKeyStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_q,1),(_r,2),(_s,3)))
_NtpAuthKeyStatus_Type.__name__=_C
_NtpAuthKeyStatus_Object=MibTableColumn
ntpAuthKeyStatus=_NtpAuthKeyStatus_Object((1,3,6,1,4,1,259,10,1,18,1,23,5,6,1,3),_NtpAuthKeyStatus_Type())
ntpAuthKeyStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:ntpAuthKeyStatus.setStatus(_A)
_FileMgt_ObjectIdentity=ObjectIdentity
fileMgt=_FileMgt_ObjectIdentity((1,3,6,1,4,1,259,10,1,18,1,24))
_FileCopyMgt_ObjectIdentity=ObjectIdentity
fileCopyMgt=_FileCopyMgt_ObjectIdentity((1,3,6,1,4,1,259,10,1,18,1,24,1))
class _FileCopySrcOperType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_u,1),('tftp',2)))
_FileCopySrcOperType_Type.__name__=_C
_FileCopySrcOperType_Object=MibScalar
fileCopySrcOperType=_FileCopySrcOperType_Object((1,3,6,1,4,1,259,10,1,18,1,24,1,1),_FileCopySrcOperType_Type())
fileCopySrcOperType.setMaxAccess(_D)
if mibBuilder.loadTexts:fileCopySrcOperType.setStatus(_A)
class _FileCopySrcFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FileCopySrcFileName_Type.__name__=_E
_FileCopySrcFileName_Object=MibScalar
fileCopySrcFileName=_FileCopySrcFileName_Object((1,3,6,1,4,1,259,10,1,18,1,24,1,2),_FileCopySrcFileName_Type())
fileCopySrcFileName.setMaxAccess(_D)
if mibBuilder.loadTexts:fileCopySrcFileName.setStatus(_A)
class _FileCopyDestOperType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_u,1),('tftp',2)))
_FileCopyDestOperType_Type.__name__=_C
_FileCopyDestOperType_Object=MibScalar
fileCopyDestOperType=_FileCopyDestOperType_Object((1,3,6,1,4,1,259,10,1,18,1,24,1,3),_FileCopyDestOperType_Type())
fileCopyDestOperType.setMaxAccess(_D)
if mibBuilder.loadTexts:fileCopyDestOperType.setStatus(_A)
class _FileCopyDestFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FileCopyDestFileName_Type.__name__=_E
_FileCopyDestFileName_Object=MibScalar
fileCopyDestFileName=_FileCopyDestFileName_Object((1,3,6,1,4,1,259,10,1,18,1,24,1,4),_FileCopyDestFileName_Type())
fileCopyDestFileName.setMaxAccess(_D)
if mibBuilder.loadTexts:fileCopyDestFileName.setStatus(_A)
class _FileCopyFileType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_j,1),(_k,2)))
_FileCopyFileType_Type.__name__=_C
_FileCopyFileType_Object=MibScalar
fileCopyFileType=_FileCopyFileType_Object((1,3,6,1,4,1,259,10,1,18,1,24,1,5),_FileCopyFileType_Type())
fileCopyFileType.setMaxAccess(_D)
if mibBuilder.loadTexts:fileCopyFileType.setStatus(_A)
_FileCopyTftpServer_Type=IpAddress
_FileCopyTftpServer_Object=MibScalar
fileCopyTftpServer=_FileCopyTftpServer_Object((1,3,6,1,4,1,259,10,1,18,1,24,1,6),_FileCopyTftpServer_Type())
fileCopyTftpServer.setMaxAccess(_D)
if mibBuilder.loadTexts:fileCopyTftpServer.setStatus(_A)
class _FileCopyAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('notCopying',1),('copy',2)))
_FileCopyAction_Type.__name__=_C
_FileCopyAction_Object=MibScalar
fileCopyAction=_FileCopyAction_Object((1,3,6,1,4,1,259,10,1,18,1,24,1,8),_FileCopyAction_Type())
fileCopyAction.setMaxAccess(_D)
if mibBuilder.loadTexts:fileCopyAction.setStatus(_A)
class _FileCopyTftpErrMsg_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_FileCopyTftpErrMsg_Type.__name__=_E
_FileCopyTftpErrMsg_Object=MibScalar
fileCopyTftpErrMsg=_FileCopyTftpErrMsg_Object((1,3,6,1,4,1,259,10,1,18,1,24,1,10),_FileCopyTftpErrMsg_Type())
fileCopyTftpErrMsg.setMaxAccess(_B)
if mibBuilder.loadTexts:fileCopyTftpErrMsg.setStatus(_A)
_Ecs4810_28tsNotifications_ObjectIdentity=ObjectIdentity
ecs4810_28tsNotifications=_Ecs4810_28tsNotifications_ObjectIdentity((1,3,6,1,4,1,259,10,1,18,2))
_Ecs4810_28tsTraps_ObjectIdentity=ObjectIdentity
ecs4810_28tsTraps=_Ecs4810_28tsTraps_ObjectIdentity((1,3,6,1,4,1,259,10,1,18,2,1))
_Ecs4810_28tsTrapsPrefix_ObjectIdentity=ObjectIdentity
ecs4810_28tsTrapsPrefix=_Ecs4810_28tsTrapsPrefix_ObjectIdentity((1,3,6,1,4,1,259,10,1,18,2,1,0))
_Ecs4810_28tsConformance_ObjectIdentity=ObjectIdentity
ecs4810_28tsConformance=_Ecs4810_28tsConformance_ObjectIdentity((1,3,6,1,4,1,259,10,1,18,3))
swPortSecurityTrap=NotificationType((1,3,6,1,4,1,259,10,1,18,2,1,0,36))
swPortSecurityTrap.setObjects((_M,_N))
if mibBuilder.loadTexts:swPortSecurityTrap.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'KeySegment':KeySegment,'ValidStatus':ValidStatus,_d:StaPathCostMode,'accton':accton,'edgecorenetworks':edgecorenetworks,'edgeCoreNetworksMgt':edgeCoreNetworksMgt,'ecs4810-28tsMIB':ecs4810_28tsMIB,'ecs4810-28tsMIBObjects':ecs4810_28tsMIBObjects,'switchMgt':switchMgt,'switchManagementVlan':switchManagementVlan,'switchNumber':switchNumber,'switchInfoTable':switchInfoTable,'switchInfoEntry':switchInfoEntry,_P:swUnitIndex,'swHardwareVer':swHardwareVer,'swMicrocodeVer':swMicrocodeVer,'swLoaderVer':swLoaderVer,'swBootRomVer':swBootRomVer,'swOpCodeVer':swOpCodeVer,'swPortNumber':swPortNumber,'swPowerStatus':swPowerStatus,'swRoleInSystem':swRoleInSystem,'swSerialNumber':swSerialNumber,'swServiceTag':swServiceTag,'switchOperState':switchOperState,'switchProductId':switchProductId,'swProdName':swProdName,'swProdManufacturer':swProdManufacturer,'swProdDescription':swProdDescription,'swProdVersion':swProdVersion,'swProdUrl':swProdUrl,'swIdentifier':swIdentifier,'swChassisServiceTag':swChassisServiceTag,'amtrMgt':amtrMgt,'amtrMacAddrAgingStatus':amtrMacAddrAgingStatus,'portMgt':portMgt,'portTable':portTable,'portEntry':portEntry,_R:portIndex,'portName':portName,'portType':portType,'portSpeedDpxCfg':portSpeedDpxCfg,'portFlowCtrlCfg':portFlowCtrlCfg,'portCapabilities':portCapabilities,'portAutonegotiation':portAutonegotiation,'portSpeedDpxStatus':portSpeedDpxStatus,'portFlowCtrlStatus':portFlowCtrlStatus,'portTrunkIndex':portTrunkIndex,'trunkMgt':trunkMgt,'trunkMaxId':trunkMaxId,'trunkValidNumber':trunkValidNumber,'trunkTable':trunkTable,'trunkEntry':trunkEntry,_a:trunkIndex,'trunkPorts':trunkPorts,'trunkCreation':trunkCreation,'trunkStatus':trunkStatus,'lacpMgt':lacpMgt,'lacpPortTable':lacpPortTable,'lacpPortEntry':lacpPortEntry,_b:lacpPortIndex,'lacpPortStatus':lacpPortStatus,'staMgt':staMgt,'staSystemStatus':staSystemStatus,'staPortTable':staPortTable,'staPortEntry':staPortEntry,_c:staPortIndex,'staPortFastForward':staPortFastForward,'staPortProtocolMigration':staPortProtocolMigration,'staPortAdminEdgePort':staPortAdminEdgePort,'staPortOperEdgePort':staPortOperEdgePort,'staPortAdminPointToPoint':staPortAdminPointToPoint,'staPortOperPointToPoint':staPortOperPointToPoint,'staPortLongPathCost':staPortLongPathCost,'staPortSystemStatus':staPortSystemStatus,'staProtocolType':staProtocolType,'staTxHoldCount':staTxHoldCount,'staPathCostMethod':staPathCostMethod,'xstMgt':xstMgt,'mstName':mstName,'mstRevision':mstRevision,'mstMaxHops':mstMaxHops,'xstInstanceCfgTable':xstInstanceCfgTable,'xstInstanceCfgEntry':xstInstanceCfgEntry,_e:xstInstanceCfgIndex,'xstInstanceCfgPriority':xstInstanceCfgPriority,'xstInstanceCfgTimeSinceTopologyChange':xstInstanceCfgTimeSinceTopologyChange,'xstInstanceCfgTopChanges':xstInstanceCfgTopChanges,'xstInstanceCfgDesignatedRoot':xstInstanceCfgDesignatedRoot,'xstInstanceCfgRootCost':xstInstanceCfgRootCost,'xstInstanceCfgRootPort':xstInstanceCfgRootPort,'xstInstanceCfgMaxAge':xstInstanceCfgMaxAge,'xstInstanceCfgHelloTime':xstInstanceCfgHelloTime,'xstInstanceCfgHoldTime':xstInstanceCfgHoldTime,'xstInstanceCfgForwardDelay':xstInstanceCfgForwardDelay,'xstInstanceCfgBridgeMaxAge':xstInstanceCfgBridgeMaxAge,'xstInstanceCfgBridgeHelloTime':xstInstanceCfgBridgeHelloTime,'xstInstanceCfgBridgeForwardDelay':xstInstanceCfgBridgeForwardDelay,'xstInstanceCfgTxHoldCount':xstInstanceCfgTxHoldCount,'xstInstanceCfgPathCostMethod':xstInstanceCfgPathCostMethod,'xstInstancePortTable':xstInstancePortTable,'xstInstancePortEntry':xstInstancePortEntry,_f:xstInstancePortInstance,_g:xstInstancePortPort,'xstInstancePortPriority':xstInstancePortPriority,'xstInstancePortState':xstInstancePortState,'xstInstancePortEnable':xstInstancePortEnable,'xstInstancePortPathCost':xstInstancePortPathCost,'xstInstancePortDesignatedRoot':xstInstancePortDesignatedRoot,'xstInstancePortDesignatedCost':xstInstancePortDesignatedCost,'xstInstancePortDesignatedBridge':xstInstancePortDesignatedBridge,'xstInstancePortDesignatedPort':xstInstancePortDesignatedPort,'xstInstancePortForwardTransitions':xstInstancePortForwardTransitions,'xstInstancePortPortRole':xstInstancePortPortRole,'mstInstanceEditTable':mstInstanceEditTable,'mstInstanceEditEntry':mstInstanceEditEntry,_h:mstInstanceEditIndex,'mstInstanceEditVlansMap':mstInstanceEditVlansMap,'mstInstanceEditVlansMap2k':mstInstanceEditVlansMap2k,'mstInstanceEditVlansMap3k':mstInstanceEditVlansMap3k,'mstInstanceEditVlansMap4k':mstInstanceEditVlansMap4k,'mstInstanceEditRemainingHops':mstInstanceEditRemainingHops,'mstInstanceOperTable':mstInstanceOperTable,'mstInstanceOperEntry':mstInstanceOperEntry,_i:mstInstanceOperIndex,'mstInstanceOperVlansMap':mstInstanceOperVlansMap,'mstInstanceOperVlansMap2k':mstInstanceOperVlansMap2k,'mstInstanceOperVlansMap3k':mstInstanceOperVlansMap3k,'mstInstanceOperVlansMap4k':mstInstanceOperVlansMap4k,'tftpMgt':tftpMgt,'tftpFileType':tftpFileType,'tftpSrcFile':tftpSrcFile,'tftpDestFile':tftpDestFile,'tftpServer':tftpServer,'tftpAction':tftpAction,'tftpStatus':tftpStatus,'restartMgt':restartMgt,'restartControl':restartControl,'vlanMgt':vlanMgt,'vlanTable':vlanTable,'vlanEntry':vlanEntry,_l:vlanIndex,'vlanAddressMethod':vlanAddressMethod,'vlanPortTable':vlanPortTable,'vlanPortEntry':vlanPortEntry,_m:vlanPortIndex,'vlanPortMode':vlanPortMode,'vlanPortPrivateVlanType':vlanPortPrivateVlanType,'sysTimeMgt':sysTimeMgt,'sntpMgt':sntpMgt,'sntpStatus':sntpStatus,'sntpServiceMode':sntpServiceMode,'sntpPollInterval':sntpPollInterval,'sntpServerTable':sntpServerTable,'sntpServerEntry':sntpServerEntry,_o:sntpServerIndex,'sntpServerIpAddress':sntpServerIpAddress,'sysCurrentTime':sysCurrentTime,'sysTimeZone':sysTimeZone,'ntpMgt':ntpMgt,'ntpStatus':ntpStatus,'ntpServiceMode':ntpServiceMode,'ntpPollInterval':ntpPollInterval,'ntpAuthenticateStatus':ntpAuthenticateStatus,'ntpServerTable':ntpServerTable,'ntpServerEntry':ntpServerEntry,_p:ntpServerIpAddress,'ntpServerVersion':ntpServerVersion,'ntpServerKeyId':ntpServerKeyId,'ntpServerStatus':ntpServerStatus,'ntpAuthKeyTable':ntpAuthKeyTable,'ntpAuthKeyEntry':ntpAuthKeyEntry,_t:ntpAuthKeyId,'ntpAuthKeyWord':ntpAuthKeyWord,'ntpAuthKeyStatus':ntpAuthKeyStatus,'fileMgt':fileMgt,'fileCopyMgt':fileCopyMgt,'fileCopySrcOperType':fileCopySrcOperType,'fileCopySrcFileName':fileCopySrcFileName,'fileCopyDestOperType':fileCopyDestOperType,'fileCopyDestFileName':fileCopyDestFileName,'fileCopyFileType':fileCopyFileType,'fileCopyTftpServer':fileCopyTftpServer,'fileCopyAction':fileCopyAction,'fileCopyTftpErrMsg':fileCopyTftpErrMsg,'ecs4810-28tsNotifications':ecs4810_28tsNotifications,'ecs4810-28tsTraps':ecs4810_28tsTraps,'ecs4810-28tsTrapsPrefix':ecs4810_28tsTrapsPrefix,'swPortSecurityTrap':swPortSecurityTrap,'ecs4810-28tsConformance':ecs4810_28tsConformance})