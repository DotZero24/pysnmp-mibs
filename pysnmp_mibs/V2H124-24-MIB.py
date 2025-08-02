_Aj='swIndivPowerStatus'
_Ai='staPortEntry'
_Ah='fileInfoFileName'
_Ag='fileInfoUnitID'
_Af='startUpCfg'
_Ae='runningCfg'
_Ad='sntpServerIndex'
_Ac='aclEgressMacMaskIndex'
_Ab='aclIngressMacMaskIndex'
_Aa='aclEgressIpMaskIndex'
_AZ='aclIngressIpMaskIndex'
_AY='aclAclGroupIfIndex'
_AX='aclMacAceIndex'
_AW='aclMacAceName'
_AV='aclIpAceIndex'
_AU='aclIpAceName'
_AT='sshConnID'
_AS='portSecPortIndex'
_AR='prioAclToCosMappingAclName'
_AQ='prioAclToCosMappingIfIndex'
_AP='markerAclName'
_AO='markerIfIndex'
_AN='rlPortIndex'
_AM='trapDestAddress'
_AL='prioWrrTrafficClass'
_AK='prioIpPortValue'
_AJ='prioIpPortPhysPort'
_AI='prioIpDscpValue'
_AH='prioIpDscpPort'
_AG='prioIpPrecValue'
_AF='prioIpPrecPort'
_AE='precedence'
_AD='vlanPortIndex'
_AC='vlanIndex'
_AB='bcastStormIfIndex'
_AA='netConfigSubnetMask'
_A9='netConfigIPAddress'
_A8='netConfigIfIndex'
_A7='igmpSnoopMulticastStaticIpAddress'
_A6='igmpSnoopMulticastStaticVlanIndex'
_A5='igmpSnoopMulticastCurrentIpAddress'
_A4='igmpSnoopMulticastCurrentVlanIndex'
_A3='igmpSnoopRouterStaticVlanIndex'
_A2='igmpSnoopRouterCurrentVlanIndex'
_A1='mirrorSourcePort'
_A0='mirrorDestinationPort'
_z='lacpPortIndex'
_y='trunkIndex'
_x='dot3xFlowControl'
_w='backPressure'
_v='fullDuplex1000'
_u='halfDuplex1000'
_t='fullDuplex100'
_s='halfDuplex100'
_r='fullDuplex10'
_q='halfDuplex10'
_p='portIndex'
_o='accessible-for-notify'
_n='tenHundredBaseT'
_m='comboStackingSfp'
_l='tenHundredBaseFxMtrj4port'
_k='tenHundredBaseT4port'
_j='stackingModule'
_i='thousandBaseLxScSmf'
_h='thousandBaseXGbic'
_g='thousandBaseSxMtrjMmf'
_f='thousandBaseSxScMmf'
_e='hundredBaseFxMtrjMmf'
_d='hundredBaseFxScSmf'
_c='hundredBaseFxScMmf'
_b='internalPower'
_a='v2h124swUnitIndex'
_Z='dot1dStpPort'
_Y='BRIDGE-MIB'
_X='xstInstanceCfgIndex'
_W='none'
_V='disabled'
_U='swIndivPowerIndex'
_T='swIndivPowerUnitIndex'
_S='thousandBaseSfp'
_R='thousandBaseT'
_Q='notPresent'
_P='Bits'
_O='range'
_N='equal'
_M='noOperator'
_L='other'
_K='EnabledStatus'
_J='Unsigned32'
_I='OctetString'
_H='DisplayString'
_G='not-accessible'
_F='V2H124-24-MIB'
_E='read-only'
_D='read-create'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
BridgeId,Timeout,dot1dStpPort,dot1dStpPortEntry=mibBuilder.importSymbols(_Y,'BridgeId','Timeout',_Z,'dot1dStpPortEntry')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB',_K)
PortList,=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI',_P,'Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_J,'enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','RowStatus','TextualConvention','TruthValue')
v2h124_24MIB=ModuleIdentity((1,3,6,1,4,1,52,4,12,30))
if mibBuilder.loadTexts:v2h124_24MIB.setRevisions(('2004-01-21 20:31','2003-12-12 17:04','2003-07-25 19:59','2003-07-18 21:42','2003-12-06 00:00'))
class ValidStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),('invalid',2)))
_V2h124_24MIBObjects_ObjectIdentity=ObjectIdentity
v2h124_24MIBObjects=_V2h124_24MIBObjects_ObjectIdentity((1,3,6,1,4,1,52,4,12,30,1))
_SwitchMgt_ObjectIdentity=ObjectIdentity
switchMgt=_SwitchMgt_ObjectIdentity((1,3,6,1,4,1,52,4,12,30,1,1))
class _SwitchManagementVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_SwitchManagementVlan_Type.__name__=_B
_SwitchManagementVlan_Object=MibScalar
switchManagementVlan=_SwitchManagementVlan_Object((1,3,6,1,4,1,52,4,12,30,1,1,1),_SwitchManagementVlan_Type())
switchManagementVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:switchManagementVlan.setStatus(_A)
_V2h124switchNumber_Type=Integer32
_V2h124switchNumber_Object=MibScalar
v2h124switchNumber=_V2h124switchNumber_Object((1,3,6,1,4,1,52,4,12,30,1,1,2),_V2h124switchNumber_Type())
v2h124switchNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:v2h124switchNumber.setStatus(_A)
_V2h124switchInfoTable_Object=MibTable
v2h124switchInfoTable=_V2h124switchInfoTable_Object((1,3,6,1,4,1,52,4,12,30,1,1,3))
if mibBuilder.loadTexts:v2h124switchInfoTable.setStatus(_A)
_V2h124switchInfoEntry_Object=MibTableRow
v2h124switchInfoEntry=_V2h124switchInfoEntry_Object((1,3,6,1,4,1,52,4,12,30,1,1,3,1))
v2h124switchInfoEntry.setIndexNames((0,_F,_a))
if mibBuilder.loadTexts:v2h124switchInfoEntry.setStatus(_A)
_V2h124swUnitIndex_Type=Integer32
_V2h124swUnitIndex_Object=MibTableColumn
v2h124swUnitIndex=_V2h124swUnitIndex_Object((1,3,6,1,4,1,52,4,12,30,1,1,3,1,1),_V2h124swUnitIndex_Type())
v2h124swUnitIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:v2h124swUnitIndex.setStatus(_A)
class _V2h124swHardwareVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_V2h124swHardwareVer_Type.__name__=_H
_V2h124swHardwareVer_Object=MibTableColumn
v2h124swHardwareVer=_V2h124swHardwareVer_Object((1,3,6,1,4,1,52,4,12,30,1,1,3,1,2),_V2h124swHardwareVer_Type())
v2h124swHardwareVer.setMaxAccess(_E)
if mibBuilder.loadTexts:v2h124swHardwareVer.setStatus(_A)
class _V2h124swMicrocodeVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_V2h124swMicrocodeVer_Type.__name__=_H
_V2h124swMicrocodeVer_Object=MibTableColumn
v2h124swMicrocodeVer=_V2h124swMicrocodeVer_Object((1,3,6,1,4,1,52,4,12,30,1,1,3,1,3),_V2h124swMicrocodeVer_Type())
v2h124swMicrocodeVer.setMaxAccess(_E)
if mibBuilder.loadTexts:v2h124swMicrocodeVer.setStatus(_A)
class _V2h124swLoaderVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_V2h124swLoaderVer_Type.__name__=_H
_V2h124swLoaderVer_Object=MibTableColumn
v2h124swLoaderVer=_V2h124swLoaderVer_Object((1,3,6,1,4,1,52,4,12,30,1,1,3,1,4),_V2h124swLoaderVer_Type())
v2h124swLoaderVer.setMaxAccess(_E)
if mibBuilder.loadTexts:v2h124swLoaderVer.setStatus(_A)
class _V2h124swBootRomVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_V2h124swBootRomVer_Type.__name__=_H
_V2h124swBootRomVer_Object=MibTableColumn
v2h124swBootRomVer=_V2h124swBootRomVer_Object((1,3,6,1,4,1,52,4,12,30,1,1,3,1,5),_V2h124swBootRomVer_Type())
v2h124swBootRomVer.setMaxAccess(_E)
if mibBuilder.loadTexts:v2h124swBootRomVer.setStatus(_A)
class _V2h124swOpCodeVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_V2h124swOpCodeVer_Type.__name__=_H
_V2h124swOpCodeVer_Object=MibTableColumn
v2h124swOpCodeVer=_V2h124swOpCodeVer_Object((1,3,6,1,4,1,52,4,12,30,1,1,3,1,6),_V2h124swOpCodeVer_Type())
v2h124swOpCodeVer.setMaxAccess(_E)
if mibBuilder.loadTexts:v2h124swOpCodeVer.setStatus(_A)
_V2h124swPortNumber_Type=Integer32
_V2h124swPortNumber_Object=MibTableColumn
v2h124swPortNumber=_V2h124swPortNumber_Object((1,3,6,1,4,1,52,4,12,30,1,1,3,1,7),_V2h124swPortNumber_Type())
v2h124swPortNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:v2h124swPortNumber.setStatus(_A)
class _V2h124swPowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_b,1),('redundantPower',2),('internalAndRedundantPower',3)))
_V2h124swPowerStatus_Type.__name__=_B
_V2h124swPowerStatus_Object=MibTableColumn
v2h124swPowerStatus=_V2h124swPowerStatus_Object((1,3,6,1,4,1,52,4,12,30,1,1,3,1,8),_V2h124swPowerStatus_Type())
v2h124swPowerStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:v2h124swPowerStatus.setStatus(_A)
class _V2h124swRoleInSystem_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('master',1),('backupMaster',2),('slave',3)))
_V2h124swRoleInSystem_Type.__name__=_B
_V2h124swRoleInSystem_Object=MibTableColumn
v2h124swRoleInSystem=_V2h124swRoleInSystem_Object((1,3,6,1,4,1,52,4,12,30,1,1,3,1,9),_V2h124swRoleInSystem_Type())
v2h124swRoleInSystem.setMaxAccess(_E)
if mibBuilder.loadTexts:v2h124swRoleInSystem.setStatus(_A)
class _V2h124swSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_V2h124swSerialNumber_Type.__name__=_H
_V2h124swSerialNumber_Object=MibTableColumn
v2h124swSerialNumber=_V2h124swSerialNumber_Object((1,3,6,1,4,1,52,4,12,30,1,1,3,1,10),_V2h124swSerialNumber_Type())
v2h124swSerialNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:v2h124swSerialNumber.setStatus(_A)
class _V2h124swExpansionSlot1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*((_Q,1),(_L,2),(_c,3),(_d,4),(_e,5),(_f,6),(_g,7),(_h,8),(_i,9),(_R,10),(_j,11),(_S,12),(_k,13),(_l,14),(_m,15),(_n,16)))
_V2h124swExpansionSlot1_Type.__name__=_B
_V2h124swExpansionSlot1_Object=MibTableColumn
v2h124swExpansionSlot1=_V2h124swExpansionSlot1_Object((1,3,6,1,4,1,52,4,12,30,1,1,3,1,11),_V2h124swExpansionSlot1_Type())
v2h124swExpansionSlot1.setMaxAccess(_E)
if mibBuilder.loadTexts:v2h124swExpansionSlot1.setStatus(_A)
class _V2h124swExpansionSlot2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*((_Q,1),(_L,2),(_c,3),(_d,4),(_e,5),(_f,6),(_g,7),(_h,8),(_i,9),(_R,10),(_j,11),(_S,12),(_k,13),(_l,14),(_m,15),(_n,16)))
_V2h124swExpansionSlot2_Type.__name__=_B
_V2h124swExpansionSlot2_Object=MibTableColumn
v2h124swExpansionSlot2=_V2h124swExpansionSlot2_Object((1,3,6,1,4,1,52,4,12,30,1,1,3,1,12),_V2h124swExpansionSlot2_Type())
v2h124swExpansionSlot2.setMaxAccess(_E)
if mibBuilder.loadTexts:v2h124swExpansionSlot2.setStatus(_A)
class _V2h124swServiceTag_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_V2h124swServiceTag_Type.__name__=_H
_V2h124swServiceTag_Object=MibTableColumn
v2h124swServiceTag=_V2h124swServiceTag_Object((1,3,6,1,4,1,52,4,12,30,1,1,3,1,13),_V2h124swServiceTag_Type())
v2h124swServiceTag.setMaxAccess(_E)
if mibBuilder.loadTexts:v2h124swServiceTag.setStatus(_A)
class _SwitchOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_L,1),('unknown',2),('ok',3),('noncritical',4),('critical',5),('nonrecoverable',6)))
_SwitchOperState_Type.__name__=_B
_SwitchOperState_Object=MibScalar
switchOperState=_SwitchOperState_Object((1,3,6,1,4,1,52,4,12,30,1,1,4),_SwitchOperState_Type())
switchOperState.setMaxAccess(_E)
if mibBuilder.loadTexts:switchOperState.setStatus(_A)
_SwitchProductId_ObjectIdentity=ObjectIdentity
switchProductId=_SwitchProductId_ObjectIdentity((1,3,6,1,4,1,52,4,12,30,1,1,5))
class _SwProdName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_SwProdName_Type.__name__=_H
_SwProdName_Object=MibScalar
swProdName=_SwProdName_Object((1,3,6,1,4,1,52,4,12,30,1,1,5,1),_SwProdName_Type())
swProdName.setMaxAccess(_E)
if mibBuilder.loadTexts:swProdName.setStatus(_A)
class _SwProdManufacturer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_SwProdManufacturer_Type.__name__=_H
_SwProdManufacturer_Object=MibScalar
swProdManufacturer=_SwProdManufacturer_Object((1,3,6,1,4,1,52,4,12,30,1,1,5,2),_SwProdManufacturer_Type())
swProdManufacturer.setMaxAccess(_E)
if mibBuilder.loadTexts:swProdManufacturer.setStatus(_A)
class _SwProdDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_SwProdDescription_Type.__name__=_H
_SwProdDescription_Object=MibScalar
swProdDescription=_SwProdDescription_Object((1,3,6,1,4,1,52,4,12,30,1,1,5,3),_SwProdDescription_Type())
swProdDescription.setMaxAccess(_E)
if mibBuilder.loadTexts:swProdDescription.setStatus(_A)
class _SwProdVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_SwProdVersion_Type.__name__=_H
_SwProdVersion_Object=MibScalar
swProdVersion=_SwProdVersion_Object((1,3,6,1,4,1,52,4,12,30,1,1,5,4),_SwProdVersion_Type())
swProdVersion.setMaxAccess(_E)
if mibBuilder.loadTexts:swProdVersion.setStatus(_A)
class _SwProdUrl_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_SwProdUrl_Type.__name__=_H
_SwProdUrl_Object=MibScalar
swProdUrl=_SwProdUrl_Object((1,3,6,1,4,1,52,4,12,30,1,1,5,5),_SwProdUrl_Type())
swProdUrl.setMaxAccess(_E)
if mibBuilder.loadTexts:swProdUrl.setStatus(_A)
_SwIdentifier_Type=Integer32
_SwIdentifier_Object=MibScalar
swIdentifier=_SwIdentifier_Object((1,3,6,1,4,1,52,4,12,30,1,1,5,6),_SwIdentifier_Type())
swIdentifier.setMaxAccess(_E)
if mibBuilder.loadTexts:swIdentifier.setStatus(_A)
class _SwChassisServiceTag_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_SwChassisServiceTag_Type.__name__=_H
_SwChassisServiceTag_Object=MibScalar
swChassisServiceTag=_SwChassisServiceTag_Object((1,3,6,1,4,1,52,4,12,30,1,1,5,7),_SwChassisServiceTag_Type())
swChassisServiceTag.setMaxAccess(_E)
if mibBuilder.loadTexts:swChassisServiceTag.setStatus(_A)
_SwitchIndivPowerTable_Object=MibTable
switchIndivPowerTable=_SwitchIndivPowerTable_Object((1,3,6,1,4,1,52,4,12,30,1,1,6))
if mibBuilder.loadTexts:switchIndivPowerTable.setStatus(_A)
_SwitchIndivPowerEntry_Object=MibTableRow
switchIndivPowerEntry=_SwitchIndivPowerEntry_Object((1,3,6,1,4,1,52,4,12,30,1,1,6,1))
switchIndivPowerEntry.setIndexNames((0,_F,_T),(0,_F,_U))
if mibBuilder.loadTexts:switchIndivPowerEntry.setStatus(_A)
_SwIndivPowerUnitIndex_Type=Integer32
_SwIndivPowerUnitIndex_Object=MibTableColumn
swIndivPowerUnitIndex=_SwIndivPowerUnitIndex_Object((1,3,6,1,4,1,52,4,12,30,1,1,6,1,1),_SwIndivPowerUnitIndex_Type())
swIndivPowerUnitIndex.setMaxAccess(_o)
if mibBuilder.loadTexts:swIndivPowerUnitIndex.setStatus(_A)
class _SwIndivPowerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_b,1),('externalPower',2)))
_SwIndivPowerIndex_Type.__name__=_B
_SwIndivPowerIndex_Object=MibTableColumn
swIndivPowerIndex=_SwIndivPowerIndex_Object((1,3,6,1,4,1,52,4,12,30,1,1,6,1,2),_SwIndivPowerIndex_Type())
swIndivPowerIndex.setMaxAccess(_o)
if mibBuilder.loadTexts:swIndivPowerIndex.setStatus(_A)
class _SwIndivPowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Q,1),('green',2),('red',3)))
_SwIndivPowerStatus_Type.__name__=_B
_SwIndivPowerStatus_Object=MibTableColumn
swIndivPowerStatus=_SwIndivPowerStatus_Object((1,3,6,1,4,1,52,4,12,30,1,1,6,1,3),_SwIndivPowerStatus_Type())
swIndivPowerStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:swIndivPowerStatus.setStatus(_A)
_PortMgt_ObjectIdentity=ObjectIdentity
portMgt=_PortMgt_ObjectIdentity((1,3,6,1,4,1,52,4,12,30,1,2))
_PortTable_Object=MibTable
portTable=_PortTable_Object((1,3,6,1,4,1,52,4,12,30,1,2,1))
if mibBuilder.loadTexts:portTable.setStatus(_A)
_PortEntry_Object=MibTableRow
portEntry=_PortEntry_Object((1,3,6,1,4,1,52,4,12,30,1,2,1,1))
portEntry.setIndexNames((0,_F,_p))
if mibBuilder.loadTexts:portEntry.setStatus(_A)
_PortIndex_Type=Integer32
_PortIndex_Object=MibTableColumn
portIndex=_PortIndex_Object((1,3,6,1,4,1,52,4,12,30,1,2,1,1,1),_PortIndex_Type())
portIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:portIndex.setStatus(_A)
class _PortName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_PortName_Type.__name__=_H
_PortName_Object=MibTableColumn
portName=_PortName_Object((1,3,6,1,4,1,52,4,12,30,1,2,1,1,2),_PortName_Type())
portName.setMaxAccess(_C)
if mibBuilder.loadTexts:portName.setStatus(_A)
class _PortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_L,1),('hundredBaseTX',2),('hundredBaseFX',3),('thousandBaseSX',4),('thousandBaseLX',5),(_R,6),('thousandBaseGBIC',7),(_S,8),('hundredBaseFxScSingleMode',9),('hundredBaseFxScMultiMode',10)))
_PortType_Type.__name__=_B
_PortType_Object=MibTableColumn
portType=_PortType_Object((1,3,6,1,4,1,52,4,12,30,1,2,1,1,3),_PortType_Type())
portType.setMaxAccess(_E)
if mibBuilder.loadTexts:portType.setStatus(_A)
class _PortSpeedDpxCfg_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('reserved',1),(_q,2),(_r,3),(_s,4),(_t,5),(_u,6),(_v,7)))
_PortSpeedDpxCfg_Type.__name__=_B
_PortSpeedDpxCfg_Object=MibTableColumn
portSpeedDpxCfg=_PortSpeedDpxCfg_Object((1,3,6,1,4,1,52,4,12,30,1,2,1,1,4),_PortSpeedDpxCfg_Type())
portSpeedDpxCfg.setMaxAccess(_C)
if mibBuilder.loadTexts:portSpeedDpxCfg.setStatus(_A)
class _PortFlowCtrlCfg_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('enabled',1),(_V,2),(_w,3),(_x,4)))
_PortFlowCtrlCfg_Type.__name__=_B
_PortFlowCtrlCfg_Object=MibTableColumn
portFlowCtrlCfg=_PortFlowCtrlCfg_Object((1,3,6,1,4,1,52,4,12,30,1,2,1,1,5),_PortFlowCtrlCfg_Type())
portFlowCtrlCfg.setMaxAccess(_C)
if mibBuilder.loadTexts:portFlowCtrlCfg.setStatus(_A)
class _PortCapabilities_Type(Bits):namedValues=NamedValues(*(('portCap10half',0),('portCap10full',1),('portCap100half',2),('portCap100full',3),('portCap1000half',4),('portCap1000full',5),('reserved6',6),('reserved7',7),('reserved8',8),('reserved9',9),('reserved10',10),('reserved11',11),('reserved12',12),('reserved13',13),('portCapSym',14),('portCapFlowCtrl',15)))
_PortCapabilities_Type.__name__=_P
_PortCapabilities_Object=MibTableColumn
portCapabilities=_PortCapabilities_Object((1,3,6,1,4,1,52,4,12,30,1,2,1,1,6),_PortCapabilities_Type())
portCapabilities.setMaxAccess(_C)
if mibBuilder.loadTexts:portCapabilities.setStatus(_A)
_PortAutonegotiation_Type=EnabledStatus
_PortAutonegotiation_Object=MibTableColumn
portAutonegotiation=_PortAutonegotiation_Object((1,3,6,1,4,1,52,4,12,30,1,2,1,1,7),_PortAutonegotiation_Type())
portAutonegotiation.setMaxAccess(_C)
if mibBuilder.loadTexts:portAutonegotiation.setStatus(_A)
class _PortSpeedDpxStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('error',1),(_q,2),(_r,3),(_s,4),(_t,5),(_u,6),(_v,7)))
_PortSpeedDpxStatus_Type.__name__=_B
_PortSpeedDpxStatus_Object=MibTableColumn
portSpeedDpxStatus=_PortSpeedDpxStatus_Object((1,3,6,1,4,1,52,4,12,30,1,2,1,1,8),_PortSpeedDpxStatus_Type())
portSpeedDpxStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:portSpeedDpxStatus.setStatus(_A)
class _PortFlowCtrlStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('error',1),(_w,2),(_x,3),(_W,4)))
_PortFlowCtrlStatus_Type.__name__=_B
_PortFlowCtrlStatus_Object=MibTableColumn
portFlowCtrlStatus=_PortFlowCtrlStatus_Object((1,3,6,1,4,1,52,4,12,30,1,2,1,1,9),_PortFlowCtrlStatus_Type())
portFlowCtrlStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:portFlowCtrlStatus.setStatus(_A)
_PortTrunkIndex_Type=Integer32
_PortTrunkIndex_Object=MibTableColumn
portTrunkIndex=_PortTrunkIndex_Object((1,3,6,1,4,1,52,4,12,30,1,2,1,1,10),_PortTrunkIndex_Type())
portTrunkIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:portTrunkIndex.setStatus(_A)
_TrunkMgt_ObjectIdentity=ObjectIdentity
trunkMgt=_TrunkMgt_ObjectIdentity((1,3,6,1,4,1,52,4,12,30,1,3))
_TrunkMaxId_Type=Integer32
_TrunkMaxId_Object=MibScalar
trunkMaxId=_TrunkMaxId_Object((1,3,6,1,4,1,52,4,12,30,1,3,1),_TrunkMaxId_Type())
trunkMaxId.setMaxAccess(_E)
if mibBuilder.loadTexts:trunkMaxId.setStatus(_A)
_TrunkValidNumber_Type=Integer32
_TrunkValidNumber_Object=MibScalar
trunkValidNumber=_TrunkValidNumber_Object((1,3,6,1,4,1,52,4,12,30,1,3,2),_TrunkValidNumber_Type())
trunkValidNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:trunkValidNumber.setStatus(_A)
_TrunkTable_Object=MibTable
trunkTable=_TrunkTable_Object((1,3,6,1,4,1,52,4,12,30,1,3,3))
if mibBuilder.loadTexts:trunkTable.setStatus(_A)
_TrunkEntry_Object=MibTableRow
trunkEntry=_TrunkEntry_Object((1,3,6,1,4,1,52,4,12,30,1,3,3,1))
trunkEntry.setIndexNames((0,_F,_y))
if mibBuilder.loadTexts:trunkEntry.setStatus(_A)
_TrunkIndex_Type=Integer32
_TrunkIndex_Object=MibTableColumn
trunkIndex=_TrunkIndex_Object((1,3,6,1,4,1,52,4,12,30,1,3,3,1,1),_TrunkIndex_Type())
trunkIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:trunkIndex.setStatus(_A)
_TrunkPorts_Type=PortList
_TrunkPorts_Object=MibTableColumn
trunkPorts=_TrunkPorts_Object((1,3,6,1,4,1,52,4,12,30,1,3,3,1,2),_TrunkPorts_Type())
trunkPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:trunkPorts.setStatus(_A)
class _TrunkCreation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('static',1),('lacp',2)))
_TrunkCreation_Type.__name__=_B
_TrunkCreation_Object=MibTableColumn
trunkCreation=_TrunkCreation_Object((1,3,6,1,4,1,52,4,12,30,1,3,3,1,3),_TrunkCreation_Type())
trunkCreation.setMaxAccess(_E)
if mibBuilder.loadTexts:trunkCreation.setStatus(_A)
_TrunkStatus_Type=ValidStatus
_TrunkStatus_Object=MibTableColumn
trunkStatus=_TrunkStatus_Object((1,3,6,1,4,1,52,4,12,30,1,3,3,1,4),_TrunkStatus_Type())
trunkStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:trunkStatus.setStatus(_A)
_LacpMgt_ObjectIdentity=ObjectIdentity
lacpMgt=_LacpMgt_ObjectIdentity((1,3,6,1,4,1,52,4,12,30,1,4))
_LacpPortTable_Object=MibTable
lacpPortTable=_LacpPortTable_Object((1,3,6,1,4,1,52,4,12,30,1,4,1))
if mibBuilder.loadTexts:lacpPortTable.setStatus(_A)
_LacpPortEntry_Object=MibTableRow
lacpPortEntry=_LacpPortEntry_Object((1,3,6,1,4,1,52,4,12,30,1,4,1,1))
lacpPortEntry.setIndexNames((0,_F,_z))
if mibBuilder.loadTexts:lacpPortEntry.setStatus(_A)
_LacpPortIndex_Type=Integer32
_LacpPortIndex_Object=MibTableColumn
lacpPortIndex=_LacpPortIndex_Object((1,3,6,1,4,1,52,4,12,30,1,4,1,1,1),_LacpPortIndex_Type())
lacpPortIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:lacpPortIndex.setStatus(_A)
_LacpPortStatus_Type=EnabledStatus
_LacpPortStatus_Object=MibTableColumn
lacpPortStatus=_LacpPortStatus_Object((1,3,6,1,4,1,52,4,12,30,1,4,1,1,2),_LacpPortStatus_Type())
lacpPortStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:lacpPortStatus.setStatus(_A)
_StaMgt_ObjectIdentity=ObjectIdentity
staMgt=_StaMgt_ObjectIdentity((1,3,6,1,4,1,52,4,12,30,1,5))
class _StaSystemStatus_Type(EnabledStatus):defaultValue=1
_StaSystemStatus_Type.__name__=_K
_StaSystemStatus_Object=MibScalar
staSystemStatus=_StaSystemStatus_Object((1,3,6,1,4,1,52,4,12,30,1,5,1),_StaSystemStatus_Type())
staSystemStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:staSystemStatus.setStatus(_A)
_StaPortTable_Object=MibTable
staPortTable=_StaPortTable_Object((1,3,6,1,4,1,52,4,12,30,1,5,2))
if mibBuilder.loadTexts:staPortTable.setStatus(_A)
_StaPortEntry_Object=MibTableRow
staPortEntry=_StaPortEntry_Object((1,3,6,1,4,1,52,4,12,30,1,5,2,1))
if mibBuilder.loadTexts:staPortEntry.setStatus(_A)
_StaPortFastForward_Type=EnabledStatus
_StaPortFastForward_Object=MibTableColumn
staPortFastForward=_StaPortFastForward_Object((1,3,6,1,4,1,52,4,12,30,1,5,2,1,2),_StaPortFastForward_Type())
staPortFastForward.setMaxAccess(_C)
if mibBuilder.loadTexts:staPortFastForward.setStatus(_A)
_StaPortProtocolMigration_Type=TruthValue
_StaPortProtocolMigration_Object=MibTableColumn
staPortProtocolMigration=_StaPortProtocolMigration_Object((1,3,6,1,4,1,52,4,12,30,1,5,2,1,3),_StaPortProtocolMigration_Type())
staPortProtocolMigration.setMaxAccess(_C)
if mibBuilder.loadTexts:staPortProtocolMigration.setStatus(_A)
_StaPortAdminEdgePort_Type=TruthValue
_StaPortAdminEdgePort_Object=MibTableColumn
staPortAdminEdgePort=_StaPortAdminEdgePort_Object((1,3,6,1,4,1,52,4,12,30,1,5,2,1,4),_StaPortAdminEdgePort_Type())
staPortAdminEdgePort.setMaxAccess(_C)
if mibBuilder.loadTexts:staPortAdminEdgePort.setStatus(_A)
_StaPortOperEdgePort_Type=TruthValue
_StaPortOperEdgePort_Object=MibTableColumn
staPortOperEdgePort=_StaPortOperEdgePort_Object((1,3,6,1,4,1,52,4,12,30,1,5,2,1,5),_StaPortOperEdgePort_Type())
staPortOperEdgePort.setMaxAccess(_E)
if mibBuilder.loadTexts:staPortOperEdgePort.setStatus(_A)
class _StaPortAdminPointToPoint_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('forceTrue',0),('forceFalse',1),('auto',2)))
_StaPortAdminPointToPoint_Type.__name__=_B
_StaPortAdminPointToPoint_Object=MibTableColumn
staPortAdminPointToPoint=_StaPortAdminPointToPoint_Object((1,3,6,1,4,1,52,4,12,30,1,5,2,1,6),_StaPortAdminPointToPoint_Type())
staPortAdminPointToPoint.setMaxAccess(_C)
if mibBuilder.loadTexts:staPortAdminPointToPoint.setStatus(_A)
_StaPortOperPointToPoint_Type=TruthValue
_StaPortOperPointToPoint_Object=MibTableColumn
staPortOperPointToPoint=_StaPortOperPointToPoint_Object((1,3,6,1,4,1,52,4,12,30,1,5,2,1,7),_StaPortOperPointToPoint_Type())
staPortOperPointToPoint.setMaxAccess(_E)
if mibBuilder.loadTexts:staPortOperPointToPoint.setStatus(_A)
class _StaPortLongPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,200000000))
_StaPortLongPathCost_Type.__name__=_B
_StaPortLongPathCost_Object=MibTableColumn
staPortLongPathCost=_StaPortLongPathCost_Object((1,3,6,1,4,1,52,4,12,30,1,5,2,1,8),_StaPortLongPathCost_Type())
staPortLongPathCost.setMaxAccess(_C)
if mibBuilder.loadTexts:staPortLongPathCost.setStatus(_A)
class _StaProtocolType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('stp',1),('rstp',2)))
_StaProtocolType_Type.__name__=_B
_StaProtocolType_Object=MibScalar
staProtocolType=_StaProtocolType_Object((1,3,6,1,4,1,52,4,12,30,1,5,3),_StaProtocolType_Type())
staProtocolType.setMaxAccess(_C)
if mibBuilder.loadTexts:staProtocolType.setStatus(_A)
class _StaTxHoldCount_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_StaTxHoldCount_Type.__name__=_B
_StaTxHoldCount_Object=MibScalar
staTxHoldCount=_StaTxHoldCount_Object((1,3,6,1,4,1,52,4,12,30,1,5,4),_StaTxHoldCount_Type())
staTxHoldCount.setMaxAccess(_C)
if mibBuilder.loadTexts:staTxHoldCount.setStatus(_A)
class _StaPathCostMethod_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('short',1),('long',2)))
_StaPathCostMethod_Type.__name__=_B
_StaPathCostMethod_Object=MibScalar
staPathCostMethod=_StaPathCostMethod_Object((1,3,6,1,4,1,52,4,12,30,1,5,5),_StaPathCostMethod_Type())
staPathCostMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:staPathCostMethod.setStatus(_A)
_XstMgt_ObjectIdentity=ObjectIdentity
xstMgt=_XstMgt_ObjectIdentity((1,3,6,1,4,1,52,4,12,30,1,5,6))
_XstInstanceCfgTable_Object=MibTable
xstInstanceCfgTable=_XstInstanceCfgTable_Object((1,3,6,1,4,1,52,4,12,30,1,5,6,4))
if mibBuilder.loadTexts:xstInstanceCfgTable.setStatus(_A)
_XstInstanceCfgEntry_Object=MibTableRow
xstInstanceCfgEntry=_XstInstanceCfgEntry_Object((1,3,6,1,4,1,52,4,12,30,1,5,6,4,1))
xstInstanceCfgEntry.setIndexNames((0,_F,_X))
if mibBuilder.loadTexts:xstInstanceCfgEntry.setStatus(_A)
class _XstInstanceCfgIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_XstInstanceCfgIndex_Type.__name__=_B
_XstInstanceCfgIndex_Object=MibTableColumn
xstInstanceCfgIndex=_XstInstanceCfgIndex_Object((1,3,6,1,4,1,52,4,12,30,1,5,6,4,1,1),_XstInstanceCfgIndex_Type())
xstInstanceCfgIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:xstInstanceCfgIndex.setStatus(_A)
class _XstInstanceCfgPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,61440))
_XstInstanceCfgPriority_Type.__name__=_B
_XstInstanceCfgPriority_Object=MibTableColumn
xstInstanceCfgPriority=_XstInstanceCfgPriority_Object((1,3,6,1,4,1,52,4,12,30,1,5,6,4,1,2),_XstInstanceCfgPriority_Type())
xstInstanceCfgPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:xstInstanceCfgPriority.setStatus(_A)
_XstInstanceCfgTimeSinceTopologyChange_Type=Integer32
_XstInstanceCfgTimeSinceTopologyChange_Object=MibTableColumn
xstInstanceCfgTimeSinceTopologyChange=_XstInstanceCfgTimeSinceTopologyChange_Object((1,3,6,1,4,1,52,4,12,30,1,5,6,4,1,3),_XstInstanceCfgTimeSinceTopologyChange_Type())
xstInstanceCfgTimeSinceTopologyChange.setMaxAccess(_E)
if mibBuilder.loadTexts:xstInstanceCfgTimeSinceTopologyChange.setStatus(_A)
_XstInstanceCfgTopChanges_Type=Integer32
_XstInstanceCfgTopChanges_Object=MibTableColumn
xstInstanceCfgTopChanges=_XstInstanceCfgTopChanges_Object((1,3,6,1,4,1,52,4,12,30,1,5,6,4,1,4),_XstInstanceCfgTopChanges_Type())
xstInstanceCfgTopChanges.setMaxAccess(_E)
if mibBuilder.loadTexts:xstInstanceCfgTopChanges.setStatus(_A)
_XstInstanceCfgDesignatedRoot_Type=BridgeId
_XstInstanceCfgDesignatedRoot_Object=MibTableColumn
xstInstanceCfgDesignatedRoot=_XstInstanceCfgDesignatedRoot_Object((1,3,6,1,4,1,52,4,12,30,1,5,6,4,1,5),_XstInstanceCfgDesignatedRoot_Type())
xstInstanceCfgDesignatedRoot.setMaxAccess(_E)
if mibBuilder.loadTexts:xstInstanceCfgDesignatedRoot.setStatus(_A)
_XstInstanceCfgRootCost_Type=Integer32
_XstInstanceCfgRootCost_Object=MibTableColumn
xstInstanceCfgRootCost=_XstInstanceCfgRootCost_Object((1,3,6,1,4,1,52,4,12,30,1,5,6,4,1,6),_XstInstanceCfgRootCost_Type())
xstInstanceCfgRootCost.setMaxAccess(_E)
if mibBuilder.loadTexts:xstInstanceCfgRootCost.setStatus(_A)
_XstInstanceCfgRootPort_Type=Integer32
_XstInstanceCfgRootPort_Object=MibTableColumn
xstInstanceCfgRootPort=_XstInstanceCfgRootPort_Object((1,3,6,1,4,1,52,4,12,30,1,5,6,4,1,7),_XstInstanceCfgRootPort_Type())
xstInstanceCfgRootPort.setMaxAccess(_E)
if mibBuilder.loadTexts:xstInstanceCfgRootPort.setStatus(_A)
_XstInstanceCfgMaxAge_Type=Timeout
_XstInstanceCfgMaxAge_Object=MibTableColumn
xstInstanceCfgMaxAge=_XstInstanceCfgMaxAge_Object((1,3,6,1,4,1,52,4,12,30,1,5,6,4,1,8),_XstInstanceCfgMaxAge_Type())
xstInstanceCfgMaxAge.setMaxAccess(_E)
if mibBuilder.loadTexts:xstInstanceCfgMaxAge.setStatus(_A)
_XstInstanceCfgHelloTime_Type=Timeout
_XstInstanceCfgHelloTime_Object=MibTableColumn
xstInstanceCfgHelloTime=_XstInstanceCfgHelloTime_Object((1,3,6,1,4,1,52,4,12,30,1,5,6,4,1,9),_XstInstanceCfgHelloTime_Type())
xstInstanceCfgHelloTime.setMaxAccess(_E)
if mibBuilder.loadTexts:xstInstanceCfgHelloTime.setStatus(_A)
_XstInstanceCfgHoldTime_Type=Timeout
_XstInstanceCfgHoldTime_Object=MibTableColumn
xstInstanceCfgHoldTime=_XstInstanceCfgHoldTime_Object((1,3,6,1,4,1,52,4,12,30,1,5,6,4,1,10),_XstInstanceCfgHoldTime_Type())
xstInstanceCfgHoldTime.setMaxAccess(_E)
if mibBuilder.loadTexts:xstInstanceCfgHoldTime.setStatus(_A)
_XstInstanceCfgForwardDelay_Type=Timeout
_XstInstanceCfgForwardDelay_Object=MibTableColumn
xstInstanceCfgForwardDelay=_XstInstanceCfgForwardDelay_Object((1,3,6,1,4,1,52,4,12,30,1,5,6,4,1,11),_XstInstanceCfgForwardDelay_Type())
xstInstanceCfgForwardDelay.setMaxAccess(_E)
if mibBuilder.loadTexts:xstInstanceCfgForwardDelay.setStatus(_A)
_XstInstanceCfgBridgeMaxAge_Type=Timeout
_XstInstanceCfgBridgeMaxAge_Object=MibTableColumn
xstInstanceCfgBridgeMaxAge=_XstInstanceCfgBridgeMaxAge_Object((1,3,6,1,4,1,52,4,12,30,1,5,6,4,1,12),_XstInstanceCfgBridgeMaxAge_Type())
xstInstanceCfgBridgeMaxAge.setMaxAccess(_E)
if mibBuilder.loadTexts:xstInstanceCfgBridgeMaxAge.setStatus(_A)
_XstInstanceCfgBridgeHelloTime_Type=Timeout
_XstInstanceCfgBridgeHelloTime_Object=MibTableColumn
xstInstanceCfgBridgeHelloTime=_XstInstanceCfgBridgeHelloTime_Object((1,3,6,1,4,1,52,4,12,30,1,5,6,4,1,13),_XstInstanceCfgBridgeHelloTime_Type())
xstInstanceCfgBridgeHelloTime.setMaxAccess(_E)
if mibBuilder.loadTexts:xstInstanceCfgBridgeHelloTime.setStatus(_A)
_XstInstanceCfgBridgeForwardDelay_Type=Timeout
_XstInstanceCfgBridgeForwardDelay_Object=MibTableColumn
xstInstanceCfgBridgeForwardDelay=_XstInstanceCfgBridgeForwardDelay_Object((1,3,6,1,4,1,52,4,12,30,1,5,6,4,1,14),_XstInstanceCfgBridgeForwardDelay_Type())
xstInstanceCfgBridgeForwardDelay.setMaxAccess(_E)
if mibBuilder.loadTexts:xstInstanceCfgBridgeForwardDelay.setStatus(_A)
_XstInstanceCfgTxHoldCount_Type=Integer32
_XstInstanceCfgTxHoldCount_Object=MibTableColumn
xstInstanceCfgTxHoldCount=_XstInstanceCfgTxHoldCount_Object((1,3,6,1,4,1,52,4,12,30,1,5,6,4,1,15),_XstInstanceCfgTxHoldCount_Type())
xstInstanceCfgTxHoldCount.setMaxAccess(_E)
if mibBuilder.loadTexts:xstInstanceCfgTxHoldCount.setStatus(_A)
class _XstInstanceCfgPathCostMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('short',1),('long',2)))
_XstInstanceCfgPathCostMethod_Type.__name__=_B
_XstInstanceCfgPathCostMethod_Object=MibTableColumn
xstInstanceCfgPathCostMethod=_XstInstanceCfgPathCostMethod_Object((1,3,6,1,4,1,52,4,12,30,1,5,6,4,1,16),_XstInstanceCfgPathCostMethod_Type())
xstInstanceCfgPathCostMethod.setMaxAccess(_E)
if mibBuilder.loadTexts:xstInstanceCfgPathCostMethod.setStatus(_A)
_XstInstancePortTable_Object=MibTable
xstInstancePortTable=_XstInstancePortTable_Object((1,3,6,1,4,1,52,4,12,30,1,5,6,5))
if mibBuilder.loadTexts:xstInstancePortTable.setStatus(_A)
_XstInstancePortEntry_Object=MibTableRow
xstInstancePortEntry=_XstInstancePortEntry_Object((1,3,6,1,4,1,52,4,12,30,1,5,6,5,1))
xstInstancePortEntry.setIndexNames((0,_F,_X),(0,_Y,_Z))
if mibBuilder.loadTexts:xstInstancePortEntry.setStatus(_A)
class _XstInstancePortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,240))
_XstInstancePortPriority_Type.__name__=_B
_XstInstancePortPriority_Object=MibTableColumn
xstInstancePortPriority=_XstInstancePortPriority_Object((1,3,6,1,4,1,52,4,12,30,1,5,6,5,1,3),_XstInstancePortPriority_Type())
xstInstancePortPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:xstInstancePortPriority.setStatus(_A)
class _XstInstancePortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('discarding',1),('learning',2),('forwarding',3)))
_XstInstancePortState_Type.__name__=_B
_XstInstancePortState_Object=MibTableColumn
xstInstancePortState=_XstInstancePortState_Object((1,3,6,1,4,1,52,4,12,30,1,5,6,5,1,4),_XstInstancePortState_Type())
xstInstancePortState.setMaxAccess(_E)
if mibBuilder.loadTexts:xstInstancePortState.setStatus(_A)
_XstInstancePortEnable_Type=EnabledStatus
_XstInstancePortEnable_Object=MibTableColumn
xstInstancePortEnable=_XstInstancePortEnable_Object((1,3,6,1,4,1,52,4,12,30,1,5,6,5,1,5),_XstInstancePortEnable_Type())
xstInstancePortEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:xstInstancePortEnable.setStatus(_A)
class _XstInstancePortPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,200000000))
_XstInstancePortPathCost_Type.__name__=_B
_XstInstancePortPathCost_Object=MibTableColumn
xstInstancePortPathCost=_XstInstancePortPathCost_Object((1,3,6,1,4,1,52,4,12,30,1,5,6,5,1,6),_XstInstancePortPathCost_Type())
xstInstancePortPathCost.setMaxAccess(_C)
if mibBuilder.loadTexts:xstInstancePortPathCost.setStatus(_A)
_XstInstancePortDesignatedRoot_Type=BridgeId
_XstInstancePortDesignatedRoot_Object=MibTableColumn
xstInstancePortDesignatedRoot=_XstInstancePortDesignatedRoot_Object((1,3,6,1,4,1,52,4,12,30,1,5,6,5,1,7),_XstInstancePortDesignatedRoot_Type())
xstInstancePortDesignatedRoot.setMaxAccess(_E)
if mibBuilder.loadTexts:xstInstancePortDesignatedRoot.setStatus(_A)
_XstInstancePortDesignatedCost_Type=Integer32
_XstInstancePortDesignatedCost_Object=MibTableColumn
xstInstancePortDesignatedCost=_XstInstancePortDesignatedCost_Object((1,3,6,1,4,1,52,4,12,30,1,5,6,5,1,8),_XstInstancePortDesignatedCost_Type())
xstInstancePortDesignatedCost.setMaxAccess(_E)
if mibBuilder.loadTexts:xstInstancePortDesignatedCost.setStatus(_A)
_XstInstancePortDesignatedBridge_Type=BridgeId
_XstInstancePortDesignatedBridge_Object=MibTableColumn
xstInstancePortDesignatedBridge=_XstInstancePortDesignatedBridge_Object((1,3,6,1,4,1,52,4,12,30,1,5,6,5,1,9),_XstInstancePortDesignatedBridge_Type())
xstInstancePortDesignatedBridge.setMaxAccess(_E)
if mibBuilder.loadTexts:xstInstancePortDesignatedBridge.setStatus(_A)
class _XstInstancePortDesignatedPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_XstInstancePortDesignatedPort_Type.__name__=_I
_XstInstancePortDesignatedPort_Object=MibTableColumn
xstInstancePortDesignatedPort=_XstInstancePortDesignatedPort_Object((1,3,6,1,4,1,52,4,12,30,1,5,6,5,1,10),_XstInstancePortDesignatedPort_Type())
xstInstancePortDesignatedPort.setMaxAccess(_E)
if mibBuilder.loadTexts:xstInstancePortDesignatedPort.setStatus(_A)
_XstInstancePortForwardTransitions_Type=Counter32
_XstInstancePortForwardTransitions_Object=MibTableColumn
xstInstancePortForwardTransitions=_XstInstancePortForwardTransitions_Object((1,3,6,1,4,1,52,4,12,30,1,5,6,5,1,11),_XstInstancePortForwardTransitions_Type())
xstInstancePortForwardTransitions.setMaxAccess(_E)
if mibBuilder.loadTexts:xstInstancePortForwardTransitions.setStatus(_A)
class _XstInstancePortPortRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_V,1),('root',2),('designated',3),('alternate',4),('backup',5)))
_XstInstancePortPortRole_Type.__name__=_B
_XstInstancePortPortRole_Object=MibTableColumn
xstInstancePortPortRole=_XstInstancePortPortRole_Object((1,3,6,1,4,1,52,4,12,30,1,5,6,5,1,12),_XstInstancePortPortRole_Type())
xstInstancePortPortRole.setMaxAccess(_E)
if mibBuilder.loadTexts:xstInstancePortPortRole.setStatus(_A)
_RestartMgt_ObjectIdentity=ObjectIdentity
restartMgt=_RestartMgt_ObjectIdentity((1,3,6,1,4,1,52,4,12,30,1,7))
class _RestartOpCodeFile_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_RestartOpCodeFile_Type.__name__=_H
_RestartOpCodeFile_Object=MibScalar
restartOpCodeFile=_RestartOpCodeFile_Object((1,3,6,1,4,1,52,4,12,30,1,7,1),_RestartOpCodeFile_Type())
restartOpCodeFile.setMaxAccess(_C)
if mibBuilder.loadTexts:restartOpCodeFile.setStatus(_A)
class _RestartConfigFile_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_RestartConfigFile_Type.__name__=_H
_RestartConfigFile_Object=MibScalar
restartConfigFile=_RestartConfigFile_Object((1,3,6,1,4,1,52,4,12,30,1,7,2),_RestartConfigFile_Type())
restartConfigFile.setMaxAccess(_C)
if mibBuilder.loadTexts:restartConfigFile.setStatus(_A)
class _RestartControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('running',1),('warmBoot',2),('coldBoot',3)))
_RestartControl_Type.__name__=_B
_RestartControl_Object=MibScalar
restartControl=_RestartControl_Object((1,3,6,1,4,1,52,4,12,30,1,7,3),_RestartControl_Type())
restartControl.setMaxAccess(_C)
if mibBuilder.loadTexts:restartControl.setStatus(_A)
_MirrorMgt_ObjectIdentity=ObjectIdentity
mirrorMgt=_MirrorMgt_ObjectIdentity((1,3,6,1,4,1,52,4,12,30,1,8))
_MirrorTable_Object=MibTable
mirrorTable=_MirrorTable_Object((1,3,6,1,4,1,52,4,12,30,1,8,1))
if mibBuilder.loadTexts:mirrorTable.setStatus(_A)
_MirrorEntry_Object=MibTableRow
mirrorEntry=_MirrorEntry_Object((1,3,6,1,4,1,52,4,12,30,1,8,1,1))
mirrorEntry.setIndexNames((0,_F,_A0),(0,_F,_A1))
if mibBuilder.loadTexts:mirrorEntry.setStatus(_A)
_MirrorDestinationPort_Type=Integer32
_MirrorDestinationPort_Object=MibTableColumn
mirrorDestinationPort=_MirrorDestinationPort_Object((1,3,6,1,4,1,52,4,12,30,1,8,1,1,1),_MirrorDestinationPort_Type())
mirrorDestinationPort.setMaxAccess(_G)
if mibBuilder.loadTexts:mirrorDestinationPort.setStatus(_A)
_MirrorSourcePort_Type=Integer32
_MirrorSourcePort_Object=MibTableColumn
mirrorSourcePort=_MirrorSourcePort_Object((1,3,6,1,4,1,52,4,12,30,1,8,1,1,2),_MirrorSourcePort_Type())
mirrorSourcePort.setMaxAccess(_G)
if mibBuilder.loadTexts:mirrorSourcePort.setStatus(_A)
class _MirrorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('rx',1),('tx',2),('both',3)))
_MirrorType_Type.__name__=_B
_MirrorType_Object=MibTableColumn
mirrorType=_MirrorType_Object((1,3,6,1,4,1,52,4,12,30,1,8,1,1,3),_MirrorType_Type())
mirrorType.setMaxAccess(_D)
if mibBuilder.loadTexts:mirrorType.setStatus(_A)
_MirrorStatus_Type=ValidStatus
_MirrorStatus_Object=MibTableColumn
mirrorStatus=_MirrorStatus_Object((1,3,6,1,4,1,52,4,12,30,1,8,1,1,4),_MirrorStatus_Type())
mirrorStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mirrorStatus.setStatus(_A)
_IgmpSnoopMgt_ObjectIdentity=ObjectIdentity
igmpSnoopMgt=_IgmpSnoopMgt_ObjectIdentity((1,3,6,1,4,1,52,4,12,30,1,9))
class _IgmpSnoopStatus_Type(EnabledStatus):defaultValue=1
_IgmpSnoopStatus_Type.__name__=_K
_IgmpSnoopStatus_Object=MibScalar
igmpSnoopStatus=_IgmpSnoopStatus_Object((1,3,6,1,4,1,52,4,12,30,1,9,1),_IgmpSnoopStatus_Type())
igmpSnoopStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpSnoopStatus.setStatus(_A)
class _IgmpSnoopQuerier_Type(EnabledStatus):defaultValue=1
_IgmpSnoopQuerier_Type.__name__=_K
_IgmpSnoopQuerier_Object=MibScalar
igmpSnoopQuerier=_IgmpSnoopQuerier_Object((1,3,6,1,4,1,52,4,12,30,1,9,2),_IgmpSnoopQuerier_Type())
igmpSnoopQuerier.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpSnoopQuerier.setStatus(_A)
class _IgmpSnoopQueryCount_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,10))
_IgmpSnoopQueryCount_Type.__name__=_B
_IgmpSnoopQueryCount_Object=MibScalar
igmpSnoopQueryCount=_IgmpSnoopQueryCount_Object((1,3,6,1,4,1,52,4,12,30,1,9,3),_IgmpSnoopQueryCount_Type())
igmpSnoopQueryCount.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpSnoopQueryCount.setStatus(_A)
class _IgmpSnoopQueryInterval_Type(Integer32):defaultValue=125;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,125))
_IgmpSnoopQueryInterval_Type.__name__=_B
_IgmpSnoopQueryInterval_Object=MibScalar
igmpSnoopQueryInterval=_IgmpSnoopQueryInterval_Object((1,3,6,1,4,1,52,4,12,30,1,9,4),_IgmpSnoopQueryInterval_Type())
igmpSnoopQueryInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpSnoopQueryInterval.setStatus(_A)
class _IgmpSnoopQueryMaxResponseTime_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,25))
_IgmpSnoopQueryMaxResponseTime_Type.__name__=_B
_IgmpSnoopQueryMaxResponseTime_Object=MibScalar
igmpSnoopQueryMaxResponseTime=_IgmpSnoopQueryMaxResponseTime_Object((1,3,6,1,4,1,52,4,12,30,1,9,5),_IgmpSnoopQueryMaxResponseTime_Type())
igmpSnoopQueryMaxResponseTime.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpSnoopQueryMaxResponseTime.setStatus(_A)
class _IgmpSnoopRouterPortExpireTime_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(300,500))
_IgmpSnoopRouterPortExpireTime_Type.__name__=_B
_IgmpSnoopRouterPortExpireTime_Object=MibScalar
igmpSnoopRouterPortExpireTime=_IgmpSnoopRouterPortExpireTime_Object((1,3,6,1,4,1,52,4,12,30,1,9,6),_IgmpSnoopRouterPortExpireTime_Type())
igmpSnoopRouterPortExpireTime.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpSnoopRouterPortExpireTime.setStatus(_A)
class _IgmpSnoopVersion_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_IgmpSnoopVersion_Type.__name__=_B
_IgmpSnoopVersion_Object=MibScalar
igmpSnoopVersion=_IgmpSnoopVersion_Object((1,3,6,1,4,1,52,4,12,30,1,9,7),_IgmpSnoopVersion_Type())
igmpSnoopVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpSnoopVersion.setStatus(_A)
_IgmpSnoopRouterCurrentTable_Object=MibTable
igmpSnoopRouterCurrentTable=_IgmpSnoopRouterCurrentTable_Object((1,3,6,1,4,1,52,4,12,30,1,9,8))
if mibBuilder.loadTexts:igmpSnoopRouterCurrentTable.setStatus(_A)
_IgmpSnoopRouterCurrentEntry_Object=MibTableRow
igmpSnoopRouterCurrentEntry=_IgmpSnoopRouterCurrentEntry_Object((1,3,6,1,4,1,52,4,12,30,1,9,8,1))
igmpSnoopRouterCurrentEntry.setIndexNames((0,_F,_A2))
if mibBuilder.loadTexts:igmpSnoopRouterCurrentEntry.setStatus(_A)
_IgmpSnoopRouterCurrentVlanIndex_Type=Unsigned32
_IgmpSnoopRouterCurrentVlanIndex_Object=MibTableColumn
igmpSnoopRouterCurrentVlanIndex=_IgmpSnoopRouterCurrentVlanIndex_Object((1,3,6,1,4,1,52,4,12,30,1,9,8,1,1),_IgmpSnoopRouterCurrentVlanIndex_Type())
igmpSnoopRouterCurrentVlanIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:igmpSnoopRouterCurrentVlanIndex.setStatus(_A)
_IgmpSnoopRouterCurrentPorts_Type=PortList
_IgmpSnoopRouterCurrentPorts_Object=MibTableColumn
igmpSnoopRouterCurrentPorts=_IgmpSnoopRouterCurrentPorts_Object((1,3,6,1,4,1,52,4,12,30,1,9,8,1,2),_IgmpSnoopRouterCurrentPorts_Type())
igmpSnoopRouterCurrentPorts.setMaxAccess(_E)
if mibBuilder.loadTexts:igmpSnoopRouterCurrentPorts.setStatus(_A)
_IgmpSnoopRouterCurrentStatus_Type=PortList
_IgmpSnoopRouterCurrentStatus_Object=MibTableColumn
igmpSnoopRouterCurrentStatus=_IgmpSnoopRouterCurrentStatus_Object((1,3,6,1,4,1,52,4,12,30,1,9,8,1,3),_IgmpSnoopRouterCurrentStatus_Type())
igmpSnoopRouterCurrentStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:igmpSnoopRouterCurrentStatus.setStatus(_A)
_IgmpSnoopRouterStaticTable_Object=MibTable
igmpSnoopRouterStaticTable=_IgmpSnoopRouterStaticTable_Object((1,3,6,1,4,1,52,4,12,30,1,9,9))
if mibBuilder.loadTexts:igmpSnoopRouterStaticTable.setStatus(_A)
_IgmpSnoopRouterStaticEntry_Object=MibTableRow
igmpSnoopRouterStaticEntry=_IgmpSnoopRouterStaticEntry_Object((1,3,6,1,4,1,52,4,12,30,1,9,9,1))
igmpSnoopRouterStaticEntry.setIndexNames((0,_F,_A3))
if mibBuilder.loadTexts:igmpSnoopRouterStaticEntry.setStatus(_A)
_IgmpSnoopRouterStaticVlanIndex_Type=Unsigned32
_IgmpSnoopRouterStaticVlanIndex_Object=MibTableColumn
igmpSnoopRouterStaticVlanIndex=_IgmpSnoopRouterStaticVlanIndex_Object((1,3,6,1,4,1,52,4,12,30,1,9,9,1,1),_IgmpSnoopRouterStaticVlanIndex_Type())
igmpSnoopRouterStaticVlanIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:igmpSnoopRouterStaticVlanIndex.setStatus(_A)
_IgmpSnoopRouterStaticPorts_Type=PortList
_IgmpSnoopRouterStaticPorts_Object=MibTableColumn
igmpSnoopRouterStaticPorts=_IgmpSnoopRouterStaticPorts_Object((1,3,6,1,4,1,52,4,12,30,1,9,9,1,2),_IgmpSnoopRouterStaticPorts_Type())
igmpSnoopRouterStaticPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:igmpSnoopRouterStaticPorts.setStatus(_A)
_IgmpSnoopRouterStaticStatus_Type=ValidStatus
_IgmpSnoopRouterStaticStatus_Object=MibTableColumn
igmpSnoopRouterStaticStatus=_IgmpSnoopRouterStaticStatus_Object((1,3,6,1,4,1,52,4,12,30,1,9,9,1,3),_IgmpSnoopRouterStaticStatus_Type())
igmpSnoopRouterStaticStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:igmpSnoopRouterStaticStatus.setStatus(_A)
_IgmpSnoopMulticastCurrentTable_Object=MibTable
igmpSnoopMulticastCurrentTable=_IgmpSnoopMulticastCurrentTable_Object((1,3,6,1,4,1,52,4,12,30,1,9,10))
if mibBuilder.loadTexts:igmpSnoopMulticastCurrentTable.setStatus(_A)
_IgmpSnoopMulticastCurrentEntry_Object=MibTableRow
igmpSnoopMulticastCurrentEntry=_IgmpSnoopMulticastCurrentEntry_Object((1,3,6,1,4,1,52,4,12,30,1,9,10,1))
igmpSnoopMulticastCurrentEntry.setIndexNames((0,_F,_A4),(0,_F,_A5))
if mibBuilder.loadTexts:igmpSnoopMulticastCurrentEntry.setStatus(_A)
_IgmpSnoopMulticastCurrentVlanIndex_Type=Unsigned32
_IgmpSnoopMulticastCurrentVlanIndex_Object=MibTableColumn
igmpSnoopMulticastCurrentVlanIndex=_IgmpSnoopMulticastCurrentVlanIndex_Object((1,3,6,1,4,1,52,4,12,30,1,9,10,1,1),_IgmpSnoopMulticastCurrentVlanIndex_Type())
igmpSnoopMulticastCurrentVlanIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:igmpSnoopMulticastCurrentVlanIndex.setStatus(_A)
_IgmpSnoopMulticastCurrentIpAddress_Type=IpAddress
_IgmpSnoopMulticastCurrentIpAddress_Object=MibTableColumn
igmpSnoopMulticastCurrentIpAddress=_IgmpSnoopMulticastCurrentIpAddress_Object((1,3,6,1,4,1,52,4,12,30,1,9,10,1,2),_IgmpSnoopMulticastCurrentIpAddress_Type())
igmpSnoopMulticastCurrentIpAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:igmpSnoopMulticastCurrentIpAddress.setStatus(_A)
_IgmpSnoopMulticastCurrentPorts_Type=PortList
_IgmpSnoopMulticastCurrentPorts_Object=MibTableColumn
igmpSnoopMulticastCurrentPorts=_IgmpSnoopMulticastCurrentPorts_Object((1,3,6,1,4,1,52,4,12,30,1,9,10,1,3),_IgmpSnoopMulticastCurrentPorts_Type())
igmpSnoopMulticastCurrentPorts.setMaxAccess(_E)
if mibBuilder.loadTexts:igmpSnoopMulticastCurrentPorts.setStatus(_A)
_IgmpSnoopMulticastCurrentStatus_Type=PortList
_IgmpSnoopMulticastCurrentStatus_Object=MibTableColumn
igmpSnoopMulticastCurrentStatus=_IgmpSnoopMulticastCurrentStatus_Object((1,3,6,1,4,1,52,4,12,30,1,9,10,1,4),_IgmpSnoopMulticastCurrentStatus_Type())
igmpSnoopMulticastCurrentStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:igmpSnoopMulticastCurrentStatus.setStatus(_A)
_IgmpSnoopMulticastStaticTable_Object=MibTable
igmpSnoopMulticastStaticTable=_IgmpSnoopMulticastStaticTable_Object((1,3,6,1,4,1,52,4,12,30,1,9,11))
if mibBuilder.loadTexts:igmpSnoopMulticastStaticTable.setStatus(_A)
_IgmpSnoopMulticastStaticEntry_Object=MibTableRow
igmpSnoopMulticastStaticEntry=_IgmpSnoopMulticastStaticEntry_Object((1,3,6,1,4,1,52,4,12,30,1,9,11,1))
igmpSnoopMulticastStaticEntry.setIndexNames((0,_F,_A6),(0,_F,_A7))
if mibBuilder.loadTexts:igmpSnoopMulticastStaticEntry.setStatus(_A)
_IgmpSnoopMulticastStaticVlanIndex_Type=Unsigned32
_IgmpSnoopMulticastStaticVlanIndex_Object=MibTableColumn
igmpSnoopMulticastStaticVlanIndex=_IgmpSnoopMulticastStaticVlanIndex_Object((1,3,6,1,4,1,52,4,12,30,1,9,11,1,1),_IgmpSnoopMulticastStaticVlanIndex_Type())
igmpSnoopMulticastStaticVlanIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:igmpSnoopMulticastStaticVlanIndex.setStatus(_A)
_IgmpSnoopMulticastStaticIpAddress_Type=IpAddress
_IgmpSnoopMulticastStaticIpAddress_Object=MibTableColumn
igmpSnoopMulticastStaticIpAddress=_IgmpSnoopMulticastStaticIpAddress_Object((1,3,6,1,4,1,52,4,12,30,1,9,11,1,2),_IgmpSnoopMulticastStaticIpAddress_Type())
igmpSnoopMulticastStaticIpAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:igmpSnoopMulticastStaticIpAddress.setStatus(_A)
_IgmpSnoopMulticastStaticPorts_Type=PortList
_IgmpSnoopMulticastStaticPorts_Object=MibTableColumn
igmpSnoopMulticastStaticPorts=_IgmpSnoopMulticastStaticPorts_Object((1,3,6,1,4,1,52,4,12,30,1,9,11,1,3),_IgmpSnoopMulticastStaticPorts_Type())
igmpSnoopMulticastStaticPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:igmpSnoopMulticastStaticPorts.setStatus(_A)
_IgmpSnoopMulticastStaticStatus_Type=ValidStatus
_IgmpSnoopMulticastStaticStatus_Object=MibTableColumn
igmpSnoopMulticastStaticStatus=_IgmpSnoopMulticastStaticStatus_Object((1,3,6,1,4,1,52,4,12,30,1,9,11,1,4),_IgmpSnoopMulticastStaticStatus_Type())
igmpSnoopMulticastStaticStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:igmpSnoopMulticastStaticStatus.setStatus(_A)
_IpMgt_ObjectIdentity=ObjectIdentity
ipMgt=_IpMgt_ObjectIdentity((1,3,6,1,4,1,52,4,12,30,1,10))
_NetConfigTable_Object=MibTable
netConfigTable=_NetConfigTable_Object((1,3,6,1,4,1,52,4,12,30,1,10,1))
if mibBuilder.loadTexts:netConfigTable.setStatus(_A)
_NetConfigEntry_Object=MibTableRow
netConfigEntry=_NetConfigEntry_Object((1,3,6,1,4,1,52,4,12,30,1,10,1,1))
netConfigEntry.setIndexNames((0,_F,_A8),(0,_F,_A9),(0,_F,_AA))
if mibBuilder.loadTexts:netConfigEntry.setStatus(_A)
_NetConfigIfIndex_Type=Integer32
_NetConfigIfIndex_Object=MibTableColumn
netConfigIfIndex=_NetConfigIfIndex_Object((1,3,6,1,4,1,52,4,12,30,1,10,1,1,1),_NetConfigIfIndex_Type())
netConfigIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:netConfigIfIndex.setStatus(_A)
_NetConfigIPAddress_Type=IpAddress
_NetConfigIPAddress_Object=MibTableColumn
netConfigIPAddress=_NetConfigIPAddress_Object((1,3,6,1,4,1,52,4,12,30,1,10,1,1,2),_NetConfigIPAddress_Type())
netConfigIPAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:netConfigIPAddress.setStatus(_A)
_NetConfigSubnetMask_Type=IpAddress
_NetConfigSubnetMask_Object=MibTableColumn
netConfigSubnetMask=_NetConfigSubnetMask_Object((1,3,6,1,4,1,52,4,12,30,1,10,1,1,3),_NetConfigSubnetMask_Type())
netConfigSubnetMask.setMaxAccess(_G)
if mibBuilder.loadTexts:netConfigSubnetMask.setStatus(_A)
class _NetConfigPrimaryInterface_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('primary',1),('secondary',2)))
_NetConfigPrimaryInterface_Type.__name__=_B
_NetConfigPrimaryInterface_Object=MibTableColumn
netConfigPrimaryInterface=_NetConfigPrimaryInterface_Object((1,3,6,1,4,1,52,4,12,30,1,10,1,1,4),_NetConfigPrimaryInterface_Type())
netConfigPrimaryInterface.setMaxAccess(_D)
if mibBuilder.loadTexts:netConfigPrimaryInterface.setStatus(_A)
class _NetConfigUnnumbered_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('unnumbered',1),('notUnnumbered',2)))
_NetConfigUnnumbered_Type.__name__=_B
_NetConfigUnnumbered_Object=MibTableColumn
netConfigUnnumbered=_NetConfigUnnumbered_Object((1,3,6,1,4,1,52,4,12,30,1,10,1,1,5),_NetConfigUnnumbered_Type())
netConfigUnnumbered.setMaxAccess(_E)
if mibBuilder.loadTexts:netConfigUnnumbered.setStatus(_A)
_NetConfigStatus_Type=RowStatus
_NetConfigStatus_Object=MibTableColumn
netConfigStatus=_NetConfigStatus_Object((1,3,6,1,4,1,52,4,12,30,1,10,1,1,6),_NetConfigStatus_Type())
netConfigStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:netConfigStatus.setStatus(_A)
_NetDefaultGateway_Type=IpAddress
_NetDefaultGateway_Object=MibScalar
netDefaultGateway=_NetDefaultGateway_Object((1,3,6,1,4,1,52,4,12,30,1,10,2),_NetDefaultGateway_Type())
netDefaultGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:netDefaultGateway.setStatus(_A)
_IpHttpState_Type=EnabledStatus
_IpHttpState_Object=MibScalar
ipHttpState=_IpHttpState_Object((1,3,6,1,4,1,52,4,12,30,1,10,3),_IpHttpState_Type())
ipHttpState.setMaxAccess(_C)
if mibBuilder.loadTexts:ipHttpState.setStatus(_A)
class _IpHttpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_IpHttpPort_Type.__name__=_B
_IpHttpPort_Object=MibScalar
ipHttpPort=_IpHttpPort_Object((1,3,6,1,4,1,52,4,12,30,1,10,4),_IpHttpPort_Type())
ipHttpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:ipHttpPort.setStatus(_A)
class _IpDhcpRestart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('restart',1),('noRestart',2)))
_IpDhcpRestart_Type.__name__=_B
_IpDhcpRestart_Object=MibScalar
ipDhcpRestart=_IpDhcpRestart_Object((1,3,6,1,4,1,52,4,12,30,1,10,5),_IpDhcpRestart_Type())
ipDhcpRestart.setMaxAccess(_C)
if mibBuilder.loadTexts:ipDhcpRestart.setStatus(_A)
_IpHttpsState_Type=EnabledStatus
_IpHttpsState_Object=MibScalar
ipHttpsState=_IpHttpsState_Object((1,3,6,1,4,1,52,4,12,30,1,10,6),_IpHttpsState_Type())
ipHttpsState.setMaxAccess(_C)
if mibBuilder.loadTexts:ipHttpsState.setStatus(_A)
class _IpHttpsPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_IpHttpsPort_Type.__name__=_B
_IpHttpsPort_Object=MibScalar
ipHttpsPort=_IpHttpsPort_Object((1,3,6,1,4,1,52,4,12,30,1,10,7),_IpHttpsPort_Type())
ipHttpsPort.setMaxAccess(_C)
if mibBuilder.loadTexts:ipHttpsPort.setStatus(_A)
_BcastStormMgt_ObjectIdentity=ObjectIdentity
bcastStormMgt=_BcastStormMgt_ObjectIdentity((1,3,6,1,4,1,52,4,12,30,1,11))
_BcastStormTable_Object=MibTable
bcastStormTable=_BcastStormTable_Object((1,3,6,1,4,1,52,4,12,30,1,11,1))
if mibBuilder.loadTexts:bcastStormTable.setStatus(_A)
_BcastStormEntry_Object=MibTableRow
bcastStormEntry=_BcastStormEntry_Object((1,3,6,1,4,1,52,4,12,30,1,11,1,1))
bcastStormEntry.setIndexNames((0,_F,_AB))
if mibBuilder.loadTexts:bcastStormEntry.setStatus(_A)
_BcastStormIfIndex_Type=Integer32
_BcastStormIfIndex_Object=MibTableColumn
bcastStormIfIndex=_BcastStormIfIndex_Object((1,3,6,1,4,1,52,4,12,30,1,11,1,1,1),_BcastStormIfIndex_Type())
bcastStormIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:bcastStormIfIndex.setStatus(_A)
_BcastStormStatus_Type=EnabledStatus
_BcastStormStatus_Object=MibTableColumn
bcastStormStatus=_BcastStormStatus_Object((1,3,6,1,4,1,52,4,12,30,1,11,1,1,2),_BcastStormStatus_Type())
bcastStormStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:bcastStormStatus.setStatus(_A)
class _BcastStormSampleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('pkt-rate',1),('octet-rate',2),('percent',3)))
_BcastStormSampleType_Type.__name__=_B
_BcastStormSampleType_Object=MibTableColumn
bcastStormSampleType=_BcastStormSampleType_Object((1,3,6,1,4,1,52,4,12,30,1,11,1,1,3),_BcastStormSampleType_Type())
bcastStormSampleType.setMaxAccess(_C)
if mibBuilder.loadTexts:bcastStormSampleType.setStatus(_A)
_BcastStormPktRate_Type=Integer32
_BcastStormPktRate_Object=MibTableColumn
bcastStormPktRate=_BcastStormPktRate_Object((1,3,6,1,4,1,52,4,12,30,1,11,1,1,4),_BcastStormPktRate_Type())
bcastStormPktRate.setMaxAccess(_C)
if mibBuilder.loadTexts:bcastStormPktRate.setStatus(_A)
_BcastStormOctetRate_Type=Integer32
_BcastStormOctetRate_Object=MibTableColumn
bcastStormOctetRate=_BcastStormOctetRate_Object((1,3,6,1,4,1,52,4,12,30,1,11,1,1,5),_BcastStormOctetRate_Type())
bcastStormOctetRate.setMaxAccess(_C)
if mibBuilder.loadTexts:bcastStormOctetRate.setStatus(_A)
_BcastStormPercent_Type=Integer32
_BcastStormPercent_Object=MibTableColumn
bcastStormPercent=_BcastStormPercent_Object((1,3,6,1,4,1,52,4,12,30,1,11,1,1,6),_BcastStormPercent_Type())
bcastStormPercent.setMaxAccess(_C)
if mibBuilder.loadTexts:bcastStormPercent.setStatus(_A)
_VlanMgt_ObjectIdentity=ObjectIdentity
vlanMgt=_VlanMgt_ObjectIdentity((1,3,6,1,4,1,52,4,12,30,1,12))
_VlanTable_Object=MibTable
vlanTable=_VlanTable_Object((1,3,6,1,4,1,52,4,12,30,1,12,1))
if mibBuilder.loadTexts:vlanTable.setStatus(_A)
_VlanEntry_Object=MibTableRow
vlanEntry=_VlanEntry_Object((1,3,6,1,4,1,52,4,12,30,1,12,1,1))
vlanEntry.setIndexNames((0,_F,_AC))
if mibBuilder.loadTexts:vlanEntry.setStatus(_A)
_VlanIndex_Type=Unsigned32
_VlanIndex_Object=MibTableColumn
vlanIndex=_VlanIndex_Object((1,3,6,1,4,1,52,4,12,30,1,12,1,1,1),_VlanIndex_Type())
vlanIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:vlanIndex.setStatus(_A)
class _VlanAddressMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('user',1),('bootp',2),('dhcp',3)))
_VlanAddressMethod_Type.__name__=_B
_VlanAddressMethod_Object=MibTableColumn
vlanAddressMethod=_VlanAddressMethod_Object((1,3,6,1,4,1,52,4,12,30,1,12,1,1,2),_VlanAddressMethod_Type())
vlanAddressMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanAddressMethod.setStatus(_A)
_VlanPortTable_Object=MibTable
vlanPortTable=_VlanPortTable_Object((1,3,6,1,4,1,52,4,12,30,1,12,2))
if mibBuilder.loadTexts:vlanPortTable.setStatus(_A)
_VlanPortEntry_Object=MibTableRow
vlanPortEntry=_VlanPortEntry_Object((1,3,6,1,4,1,52,4,12,30,1,12,2,1))
vlanPortEntry.setIndexNames((0,_F,_AD))
if mibBuilder.loadTexts:vlanPortEntry.setStatus(_A)
_VlanPortIndex_Type=Integer32
_VlanPortIndex_Object=MibTableColumn
vlanPortIndex=_VlanPortIndex_Object((1,3,6,1,4,1,52,4,12,30,1,12,2,1,1),_VlanPortIndex_Type())
vlanPortIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:vlanPortIndex.setStatus(_A)
class _VlanPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('hybrid',1),('dot1qTrunk',2),('access',3)))
_VlanPortMode_Type.__name__=_B
_VlanPortMode_Object=MibTableColumn
vlanPortMode=_VlanPortMode_Object((1,3,6,1,4,1,52,4,12,30,1,12,2,1,2),_VlanPortMode_Type())
vlanPortMode.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanPortMode.setStatus(_A)
_PriorityMgt_ObjectIdentity=ObjectIdentity
priorityMgt=_PriorityMgt_ObjectIdentity((1,3,6,1,4,1,52,4,12,30,1,13))
class _PrioIpPrecDscpStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_V,1),(_AE,2),('dscp',3)))
_PrioIpPrecDscpStatus_Type.__name__=_B
_PrioIpPrecDscpStatus_Object=MibScalar
prioIpPrecDscpStatus=_PrioIpPrecDscpStatus_Object((1,3,6,1,4,1,52,4,12,30,1,13,1),_PrioIpPrecDscpStatus_Type())
prioIpPrecDscpStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:prioIpPrecDscpStatus.setStatus(_A)
_PrioIpPrecTable_Object=MibTable
prioIpPrecTable=_PrioIpPrecTable_Object((1,3,6,1,4,1,52,4,12,30,1,13,2))
if mibBuilder.loadTexts:prioIpPrecTable.setStatus(_A)
_PrioIpPrecEntry_Object=MibTableRow
prioIpPrecEntry=_PrioIpPrecEntry_Object((1,3,6,1,4,1,52,4,12,30,1,13,2,1))
prioIpPrecEntry.setIndexNames((0,_F,_AF),(0,_F,_AG))
if mibBuilder.loadTexts:prioIpPrecEntry.setStatus(_A)
_PrioIpPrecPort_Type=Integer32
_PrioIpPrecPort_Object=MibTableColumn
prioIpPrecPort=_PrioIpPrecPort_Object((1,3,6,1,4,1,52,4,12,30,1,13,2,1,2),_PrioIpPrecPort_Type())
prioIpPrecPort.setMaxAccess(_G)
if mibBuilder.loadTexts:prioIpPrecPort.setStatus(_A)
class _PrioIpPrecValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_PrioIpPrecValue_Type.__name__=_B
_PrioIpPrecValue_Object=MibTableColumn
prioIpPrecValue=_PrioIpPrecValue_Object((1,3,6,1,4,1,52,4,12,30,1,13,2,1,3),_PrioIpPrecValue_Type())
prioIpPrecValue.setMaxAccess(_G)
if mibBuilder.loadTexts:prioIpPrecValue.setStatus(_A)
class _PrioIpPrecCos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_PrioIpPrecCos_Type.__name__=_B
_PrioIpPrecCos_Object=MibTableColumn
prioIpPrecCos=_PrioIpPrecCos_Object((1,3,6,1,4,1,52,4,12,30,1,13,2,1,4),_PrioIpPrecCos_Type())
prioIpPrecCos.setMaxAccess(_C)
if mibBuilder.loadTexts:prioIpPrecCos.setStatus(_A)
_PrioIpPrecRestoreDefault_Type=Integer32
_PrioIpPrecRestoreDefault_Object=MibScalar
prioIpPrecRestoreDefault=_PrioIpPrecRestoreDefault_Object((1,3,6,1,4,1,52,4,12,30,1,13,3),_PrioIpPrecRestoreDefault_Type())
prioIpPrecRestoreDefault.setMaxAccess(_C)
if mibBuilder.loadTexts:prioIpPrecRestoreDefault.setStatus(_A)
_PrioIpDscpTable_Object=MibTable
prioIpDscpTable=_PrioIpDscpTable_Object((1,3,6,1,4,1,52,4,12,30,1,13,4))
if mibBuilder.loadTexts:prioIpDscpTable.setStatus(_A)
_PrioIpDscpEntry_Object=MibTableRow
prioIpDscpEntry=_PrioIpDscpEntry_Object((1,3,6,1,4,1,52,4,12,30,1,13,4,1))
prioIpDscpEntry.setIndexNames((0,_F,_AH),(0,_F,_AI))
if mibBuilder.loadTexts:prioIpDscpEntry.setStatus(_A)
_PrioIpDscpPort_Type=Integer32
_PrioIpDscpPort_Object=MibTableColumn
prioIpDscpPort=_PrioIpDscpPort_Object((1,3,6,1,4,1,52,4,12,30,1,13,4,1,1),_PrioIpDscpPort_Type())
prioIpDscpPort.setMaxAccess(_G)
if mibBuilder.loadTexts:prioIpDscpPort.setStatus(_A)
class _PrioIpDscpValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_PrioIpDscpValue_Type.__name__=_B
_PrioIpDscpValue_Object=MibTableColumn
prioIpDscpValue=_PrioIpDscpValue_Object((1,3,6,1,4,1,52,4,12,30,1,13,4,1,2),_PrioIpDscpValue_Type())
prioIpDscpValue.setMaxAccess(_G)
if mibBuilder.loadTexts:prioIpDscpValue.setStatus(_A)
class _PrioIpDscpCos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_PrioIpDscpCos_Type.__name__=_B
_PrioIpDscpCos_Object=MibTableColumn
prioIpDscpCos=_PrioIpDscpCos_Object((1,3,6,1,4,1,52,4,12,30,1,13,4,1,3),_PrioIpDscpCos_Type())
prioIpDscpCos.setMaxAccess(_C)
if mibBuilder.loadTexts:prioIpDscpCos.setStatus(_A)
_PrioIpDscpRestoreDefault_Type=Integer32
_PrioIpDscpRestoreDefault_Object=MibScalar
prioIpDscpRestoreDefault=_PrioIpDscpRestoreDefault_Object((1,3,6,1,4,1,52,4,12,30,1,13,5),_PrioIpDscpRestoreDefault_Type())
prioIpDscpRestoreDefault.setMaxAccess(_C)
if mibBuilder.loadTexts:prioIpDscpRestoreDefault.setStatus(_A)
_PrioIpPortEnableStatus_Type=EnabledStatus
_PrioIpPortEnableStatus_Object=MibScalar
prioIpPortEnableStatus=_PrioIpPortEnableStatus_Object((1,3,6,1,4,1,52,4,12,30,1,13,6),_PrioIpPortEnableStatus_Type())
prioIpPortEnableStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:prioIpPortEnableStatus.setStatus(_A)
_PrioIpPortTable_Object=MibTable
prioIpPortTable=_PrioIpPortTable_Object((1,3,6,1,4,1,52,4,12,30,1,13,7))
if mibBuilder.loadTexts:prioIpPortTable.setStatus(_A)
_PrioIpPortEntry_Object=MibTableRow
prioIpPortEntry=_PrioIpPortEntry_Object((1,3,6,1,4,1,52,4,12,30,1,13,7,1))
prioIpPortEntry.setIndexNames((0,_F,_AJ),(0,_F,_AK))
if mibBuilder.loadTexts:prioIpPortEntry.setStatus(_A)
_PrioIpPortPhysPort_Type=Integer32
_PrioIpPortPhysPort_Object=MibTableColumn
prioIpPortPhysPort=_PrioIpPortPhysPort_Object((1,3,6,1,4,1,52,4,12,30,1,13,7,1,1),_PrioIpPortPhysPort_Type())
prioIpPortPhysPort.setMaxAccess(_G)
if mibBuilder.loadTexts:prioIpPortPhysPort.setStatus(_A)
class _PrioIpPortValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PrioIpPortValue_Type.__name__=_B
_PrioIpPortValue_Object=MibTableColumn
prioIpPortValue=_PrioIpPortValue_Object((1,3,6,1,4,1,52,4,12,30,1,13,7,1,2),_PrioIpPortValue_Type())
prioIpPortValue.setMaxAccess(_G)
if mibBuilder.loadTexts:prioIpPortValue.setStatus(_A)
class _PrioIpPortCos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_PrioIpPortCos_Type.__name__=_B
_PrioIpPortCos_Object=MibTableColumn
prioIpPortCos=_PrioIpPortCos_Object((1,3,6,1,4,1,52,4,12,30,1,13,7,1,3),_PrioIpPortCos_Type())
prioIpPortCos.setMaxAccess(_D)
if mibBuilder.loadTexts:prioIpPortCos.setStatus(_A)
_PrioIpPortStatus_Type=ValidStatus
_PrioIpPortStatus_Object=MibTableColumn
prioIpPortStatus=_PrioIpPortStatus_Object((1,3,6,1,4,1,52,4,12,30,1,13,7,1,4),_PrioIpPortStatus_Type())
prioIpPortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:prioIpPortStatus.setStatus(_A)
_PrioCopy_ObjectIdentity=ObjectIdentity
prioCopy=_PrioCopy_ObjectIdentity((1,3,6,1,4,1,52,4,12,30,1,13,8))
_PrioCopyIpPrec_Type=OctetString
_PrioCopyIpPrec_Object=MibScalar
prioCopyIpPrec=_PrioCopyIpPrec_Object((1,3,6,1,4,1,52,4,12,30,1,13,8,1),_PrioCopyIpPrec_Type())
prioCopyIpPrec.setMaxAccess(_C)
if mibBuilder.loadTexts:prioCopyIpPrec.setStatus(_A)
_PrioCopyIpDscp_Type=OctetString
_PrioCopyIpDscp_Object=MibScalar
prioCopyIpDscp=_PrioCopyIpDscp_Object((1,3,6,1,4,1,52,4,12,30,1,13,8,2),_PrioCopyIpDscp_Type())
prioCopyIpDscp.setMaxAccess(_C)
if mibBuilder.loadTexts:prioCopyIpDscp.setStatus(_A)
_PrioCopyIpPort_Type=OctetString
_PrioCopyIpPort_Object=MibScalar
prioCopyIpPort=_PrioCopyIpPort_Object((1,3,6,1,4,1,52,4,12,30,1,13,8,3),_PrioCopyIpPort_Type())
prioCopyIpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:prioCopyIpPort.setStatus(_A)
_PrioWrrTable_Object=MibTable
prioWrrTable=_PrioWrrTable_Object((1,3,6,1,4,1,52,4,12,30,1,13,9))
if mibBuilder.loadTexts:prioWrrTable.setStatus(_A)
_PrioWrrEntry_Object=MibTableRow
prioWrrEntry=_PrioWrrEntry_Object((1,3,6,1,4,1,52,4,12,30,1,13,9,1))
prioWrrEntry.setIndexNames((0,_F,_AL))
if mibBuilder.loadTexts:prioWrrEntry.setStatus(_A)
class _PrioWrrTrafficClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_PrioWrrTrafficClass_Type.__name__=_B
_PrioWrrTrafficClass_Object=MibTableColumn
prioWrrTrafficClass=_PrioWrrTrafficClass_Object((1,3,6,1,4,1,52,4,12,30,1,13,9,1,1),_PrioWrrTrafficClass_Type())
prioWrrTrafficClass.setMaxAccess(_G)
if mibBuilder.loadTexts:prioWrrTrafficClass.setStatus(_A)
class _PrioWrrWeight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_PrioWrrWeight_Type.__name__=_B
_PrioWrrWeight_Object=MibTableColumn
prioWrrWeight=_PrioWrrWeight_Object((1,3,6,1,4,1,52,4,12,30,1,13,9,1,2),_PrioWrrWeight_Type())
prioWrrWeight.setMaxAccess(_C)
if mibBuilder.loadTexts:prioWrrWeight.setStatus(_A)
_TrapDestMgt_ObjectIdentity=ObjectIdentity
trapDestMgt=_TrapDestMgt_ObjectIdentity((1,3,6,1,4,1,52,4,12,30,1,14))
_TrapDestTable_Object=MibTable
trapDestTable=_TrapDestTable_Object((1,3,6,1,4,1,52,4,12,30,1,14,1))
if mibBuilder.loadTexts:trapDestTable.setStatus(_A)
_TrapDestEntry_Object=MibTableRow
trapDestEntry=_TrapDestEntry_Object((1,3,6,1,4,1,52,4,12,30,1,14,1,1))
trapDestEntry.setIndexNames((0,_F,_AM))
if mibBuilder.loadTexts:trapDestEntry.setStatus(_A)
_TrapDestAddress_Type=IpAddress
_TrapDestAddress_Object=MibTableColumn
trapDestAddress=_TrapDestAddress_Object((1,3,6,1,4,1,52,4,12,30,1,14,1,1,1),_TrapDestAddress_Type())
trapDestAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:trapDestAddress.setStatus(_A)
class _TrapDestCommunity_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_TrapDestCommunity_Type.__name__=_I
_TrapDestCommunity_Object=MibTableColumn
trapDestCommunity=_TrapDestCommunity_Object((1,3,6,1,4,1,52,4,12,30,1,14,1,1,2),_TrapDestCommunity_Type())
trapDestCommunity.setMaxAccess(_D)
if mibBuilder.loadTexts:trapDestCommunity.setStatus(_A)
_TrapDestStatus_Type=ValidStatus
_TrapDestStatus_Object=MibTableColumn
trapDestStatus=_TrapDestStatus_Object((1,3,6,1,4,1,52,4,12,30,1,14,1,1,3),_TrapDestStatus_Type())
trapDestStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:trapDestStatus.setStatus(_A)
class _TrapDestVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('version1',1),('version2',2)))
_TrapDestVersion_Type.__name__=_B
_TrapDestVersion_Object=MibTableColumn
trapDestVersion=_TrapDestVersion_Object((1,3,6,1,4,1,52,4,12,30,1,14,1,1,4),_TrapDestVersion_Type())
trapDestVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:trapDestVersion.setStatus(_A)
_QosMgt_ObjectIdentity=ObjectIdentity
qosMgt=_QosMgt_ObjectIdentity((1,3,6,1,4,1,52,4,12,30,1,16))
_RateLimitMgt_ObjectIdentity=ObjectIdentity
rateLimitMgt=_RateLimitMgt_ObjectIdentity((1,3,6,1,4,1,52,4,12,30,1,16,1))
_RateLimitStatus_Type=EnabledStatus
_RateLimitStatus_Object=MibScalar
rateLimitStatus=_RateLimitStatus_Object((1,3,6,1,4,1,52,4,12,30,1,16,1,1),_RateLimitStatus_Type())
rateLimitStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rateLimitStatus.setStatus(_A)
_RateLimitPortTable_Object=MibTable
rateLimitPortTable=_RateLimitPortTable_Object((1,3,6,1,4,1,52,4,12,30,1,16,1,2))
if mibBuilder.loadTexts:rateLimitPortTable.setStatus(_A)
_RateLimitPortEntry_Object=MibTableRow
rateLimitPortEntry=_RateLimitPortEntry_Object((1,3,6,1,4,1,52,4,12,30,1,16,1,2,1))
rateLimitPortEntry.setIndexNames((0,_F,_AN))
if mibBuilder.loadTexts:rateLimitPortEntry.setStatus(_A)
_RlPortIndex_Type=Integer32
_RlPortIndex_Object=MibTableColumn
rlPortIndex=_RlPortIndex_Object((1,3,6,1,4,1,52,4,12,30,1,16,1,2,1,1),_RlPortIndex_Type())
rlPortIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:rlPortIndex.setStatus(_A)
_RlPortInputLimit_Type=Integer32
_RlPortInputLimit_Object=MibTableColumn
rlPortInputLimit=_RlPortInputLimit_Object((1,3,6,1,4,1,52,4,12,30,1,16,1,2,1,2),_RlPortInputLimit_Type())
rlPortInputLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPortInputLimit.setStatus(_A)
_RlPortOutputLimit_Type=Integer32
_RlPortOutputLimit_Object=MibTableColumn
rlPortOutputLimit=_RlPortOutputLimit_Object((1,3,6,1,4,1,52,4,12,30,1,16,1,2,1,3),_RlPortOutputLimit_Type())
rlPortOutputLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPortOutputLimit.setStatus(_A)
_RlPortInputStatus_Type=EnabledStatus
_RlPortInputStatus_Object=MibTableColumn
rlPortInputStatus=_RlPortInputStatus_Object((1,3,6,1,4,1,52,4,12,30,1,16,1,2,1,6),_RlPortInputStatus_Type())
rlPortInputStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPortInputStatus.setStatus(_A)
_RlPortOutputStatus_Type=EnabledStatus
_RlPortOutputStatus_Object=MibTableColumn
rlPortOutputStatus=_RlPortOutputStatus_Object((1,3,6,1,4,1,52,4,12,30,1,16,1,2,1,7),_RlPortOutputStatus_Type())
rlPortOutputStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPortOutputStatus.setStatus(_A)
_MarkerMgt_ObjectIdentity=ObjectIdentity
markerMgt=_MarkerMgt_ObjectIdentity((1,3,6,1,4,1,52,4,12,30,1,16,2))
_MarkerTable_Object=MibTable
markerTable=_MarkerTable_Object((1,3,6,1,4,1,52,4,12,30,1,16,2,1))
if mibBuilder.loadTexts:markerTable.setStatus(_A)
_MarkerEntry_Object=MibTableRow
markerEntry=_MarkerEntry_Object((1,3,6,1,4,1,52,4,12,30,1,16,2,1,1))
markerEntry.setIndexNames((0,_F,_AO),(0,_F,_AP))
if mibBuilder.loadTexts:markerEntry.setStatus(_A)
_MarkerIfIndex_Type=Integer32
_MarkerIfIndex_Object=MibTableColumn
markerIfIndex=_MarkerIfIndex_Object((1,3,6,1,4,1,52,4,12,30,1,16,2,1,1,1),_MarkerIfIndex_Type())
markerIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:markerIfIndex.setStatus(_A)
class _MarkerAclName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
_MarkerAclName_Type.__name__=_H
_MarkerAclName_Object=MibTableColumn
markerAclName=_MarkerAclName_Object((1,3,6,1,4,1,52,4,12,30,1,16,2,1,1,2),_MarkerAclName_Type())
markerAclName.setMaxAccess(_G)
if mibBuilder.loadTexts:markerAclName.setStatus(_A)
class _MarkerActionBitList_Type(Bits):namedValues=NamedValues(*(('dscp',0),(_AE,1),('priority',2)))
_MarkerActionBitList_Type.__name__=_P
_MarkerActionBitList_Object=MibTableColumn
markerActionBitList=_MarkerActionBitList_Object((1,3,6,1,4,1,52,4,12,30,1,16,2,1,1,3),_MarkerActionBitList_Type())
markerActionBitList.setMaxAccess(_D)
if mibBuilder.loadTexts:markerActionBitList.setStatus(_A)
class _MarkerDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_MarkerDscp_Type.__name__=_B
_MarkerDscp_Object=MibTableColumn
markerDscp=_MarkerDscp_Object((1,3,6,1,4,1,52,4,12,30,1,16,2,1,1,4),_MarkerDscp_Type())
markerDscp.setMaxAccess(_D)
if mibBuilder.loadTexts:markerDscp.setStatus(_A)
class _MarkerPrecedence_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_MarkerPrecedence_Type.__name__=_B
_MarkerPrecedence_Object=MibTableColumn
markerPrecedence=_MarkerPrecedence_Object((1,3,6,1,4,1,52,4,12,30,1,16,2,1,1,5),_MarkerPrecedence_Type())
markerPrecedence.setMaxAccess(_D)
if mibBuilder.loadTexts:markerPrecedence.setStatus(_A)
class _MarkerPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_MarkerPriority_Type.__name__=_B
_MarkerPriority_Object=MibTableColumn
markerPriority=_MarkerPriority_Object((1,3,6,1,4,1,52,4,12,30,1,16,2,1,1,6),_MarkerPriority_Type())
markerPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:markerPriority.setStatus(_A)
_MarkerStatus_Type=RowStatus
_MarkerStatus_Object=MibTableColumn
markerStatus=_MarkerStatus_Object((1,3,6,1,4,1,52,4,12,30,1,16,2,1,1,7),_MarkerStatus_Type())
markerStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:markerStatus.setStatus(_A)
_CosMgt_ObjectIdentity=ObjectIdentity
cosMgt=_CosMgt_ObjectIdentity((1,3,6,1,4,1,52,4,12,30,1,16,3))
_PrioAclToCosMappingTable_Object=MibTable
prioAclToCosMappingTable=_PrioAclToCosMappingTable_Object((1,3,6,1,4,1,52,4,12,30,1,16,3,1))
if mibBuilder.loadTexts:prioAclToCosMappingTable.setStatus(_A)
_PrioAclToCosMappingEntry_Object=MibTableRow
prioAclToCosMappingEntry=_PrioAclToCosMappingEntry_Object((1,3,6,1,4,1,52,4,12,30,1,16,3,1,1))
prioAclToCosMappingEntry.setIndexNames((0,_F,_AQ),(0,_F,_AR))
if mibBuilder.loadTexts:prioAclToCosMappingEntry.setStatus(_A)
_PrioAclToCosMappingIfIndex_Type=Integer32
_PrioAclToCosMappingIfIndex_Object=MibTableColumn
prioAclToCosMappingIfIndex=_PrioAclToCosMappingIfIndex_Object((1,3,6,1,4,1,52,4,12,30,1,16,3,1,1,1),_PrioAclToCosMappingIfIndex_Type())
prioAclToCosMappingIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:prioAclToCosMappingIfIndex.setStatus(_A)
class _PrioAclToCosMappingAclName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
_PrioAclToCosMappingAclName_Type.__name__=_H
_PrioAclToCosMappingAclName_Object=MibTableColumn
prioAclToCosMappingAclName=_PrioAclToCosMappingAclName_Object((1,3,6,1,4,1,52,4,12,30,1,16,3,1,1,2),_PrioAclToCosMappingAclName_Type())
prioAclToCosMappingAclName.setMaxAccess(_G)
if mibBuilder.loadTexts:prioAclToCosMappingAclName.setStatus(_A)
class _PrioAclToCosMappingCosValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_PrioAclToCosMappingCosValue_Type.__name__=_B
_PrioAclToCosMappingCosValue_Object=MibTableColumn
prioAclToCosMappingCosValue=_PrioAclToCosMappingCosValue_Object((1,3,6,1,4,1,52,4,12,30,1,16,3,1,1,3),_PrioAclToCosMappingCosValue_Type())
prioAclToCosMappingCosValue.setMaxAccess(_D)
if mibBuilder.loadTexts:prioAclToCosMappingCosValue.setStatus(_A)
_PrioAclToCosMappingStatus_Type=RowStatus
_PrioAclToCosMappingStatus_Object=MibTableColumn
prioAclToCosMappingStatus=_PrioAclToCosMappingStatus_Object((1,3,6,1,4,1,52,4,12,30,1,16,3,1,1,4),_PrioAclToCosMappingStatus_Type())
prioAclToCosMappingStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:prioAclToCosMappingStatus.setStatus(_A)
_SecurityMgt_ObjectIdentity=ObjectIdentity
securityMgt=_SecurityMgt_ObjectIdentity((1,3,6,1,4,1,52,4,12,30,1,17))
_PortSecurityMgt_ObjectIdentity=ObjectIdentity
portSecurityMgt=_PortSecurityMgt_ObjectIdentity((1,3,6,1,4,1,52,4,12,30,1,17,2))
_PortSecPortTable_Object=MibTable
portSecPortTable=_PortSecPortTable_Object((1,3,6,1,4,1,52,4,12,30,1,17,2,1))
if mibBuilder.loadTexts:portSecPortTable.setStatus(_A)
_PortSecPortEntry_Object=MibTableRow
portSecPortEntry=_PortSecPortEntry_Object((1,3,6,1,4,1,52,4,12,30,1,17,2,1,1))
portSecPortEntry.setIndexNames((0,_F,_AS))
if mibBuilder.loadTexts:portSecPortEntry.setStatus(_A)
_PortSecPortIndex_Type=Integer32
_PortSecPortIndex_Object=MibTableColumn
portSecPortIndex=_PortSecPortIndex_Object((1,3,6,1,4,1,52,4,12,30,1,17,2,1,1,1),_PortSecPortIndex_Type())
portSecPortIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:portSecPortIndex.setStatus(_A)
_PortSecPortStatus_Type=EnabledStatus
_PortSecPortStatus_Object=MibTableColumn
portSecPortStatus=_PortSecPortStatus_Object((1,3,6,1,4,1,52,4,12,30,1,17,2,1,1,2),_PortSecPortStatus_Type())
portSecPortStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:portSecPortStatus.setStatus(_A)
class _PortSecAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_W,1),('trap',2),('shutdown',3),('trapAndShutdown',4)))
_PortSecAction_Type.__name__=_B
_PortSecAction_Object=MibTableColumn
portSecAction=_PortSecAction_Object((1,3,6,1,4,1,52,4,12,30,1,17,2,1,1,3),_PortSecAction_Type())
portSecAction.setMaxAccess(_C)
if mibBuilder.loadTexts:portSecAction.setStatus(_A)
class _PortSecMaxMacCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,20))
_PortSecMaxMacCount_Type.__name__=_B
_PortSecMaxMacCount_Object=MibTableColumn
portSecMaxMacCount=_PortSecMaxMacCount_Object((1,3,6,1,4,1,52,4,12,30,1,17,2,1,1,4),_PortSecMaxMacCount_Type())
portSecMaxMacCount.setMaxAccess(_C)
if mibBuilder.loadTexts:portSecMaxMacCount.setStatus(_A)
_RadiusMgt_ObjectIdentity=ObjectIdentity
radiusMgt=_RadiusMgt_ObjectIdentity((1,3,6,1,4,1,52,4,12,30,1,17,4))
_RadiusServerAddress_Type=IpAddress
_RadiusServerAddress_Object=MibScalar
radiusServerAddress=_RadiusServerAddress_Object((1,3,6,1,4,1,52,4,12,30,1,17,4,1),_RadiusServerAddress_Type())
radiusServerAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:radiusServerAddress.setStatus(_A)
class _RadiusServerPortNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_RadiusServerPortNumber_Type.__name__=_B
_RadiusServerPortNumber_Object=MibScalar
radiusServerPortNumber=_RadiusServerPortNumber_Object((1,3,6,1,4,1,52,4,12,30,1,17,4,2),_RadiusServerPortNumber_Type())
radiusServerPortNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:radiusServerPortNumber.setStatus(_A)
class _RadiusServerKey_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,48))
_RadiusServerKey_Type.__name__=_H
_RadiusServerKey_Object=MibScalar
radiusServerKey=_RadiusServerKey_Object((1,3,6,1,4,1,52,4,12,30,1,17,4,3),_RadiusServerKey_Type())
radiusServerKey.setMaxAccess(_C)
if mibBuilder.loadTexts:radiusServerKey.setStatus(_A)
class _RadiusServerRetransmit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_RadiusServerRetransmit_Type.__name__=_B
_RadiusServerRetransmit_Object=MibScalar
radiusServerRetransmit=_RadiusServerRetransmit_Object((1,3,6,1,4,1,52,4,12,30,1,17,4,4),_RadiusServerRetransmit_Type())
radiusServerRetransmit.setMaxAccess(_C)
if mibBuilder.loadTexts:radiusServerRetransmit.setStatus(_A)
class _RadiusServerTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_RadiusServerTimeout_Type.__name__=_B
_RadiusServerTimeout_Object=MibScalar
radiusServerTimeout=_RadiusServerTimeout_Object((1,3,6,1,4,1,52,4,12,30,1,17,4,5),_RadiusServerTimeout_Type())
radiusServerTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:radiusServerTimeout.setStatus(_A)
_TacacsMgt_ObjectIdentity=ObjectIdentity
tacacsMgt=_TacacsMgt_ObjectIdentity((1,3,6,1,4,1,52,4,12,30,1,17,5))
_TacacsServerAddress_Type=IpAddress
_TacacsServerAddress_Object=MibScalar
tacacsServerAddress=_TacacsServerAddress_Object((1,3,6,1,4,1,52,4,12,30,1,17,5,1),_TacacsServerAddress_Type())
tacacsServerAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:tacacsServerAddress.setStatus(_A)
class _TacacsServerPortNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_TacacsServerPortNumber_Type.__name__=_B
_TacacsServerPortNumber_Object=MibScalar
tacacsServerPortNumber=_TacacsServerPortNumber_Object((1,3,6,1,4,1,52,4,12,30,1,17,5,2),_TacacsServerPortNumber_Type())
tacacsServerPortNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:tacacsServerPortNumber.setStatus(_A)
class _TacacsServerKey_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,48))
_TacacsServerKey_Type.__name__=_H
_TacacsServerKey_Object=MibScalar
tacacsServerKey=_TacacsServerKey_Object((1,3,6,1,4,1,52,4,12,30,1,17,5,3),_TacacsServerKey_Type())
tacacsServerKey.setMaxAccess(_C)
if mibBuilder.loadTexts:tacacsServerKey.setStatus(_A)
_SshMgt_ObjectIdentity=ObjectIdentity
sshMgt=_SshMgt_ObjectIdentity((1,3,6,1,4,1,52,4,12,30,1,17,6))
_SshServerStatus_Type=EnabledStatus
_SshServerStatus_Object=MibScalar
sshServerStatus=_SshServerStatus_Object((1,3,6,1,4,1,52,4,12,30,1,17,6,1),_SshServerStatus_Type())
sshServerStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sshServerStatus.setStatus(_A)
_SshServerMajorVersion_Type=Integer32
_SshServerMajorVersion_Object=MibScalar
sshServerMajorVersion=_SshServerMajorVersion_Object((1,3,6,1,4,1,52,4,12,30,1,17,6,2),_SshServerMajorVersion_Type())
sshServerMajorVersion.setMaxAccess(_E)
if mibBuilder.loadTexts:sshServerMajorVersion.setStatus(_A)
_SshServerMinorVersion_Type=Integer32
_SshServerMinorVersion_Object=MibScalar
sshServerMinorVersion=_SshServerMinorVersion_Object((1,3,6,1,4,1,52,4,12,30,1,17,6,3),_SshServerMinorVersion_Type())
sshServerMinorVersion.setMaxAccess(_E)
if mibBuilder.loadTexts:sshServerMinorVersion.setStatus(_A)
class _SshTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,120))
_SshTimeout_Type.__name__=_B
_SshTimeout_Object=MibScalar
sshTimeout=_SshTimeout_Object((1,3,6,1,4,1,52,4,12,30,1,17,6,4),_SshTimeout_Type())
sshTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:sshTimeout.setStatus(_A)
class _SshAuthRetries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_SshAuthRetries_Type.__name__=_B
_SshAuthRetries_Object=MibScalar
sshAuthRetries=_SshAuthRetries_Object((1,3,6,1,4,1,52,4,12,30,1,17,6,5),_SshAuthRetries_Type())
sshAuthRetries.setMaxAccess(_C)
if mibBuilder.loadTexts:sshAuthRetries.setStatus(_A)
_SshConnInfoTable_Object=MibTable
sshConnInfoTable=_SshConnInfoTable_Object((1,3,6,1,4,1,52,4,12,30,1,17,6,6))
if mibBuilder.loadTexts:sshConnInfoTable.setStatus(_A)
_SshConnInfoEntry_Object=MibTableRow
sshConnInfoEntry=_SshConnInfoEntry_Object((1,3,6,1,4,1,52,4,12,30,1,17,6,6,1))
sshConnInfoEntry.setIndexNames((0,_F,_AT))
if mibBuilder.loadTexts:sshConnInfoEntry.setStatus(_A)
_SshConnID_Type=Integer32
_SshConnID_Object=MibTableColumn
sshConnID=_SshConnID_Object((1,3,6,1,4,1,52,4,12,30,1,17,6,6,1,1),_SshConnID_Type())
sshConnID.setMaxAccess(_G)
if mibBuilder.loadTexts:sshConnID.setStatus(_A)
_SshConnMajorVersion_Type=Integer32
_SshConnMajorVersion_Object=MibTableColumn
sshConnMajorVersion=_SshConnMajorVersion_Object((1,3,6,1,4,1,52,4,12,30,1,17,6,6,1,2),_SshConnMajorVersion_Type())
sshConnMajorVersion.setMaxAccess(_E)
if mibBuilder.loadTexts:sshConnMajorVersion.setStatus(_A)
_SshConnMinorVersion_Type=Integer32
_SshConnMinorVersion_Object=MibTableColumn
sshConnMinorVersion=_SshConnMinorVersion_Object((1,3,6,1,4,1,52,4,12,30,1,17,6,6,1,3),_SshConnMinorVersion_Type())
sshConnMinorVersion.setMaxAccess(_E)
if mibBuilder.loadTexts:sshConnMinorVersion.setStatus(_A)
class _SshConnEncryptionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_W,1),('des',2),('tribeDes',3)))
_SshConnEncryptionType_Type.__name__=_B
_SshConnEncryptionType_Object=MibTableColumn
sshConnEncryptionType=_SshConnEncryptionType_Object((1,3,6,1,4,1,52,4,12,30,1,17,6,6,1,4),_SshConnEncryptionType_Type())
sshConnEncryptionType.setMaxAccess(_E)
if mibBuilder.loadTexts:sshConnEncryptionType.setStatus(_A)
class _SshConnStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('negotiationStart',1),('authenticationStart',2),('sessionStart',3)))
_SshConnStatus_Type.__name__=_B
_SshConnStatus_Object=MibTableColumn
sshConnStatus=_SshConnStatus_Object((1,3,6,1,4,1,52,4,12,30,1,17,6,6,1,5),_SshConnStatus_Type())
sshConnStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:sshConnStatus.setStatus(_A)
_SshConnUserName_Type=OctetString
_SshConnUserName_Object=MibTableColumn
sshConnUserName=_SshConnUserName_Object((1,3,6,1,4,1,52,4,12,30,1,17,6,6,1,6),_SshConnUserName_Type())
sshConnUserName.setMaxAccess(_E)
if mibBuilder.loadTexts:sshConnUserName.setStatus(_A)
class _SshDisconnect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noDisconnect',1),('disconnect',2)))
_SshDisconnect_Type.__name__=_B
_SshDisconnect_Object=MibTableColumn
sshDisconnect=_SshDisconnect_Object((1,3,6,1,4,1,52,4,12,30,1,17,6,6,1,7),_SshDisconnect_Type())
sshDisconnect.setMaxAccess(_C)
if mibBuilder.loadTexts:sshDisconnect.setStatus(_A)
_AclMgt_ObjectIdentity=ObjectIdentity
aclMgt=_AclMgt_ObjectIdentity((1,3,6,1,4,1,52,4,12,30,1,17,7))
_AclIpAceTable_Object=MibTable
aclIpAceTable=_AclIpAceTable_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,1))
if mibBuilder.loadTexts:aclIpAceTable.setStatus(_A)
_AclIpAceEntry_Object=MibTableRow
aclIpAceEntry=_AclIpAceEntry_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,1,1))
aclIpAceEntry.setIndexNames((0,_F,_AU),(0,_F,_AV))
if mibBuilder.loadTexts:aclIpAceEntry.setStatus(_A)
class _AclIpAceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
_AclIpAceName_Type.__name__=_H
_AclIpAceName_Object=MibTableColumn
aclIpAceName=_AclIpAceName_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,1,1,1),_AclIpAceName_Type())
aclIpAceName.setMaxAccess(_G)
if mibBuilder.loadTexts:aclIpAceName.setStatus(_A)
class _AclIpAceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_AclIpAceIndex_Type.__name__=_B
_AclIpAceIndex_Object=MibTableColumn
aclIpAceIndex=_AclIpAceIndex_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,1,1,2),_AclIpAceIndex_Type())
aclIpAceIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:aclIpAceIndex.setStatus(_A)
class _AclIpAcePrecedence_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_AclIpAcePrecedence_Type.__name__=_B
_AclIpAcePrecedence_Object=MibTableColumn
aclIpAcePrecedence=_AclIpAcePrecedence_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,1,1,3),_AclIpAcePrecedence_Type())
aclIpAcePrecedence.setMaxAccess(_E)
if mibBuilder.loadTexts:aclIpAcePrecedence.setStatus(_A)
class _AclIpAceAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('permit',1),('deny',2)))
_AclIpAceAction_Type.__name__=_B
_AclIpAceAction_Object=MibTableColumn
aclIpAceAction=_AclIpAceAction_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,1,1,4),_AclIpAceAction_Type())
aclIpAceAction.setMaxAccess(_D)
if mibBuilder.loadTexts:aclIpAceAction.setStatus(_A)
_AclIpAceSourceIpAddr_Type=IpAddress
_AclIpAceSourceIpAddr_Object=MibTableColumn
aclIpAceSourceIpAddr=_AclIpAceSourceIpAddr_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,1,1,5),_AclIpAceSourceIpAddr_Type())
aclIpAceSourceIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:aclIpAceSourceIpAddr.setStatus(_A)
_AclIpAceSourceIpAddrBitmask_Type=IpAddress
_AclIpAceSourceIpAddrBitmask_Object=MibTableColumn
aclIpAceSourceIpAddrBitmask=_AclIpAceSourceIpAddrBitmask_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,1,1,6),_AclIpAceSourceIpAddrBitmask_Type())
aclIpAceSourceIpAddrBitmask.setMaxAccess(_D)
if mibBuilder.loadTexts:aclIpAceSourceIpAddrBitmask.setStatus(_A)
_AclIpAceDestIpAddr_Type=IpAddress
_AclIpAceDestIpAddr_Object=MibTableColumn
aclIpAceDestIpAddr=_AclIpAceDestIpAddr_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,1,1,7),_AclIpAceDestIpAddr_Type())
aclIpAceDestIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:aclIpAceDestIpAddr.setStatus(_A)
_AclIpAceDestIpAddrBitmask_Type=IpAddress
_AclIpAceDestIpAddrBitmask_Object=MibTableColumn
aclIpAceDestIpAddrBitmask=_AclIpAceDestIpAddrBitmask_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,1,1,8),_AclIpAceDestIpAddrBitmask_Type())
aclIpAceDestIpAddrBitmask.setMaxAccess(_D)
if mibBuilder.loadTexts:aclIpAceDestIpAddrBitmask.setStatus(_A)
class _AclIpAceProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_AclIpAceProtocol_Type.__name__=_B
_AclIpAceProtocol_Object=MibTableColumn
aclIpAceProtocol=_AclIpAceProtocol_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,1,1,9),_AclIpAceProtocol_Type())
aclIpAceProtocol.setMaxAccess(_D)
if mibBuilder.loadTexts:aclIpAceProtocol.setStatus(_A)
class _AclIpAcePrec_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_AclIpAcePrec_Type.__name__=_B
_AclIpAcePrec_Object=MibTableColumn
aclIpAcePrec=_AclIpAcePrec_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,1,1,10),_AclIpAcePrec_Type())
aclIpAcePrec.setMaxAccess(_D)
if mibBuilder.loadTexts:aclIpAcePrec.setStatus(_A)
class _AclIpAceTos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_AclIpAceTos_Type.__name__=_B
_AclIpAceTos_Object=MibTableColumn
aclIpAceTos=_AclIpAceTos_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,1,1,11),_AclIpAceTos_Type())
aclIpAceTos.setMaxAccess(_D)
if mibBuilder.loadTexts:aclIpAceTos.setStatus(_A)
class _AclIpAceDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_AclIpAceDscp_Type.__name__=_B
_AclIpAceDscp_Object=MibTableColumn
aclIpAceDscp=_AclIpAceDscp_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,1,1,12),_AclIpAceDscp_Type())
aclIpAceDscp.setMaxAccess(_D)
if mibBuilder.loadTexts:aclIpAceDscp.setStatus(_A)
class _AclIpAceSourcePortOp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3)))
_AclIpAceSourcePortOp_Type.__name__=_B
_AclIpAceSourcePortOp_Object=MibTableColumn
aclIpAceSourcePortOp=_AclIpAceSourcePortOp_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,1,1,13),_AclIpAceSourcePortOp_Type())
aclIpAceSourcePortOp.setMaxAccess(_D)
if mibBuilder.loadTexts:aclIpAceSourcePortOp.setStatus(_A)
class _AclIpAceMinSourcePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AclIpAceMinSourcePort_Type.__name__=_B
_AclIpAceMinSourcePort_Object=MibTableColumn
aclIpAceMinSourcePort=_AclIpAceMinSourcePort_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,1,1,14),_AclIpAceMinSourcePort_Type())
aclIpAceMinSourcePort.setMaxAccess(_D)
if mibBuilder.loadTexts:aclIpAceMinSourcePort.setStatus(_A)
class _AclIpAceMaxSourcePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AclIpAceMaxSourcePort_Type.__name__=_B
_AclIpAceMaxSourcePort_Object=MibTableColumn
aclIpAceMaxSourcePort=_AclIpAceMaxSourcePort_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,1,1,15),_AclIpAceMaxSourcePort_Type())
aclIpAceMaxSourcePort.setMaxAccess(_D)
if mibBuilder.loadTexts:aclIpAceMaxSourcePort.setStatus(_A)
class _AclIpAceSourcePortBitmask_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AclIpAceSourcePortBitmask_Type.__name__=_B
_AclIpAceSourcePortBitmask_Object=MibTableColumn
aclIpAceSourcePortBitmask=_AclIpAceSourcePortBitmask_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,1,1,16),_AclIpAceSourcePortBitmask_Type())
aclIpAceSourcePortBitmask.setMaxAccess(_D)
if mibBuilder.loadTexts:aclIpAceSourcePortBitmask.setStatus(_A)
class _AclIpAceDestPortOp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3)))
_AclIpAceDestPortOp_Type.__name__=_B
_AclIpAceDestPortOp_Object=MibTableColumn
aclIpAceDestPortOp=_AclIpAceDestPortOp_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,1,1,17),_AclIpAceDestPortOp_Type())
aclIpAceDestPortOp.setMaxAccess(_D)
if mibBuilder.loadTexts:aclIpAceDestPortOp.setStatus(_A)
class _AclIpAceMinDestPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AclIpAceMinDestPort_Type.__name__=_B
_AclIpAceMinDestPort_Object=MibTableColumn
aclIpAceMinDestPort=_AclIpAceMinDestPort_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,1,1,18),_AclIpAceMinDestPort_Type())
aclIpAceMinDestPort.setMaxAccess(_D)
if mibBuilder.loadTexts:aclIpAceMinDestPort.setStatus(_A)
class _AclIpAceMaxDestPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AclIpAceMaxDestPort_Type.__name__=_B
_AclIpAceMaxDestPort_Object=MibTableColumn
aclIpAceMaxDestPort=_AclIpAceMaxDestPort_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,1,1,19),_AclIpAceMaxDestPort_Type())
aclIpAceMaxDestPort.setMaxAccess(_D)
if mibBuilder.loadTexts:aclIpAceMaxDestPort.setStatus(_A)
class _AclIpAceDestPortBitmask_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AclIpAceDestPortBitmask_Type.__name__=_B
_AclIpAceDestPortBitmask_Object=MibTableColumn
aclIpAceDestPortBitmask=_AclIpAceDestPortBitmask_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,1,1,20),_AclIpAceDestPortBitmask_Type())
aclIpAceDestPortBitmask.setMaxAccess(_D)
if mibBuilder.loadTexts:aclIpAceDestPortBitmask.setStatus(_A)
class _AclIpAceControlCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_AclIpAceControlCode_Type.__name__=_B
_AclIpAceControlCode_Object=MibTableColumn
aclIpAceControlCode=_AclIpAceControlCode_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,1,1,21),_AclIpAceControlCode_Type())
aclIpAceControlCode.setMaxAccess(_D)
if mibBuilder.loadTexts:aclIpAceControlCode.setStatus(_A)
class _AclIpAceControlCodeBitmask_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_AclIpAceControlCodeBitmask_Type.__name__=_B
_AclIpAceControlCodeBitmask_Object=MibTableColumn
aclIpAceControlCodeBitmask=_AclIpAceControlCodeBitmask_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,1,1,22),_AclIpAceControlCodeBitmask_Type())
aclIpAceControlCodeBitmask.setMaxAccess(_D)
if mibBuilder.loadTexts:aclIpAceControlCodeBitmask.setStatus(_A)
_AclIpAceStatus_Type=RowStatus
_AclIpAceStatus_Object=MibTableColumn
aclIpAceStatus=_AclIpAceStatus_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,1,1,23),_AclIpAceStatus_Type())
aclIpAceStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:aclIpAceStatus.setStatus(_A)
_AclMacAceTable_Object=MibTable
aclMacAceTable=_AclMacAceTable_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,2))
if mibBuilder.loadTexts:aclMacAceTable.setStatus(_A)
_AclMacAceEntry_Object=MibTableRow
aclMacAceEntry=_AclMacAceEntry_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,2,1))
aclMacAceEntry.setIndexNames((0,_F,_AW),(0,_F,_AX))
if mibBuilder.loadTexts:aclMacAceEntry.setStatus(_A)
class _AclMacAceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
_AclMacAceName_Type.__name__=_H
_AclMacAceName_Object=MibTableColumn
aclMacAceName=_AclMacAceName_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,2,1,1),_AclMacAceName_Type())
aclMacAceName.setMaxAccess(_G)
if mibBuilder.loadTexts:aclMacAceName.setStatus(_A)
class _AclMacAceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_AclMacAceIndex_Type.__name__=_B
_AclMacAceIndex_Object=MibTableColumn
aclMacAceIndex=_AclMacAceIndex_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,2,1,2),_AclMacAceIndex_Type())
aclMacAceIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:aclMacAceIndex.setStatus(_A)
class _AclMacAcePrecedence_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_AclMacAcePrecedence_Type.__name__=_B
_AclMacAcePrecedence_Object=MibTableColumn
aclMacAcePrecedence=_AclMacAcePrecedence_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,2,1,3),_AclMacAcePrecedence_Type())
aclMacAcePrecedence.setMaxAccess(_E)
if mibBuilder.loadTexts:aclMacAcePrecedence.setStatus(_A)
class _AclMacAceAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('permit',1),('deny',2)))
_AclMacAceAction_Type.__name__=_B
_AclMacAceAction_Object=MibTableColumn
aclMacAceAction=_AclMacAceAction_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,2,1,4),_AclMacAceAction_Type())
aclMacAceAction.setMaxAccess(_D)
if mibBuilder.loadTexts:aclMacAceAction.setStatus(_A)
class _AclMacAcePktformat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('any',1),('untagged-Eth2',2),('untagged802Dot3',3),('tagggedEth2',4),('tagged802Dot3',5)))
_AclMacAcePktformat_Type.__name__=_B
_AclMacAcePktformat_Object=MibTableColumn
aclMacAcePktformat=_AclMacAcePktformat_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,2,1,5),_AclMacAcePktformat_Type())
aclMacAcePktformat.setMaxAccess(_D)
if mibBuilder.loadTexts:aclMacAcePktformat.setStatus(_A)
class _AclMacAceSourceMacAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_AclMacAceSourceMacAddr_Type.__name__=_I
_AclMacAceSourceMacAddr_Object=MibTableColumn
aclMacAceSourceMacAddr=_AclMacAceSourceMacAddr_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,2,1,6),_AclMacAceSourceMacAddr_Type())
aclMacAceSourceMacAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:aclMacAceSourceMacAddr.setStatus(_A)
class _AclMacAceSourceMacAddrBitmask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_AclMacAceSourceMacAddrBitmask_Type.__name__=_I
_AclMacAceSourceMacAddrBitmask_Object=MibTableColumn
aclMacAceSourceMacAddrBitmask=_AclMacAceSourceMacAddrBitmask_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,2,1,7),_AclMacAceSourceMacAddrBitmask_Type())
aclMacAceSourceMacAddrBitmask.setMaxAccess(_D)
if mibBuilder.loadTexts:aclMacAceSourceMacAddrBitmask.setStatus(_A)
class _AclMacAceDestMacAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_AclMacAceDestMacAddr_Type.__name__=_I
_AclMacAceDestMacAddr_Object=MibTableColumn
aclMacAceDestMacAddr=_AclMacAceDestMacAddr_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,2,1,8),_AclMacAceDestMacAddr_Type())
aclMacAceDestMacAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:aclMacAceDestMacAddr.setStatus(_A)
class _AclMacAceDestMacAddrBitmask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_AclMacAceDestMacAddrBitmask_Type.__name__=_I
_AclMacAceDestMacAddrBitmask_Object=MibTableColumn
aclMacAceDestMacAddrBitmask=_AclMacAceDestMacAddrBitmask_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,2,1,9),_AclMacAceDestMacAddrBitmask_Type())
aclMacAceDestMacAddrBitmask.setMaxAccess(_D)
if mibBuilder.loadTexts:aclMacAceDestMacAddrBitmask.setStatus(_A)
class _AclMacAceVidOp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3)))
_AclMacAceVidOp_Type.__name__=_B
_AclMacAceVidOp_Object=MibTableColumn
aclMacAceVidOp=_AclMacAceVidOp_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,2,1,10),_AclMacAceVidOp_Type())
aclMacAceVidOp.setMaxAccess(_D)
if mibBuilder.loadTexts:aclMacAceVidOp.setStatus(_A)
class _AclMacAceMinVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_AclMacAceMinVid_Type.__name__=_B
_AclMacAceMinVid_Object=MibTableColumn
aclMacAceMinVid=_AclMacAceMinVid_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,2,1,11),_AclMacAceMinVid_Type())
aclMacAceMinVid.setMaxAccess(_D)
if mibBuilder.loadTexts:aclMacAceMinVid.setStatus(_A)
class _AclMacAceVidBitmask_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_AclMacAceVidBitmask_Type.__name__=_B
_AclMacAceVidBitmask_Object=MibTableColumn
aclMacAceVidBitmask=_AclMacAceVidBitmask_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,2,1,12),_AclMacAceVidBitmask_Type())
aclMacAceVidBitmask.setMaxAccess(_D)
if mibBuilder.loadTexts:aclMacAceVidBitmask.setStatus(_A)
class _AclMacAceMaxVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_AclMacAceMaxVid_Type.__name__=_B
_AclMacAceMaxVid_Object=MibTableColumn
aclMacAceMaxVid=_AclMacAceMaxVid_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,2,1,13),_AclMacAceMaxVid_Type())
aclMacAceMaxVid.setMaxAccess(_D)
if mibBuilder.loadTexts:aclMacAceMaxVid.setStatus(_A)
class _AclMacAceEtherTypeOp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3)))
_AclMacAceEtherTypeOp_Type.__name__=_B
_AclMacAceEtherTypeOp_Object=MibTableColumn
aclMacAceEtherTypeOp=_AclMacAceEtherTypeOp_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,2,1,14),_AclMacAceEtherTypeOp_Type())
aclMacAceEtherTypeOp.setMaxAccess(_D)
if mibBuilder.loadTexts:aclMacAceEtherTypeOp.setStatus(_A)
class _AclMacAceEtherTypeBitmask_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AclMacAceEtherTypeBitmask_Type.__name__=_B
_AclMacAceEtherTypeBitmask_Object=MibTableColumn
aclMacAceEtherTypeBitmask=_AclMacAceEtherTypeBitmask_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,2,1,15),_AclMacAceEtherTypeBitmask_Type())
aclMacAceEtherTypeBitmask.setMaxAccess(_D)
if mibBuilder.loadTexts:aclMacAceEtherTypeBitmask.setStatus(_A)
class _AclMacAceMinEtherType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1536,65535))
_AclMacAceMinEtherType_Type.__name__=_B
_AclMacAceMinEtherType_Object=MibTableColumn
aclMacAceMinEtherType=_AclMacAceMinEtherType_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,2,1,16),_AclMacAceMinEtherType_Type())
aclMacAceMinEtherType.setMaxAccess(_D)
if mibBuilder.loadTexts:aclMacAceMinEtherType.setStatus(_A)
class _AclMacAceMaxEtherType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1536,65535))
_AclMacAceMaxEtherType_Type.__name__=_B
_AclMacAceMaxEtherType_Object=MibTableColumn
aclMacAceMaxEtherType=_AclMacAceMaxEtherType_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,2,1,17),_AclMacAceMaxEtherType_Type())
aclMacAceMaxEtherType.setMaxAccess(_D)
if mibBuilder.loadTexts:aclMacAceMaxEtherType.setStatus(_A)
_AclMacAceStatus_Type=RowStatus
_AclMacAceStatus_Object=MibTableColumn
aclMacAceStatus=_AclMacAceStatus_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,2,1,18),_AclMacAceStatus_Type())
aclMacAceStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:aclMacAceStatus.setStatus(_A)
_AclAclGroupTable_Object=MibTable
aclAclGroupTable=_AclAclGroupTable_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,3))
if mibBuilder.loadTexts:aclAclGroupTable.setStatus(_A)
_AclAclGroupEntry_Object=MibTableRow
aclAclGroupEntry=_AclAclGroupEntry_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,3,1))
aclAclGroupEntry.setIndexNames((0,_F,_AY))
if mibBuilder.loadTexts:aclAclGroupEntry.setStatus(_A)
_AclAclGroupIfIndex_Type=Integer32
_AclAclGroupIfIndex_Object=MibTableColumn
aclAclGroupIfIndex=_AclAclGroupIfIndex_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,3,1,1),_AclAclGroupIfIndex_Type())
aclAclGroupIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:aclAclGroupIfIndex.setStatus(_A)
class _AclAclGroupIngressIpAcl_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_AclAclGroupIngressIpAcl_Type.__name__=_H
_AclAclGroupIngressIpAcl_Object=MibTableColumn
aclAclGroupIngressIpAcl=_AclAclGroupIngressIpAcl_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,3,1,2),_AclAclGroupIngressIpAcl_Type())
aclAclGroupIngressIpAcl.setMaxAccess(_C)
if mibBuilder.loadTexts:aclAclGroupIngressIpAcl.setStatus(_A)
class _AclAclGroupEgressIpAcl_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_AclAclGroupEgressIpAcl_Type.__name__=_H
_AclAclGroupEgressIpAcl_Object=MibTableColumn
aclAclGroupEgressIpAcl=_AclAclGroupEgressIpAcl_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,3,1,3),_AclAclGroupEgressIpAcl_Type())
aclAclGroupEgressIpAcl.setMaxAccess(_C)
if mibBuilder.loadTexts:aclAclGroupEgressIpAcl.setStatus(_A)
class _AclAclGroupIngressMacAcl_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_AclAclGroupIngressMacAcl_Type.__name__=_H
_AclAclGroupIngressMacAcl_Object=MibTableColumn
aclAclGroupIngressMacAcl=_AclAclGroupIngressMacAcl_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,3,1,4),_AclAclGroupIngressMacAcl_Type())
aclAclGroupIngressMacAcl.setMaxAccess(_C)
if mibBuilder.loadTexts:aclAclGroupIngressMacAcl.setStatus(_A)
class _AclAclGroupEgressMacAcl_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_AclAclGroupEgressMacAcl_Type.__name__=_H
_AclAclGroupEgressMacAcl_Object=MibTableColumn
aclAclGroupEgressMacAcl=_AclAclGroupEgressMacAcl_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,3,1,5),_AclAclGroupEgressMacAcl_Type())
aclAclGroupEgressMacAcl.setMaxAccess(_C)
if mibBuilder.loadTexts:aclAclGroupEgressMacAcl.setStatus(_A)
_AclIngressIpMaskTable_Object=MibTable
aclIngressIpMaskTable=_AclIngressIpMaskTable_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,4))
if mibBuilder.loadTexts:aclIngressIpMaskTable.setStatus(_A)
_AclIngressIpMaskEntry_Object=MibTableRow
aclIngressIpMaskEntry=_AclIngressIpMaskEntry_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,4,1))
aclIngressIpMaskEntry.setIndexNames((0,_F,_AZ))
if mibBuilder.loadTexts:aclIngressIpMaskEntry.setStatus(_A)
class _AclIngressIpMaskIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_AclIngressIpMaskIndex_Type.__name__=_B
_AclIngressIpMaskIndex_Object=MibTableColumn
aclIngressIpMaskIndex=_AclIngressIpMaskIndex_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,4,1,1),_AclIngressIpMaskIndex_Type())
aclIngressIpMaskIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:aclIngressIpMaskIndex.setStatus(_A)
class _AclIngressIpMaskPrecedence_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_AclIngressIpMaskPrecedence_Type.__name__=_B
_AclIngressIpMaskPrecedence_Object=MibTableColumn
aclIngressIpMaskPrecedence=_AclIngressIpMaskPrecedence_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,4,1,2),_AclIngressIpMaskPrecedence_Type())
aclIngressIpMaskPrecedence.setMaxAccess(_E)
if mibBuilder.loadTexts:aclIngressIpMaskPrecedence.setStatus(_A)
_AclIngressIpMaskIsEnableTos_Type=EnabledStatus
_AclIngressIpMaskIsEnableTos_Object=MibTableColumn
aclIngressIpMaskIsEnableTos=_AclIngressIpMaskIsEnableTos_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,4,1,3),_AclIngressIpMaskIsEnableTos_Type())
aclIngressIpMaskIsEnableTos.setMaxAccess(_D)
if mibBuilder.loadTexts:aclIngressIpMaskIsEnableTos.setStatus(_A)
_AclIngressIpMaskIsEnableDscp_Type=EnabledStatus
_AclIngressIpMaskIsEnableDscp_Object=MibTableColumn
aclIngressIpMaskIsEnableDscp=_AclIngressIpMaskIsEnableDscp_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,4,1,4),_AclIngressIpMaskIsEnableDscp_Type())
aclIngressIpMaskIsEnableDscp.setMaxAccess(_D)
if mibBuilder.loadTexts:aclIngressIpMaskIsEnableDscp.setStatus(_A)
_AclIngressIpMaskIsEnablePrecedence_Type=EnabledStatus
_AclIngressIpMaskIsEnablePrecedence_Object=MibTableColumn
aclIngressIpMaskIsEnablePrecedence=_AclIngressIpMaskIsEnablePrecedence_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,4,1,5),_AclIngressIpMaskIsEnablePrecedence_Type())
aclIngressIpMaskIsEnablePrecedence.setMaxAccess(_D)
if mibBuilder.loadTexts:aclIngressIpMaskIsEnablePrecedence.setStatus(_A)
_AclIngressIpMaskIsEnableProtocol_Type=EnabledStatus
_AclIngressIpMaskIsEnableProtocol_Object=MibTableColumn
aclIngressIpMaskIsEnableProtocol=_AclIngressIpMaskIsEnableProtocol_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,4,1,6),_AclIngressIpMaskIsEnableProtocol_Type())
aclIngressIpMaskIsEnableProtocol.setMaxAccess(_D)
if mibBuilder.loadTexts:aclIngressIpMaskIsEnableProtocol.setStatus(_A)
class _AclIngressIpMaskSourceIpAddrBitmask_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_AclIngressIpMaskSourceIpAddrBitmask_Type.__name__=_J
_AclIngressIpMaskSourceIpAddrBitmask_Object=MibTableColumn
aclIngressIpMaskSourceIpAddrBitmask=_AclIngressIpMaskSourceIpAddrBitmask_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,4,1,7),_AclIngressIpMaskSourceIpAddrBitmask_Type())
aclIngressIpMaskSourceIpAddrBitmask.setMaxAccess(_D)
if mibBuilder.loadTexts:aclIngressIpMaskSourceIpAddrBitmask.setStatus(_A)
class _AclIngressIpMaskDestIpAddrBitmask_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_AclIngressIpMaskDestIpAddrBitmask_Type.__name__=_J
_AclIngressIpMaskDestIpAddrBitmask_Object=MibTableColumn
aclIngressIpMaskDestIpAddrBitmask=_AclIngressIpMaskDestIpAddrBitmask_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,4,1,8),_AclIngressIpMaskDestIpAddrBitmask_Type())
aclIngressIpMaskDestIpAddrBitmask.setMaxAccess(_D)
if mibBuilder.loadTexts:aclIngressIpMaskDestIpAddrBitmask.setStatus(_A)
class _AclIngressIpMaskSourcePortBitmask_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AclIngressIpMaskSourcePortBitmask_Type.__name__=_B
_AclIngressIpMaskSourcePortBitmask_Object=MibTableColumn
aclIngressIpMaskSourcePortBitmask=_AclIngressIpMaskSourcePortBitmask_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,4,1,9),_AclIngressIpMaskSourcePortBitmask_Type())
aclIngressIpMaskSourcePortBitmask.setMaxAccess(_D)
if mibBuilder.loadTexts:aclIngressIpMaskSourcePortBitmask.setStatus(_A)
class _AclIngressIpMaskDestPortBitmask_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AclIngressIpMaskDestPortBitmask_Type.__name__=_B
_AclIngressIpMaskDestPortBitmask_Object=MibTableColumn
aclIngressIpMaskDestPortBitmask=_AclIngressIpMaskDestPortBitmask_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,4,1,10),_AclIngressIpMaskDestPortBitmask_Type())
aclIngressIpMaskDestPortBitmask.setMaxAccess(_D)
if mibBuilder.loadTexts:aclIngressIpMaskDestPortBitmask.setStatus(_A)
class _AclIngressIpMaskControlCodeBitmask_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_AclIngressIpMaskControlCodeBitmask_Type.__name__=_B
_AclIngressIpMaskControlCodeBitmask_Object=MibTableColumn
aclIngressIpMaskControlCodeBitmask=_AclIngressIpMaskControlCodeBitmask_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,4,1,11),_AclIngressIpMaskControlCodeBitmask_Type())
aclIngressIpMaskControlCodeBitmask.setMaxAccess(_D)
if mibBuilder.loadTexts:aclIngressIpMaskControlCodeBitmask.setStatus(_A)
_AclIngressIpMaskStatus_Type=RowStatus
_AclIngressIpMaskStatus_Object=MibTableColumn
aclIngressIpMaskStatus=_AclIngressIpMaskStatus_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,4,1,12),_AclIngressIpMaskStatus_Type())
aclIngressIpMaskStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:aclIngressIpMaskStatus.setStatus(_A)
_AclEgressIpMaskTable_Object=MibTable
aclEgressIpMaskTable=_AclEgressIpMaskTable_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,5))
if mibBuilder.loadTexts:aclEgressIpMaskTable.setStatus(_A)
_AclEgressIpMaskEntry_Object=MibTableRow
aclEgressIpMaskEntry=_AclEgressIpMaskEntry_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,5,1))
aclEgressIpMaskEntry.setIndexNames((0,_F,_Aa))
if mibBuilder.loadTexts:aclEgressIpMaskEntry.setStatus(_A)
class _AclEgressIpMaskIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_AclEgressIpMaskIndex_Type.__name__=_B
_AclEgressIpMaskIndex_Object=MibTableColumn
aclEgressIpMaskIndex=_AclEgressIpMaskIndex_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,5,1,1),_AclEgressIpMaskIndex_Type())
aclEgressIpMaskIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:aclEgressIpMaskIndex.setStatus(_A)
class _AclEgressIpMaskPrecedence_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_AclEgressIpMaskPrecedence_Type.__name__=_B
_AclEgressIpMaskPrecedence_Object=MibTableColumn
aclEgressIpMaskPrecedence=_AclEgressIpMaskPrecedence_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,5,1,2),_AclEgressIpMaskPrecedence_Type())
aclEgressIpMaskPrecedence.setMaxAccess(_E)
if mibBuilder.loadTexts:aclEgressIpMaskPrecedence.setStatus(_A)
_AclEgressIpMaskIsEnableTos_Type=EnabledStatus
_AclEgressIpMaskIsEnableTos_Object=MibTableColumn
aclEgressIpMaskIsEnableTos=_AclEgressIpMaskIsEnableTos_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,5,1,3),_AclEgressIpMaskIsEnableTos_Type())
aclEgressIpMaskIsEnableTos.setMaxAccess(_D)
if mibBuilder.loadTexts:aclEgressIpMaskIsEnableTos.setStatus(_A)
_AclEgressIpMaskIsEnableDscp_Type=EnabledStatus
_AclEgressIpMaskIsEnableDscp_Object=MibTableColumn
aclEgressIpMaskIsEnableDscp=_AclEgressIpMaskIsEnableDscp_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,5,1,4),_AclEgressIpMaskIsEnableDscp_Type())
aclEgressIpMaskIsEnableDscp.setMaxAccess(_D)
if mibBuilder.loadTexts:aclEgressIpMaskIsEnableDscp.setStatus(_A)
_AclEgressIpMaskIsEnablePrecedence_Type=EnabledStatus
_AclEgressIpMaskIsEnablePrecedence_Object=MibTableColumn
aclEgressIpMaskIsEnablePrecedence=_AclEgressIpMaskIsEnablePrecedence_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,5,1,5),_AclEgressIpMaskIsEnablePrecedence_Type())
aclEgressIpMaskIsEnablePrecedence.setMaxAccess(_D)
if mibBuilder.loadTexts:aclEgressIpMaskIsEnablePrecedence.setStatus(_A)
_AclEgressIpMaskIsEnableProtocol_Type=EnabledStatus
_AclEgressIpMaskIsEnableProtocol_Object=MibTableColumn
aclEgressIpMaskIsEnableProtocol=_AclEgressIpMaskIsEnableProtocol_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,5,1,6),_AclEgressIpMaskIsEnableProtocol_Type())
aclEgressIpMaskIsEnableProtocol.setMaxAccess(_D)
if mibBuilder.loadTexts:aclEgressIpMaskIsEnableProtocol.setStatus(_A)
class _AclEgressIpMaskSourceIpAddrBitmask_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_AclEgressIpMaskSourceIpAddrBitmask_Type.__name__=_J
_AclEgressIpMaskSourceIpAddrBitmask_Object=MibTableColumn
aclEgressIpMaskSourceIpAddrBitmask=_AclEgressIpMaskSourceIpAddrBitmask_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,5,1,7),_AclEgressIpMaskSourceIpAddrBitmask_Type())
aclEgressIpMaskSourceIpAddrBitmask.setMaxAccess(_D)
if mibBuilder.loadTexts:aclEgressIpMaskSourceIpAddrBitmask.setStatus(_A)
class _AclEgressIpMaskDestIpAddrBitmask_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_AclEgressIpMaskDestIpAddrBitmask_Type.__name__=_J
_AclEgressIpMaskDestIpAddrBitmask_Object=MibTableColumn
aclEgressIpMaskDestIpAddrBitmask=_AclEgressIpMaskDestIpAddrBitmask_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,5,1,8),_AclEgressIpMaskDestIpAddrBitmask_Type())
aclEgressIpMaskDestIpAddrBitmask.setMaxAccess(_D)
if mibBuilder.loadTexts:aclEgressIpMaskDestIpAddrBitmask.setStatus(_A)
class _AclEgressIpMaskSourcePortBitmask_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AclEgressIpMaskSourcePortBitmask_Type.__name__=_B
_AclEgressIpMaskSourcePortBitmask_Object=MibTableColumn
aclEgressIpMaskSourcePortBitmask=_AclEgressIpMaskSourcePortBitmask_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,5,1,9),_AclEgressIpMaskSourcePortBitmask_Type())
aclEgressIpMaskSourcePortBitmask.setMaxAccess(_D)
if mibBuilder.loadTexts:aclEgressIpMaskSourcePortBitmask.setStatus(_A)
class _AclEgressIpMaskDestPortBitmask_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AclEgressIpMaskDestPortBitmask_Type.__name__=_B
_AclEgressIpMaskDestPortBitmask_Object=MibTableColumn
aclEgressIpMaskDestPortBitmask=_AclEgressIpMaskDestPortBitmask_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,5,1,10),_AclEgressIpMaskDestPortBitmask_Type())
aclEgressIpMaskDestPortBitmask.setMaxAccess(_D)
if mibBuilder.loadTexts:aclEgressIpMaskDestPortBitmask.setStatus(_A)
class _AclEgressIpMaskControlCodeBitmask_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_AclEgressIpMaskControlCodeBitmask_Type.__name__=_B
_AclEgressIpMaskControlCodeBitmask_Object=MibTableColumn
aclEgressIpMaskControlCodeBitmask=_AclEgressIpMaskControlCodeBitmask_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,5,1,11),_AclEgressIpMaskControlCodeBitmask_Type())
aclEgressIpMaskControlCodeBitmask.setMaxAccess(_D)
if mibBuilder.loadTexts:aclEgressIpMaskControlCodeBitmask.setStatus(_A)
_AclEgressIpMaskStatus_Type=RowStatus
_AclEgressIpMaskStatus_Object=MibTableColumn
aclEgressIpMaskStatus=_AclEgressIpMaskStatus_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,5,1,12),_AclEgressIpMaskStatus_Type())
aclEgressIpMaskStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:aclEgressIpMaskStatus.setStatus(_A)
_AclIngressMacMaskTable_Object=MibTable
aclIngressMacMaskTable=_AclIngressMacMaskTable_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,6))
if mibBuilder.loadTexts:aclIngressMacMaskTable.setStatus(_A)
_AclIngressMacMaskEntry_Object=MibTableRow
aclIngressMacMaskEntry=_AclIngressMacMaskEntry_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,6,1))
aclIngressMacMaskEntry.setIndexNames((0,_F,_Ab))
if mibBuilder.loadTexts:aclIngressMacMaskEntry.setStatus(_A)
class _AclIngressMacMaskIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_AclIngressMacMaskIndex_Type.__name__=_B
_AclIngressMacMaskIndex_Object=MibTableColumn
aclIngressMacMaskIndex=_AclIngressMacMaskIndex_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,6,1,1),_AclIngressMacMaskIndex_Type())
aclIngressMacMaskIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:aclIngressMacMaskIndex.setStatus(_A)
class _AclIngressMacMaskPrecedence_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_AclIngressMacMaskPrecedence_Type.__name__=_B
_AclIngressMacMaskPrecedence_Object=MibTableColumn
aclIngressMacMaskPrecedence=_AclIngressMacMaskPrecedence_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,6,1,2),_AclIngressMacMaskPrecedence_Type())
aclIngressMacMaskPrecedence.setMaxAccess(_E)
if mibBuilder.loadTexts:aclIngressMacMaskPrecedence.setStatus(_A)
class _AclIngressMacMaskSourceMacAddrBitmask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_AclIngressMacMaskSourceMacAddrBitmask_Type.__name__=_I
_AclIngressMacMaskSourceMacAddrBitmask_Object=MibTableColumn
aclIngressMacMaskSourceMacAddrBitmask=_AclIngressMacMaskSourceMacAddrBitmask_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,6,1,3),_AclIngressMacMaskSourceMacAddrBitmask_Type())
aclIngressMacMaskSourceMacAddrBitmask.setMaxAccess(_D)
if mibBuilder.loadTexts:aclIngressMacMaskSourceMacAddrBitmask.setStatus(_A)
class _AclIngressMacMaskDestMacAddrBitmask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_AclIngressMacMaskDestMacAddrBitmask_Type.__name__=_I
_AclIngressMacMaskDestMacAddrBitmask_Object=MibTableColumn
aclIngressMacMaskDestMacAddrBitmask=_AclIngressMacMaskDestMacAddrBitmask_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,6,1,4),_AclIngressMacMaskDestMacAddrBitmask_Type())
aclIngressMacMaskDestMacAddrBitmask.setMaxAccess(_D)
if mibBuilder.loadTexts:aclIngressMacMaskDestMacAddrBitmask.setStatus(_A)
class _AclIngressMacMaskVidBitmask_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_AclIngressMacMaskVidBitmask_Type.__name__=_B
_AclIngressMacMaskVidBitmask_Object=MibTableColumn
aclIngressMacMaskVidBitmask=_AclIngressMacMaskVidBitmask_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,6,1,5),_AclIngressMacMaskVidBitmask_Type())
aclIngressMacMaskVidBitmask.setMaxAccess(_D)
if mibBuilder.loadTexts:aclIngressMacMaskVidBitmask.setStatus(_A)
class _AclIngressMacMaskEtherTypeBitmask_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AclIngressMacMaskEtherTypeBitmask_Type.__name__=_B
_AclIngressMacMaskEtherTypeBitmask_Object=MibTableColumn
aclIngressMacMaskEtherTypeBitmask=_AclIngressMacMaskEtherTypeBitmask_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,6,1,6),_AclIngressMacMaskEtherTypeBitmask_Type())
aclIngressMacMaskEtherTypeBitmask.setMaxAccess(_D)
if mibBuilder.loadTexts:aclIngressMacMaskEtherTypeBitmask.setStatus(_A)
_AclIngressMacMaskIsEnablePktformat_Type=EnabledStatus
_AclIngressMacMaskIsEnablePktformat_Object=MibTableColumn
aclIngressMacMaskIsEnablePktformat=_AclIngressMacMaskIsEnablePktformat_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,6,1,7),_AclIngressMacMaskIsEnablePktformat_Type())
aclIngressMacMaskIsEnablePktformat.setMaxAccess(_D)
if mibBuilder.loadTexts:aclIngressMacMaskIsEnablePktformat.setStatus(_A)
_AclIngressMacMaskStatus_Type=RowStatus
_AclIngressMacMaskStatus_Object=MibTableColumn
aclIngressMacMaskStatus=_AclIngressMacMaskStatus_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,6,1,8),_AclIngressMacMaskStatus_Type())
aclIngressMacMaskStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:aclIngressMacMaskStatus.setStatus(_A)
_AclEgressMacMaskTable_Object=MibTable
aclEgressMacMaskTable=_AclEgressMacMaskTable_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,7))
if mibBuilder.loadTexts:aclEgressMacMaskTable.setStatus(_A)
_AclEgressMacMaskEntry_Object=MibTableRow
aclEgressMacMaskEntry=_AclEgressMacMaskEntry_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,7,1))
aclEgressMacMaskEntry.setIndexNames((0,_F,_Ac))
if mibBuilder.loadTexts:aclEgressMacMaskEntry.setStatus(_A)
class _AclEgressMacMaskIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_AclEgressMacMaskIndex_Type.__name__=_B
_AclEgressMacMaskIndex_Object=MibTableColumn
aclEgressMacMaskIndex=_AclEgressMacMaskIndex_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,7,1,1),_AclEgressMacMaskIndex_Type())
aclEgressMacMaskIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:aclEgressMacMaskIndex.setStatus(_A)
class _AclEgressMacMaskPrecedence_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_AclEgressMacMaskPrecedence_Type.__name__=_B
_AclEgressMacMaskPrecedence_Object=MibTableColumn
aclEgressMacMaskPrecedence=_AclEgressMacMaskPrecedence_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,7,1,2),_AclEgressMacMaskPrecedence_Type())
aclEgressMacMaskPrecedence.setMaxAccess(_E)
if mibBuilder.loadTexts:aclEgressMacMaskPrecedence.setStatus(_A)
class _AclEgressMacMaskSourceMacAddrBitmask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_AclEgressMacMaskSourceMacAddrBitmask_Type.__name__=_I
_AclEgressMacMaskSourceMacAddrBitmask_Object=MibTableColumn
aclEgressMacMaskSourceMacAddrBitmask=_AclEgressMacMaskSourceMacAddrBitmask_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,7,1,3),_AclEgressMacMaskSourceMacAddrBitmask_Type())
aclEgressMacMaskSourceMacAddrBitmask.setMaxAccess(_D)
if mibBuilder.loadTexts:aclEgressMacMaskSourceMacAddrBitmask.setStatus(_A)
class _AclEgressMacMaskDestMacAddrBitmask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_AclEgressMacMaskDestMacAddrBitmask_Type.__name__=_I
_AclEgressMacMaskDestMacAddrBitmask_Object=MibTableColumn
aclEgressMacMaskDestMacAddrBitmask=_AclEgressMacMaskDestMacAddrBitmask_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,7,1,4),_AclEgressMacMaskDestMacAddrBitmask_Type())
aclEgressMacMaskDestMacAddrBitmask.setMaxAccess(_D)
if mibBuilder.loadTexts:aclEgressMacMaskDestMacAddrBitmask.setStatus(_A)
class _AclEgressMacMaskVidBitmask_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_AclEgressMacMaskVidBitmask_Type.__name__=_B
_AclEgressMacMaskVidBitmask_Object=MibTableColumn
aclEgressMacMaskVidBitmask=_AclEgressMacMaskVidBitmask_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,7,1,5),_AclEgressMacMaskVidBitmask_Type())
aclEgressMacMaskVidBitmask.setMaxAccess(_D)
if mibBuilder.loadTexts:aclEgressMacMaskVidBitmask.setStatus(_A)
class _AclEgressMacMaskEtherTypeBitmask_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AclEgressMacMaskEtherTypeBitmask_Type.__name__=_B
_AclEgressMacMaskEtherTypeBitmask_Object=MibTableColumn
aclEgressMacMaskEtherTypeBitmask=_AclEgressMacMaskEtherTypeBitmask_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,7,1,6),_AclEgressMacMaskEtherTypeBitmask_Type())
aclEgressMacMaskEtherTypeBitmask.setMaxAccess(_D)
if mibBuilder.loadTexts:aclEgressMacMaskEtherTypeBitmask.setStatus(_A)
_AclEgressMacMaskIsEnablePktformat_Type=EnabledStatus
_AclEgressMacMaskIsEnablePktformat_Object=MibTableColumn
aclEgressMacMaskIsEnablePktformat=_AclEgressMacMaskIsEnablePktformat_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,7,1,7),_AclEgressMacMaskIsEnablePktformat_Type())
aclEgressMacMaskIsEnablePktformat.setMaxAccess(_D)
if mibBuilder.loadTexts:aclEgressMacMaskIsEnablePktformat.setStatus(_A)
_AclEgressMacMaskStatus_Type=RowStatus
_AclEgressMacMaskStatus_Object=MibTableColumn
aclEgressMacMaskStatus=_AclEgressMacMaskStatus_Object((1,3,6,1,4,1,52,4,12,30,1,17,7,7,1,8),_AclEgressMacMaskStatus_Type())
aclEgressMacMaskStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:aclEgressMacMaskStatus.setStatus(_A)
_SysLogMgt_ObjectIdentity=ObjectIdentity
sysLogMgt=_SysLogMgt_ObjectIdentity((1,3,6,1,4,1,52,4,12,30,1,19))
_SysLogStatus_Type=EnabledStatus
_SysLogStatus_Object=MibScalar
sysLogStatus=_SysLogStatus_Object((1,3,6,1,4,1,52,4,12,30,1,19,1),_SysLogStatus_Type())
sysLogStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sysLogStatus.setStatus(_A)
class _SysLogHistoryFlashLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_SysLogHistoryFlashLevel_Type.__name__=_B
_SysLogHistoryFlashLevel_Object=MibScalar
sysLogHistoryFlashLevel=_SysLogHistoryFlashLevel_Object((1,3,6,1,4,1,52,4,12,30,1,19,2),_SysLogHistoryFlashLevel_Type())
sysLogHistoryFlashLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:sysLogHistoryFlashLevel.setStatus(_A)
class _SysLogHistoryRamLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_SysLogHistoryRamLevel_Type.__name__=_B
_SysLogHistoryRamLevel_Object=MibScalar
sysLogHistoryRamLevel=_SysLogHistoryRamLevel_Object((1,3,6,1,4,1,52,4,12,30,1,19,3),_SysLogHistoryRamLevel_Type())
sysLogHistoryRamLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:sysLogHistoryRamLevel.setStatus(_A)
_LineMgt_ObjectIdentity=ObjectIdentity
lineMgt=_LineMgt_ObjectIdentity((1,3,6,1,4,1,52,4,12,30,1,20))
_ConsoleMgt_ObjectIdentity=ObjectIdentity
consoleMgt=_ConsoleMgt_ObjectIdentity((1,3,6,1,4,1,52,4,12,30,1,20,1))
class _ConsoleDataBits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('databits7',1),('databits8',2)))
_ConsoleDataBits_Type.__name__=_B
_ConsoleDataBits_Object=MibScalar
consoleDataBits=_ConsoleDataBits_Object((1,3,6,1,4,1,52,4,12,30,1,20,1,1),_ConsoleDataBits_Type())
consoleDataBits.setMaxAccess(_C)
if mibBuilder.loadTexts:consoleDataBits.setStatus(_A)
class _ConsoleParity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('partyNone',1),('partyEven',2),('partyOdd',3)))
_ConsoleParity_Type.__name__=_B
_ConsoleParity_Object=MibScalar
consoleParity=_ConsoleParity_Object((1,3,6,1,4,1,52,4,12,30,1,20,1,2),_ConsoleParity_Type())
consoleParity.setMaxAccess(_C)
if mibBuilder.loadTexts:consoleParity.setStatus(_A)
class _ConsoleBaudRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('baudRate9600',1),('baudRate19200',2),('baudRate38400',3),('baudRate57600',4),('baudRate115200',5)))
_ConsoleBaudRate_Type.__name__=_B
_ConsoleBaudRate_Object=MibScalar
consoleBaudRate=_ConsoleBaudRate_Object((1,3,6,1,4,1,52,4,12,30,1,20,1,3),_ConsoleBaudRate_Type())
consoleBaudRate.setMaxAccess(_C)
if mibBuilder.loadTexts:consoleBaudRate.setStatus(_A)
class _ConsoleStopBits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('stopbits1',1),('stopbits2',2)))
_ConsoleStopBits_Type.__name__=_B
_ConsoleStopBits_Object=MibScalar
consoleStopBits=_ConsoleStopBits_Object((1,3,6,1,4,1,52,4,12,30,1,20,1,4),_ConsoleStopBits_Type())
consoleStopBits.setMaxAccess(_C)
if mibBuilder.loadTexts:consoleStopBits.setStatus(_A)
class _ConsoleExecTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ConsoleExecTimeout_Type.__name__=_B
_ConsoleExecTimeout_Object=MibScalar
consoleExecTimeout=_ConsoleExecTimeout_Object((1,3,6,1,4,1,52,4,12,30,1,20,1,5),_ConsoleExecTimeout_Type())
consoleExecTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:consoleExecTimeout.setStatus(_A)
class _ConsolePasswordThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,120))
_ConsolePasswordThreshold_Type.__name__=_B
_ConsolePasswordThreshold_Object=MibScalar
consolePasswordThreshold=_ConsolePasswordThreshold_Object((1,3,6,1,4,1,52,4,12,30,1,20,1,6),_ConsolePasswordThreshold_Type())
consolePasswordThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:consolePasswordThreshold.setStatus(_A)
class _ConsoleSilentTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ConsoleSilentTime_Type.__name__=_B
_ConsoleSilentTime_Object=MibScalar
consoleSilentTime=_ConsoleSilentTime_Object((1,3,6,1,4,1,52,4,12,30,1,20,1,7),_ConsoleSilentTime_Type())
consoleSilentTime.setMaxAccess(_C)
if mibBuilder.loadTexts:consoleSilentTime.setStatus(_A)
_TelnetMgt_ObjectIdentity=ObjectIdentity
telnetMgt=_TelnetMgt_ObjectIdentity((1,3,6,1,4,1,52,4,12,30,1,20,2))
class _TelnetExecTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_TelnetExecTimeout_Type.__name__=_B
_TelnetExecTimeout_Object=MibScalar
telnetExecTimeout=_TelnetExecTimeout_Object((1,3,6,1,4,1,52,4,12,30,1,20,2,1),_TelnetExecTimeout_Type())
telnetExecTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:telnetExecTimeout.setStatus(_A)
class _TelnetPasswordThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,120))
_TelnetPasswordThreshold_Type.__name__=_B
_TelnetPasswordThreshold_Object=MibScalar
telnetPasswordThreshold=_TelnetPasswordThreshold_Object((1,3,6,1,4,1,52,4,12,30,1,20,2,2),_TelnetPasswordThreshold_Type())
telnetPasswordThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:telnetPasswordThreshold.setStatus(_A)
_SysTimeMgt_ObjectIdentity=ObjectIdentity
sysTimeMgt=_SysTimeMgt_ObjectIdentity((1,3,6,1,4,1,52,4,12,30,1,23))
_SntpMgt_ObjectIdentity=ObjectIdentity
sntpMgt=_SntpMgt_ObjectIdentity((1,3,6,1,4,1,52,4,12,30,1,23,1))
_SntpStatus_Type=EnabledStatus
_SntpStatus_Object=MibScalar
sntpStatus=_SntpStatus_Object((1,3,6,1,4,1,52,4,12,30,1,23,1,1),_SntpStatus_Type())
sntpStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sntpStatus.setStatus(_A)
class _SntpServiceMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unicast',1),('broadcast',2),('anycast',3)))
_SntpServiceMode_Type.__name__=_B
_SntpServiceMode_Object=MibScalar
sntpServiceMode=_SntpServiceMode_Object((1,3,6,1,4,1,52,4,12,30,1,23,1,2),_SntpServiceMode_Type())
sntpServiceMode.setMaxAccess(_C)
if mibBuilder.loadTexts:sntpServiceMode.setStatus(_A)
class _SntpPollInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,16384))
_SntpPollInterval_Type.__name__=_B
_SntpPollInterval_Object=MibScalar
sntpPollInterval=_SntpPollInterval_Object((1,3,6,1,4,1,52,4,12,30,1,23,1,3),_SntpPollInterval_Type())
sntpPollInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:sntpPollInterval.setStatus(_A)
_SntpServerTable_Object=MibTable
sntpServerTable=_SntpServerTable_Object((1,3,6,1,4,1,52,4,12,30,1,23,1,4))
if mibBuilder.loadTexts:sntpServerTable.setStatus(_A)
_SntpServerEntry_Object=MibTableRow
sntpServerEntry=_SntpServerEntry_Object((1,3,6,1,4,1,52,4,12,30,1,23,1,4,1))
sntpServerEntry.setIndexNames((0,_F,_Ad))
if mibBuilder.loadTexts:sntpServerEntry.setStatus(_A)
class _SntpServerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_SntpServerIndex_Type.__name__=_B
_SntpServerIndex_Object=MibTableColumn
sntpServerIndex=_SntpServerIndex_Object((1,3,6,1,4,1,52,4,12,30,1,23,1,4,1,1),_SntpServerIndex_Type())
sntpServerIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:sntpServerIndex.setStatus(_A)
_SntpServerIpAddress_Type=IpAddress
_SntpServerIpAddress_Object=MibTableColumn
sntpServerIpAddress=_SntpServerIpAddress_Object((1,3,6,1,4,1,52,4,12,30,1,23,1,4,1,2),_SntpServerIpAddress_Type())
sntpServerIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:sntpServerIpAddress.setStatus(_A)
class _SysCurrentTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(20,20));fixedLength=20
_SysCurrentTime_Type.__name__=_H
_SysCurrentTime_Object=MibScalar
sysCurrentTime=_SysCurrentTime_Object((1,3,6,1,4,1,52,4,12,30,1,23,2),_SysCurrentTime_Type())
sysCurrentTime.setMaxAccess(_C)
if mibBuilder.loadTexts:sysCurrentTime.setStatus(_A)
class _SysTimeZone_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_SysTimeZone_Type.__name__=_H
_SysTimeZone_Object=MibScalar
sysTimeZone=_SysTimeZone_Object((1,3,6,1,4,1,52,4,12,30,1,23,3),_SysTimeZone_Type())
sysTimeZone.setMaxAccess(_C)
if mibBuilder.loadTexts:sysTimeZone.setStatus(_A)
class _SysTimeZoneName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_SysTimeZoneName_Type.__name__=_H
_SysTimeZoneName_Object=MibScalar
sysTimeZoneName=_SysTimeZoneName_Object((1,3,6,1,4,1,52,4,12,30,1,23,4),_SysTimeZoneName_Type())
sysTimeZoneName.setMaxAccess(_C)
if mibBuilder.loadTexts:sysTimeZoneName.setStatus(_A)
_FileMgt_ObjectIdentity=ObjectIdentity
fileMgt=_FileMgt_ObjectIdentity((1,3,6,1,4,1,52,4,12,30,1,24))
_FileCopyMgt_ObjectIdentity=ObjectIdentity
fileCopyMgt=_FileCopyMgt_ObjectIdentity((1,3,6,1,4,1,52,4,12,30,1,24,1))
class _FileCopySrcOperType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('file',1),(_Ae,2),(_Af,3),('tftp',4),('unit',5)))
_FileCopySrcOperType_Type.__name__=_B
_FileCopySrcOperType_Object=MibScalar
fileCopySrcOperType=_FileCopySrcOperType_Object((1,3,6,1,4,1,52,4,12,30,1,24,1,1),_FileCopySrcOperType_Type())
fileCopySrcOperType.setMaxAccess(_C)
if mibBuilder.loadTexts:fileCopySrcOperType.setStatus(_A)
class _FileCopySrcFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_FileCopySrcFileName_Type.__name__=_H
_FileCopySrcFileName_Object=MibScalar
fileCopySrcFileName=_FileCopySrcFileName_Object((1,3,6,1,4,1,52,4,12,30,1,24,1,2),_FileCopySrcFileName_Type())
fileCopySrcFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:fileCopySrcFileName.setStatus(_A)
class _FileCopyDestOperType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('file',1),(_Ae,2),(_Af,3),('tftp',4),('unit',5)))
_FileCopyDestOperType_Type.__name__=_B
_FileCopyDestOperType_Object=MibScalar
fileCopyDestOperType=_FileCopyDestOperType_Object((1,3,6,1,4,1,52,4,12,30,1,24,1,3),_FileCopyDestOperType_Type())
fileCopyDestOperType.setMaxAccess(_C)
if mibBuilder.loadTexts:fileCopyDestOperType.setStatus(_A)
class _FileCopyDestFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_FileCopyDestFileName_Type.__name__=_H
_FileCopyDestFileName_Object=MibScalar
fileCopyDestFileName=_FileCopyDestFileName_Object((1,3,6,1,4,1,52,4,12,30,1,24,1,4),_FileCopyDestFileName_Type())
fileCopyDestFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:fileCopyDestFileName.setStatus(_A)
class _FileCopyFileType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('opcode',1),('config',2),('bootRom',3)))
_FileCopyFileType_Type.__name__=_B
_FileCopyFileType_Object=MibScalar
fileCopyFileType=_FileCopyFileType_Object((1,3,6,1,4,1,52,4,12,30,1,24,1,5),_FileCopyFileType_Type())
fileCopyFileType.setMaxAccess(_C)
if mibBuilder.loadTexts:fileCopyFileType.setStatus(_A)
_FileCopyTftpServer_Type=IpAddress
_FileCopyTftpServer_Object=MibScalar
fileCopyTftpServer=_FileCopyTftpServer_Object((1,3,6,1,4,1,52,4,12,30,1,24,1,6),_FileCopyTftpServer_Type())
fileCopyTftpServer.setMaxAccess(_C)
if mibBuilder.loadTexts:fileCopyTftpServer.setStatus(_A)
_FileCopyUnitId_Type=Integer32
_FileCopyUnitId_Object=MibScalar
fileCopyUnitId=_FileCopyUnitId_Object((1,3,6,1,4,1,52,4,12,30,1,24,1,7),_FileCopyUnitId_Type())
fileCopyUnitId.setMaxAccess(_C)
if mibBuilder.loadTexts:fileCopyUnitId.setStatus(_A)
class _FileCopyAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('notCopying',1),('copy',2)))
_FileCopyAction_Type.__name__=_B
_FileCopyAction_Object=MibScalar
fileCopyAction=_FileCopyAction_Object((1,3,6,1,4,1,52,4,12,30,1,24,1,8),_FileCopyAction_Type())
fileCopyAction.setMaxAccess(_C)
if mibBuilder.loadTexts:fileCopyAction.setStatus(_A)
class _FileCopyStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31)));namedValues=NamedValues(*(('fileCopyTftpUndefError',1),('fileCopyTftpFileNotFound',2),('fileCopyTftpAccessViolation',3),('fileCopyTftpDiskFull',4),('fileCopyTftpIllegalOperation',5),('fileCopyTftpUnkownTransferId',6),('fileCopyTftpFileExisted',7),('fileCopyTftpNoSuchUser',8),('fileCopyTftpTimeout',9),('fileCopyTftpSendError',10),('fileCopyTftpReceiverError',11),('fileCopyTftpSocketOpenError',12),('fileCopyTftpSocketBindError',13),('fileCopyTftpUserCancel',14),('fileCopyTftpCompleted',15),('fileCopyParaError',16),('fileCopyBusy',17),('fileCopyUnknown',18),('fileCopyReadFileError',19),('fileCopySetStartupError',20),('fileCopyFileSizeExceed',21),('fileCopyMagicWordError',22),('fileCopyImageTypeError',23),('fileCopyHeaderChecksumError',24),('fileCopyImageChecksumError',25),('fileCopyWriteFlashFinish',26),('fileCopyWriteFlashError',27),('fileCopyWriteFlashProgramming',28),('fileCopyError',29),('fileCopySuccess',30),('fileCopyCompleted',31)))
_FileCopyStatus_Type.__name__=_B
_FileCopyStatus_Object=MibScalar
fileCopyStatus=_FileCopyStatus_Object((1,3,6,1,4,1,52,4,12,30,1,24,1,9),_FileCopyStatus_Type())
fileCopyStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:fileCopyStatus.setStatus(_A)
class _FileCopyTftpErrMsg_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_FileCopyTftpErrMsg_Type.__name__=_H
_FileCopyTftpErrMsg_Object=MibScalar
fileCopyTftpErrMsg=_FileCopyTftpErrMsg_Object((1,3,6,1,4,1,52,4,12,30,1,24,1,10),_FileCopyTftpErrMsg_Type())
fileCopyTftpErrMsg.setMaxAccess(_E)
if mibBuilder.loadTexts:fileCopyTftpErrMsg.setStatus(_A)
class _FileCopyTftpServerHostName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_FileCopyTftpServerHostName_Type.__name__=_H
_FileCopyTftpServerHostName_Object=MibScalar
fileCopyTftpServerHostName=_FileCopyTftpServerHostName_Object((1,3,6,1,4,1,52,4,12,30,1,24,1,11),_FileCopyTftpServerHostName_Type())
fileCopyTftpServerHostName.setMaxAccess(_C)
if mibBuilder.loadTexts:fileCopyTftpServerHostName.setStatus(_A)
_FileInfoMgt_ObjectIdentity=ObjectIdentity
fileInfoMgt=_FileInfoMgt_ObjectIdentity((1,3,6,1,4,1,52,4,12,30,1,24,2))
_FileInfoTable_Object=MibTable
fileInfoTable=_FileInfoTable_Object((1,3,6,1,4,1,52,4,12,30,1,24,2,1))
if mibBuilder.loadTexts:fileInfoTable.setStatus(_A)
_FileInfoEntry_Object=MibTableRow
fileInfoEntry=_FileInfoEntry_Object((1,3,6,1,4,1,52,4,12,30,1,24,2,1,1))
fileInfoEntry.setIndexNames((0,_F,_Ag),(1,_F,_Ah))
if mibBuilder.loadTexts:fileInfoEntry.setStatus(_A)
_FileInfoUnitID_Type=Integer32
_FileInfoUnitID_Object=MibTableColumn
fileInfoUnitID=_FileInfoUnitID_Object((1,3,6,1,4,1,52,4,12,30,1,24,2,1,1,1),_FileInfoUnitID_Type())
fileInfoUnitID.setMaxAccess(_G)
if mibBuilder.loadTexts:fileInfoUnitID.setStatus(_A)
class _FileInfoFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_FileInfoFileName_Type.__name__=_H
_FileInfoFileName_Object=MibTableColumn
fileInfoFileName=_FileInfoFileName_Object((1,3,6,1,4,1,52,4,12,30,1,24,2,1,1,2),_FileInfoFileName_Type())
fileInfoFileName.setMaxAccess(_G)
if mibBuilder.loadTexts:fileInfoFileName.setStatus(_A)
class _FileInfoFileType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('diag',1),('runtime',2),('syslog',3),('cmdlog',4),('config',5),('postlog',6),('private',7),('certificate',8),('webarchive',9)))
_FileInfoFileType_Type.__name__=_B
_FileInfoFileType_Object=MibTableColumn
fileInfoFileType=_FileInfoFileType_Object((1,3,6,1,4,1,52,4,12,30,1,24,2,1,1,3),_FileInfoFileType_Type())
fileInfoFileType.setMaxAccess(_E)
if mibBuilder.loadTexts:fileInfoFileType.setStatus(_A)
_FileInfoIsStartUp_Type=TruthValue
_FileInfoIsStartUp_Object=MibTableColumn
fileInfoIsStartUp=_FileInfoIsStartUp_Object((1,3,6,1,4,1,52,4,12,30,1,24,2,1,1,4),_FileInfoIsStartUp_Type())
fileInfoIsStartUp.setMaxAccess(_C)
if mibBuilder.loadTexts:fileInfoIsStartUp.setStatus(_A)
_FileInfoFileSize_Type=Integer32
_FileInfoFileSize_Object=MibTableColumn
fileInfoFileSize=_FileInfoFileSize_Object((1,3,6,1,4,1,52,4,12,30,1,24,2,1,1,5),_FileInfoFileSize_Type())
fileInfoFileSize.setMaxAccess(_E)
if mibBuilder.loadTexts:fileInfoFileSize.setStatus(_A)
class _FileInfoCreationTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(20,20));fixedLength=20
_FileInfoCreationTime_Type.__name__=_H
_FileInfoCreationTime_Object=MibTableColumn
fileInfoCreationTime=_FileInfoCreationTime_Object((1,3,6,1,4,1,52,4,12,30,1,24,2,1,1,6),_FileInfoCreationTime_Type())
fileInfoCreationTime.setMaxAccess(_E)
if mibBuilder.loadTexts:fileInfoCreationTime.setStatus(_A)
class _FileInfoDelete_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noDelete',1),('delete',2)))
_FileInfoDelete_Type.__name__=_B
_FileInfoDelete_Object=MibTableColumn
fileInfoDelete=_FileInfoDelete_Object((1,3,6,1,4,1,52,4,12,30,1,24,2,1,1,7),_FileInfoDelete_Type())
fileInfoDelete.setMaxAccess(_C)
if mibBuilder.loadTexts:fileInfoDelete.setStatus(_A)
_V2h124_24Notifications_ObjectIdentity=ObjectIdentity
v2h124_24Notifications=_V2h124_24Notifications_ObjectIdentity((1,3,6,1,4,1,52,4,12,30,2))
_V2h124_24Traps_ObjectIdentity=ObjectIdentity
v2h124_24Traps=_V2h124_24Traps_ObjectIdentity((1,3,6,1,4,1,52,4,12,30,2,1))
_V2h124_24TrapsPrefix_ObjectIdentity=ObjectIdentity
v2h124_24TrapsPrefix=_V2h124_24TrapsPrefix_ObjectIdentity((1,3,6,1,4,1,52,4,12,30,2,1,0))
_V2h124_24Conformance_ObjectIdentity=ObjectIdentity
v2h124_24Conformance=_V2h124_24Conformance_ObjectIdentity((1,3,6,1,4,1,52,4,12,30,3))
dot1dStpPortEntry.registerAugmentions((_F,_Ai))
staPortEntry.setIndexNames(*dot1dStpPortEntry.getIndexNames())
swPowerStatusChangeTrap=NotificationType((1,3,6,1,4,1,52,4,12,30,2,1,0,1))
swPowerStatusChangeTrap.setObjects(*((_F,_T),(_F,_U),(_F,_Aj)))
if mibBuilder.loadTexts:swPowerStatusChangeTrap.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'ValidStatus':ValidStatus,'v2h124-24MIB':v2h124_24MIB,'v2h124-24MIBObjects':v2h124_24MIBObjects,'switchMgt':switchMgt,'switchManagementVlan':switchManagementVlan,'v2h124switchNumber':v2h124switchNumber,'v2h124switchInfoTable':v2h124switchInfoTable,'v2h124switchInfoEntry':v2h124switchInfoEntry,_a:v2h124swUnitIndex,'v2h124swHardwareVer':v2h124swHardwareVer,'v2h124swMicrocodeVer':v2h124swMicrocodeVer,'v2h124swLoaderVer':v2h124swLoaderVer,'v2h124swBootRomVer':v2h124swBootRomVer,'v2h124swOpCodeVer':v2h124swOpCodeVer,'v2h124swPortNumber':v2h124swPortNumber,'v2h124swPowerStatus':v2h124swPowerStatus,'v2h124swRoleInSystem':v2h124swRoleInSystem,'v2h124swSerialNumber':v2h124swSerialNumber,'v2h124swExpansionSlot1':v2h124swExpansionSlot1,'v2h124swExpansionSlot2':v2h124swExpansionSlot2,'v2h124swServiceTag':v2h124swServiceTag,'switchOperState':switchOperState,'switchProductId':switchProductId,'swProdName':swProdName,'swProdManufacturer':swProdManufacturer,'swProdDescription':swProdDescription,'swProdVersion':swProdVersion,'swProdUrl':swProdUrl,'swIdentifier':swIdentifier,'swChassisServiceTag':swChassisServiceTag,'switchIndivPowerTable':switchIndivPowerTable,'switchIndivPowerEntry':switchIndivPowerEntry,_T:swIndivPowerUnitIndex,_U:swIndivPowerIndex,_Aj:swIndivPowerStatus,'portMgt':portMgt,'portTable':portTable,'portEntry':portEntry,_p:portIndex,'portName':portName,'portType':portType,'portSpeedDpxCfg':portSpeedDpxCfg,'portFlowCtrlCfg':portFlowCtrlCfg,'portCapabilities':portCapabilities,'portAutonegotiation':portAutonegotiation,'portSpeedDpxStatus':portSpeedDpxStatus,'portFlowCtrlStatus':portFlowCtrlStatus,'portTrunkIndex':portTrunkIndex,'trunkMgt':trunkMgt,'trunkMaxId':trunkMaxId,'trunkValidNumber':trunkValidNumber,'trunkTable':trunkTable,'trunkEntry':trunkEntry,_y:trunkIndex,'trunkPorts':trunkPorts,'trunkCreation':trunkCreation,'trunkStatus':trunkStatus,'lacpMgt':lacpMgt,'lacpPortTable':lacpPortTable,'lacpPortEntry':lacpPortEntry,_z:lacpPortIndex,'lacpPortStatus':lacpPortStatus,'staMgt':staMgt,'staSystemStatus':staSystemStatus,'staPortTable':staPortTable,_Ai:staPortEntry,'staPortFastForward':staPortFastForward,'staPortProtocolMigration':staPortProtocolMigration,'staPortAdminEdgePort':staPortAdminEdgePort,'staPortOperEdgePort':staPortOperEdgePort,'staPortAdminPointToPoint':staPortAdminPointToPoint,'staPortOperPointToPoint':staPortOperPointToPoint,'staPortLongPathCost':staPortLongPathCost,'staProtocolType':staProtocolType,'staTxHoldCount':staTxHoldCount,'staPathCostMethod':staPathCostMethod,'xstMgt':xstMgt,'xstInstanceCfgTable':xstInstanceCfgTable,'xstInstanceCfgEntry':xstInstanceCfgEntry,_X:xstInstanceCfgIndex,'xstInstanceCfgPriority':xstInstanceCfgPriority,'xstInstanceCfgTimeSinceTopologyChange':xstInstanceCfgTimeSinceTopologyChange,'xstInstanceCfgTopChanges':xstInstanceCfgTopChanges,'xstInstanceCfgDesignatedRoot':xstInstanceCfgDesignatedRoot,'xstInstanceCfgRootCost':xstInstanceCfgRootCost,'xstInstanceCfgRootPort':xstInstanceCfgRootPort,'xstInstanceCfgMaxAge':xstInstanceCfgMaxAge,'xstInstanceCfgHelloTime':xstInstanceCfgHelloTime,'xstInstanceCfgHoldTime':xstInstanceCfgHoldTime,'xstInstanceCfgForwardDelay':xstInstanceCfgForwardDelay,'xstInstanceCfgBridgeMaxAge':xstInstanceCfgBridgeMaxAge,'xstInstanceCfgBridgeHelloTime':xstInstanceCfgBridgeHelloTime,'xstInstanceCfgBridgeForwardDelay':xstInstanceCfgBridgeForwardDelay,'xstInstanceCfgTxHoldCount':xstInstanceCfgTxHoldCount,'xstInstanceCfgPathCostMethod':xstInstanceCfgPathCostMethod,'xstInstancePortTable':xstInstancePortTable,'xstInstancePortEntry':xstInstancePortEntry,'xstInstancePortPriority':xstInstancePortPriority,'xstInstancePortState':xstInstancePortState,'xstInstancePortEnable':xstInstancePortEnable,'xstInstancePortPathCost':xstInstancePortPathCost,'xstInstancePortDesignatedRoot':xstInstancePortDesignatedRoot,'xstInstancePortDesignatedCost':xstInstancePortDesignatedCost,'xstInstancePortDesignatedBridge':xstInstancePortDesignatedBridge,'xstInstancePortDesignatedPort':xstInstancePortDesignatedPort,'xstInstancePortForwardTransitions':xstInstancePortForwardTransitions,'xstInstancePortPortRole':xstInstancePortPortRole,'restartMgt':restartMgt,'restartOpCodeFile':restartOpCodeFile,'restartConfigFile':restartConfigFile,'restartControl':restartControl,'mirrorMgt':mirrorMgt,'mirrorTable':mirrorTable,'mirrorEntry':mirrorEntry,_A0:mirrorDestinationPort,_A1:mirrorSourcePort,'mirrorType':mirrorType,'mirrorStatus':mirrorStatus,'igmpSnoopMgt':igmpSnoopMgt,'igmpSnoopStatus':igmpSnoopStatus,'igmpSnoopQuerier':igmpSnoopQuerier,'igmpSnoopQueryCount':igmpSnoopQueryCount,'igmpSnoopQueryInterval':igmpSnoopQueryInterval,'igmpSnoopQueryMaxResponseTime':igmpSnoopQueryMaxResponseTime,'igmpSnoopRouterPortExpireTime':igmpSnoopRouterPortExpireTime,'igmpSnoopVersion':igmpSnoopVersion,'igmpSnoopRouterCurrentTable':igmpSnoopRouterCurrentTable,'igmpSnoopRouterCurrentEntry':igmpSnoopRouterCurrentEntry,_A2:igmpSnoopRouterCurrentVlanIndex,'igmpSnoopRouterCurrentPorts':igmpSnoopRouterCurrentPorts,'igmpSnoopRouterCurrentStatus':igmpSnoopRouterCurrentStatus,'igmpSnoopRouterStaticTable':igmpSnoopRouterStaticTable,'igmpSnoopRouterStaticEntry':igmpSnoopRouterStaticEntry,_A3:igmpSnoopRouterStaticVlanIndex,'igmpSnoopRouterStaticPorts':igmpSnoopRouterStaticPorts,'igmpSnoopRouterStaticStatus':igmpSnoopRouterStaticStatus,'igmpSnoopMulticastCurrentTable':igmpSnoopMulticastCurrentTable,'igmpSnoopMulticastCurrentEntry':igmpSnoopMulticastCurrentEntry,_A4:igmpSnoopMulticastCurrentVlanIndex,_A5:igmpSnoopMulticastCurrentIpAddress,'igmpSnoopMulticastCurrentPorts':igmpSnoopMulticastCurrentPorts,'igmpSnoopMulticastCurrentStatus':igmpSnoopMulticastCurrentStatus,'igmpSnoopMulticastStaticTable':igmpSnoopMulticastStaticTable,'igmpSnoopMulticastStaticEntry':igmpSnoopMulticastStaticEntry,_A6:igmpSnoopMulticastStaticVlanIndex,_A7:igmpSnoopMulticastStaticIpAddress,'igmpSnoopMulticastStaticPorts':igmpSnoopMulticastStaticPorts,'igmpSnoopMulticastStaticStatus':igmpSnoopMulticastStaticStatus,'ipMgt':ipMgt,'netConfigTable':netConfigTable,'netConfigEntry':netConfigEntry,_A8:netConfigIfIndex,_A9:netConfigIPAddress,_AA:netConfigSubnetMask,'netConfigPrimaryInterface':netConfigPrimaryInterface,'netConfigUnnumbered':netConfigUnnumbered,'netConfigStatus':netConfigStatus,'netDefaultGateway':netDefaultGateway,'ipHttpState':ipHttpState,'ipHttpPort':ipHttpPort,'ipDhcpRestart':ipDhcpRestart,'ipHttpsState':ipHttpsState,'ipHttpsPort':ipHttpsPort,'bcastStormMgt':bcastStormMgt,'bcastStormTable':bcastStormTable,'bcastStormEntry':bcastStormEntry,_AB:bcastStormIfIndex,'bcastStormStatus':bcastStormStatus,'bcastStormSampleType':bcastStormSampleType,'bcastStormPktRate':bcastStormPktRate,'bcastStormOctetRate':bcastStormOctetRate,'bcastStormPercent':bcastStormPercent,'vlanMgt':vlanMgt,'vlanTable':vlanTable,'vlanEntry':vlanEntry,_AC:vlanIndex,'vlanAddressMethod':vlanAddressMethod,'vlanPortTable':vlanPortTable,'vlanPortEntry':vlanPortEntry,_AD:vlanPortIndex,'vlanPortMode':vlanPortMode,'priorityMgt':priorityMgt,'prioIpPrecDscpStatus':prioIpPrecDscpStatus,'prioIpPrecTable':prioIpPrecTable,'prioIpPrecEntry':prioIpPrecEntry,_AF:prioIpPrecPort,_AG:prioIpPrecValue,'prioIpPrecCos':prioIpPrecCos,'prioIpPrecRestoreDefault':prioIpPrecRestoreDefault,'prioIpDscpTable':prioIpDscpTable,'prioIpDscpEntry':prioIpDscpEntry,_AH:prioIpDscpPort,_AI:prioIpDscpValue,'prioIpDscpCos':prioIpDscpCos,'prioIpDscpRestoreDefault':prioIpDscpRestoreDefault,'prioIpPortEnableStatus':prioIpPortEnableStatus,'prioIpPortTable':prioIpPortTable,'prioIpPortEntry':prioIpPortEntry,_AJ:prioIpPortPhysPort,_AK:prioIpPortValue,'prioIpPortCos':prioIpPortCos,'prioIpPortStatus':prioIpPortStatus,'prioCopy':prioCopy,'prioCopyIpPrec':prioCopyIpPrec,'prioCopyIpDscp':prioCopyIpDscp,'prioCopyIpPort':prioCopyIpPort,'prioWrrTable':prioWrrTable,'prioWrrEntry':prioWrrEntry,_AL:prioWrrTrafficClass,'prioWrrWeight':prioWrrWeight,'trapDestMgt':trapDestMgt,'trapDestTable':trapDestTable,'trapDestEntry':trapDestEntry,_AM:trapDestAddress,'trapDestCommunity':trapDestCommunity,'trapDestStatus':trapDestStatus,'trapDestVersion':trapDestVersion,'qosMgt':qosMgt,'rateLimitMgt':rateLimitMgt,'rateLimitStatus':rateLimitStatus,'rateLimitPortTable':rateLimitPortTable,'rateLimitPortEntry':rateLimitPortEntry,_AN:rlPortIndex,'rlPortInputLimit':rlPortInputLimit,'rlPortOutputLimit':rlPortOutputLimit,'rlPortInputStatus':rlPortInputStatus,'rlPortOutputStatus':rlPortOutputStatus,'markerMgt':markerMgt,'markerTable':markerTable,'markerEntry':markerEntry,_AO:markerIfIndex,_AP:markerAclName,'markerActionBitList':markerActionBitList,'markerDscp':markerDscp,'markerPrecedence':markerPrecedence,'markerPriority':markerPriority,'markerStatus':markerStatus,'cosMgt':cosMgt,'prioAclToCosMappingTable':prioAclToCosMappingTable,'prioAclToCosMappingEntry':prioAclToCosMappingEntry,_AQ:prioAclToCosMappingIfIndex,_AR:prioAclToCosMappingAclName,'prioAclToCosMappingCosValue':prioAclToCosMappingCosValue,'prioAclToCosMappingStatus':prioAclToCosMappingStatus,'securityMgt':securityMgt,'portSecurityMgt':portSecurityMgt,'portSecPortTable':portSecPortTable,'portSecPortEntry':portSecPortEntry,_AS:portSecPortIndex,'portSecPortStatus':portSecPortStatus,'portSecAction':portSecAction,'portSecMaxMacCount':portSecMaxMacCount,'radiusMgt':radiusMgt,'radiusServerAddress':radiusServerAddress,'radiusServerPortNumber':radiusServerPortNumber,'radiusServerKey':radiusServerKey,'radiusServerRetransmit':radiusServerRetransmit,'radiusServerTimeout':radiusServerTimeout,'tacacsMgt':tacacsMgt,'tacacsServerAddress':tacacsServerAddress,'tacacsServerPortNumber':tacacsServerPortNumber,'tacacsServerKey':tacacsServerKey,'sshMgt':sshMgt,'sshServerStatus':sshServerStatus,'sshServerMajorVersion':sshServerMajorVersion,'sshServerMinorVersion':sshServerMinorVersion,'sshTimeout':sshTimeout,'sshAuthRetries':sshAuthRetries,'sshConnInfoTable':sshConnInfoTable,'sshConnInfoEntry':sshConnInfoEntry,_AT:sshConnID,'sshConnMajorVersion':sshConnMajorVersion,'sshConnMinorVersion':sshConnMinorVersion,'sshConnEncryptionType':sshConnEncryptionType,'sshConnStatus':sshConnStatus,'sshConnUserName':sshConnUserName,'sshDisconnect':sshDisconnect,'aclMgt':aclMgt,'aclIpAceTable':aclIpAceTable,'aclIpAceEntry':aclIpAceEntry,_AU:aclIpAceName,_AV:aclIpAceIndex,'aclIpAcePrecedence':aclIpAcePrecedence,'aclIpAceAction':aclIpAceAction,'aclIpAceSourceIpAddr':aclIpAceSourceIpAddr,'aclIpAceSourceIpAddrBitmask':aclIpAceSourceIpAddrBitmask,'aclIpAceDestIpAddr':aclIpAceDestIpAddr,'aclIpAceDestIpAddrBitmask':aclIpAceDestIpAddrBitmask,'aclIpAceProtocol':aclIpAceProtocol,'aclIpAcePrec':aclIpAcePrec,'aclIpAceTos':aclIpAceTos,'aclIpAceDscp':aclIpAceDscp,'aclIpAceSourcePortOp':aclIpAceSourcePortOp,'aclIpAceMinSourcePort':aclIpAceMinSourcePort,'aclIpAceMaxSourcePort':aclIpAceMaxSourcePort,'aclIpAceSourcePortBitmask':aclIpAceSourcePortBitmask,'aclIpAceDestPortOp':aclIpAceDestPortOp,'aclIpAceMinDestPort':aclIpAceMinDestPort,'aclIpAceMaxDestPort':aclIpAceMaxDestPort,'aclIpAceDestPortBitmask':aclIpAceDestPortBitmask,'aclIpAceControlCode':aclIpAceControlCode,'aclIpAceControlCodeBitmask':aclIpAceControlCodeBitmask,'aclIpAceStatus':aclIpAceStatus,'aclMacAceTable':aclMacAceTable,'aclMacAceEntry':aclMacAceEntry,_AW:aclMacAceName,_AX:aclMacAceIndex,'aclMacAcePrecedence':aclMacAcePrecedence,'aclMacAceAction':aclMacAceAction,'aclMacAcePktformat':aclMacAcePktformat,'aclMacAceSourceMacAddr':aclMacAceSourceMacAddr,'aclMacAceSourceMacAddrBitmask':aclMacAceSourceMacAddrBitmask,'aclMacAceDestMacAddr':aclMacAceDestMacAddr,'aclMacAceDestMacAddrBitmask':aclMacAceDestMacAddrBitmask,'aclMacAceVidOp':aclMacAceVidOp,'aclMacAceMinVid':aclMacAceMinVid,'aclMacAceVidBitmask':aclMacAceVidBitmask,'aclMacAceMaxVid':aclMacAceMaxVid,'aclMacAceEtherTypeOp':aclMacAceEtherTypeOp,'aclMacAceEtherTypeBitmask':aclMacAceEtherTypeBitmask,'aclMacAceMinEtherType':aclMacAceMinEtherType,'aclMacAceMaxEtherType':aclMacAceMaxEtherType,'aclMacAceStatus':aclMacAceStatus,'aclAclGroupTable':aclAclGroupTable,'aclAclGroupEntry':aclAclGroupEntry,_AY:aclAclGroupIfIndex,'aclAclGroupIngressIpAcl':aclAclGroupIngressIpAcl,'aclAclGroupEgressIpAcl':aclAclGroupEgressIpAcl,'aclAclGroupIngressMacAcl':aclAclGroupIngressMacAcl,'aclAclGroupEgressMacAcl':aclAclGroupEgressMacAcl,'aclIngressIpMaskTable':aclIngressIpMaskTable,'aclIngressIpMaskEntry':aclIngressIpMaskEntry,_AZ:aclIngressIpMaskIndex,'aclIngressIpMaskPrecedence':aclIngressIpMaskPrecedence,'aclIngressIpMaskIsEnableTos':aclIngressIpMaskIsEnableTos,'aclIngressIpMaskIsEnableDscp':aclIngressIpMaskIsEnableDscp,'aclIngressIpMaskIsEnablePrecedence':aclIngressIpMaskIsEnablePrecedence,'aclIngressIpMaskIsEnableProtocol':aclIngressIpMaskIsEnableProtocol,'aclIngressIpMaskSourceIpAddrBitmask':aclIngressIpMaskSourceIpAddrBitmask,'aclIngressIpMaskDestIpAddrBitmask':aclIngressIpMaskDestIpAddrBitmask,'aclIngressIpMaskSourcePortBitmask':aclIngressIpMaskSourcePortBitmask,'aclIngressIpMaskDestPortBitmask':aclIngressIpMaskDestPortBitmask,'aclIngressIpMaskControlCodeBitmask':aclIngressIpMaskControlCodeBitmask,'aclIngressIpMaskStatus':aclIngressIpMaskStatus,'aclEgressIpMaskTable':aclEgressIpMaskTable,'aclEgressIpMaskEntry':aclEgressIpMaskEntry,_Aa:aclEgressIpMaskIndex,'aclEgressIpMaskPrecedence':aclEgressIpMaskPrecedence,'aclEgressIpMaskIsEnableTos':aclEgressIpMaskIsEnableTos,'aclEgressIpMaskIsEnableDscp':aclEgressIpMaskIsEnableDscp,'aclEgressIpMaskIsEnablePrecedence':aclEgressIpMaskIsEnablePrecedence,'aclEgressIpMaskIsEnableProtocol':aclEgressIpMaskIsEnableProtocol,'aclEgressIpMaskSourceIpAddrBitmask':aclEgressIpMaskSourceIpAddrBitmask,'aclEgressIpMaskDestIpAddrBitmask':aclEgressIpMaskDestIpAddrBitmask,'aclEgressIpMaskSourcePortBitmask':aclEgressIpMaskSourcePortBitmask,'aclEgressIpMaskDestPortBitmask':aclEgressIpMaskDestPortBitmask,'aclEgressIpMaskControlCodeBitmask':aclEgressIpMaskControlCodeBitmask,'aclEgressIpMaskStatus':aclEgressIpMaskStatus,'aclIngressMacMaskTable':aclIngressMacMaskTable,'aclIngressMacMaskEntry':aclIngressMacMaskEntry,_Ab:aclIngressMacMaskIndex,'aclIngressMacMaskPrecedence':aclIngressMacMaskPrecedence,'aclIngressMacMaskSourceMacAddrBitmask':aclIngressMacMaskSourceMacAddrBitmask,'aclIngressMacMaskDestMacAddrBitmask':aclIngressMacMaskDestMacAddrBitmask,'aclIngressMacMaskVidBitmask':aclIngressMacMaskVidBitmask,'aclIngressMacMaskEtherTypeBitmask':aclIngressMacMaskEtherTypeBitmask,'aclIngressMacMaskIsEnablePktformat':aclIngressMacMaskIsEnablePktformat,'aclIngressMacMaskStatus':aclIngressMacMaskStatus,'aclEgressMacMaskTable':aclEgressMacMaskTable,'aclEgressMacMaskEntry':aclEgressMacMaskEntry,_Ac:aclEgressMacMaskIndex,'aclEgressMacMaskPrecedence':aclEgressMacMaskPrecedence,'aclEgressMacMaskSourceMacAddrBitmask':aclEgressMacMaskSourceMacAddrBitmask,'aclEgressMacMaskDestMacAddrBitmask':aclEgressMacMaskDestMacAddrBitmask,'aclEgressMacMaskVidBitmask':aclEgressMacMaskVidBitmask,'aclEgressMacMaskEtherTypeBitmask':aclEgressMacMaskEtherTypeBitmask,'aclEgressMacMaskIsEnablePktformat':aclEgressMacMaskIsEnablePktformat,'aclEgressMacMaskStatus':aclEgressMacMaskStatus,'sysLogMgt':sysLogMgt,'sysLogStatus':sysLogStatus,'sysLogHistoryFlashLevel':sysLogHistoryFlashLevel,'sysLogHistoryRamLevel':sysLogHistoryRamLevel,'lineMgt':lineMgt,'consoleMgt':consoleMgt,'consoleDataBits':consoleDataBits,'consoleParity':consoleParity,'consoleBaudRate':consoleBaudRate,'consoleStopBits':consoleStopBits,'consoleExecTimeout':consoleExecTimeout,'consolePasswordThreshold':consolePasswordThreshold,'consoleSilentTime':consoleSilentTime,'telnetMgt':telnetMgt,'telnetExecTimeout':telnetExecTimeout,'telnetPasswordThreshold':telnetPasswordThreshold,'sysTimeMgt':sysTimeMgt,'sntpMgt':sntpMgt,'sntpStatus':sntpStatus,'sntpServiceMode':sntpServiceMode,'sntpPollInterval':sntpPollInterval,'sntpServerTable':sntpServerTable,'sntpServerEntry':sntpServerEntry,_Ad:sntpServerIndex,'sntpServerIpAddress':sntpServerIpAddress,'sysCurrentTime':sysCurrentTime,'sysTimeZone':sysTimeZone,'sysTimeZoneName':sysTimeZoneName,'fileMgt':fileMgt,'fileCopyMgt':fileCopyMgt,'fileCopySrcOperType':fileCopySrcOperType,'fileCopySrcFileName':fileCopySrcFileName,'fileCopyDestOperType':fileCopyDestOperType,'fileCopyDestFileName':fileCopyDestFileName,'fileCopyFileType':fileCopyFileType,'fileCopyTftpServer':fileCopyTftpServer,'fileCopyUnitId':fileCopyUnitId,'fileCopyAction':fileCopyAction,'fileCopyStatus':fileCopyStatus,'fileCopyTftpErrMsg':fileCopyTftpErrMsg,'fileCopyTftpServerHostName':fileCopyTftpServerHostName,'fileInfoMgt':fileInfoMgt,'fileInfoTable':fileInfoTable,'fileInfoEntry':fileInfoEntry,_Ag:fileInfoUnitID,_Ah:fileInfoFileName,'fileInfoFileType':fileInfoFileType,'fileInfoIsStartUp':fileInfoIsStartUp,'fileInfoFileSize':fileInfoFileSize,'fileInfoCreationTime':fileInfoCreationTime,'fileInfoDelete':fileInfoDelete,'v2h124-24Notifications':v2h124_24Notifications,'v2h124-24Traps':v2h124_24Traps,'v2h124-24TrapsPrefix':v2h124_24TrapsPrefix,'swPowerStatusChangeTrap':swPowerStatusChangeTrap,'v2h124-24Conformance':v2h124_24Conformance})