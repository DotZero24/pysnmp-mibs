_AK='swIndivPowerStatus'
_AJ='remoteLogServerIp'
_AI='sshConnID'
_AH='portSecPortIndex'
_AG='trapDestAddress'
_AF='prioWrrTrafficClass'
_AE='prioIpPortValue'
_AD='prioIpPortPhysPort'
_AC='prioIpDscpValue'
_AB='prioIpDscpPort'
_AA='prioIpPrecValue'
_A9='prioIpPrecPort'
_A8='vlanPortIndex'
_A7='vlanIndex'
_A6='bcastStormIfIndex'
_A5='netConfigSubnetMask'
_A4='netConfigIPAddress'
_A3='netConfigIfIndex'
_A2='igmpSnoopMulticastStaticIpAddress'
_A1='igmpSnoopMulticastStaticVlanIndex'
_A0='igmpSnoopMulticastCurrentIpAddress'
_z='igmpSnoopMulticastCurrentVlanIndex'
_y='igmpSnoopRouterStaticVlanIndex'
_x='igmpSnoopRouterCurrentVlanIndex'
_w='mirrorSourcePort'
_v='mirrorDestinationPort'
_u='xstInstancePortPort'
_t='xstInstancePortInstance'
_s='xstInstanceCfgIndex'
_r='staPortIndex'
_q='lacpPortIndex'
_p='trunkIndex'
_o='dot3xFlowControl'
_n='backPressure'
_m='fullDuplex1000'
_l='halfDuplex1000'
_k='fullDuplex100'
_j='halfDuplex100'
_i='fullDuplex10'
_h='halfDuplex10'
_g='portIndex'
_f='stackingModule'
_e='thousandBaseLxScSmf'
_d='thousandBaseXGbic'
_c='thousandBaseSxMtrjMmf'
_b='thousandBaseSxScMmf'
_a='hundredBaseFxMtrjMmf'
_Z='hundredBaseFxScSmf'
_Y='hundredBaseFxScMmf'
_X='master'
_W='swUnitIndex'
_V='EnabledStatus'
_U='ifIndex'
_T='IF-MIB'
_S='none'
_R='swIndivPowerIndex'
_Q='swIndivPowerUnitIndex'
_P='thousandBaseSfp'
_O='thousandBaseT'
_N='notPresent'
_M='OctetString'
_L='other'
_K='invalid'
_J='valid'
_I='enabled'
_H='disabled'
_G='read-create'
_F='DisplayString'
_E='PowerConnect3248-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_M,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
BridgeId,Timeout,dot1dStpPort,dot1dStpPortEntry=mibBuilder.importSymbols('BRIDGE-MIB','BridgeId','Timeout','dot1dStpPort','dot1dStpPortEntry')
ifIndex,=mibBuilder.importSymbols(_T,_U)
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB',_V)
PortList,=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,internet,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','internet','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','RowStatus','TextualConvention','TruthValue')
powerConnect3248MIB=ModuleIdentity((1,3,6,1,4,1,674,10895,3))
if mibBuilder.loadTexts:powerConnect3248MIB.setRevisions(('2001-09-06 00:00',))
class ValidStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_Private_ObjectIdentity=ObjectIdentity
private=_Private_ObjectIdentity((1,3,6,1,4))
_Enterprises_ObjectIdentity=ObjectIdentity
enterprises=_Enterprises_ObjectIdentity((1,3,6,1,4,1))
_Dell_ObjectIdentity=ObjectIdentity
dell=_Dell_ObjectIdentity((1,3,6,1,4,1,674))
_DellLan_ObjectIdentity=ObjectIdentity
dellLan=_DellLan_ObjectIdentity((1,3,6,1,4,1,674,10895))
_PowerConnect3248MIBObjects_ObjectIdentity=ObjectIdentity
powerConnect3248MIBObjects=_PowerConnect3248MIBObjects_ObjectIdentity((1,3,6,1,4,1,674,10895,3,1))
_SwitchMgt_ObjectIdentity=ObjectIdentity
switchMgt=_SwitchMgt_ObjectIdentity((1,3,6,1,4,1,674,10895,3,1,1))
class _SwitchManagementVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_SwitchManagementVlan_Type.__name__=_C
_SwitchManagementVlan_Object=MibScalar
switchManagementVlan=_SwitchManagementVlan_Object((1,3,6,1,4,1,674,10895,3,1,1,1),_SwitchManagementVlan_Type())
switchManagementVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:switchManagementVlan.setStatus(_A)
_SwitchNumber_Type=Integer32
_SwitchNumber_Object=MibScalar
switchNumber=_SwitchNumber_Object((1,3,6,1,4,1,674,10895,3,1,1,2),_SwitchNumber_Type())
switchNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:switchNumber.setStatus(_A)
_SwitchInfoTable_Object=MibTable
switchInfoTable=_SwitchInfoTable_Object((1,3,6,1,4,1,674,10895,3,1,1,3))
if mibBuilder.loadTexts:switchInfoTable.setStatus(_A)
_SwitchInfoEntry_Object=MibTableRow
switchInfoEntry=_SwitchInfoEntry_Object((1,3,6,1,4,1,674,10895,3,1,1,3,1))
switchInfoEntry.setIndexNames((0,_E,_W))
if mibBuilder.loadTexts:switchInfoEntry.setStatus(_A)
_SwUnitIndex_Type=Integer32
_SwUnitIndex_Object=MibTableColumn
swUnitIndex=_SwUnitIndex_Object((1,3,6,1,4,1,674,10895,3,1,1,3,1,1),_SwUnitIndex_Type())
swUnitIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:swUnitIndex.setStatus(_A)
class _SwHardwareVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_SwHardwareVer_Type.__name__=_F
_SwHardwareVer_Object=MibTableColumn
swHardwareVer=_SwHardwareVer_Object((1,3,6,1,4,1,674,10895,3,1,1,3,1,2),_SwHardwareVer_Type())
swHardwareVer.setMaxAccess(_B)
if mibBuilder.loadTexts:swHardwareVer.setStatus(_A)
class _SwMicrocodeVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_SwMicrocodeVer_Type.__name__=_F
_SwMicrocodeVer_Object=MibTableColumn
swMicrocodeVer=_SwMicrocodeVer_Object((1,3,6,1,4,1,674,10895,3,1,1,3,1,3),_SwMicrocodeVer_Type())
swMicrocodeVer.setMaxAccess(_B)
if mibBuilder.loadTexts:swMicrocodeVer.setStatus(_A)
class _SwLoaderVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_SwLoaderVer_Type.__name__=_F
_SwLoaderVer_Object=MibTableColumn
swLoaderVer=_SwLoaderVer_Object((1,3,6,1,4,1,674,10895,3,1,1,3,1,4),_SwLoaderVer_Type())
swLoaderVer.setMaxAccess(_B)
if mibBuilder.loadTexts:swLoaderVer.setStatus(_A)
class _SwBootRomVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_SwBootRomVer_Type.__name__=_F
_SwBootRomVer_Object=MibTableColumn
swBootRomVer=_SwBootRomVer_Object((1,3,6,1,4,1,674,10895,3,1,1,3,1,5),_SwBootRomVer_Type())
swBootRomVer.setMaxAccess(_B)
if mibBuilder.loadTexts:swBootRomVer.setStatus(_A)
class _SwOpCodeVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_SwOpCodeVer_Type.__name__=_F
_SwOpCodeVer_Object=MibTableColumn
swOpCodeVer=_SwOpCodeVer_Object((1,3,6,1,4,1,674,10895,3,1,1,3,1,6),_SwOpCodeVer_Type())
swOpCodeVer.setMaxAccess(_B)
if mibBuilder.loadTexts:swOpCodeVer.setStatus(_A)
_SwPortNumber_Type=Integer32
_SwPortNumber_Object=MibTableColumn
swPortNumber=_SwPortNumber_Object((1,3,6,1,4,1,674,10895,3,1,1,3,1,7),_SwPortNumber_Type())
swPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:swPortNumber.setStatus(_A)
class _SwPowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('internalPower',1),('redundantPower',2),('internalAndRedundantPower',3)))
_SwPowerStatus_Type.__name__=_C
_SwPowerStatus_Object=MibTableColumn
swPowerStatus=_SwPowerStatus_Object((1,3,6,1,4,1,674,10895,3,1,1,3,1,8),_SwPowerStatus_Type())
swPowerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:swPowerStatus.setStatus(_A)
class _SwRoleInSystem_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_X,1),('backupMaster',2),('slave',3)))
_SwRoleInSystem_Type.__name__=_C
_SwRoleInSystem_Object=MibTableColumn
swRoleInSystem=_SwRoleInSystem_Object((1,3,6,1,4,1,674,10895,3,1,1,3,1,9),_SwRoleInSystem_Type())
swRoleInSystem.setMaxAccess(_B)
if mibBuilder.loadTexts:swRoleInSystem.setStatus(_A)
class _SwSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_SwSerialNumber_Type.__name__=_F
_SwSerialNumber_Object=MibTableColumn
swSerialNumber=_SwSerialNumber_Object((1,3,6,1,4,1,674,10895,3,1,1,3,1,10),_SwSerialNumber_Type())
swSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:swSerialNumber.setStatus(_A)
class _SwExpansionSlot1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*((_N,1),(_L,2),(_Y,3),(_Z,4),(_a,5),(_b,6),(_c,7),(_d,8),(_e,9),(_O,10),(_f,11),(_P,12)))
_SwExpansionSlot1_Type.__name__=_C
_SwExpansionSlot1_Object=MibTableColumn
swExpansionSlot1=_SwExpansionSlot1_Object((1,3,6,1,4,1,674,10895,3,1,1,3,1,11),_SwExpansionSlot1_Type())
swExpansionSlot1.setMaxAccess(_B)
if mibBuilder.loadTexts:swExpansionSlot1.setStatus(_A)
class _SwExpansionSlot2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*((_N,1),(_L,2),(_Y,3),(_Z,4),(_a,5),(_b,6),(_c,7),(_d,8),(_e,9),(_O,10),(_f,11),(_P,12)))
_SwExpansionSlot2_Type.__name__=_C
_SwExpansionSlot2_Object=MibTableColumn
swExpansionSlot2=_SwExpansionSlot2_Object((1,3,6,1,4,1,674,10895,3,1,1,3,1,12),_SwExpansionSlot2_Type())
swExpansionSlot2.setMaxAccess(_B)
if mibBuilder.loadTexts:swExpansionSlot2.setStatus(_A)
class _SwServiceTag_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_SwServiceTag_Type.__name__=_F
_SwServiceTag_Object=MibTableColumn
swServiceTag=_SwServiceTag_Object((1,3,6,1,4,1,674,10895,3,1,1,3,1,13),_SwServiceTag_Type())
swServiceTag.setMaxAccess(_B)
if mibBuilder.loadTexts:swServiceTag.setStatus(_A)
class _SwitchOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_L,1),('unknown',2),('ok',3),('noncritical',4),('critical',5),('nonrecoverable',6)))
_SwitchOperState_Type.__name__=_C
_SwitchOperState_Object=MibScalar
switchOperState=_SwitchOperState_Object((1,3,6,1,4,1,674,10895,3,1,1,4),_SwitchOperState_Type())
switchOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:switchOperState.setStatus(_A)
_SwitchProductId_ObjectIdentity=ObjectIdentity
switchProductId=_SwitchProductId_ObjectIdentity((1,3,6,1,4,1,674,10895,3,1,1,5))
class _SwProdName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_SwProdName_Type.__name__=_F
_SwProdName_Object=MibScalar
swProdName=_SwProdName_Object((1,3,6,1,4,1,674,10895,3,1,1,5,1),_SwProdName_Type())
swProdName.setMaxAccess(_B)
if mibBuilder.loadTexts:swProdName.setStatus(_A)
class _SwProdManufacturer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_SwProdManufacturer_Type.__name__=_F
_SwProdManufacturer_Object=MibScalar
swProdManufacturer=_SwProdManufacturer_Object((1,3,6,1,4,1,674,10895,3,1,1,5,2),_SwProdManufacturer_Type())
swProdManufacturer.setMaxAccess(_B)
if mibBuilder.loadTexts:swProdManufacturer.setStatus(_A)
class _SwProdDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_SwProdDescription_Type.__name__=_F
_SwProdDescription_Object=MibScalar
swProdDescription=_SwProdDescription_Object((1,3,6,1,4,1,674,10895,3,1,1,5,3),_SwProdDescription_Type())
swProdDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:swProdDescription.setStatus(_A)
class _SwProdVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_SwProdVersion_Type.__name__=_F
_SwProdVersion_Object=MibScalar
swProdVersion=_SwProdVersion_Object((1,3,6,1,4,1,674,10895,3,1,1,5,4),_SwProdVersion_Type())
swProdVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:swProdVersion.setStatus(_A)
class _SwProdUrl_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_SwProdUrl_Type.__name__=_F
_SwProdUrl_Object=MibScalar
swProdUrl=_SwProdUrl_Object((1,3,6,1,4,1,674,10895,3,1,1,5,5),_SwProdUrl_Type())
swProdUrl.setMaxAccess(_B)
if mibBuilder.loadTexts:swProdUrl.setStatus(_A)
_SwIdentifier_Type=Integer32
_SwIdentifier_Object=MibScalar
swIdentifier=_SwIdentifier_Object((1,3,6,1,4,1,674,10895,3,1,1,5,6),_SwIdentifier_Type())
swIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:swIdentifier.setStatus(_A)
class _SwChassisServiceTag_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_SwChassisServiceTag_Type.__name__=_F
_SwChassisServiceTag_Object=MibScalar
swChassisServiceTag=_SwChassisServiceTag_Object((1,3,6,1,4,1,674,10895,3,1,1,5,7),_SwChassisServiceTag_Type())
swChassisServiceTag.setMaxAccess(_B)
if mibBuilder.loadTexts:swChassisServiceTag.setStatus(_A)
_SwitchIndivPowerTable_Object=MibTable
switchIndivPowerTable=_SwitchIndivPowerTable_Object((1,3,6,1,4,1,674,10895,3,1,1,6))
if mibBuilder.loadTexts:switchIndivPowerTable.setStatus(_A)
_SwitchIndivPowerEntry_Object=MibTableRow
switchIndivPowerEntry=_SwitchIndivPowerEntry_Object((1,3,6,1,4,1,674,10895,3,1,1,6,1))
switchIndivPowerEntry.setIndexNames((0,_E,_Q),(0,_E,_R))
if mibBuilder.loadTexts:switchIndivPowerEntry.setStatus(_A)
_SwIndivPowerUnitIndex_Type=Integer32
_SwIndivPowerUnitIndex_Object=MibTableColumn
swIndivPowerUnitIndex=_SwIndivPowerUnitIndex_Object((1,3,6,1,4,1,674,10895,3,1,1,6,1,1),_SwIndivPowerUnitIndex_Type())
swIndivPowerUnitIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:swIndivPowerUnitIndex.setStatus(_A)
class _SwIndivPowerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_SwIndivPowerIndex_Type.__name__=_C
_SwIndivPowerIndex_Object=MibTableColumn
swIndivPowerIndex=_SwIndivPowerIndex_Object((1,3,6,1,4,1,674,10895,3,1,1,6,1,2),_SwIndivPowerIndex_Type())
swIndivPowerIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:swIndivPowerIndex.setStatus(_A)
class _SwIndivPowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),('green',2),('red',3)))
_SwIndivPowerStatus_Type.__name__=_C
_SwIndivPowerStatus_Object=MibTableColumn
swIndivPowerStatus=_SwIndivPowerStatus_Object((1,3,6,1,4,1,674,10895,3,1,1,6,1,3),_SwIndivPowerStatus_Type())
swIndivPowerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:swIndivPowerStatus.setStatus(_A)
_PortMgt_ObjectIdentity=ObjectIdentity
portMgt=_PortMgt_ObjectIdentity((1,3,6,1,4,1,674,10895,3,1,2))
_PortTable_Object=MibTable
portTable=_PortTable_Object((1,3,6,1,4,1,674,10895,3,1,2,1))
if mibBuilder.loadTexts:portTable.setStatus(_A)
_PortEntry_Object=MibTableRow
portEntry=_PortEntry_Object((1,3,6,1,4,1,674,10895,3,1,2,1,1))
portEntry.setIndexNames((0,_E,_g))
if mibBuilder.loadTexts:portEntry.setStatus(_A)
_PortIndex_Type=Integer32
_PortIndex_Object=MibTableColumn
portIndex=_PortIndex_Object((1,3,6,1,4,1,674,10895,3,1,2,1,1,1),_PortIndex_Type())
portIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:portIndex.setStatus(_A)
class _PortName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_PortName_Type.__name__=_F
_PortName_Object=MibTableColumn
portName=_PortName_Object((1,3,6,1,4,1,674,10895,3,1,2,1,1,2),_PortName_Type())
portName.setMaxAccess(_D)
if mibBuilder.loadTexts:portName.setStatus(_A)
class _PortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_L,1),('hundredBaseTX',2),('hundredBaseFX',3),('thousandBaseSX',4),('thousandBaseLX',5),(_O,6),('thousandBaseGBIC',7),(_P,8)))
_PortType_Type.__name__=_C
_PortType_Object=MibTableColumn
portType=_PortType_Object((1,3,6,1,4,1,674,10895,3,1,2,1,1,3),_PortType_Type())
portType.setMaxAccess(_B)
if mibBuilder.loadTexts:portType.setStatus(_A)
class _PortSpeedDpxCfg_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('reserved',1),(_h,2),(_i,3),(_j,4),(_k,5),(_l,6),(_m,7)))
_PortSpeedDpxCfg_Type.__name__=_C
_PortSpeedDpxCfg_Object=MibTableColumn
portSpeedDpxCfg=_PortSpeedDpxCfg_Object((1,3,6,1,4,1,674,10895,3,1,2,1,1,4),_PortSpeedDpxCfg_Type())
portSpeedDpxCfg.setMaxAccess(_D)
if mibBuilder.loadTexts:portSpeedDpxCfg.setStatus(_A)
class _PortFlowCtrlCfg_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_I,1),(_H,2),(_n,3),(_o,4)))
_PortFlowCtrlCfg_Type.__name__=_C
_PortFlowCtrlCfg_Object=MibTableColumn
portFlowCtrlCfg=_PortFlowCtrlCfg_Object((1,3,6,1,4,1,674,10895,3,1,2,1,1,5),_PortFlowCtrlCfg_Type())
portFlowCtrlCfg.setMaxAccess(_D)
if mibBuilder.loadTexts:portFlowCtrlCfg.setStatus(_A)
class _PortCapabilities_Type(Bits):namedValues=NamedValues(*(('portCap10half',0),('portCap10full',1),('portCap100half',2),('portCap100full',3),('portCap1000half',4),('portCap1000full',5),('reserved6',6),('reserved7',7),('reserved8',8),('reserved9',9),('reserved10',10),('reserved11',11),('reserved12',12),('reserved13',13),('portCapSym',14),('portCapFlowCtrl',15)))
_PortCapabilities_Type.__name__='Bits'
_PortCapabilities_Object=MibTableColumn
portCapabilities=_PortCapabilities_Object((1,3,6,1,4,1,674,10895,3,1,2,1,1,6),_PortCapabilities_Type())
portCapabilities.setMaxAccess(_D)
if mibBuilder.loadTexts:portCapabilities.setStatus(_A)
class _PortAutonegotiation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_H,2)))
_PortAutonegotiation_Type.__name__=_C
_PortAutonegotiation_Object=MibTableColumn
portAutonegotiation=_PortAutonegotiation_Object((1,3,6,1,4,1,674,10895,3,1,2,1,1,7),_PortAutonegotiation_Type())
portAutonegotiation.setMaxAccess(_D)
if mibBuilder.loadTexts:portAutonegotiation.setStatus(_A)
class _PortSpeedDpxStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('error',1),(_h,2),(_i,3),(_j,4),(_k,5),(_l,6),(_m,7)))
_PortSpeedDpxStatus_Type.__name__=_C
_PortSpeedDpxStatus_Object=MibTableColumn
portSpeedDpxStatus=_PortSpeedDpxStatus_Object((1,3,6,1,4,1,674,10895,3,1,2,1,1,8),_PortSpeedDpxStatus_Type())
portSpeedDpxStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:portSpeedDpxStatus.setStatus(_A)
class _PortFlowCtrlStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('error',1),(_n,2),(_o,3),(_S,4)))
_PortFlowCtrlStatus_Type.__name__=_C
_PortFlowCtrlStatus_Object=MibTableColumn
portFlowCtrlStatus=_PortFlowCtrlStatus_Object((1,3,6,1,4,1,674,10895,3,1,2,1,1,9),_PortFlowCtrlStatus_Type())
portFlowCtrlStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:portFlowCtrlStatus.setStatus(_A)
_PortTrunkIndex_Type=Integer32
_PortTrunkIndex_Object=MibTableColumn
portTrunkIndex=_PortTrunkIndex_Object((1,3,6,1,4,1,674,10895,3,1,2,1,1,10),_PortTrunkIndex_Type())
portTrunkIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:portTrunkIndex.setStatus(_A)
_TrunkMgt_ObjectIdentity=ObjectIdentity
trunkMgt=_TrunkMgt_ObjectIdentity((1,3,6,1,4,1,674,10895,3,1,3))
_TrunkMaxId_Type=Integer32
_TrunkMaxId_Object=MibScalar
trunkMaxId=_TrunkMaxId_Object((1,3,6,1,4,1,674,10895,3,1,3,1),_TrunkMaxId_Type())
trunkMaxId.setMaxAccess(_B)
if mibBuilder.loadTexts:trunkMaxId.setStatus(_A)
_TrunkValidNumber_Type=Integer32
_TrunkValidNumber_Object=MibScalar
trunkValidNumber=_TrunkValidNumber_Object((1,3,6,1,4,1,674,10895,3,1,3,2),_TrunkValidNumber_Type())
trunkValidNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:trunkValidNumber.setStatus(_A)
_TrunkTable_Object=MibTable
trunkTable=_TrunkTable_Object((1,3,6,1,4,1,674,10895,3,1,3,3))
if mibBuilder.loadTexts:trunkTable.setStatus(_A)
_TrunkEntry_Object=MibTableRow
trunkEntry=_TrunkEntry_Object((1,3,6,1,4,1,674,10895,3,1,3,3,1))
trunkEntry.setIndexNames((0,_E,_p))
if mibBuilder.loadTexts:trunkEntry.setStatus(_A)
_TrunkIndex_Type=Integer32
_TrunkIndex_Object=MibTableColumn
trunkIndex=_TrunkIndex_Object((1,3,6,1,4,1,674,10895,3,1,3,3,1,1),_TrunkIndex_Type())
trunkIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:trunkIndex.setStatus(_A)
_TrunkPorts_Type=PortList
_TrunkPorts_Object=MibTableColumn
trunkPorts=_TrunkPorts_Object((1,3,6,1,4,1,674,10895,3,1,3,3,1,2),_TrunkPorts_Type())
trunkPorts.setMaxAccess(_G)
if mibBuilder.loadTexts:trunkPorts.setStatus(_A)
class _TrunkCreation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('static',1),('lacp',2)))
_TrunkCreation_Type.__name__=_C
_TrunkCreation_Object=MibTableColumn
trunkCreation=_TrunkCreation_Object((1,3,6,1,4,1,674,10895,3,1,3,3,1,3),_TrunkCreation_Type())
trunkCreation.setMaxAccess(_B)
if mibBuilder.loadTexts:trunkCreation.setStatus(_A)
class _TrunkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_TrunkStatus_Type.__name__=_C
_TrunkStatus_Object=MibTableColumn
trunkStatus=_TrunkStatus_Object((1,3,6,1,4,1,674,10895,3,1,3,3,1,4),_TrunkStatus_Type())
trunkStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:trunkStatus.setStatus(_A)
_LacpMgt_ObjectIdentity=ObjectIdentity
lacpMgt=_LacpMgt_ObjectIdentity((1,3,6,1,4,1,674,10895,3,1,4))
_LacpPortTable_Object=MibTable
lacpPortTable=_LacpPortTable_Object((1,3,6,1,4,1,674,10895,3,1,4,1))
if mibBuilder.loadTexts:lacpPortTable.setStatus(_A)
_LacpPortEntry_Object=MibTableRow
lacpPortEntry=_LacpPortEntry_Object((1,3,6,1,4,1,674,10895,3,1,4,1,1))
lacpPortEntry.setIndexNames((0,_E,_q))
if mibBuilder.loadTexts:lacpPortEntry.setStatus(_A)
_LacpPortIndex_Type=Integer32
_LacpPortIndex_Object=MibTableColumn
lacpPortIndex=_LacpPortIndex_Object((1,3,6,1,4,1,674,10895,3,1,4,1,1,1),_LacpPortIndex_Type())
lacpPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:lacpPortIndex.setStatus(_A)
class _LacpPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_H,2)))
_LacpPortStatus_Type.__name__=_C
_LacpPortStatus_Object=MibTableColumn
lacpPortStatus=_LacpPortStatus_Object((1,3,6,1,4,1,674,10895,3,1,4,1,1,2),_LacpPortStatus_Type())
lacpPortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:lacpPortStatus.setStatus(_A)
_StaMgt_ObjectIdentity=ObjectIdentity
staMgt=_StaMgt_ObjectIdentity((1,3,6,1,4,1,674,10895,3,1,5))
class _StaSystemStatus_Type(EnabledStatus):defaultValue=1
_StaSystemStatus_Type.__name__=_V
_StaSystemStatus_Object=MibScalar
staSystemStatus=_StaSystemStatus_Object((1,3,6,1,4,1,674,10895,3,1,5,1),_StaSystemStatus_Type())
staSystemStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:staSystemStatus.setStatus(_A)
_StaPortTable_Object=MibTable
staPortTable=_StaPortTable_Object((1,3,6,1,4,1,674,10895,3,1,5,2))
if mibBuilder.loadTexts:staPortTable.setStatus(_A)
_StaPortEntry_Object=MibTableRow
staPortEntry=_StaPortEntry_Object((1,3,6,1,4,1,674,10895,3,1,5,2,1))
staPortEntry.setIndexNames((0,_E,_r))
if mibBuilder.loadTexts:staPortEntry.setStatus(_A)
_StaPortIndex_Type=Integer32
_StaPortIndex_Object=MibTableColumn
staPortIndex=_StaPortIndex_Object((1,3,6,1,4,1,674,10895,3,1,5,2,1,1),_StaPortIndex_Type())
staPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:staPortIndex.setStatus(_A)
_StaPortFastForward_Type=EnabledStatus
_StaPortFastForward_Object=MibTableColumn
staPortFastForward=_StaPortFastForward_Object((1,3,6,1,4,1,674,10895,3,1,5,2,1,2),_StaPortFastForward_Type())
staPortFastForward.setMaxAccess(_D)
if mibBuilder.loadTexts:staPortFastForward.setStatus(_A)
_StaPortProtocolMigration_Type=TruthValue
_StaPortProtocolMigration_Object=MibTableColumn
staPortProtocolMigration=_StaPortProtocolMigration_Object((1,3,6,1,4,1,674,10895,3,1,5,2,1,3),_StaPortProtocolMigration_Type())
staPortProtocolMigration.setMaxAccess(_D)
if mibBuilder.loadTexts:staPortProtocolMigration.setStatus(_A)
_StaPortAdminEdgePort_Type=TruthValue
_StaPortAdminEdgePort_Object=MibTableColumn
staPortAdminEdgePort=_StaPortAdminEdgePort_Object((1,3,6,1,4,1,674,10895,3,1,5,2,1,4),_StaPortAdminEdgePort_Type())
staPortAdminEdgePort.setMaxAccess(_D)
if mibBuilder.loadTexts:staPortAdminEdgePort.setStatus(_A)
_StaPortOperEdgePort_Type=TruthValue
_StaPortOperEdgePort_Object=MibTableColumn
staPortOperEdgePort=_StaPortOperEdgePort_Object((1,3,6,1,4,1,674,10895,3,1,5,2,1,5),_StaPortOperEdgePort_Type())
staPortOperEdgePort.setMaxAccess(_B)
if mibBuilder.loadTexts:staPortOperEdgePort.setStatus(_A)
class _StaPortAdminPointToPoint_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('forceTrue',0),('forceFalse',1),('auto',2)))
_StaPortAdminPointToPoint_Type.__name__=_C
_StaPortAdminPointToPoint_Object=MibTableColumn
staPortAdminPointToPoint=_StaPortAdminPointToPoint_Object((1,3,6,1,4,1,674,10895,3,1,5,2,1,6),_StaPortAdminPointToPoint_Type())
staPortAdminPointToPoint.setMaxAccess(_D)
if mibBuilder.loadTexts:staPortAdminPointToPoint.setStatus(_A)
_StaPortOperPointToPoint_Type=TruthValue
_StaPortOperPointToPoint_Object=MibTableColumn
staPortOperPointToPoint=_StaPortOperPointToPoint_Object((1,3,6,1,4,1,674,10895,3,1,5,2,1,7),_StaPortOperPointToPoint_Type())
staPortOperPointToPoint.setMaxAccess(_B)
if mibBuilder.loadTexts:staPortOperPointToPoint.setStatus(_A)
class _StaPortLongPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,200000000))
_StaPortLongPathCost_Type.__name__=_C
_StaPortLongPathCost_Object=MibTableColumn
staPortLongPathCost=_StaPortLongPathCost_Object((1,3,6,1,4,1,674,10895,3,1,5,2,1,8),_StaPortLongPathCost_Type())
staPortLongPathCost.setMaxAccess(_D)
if mibBuilder.loadTexts:staPortLongPathCost.setStatus(_A)
class _StaProtocolType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('stp',1),('rstp',2),('mstp',3)))
_StaProtocolType_Type.__name__=_C
_StaProtocolType_Object=MibScalar
staProtocolType=_StaProtocolType_Object((1,3,6,1,4,1,674,10895,3,1,5,3),_StaProtocolType_Type())
staProtocolType.setMaxAccess(_D)
if mibBuilder.loadTexts:staProtocolType.setStatus(_A)
class _StaTxHoldCount_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_StaTxHoldCount_Type.__name__=_C
_StaTxHoldCount_Object=MibScalar
staTxHoldCount=_StaTxHoldCount_Object((1,3,6,1,4,1,674,10895,3,1,5,4),_StaTxHoldCount_Type())
staTxHoldCount.setMaxAccess(_D)
if mibBuilder.loadTexts:staTxHoldCount.setStatus(_A)
class _StaPathCostMethod_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('short',1),('long',2)))
_StaPathCostMethod_Type.__name__=_C
_StaPathCostMethod_Object=MibScalar
staPathCostMethod=_StaPathCostMethod_Object((1,3,6,1,4,1,674,10895,3,1,5,5),_StaPathCostMethod_Type())
staPathCostMethod.setMaxAccess(_D)
if mibBuilder.loadTexts:staPathCostMethod.setStatus(_A)
_XstMgt_ObjectIdentity=ObjectIdentity
xstMgt=_XstMgt_ObjectIdentity((1,3,6,1,4,1,674,10895,3,1,5,6))
_XstInstanceCfgTable_Object=MibTable
xstInstanceCfgTable=_XstInstanceCfgTable_Object((1,3,6,1,4,1,674,10895,3,1,5,6,4))
if mibBuilder.loadTexts:xstInstanceCfgTable.setStatus(_A)
_XstInstanceCfgEntry_Object=MibTableRow
xstInstanceCfgEntry=_XstInstanceCfgEntry_Object((1,3,6,1,4,1,674,10895,3,1,5,6,4,1))
xstInstanceCfgEntry.setIndexNames((0,_E,_s))
if mibBuilder.loadTexts:xstInstanceCfgEntry.setStatus(_A)
class _XstInstanceCfgIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_XstInstanceCfgIndex_Type.__name__=_C
_XstInstanceCfgIndex_Object=MibTableColumn
xstInstanceCfgIndex=_XstInstanceCfgIndex_Object((1,3,6,1,4,1,674,10895,3,1,5,6,4,1,1),_XstInstanceCfgIndex_Type())
xstInstanceCfgIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:xstInstanceCfgIndex.setStatus(_A)
class _XstInstanceCfgPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,61440))
_XstInstanceCfgPriority_Type.__name__=_C
_XstInstanceCfgPriority_Object=MibTableColumn
xstInstanceCfgPriority=_XstInstanceCfgPriority_Object((1,3,6,1,4,1,674,10895,3,1,5,6,4,1,2),_XstInstanceCfgPriority_Type())
xstInstanceCfgPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:xstInstanceCfgPriority.setStatus(_A)
_XstInstanceCfgTimeSinceTopologyChange_Type=Integer32
_XstInstanceCfgTimeSinceTopologyChange_Object=MibTableColumn
xstInstanceCfgTimeSinceTopologyChange=_XstInstanceCfgTimeSinceTopologyChange_Object((1,3,6,1,4,1,674,10895,3,1,5,6,4,1,3),_XstInstanceCfgTimeSinceTopologyChange_Type())
xstInstanceCfgTimeSinceTopologyChange.setMaxAccess(_B)
if mibBuilder.loadTexts:xstInstanceCfgTimeSinceTopologyChange.setStatus(_A)
_XstInstanceCfgTopChanges_Type=Integer32
_XstInstanceCfgTopChanges_Object=MibTableColumn
xstInstanceCfgTopChanges=_XstInstanceCfgTopChanges_Object((1,3,6,1,4,1,674,10895,3,1,5,6,4,1,4),_XstInstanceCfgTopChanges_Type())
xstInstanceCfgTopChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:xstInstanceCfgTopChanges.setStatus(_A)
_XstInstanceCfgDesignatedRoot_Type=BridgeId
_XstInstanceCfgDesignatedRoot_Object=MibTableColumn
xstInstanceCfgDesignatedRoot=_XstInstanceCfgDesignatedRoot_Object((1,3,6,1,4,1,674,10895,3,1,5,6,4,1,5),_XstInstanceCfgDesignatedRoot_Type())
xstInstanceCfgDesignatedRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:xstInstanceCfgDesignatedRoot.setStatus(_A)
_XstInstanceCfgRootCost_Type=Integer32
_XstInstanceCfgRootCost_Object=MibTableColumn
xstInstanceCfgRootCost=_XstInstanceCfgRootCost_Object((1,3,6,1,4,1,674,10895,3,1,5,6,4,1,6),_XstInstanceCfgRootCost_Type())
xstInstanceCfgRootCost.setMaxAccess(_B)
if mibBuilder.loadTexts:xstInstanceCfgRootCost.setStatus(_A)
_XstInstanceCfgRootPort_Type=Integer32
_XstInstanceCfgRootPort_Object=MibTableColumn
xstInstanceCfgRootPort=_XstInstanceCfgRootPort_Object((1,3,6,1,4,1,674,10895,3,1,5,6,4,1,7),_XstInstanceCfgRootPort_Type())
xstInstanceCfgRootPort.setMaxAccess(_B)
if mibBuilder.loadTexts:xstInstanceCfgRootPort.setStatus(_A)
_XstInstanceCfgMaxAge_Type=Timeout
_XstInstanceCfgMaxAge_Object=MibTableColumn
xstInstanceCfgMaxAge=_XstInstanceCfgMaxAge_Object((1,3,6,1,4,1,674,10895,3,1,5,6,4,1,8),_XstInstanceCfgMaxAge_Type())
xstInstanceCfgMaxAge.setMaxAccess(_B)
if mibBuilder.loadTexts:xstInstanceCfgMaxAge.setStatus(_A)
_XstInstanceCfgHelloTime_Type=Timeout
_XstInstanceCfgHelloTime_Object=MibTableColumn
xstInstanceCfgHelloTime=_XstInstanceCfgHelloTime_Object((1,3,6,1,4,1,674,10895,3,1,5,6,4,1,9),_XstInstanceCfgHelloTime_Type())
xstInstanceCfgHelloTime.setMaxAccess(_B)
if mibBuilder.loadTexts:xstInstanceCfgHelloTime.setStatus(_A)
_XstInstanceCfgHoldTime_Type=Timeout
_XstInstanceCfgHoldTime_Object=MibTableColumn
xstInstanceCfgHoldTime=_XstInstanceCfgHoldTime_Object((1,3,6,1,4,1,674,10895,3,1,5,6,4,1,10),_XstInstanceCfgHoldTime_Type())
xstInstanceCfgHoldTime.setMaxAccess(_B)
if mibBuilder.loadTexts:xstInstanceCfgHoldTime.setStatus(_A)
_XstInstanceCfgForwardDelay_Type=Timeout
_XstInstanceCfgForwardDelay_Object=MibTableColumn
xstInstanceCfgForwardDelay=_XstInstanceCfgForwardDelay_Object((1,3,6,1,4,1,674,10895,3,1,5,6,4,1,11),_XstInstanceCfgForwardDelay_Type())
xstInstanceCfgForwardDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:xstInstanceCfgForwardDelay.setStatus(_A)
_XstInstanceCfgBridgeMaxAge_Type=Timeout
_XstInstanceCfgBridgeMaxAge_Object=MibTableColumn
xstInstanceCfgBridgeMaxAge=_XstInstanceCfgBridgeMaxAge_Object((1,3,6,1,4,1,674,10895,3,1,5,6,4,1,12),_XstInstanceCfgBridgeMaxAge_Type())
xstInstanceCfgBridgeMaxAge.setMaxAccess(_B)
if mibBuilder.loadTexts:xstInstanceCfgBridgeMaxAge.setStatus(_A)
_XstInstanceCfgBridgeHelloTime_Type=Timeout
_XstInstanceCfgBridgeHelloTime_Object=MibTableColumn
xstInstanceCfgBridgeHelloTime=_XstInstanceCfgBridgeHelloTime_Object((1,3,6,1,4,1,674,10895,3,1,5,6,4,1,13),_XstInstanceCfgBridgeHelloTime_Type())
xstInstanceCfgBridgeHelloTime.setMaxAccess(_B)
if mibBuilder.loadTexts:xstInstanceCfgBridgeHelloTime.setStatus(_A)
_XstInstanceCfgBridgeForwardDelay_Type=Timeout
_XstInstanceCfgBridgeForwardDelay_Object=MibTableColumn
xstInstanceCfgBridgeForwardDelay=_XstInstanceCfgBridgeForwardDelay_Object((1,3,6,1,4,1,674,10895,3,1,5,6,4,1,14),_XstInstanceCfgBridgeForwardDelay_Type())
xstInstanceCfgBridgeForwardDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:xstInstanceCfgBridgeForwardDelay.setStatus(_A)
_XstInstanceCfgTxHoldCount_Type=Integer32
_XstInstanceCfgTxHoldCount_Object=MibTableColumn
xstInstanceCfgTxHoldCount=_XstInstanceCfgTxHoldCount_Object((1,3,6,1,4,1,674,10895,3,1,5,6,4,1,15),_XstInstanceCfgTxHoldCount_Type())
xstInstanceCfgTxHoldCount.setMaxAccess(_B)
if mibBuilder.loadTexts:xstInstanceCfgTxHoldCount.setStatus(_A)
class _XstInstanceCfgPathCostMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('short',1),('long',2)))
_XstInstanceCfgPathCostMethod_Type.__name__=_C
_XstInstanceCfgPathCostMethod_Object=MibTableColumn
xstInstanceCfgPathCostMethod=_XstInstanceCfgPathCostMethod_Object((1,3,6,1,4,1,674,10895,3,1,5,6,4,1,16),_XstInstanceCfgPathCostMethod_Type())
xstInstanceCfgPathCostMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:xstInstanceCfgPathCostMethod.setStatus(_A)
_XstInstancePortTable_Object=MibTable
xstInstancePortTable=_XstInstancePortTable_Object((1,3,6,1,4,1,674,10895,3,1,5,6,5))
if mibBuilder.loadTexts:xstInstancePortTable.setStatus(_A)
_XstInstancePortEntry_Object=MibTableRow
xstInstancePortEntry=_XstInstancePortEntry_Object((1,3,6,1,4,1,674,10895,3,1,5,6,5,1))
xstInstancePortEntry.setIndexNames((0,_E,_t),(0,_E,_u))
if mibBuilder.loadTexts:xstInstancePortEntry.setStatus(_A)
_XstInstancePortInstance_Type=Integer32
_XstInstancePortInstance_Object=MibTableColumn
xstInstancePortInstance=_XstInstancePortInstance_Object((1,3,6,1,4,1,674,10895,3,1,5,6,5,1,1),_XstInstancePortInstance_Type())
xstInstancePortInstance.setMaxAccess(_B)
if mibBuilder.loadTexts:xstInstancePortInstance.setStatus(_A)
_XstInstancePortPort_Type=Integer32
_XstInstancePortPort_Object=MibTableColumn
xstInstancePortPort=_XstInstancePortPort_Object((1,3,6,1,4,1,674,10895,3,1,5,6,5,1,2),_XstInstancePortPort_Type())
xstInstancePortPort.setMaxAccess(_B)
if mibBuilder.loadTexts:xstInstancePortPort.setStatus(_A)
class _XstInstancePortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,240))
_XstInstancePortPriority_Type.__name__=_C
_XstInstancePortPriority_Object=MibTableColumn
xstInstancePortPriority=_XstInstancePortPriority_Object((1,3,6,1,4,1,674,10895,3,1,5,6,5,1,3),_XstInstancePortPriority_Type())
xstInstancePortPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:xstInstancePortPriority.setStatus(_A)
class _XstInstancePortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('discarding',1),('learning',2),('forwarding',3)))
_XstInstancePortState_Type.__name__=_C
_XstInstancePortState_Object=MibTableColumn
xstInstancePortState=_XstInstancePortState_Object((1,3,6,1,4,1,674,10895,3,1,5,6,5,1,4),_XstInstancePortState_Type())
xstInstancePortState.setMaxAccess(_B)
if mibBuilder.loadTexts:xstInstancePortState.setStatus(_A)
_XstInstancePortEnable_Type=EnabledStatus
_XstInstancePortEnable_Object=MibTableColumn
xstInstancePortEnable=_XstInstancePortEnable_Object((1,3,6,1,4,1,674,10895,3,1,5,6,5,1,5),_XstInstancePortEnable_Type())
xstInstancePortEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:xstInstancePortEnable.setStatus(_A)
class _XstInstancePortPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,200000000))
_XstInstancePortPathCost_Type.__name__=_C
_XstInstancePortPathCost_Object=MibTableColumn
xstInstancePortPathCost=_XstInstancePortPathCost_Object((1,3,6,1,4,1,674,10895,3,1,5,6,5,1,6),_XstInstancePortPathCost_Type())
xstInstancePortPathCost.setMaxAccess(_D)
if mibBuilder.loadTexts:xstInstancePortPathCost.setStatus(_A)
_XstInstancePortDesignatedRoot_Type=BridgeId
_XstInstancePortDesignatedRoot_Object=MibTableColumn
xstInstancePortDesignatedRoot=_XstInstancePortDesignatedRoot_Object((1,3,6,1,4,1,674,10895,3,1,5,6,5,1,7),_XstInstancePortDesignatedRoot_Type())
xstInstancePortDesignatedRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:xstInstancePortDesignatedRoot.setStatus(_A)
_XstInstancePortDesignatedCost_Type=Integer32
_XstInstancePortDesignatedCost_Object=MibTableColumn
xstInstancePortDesignatedCost=_XstInstancePortDesignatedCost_Object((1,3,6,1,4,1,674,10895,3,1,5,6,5,1,8),_XstInstancePortDesignatedCost_Type())
xstInstancePortDesignatedCost.setMaxAccess(_B)
if mibBuilder.loadTexts:xstInstancePortDesignatedCost.setStatus(_A)
_XstInstancePortDesignatedBridge_Type=BridgeId
_XstInstancePortDesignatedBridge_Object=MibTableColumn
xstInstancePortDesignatedBridge=_XstInstancePortDesignatedBridge_Object((1,3,6,1,4,1,674,10895,3,1,5,6,5,1,9),_XstInstancePortDesignatedBridge_Type())
xstInstancePortDesignatedBridge.setMaxAccess(_B)
if mibBuilder.loadTexts:xstInstancePortDesignatedBridge.setStatus(_A)
class _XstInstancePortDesignatedPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_XstInstancePortDesignatedPort_Type.__name__=_M
_XstInstancePortDesignatedPort_Object=MibTableColumn
xstInstancePortDesignatedPort=_XstInstancePortDesignatedPort_Object((1,3,6,1,4,1,674,10895,3,1,5,6,5,1,10),_XstInstancePortDesignatedPort_Type())
xstInstancePortDesignatedPort.setMaxAccess(_B)
if mibBuilder.loadTexts:xstInstancePortDesignatedPort.setStatus(_A)
_XstInstancePortForwardTransitions_Type=Counter32
_XstInstancePortForwardTransitions_Object=MibTableColumn
xstInstancePortForwardTransitions=_XstInstancePortForwardTransitions_Object((1,3,6,1,4,1,674,10895,3,1,5,6,5,1,11),_XstInstancePortForwardTransitions_Type())
xstInstancePortForwardTransitions.setMaxAccess(_B)
if mibBuilder.loadTexts:xstInstancePortForwardTransitions.setStatus(_A)
class _XstInstancePortPortRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_H,1),('root',2),('designated',3),('alternate',4),('backup',5),(_X,6)))
_XstInstancePortPortRole_Type.__name__=_C
_XstInstancePortPortRole_Object=MibTableColumn
xstInstancePortPortRole=_XstInstancePortPortRole_Object((1,3,6,1,4,1,674,10895,3,1,5,6,5,1,12),_XstInstancePortPortRole_Type())
xstInstancePortPortRole.setMaxAccess(_B)
if mibBuilder.loadTexts:xstInstancePortPortRole.setStatus(_A)
_TftpMgt_ObjectIdentity=ObjectIdentity
tftpMgt=_TftpMgt_ObjectIdentity((1,3,6,1,4,1,674,10895,3,1,6))
class _TftpFileType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('opcode',1),('config',2)))
_TftpFileType_Type.__name__=_C
_TftpFileType_Object=MibScalar
tftpFileType=_TftpFileType_Object((1,3,6,1,4,1,674,10895,3,1,6,1),_TftpFileType_Type())
tftpFileType.setMaxAccess(_D)
if mibBuilder.loadTexts:tftpFileType.setStatus(_A)
class _TftpSrcFile_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_TftpSrcFile_Type.__name__=_F
_TftpSrcFile_Object=MibScalar
tftpSrcFile=_TftpSrcFile_Object((1,3,6,1,4,1,674,10895,3,1,6,2),_TftpSrcFile_Type())
tftpSrcFile.setMaxAccess(_D)
if mibBuilder.loadTexts:tftpSrcFile.setStatus(_A)
class _TftpDestFile_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_TftpDestFile_Type.__name__=_F
_TftpDestFile_Object=MibScalar
tftpDestFile=_TftpDestFile_Object((1,3,6,1,4,1,674,10895,3,1,6,3),_TftpDestFile_Type())
tftpDestFile.setMaxAccess(_D)
if mibBuilder.loadTexts:tftpDestFile.setStatus(_A)
_TftpServer_Type=IpAddress
_TftpServer_Object=MibScalar
tftpServer=_TftpServer_Object((1,3,6,1,4,1,674,10895,3,1,6,4),_TftpServer_Type())
tftpServer.setMaxAccess(_D)
if mibBuilder.loadTexts:tftpServer.setStatus(_A)
class _TftpAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('notDownloading',1),('downloadToPROM',2),('downloadToRAM',3),('upload',4)))
_TftpAction_Type.__name__=_C
_TftpAction_Object=MibScalar
tftpAction=_TftpAction_Object((1,3,6,1,4,1,674,10895,3,1,6,5),_TftpAction_Type())
tftpAction.setMaxAccess(_D)
if mibBuilder.loadTexts:tftpAction.setStatus(_A)
class _TftpStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('tftpSuccess',1),('tftpStatusUnknown',2),('tftpGeneralError',3),('tftpNoResponseFromServer',4),('tftpDownloadChecksumError',5),('tftpDownloadIncompatibleImage',6),('tftpTftpFileNotFound',7),('tftpTftpAccessViolation',8)))
_TftpStatus_Type.__name__=_C
_TftpStatus_Object=MibScalar
tftpStatus=_TftpStatus_Object((1,3,6,1,4,1,674,10895,3,1,6,6),_TftpStatus_Type())
tftpStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tftpStatus.setStatus(_A)
_RestartMgt_ObjectIdentity=ObjectIdentity
restartMgt=_RestartMgt_ObjectIdentity((1,3,6,1,4,1,674,10895,3,1,7))
class _RestartOpCodeFile_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_RestartOpCodeFile_Type.__name__=_F
_RestartOpCodeFile_Object=MibScalar
restartOpCodeFile=_RestartOpCodeFile_Object((1,3,6,1,4,1,674,10895,3,1,7,1),_RestartOpCodeFile_Type())
restartOpCodeFile.setMaxAccess(_D)
if mibBuilder.loadTexts:restartOpCodeFile.setStatus(_A)
class _RestartConfigFile_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_RestartConfigFile_Type.__name__=_F
_RestartConfigFile_Object=MibScalar
restartConfigFile=_RestartConfigFile_Object((1,3,6,1,4,1,674,10895,3,1,7,2),_RestartConfigFile_Type())
restartConfigFile.setMaxAccess(_D)
if mibBuilder.loadTexts:restartConfigFile.setStatus(_A)
class _RestartControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('running',1),('warmBoot',2),('coldBoot',3)))
_RestartControl_Type.__name__=_C
_RestartControl_Object=MibScalar
restartControl=_RestartControl_Object((1,3,6,1,4,1,674,10895,3,1,7,3),_RestartControl_Type())
restartControl.setMaxAccess(_D)
if mibBuilder.loadTexts:restartControl.setStatus(_A)
_MirrorMgt_ObjectIdentity=ObjectIdentity
mirrorMgt=_MirrorMgt_ObjectIdentity((1,3,6,1,4,1,674,10895,3,1,8))
_MirrorTable_Object=MibTable
mirrorTable=_MirrorTable_Object((1,3,6,1,4,1,674,10895,3,1,8,1))
if mibBuilder.loadTexts:mirrorTable.setStatus(_A)
_MirrorEntry_Object=MibTableRow
mirrorEntry=_MirrorEntry_Object((1,3,6,1,4,1,674,10895,3,1,8,1,1))
mirrorEntry.setIndexNames((0,_E,_v),(0,_E,_w))
if mibBuilder.loadTexts:mirrorEntry.setStatus(_A)
_MirrorDestinationPort_Type=Integer32
_MirrorDestinationPort_Object=MibTableColumn
mirrorDestinationPort=_MirrorDestinationPort_Object((1,3,6,1,4,1,674,10895,3,1,8,1,1,1),_MirrorDestinationPort_Type())
mirrorDestinationPort.setMaxAccess(_B)
if mibBuilder.loadTexts:mirrorDestinationPort.setStatus(_A)
_MirrorSourcePort_Type=Integer32
_MirrorSourcePort_Object=MibTableColumn
mirrorSourcePort=_MirrorSourcePort_Object((1,3,6,1,4,1,674,10895,3,1,8,1,1,2),_MirrorSourcePort_Type())
mirrorSourcePort.setMaxAccess(_B)
if mibBuilder.loadTexts:mirrorSourcePort.setStatus(_A)
class _MirrorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('rx',1),('tx',2),('both',3)))
_MirrorType_Type.__name__=_C
_MirrorType_Object=MibTableColumn
mirrorType=_MirrorType_Object((1,3,6,1,4,1,674,10895,3,1,8,1,1,3),_MirrorType_Type())
mirrorType.setMaxAccess(_G)
if mibBuilder.loadTexts:mirrorType.setStatus(_A)
class _MirrorStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_MirrorStatus_Type.__name__=_C
_MirrorStatus_Object=MibTableColumn
mirrorStatus=_MirrorStatus_Object((1,3,6,1,4,1,674,10895,3,1,8,1,1,4),_MirrorStatus_Type())
mirrorStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:mirrorStatus.setStatus(_A)
_IgmpSnoopMgt_ObjectIdentity=ObjectIdentity
igmpSnoopMgt=_IgmpSnoopMgt_ObjectIdentity((1,3,6,1,4,1,674,10895,3,1,9))
class _IgmpSnoopStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_H,2)))
_IgmpSnoopStatus_Type.__name__=_C
_IgmpSnoopStatus_Object=MibScalar
igmpSnoopStatus=_IgmpSnoopStatus_Object((1,3,6,1,4,1,674,10895,3,1,9,1),_IgmpSnoopStatus_Type())
igmpSnoopStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:igmpSnoopStatus.setStatus(_A)
class _IgmpSnoopQuerier_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_H,2)))
_IgmpSnoopQuerier_Type.__name__=_C
_IgmpSnoopQuerier_Object=MibScalar
igmpSnoopQuerier=_IgmpSnoopQuerier_Object((1,3,6,1,4,1,674,10895,3,1,9,2),_IgmpSnoopQuerier_Type())
igmpSnoopQuerier.setMaxAccess(_D)
if mibBuilder.loadTexts:igmpSnoopQuerier.setStatus(_A)
class _IgmpSnoopQueryCount_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,10))
_IgmpSnoopQueryCount_Type.__name__=_C
_IgmpSnoopQueryCount_Object=MibScalar
igmpSnoopQueryCount=_IgmpSnoopQueryCount_Object((1,3,6,1,4,1,674,10895,3,1,9,3),_IgmpSnoopQueryCount_Type())
igmpSnoopQueryCount.setMaxAccess(_D)
if mibBuilder.loadTexts:igmpSnoopQueryCount.setStatus(_A)
class _IgmpSnoopQueryInterval_Type(Integer32):defaultValue=125;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,125))
_IgmpSnoopQueryInterval_Type.__name__=_C
_IgmpSnoopQueryInterval_Object=MibScalar
igmpSnoopQueryInterval=_IgmpSnoopQueryInterval_Object((1,3,6,1,4,1,674,10895,3,1,9,4),_IgmpSnoopQueryInterval_Type())
igmpSnoopQueryInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:igmpSnoopQueryInterval.setStatus(_A)
class _IgmpSnoopQueryMaxResponseTime_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,30))
_IgmpSnoopQueryMaxResponseTime_Type.__name__=_C
_IgmpSnoopQueryMaxResponseTime_Object=MibScalar
igmpSnoopQueryMaxResponseTime=_IgmpSnoopQueryMaxResponseTime_Object((1,3,6,1,4,1,674,10895,3,1,9,5),_IgmpSnoopQueryMaxResponseTime_Type())
igmpSnoopQueryMaxResponseTime.setMaxAccess(_D)
if mibBuilder.loadTexts:igmpSnoopQueryMaxResponseTime.setStatus(_A)
class _IgmpSnoopQueryTimeout_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(300,500))
_IgmpSnoopQueryTimeout_Type.__name__=_C
_IgmpSnoopQueryTimeout_Object=MibScalar
igmpSnoopQueryTimeout=_IgmpSnoopQueryTimeout_Object((1,3,6,1,4,1,674,10895,3,1,9,6),_IgmpSnoopQueryTimeout_Type())
igmpSnoopQueryTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:igmpSnoopQueryTimeout.setStatus(_A)
class _IgmpSnoopVersion_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_IgmpSnoopVersion_Type.__name__=_C
_IgmpSnoopVersion_Object=MibScalar
igmpSnoopVersion=_IgmpSnoopVersion_Object((1,3,6,1,4,1,674,10895,3,1,9,7),_IgmpSnoopVersion_Type())
igmpSnoopVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:igmpSnoopVersion.setStatus(_A)
_IgmpSnoopRouterCurrentTable_Object=MibTable
igmpSnoopRouterCurrentTable=_IgmpSnoopRouterCurrentTable_Object((1,3,6,1,4,1,674,10895,3,1,9,8))
if mibBuilder.loadTexts:igmpSnoopRouterCurrentTable.setStatus(_A)
_IgmpSnoopRouterCurrentEntry_Object=MibTableRow
igmpSnoopRouterCurrentEntry=_IgmpSnoopRouterCurrentEntry_Object((1,3,6,1,4,1,674,10895,3,1,9,8,1))
igmpSnoopRouterCurrentEntry.setIndexNames((0,_E,_x))
if mibBuilder.loadTexts:igmpSnoopRouterCurrentEntry.setStatus(_A)
_IgmpSnoopRouterCurrentVlanIndex_Type=Unsigned32
_IgmpSnoopRouterCurrentVlanIndex_Object=MibTableColumn
igmpSnoopRouterCurrentVlanIndex=_IgmpSnoopRouterCurrentVlanIndex_Object((1,3,6,1,4,1,674,10895,3,1,9,8,1,1),_IgmpSnoopRouterCurrentVlanIndex_Type())
igmpSnoopRouterCurrentVlanIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:igmpSnoopRouterCurrentVlanIndex.setStatus(_A)
_IgmpSnoopRouterCurrentPorts_Type=PortList
_IgmpSnoopRouterCurrentPorts_Object=MibTableColumn
igmpSnoopRouterCurrentPorts=_IgmpSnoopRouterCurrentPorts_Object((1,3,6,1,4,1,674,10895,3,1,9,8,1,2),_IgmpSnoopRouterCurrentPorts_Type())
igmpSnoopRouterCurrentPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:igmpSnoopRouterCurrentPorts.setStatus(_A)
_IgmpSnoopRouterCurrentStatus_Type=PortList
_IgmpSnoopRouterCurrentStatus_Object=MibTableColumn
igmpSnoopRouterCurrentStatus=_IgmpSnoopRouterCurrentStatus_Object((1,3,6,1,4,1,674,10895,3,1,9,8,1,3),_IgmpSnoopRouterCurrentStatus_Type())
igmpSnoopRouterCurrentStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:igmpSnoopRouterCurrentStatus.setStatus(_A)
_IgmpSnoopRouterStaticTable_Object=MibTable
igmpSnoopRouterStaticTable=_IgmpSnoopRouterStaticTable_Object((1,3,6,1,4,1,674,10895,3,1,9,9))
if mibBuilder.loadTexts:igmpSnoopRouterStaticTable.setStatus(_A)
_IgmpSnoopRouterStaticEntry_Object=MibTableRow
igmpSnoopRouterStaticEntry=_IgmpSnoopRouterStaticEntry_Object((1,3,6,1,4,1,674,10895,3,1,9,9,1))
igmpSnoopRouterStaticEntry.setIndexNames((0,_E,_y))
if mibBuilder.loadTexts:igmpSnoopRouterStaticEntry.setStatus(_A)
_IgmpSnoopRouterStaticVlanIndex_Type=Unsigned32
_IgmpSnoopRouterStaticVlanIndex_Object=MibTableColumn
igmpSnoopRouterStaticVlanIndex=_IgmpSnoopRouterStaticVlanIndex_Object((1,3,6,1,4,1,674,10895,3,1,9,9,1,1),_IgmpSnoopRouterStaticVlanIndex_Type())
igmpSnoopRouterStaticVlanIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:igmpSnoopRouterStaticVlanIndex.setStatus(_A)
_IgmpSnoopRouterStaticPorts_Type=PortList
_IgmpSnoopRouterStaticPorts_Object=MibTableColumn
igmpSnoopRouterStaticPorts=_IgmpSnoopRouterStaticPorts_Object((1,3,6,1,4,1,674,10895,3,1,9,9,1,2),_IgmpSnoopRouterStaticPorts_Type())
igmpSnoopRouterStaticPorts.setMaxAccess(_G)
if mibBuilder.loadTexts:igmpSnoopRouterStaticPorts.setStatus(_A)
class _IgmpSnoopRouterStaticStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_IgmpSnoopRouterStaticStatus_Type.__name__=_C
_IgmpSnoopRouterStaticStatus_Object=MibTableColumn
igmpSnoopRouterStaticStatus=_IgmpSnoopRouterStaticStatus_Object((1,3,6,1,4,1,674,10895,3,1,9,9,1,3),_IgmpSnoopRouterStaticStatus_Type())
igmpSnoopRouterStaticStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:igmpSnoopRouterStaticStatus.setStatus(_A)
_IgmpSnoopMulticastCurrentTable_Object=MibTable
igmpSnoopMulticastCurrentTable=_IgmpSnoopMulticastCurrentTable_Object((1,3,6,1,4,1,674,10895,3,1,9,10))
if mibBuilder.loadTexts:igmpSnoopMulticastCurrentTable.setStatus(_A)
_IgmpSnoopMulticastCurrentEntry_Object=MibTableRow
igmpSnoopMulticastCurrentEntry=_IgmpSnoopMulticastCurrentEntry_Object((1,3,6,1,4,1,674,10895,3,1,9,10,1))
igmpSnoopMulticastCurrentEntry.setIndexNames((0,_E,_z),(0,_E,_A0))
if mibBuilder.loadTexts:igmpSnoopMulticastCurrentEntry.setStatus(_A)
_IgmpSnoopMulticastCurrentVlanIndex_Type=Unsigned32
_IgmpSnoopMulticastCurrentVlanIndex_Object=MibTableColumn
igmpSnoopMulticastCurrentVlanIndex=_IgmpSnoopMulticastCurrentVlanIndex_Object((1,3,6,1,4,1,674,10895,3,1,9,10,1,1),_IgmpSnoopMulticastCurrentVlanIndex_Type())
igmpSnoopMulticastCurrentVlanIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:igmpSnoopMulticastCurrentVlanIndex.setStatus(_A)
_IgmpSnoopMulticastCurrentIpAddress_Type=IpAddress
_IgmpSnoopMulticastCurrentIpAddress_Object=MibTableColumn
igmpSnoopMulticastCurrentIpAddress=_IgmpSnoopMulticastCurrentIpAddress_Object((1,3,6,1,4,1,674,10895,3,1,9,10,1,2),_IgmpSnoopMulticastCurrentIpAddress_Type())
igmpSnoopMulticastCurrentIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:igmpSnoopMulticastCurrentIpAddress.setStatus(_A)
_IgmpSnoopMulticastCurrentPorts_Type=PortList
_IgmpSnoopMulticastCurrentPorts_Object=MibTableColumn
igmpSnoopMulticastCurrentPorts=_IgmpSnoopMulticastCurrentPorts_Object((1,3,6,1,4,1,674,10895,3,1,9,10,1,3),_IgmpSnoopMulticastCurrentPorts_Type())
igmpSnoopMulticastCurrentPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:igmpSnoopMulticastCurrentPorts.setStatus(_A)
_IgmpSnoopMulticastCurrentStatus_Type=PortList
_IgmpSnoopMulticastCurrentStatus_Object=MibTableColumn
igmpSnoopMulticastCurrentStatus=_IgmpSnoopMulticastCurrentStatus_Object((1,3,6,1,4,1,674,10895,3,1,9,10,1,4),_IgmpSnoopMulticastCurrentStatus_Type())
igmpSnoopMulticastCurrentStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:igmpSnoopMulticastCurrentStatus.setStatus(_A)
_IgmpSnoopMulticastStaticTable_Object=MibTable
igmpSnoopMulticastStaticTable=_IgmpSnoopMulticastStaticTable_Object((1,3,6,1,4,1,674,10895,3,1,9,11))
if mibBuilder.loadTexts:igmpSnoopMulticastStaticTable.setStatus(_A)
_IgmpSnoopMulticastStaticEntry_Object=MibTableRow
igmpSnoopMulticastStaticEntry=_IgmpSnoopMulticastStaticEntry_Object((1,3,6,1,4,1,674,10895,3,1,9,11,1))
igmpSnoopMulticastStaticEntry.setIndexNames((0,_E,_A1),(0,_E,_A2))
if mibBuilder.loadTexts:igmpSnoopMulticastStaticEntry.setStatus(_A)
_IgmpSnoopMulticastStaticVlanIndex_Type=Unsigned32
_IgmpSnoopMulticastStaticVlanIndex_Object=MibTableColumn
igmpSnoopMulticastStaticVlanIndex=_IgmpSnoopMulticastStaticVlanIndex_Object((1,3,6,1,4,1,674,10895,3,1,9,11,1,1),_IgmpSnoopMulticastStaticVlanIndex_Type())
igmpSnoopMulticastStaticVlanIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:igmpSnoopMulticastStaticVlanIndex.setStatus(_A)
_IgmpSnoopMulticastStaticIpAddress_Type=IpAddress
_IgmpSnoopMulticastStaticIpAddress_Object=MibTableColumn
igmpSnoopMulticastStaticIpAddress=_IgmpSnoopMulticastStaticIpAddress_Object((1,3,6,1,4,1,674,10895,3,1,9,11,1,2),_IgmpSnoopMulticastStaticIpAddress_Type())
igmpSnoopMulticastStaticIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:igmpSnoopMulticastStaticIpAddress.setStatus(_A)
_IgmpSnoopMulticastStaticPorts_Type=PortList
_IgmpSnoopMulticastStaticPorts_Object=MibTableColumn
igmpSnoopMulticastStaticPorts=_IgmpSnoopMulticastStaticPorts_Object((1,3,6,1,4,1,674,10895,3,1,9,11,1,3),_IgmpSnoopMulticastStaticPorts_Type())
igmpSnoopMulticastStaticPorts.setMaxAccess(_G)
if mibBuilder.loadTexts:igmpSnoopMulticastStaticPorts.setStatus(_A)
class _IgmpSnoopMulticastStaticStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_IgmpSnoopMulticastStaticStatus_Type.__name__=_C
_IgmpSnoopMulticastStaticStatus_Object=MibTableColumn
igmpSnoopMulticastStaticStatus=_IgmpSnoopMulticastStaticStatus_Object((1,3,6,1,4,1,674,10895,3,1,9,11,1,4),_IgmpSnoopMulticastStaticStatus_Type())
igmpSnoopMulticastStaticStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:igmpSnoopMulticastStaticStatus.setStatus(_A)
_IpMgt_ObjectIdentity=ObjectIdentity
ipMgt=_IpMgt_ObjectIdentity((1,3,6,1,4,1,674,10895,3,1,10))
_NetConfigTable_Object=MibTable
netConfigTable=_NetConfigTable_Object((1,3,6,1,4,1,674,10895,3,1,10,1))
if mibBuilder.loadTexts:netConfigTable.setStatus(_A)
_NetConfigEntry_Object=MibTableRow
netConfigEntry=_NetConfigEntry_Object((1,3,6,1,4,1,674,10895,3,1,10,1,1))
netConfigEntry.setIndexNames((0,_E,_A3),(0,_E,_A4),(0,_E,_A5))
if mibBuilder.loadTexts:netConfigEntry.setStatus(_A)
_NetConfigIfIndex_Type=Integer32
_NetConfigIfIndex_Object=MibTableColumn
netConfigIfIndex=_NetConfigIfIndex_Object((1,3,6,1,4,1,674,10895,3,1,10,1,1,1),_NetConfigIfIndex_Type())
netConfigIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:netConfigIfIndex.setStatus(_A)
_NetConfigIPAddress_Type=IpAddress
_NetConfigIPAddress_Object=MibTableColumn
netConfigIPAddress=_NetConfigIPAddress_Object((1,3,6,1,4,1,674,10895,3,1,10,1,1,2),_NetConfigIPAddress_Type())
netConfigIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:netConfigIPAddress.setStatus(_A)
_NetConfigSubnetMask_Type=IpAddress
_NetConfigSubnetMask_Object=MibTableColumn
netConfigSubnetMask=_NetConfigSubnetMask_Object((1,3,6,1,4,1,674,10895,3,1,10,1,1,3),_NetConfigSubnetMask_Type())
netConfigSubnetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:netConfigSubnetMask.setStatus(_A)
class _NetConfigPrimaryInterface_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('primary',1),('secondary',2)))
_NetConfigPrimaryInterface_Type.__name__=_C
_NetConfigPrimaryInterface_Object=MibTableColumn
netConfigPrimaryInterface=_NetConfigPrimaryInterface_Object((1,3,6,1,4,1,674,10895,3,1,10,1,1,4),_NetConfigPrimaryInterface_Type())
netConfigPrimaryInterface.setMaxAccess(_G)
if mibBuilder.loadTexts:netConfigPrimaryInterface.setStatus(_A)
class _NetConfigUnnumbered_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('unnumbered',1),('notUnnumbered',2)))
_NetConfigUnnumbered_Type.__name__=_C
_NetConfigUnnumbered_Object=MibTableColumn
netConfigUnnumbered=_NetConfigUnnumbered_Object((1,3,6,1,4,1,674,10895,3,1,10,1,1,5),_NetConfigUnnumbered_Type())
netConfigUnnumbered.setMaxAccess(_G)
if mibBuilder.loadTexts:netConfigUnnumbered.setStatus(_A)
_NetConfigStatus_Type=RowStatus
_NetConfigStatus_Object=MibTableColumn
netConfigStatus=_NetConfigStatus_Object((1,3,6,1,4,1,674,10895,3,1,10,1,1,6),_NetConfigStatus_Type())
netConfigStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:netConfigStatus.setStatus(_A)
_NetDefaultGateway_Type=IpAddress
_NetDefaultGateway_Object=MibScalar
netDefaultGateway=_NetDefaultGateway_Object((1,3,6,1,4,1,674,10895,3,1,10,2),_NetDefaultGateway_Type())
netDefaultGateway.setMaxAccess(_D)
if mibBuilder.loadTexts:netDefaultGateway.setStatus(_A)
class _IpHttpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_H,2)))
_IpHttpState_Type.__name__=_C
_IpHttpState_Object=MibScalar
ipHttpState=_IpHttpState_Object((1,3,6,1,4,1,674,10895,3,1,10,3),_IpHttpState_Type())
ipHttpState.setMaxAccess(_D)
if mibBuilder.loadTexts:ipHttpState.setStatus(_A)
class _IpHttpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_IpHttpPort_Type.__name__=_C
_IpHttpPort_Object=MibScalar
ipHttpPort=_IpHttpPort_Object((1,3,6,1,4,1,674,10895,3,1,10,4),_IpHttpPort_Type())
ipHttpPort.setMaxAccess(_D)
if mibBuilder.loadTexts:ipHttpPort.setStatus(_A)
class _IpDhcpRestart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('restart',1),('noRestart',2)))
_IpDhcpRestart_Type.__name__=_C
_IpDhcpRestart_Object=MibScalar
ipDhcpRestart=_IpDhcpRestart_Object((1,3,6,1,4,1,674,10895,3,1,10,5),_IpDhcpRestart_Type())
ipDhcpRestart.setMaxAccess(_D)
if mibBuilder.loadTexts:ipDhcpRestart.setStatus(_A)
_IpHttpsState_Type=EnabledStatus
_IpHttpsState_Object=MibScalar
ipHttpsState=_IpHttpsState_Object((1,3,6,1,4,1,674,10895,3,1,10,6),_IpHttpsState_Type())
ipHttpsState.setMaxAccess(_D)
if mibBuilder.loadTexts:ipHttpsState.setStatus(_A)
class _IpHttpsPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_IpHttpsPort_Type.__name__=_C
_IpHttpsPort_Object=MibScalar
ipHttpsPort=_IpHttpsPort_Object((1,3,6,1,4,1,674,10895,3,1,10,7),_IpHttpsPort_Type())
ipHttpsPort.setMaxAccess(_D)
if mibBuilder.loadTexts:ipHttpsPort.setStatus(_A)
_BcastStormMgt_ObjectIdentity=ObjectIdentity
bcastStormMgt=_BcastStormMgt_ObjectIdentity((1,3,6,1,4,1,674,10895,3,1,11))
_BcastStormTable_Object=MibTable
bcastStormTable=_BcastStormTable_Object((1,3,6,1,4,1,674,10895,3,1,11,1))
if mibBuilder.loadTexts:bcastStormTable.setStatus(_A)
_BcastStormEntry_Object=MibTableRow
bcastStormEntry=_BcastStormEntry_Object((1,3,6,1,4,1,674,10895,3,1,11,1,1))
bcastStormEntry.setIndexNames((0,_E,_A6))
if mibBuilder.loadTexts:bcastStormEntry.setStatus(_A)
_BcastStormIfIndex_Type=Integer32
_BcastStormIfIndex_Object=MibTableColumn
bcastStormIfIndex=_BcastStormIfIndex_Object((1,3,6,1,4,1,674,10895,3,1,11,1,1,1),_BcastStormIfIndex_Type())
bcastStormIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:bcastStormIfIndex.setStatus(_A)
class _BcastStormStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_H,2)))
_BcastStormStatus_Type.__name__=_C
_BcastStormStatus_Object=MibTableColumn
bcastStormStatus=_BcastStormStatus_Object((1,3,6,1,4,1,674,10895,3,1,11,1,1,2),_BcastStormStatus_Type())
bcastStormStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:bcastStormStatus.setStatus(_A)
class _BcastStormSampleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('pkt-rate',1),('octet-rate',2),('percent',3)))
_BcastStormSampleType_Type.__name__=_C
_BcastStormSampleType_Object=MibTableColumn
bcastStormSampleType=_BcastStormSampleType_Object((1,3,6,1,4,1,674,10895,3,1,11,1,1,3),_BcastStormSampleType_Type())
bcastStormSampleType.setMaxAccess(_D)
if mibBuilder.loadTexts:bcastStormSampleType.setStatus(_A)
_BcastStormPktRate_Type=Integer32
_BcastStormPktRate_Object=MibTableColumn
bcastStormPktRate=_BcastStormPktRate_Object((1,3,6,1,4,1,674,10895,3,1,11,1,1,4),_BcastStormPktRate_Type())
bcastStormPktRate.setMaxAccess(_D)
if mibBuilder.loadTexts:bcastStormPktRate.setStatus(_A)
_BcastStormOctetRate_Type=Integer32
_BcastStormOctetRate_Object=MibTableColumn
bcastStormOctetRate=_BcastStormOctetRate_Object((1,3,6,1,4,1,674,10895,3,1,11,1,1,5),_BcastStormOctetRate_Type())
bcastStormOctetRate.setMaxAccess(_D)
if mibBuilder.loadTexts:bcastStormOctetRate.setStatus(_A)
_BcastStormPercent_Type=Integer32
_BcastStormPercent_Object=MibTableColumn
bcastStormPercent=_BcastStormPercent_Object((1,3,6,1,4,1,674,10895,3,1,11,1,1,6),_BcastStormPercent_Type())
bcastStormPercent.setMaxAccess(_D)
if mibBuilder.loadTexts:bcastStormPercent.setStatus(_A)
_VlanMgt_ObjectIdentity=ObjectIdentity
vlanMgt=_VlanMgt_ObjectIdentity((1,3,6,1,4,1,674,10895,3,1,12))
_VlanTable_Object=MibTable
vlanTable=_VlanTable_Object((1,3,6,1,4,1,674,10895,3,1,12,1))
if mibBuilder.loadTexts:vlanTable.setStatus(_A)
_VlanEntry_Object=MibTableRow
vlanEntry=_VlanEntry_Object((1,3,6,1,4,1,674,10895,3,1,12,1,1))
vlanEntry.setIndexNames((0,_E,_A7))
if mibBuilder.loadTexts:vlanEntry.setStatus(_A)
_VlanIndex_Type=Unsigned32
_VlanIndex_Object=MibTableColumn
vlanIndex=_VlanIndex_Object((1,3,6,1,4,1,674,10895,3,1,12,1,1,1),_VlanIndex_Type())
vlanIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanIndex.setStatus(_A)
class _VlanAddressMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('user',1),('bootp',2),('dhcp',3)))
_VlanAddressMethod_Type.__name__=_C
_VlanAddressMethod_Object=MibTableColumn
vlanAddressMethod=_VlanAddressMethod_Object((1,3,6,1,4,1,674,10895,3,1,12,1,1,2),_VlanAddressMethod_Type())
vlanAddressMethod.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanAddressMethod.setStatus(_A)
_VlanPortTable_Object=MibTable
vlanPortTable=_VlanPortTable_Object((1,3,6,1,4,1,674,10895,3,1,12,2))
if mibBuilder.loadTexts:vlanPortTable.setStatus(_A)
_VlanPortEntry_Object=MibTableRow
vlanPortEntry=_VlanPortEntry_Object((1,3,6,1,4,1,674,10895,3,1,12,2,1))
vlanPortEntry.setIndexNames((0,_E,_A8))
if mibBuilder.loadTexts:vlanPortEntry.setStatus(_A)
_VlanPortIndex_Type=Integer32
_VlanPortIndex_Object=MibTableColumn
vlanPortIndex=_VlanPortIndex_Object((1,3,6,1,4,1,674,10895,3,1,12,2,1,1),_VlanPortIndex_Type())
vlanPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanPortIndex.setStatus(_A)
class _VlanPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('hybrid',1),('dot1qTrunk',2),('access',3)))
_VlanPortMode_Type.__name__=_C
_VlanPortMode_Object=MibTableColumn
vlanPortMode=_VlanPortMode_Object((1,3,6,1,4,1,674,10895,3,1,12,2,1,2),_VlanPortMode_Type())
vlanPortMode.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanPortMode.setStatus(_A)
_PriorityMgt_ObjectIdentity=ObjectIdentity
priorityMgt=_PriorityMgt_ObjectIdentity((1,3,6,1,4,1,674,10895,3,1,13))
class _PrioIpPrecDscpStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),('precedence',2),('dscp',3)))
_PrioIpPrecDscpStatus_Type.__name__=_C
_PrioIpPrecDscpStatus_Object=MibScalar
prioIpPrecDscpStatus=_PrioIpPrecDscpStatus_Object((1,3,6,1,4,1,674,10895,3,1,13,1),_PrioIpPrecDscpStatus_Type())
prioIpPrecDscpStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:prioIpPrecDscpStatus.setStatus(_A)
_PrioIpPrecTable_Object=MibTable
prioIpPrecTable=_PrioIpPrecTable_Object((1,3,6,1,4,1,674,10895,3,1,13,2))
if mibBuilder.loadTexts:prioIpPrecTable.setStatus(_A)
_PrioIpPrecEntry_Object=MibTableRow
prioIpPrecEntry=_PrioIpPrecEntry_Object((1,3,6,1,4,1,674,10895,3,1,13,2,1))
prioIpPrecEntry.setIndexNames((0,_E,_A9),(0,_E,_AA))
if mibBuilder.loadTexts:prioIpPrecEntry.setStatus(_A)
_PrioIpPrecPort_Type=Integer32
_PrioIpPrecPort_Object=MibTableColumn
prioIpPrecPort=_PrioIpPrecPort_Object((1,3,6,1,4,1,674,10895,3,1,13,2,1,2),_PrioIpPrecPort_Type())
prioIpPrecPort.setMaxAccess(_B)
if mibBuilder.loadTexts:prioIpPrecPort.setStatus(_A)
class _PrioIpPrecValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_PrioIpPrecValue_Type.__name__=_C
_PrioIpPrecValue_Object=MibTableColumn
prioIpPrecValue=_PrioIpPrecValue_Object((1,3,6,1,4,1,674,10895,3,1,13,2,1,3),_PrioIpPrecValue_Type())
prioIpPrecValue.setMaxAccess(_B)
if mibBuilder.loadTexts:prioIpPrecValue.setStatus(_A)
class _PrioIpPrecCos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_PrioIpPrecCos_Type.__name__=_C
_PrioIpPrecCos_Object=MibTableColumn
prioIpPrecCos=_PrioIpPrecCos_Object((1,3,6,1,4,1,674,10895,3,1,13,2,1,4),_PrioIpPrecCos_Type())
prioIpPrecCos.setMaxAccess(_D)
if mibBuilder.loadTexts:prioIpPrecCos.setStatus(_A)
_PrioIpPrecRestoreDefault_Type=Integer32
_PrioIpPrecRestoreDefault_Object=MibScalar
prioIpPrecRestoreDefault=_PrioIpPrecRestoreDefault_Object((1,3,6,1,4,1,674,10895,3,1,13,3),_PrioIpPrecRestoreDefault_Type())
prioIpPrecRestoreDefault.setMaxAccess(_D)
if mibBuilder.loadTexts:prioIpPrecRestoreDefault.setStatus(_A)
_PrioIpDscpTable_Object=MibTable
prioIpDscpTable=_PrioIpDscpTable_Object((1,3,6,1,4,1,674,10895,3,1,13,4))
if mibBuilder.loadTexts:prioIpDscpTable.setStatus(_A)
_PrioIpDscpEntry_Object=MibTableRow
prioIpDscpEntry=_PrioIpDscpEntry_Object((1,3,6,1,4,1,674,10895,3,1,13,4,1))
prioIpDscpEntry.setIndexNames((0,_E,_AB),(0,_E,_AC))
if mibBuilder.loadTexts:prioIpDscpEntry.setStatus(_A)
_PrioIpDscpPort_Type=Integer32
_PrioIpDscpPort_Object=MibTableColumn
prioIpDscpPort=_PrioIpDscpPort_Object((1,3,6,1,4,1,674,10895,3,1,13,4,1,1),_PrioIpDscpPort_Type())
prioIpDscpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:prioIpDscpPort.setStatus(_A)
class _PrioIpDscpValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_PrioIpDscpValue_Type.__name__=_C
_PrioIpDscpValue_Object=MibTableColumn
prioIpDscpValue=_PrioIpDscpValue_Object((1,3,6,1,4,1,674,10895,3,1,13,4,1,2),_PrioIpDscpValue_Type())
prioIpDscpValue.setMaxAccess(_B)
if mibBuilder.loadTexts:prioIpDscpValue.setStatus(_A)
class _PrioIpDscpCos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_PrioIpDscpCos_Type.__name__=_C
_PrioIpDscpCos_Object=MibTableColumn
prioIpDscpCos=_PrioIpDscpCos_Object((1,3,6,1,4,1,674,10895,3,1,13,4,1,3),_PrioIpDscpCos_Type())
prioIpDscpCos.setMaxAccess(_D)
if mibBuilder.loadTexts:prioIpDscpCos.setStatus(_A)
_PrioIpDscpRestoreDefault_Type=Integer32
_PrioIpDscpRestoreDefault_Object=MibScalar
prioIpDscpRestoreDefault=_PrioIpDscpRestoreDefault_Object((1,3,6,1,4,1,674,10895,3,1,13,5),_PrioIpDscpRestoreDefault_Type())
prioIpDscpRestoreDefault.setMaxAccess(_D)
if mibBuilder.loadTexts:prioIpDscpRestoreDefault.setStatus(_A)
class _PrioIpPortEnableStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_H,2)))
_PrioIpPortEnableStatus_Type.__name__=_C
_PrioIpPortEnableStatus_Object=MibScalar
prioIpPortEnableStatus=_PrioIpPortEnableStatus_Object((1,3,6,1,4,1,674,10895,3,1,13,6),_PrioIpPortEnableStatus_Type())
prioIpPortEnableStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:prioIpPortEnableStatus.setStatus(_A)
_PrioIpPortTable_Object=MibTable
prioIpPortTable=_PrioIpPortTable_Object((1,3,6,1,4,1,674,10895,3,1,13,7))
if mibBuilder.loadTexts:prioIpPortTable.setStatus(_A)
_PrioIpPortEntry_Object=MibTableRow
prioIpPortEntry=_PrioIpPortEntry_Object((1,3,6,1,4,1,674,10895,3,1,13,7,1))
prioIpPortEntry.setIndexNames((0,_E,_AD),(0,_E,_AE))
if mibBuilder.loadTexts:prioIpPortEntry.setStatus(_A)
_PrioIpPortPhysPort_Type=Integer32
_PrioIpPortPhysPort_Object=MibTableColumn
prioIpPortPhysPort=_PrioIpPortPhysPort_Object((1,3,6,1,4,1,674,10895,3,1,13,7,1,1),_PrioIpPortPhysPort_Type())
prioIpPortPhysPort.setMaxAccess(_B)
if mibBuilder.loadTexts:prioIpPortPhysPort.setStatus(_A)
class _PrioIpPortValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PrioIpPortValue_Type.__name__=_C
_PrioIpPortValue_Object=MibTableColumn
prioIpPortValue=_PrioIpPortValue_Object((1,3,6,1,4,1,674,10895,3,1,13,7,1,2),_PrioIpPortValue_Type())
prioIpPortValue.setMaxAccess(_B)
if mibBuilder.loadTexts:prioIpPortValue.setStatus(_A)
class _PrioIpPortCos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_PrioIpPortCos_Type.__name__=_C
_PrioIpPortCos_Object=MibTableColumn
prioIpPortCos=_PrioIpPortCos_Object((1,3,6,1,4,1,674,10895,3,1,13,7,1,3),_PrioIpPortCos_Type())
prioIpPortCos.setMaxAccess(_G)
if mibBuilder.loadTexts:prioIpPortCos.setStatus(_A)
class _PrioIpPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_PrioIpPortStatus_Type.__name__=_C
_PrioIpPortStatus_Object=MibTableColumn
prioIpPortStatus=_PrioIpPortStatus_Object((1,3,6,1,4,1,674,10895,3,1,13,7,1,4),_PrioIpPortStatus_Type())
prioIpPortStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:prioIpPortStatus.setStatus(_A)
_PrioCopy_ObjectIdentity=ObjectIdentity
prioCopy=_PrioCopy_ObjectIdentity((1,3,6,1,4,1,674,10895,3,1,13,8))
_PrioCopyIpPrec_Type=OctetString
_PrioCopyIpPrec_Object=MibScalar
prioCopyIpPrec=_PrioCopyIpPrec_Object((1,3,6,1,4,1,674,10895,3,1,13,8,1),_PrioCopyIpPrec_Type())
prioCopyIpPrec.setMaxAccess(_D)
if mibBuilder.loadTexts:prioCopyIpPrec.setStatus(_A)
_PrioCopyIpDscp_Type=OctetString
_PrioCopyIpDscp_Object=MibScalar
prioCopyIpDscp=_PrioCopyIpDscp_Object((1,3,6,1,4,1,674,10895,3,1,13,8,2),_PrioCopyIpDscp_Type())
prioCopyIpDscp.setMaxAccess(_D)
if mibBuilder.loadTexts:prioCopyIpDscp.setStatus(_A)
_PrioCopyIpPort_Type=OctetString
_PrioCopyIpPort_Object=MibScalar
prioCopyIpPort=_PrioCopyIpPort_Object((1,3,6,1,4,1,674,10895,3,1,13,8,3),_PrioCopyIpPort_Type())
prioCopyIpPort.setMaxAccess(_D)
if mibBuilder.loadTexts:prioCopyIpPort.setStatus(_A)
_PrioWrrTable_Object=MibTable
prioWrrTable=_PrioWrrTable_Object((1,3,6,1,4,1,674,10895,3,1,13,9))
if mibBuilder.loadTexts:prioWrrTable.setStatus(_A)
_PrioWrrEntry_Object=MibTableRow
prioWrrEntry=_PrioWrrEntry_Object((1,3,6,1,4,1,674,10895,3,1,13,9,1))
prioWrrEntry.setIndexNames((0,_E,_AF))
if mibBuilder.loadTexts:prioWrrEntry.setStatus(_A)
class _PrioWrrTrafficClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_PrioWrrTrafficClass_Type.__name__=_C
_PrioWrrTrafficClass_Object=MibTableColumn
prioWrrTrafficClass=_PrioWrrTrafficClass_Object((1,3,6,1,4,1,674,10895,3,1,13,9,1,1),_PrioWrrTrafficClass_Type())
prioWrrTrafficClass.setMaxAccess(_B)
if mibBuilder.loadTexts:prioWrrTrafficClass.setStatus(_A)
class _PrioWrrWeight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_PrioWrrWeight_Type.__name__=_C
_PrioWrrWeight_Object=MibTableColumn
prioWrrWeight=_PrioWrrWeight_Object((1,3,6,1,4,1,674,10895,3,1,13,9,1,2),_PrioWrrWeight_Type())
prioWrrWeight.setMaxAccess(_D)
if mibBuilder.loadTexts:prioWrrWeight.setStatus(_A)
_TrapDestMgt_ObjectIdentity=ObjectIdentity
trapDestMgt=_TrapDestMgt_ObjectIdentity((1,3,6,1,4,1,674,10895,3,1,14))
_TrapDestTable_Object=MibTable
trapDestTable=_TrapDestTable_Object((1,3,6,1,4,1,674,10895,3,1,14,1))
if mibBuilder.loadTexts:trapDestTable.setStatus(_A)
_TrapDestEntry_Object=MibTableRow
trapDestEntry=_TrapDestEntry_Object((1,3,6,1,4,1,674,10895,3,1,14,1,1))
trapDestEntry.setIndexNames((0,_E,_AG))
if mibBuilder.loadTexts:trapDestEntry.setStatus(_A)
_TrapDestAddress_Type=IpAddress
_TrapDestAddress_Object=MibTableColumn
trapDestAddress=_TrapDestAddress_Object((1,3,6,1,4,1,674,10895,3,1,14,1,1,1),_TrapDestAddress_Type())
trapDestAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:trapDestAddress.setStatus(_A)
class _TrapDestCommunity_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_TrapDestCommunity_Type.__name__=_M
_TrapDestCommunity_Object=MibTableColumn
trapDestCommunity=_TrapDestCommunity_Object((1,3,6,1,4,1,674,10895,3,1,14,1,1,2),_TrapDestCommunity_Type())
trapDestCommunity.setMaxAccess(_G)
if mibBuilder.loadTexts:trapDestCommunity.setStatus(_A)
class _TrapDestStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_TrapDestStatus_Type.__name__=_C
_TrapDestStatus_Object=MibTableColumn
trapDestStatus=_TrapDestStatus_Object((1,3,6,1,4,1,674,10895,3,1,14,1,1,3),_TrapDestStatus_Type())
trapDestStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:trapDestStatus.setStatus(_A)
class _TrapDestVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('version1',1),('version2',2)))
_TrapDestVersion_Type.__name__=_C
_TrapDestVersion_Object=MibTableColumn
trapDestVersion=_TrapDestVersion_Object((1,3,6,1,4,1,674,10895,3,1,14,1,1,4),_TrapDestVersion_Type())
trapDestVersion.setMaxAccess(_G)
if mibBuilder.loadTexts:trapDestVersion.setStatus(_A)
_SecurityMgt_ObjectIdentity=ObjectIdentity
securityMgt=_SecurityMgt_ObjectIdentity((1,3,6,1,4,1,674,10895,3,1,17))
_PortSecurityMgt_ObjectIdentity=ObjectIdentity
portSecurityMgt=_PortSecurityMgt_ObjectIdentity((1,3,6,1,4,1,674,10895,3,1,17,2))
_PortSecPortTable_Object=MibTable
portSecPortTable=_PortSecPortTable_Object((1,3,6,1,4,1,674,10895,3,1,17,2,1))
if mibBuilder.loadTexts:portSecPortTable.setStatus(_A)
_PortSecPortEntry_Object=MibTableRow
portSecPortEntry=_PortSecPortEntry_Object((1,3,6,1,4,1,674,10895,3,1,17,2,1,1))
portSecPortEntry.setIndexNames((0,_E,_AH))
if mibBuilder.loadTexts:portSecPortEntry.setStatus(_A)
_PortSecPortIndex_Type=Integer32
_PortSecPortIndex_Object=MibTableColumn
portSecPortIndex=_PortSecPortIndex_Object((1,3,6,1,4,1,674,10895,3,1,17,2,1,1,1),_PortSecPortIndex_Type())
portSecPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:portSecPortIndex.setStatus(_A)
_PortSecPortStatus_Type=EnabledStatus
_PortSecPortStatus_Object=MibTableColumn
portSecPortStatus=_PortSecPortStatus_Object((1,3,6,1,4,1,674,10895,3,1,17,2,1,1,2),_PortSecPortStatus_Type())
portSecPortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:portSecPortStatus.setStatus(_A)
class _PortSecAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_S,1),('trap',2),('shutdown',3),('trapAndShutdown',4)))
_PortSecAction_Type.__name__=_C
_PortSecAction_Object=MibTableColumn
portSecAction=_PortSecAction_Object((1,3,6,1,4,1,674,10895,3,1,17,2,1,1,3),_PortSecAction_Type())
portSecAction.setMaxAccess(_D)
if mibBuilder.loadTexts:portSecAction.setStatus(_A)
_RadiusMgt_ObjectIdentity=ObjectIdentity
radiusMgt=_RadiusMgt_ObjectIdentity((1,3,6,1,4,1,674,10895,3,1,17,4))
_RadiusServerAddress_Type=IpAddress
_RadiusServerAddress_Object=MibScalar
radiusServerAddress=_RadiusServerAddress_Object((1,3,6,1,4,1,674,10895,3,1,17,4,1),_RadiusServerAddress_Type())
radiusServerAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:radiusServerAddress.setStatus(_A)
class _RadiusServerPortNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_RadiusServerPortNumber_Type.__name__=_C
_RadiusServerPortNumber_Object=MibScalar
radiusServerPortNumber=_RadiusServerPortNumber_Object((1,3,6,1,4,1,674,10895,3,1,17,4,2),_RadiusServerPortNumber_Type())
radiusServerPortNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:radiusServerPortNumber.setStatus(_A)
_RadiusServerKey_Type=DisplayString
_RadiusServerKey_Object=MibScalar
radiusServerKey=_RadiusServerKey_Object((1,3,6,1,4,1,674,10895,3,1,17,4,3),_RadiusServerKey_Type())
radiusServerKey.setMaxAccess(_D)
if mibBuilder.loadTexts:radiusServerKey.setStatus(_A)
class _RadiusServerRetransmit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_RadiusServerRetransmit_Type.__name__=_C
_RadiusServerRetransmit_Object=MibScalar
radiusServerRetransmit=_RadiusServerRetransmit_Object((1,3,6,1,4,1,674,10895,3,1,17,4,4),_RadiusServerRetransmit_Type())
radiusServerRetransmit.setMaxAccess(_D)
if mibBuilder.loadTexts:radiusServerRetransmit.setStatus(_A)
class _RadiusServerTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_RadiusServerTimeout_Type.__name__=_C
_RadiusServerTimeout_Object=MibScalar
radiusServerTimeout=_RadiusServerTimeout_Object((1,3,6,1,4,1,674,10895,3,1,17,4,5),_RadiusServerTimeout_Type())
radiusServerTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:radiusServerTimeout.setStatus(_A)
_TacacsMgt_ObjectIdentity=ObjectIdentity
tacacsMgt=_TacacsMgt_ObjectIdentity((1,3,6,1,4,1,674,10895,3,1,17,5))
_TacacsServerAddress_Type=IpAddress
_TacacsServerAddress_Object=MibScalar
tacacsServerAddress=_TacacsServerAddress_Object((1,3,6,1,4,1,674,10895,3,1,17,5,1),_TacacsServerAddress_Type())
tacacsServerAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:tacacsServerAddress.setStatus(_A)
class _TacacsServerPortNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_TacacsServerPortNumber_Type.__name__=_C
_TacacsServerPortNumber_Object=MibScalar
tacacsServerPortNumber=_TacacsServerPortNumber_Object((1,3,6,1,4,1,674,10895,3,1,17,5,2),_TacacsServerPortNumber_Type())
tacacsServerPortNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:tacacsServerPortNumber.setStatus(_A)
_TacacsServerKey_Type=DisplayString
_TacacsServerKey_Object=MibScalar
tacacsServerKey=_TacacsServerKey_Object((1,3,6,1,4,1,674,10895,3,1,17,5,3),_TacacsServerKey_Type())
tacacsServerKey.setMaxAccess(_D)
if mibBuilder.loadTexts:tacacsServerKey.setStatus(_A)
_SshMgt_ObjectIdentity=ObjectIdentity
sshMgt=_SshMgt_ObjectIdentity((1,3,6,1,4,1,674,10895,3,1,17,6))
_SshServerStatus_Type=EnabledStatus
_SshServerStatus_Object=MibScalar
sshServerStatus=_SshServerStatus_Object((1,3,6,1,4,1,674,10895,3,1,17,6,1),_SshServerStatus_Type())
sshServerStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:sshServerStatus.setStatus(_A)
_SshServerMajorVersion_Type=Integer32
_SshServerMajorVersion_Object=MibScalar
sshServerMajorVersion=_SshServerMajorVersion_Object((1,3,6,1,4,1,674,10895,3,1,17,6,2),_SshServerMajorVersion_Type())
sshServerMajorVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:sshServerMajorVersion.setStatus(_A)
_SshServerMinorVersion_Type=Integer32
_SshServerMinorVersion_Object=MibScalar
sshServerMinorVersion=_SshServerMinorVersion_Object((1,3,6,1,4,1,674,10895,3,1,17,6,3),_SshServerMinorVersion_Type())
sshServerMinorVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:sshServerMinorVersion.setStatus(_A)
class _SshTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,120))
_SshTimeout_Type.__name__=_C
_SshTimeout_Object=MibScalar
sshTimeout=_SshTimeout_Object((1,3,6,1,4,1,674,10895,3,1,17,6,4),_SshTimeout_Type())
sshTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:sshTimeout.setStatus(_A)
class _SshAuthRetries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_SshAuthRetries_Type.__name__=_C
_SshAuthRetries_Object=MibScalar
sshAuthRetries=_SshAuthRetries_Object((1,3,6,1,4,1,674,10895,3,1,17,6,5),_SshAuthRetries_Type())
sshAuthRetries.setMaxAccess(_D)
if mibBuilder.loadTexts:sshAuthRetries.setStatus(_A)
_SshConnInfoTable_Object=MibTable
sshConnInfoTable=_SshConnInfoTable_Object((1,3,6,1,4,1,674,10895,3,1,17,6,6))
if mibBuilder.loadTexts:sshConnInfoTable.setStatus(_A)
_SshConnInfoEntry_Object=MibTableRow
sshConnInfoEntry=_SshConnInfoEntry_Object((1,3,6,1,4,1,674,10895,3,1,17,6,6,1))
sshConnInfoEntry.setIndexNames((0,_E,_AI))
if mibBuilder.loadTexts:sshConnInfoEntry.setStatus(_A)
_SshConnID_Type=Integer32
_SshConnID_Object=MibTableColumn
sshConnID=_SshConnID_Object((1,3,6,1,4,1,674,10895,3,1,17,6,6,1,1),_SshConnID_Type())
sshConnID.setMaxAccess(_B)
if mibBuilder.loadTexts:sshConnID.setStatus(_A)
_SshConnMajorVersion_Type=Integer32
_SshConnMajorVersion_Object=MibTableColumn
sshConnMajorVersion=_SshConnMajorVersion_Object((1,3,6,1,4,1,674,10895,3,1,17,6,6,1,2),_SshConnMajorVersion_Type())
sshConnMajorVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:sshConnMajorVersion.setStatus(_A)
_SshConnMinorVersion_Type=Integer32
_SshConnMinorVersion_Object=MibTableColumn
sshConnMinorVersion=_SshConnMinorVersion_Object((1,3,6,1,4,1,674,10895,3,1,17,6,6,1,3),_SshConnMinorVersion_Type())
sshConnMinorVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:sshConnMinorVersion.setStatus(_A)
class _SshConnEncryptionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_S,1),('des',2),('tribeDes',3)))
_SshConnEncryptionType_Type.__name__=_C
_SshConnEncryptionType_Object=MibTableColumn
sshConnEncryptionType=_SshConnEncryptionType_Object((1,3,6,1,4,1,674,10895,3,1,17,6,6,1,4),_SshConnEncryptionType_Type())
sshConnEncryptionType.setMaxAccess(_B)
if mibBuilder.loadTexts:sshConnEncryptionType.setStatus(_A)
class _SshConnStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('negotiationStart',1),('authenticationStart',2),('sessionStart',3)))
_SshConnStatus_Type.__name__=_C
_SshConnStatus_Object=MibTableColumn
sshConnStatus=_SshConnStatus_Object((1,3,6,1,4,1,674,10895,3,1,17,6,6,1,5),_SshConnStatus_Type())
sshConnStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sshConnStatus.setStatus(_A)
_SshConnUserName_Type=OctetString
_SshConnUserName_Object=MibTableColumn
sshConnUserName=_SshConnUserName_Object((1,3,6,1,4,1,674,10895,3,1,17,6,6,1,6),_SshConnUserName_Type())
sshConnUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:sshConnUserName.setStatus(_A)
class _SshDisconnect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noDisconnect',1),('disconnect',2)))
_SshDisconnect_Type.__name__=_C
_SshDisconnect_Object=MibTableColumn
sshDisconnect=_SshDisconnect_Object((1,3,6,1,4,1,674,10895,3,1,17,6,6,1,7),_SshDisconnect_Type())
sshDisconnect.setMaxAccess(_D)
if mibBuilder.loadTexts:sshDisconnect.setStatus(_A)
_SysLogMgt_ObjectIdentity=ObjectIdentity
sysLogMgt=_SysLogMgt_ObjectIdentity((1,3,6,1,4,1,674,10895,3,1,19))
class _SysLogStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_H,2)))
_SysLogStatus_Type.__name__=_C
_SysLogStatus_Object=MibScalar
sysLogStatus=_SysLogStatus_Object((1,3,6,1,4,1,674,10895,3,1,19,1),_SysLogStatus_Type())
sysLogStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:sysLogStatus.setStatus(_A)
class _SysLogHistoryFlashLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_SysLogHistoryFlashLevel_Type.__name__=_C
_SysLogHistoryFlashLevel_Object=MibScalar
sysLogHistoryFlashLevel=_SysLogHistoryFlashLevel_Object((1,3,6,1,4,1,674,10895,3,1,19,2),_SysLogHistoryFlashLevel_Type())
sysLogHistoryFlashLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:sysLogHistoryFlashLevel.setStatus(_A)
class _SysLogHistoryRamLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_SysLogHistoryRamLevel_Type.__name__=_C
_SysLogHistoryRamLevel_Object=MibScalar
sysLogHistoryRamLevel=_SysLogHistoryRamLevel_Object((1,3,6,1,4,1,674,10895,3,1,19,3),_SysLogHistoryRamLevel_Type())
sysLogHistoryRamLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:sysLogHistoryRamLevel.setStatus(_A)
_RemoteLogMgt_ObjectIdentity=ObjectIdentity
remoteLogMgt=_RemoteLogMgt_ObjectIdentity((1,3,6,1,4,1,674,10895,3,1,19,6))
_RemoteLogStatus_Type=EnabledStatus
_RemoteLogStatus_Object=MibScalar
remoteLogStatus=_RemoteLogStatus_Object((1,3,6,1,4,1,674,10895,3,1,19,6,1),_RemoteLogStatus_Type())
remoteLogStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:remoteLogStatus.setStatus(_A)
class _RemoteLogLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RemoteLogLevel_Type.__name__=_C
_RemoteLogLevel_Object=MibScalar
remoteLogLevel=_RemoteLogLevel_Object((1,3,6,1,4,1,674,10895,3,1,19,6,2),_RemoteLogLevel_Type())
remoteLogLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:remoteLogLevel.setStatus(_A)
class _RemoteLogFacilityType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(16,17,18,19,20,21,22,23)));namedValues=NamedValues(*(('localUse0',16),('localUse1',17),('localUse2',18),('localUse3',19),('localUse4',20),('localUse5',21),('localUse6',22),('localUse7',23)))
_RemoteLogFacilityType_Type.__name__=_C
_RemoteLogFacilityType_Object=MibScalar
remoteLogFacilityType=_RemoteLogFacilityType_Object((1,3,6,1,4,1,674,10895,3,1,19,6,3),_RemoteLogFacilityType_Type())
remoteLogFacilityType.setMaxAccess(_D)
if mibBuilder.loadTexts:remoteLogFacilityType.setStatus(_A)
_RemoteLogServerTable_Object=MibTable
remoteLogServerTable=_RemoteLogServerTable_Object((1,3,6,1,4,1,674,10895,3,1,19,6,4))
if mibBuilder.loadTexts:remoteLogServerTable.setStatus(_A)
_RemoteLogServerEntry_Object=MibTableRow
remoteLogServerEntry=_RemoteLogServerEntry_Object((1,3,6,1,4,1,674,10895,3,1,19,6,4,1))
remoteLogServerEntry.setIndexNames((0,_E,_AJ))
if mibBuilder.loadTexts:remoteLogServerEntry.setStatus(_A)
_RemoteLogServerIp_Type=IpAddress
_RemoteLogServerIp_Object=MibTableColumn
remoteLogServerIp=_RemoteLogServerIp_Object((1,3,6,1,4,1,674,10895,3,1,19,6,4,1,1),_RemoteLogServerIp_Type())
remoteLogServerIp.setMaxAccess(_G)
if mibBuilder.loadTexts:remoteLogServerIp.setStatus(_A)
_RemoteLogServerStatus_Type=ValidStatus
_RemoteLogServerStatus_Object=MibTableColumn
remoteLogServerStatus=_RemoteLogServerStatus_Object((1,3,6,1,4,1,674,10895,3,1,19,6,4,1,2),_RemoteLogServerStatus_Type())
remoteLogServerStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:remoteLogServerStatus.setStatus(_A)
_LineMgt_ObjectIdentity=ObjectIdentity
lineMgt=_LineMgt_ObjectIdentity((1,3,6,1,4,1,674,10895,3,1,20))
_ConsoleMgt_ObjectIdentity=ObjectIdentity
consoleMgt=_ConsoleMgt_ObjectIdentity((1,3,6,1,4,1,674,10895,3,1,20,1))
class _ConsoleDataBits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('databits7',1),('databits8',2)))
_ConsoleDataBits_Type.__name__=_C
_ConsoleDataBits_Object=MibScalar
consoleDataBits=_ConsoleDataBits_Object((1,3,6,1,4,1,674,10895,3,1,20,1,1),_ConsoleDataBits_Type())
consoleDataBits.setMaxAccess(_D)
if mibBuilder.loadTexts:consoleDataBits.setStatus(_A)
class _ConsoleParity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('partyNone',1),('partyEven',2),('partyOdd',3)))
_ConsoleParity_Type.__name__=_C
_ConsoleParity_Object=MibScalar
consoleParity=_ConsoleParity_Object((1,3,6,1,4,1,674,10895,3,1,20,1,2),_ConsoleParity_Type())
consoleParity.setMaxAccess(_D)
if mibBuilder.loadTexts:consoleParity.setStatus(_A)
class _ConsoleBaudRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('baudRate9600',1),('baudRate19200',2),('baudRate38400',3),('baudRate57600',4),('baudRate115200',5)))
_ConsoleBaudRate_Type.__name__=_C
_ConsoleBaudRate_Object=MibScalar
consoleBaudRate=_ConsoleBaudRate_Object((1,3,6,1,4,1,674,10895,3,1,20,1,3),_ConsoleBaudRate_Type())
consoleBaudRate.setMaxAccess(_D)
if mibBuilder.loadTexts:consoleBaudRate.setStatus(_A)
class _ConsoleStopBits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('stopbits1',1),('stopbits2',2)))
_ConsoleStopBits_Type.__name__=_C
_ConsoleStopBits_Object=MibScalar
consoleStopBits=_ConsoleStopBits_Object((1,3,6,1,4,1,674,10895,3,1,20,1,4),_ConsoleStopBits_Type())
consoleStopBits.setMaxAccess(_D)
if mibBuilder.loadTexts:consoleStopBits.setStatus(_A)
class _ConsoleExecTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ConsoleExecTimeout_Type.__name__=_C
_ConsoleExecTimeout_Object=MibScalar
consoleExecTimeout=_ConsoleExecTimeout_Object((1,3,6,1,4,1,674,10895,3,1,20,1,5),_ConsoleExecTimeout_Type())
consoleExecTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:consoleExecTimeout.setStatus(_A)
class _ConsolePasswordThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,120))
_ConsolePasswordThreshold_Type.__name__=_C
_ConsolePasswordThreshold_Object=MibScalar
consolePasswordThreshold=_ConsolePasswordThreshold_Object((1,3,6,1,4,1,674,10895,3,1,20,1,6),_ConsolePasswordThreshold_Type())
consolePasswordThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:consolePasswordThreshold.setStatus(_A)
class _ConsoleSilentTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ConsoleSilentTime_Type.__name__=_C
_ConsoleSilentTime_Object=MibScalar
consoleSilentTime=_ConsoleSilentTime_Object((1,3,6,1,4,1,674,10895,3,1,20,1,7),_ConsoleSilentTime_Type())
consoleSilentTime.setMaxAccess(_D)
if mibBuilder.loadTexts:consoleSilentTime.setStatus(_A)
_TelnetMgt_ObjectIdentity=ObjectIdentity
telnetMgt=_TelnetMgt_ObjectIdentity((1,3,6,1,4,1,674,10895,3,1,20,2))
class _TelnetExecTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_TelnetExecTimeout_Type.__name__=_C
_TelnetExecTimeout_Object=MibScalar
telnetExecTimeout=_TelnetExecTimeout_Object((1,3,6,1,4,1,674,10895,3,1,20,2,1),_TelnetExecTimeout_Type())
telnetExecTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:telnetExecTimeout.setStatus(_A)
class _TelnetPasswordThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,120))
_TelnetPasswordThreshold_Type.__name__=_C
_TelnetPasswordThreshold_Object=MibScalar
telnetPasswordThreshold=_TelnetPasswordThreshold_Object((1,3,6,1,4,1,674,10895,3,1,20,2,2),_TelnetPasswordThreshold_Type())
telnetPasswordThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:telnetPasswordThreshold.setStatus(_A)
_PowerConnect3248Notifications_ObjectIdentity=ObjectIdentity
powerConnect3248Notifications=_PowerConnect3248Notifications_ObjectIdentity((1,3,6,1,4,1,674,10895,3,2))
_PowerConnect3248Traps_ObjectIdentity=ObjectIdentity
powerConnect3248Traps=_PowerConnect3248Traps_ObjectIdentity((1,3,6,1,4,1,674,10895,3,2,1))
_PowerConnect3248TrapsPrefix_ObjectIdentity=ObjectIdentity
powerConnect3248TrapsPrefix=_PowerConnect3248TrapsPrefix_ObjectIdentity((1,3,6,1,4,1,674,10895,3,2,1,0))
_PowerConnect3248Conformance_ObjectIdentity=ObjectIdentity
powerConnect3248Conformance=_PowerConnect3248Conformance_ObjectIdentity((1,3,6,1,4,1,674,10895,3,3))
swPowerStatusChangeTrap=NotificationType((1,3,6,1,4,1,674,10895,3,2,1,0,1))
swPowerStatusChangeTrap.setObjects(*((_E,_Q),(_E,_R),(_E,_AK)))
if mibBuilder.loadTexts:swPowerStatusChangeTrap.setStatus(_A)
swPortSecurityTrap=NotificationType((1,3,6,1,4,1,674,10895,3,2,1,0,36))
swPortSecurityTrap.setObjects((_T,_U))
if mibBuilder.loadTexts:swPortSecurityTrap.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'ValidStatus':ValidStatus,'private':private,'enterprises':enterprises,'dell':dell,'dellLan':dellLan,'powerConnect3248MIB':powerConnect3248MIB,'powerConnect3248MIBObjects':powerConnect3248MIBObjects,'switchMgt':switchMgt,'switchManagementVlan':switchManagementVlan,'switchNumber':switchNumber,'switchInfoTable':switchInfoTable,'switchInfoEntry':switchInfoEntry,_W:swUnitIndex,'swHardwareVer':swHardwareVer,'swMicrocodeVer':swMicrocodeVer,'swLoaderVer':swLoaderVer,'swBootRomVer':swBootRomVer,'swOpCodeVer':swOpCodeVer,'swPortNumber':swPortNumber,'swPowerStatus':swPowerStatus,'swRoleInSystem':swRoleInSystem,'swSerialNumber':swSerialNumber,'swExpansionSlot1':swExpansionSlot1,'swExpansionSlot2':swExpansionSlot2,'swServiceTag':swServiceTag,'switchOperState':switchOperState,'switchProductId':switchProductId,'swProdName':swProdName,'swProdManufacturer':swProdManufacturer,'swProdDescription':swProdDescription,'swProdVersion':swProdVersion,'swProdUrl':swProdUrl,'swIdentifier':swIdentifier,'swChassisServiceTag':swChassisServiceTag,'switchIndivPowerTable':switchIndivPowerTable,'switchIndivPowerEntry':switchIndivPowerEntry,_Q:swIndivPowerUnitIndex,_R:swIndivPowerIndex,_AK:swIndivPowerStatus,'portMgt':portMgt,'portTable':portTable,'portEntry':portEntry,_g:portIndex,'portName':portName,'portType':portType,'portSpeedDpxCfg':portSpeedDpxCfg,'portFlowCtrlCfg':portFlowCtrlCfg,'portCapabilities':portCapabilities,'portAutonegotiation':portAutonegotiation,'portSpeedDpxStatus':portSpeedDpxStatus,'portFlowCtrlStatus':portFlowCtrlStatus,'portTrunkIndex':portTrunkIndex,'trunkMgt':trunkMgt,'trunkMaxId':trunkMaxId,'trunkValidNumber':trunkValidNumber,'trunkTable':trunkTable,'trunkEntry':trunkEntry,_p:trunkIndex,'trunkPorts':trunkPorts,'trunkCreation':trunkCreation,'trunkStatus':trunkStatus,'lacpMgt':lacpMgt,'lacpPortTable':lacpPortTable,'lacpPortEntry':lacpPortEntry,_q:lacpPortIndex,'lacpPortStatus':lacpPortStatus,'staMgt':staMgt,'staSystemStatus':staSystemStatus,'staPortTable':staPortTable,'staPortEntry':staPortEntry,_r:staPortIndex,'staPortFastForward':staPortFastForward,'staPortProtocolMigration':staPortProtocolMigration,'staPortAdminEdgePort':staPortAdminEdgePort,'staPortOperEdgePort':staPortOperEdgePort,'staPortAdminPointToPoint':staPortAdminPointToPoint,'staPortOperPointToPoint':staPortOperPointToPoint,'staPortLongPathCost':staPortLongPathCost,'staProtocolType':staProtocolType,'staTxHoldCount':staTxHoldCount,'staPathCostMethod':staPathCostMethod,'xstMgt':xstMgt,'xstInstanceCfgTable':xstInstanceCfgTable,'xstInstanceCfgEntry':xstInstanceCfgEntry,_s:xstInstanceCfgIndex,'xstInstanceCfgPriority':xstInstanceCfgPriority,'xstInstanceCfgTimeSinceTopologyChange':xstInstanceCfgTimeSinceTopologyChange,'xstInstanceCfgTopChanges':xstInstanceCfgTopChanges,'xstInstanceCfgDesignatedRoot':xstInstanceCfgDesignatedRoot,'xstInstanceCfgRootCost':xstInstanceCfgRootCost,'xstInstanceCfgRootPort':xstInstanceCfgRootPort,'xstInstanceCfgMaxAge':xstInstanceCfgMaxAge,'xstInstanceCfgHelloTime':xstInstanceCfgHelloTime,'xstInstanceCfgHoldTime':xstInstanceCfgHoldTime,'xstInstanceCfgForwardDelay':xstInstanceCfgForwardDelay,'xstInstanceCfgBridgeMaxAge':xstInstanceCfgBridgeMaxAge,'xstInstanceCfgBridgeHelloTime':xstInstanceCfgBridgeHelloTime,'xstInstanceCfgBridgeForwardDelay':xstInstanceCfgBridgeForwardDelay,'xstInstanceCfgTxHoldCount':xstInstanceCfgTxHoldCount,'xstInstanceCfgPathCostMethod':xstInstanceCfgPathCostMethod,'xstInstancePortTable':xstInstancePortTable,'xstInstancePortEntry':xstInstancePortEntry,_t:xstInstancePortInstance,_u:xstInstancePortPort,'xstInstancePortPriority':xstInstancePortPriority,'xstInstancePortState':xstInstancePortState,'xstInstancePortEnable':xstInstancePortEnable,'xstInstancePortPathCost':xstInstancePortPathCost,'xstInstancePortDesignatedRoot':xstInstancePortDesignatedRoot,'xstInstancePortDesignatedCost':xstInstancePortDesignatedCost,'xstInstancePortDesignatedBridge':xstInstancePortDesignatedBridge,'xstInstancePortDesignatedPort':xstInstancePortDesignatedPort,'xstInstancePortForwardTransitions':xstInstancePortForwardTransitions,'xstInstancePortPortRole':xstInstancePortPortRole,'tftpMgt':tftpMgt,'tftpFileType':tftpFileType,'tftpSrcFile':tftpSrcFile,'tftpDestFile':tftpDestFile,'tftpServer':tftpServer,'tftpAction':tftpAction,'tftpStatus':tftpStatus,'restartMgt':restartMgt,'restartOpCodeFile':restartOpCodeFile,'restartConfigFile':restartConfigFile,'restartControl':restartControl,'mirrorMgt':mirrorMgt,'mirrorTable':mirrorTable,'mirrorEntry':mirrorEntry,_v:mirrorDestinationPort,_w:mirrorSourcePort,'mirrorType':mirrorType,'mirrorStatus':mirrorStatus,'igmpSnoopMgt':igmpSnoopMgt,'igmpSnoopStatus':igmpSnoopStatus,'igmpSnoopQuerier':igmpSnoopQuerier,'igmpSnoopQueryCount':igmpSnoopQueryCount,'igmpSnoopQueryInterval':igmpSnoopQueryInterval,'igmpSnoopQueryMaxResponseTime':igmpSnoopQueryMaxResponseTime,'igmpSnoopQueryTimeout':igmpSnoopQueryTimeout,'igmpSnoopVersion':igmpSnoopVersion,'igmpSnoopRouterCurrentTable':igmpSnoopRouterCurrentTable,'igmpSnoopRouterCurrentEntry':igmpSnoopRouterCurrentEntry,_x:igmpSnoopRouterCurrentVlanIndex,'igmpSnoopRouterCurrentPorts':igmpSnoopRouterCurrentPorts,'igmpSnoopRouterCurrentStatus':igmpSnoopRouterCurrentStatus,'igmpSnoopRouterStaticTable':igmpSnoopRouterStaticTable,'igmpSnoopRouterStaticEntry':igmpSnoopRouterStaticEntry,_y:igmpSnoopRouterStaticVlanIndex,'igmpSnoopRouterStaticPorts':igmpSnoopRouterStaticPorts,'igmpSnoopRouterStaticStatus':igmpSnoopRouterStaticStatus,'igmpSnoopMulticastCurrentTable':igmpSnoopMulticastCurrentTable,'igmpSnoopMulticastCurrentEntry':igmpSnoopMulticastCurrentEntry,_z:igmpSnoopMulticastCurrentVlanIndex,_A0:igmpSnoopMulticastCurrentIpAddress,'igmpSnoopMulticastCurrentPorts':igmpSnoopMulticastCurrentPorts,'igmpSnoopMulticastCurrentStatus':igmpSnoopMulticastCurrentStatus,'igmpSnoopMulticastStaticTable':igmpSnoopMulticastStaticTable,'igmpSnoopMulticastStaticEntry':igmpSnoopMulticastStaticEntry,_A1:igmpSnoopMulticastStaticVlanIndex,_A2:igmpSnoopMulticastStaticIpAddress,'igmpSnoopMulticastStaticPorts':igmpSnoopMulticastStaticPorts,'igmpSnoopMulticastStaticStatus':igmpSnoopMulticastStaticStatus,'ipMgt':ipMgt,'netConfigTable':netConfigTable,'netConfigEntry':netConfigEntry,_A3:netConfigIfIndex,_A4:netConfigIPAddress,_A5:netConfigSubnetMask,'netConfigPrimaryInterface':netConfigPrimaryInterface,'netConfigUnnumbered':netConfigUnnumbered,'netConfigStatus':netConfigStatus,'netDefaultGateway':netDefaultGateway,'ipHttpState':ipHttpState,'ipHttpPort':ipHttpPort,'ipDhcpRestart':ipDhcpRestart,'ipHttpsState':ipHttpsState,'ipHttpsPort':ipHttpsPort,'bcastStormMgt':bcastStormMgt,'bcastStormTable':bcastStormTable,'bcastStormEntry':bcastStormEntry,_A6:bcastStormIfIndex,'bcastStormStatus':bcastStormStatus,'bcastStormSampleType':bcastStormSampleType,'bcastStormPktRate':bcastStormPktRate,'bcastStormOctetRate':bcastStormOctetRate,'bcastStormPercent':bcastStormPercent,'vlanMgt':vlanMgt,'vlanTable':vlanTable,'vlanEntry':vlanEntry,_A7:vlanIndex,'vlanAddressMethod':vlanAddressMethod,'vlanPortTable':vlanPortTable,'vlanPortEntry':vlanPortEntry,_A8:vlanPortIndex,'vlanPortMode':vlanPortMode,'priorityMgt':priorityMgt,'prioIpPrecDscpStatus':prioIpPrecDscpStatus,'prioIpPrecTable':prioIpPrecTable,'prioIpPrecEntry':prioIpPrecEntry,_A9:prioIpPrecPort,_AA:prioIpPrecValue,'prioIpPrecCos':prioIpPrecCos,'prioIpPrecRestoreDefault':prioIpPrecRestoreDefault,'prioIpDscpTable':prioIpDscpTable,'prioIpDscpEntry':prioIpDscpEntry,_AB:prioIpDscpPort,_AC:prioIpDscpValue,'prioIpDscpCos':prioIpDscpCos,'prioIpDscpRestoreDefault':prioIpDscpRestoreDefault,'prioIpPortEnableStatus':prioIpPortEnableStatus,'prioIpPortTable':prioIpPortTable,'prioIpPortEntry':prioIpPortEntry,_AD:prioIpPortPhysPort,_AE:prioIpPortValue,'prioIpPortCos':prioIpPortCos,'prioIpPortStatus':prioIpPortStatus,'prioCopy':prioCopy,'prioCopyIpPrec':prioCopyIpPrec,'prioCopyIpDscp':prioCopyIpDscp,'prioCopyIpPort':prioCopyIpPort,'prioWrrTable':prioWrrTable,'prioWrrEntry':prioWrrEntry,_AF:prioWrrTrafficClass,'prioWrrWeight':prioWrrWeight,'trapDestMgt':trapDestMgt,'trapDestTable':trapDestTable,'trapDestEntry':trapDestEntry,_AG:trapDestAddress,'trapDestCommunity':trapDestCommunity,'trapDestStatus':trapDestStatus,'trapDestVersion':trapDestVersion,'securityMgt':securityMgt,'portSecurityMgt':portSecurityMgt,'portSecPortTable':portSecPortTable,'portSecPortEntry':portSecPortEntry,_AH:portSecPortIndex,'portSecPortStatus':portSecPortStatus,'portSecAction':portSecAction,'radiusMgt':radiusMgt,'radiusServerAddress':radiusServerAddress,'radiusServerPortNumber':radiusServerPortNumber,'radiusServerKey':radiusServerKey,'radiusServerRetransmit':radiusServerRetransmit,'radiusServerTimeout':radiusServerTimeout,'tacacsMgt':tacacsMgt,'tacacsServerAddress':tacacsServerAddress,'tacacsServerPortNumber':tacacsServerPortNumber,'tacacsServerKey':tacacsServerKey,'sshMgt':sshMgt,'sshServerStatus':sshServerStatus,'sshServerMajorVersion':sshServerMajorVersion,'sshServerMinorVersion':sshServerMinorVersion,'sshTimeout':sshTimeout,'sshAuthRetries':sshAuthRetries,'sshConnInfoTable':sshConnInfoTable,'sshConnInfoEntry':sshConnInfoEntry,_AI:sshConnID,'sshConnMajorVersion':sshConnMajorVersion,'sshConnMinorVersion':sshConnMinorVersion,'sshConnEncryptionType':sshConnEncryptionType,'sshConnStatus':sshConnStatus,'sshConnUserName':sshConnUserName,'sshDisconnect':sshDisconnect,'sysLogMgt':sysLogMgt,'sysLogStatus':sysLogStatus,'sysLogHistoryFlashLevel':sysLogHistoryFlashLevel,'sysLogHistoryRamLevel':sysLogHistoryRamLevel,'remoteLogMgt':remoteLogMgt,'remoteLogStatus':remoteLogStatus,'remoteLogLevel':remoteLogLevel,'remoteLogFacilityType':remoteLogFacilityType,'remoteLogServerTable':remoteLogServerTable,'remoteLogServerEntry':remoteLogServerEntry,_AJ:remoteLogServerIp,'remoteLogServerStatus':remoteLogServerStatus,'lineMgt':lineMgt,'consoleMgt':consoleMgt,'consoleDataBits':consoleDataBits,'consoleParity':consoleParity,'consoleBaudRate':consoleBaudRate,'consoleStopBits':consoleStopBits,'consoleExecTimeout':consoleExecTimeout,'consolePasswordThreshold':consolePasswordThreshold,'consoleSilentTime':consoleSilentTime,'telnetMgt':telnetMgt,'telnetExecTimeout':telnetExecTimeout,'telnetPasswordThreshold':telnetPasswordThreshold,'powerConnect3248Notifications':powerConnect3248Notifications,'powerConnect3248Traps':powerConnect3248Traps,'powerConnect3248TrapsPrefix':powerConnect3248TrapsPrefix,'swPowerStatusChangeTrap':swPowerStatusChangeTrap,'swPortSecurityTrap':swPortSecurityTrap,'powerConnect3248Conformance':powerConnect3248Conformance})