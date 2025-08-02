_AT='wanRouterBladeGroup'
_AS='hostModuleGroup'
_AR='ifTableXtndCarrierDelay'
_AQ='ifTableXtndDtrRestartDelay'
_AP='frStaticCircuitMapClass'
_AO='ifTableXtndFrTrafficShaping'
_AN='frMapClassBcOut'
_AM='frMapClassBeOut'
_AL='frMapClassCirOut'
_AK='frMapClassFrf12Frag'
_AJ='frMapClassRowStatus'
_AI='ifTableXtndDtrPulseTime'
_AH='ifTableXtndLoadInterval'
_AG='ifTableXtndInputRate'
_AF='ifTableXtndOutputRate'
_AE='ifTableXtndInputLoad'
_AD='ifTableXtndOutputLoad'
_AC='ifTableXtndReliability'
_AB='frStaticCircuitStatus'
_AA='ifTableXtndOperStatus'
_A9='ds0BundleMemmbersList'
_A8='ds1DeviceMode'
_A7='ifTableXtndBackupCapabilities'
_A6='ifTableXtndBackupIf'
_A5='ifTableXtndBackupEnableDelay'
_A4='ifTableXtndBackupDisableDelay'
_A3='ifTableXtndPrimaryIf'
_A2='frSubIfStatus'
_A1='frDlcmiXtndLMIAutoSense'
_A0='ifTableXtndEncapsulation'
_z='ifTableXtndBandwidth'
_y='ifTableXtndIdleChars'
_x='ifTableXtndIgnoreDCD'
_w='ifTableXtndDTELoopback'
_v='ifTableXtndInvertTxClock'
_u='ifTableXtndMtu'
_t='ifTableXtndKeepAlive'
_s='ifTableXtndDescription'
_r='ifTableXtndGain'
_q='ifTableXtndCableLength'
_p='ifTableXtndVoIPQueue'
_o='ifTableXtndPeerAddress'
_n='ds0BundleSpeedFactor'
_m='intWanPortVlanList'
_l='intWanPortVLANBindingMode'
_k='intWanPortVLANMode'
_j='intWanPortAutoNegotiation'
_i='intWanPortMode'
_h='intWanPortSpeed'
_g='frMapClassName'
_f='xtndKeepAliveifIndex'
_e='frameRelay'
_d='PhysAddress'
_c='ifIndex'
_b='IF-MIB'
_a='dsx0BundleIndex'
_Z='DS0BUNDLE-MIB'
_Y='OctetString'
_X='frSubIfType'
_W='frSubIfSubIndex'
_V='frSubIfDlcmiIndex'
_U='frStaticCircuitDLCIrole'
_T='frStaticCircuitDLCI'
_S='frStaticCircuitSubIfIndex'
_R='frDlcmiXtndIndex'
_Q='ifTableXtndIndex'
_P='enable'
_O='intWanPortID'
_N='intWanGroupID'
_M='notRelevant'
_L='IpAddress'
_K='Bits'
_J='disable'
_I='DisplayString'
_H='Unsigned32'
_G='OnOff'
_F='notSupported'
_E='read-only'
_D='Integer32'
_C='read-write'
_B='WAN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_Y,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lsg,=mibBuilder.importSymbols('AVAYAGEN-MIB','lsg')
dsx0BundleCircuitIdentifier,dsx0BundleIfIndex,dsx0BundleIndex,dsx0BundleRowStatus=mibBuilder.importSymbols(_Z,'dsx0BundleCircuitIdentifier','dsx0BundleIfIndex',_a,'dsx0BundleRowStatus')
DLCI,=mibBuilder.importSymbols('FRAME-RELAY-DTE-MIB','DLCI')
InterfaceIndex,ifAdminStatus,ifAlias,ifIndex,ifName,ifOperStatus=mibBuilder.importSymbols(_b,'InterfaceIndex','ifAdminStatus','ifAlias',_c,'ifName','ifOperStatus')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_K,'Counter32','Counter64','Gauge32',_D,_L,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_I,_d,'RowStatus','TextualConvention')
avayaEISWan=ModuleIdentity((1,3,6,1,4,1,6889,2,1,6))
class OnOff(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*(('on',1),('off',2),(_M,255)))
_DeviceSpecific_ObjectIdentity=ObjectIdentity
deviceSpecific=_DeviceSpecific_ObjectIdentity((1,3,6,1,4,1,6889,2,1,6,1))
_X330wanSpecific_ObjectIdentity=ObjectIdentity
x330wanSpecific=_X330wanSpecific_ObjectIdentity((1,3,6,1,4,1,6889,2,1,6,1,1))
_IntWanPortTable_Object=MibTable
intWanPortTable=_IntWanPortTable_Object((1,3,6,1,4,1,6889,2,1,6,1,1,1))
if mibBuilder.loadTexts:intWanPortTable.setStatus(_A)
_IntWanPortEntry_Object=MibTableRow
intWanPortEntry=_IntWanPortEntry_Object((1,3,6,1,4,1,6889,2,1,6,1,1,1,1))
intWanPortEntry.setIndexNames((0,_B,_N),(0,_B,_O))
if mibBuilder.loadTexts:intWanPortEntry.setStatus(_A)
class _IntWanGroupID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_IntWanGroupID_Type.__name__=_D
_IntWanGroupID_Object=MibTableColumn
intWanGroupID=_IntWanGroupID_Object((1,3,6,1,4,1,6889,2,1,6,1,1,1,1,1),_IntWanGroupID_Type())
intWanGroupID.setMaxAccess(_E)
if mibBuilder.loadTexts:intWanGroupID.setStatus(_A)
class _IntWanPortID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_IntWanPortID_Type.__name__=_D
_IntWanPortID_Object=MibTableColumn
intWanPortID=_IntWanPortID_Object((1,3,6,1,4,1,6889,2,1,6,1,1,1,1,2),_IntWanPortID_Type())
intWanPortID.setMaxAccess(_E)
if mibBuilder.loadTexts:intWanPortID.setStatus(_A)
class _IntWanPortSpeed_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*(('ethernet',1),('fastEthernet',2),(_F,255)))
_IntWanPortSpeed_Type.__name__=_D
_IntWanPortSpeed_Object=MibTableColumn
intWanPortSpeed=_IntWanPortSpeed_Object((1,3,6,1,4,1,6889,2,1,6,1,1,1,1,3),_IntWanPortSpeed_Type())
intWanPortSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:intWanPortSpeed.setStatus(_A)
class _IntWanPortMode_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,7,255)));namedValues=NamedValues(*(('halfDuplex',1),('fullDuplexSymPause',7),(_F,255)))
_IntWanPortMode_Type.__name__=_D
_IntWanPortMode_Object=MibTableColumn
intWanPortMode=_IntWanPortMode_Object((1,3,6,1,4,1,6889,2,1,6,1,1,1,1,4),_IntWanPortMode_Type())
intWanPortMode.setMaxAccess(_C)
if mibBuilder.loadTexts:intWanPortMode.setStatus(_A)
class _IntWanPortAutoNegotiation_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_P,1),(_J,2),(_F,255)))
_IntWanPortAutoNegotiation_Type.__name__=_D
_IntWanPortAutoNegotiation_Object=MibTableColumn
intWanPortAutoNegotiation=_IntWanPortAutoNegotiation_Object((1,3,6,1,4,1,6889,2,1,6,1,1,1,1,5),_IntWanPortAutoNegotiation_Type())
intWanPortAutoNegotiation.setMaxAccess(_C)
if mibBuilder.loadTexts:intWanPortAutoNegotiation.setStatus(_A)
class _IntWanPortVLANMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*(('perPortOnly',1),('dot1QTagging',2),(_F,255)))
_IntWanPortVLANMode_Type.__name__=_D
_IntWanPortVLANMode_Object=MibTableColumn
intWanPortVLANMode=_IntWanPortVLANMode_Object((1,3,6,1,4,1,6889,2,1,6,1,1,1,1,6),_IntWanPortVLANMode_Type())
intWanPortVLANMode.setMaxAccess(_C)
if mibBuilder.loadTexts:intWanPortVLANMode.setStatus(_A)
class _IntWanPortVLANBindingMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,255)));namedValues=NamedValues(*(('static',1),('bindToReceive',2),('bindToAll',3),(_F,255)))
_IntWanPortVLANBindingMode_Type.__name__=_D
_IntWanPortVLANBindingMode_Object=MibTableColumn
intWanPortVLANBindingMode=_IntWanPortVLANBindingMode_Object((1,3,6,1,4,1,6889,2,1,6,1,1,1,1,7),_IntWanPortVLANBindingMode_Type())
intWanPortVLANBindingMode.setMaxAccess(_C)
if mibBuilder.loadTexts:intWanPortVLANBindingMode.setStatus(_A)
_IntWanPortVlanList_Type=OctetString
_IntWanPortVlanList_Object=MibTableColumn
intWanPortVlanList=_IntWanPortVlanList_Object((1,3,6,1,4,1,6889,2,1,6,1,1,1,1,8),_IntWanPortVlanList_Type())
intWanPortVlanList.setMaxAccess(_C)
if mibBuilder.loadTexts:intWanPortVlanList.setStatus(_A)
_Ds0BundleMemmbersTable_Object=MibTable
ds0BundleMemmbersTable=_Ds0BundleMemmbersTable_Object((1,3,6,1,4,1,6889,2,1,6,1,1,2))
if mibBuilder.loadTexts:ds0BundleMemmbersTable.setStatus(_A)
_Ds0BundleMemmbersEntry_Object=MibTableRow
ds0BundleMemmbersEntry=_Ds0BundleMemmbersEntry_Object((1,3,6,1,4,1,6889,2,1,6,1,1,2,1))
ds0BundleMemmbersEntry.setIndexNames((0,_Z,_a))
if mibBuilder.loadTexts:ds0BundleMemmbersEntry.setStatus(_A)
class _Ds0BundleMemmbersList_Type(OctetString):defaultHexValue='00'
_Ds0BundleMemmbersList_Type.__name__=_Y
_Ds0BundleMemmbersList_Object=MibTableColumn
ds0BundleMemmbersList=_Ds0BundleMemmbersList_Object((1,3,6,1,4,1,6889,2,1,6,1,1,2,1,1),_Ds0BundleMemmbersList_Type())
ds0BundleMemmbersList.setMaxAccess(_C)
if mibBuilder.loadTexts:ds0BundleMemmbersList.setStatus(_A)
class _Ds0BundleSpeedFactor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('a64kbps',1),('a56kbps',2)))
_Ds0BundleSpeedFactor_Type.__name__=_D
_Ds0BundleSpeedFactor_Object=MibTableColumn
ds0BundleSpeedFactor=_Ds0BundleSpeedFactor_Object((1,3,6,1,4,1,6889,2,1,6,1,1,2,1,2),_Ds0BundleSpeedFactor_Type())
ds0BundleSpeedFactor.setMaxAccess(_C)
if mibBuilder.loadTexts:ds0BundleSpeedFactor.setStatus(_A)
_Ifs_ObjectIdentity=ObjectIdentity
ifs=_Ifs_ObjectIdentity((1,3,6,1,4,1,6889,2,1,6,2))
_Ds1objs_ObjectIdentity=ObjectIdentity
ds1objs=_Ds1objs_ObjectIdentity((1,3,6,1,4,1,6889,2,1,6,2,1))
class _Ds1DeviceMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('e1',1),('t1',2),('j1',3)))
_Ds1DeviceMode_Type.__name__=_D
_Ds1DeviceMode_Object=MibScalar
ds1DeviceMode=_Ds1DeviceMode_Object((1,3,6,1,4,1,6889,2,1,6,2,1,1),_Ds1DeviceMode_Type())
ds1DeviceMode.setMaxAccess(_C)
if mibBuilder.loadTexts:ds1DeviceMode.setStatus(_A)
class _Ds1CurrentDeviceMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('e1',1),('t1',2),('j1',3)))
_Ds1CurrentDeviceMode_Type.__name__=_D
_Ds1CurrentDeviceMode_Object=MibScalar
ds1CurrentDeviceMode=_Ds1CurrentDeviceMode_Object((1,3,6,1,4,1,6889,2,1,6,2,1,2),_Ds1CurrentDeviceMode_Type())
ds1CurrentDeviceMode.setMaxAccess(_E)
if mibBuilder.loadTexts:ds1CurrentDeviceMode.setStatus(_A)
_IfTablePrivateExtensions_ObjectIdentity=ObjectIdentity
ifTablePrivateExtensions=_IfTablePrivateExtensions_ObjectIdentity((1,3,6,1,4,1,6889,2,1,6,2,2))
_IfTableXtndTable_Object=MibTable
ifTableXtndTable=_IfTableXtndTable_Object((1,3,6,1,4,1,6889,2,1,6,2,2,1))
if mibBuilder.loadTexts:ifTableXtndTable.setStatus(_A)
_IfTableXtndEntry_Object=MibTableRow
ifTableXtndEntry=_IfTableXtndEntry_Object((1,3,6,1,4,1,6889,2,1,6,2,2,1,1))
ifTableXtndEntry.setIndexNames((0,_B,_Q))
if mibBuilder.loadTexts:ifTableXtndEntry.setStatus(_A)
_IfTableXtndIndex_Type=InterfaceIndex
_IfTableXtndIndex_Object=MibTableColumn
ifTableXtndIndex=_IfTableXtndIndex_Object((1,3,6,1,4,1,6889,2,1,6,2,2,1,1,1),_IfTableXtndIndex_Type())
ifTableXtndIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ifTableXtndIndex.setStatus(_A)
_IfTableXtndPeerAddress_Type=IpAddress
_IfTableXtndPeerAddress_Object=MibTableColumn
ifTableXtndPeerAddress=_IfTableXtndPeerAddress_Object((1,3,6,1,4,1,6889,2,1,6,2,2,1,1,2),_IfTableXtndPeerAddress_Type())
ifTableXtndPeerAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:ifTableXtndPeerAddress.setStatus(_A)
class _IfTableXtndVoIPQueue_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,255)));namedValues=NamedValues(*(('on',1),('off',2),('fairQ',3),(_M,255)))
_IfTableXtndVoIPQueue_Type.__name__=_D
_IfTableXtndVoIPQueue_Object=MibTableColumn
ifTableXtndVoIPQueue=_IfTableXtndVoIPQueue_Object((1,3,6,1,4,1,6889,2,1,6,2,2,1,1,3),_IfTableXtndVoIPQueue_Type())
ifTableXtndVoIPQueue.setMaxAccess(_C)
if mibBuilder.loadTexts:ifTableXtndVoIPQueue.setStatus(_A)
class _IfTableXtndCableLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,255)));namedValues=NamedValues(*(('long15db',1),('long22dot5db',2),('long7dot5db',3),('long0db',4),('short133ft',5),('short266ft',6),('short399ft',7),('short533ft',8),('short655ft',9),(_F,255)))
_IfTableXtndCableLength_Type.__name__=_D
_IfTableXtndCableLength_Object=MibTableColumn
ifTableXtndCableLength=_IfTableXtndCableLength_Object((1,3,6,1,4,1,6889,2,1,6,2,2,1,1,4),_IfTableXtndCableLength_Type())
ifTableXtndCableLength.setMaxAccess(_C)
if mibBuilder.loadTexts:ifTableXtndCableLength.setStatus(_A)
class _IfTableXtndGain_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*(('a26',1),('a36',2),(_F,255)))
_IfTableXtndGain_Type.__name__=_D
_IfTableXtndGain_Object=MibTableColumn
ifTableXtndGain=_IfTableXtndGain_Object((1,3,6,1,4,1,6889,2,1,6,2,2,1,1,5),_IfTableXtndGain_Type())
ifTableXtndGain.setMaxAccess(_C)
if mibBuilder.loadTexts:ifTableXtndGain.setStatus(_A)
class _IfTableXtndDescription_Type(DisplayString):defaultHexValue=''
_IfTableXtndDescription_Type.__name__=_I
_IfTableXtndDescription_Object=MibTableColumn
ifTableXtndDescription=_IfTableXtndDescription_Object((1,3,6,1,4,1,6889,2,1,6,2,2,1,1,6),_IfTableXtndDescription_Type())
ifTableXtndDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:ifTableXtndDescription.setStatus(_A)
class _IfTableXtndKeepAlive_Type(Integer32):defaultValue=0
_IfTableXtndKeepAlive_Type.__name__=_D
_IfTableXtndKeepAlive_Object=MibTableColumn
ifTableXtndKeepAlive=_IfTableXtndKeepAlive_Object((1,3,6,1,4,1,6889,2,1,6,2,2,1,1,7),_IfTableXtndKeepAlive_Type())
ifTableXtndKeepAlive.setMaxAccess(_C)
if mibBuilder.loadTexts:ifTableXtndKeepAlive.setStatus(_A)
class _IfTableXtndMtu_Type(Integer32):defaultValue=0
_IfTableXtndMtu_Type.__name__=_D
_IfTableXtndMtu_Object=MibTableColumn
ifTableXtndMtu=_IfTableXtndMtu_Object((1,3,6,1,4,1,6889,2,1,6,2,2,1,1,8),_IfTableXtndMtu_Type())
ifTableXtndMtu.setMaxAccess(_C)
if mibBuilder.loadTexts:ifTableXtndMtu.setStatus(_A)
class _IfTableXtndInvertTxClock_Type(OnOff):defaultValue=255
_IfTableXtndInvertTxClock_Type.__name__=_G
_IfTableXtndInvertTxClock_Object=MibTableColumn
ifTableXtndInvertTxClock=_IfTableXtndInvertTxClock_Object((1,3,6,1,4,1,6889,2,1,6,2,2,1,1,9),_IfTableXtndInvertTxClock_Type())
ifTableXtndInvertTxClock.setMaxAccess(_C)
if mibBuilder.loadTexts:ifTableXtndInvertTxClock.setStatus(_A)
class _IfTableXtndDTELoopback_Type(OnOff):defaultValue=255
_IfTableXtndDTELoopback_Type.__name__=_G
_IfTableXtndDTELoopback_Object=MibTableColumn
ifTableXtndDTELoopback=_IfTableXtndDTELoopback_Object((1,3,6,1,4,1,6889,2,1,6,2,2,1,1,10),_IfTableXtndDTELoopback_Type())
ifTableXtndDTELoopback.setMaxAccess(_C)
if mibBuilder.loadTexts:ifTableXtndDTELoopback.setStatus(_A)
class _IfTableXtndIgnoreDCD_Type(OnOff):defaultValue=255
_IfTableXtndIgnoreDCD_Type.__name__=_G
_IfTableXtndIgnoreDCD_Object=MibTableColumn
ifTableXtndIgnoreDCD=_IfTableXtndIgnoreDCD_Object((1,3,6,1,4,1,6889,2,1,6,2,2,1,1,11),_IfTableXtndIgnoreDCD_Type())
ifTableXtndIgnoreDCD.setMaxAccess(_C)
if mibBuilder.loadTexts:ifTableXtndIgnoreDCD.setStatus(_A)
class _IfTableXtndIdleChars_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,255)));namedValues=NamedValues(*(('flag',1),('mark',2),('space',3),(_M,255)))
_IfTableXtndIdleChars_Type.__name__=_D
_IfTableXtndIdleChars_Object=MibTableColumn
ifTableXtndIdleChars=_IfTableXtndIdleChars_Object((1,3,6,1,4,1,6889,2,1,6,2,2,1,1,12),_IfTableXtndIdleChars_Type())
ifTableXtndIdleChars.setMaxAccess(_C)
if mibBuilder.loadTexts:ifTableXtndIdleChars.setStatus(_A)
class _IfTableXtndBandwidth_Type(Integer32):defaultValue=0
_IfTableXtndBandwidth_Type.__name__=_D
_IfTableXtndBandwidth_Object=MibTableColumn
ifTableXtndBandwidth=_IfTableXtndBandwidth_Object((1,3,6,1,4,1,6889,2,1,6,2,2,1,1,13),_IfTableXtndBandwidth_Type())
ifTableXtndBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:ifTableXtndBandwidth.setStatus(_A)
class _IfTableXtndEncapsulation_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,255)));namedValues=NamedValues(*(('ppp',1),(_e,2),('pppoe',3),('arpa',4),('frameRelayNonIetf',5),(_F,255)))
_IfTableXtndEncapsulation_Type.__name__=_D
_IfTableXtndEncapsulation_Object=MibTableColumn
ifTableXtndEncapsulation=_IfTableXtndEncapsulation_Object((1,3,6,1,4,1,6889,2,1,6,2,2,1,1,14),_IfTableXtndEncapsulation_Type())
ifTableXtndEncapsulation.setMaxAccess(_C)
if mibBuilder.loadTexts:ifTableXtndEncapsulation.setStatus(_A)
class _IfTableXtndOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,255)));namedValues=NamedValues(*(('up',1),('faultDown',2),('testing',3),('partiallyDownFault',4),('adminDown',5),('dormantDown',6),('xtndKeepAliveDown',7),('modemUndetected',8),('modemReady',9),('modemDialing',10),('modemConnectedDialin',11),('modemConnectedDialout',12),(_F,255)))
_IfTableXtndOperStatus_Type.__name__=_D
_IfTableXtndOperStatus_Object=MibTableColumn
ifTableXtndOperStatus=_IfTableXtndOperStatus_Object((1,3,6,1,4,1,6889,2,1,6,2,2,1,1,15),_IfTableXtndOperStatus_Type())
ifTableXtndOperStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:ifTableXtndOperStatus.setStatus(_A)
class _IfTableXtndBackupCapabilities_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,255)));namedValues=NamedValues(*(('primaryAndBackUp',1),('primaryOnly',2),('backupOnly',3),(_F,255)))
_IfTableXtndBackupCapabilities_Type.__name__=_D
_IfTableXtndBackupCapabilities_Object=MibTableColumn
ifTableXtndBackupCapabilities=_IfTableXtndBackupCapabilities_Object((1,3,6,1,4,1,6889,2,1,6,2,2,1,1,16),_IfTableXtndBackupCapabilities_Type())
ifTableXtndBackupCapabilities.setMaxAccess(_E)
if mibBuilder.loadTexts:ifTableXtndBackupCapabilities.setStatus(_A)
_IfTableXtndBackupIf_Type=InterfaceIndex
_IfTableXtndBackupIf_Object=MibTableColumn
ifTableXtndBackupIf=_IfTableXtndBackupIf_Object((1,3,6,1,4,1,6889,2,1,6,2,2,1,1,17),_IfTableXtndBackupIf_Type())
ifTableXtndBackupIf.setMaxAccess(_C)
if mibBuilder.loadTexts:ifTableXtndBackupIf.setStatus(_A)
class _IfTableXtndBackupEnableDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_IfTableXtndBackupEnableDelay_Type.__name__=_D
_IfTableXtndBackupEnableDelay_Object=MibTableColumn
ifTableXtndBackupEnableDelay=_IfTableXtndBackupEnableDelay_Object((1,3,6,1,4,1,6889,2,1,6,2,2,1,1,18),_IfTableXtndBackupEnableDelay_Type())
ifTableXtndBackupEnableDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:ifTableXtndBackupEnableDelay.setStatus(_A)
class _IfTableXtndBackupDisableDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,3600))
_IfTableXtndBackupDisableDelay_Type.__name__=_D
_IfTableXtndBackupDisableDelay_Object=MibTableColumn
ifTableXtndBackupDisableDelay=_IfTableXtndBackupDisableDelay_Object((1,3,6,1,4,1,6889,2,1,6,2,2,1,1,19),_IfTableXtndBackupDisableDelay_Type())
ifTableXtndBackupDisableDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:ifTableXtndBackupDisableDelay.setStatus(_A)
_IfTableXtndPrimaryIf_Type=InterfaceIndex
_IfTableXtndPrimaryIf_Object=MibTableColumn
ifTableXtndPrimaryIf=_IfTableXtndPrimaryIf_Object((1,3,6,1,4,1,6889,2,1,6,2,2,1,1,20),_IfTableXtndPrimaryIf_Type())
ifTableXtndPrimaryIf.setMaxAccess(_E)
if mibBuilder.loadTexts:ifTableXtndPrimaryIf.setStatus(_A)
class _IfTableXtndCarrierDelay_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60))
_IfTableXtndCarrierDelay_Type.__name__=_D
_IfTableXtndCarrierDelay_Object=MibTableColumn
ifTableXtndCarrierDelay=_IfTableXtndCarrierDelay_Object((1,3,6,1,4,1,6889,2,1,6,2,2,1,1,21),_IfTableXtndCarrierDelay_Type())
ifTableXtndCarrierDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:ifTableXtndCarrierDelay.setStatus(_A)
class _IfTableXtndDtrRestartDelay_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,900))
_IfTableXtndDtrRestartDelay_Type.__name__=_D
_IfTableXtndDtrRestartDelay_Object=MibTableColumn
ifTableXtndDtrRestartDelay=_IfTableXtndDtrRestartDelay_Object((1,3,6,1,4,1,6889,2,1,6,2,2,1,1,22),_IfTableXtndDtrRestartDelay_Type())
ifTableXtndDtrRestartDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:ifTableXtndDtrRestartDelay.setStatus(_A)
class _IfTableXtndDtrPulseTime_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60))
_IfTableXtndDtrPulseTime_Type.__name__=_D
_IfTableXtndDtrPulseTime_Object=MibTableColumn
ifTableXtndDtrPulseTime=_IfTableXtndDtrPulseTime_Object((1,3,6,1,4,1,6889,2,1,6,2,2,1,1,23),_IfTableXtndDtrPulseTime_Type())
ifTableXtndDtrPulseTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifTableXtndDtrPulseTime.setStatus(_A)
class _IfTableXtndLoadInterval_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,600))
_IfTableXtndLoadInterval_Type.__name__=_D
_IfTableXtndLoadInterval_Object=MibTableColumn
ifTableXtndLoadInterval=_IfTableXtndLoadInterval_Object((1,3,6,1,4,1,6889,2,1,6,2,2,1,1,24),_IfTableXtndLoadInterval_Type())
ifTableXtndLoadInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:ifTableXtndLoadInterval.setStatus(_A)
_IfTableXtndInputRate_Type=Gauge32
_IfTableXtndInputRate_Object=MibTableColumn
ifTableXtndInputRate=_IfTableXtndInputRate_Object((1,3,6,1,4,1,6889,2,1,6,2,2,1,1,25),_IfTableXtndInputRate_Type())
ifTableXtndInputRate.setMaxAccess(_E)
if mibBuilder.loadTexts:ifTableXtndInputRate.setStatus(_A)
_IfTableXtndOutputRate_Type=Gauge32
_IfTableXtndOutputRate_Object=MibTableColumn
ifTableXtndOutputRate=_IfTableXtndOutputRate_Object((1,3,6,1,4,1,6889,2,1,6,2,2,1,1,26),_IfTableXtndOutputRate_Type())
ifTableXtndOutputRate.setMaxAccess(_E)
if mibBuilder.loadTexts:ifTableXtndOutputRate.setStatus(_A)
_IfTableXtndInputLoad_Type=Gauge32
_IfTableXtndInputLoad_Object=MibTableColumn
ifTableXtndInputLoad=_IfTableXtndInputLoad_Object((1,3,6,1,4,1,6889,2,1,6,2,2,1,1,27),_IfTableXtndInputLoad_Type())
ifTableXtndInputLoad.setMaxAccess(_E)
if mibBuilder.loadTexts:ifTableXtndInputLoad.setStatus(_A)
_IfTableXtndOutputLoad_Type=Gauge32
_IfTableXtndOutputLoad_Object=MibTableColumn
ifTableXtndOutputLoad=_IfTableXtndOutputLoad_Object((1,3,6,1,4,1,6889,2,1,6,2,2,1,1,28),_IfTableXtndOutputLoad_Type())
ifTableXtndOutputLoad.setMaxAccess(_E)
if mibBuilder.loadTexts:ifTableXtndOutputLoad.setStatus(_A)
_IfTableXtndReliability_Type=Gauge32
_IfTableXtndReliability_Object=MibTableColumn
ifTableXtndReliability=_IfTableXtndReliability_Object((1,3,6,1,4,1,6889,2,1,6,2,2,1,1,29),_IfTableXtndReliability_Type())
ifTableXtndReliability.setMaxAccess(_E)
if mibBuilder.loadTexts:ifTableXtndReliability.setStatus(_A)
class _IfTableXtndTrafficShaperRate_Type(Integer32):defaultValue=0
_IfTableXtndTrafficShaperRate_Type.__name__=_D
_IfTableXtndTrafficShaperRate_Object=MibTableColumn
ifTableXtndTrafficShaperRate=_IfTableXtndTrafficShaperRate_Object((1,3,6,1,4,1,6889,2,1,6,2,2,1,1,30),_IfTableXtndTrafficShaperRate_Type())
ifTableXtndTrafficShaperRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ifTableXtndTrafficShaperRate.setStatus(_A)
class _IfTableXtndCacBBL_Type(Integer32):defaultValue=-1
_IfTableXtndCacBBL_Type.__name__=_D
_IfTableXtndCacBBL_Object=MibTableColumn
ifTableXtndCacBBL=_IfTableXtndCacBBL_Object((1,3,6,1,4,1,6889,2,1,6,2,2,1,1,31),_IfTableXtndCacBBL_Type())
ifTableXtndCacBBL.setMaxAccess(_C)
if mibBuilder.loadTexts:ifTableXtndCacBBL.setStatus(_A)
class _IfTableXtndCacPriority_Type(Integer32):defaultValue=5
_IfTableXtndCacPriority_Type.__name__=_D
_IfTableXtndCacPriority_Object=MibTableColumn
ifTableXtndCacPriority=_IfTableXtndCacPriority_Object((1,3,6,1,4,1,6889,2,1,6,2,2,1,1,32),_IfTableXtndCacPriority_Type())
ifTableXtndCacPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:ifTableXtndCacPriority.setStatus(_A)
class _IfTableXtndCacifStatus_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,255)));namedValues=NamedValues(*(('notConfigured',1),('active',2),('notActive',3),('activeECMP',4),(_F,255)))
_IfTableXtndCacifStatus_Type.__name__=_D
_IfTableXtndCacifStatus_Object=MibTableColumn
ifTableXtndCacifStatus=_IfTableXtndCacifStatus_Object((1,3,6,1,4,1,6889,2,1,6,2,2,1,1,33),_IfTableXtndCacifStatus_Type())
ifTableXtndCacifStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:ifTableXtndCacifStatus.setStatus(_A)
_IfTableXtndCommonApplifStatus_Type=OctetString
_IfTableXtndCommonApplifStatus_Object=MibTableColumn
ifTableXtndCommonApplifStatus=_IfTableXtndCommonApplifStatus_Object((1,3,6,1,4,1,6889,2,1,6,2,2,1,1,34),_IfTableXtndCommonApplifStatus_Type())
ifTableXtndCommonApplifStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:ifTableXtndCommonApplifStatus.setStatus(_A)
class _IfTableXtndIpSecDfBit_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*(('clear',1),('copy',2),(_F,255)))
_IfTableXtndIpSecDfBit_Type.__name__=_D
_IfTableXtndIpSecDfBit_Object=MibTableColumn
ifTableXtndIpSecDfBit=_IfTableXtndIpSecDfBit_Object((1,3,6,1,4,1,6889,2,1,6,2,2,1,1,35),_IfTableXtndIpSecDfBit_Type())
ifTableXtndIpSecDfBit.setMaxAccess(_C)
if mibBuilder.loadTexts:ifTableXtndIpSecDfBit.setStatus(_A)
_IfTableXtndMinPmtu_Type=Integer32
_IfTableXtndMinPmtu_Object=MibTableColumn
ifTableXtndMinPmtu=_IfTableXtndMinPmtu_Object((1,3,6,1,4,1,6889,2,1,6,2,2,1,1,36),_IfTableXtndMinPmtu_Type())
ifTableXtndMinPmtu.setMaxAccess(_C)
if mibBuilder.loadTexts:ifTableXtndMinPmtu.setStatus(_A)
_IfTableXtndConfString_Type=DisplayString
_IfTableXtndConfString_Object=MibTableColumn
ifTableXtndConfString=_IfTableXtndConfString_Object((1,3,6,1,4,1,6889,2,1,6,2,2,1,1,37),_IfTableXtndConfString_Type())
ifTableXtndConfString.setMaxAccess(_C)
if mibBuilder.loadTexts:ifTableXtndConfString.setStatus(_A)
class _IfTableXtndPppIpcpDnsOptionRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_P,1),(_J,2),(_F,255)))
_IfTableXtndPppIpcpDnsOptionRequest_Type.__name__=_D
_IfTableXtndPppIpcpDnsOptionRequest_Object=MibTableColumn
ifTableXtndPppIpcpDnsOptionRequest=_IfTableXtndPppIpcpDnsOptionRequest_Object((1,3,6,1,4,1,6889,2,1,6,2,2,1,1,38),_IfTableXtndPppIpcpDnsOptionRequest_Type())
ifTableXtndPppIpcpDnsOptionRequest.setMaxAccess(_C)
if mibBuilder.loadTexts:ifTableXtndPppIpcpDnsOptionRequest.setStatus(_A)
class _IfTableXtndKeepaliveTrackId_Type(Unsigned32):defaultValue=4294967295
_IfTableXtndKeepaliveTrackId_Type.__name__=_H
_IfTableXtndKeepaliveTrackId_Object=MibTableColumn
ifTableXtndKeepaliveTrackId=_IfTableXtndKeepaliveTrackId_Object((1,3,6,1,4,1,6889,2,1,6,2,2,1,1,39),_IfTableXtndKeepaliveTrackId_Type())
ifTableXtndKeepaliveTrackId.setMaxAccess(_C)
if mibBuilder.loadTexts:ifTableXtndKeepaliveTrackId.setStatus(_A)
class _IfTableXtndFrTrafficShaping_Type(OnOff):defaultValue=2
_IfTableXtndFrTrafficShaping_Type.__name__=_G
_IfTableXtndFrTrafficShaping_Object=MibTableColumn
ifTableXtndFrTrafficShaping=_IfTableXtndFrTrafficShaping_Object((1,3,6,1,4,1,6889,2,1,6,2,2,1,1,40),_IfTableXtndFrTrafficShaping_Type())
ifTableXtndFrTrafficShaping.setMaxAccess(_C)
if mibBuilder.loadTexts:ifTableXtndFrTrafficShaping.setStatus(_A)
class _IfTableXtndType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,255)));namedValues=NamedValues(*(('nullModem',1),('usrSporsterModem',2),('multitechZbaModem',3),('multitechIsdnModem',4),(_F,255)))
_IfTableXtndType_Type.__name__=_D
_IfTableXtndType_Object=MibTableColumn
ifTableXtndType=_IfTableXtndType_Object((1,3,6,1,4,1,6889,2,1,6,2,2,1,1,41),_IfTableXtndType_Type())
ifTableXtndType.setMaxAccess(_C)
if mibBuilder.loadTexts:ifTableXtndType.setStatus(_A)
_XtndKeepAliveTable_Object=MibTable
xtndKeepAliveTable=_XtndKeepAliveTable_Object((1,3,6,1,4,1,6889,2,1,6,2,2,2))
if mibBuilder.loadTexts:xtndKeepAliveTable.setStatus(_A)
_XtndKeepAliveEntry_Object=MibTableRow
xtndKeepAliveEntry=_XtndKeepAliveEntry_Object((1,3,6,1,4,1,6889,2,1,6,2,2,2,1))
xtndKeepAliveEntry.setIndexNames((0,_B,_f))
if mibBuilder.loadTexts:xtndKeepAliveEntry.setStatus(_A)
_XtndKeepAliveifIndex_Type=InterfaceIndex
_XtndKeepAliveifIndex_Object=MibTableColumn
xtndKeepAliveifIndex=_XtndKeepAliveifIndex_Object((1,3,6,1,4,1,6889,2,1,6,2,2,2,1,1),_XtndKeepAliveifIndex_Type())
xtndKeepAliveifIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:xtndKeepAliveifIndex.setStatus(_A)
class _XtndKeepAliveMethod_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('icmpPing',1),('tcpConnect',2),('httpGet',3)))
_XtndKeepAliveMethod_Type.__name__=_D
_XtndKeepAliveMethod_Object=MibTableColumn
xtndKeepAliveMethod=_XtndKeepAliveMethod_Object((1,3,6,1,4,1,6889,2,1,6,2,2,2,1,2),_XtndKeepAliveMethod_Type())
xtndKeepAliveMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:xtndKeepAliveMethod.setStatus(_A)
_XtndKeepAliveTimeout_Type=Integer32
_XtndKeepAliveTimeout_Object=MibTableColumn
xtndKeepAliveTimeout=_XtndKeepAliveTimeout_Object((1,3,6,1,4,1,6889,2,1,6,2,2,2,1,3),_XtndKeepAliveTimeout_Type())
xtndKeepAliveTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:xtndKeepAliveTimeout.setStatus(_A)
_XtndKeepAliveUpRetries_Type=Integer32
_XtndKeepAliveUpRetries_Object=MibTableColumn
xtndKeepAliveUpRetries=_XtndKeepAliveUpRetries_Object((1,3,6,1,4,1,6889,2,1,6,2,2,2,1,4),_XtndKeepAliveUpRetries_Type())
xtndKeepAliveUpRetries.setMaxAccess(_C)
if mibBuilder.loadTexts:xtndKeepAliveUpRetries.setStatus(_A)
_XtndKeepAliveDownRetries_Type=Integer32
_XtndKeepAliveDownRetries_Object=MibTableColumn
xtndKeepAliveDownRetries=_XtndKeepAliveDownRetries_Object((1,3,6,1,4,1,6889,2,1,6,2,2,2,1,5),_XtndKeepAliveDownRetries_Type())
xtndKeepAliveDownRetries.setMaxAccess(_C)
if mibBuilder.loadTexts:xtndKeepAliveDownRetries.setStatus(_A)
_XtndKeepAliveInterval_Type=Integer32
_XtndKeepAliveInterval_Object=MibTableColumn
xtndKeepAliveInterval=_XtndKeepAliveInterval_Object((1,3,6,1,4,1,6889,2,1,6,2,2,2,1,6),_XtndKeepAliveInterval_Type())
xtndKeepAliveInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:xtndKeepAliveInterval.setStatus(_A)
class _XtndKeepAliveSrcIPAddr_Type(IpAddress):defaultHexValue='7f000001'
_XtndKeepAliveSrcIPAddr_Type.__name__=_L
_XtndKeepAliveSrcIPAddr_Object=MibTableColumn
xtndKeepAliveSrcIPAddr=_XtndKeepAliveSrcIPAddr_Object((1,3,6,1,4,1,6889,2,1,6,2,2,2,1,7),_XtndKeepAliveSrcIPAddr_Type())
xtndKeepAliveSrcIPAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:xtndKeepAliveSrcIPAddr.setStatus(_A)
class _XtndKeepAliveIPAddr_Type(IpAddress):defaultHexValue='00000000'
_XtndKeepAliveIPAddr_Type.__name__=_L
_XtndKeepAliveIPAddr_Object=MibTableColumn
xtndKeepAliveIPAddr=_XtndKeepAliveIPAddr_Object((1,3,6,1,4,1,6889,2,1,6,2,2,2,1,8),_XtndKeepAliveIPAddr_Type())
xtndKeepAliveIPAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:xtndKeepAliveIPAddr.setStatus(_A)
class _XtndKeepAliveNextHopMAC_Type(PhysAddress):defaultHexValue='000000000000'
_XtndKeepAliveNextHopMAC_Type.__name__=_d
_XtndKeepAliveNextHopMAC_Object=MibTableColumn
xtndKeepAliveNextHopMAC=_XtndKeepAliveNextHopMAC_Object((1,3,6,1,4,1,6889,2,1,6,2,2,2,1,9),_XtndKeepAliveNextHopMAC_Type())
xtndKeepAliveNextHopMAC.setMaxAccess(_C)
if mibBuilder.loadTexts:xtndKeepAliveNextHopMAC.setStatus(_A)
class _XtndKeepAliveStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),(_J,3)))
_XtndKeepAliveStatus_Type.__name__=_D
_XtndKeepAliveStatus_Object=MibTableColumn
xtndKeepAliveStatus=_XtndKeepAliveStatus_Object((1,3,6,1,4,1,6889,2,1,6,2,2,2,1,10),_XtndKeepAliveStatus_Type())
xtndKeepAliveStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:xtndKeepAliveStatus.setStatus(_A)
class _XtndKeepAliveMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_J,2)))
_XtndKeepAliveMode_Type.__name__=_D
_XtndKeepAliveMode_Object=MibTableColumn
xtndKeepAliveMode=_XtndKeepAliveMode_Object((1,3,6,1,4,1,6889,2,1,6,2,2,2,1,11),_XtndKeepAliveMode_Type())
xtndKeepAliveMode.setMaxAccess(_C)
if mibBuilder.loadTexts:xtndKeepAliveMode.setStatus(_A)
_FrameRelay_ObjectIdentity=ObjectIdentity
frameRelay=_FrameRelay_ObjectIdentity((1,3,6,1,4,1,6889,2,1,6,2,4))
_FrDlcmiXtndTable_Object=MibTable
frDlcmiXtndTable=_FrDlcmiXtndTable_Object((1,3,6,1,4,1,6889,2,1,6,2,4,1))
if mibBuilder.loadTexts:frDlcmiXtndTable.setStatus(_A)
_FrDlcmiXtndEntry_Object=MibTableRow
frDlcmiXtndEntry=_FrDlcmiXtndEntry_Object((1,3,6,1,4,1,6889,2,1,6,2,4,1,1))
frDlcmiXtndEntry.setIndexNames((0,_B,_R))
if mibBuilder.loadTexts:frDlcmiXtndEntry.setStatus(_A)
_FrDlcmiXtndIndex_Type=InterfaceIndex
_FrDlcmiXtndIndex_Object=MibTableColumn
frDlcmiXtndIndex=_FrDlcmiXtndIndex_Object((1,3,6,1,4,1,6889,2,1,6,2,4,1,1,1),_FrDlcmiXtndIndex_Type())
frDlcmiXtndIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:frDlcmiXtndIndex.setStatus(_A)
class _FrDlcmiXtndLMIAutoSense_Type(OnOff):defaultValue=1
_FrDlcmiXtndLMIAutoSense_Type.__name__=_G
_FrDlcmiXtndLMIAutoSense_Object=MibTableColumn
frDlcmiXtndLMIAutoSense=_FrDlcmiXtndLMIAutoSense_Object((1,3,6,1,4,1,6889,2,1,6,2,4,1,1,2),_FrDlcmiXtndLMIAutoSense_Type())
frDlcmiXtndLMIAutoSense.setMaxAccess(_C)
if mibBuilder.loadTexts:frDlcmiXtndLMIAutoSense.setStatus(_A)
_FrStaticCircuitTable_Object=MibTable
frStaticCircuitTable=_FrStaticCircuitTable_Object((1,3,6,1,4,1,6889,2,1,6,2,4,2))
if mibBuilder.loadTexts:frStaticCircuitTable.setStatus(_A)
_FrStaticCircuitEntry_Object=MibTableRow
frStaticCircuitEntry=_FrStaticCircuitEntry_Object((1,3,6,1,4,1,6889,2,1,6,2,4,2,1))
frStaticCircuitEntry.setIndexNames((0,_B,_S),(0,_B,_T),(0,_B,_U))
if mibBuilder.loadTexts:frStaticCircuitEntry.setStatus(_A)
_FrStaticCircuitSubIfIndex_Type=InterfaceIndex
_FrStaticCircuitSubIfIndex_Object=MibTableColumn
frStaticCircuitSubIfIndex=_FrStaticCircuitSubIfIndex_Object((1,3,6,1,4,1,6889,2,1,6,2,4,2,1,1),_FrStaticCircuitSubIfIndex_Type())
frStaticCircuitSubIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:frStaticCircuitSubIfIndex.setStatus(_A)
_FrStaticCircuitDLCI_Type=DLCI
_FrStaticCircuitDLCI_Object=MibTableColumn
frStaticCircuitDLCI=_FrStaticCircuitDLCI_Object((1,3,6,1,4,1,6889,2,1,6,2,4,2,1,2),_FrStaticCircuitDLCI_Type())
frStaticCircuitDLCI.setMaxAccess(_E)
if mibBuilder.loadTexts:frStaticCircuitDLCI.setStatus(_A)
class _FrStaticCircuitDLCIrole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,100)));namedValues=NamedValues(*(('priority6to7',1),('priority4to5',2),('priority2to3',3),('priority0to1',4),('primary',100)))
_FrStaticCircuitDLCIrole_Type.__name__=_D
_FrStaticCircuitDLCIrole_Object=MibTableColumn
frStaticCircuitDLCIrole=_FrStaticCircuitDLCIrole_Object((1,3,6,1,4,1,6889,2,1,6,2,4,2,1,3),_FrStaticCircuitDLCIrole_Type())
frStaticCircuitDLCIrole.setMaxAccess(_E)
if mibBuilder.loadTexts:frStaticCircuitDLCIrole.setStatus(_A)
_FrStaticCircuitStatus_Type=RowStatus
_FrStaticCircuitStatus_Object=MibTableColumn
frStaticCircuitStatus=_FrStaticCircuitStatus_Object((1,3,6,1,4,1,6889,2,1,6,2,4,2,1,4),_FrStaticCircuitStatus_Type())
frStaticCircuitStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:frStaticCircuitStatus.setStatus(_A)
class _FrStaticCircuitMapClass_Type(DisplayString):defaultValue=OctetString('default');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_FrStaticCircuitMapClass_Type.__name__=_I
_FrStaticCircuitMapClass_Object=MibTableColumn
frStaticCircuitMapClass=_FrStaticCircuitMapClass_Object((1,3,6,1,4,1,6889,2,1,6,2,4,2,1,5),_FrStaticCircuitMapClass_Type())
frStaticCircuitMapClass.setMaxAccess(_C)
if mibBuilder.loadTexts:frStaticCircuitMapClass.setStatus(_A)
_FrSubIfTable_Object=MibTable
frSubIfTable=_FrSubIfTable_Object((1,3,6,1,4,1,6889,2,1,6,2,4,3))
if mibBuilder.loadTexts:frSubIfTable.setStatus(_A)
_FrSubIfEntry_Object=MibTableRow
frSubIfEntry=_FrSubIfEntry_Object((1,3,6,1,4,1,6889,2,1,6,2,4,3,1))
frSubIfEntry.setIndexNames((0,_B,_V),(0,_B,_W),(0,_B,_X))
if mibBuilder.loadTexts:frSubIfEntry.setStatus(_A)
_FrSubIfDlcmiIndex_Type=InterfaceIndex
_FrSubIfDlcmiIndex_Object=MibTableColumn
frSubIfDlcmiIndex=_FrSubIfDlcmiIndex_Object((1,3,6,1,4,1,6889,2,1,6,2,4,3,1,1),_FrSubIfDlcmiIndex_Type())
frSubIfDlcmiIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:frSubIfDlcmiIndex.setStatus(_A)
_FrSubIfSubIndex_Type=InterfaceIndex
_FrSubIfSubIndex_Object=MibTableColumn
frSubIfSubIndex=_FrSubIfSubIndex_Object((1,3,6,1,4,1,6889,2,1,6,2,4,3,1,2),_FrSubIfSubIndex_Type())
frSubIfSubIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:frSubIfSubIndex.setStatus(_A)
class _FrSubIfType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('point2point',1),('point2multiPoint',2)))
_FrSubIfType_Type.__name__=_D
_FrSubIfType_Object=MibTableColumn
frSubIfType=_FrSubIfType_Object((1,3,6,1,4,1,6889,2,1,6,2,4,3,1,3),_FrSubIfType_Type())
frSubIfType.setMaxAccess(_E)
if mibBuilder.loadTexts:frSubIfType.setStatus(_A)
_FrSubIfStatus_Type=RowStatus
_FrSubIfStatus_Object=MibTableColumn
frSubIfStatus=_FrSubIfStatus_Object((1,3,6,1,4,1,6889,2,1,6,2,4,3,1,4),_FrSubIfStatus_Type())
frSubIfStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:frSubIfStatus.setStatus(_A)
_FrMapClassTable_Object=MibTable
frMapClassTable=_FrMapClassTable_Object((1,3,6,1,4,1,6889,2,1,6,2,4,4))
if mibBuilder.loadTexts:frMapClassTable.setStatus(_A)
_FrMapClassEntry_Object=MibTableRow
frMapClassEntry=_FrMapClassEntry_Object((1,3,6,1,4,1,6889,2,1,6,2,4,4,1))
frMapClassEntry.setIndexNames((1,_B,_g))
if mibBuilder.loadTexts:frMapClassEntry.setStatus(_A)
class _FrMapClassName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_FrMapClassName_Type.__name__=_I
_FrMapClassName_Object=MibTableColumn
frMapClassName=_FrMapClassName_Object((1,3,6,1,4,1,6889,2,1,6,2,4,4,1,1),_FrMapClassName_Type())
frMapClassName.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:frMapClassName.setStatus(_A)
class _FrMapClassBcOut_Type(Unsigned32):defaultValue=7000
_FrMapClassBcOut_Type.__name__=_H
_FrMapClassBcOut_Object=MibTableColumn
frMapClassBcOut=_FrMapClassBcOut_Object((1,3,6,1,4,1,6889,2,1,6,2,4,4,1,2),_FrMapClassBcOut_Type())
frMapClassBcOut.setMaxAccess(_C)
if mibBuilder.loadTexts:frMapClassBcOut.setStatus(_A)
if mibBuilder.loadTexts:frMapClassBcOut.setUnits(_K)
class _FrMapClassBeOut_Type(Unsigned32):defaultValue=0
_FrMapClassBeOut_Type.__name__=_H
_FrMapClassBeOut_Object=MibTableColumn
frMapClassBeOut=_FrMapClassBeOut_Object((1,3,6,1,4,1,6889,2,1,6,2,4,4,1,3),_FrMapClassBeOut_Type())
frMapClassBeOut.setMaxAccess(_C)
if mibBuilder.loadTexts:frMapClassBeOut.setStatus(_A)
if mibBuilder.loadTexts:frMapClassBeOut.setUnits(_K)
class _FrMapClassCirOut_Type(Unsigned32):defaultValue=56000
_FrMapClassCirOut_Type.__name__=_H
_FrMapClassCirOut_Object=MibTableColumn
frMapClassCirOut=_FrMapClassCirOut_Object((1,3,6,1,4,1,6889,2,1,6,2,4,4,1,4),_FrMapClassCirOut_Type())
frMapClassCirOut.setMaxAccess(_C)
if mibBuilder.loadTexts:frMapClassCirOut.setStatus(_A)
if mibBuilder.loadTexts:frMapClassCirOut.setUnits('Bits per second')
class _FrMapClassFrf12Frag_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(16,1600))
_FrMapClassFrf12Frag_Type.__name__=_D
_FrMapClassFrf12Frag_Object=MibTableColumn
frMapClassFrf12Frag=_FrMapClassFrf12Frag_Object((1,3,6,1,4,1,6889,2,1,6,2,4,4,1,5),_FrMapClassFrf12Frag_Type())
frMapClassFrf12Frag.setMaxAccess(_C)
if mibBuilder.loadTexts:frMapClassFrf12Frag.setStatus(_A)
if mibBuilder.loadTexts:frMapClassFrf12Frag.setUnits('Bytes')
_FrMapClassRowStatus_Type=RowStatus
_FrMapClassRowStatus_Object=MibTableColumn
frMapClassRowStatus=_FrMapClassRowStatus_Object((1,3,6,1,4,1,6889,2,1,6,2,4,4,1,6),_FrMapClassRowStatus_Type())
frMapClassRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:frMapClassRowStatus.setStatus(_A)
_WanDialer_ObjectIdentity=ObjectIdentity
wanDialer=_WanDialer_ObjectIdentity((1,3,6,1,4,1,6889,2,1,6,2,5))
_WanDialerTable_Object=MibTable
wanDialerTable=_WanDialerTable_Object((1,3,6,1,4,1,6889,2,1,6,2,5,1))
if mibBuilder.loadTexts:wanDialerTable.setStatus(_A)
_WanDialerEntry_Object=MibTableRow
wanDialerEntry=_WanDialerEntry_Object((1,3,6,1,4,1,6889,2,1,6,2,5,1,1))
wanDialerEntry.setIndexNames((0,_b,_c))
if mibBuilder.loadTexts:wanDialerEntry.setStatus(_A)
_WanDialerModemIf_Type=Integer32
_WanDialerModemIf_Object=MibTableColumn
wanDialerModemIf=_WanDialerModemIf_Object((1,3,6,1,4,1,6889,2,1,6,2,5,1,1,1),_WanDialerModemIf_Type())
wanDialerModemIf.setMaxAccess(_C)
if mibBuilder.loadTexts:wanDialerModemIf.setStatus(_A)
class _WanDialerState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('initModem',1),('idle',2),('waiting4Modem',3),('maxAttemptsDisabled',4),('preDialReset',5),('waitForConnect',6),('waitForDCD',7),('hangUp',8),('persistentDelay',9),('waitForIPCP',10),('connected',11)))
_WanDialerState_Type.__name__=_D
_WanDialerState_Object=MibTableColumn
wanDialerState=_WanDialerState_Object((1,3,6,1,4,1,6889,2,1,6,2,5,1,1,2),_WanDialerState_Type())
wanDialerState.setMaxAccess(_E)
if mibBuilder.loadTexts:wanDialerState.setStatus(_A)
_WanDialerPersistentDelay_Type=Integer32
_WanDialerPersistentDelay_Object=MibTableColumn
wanDialerPersistentDelay=_WanDialerPersistentDelay_Object((1,3,6,1,4,1,6889,2,1,6,2,5,1,1,3),_WanDialerPersistentDelay_Type())
wanDialerPersistentDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:wanDialerPersistentDelay.setStatus(_A)
_WanDialerPersistentMaxAttempts_Type=Integer32
_WanDialerPersistentMaxAttempts_Object=MibTableColumn
wanDialerPersistentMaxAttempts=_WanDialerPersistentMaxAttempts_Object((1,3,6,1,4,1,6889,2,1,6,2,5,1,1,4),_WanDialerPersistentMaxAttempts_Type())
wanDialerPersistentMaxAttempts.setMaxAccess(_C)
if mibBuilder.loadTexts:wanDialerPersistentMaxAttempts.setStatus(_A)
_WanDialerPersistentReenable_Type=Integer32
_WanDialerPersistentReenable_Object=MibTableColumn
wanDialerPersistentReenable=_WanDialerPersistentReenable_Object((1,3,6,1,4,1,6889,2,1,6,2,5,1,1,5),_WanDialerPersistentReenable_Type())
wanDialerPersistentReenable.setMaxAccess(_C)
if mibBuilder.loadTexts:wanDialerPersistentReenable.setStatus(_A)
class _WanDialerOrder_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('sequential',1),('roundRobin',2),('lastSuccessful',3)))
_WanDialerOrder_Type.__name__=_D
_WanDialerOrder_Object=MibTableColumn
wanDialerOrder=_WanDialerOrder_Object((1,3,6,1,4,1,6889,2,1,6,2,5,1,1,6),_WanDialerOrder_Type())
wanDialerOrder.setMaxAccess(_C)
if mibBuilder.loadTexts:wanDialerOrder.setStatus(_A)
_WanDialerString1_Type=DisplayString
_WanDialerString1_Object=MibTableColumn
wanDialerString1=_WanDialerString1_Object((1,3,6,1,4,1,6889,2,1,6,2,5,1,1,7),_WanDialerString1_Type())
wanDialerString1.setMaxAccess(_C)
if mibBuilder.loadTexts:wanDialerString1.setStatus(_A)
_WanDialerString2_Type=DisplayString
_WanDialerString2_Object=MibTableColumn
wanDialerString2=_WanDialerString2_Object((1,3,6,1,4,1,6889,2,1,6,2,5,1,1,8),_WanDialerString2_Type())
wanDialerString2.setMaxAccess(_C)
if mibBuilder.loadTexts:wanDialerString2.setStatus(_A)
_WanDialerString3_Type=DisplayString
_WanDialerString3_Object=MibTableColumn
wanDialerString3=_WanDialerString3_Object((1,3,6,1,4,1,6889,2,1,6,2,5,1,1,9),_WanDialerString3_Type())
wanDialerString3.setMaxAccess(_C)
if mibBuilder.loadTexts:wanDialerString3.setStatus(_A)
_WanDialerString4_Type=DisplayString
_WanDialerString4_Object=MibTableColumn
wanDialerString4=_WanDialerString4_Object((1,3,6,1,4,1,6889,2,1,6,2,5,1,1,10),_WanDialerString4_Type())
wanDialerString4.setMaxAccess(_C)
if mibBuilder.loadTexts:wanDialerString4.setStatus(_A)
_WanDialerString5_Type=DisplayString
_WanDialerString5_Object=MibTableColumn
wanDialerString5=_WanDialerString5_Object((1,3,6,1,4,1,6889,2,1,6,2,5,1,1,11),_WanDialerString5_Type())
wanDialerString5.setMaxAccess(_C)
if mibBuilder.loadTexts:wanDialerString5.setStatus(_A)
_WanDialerLastDialed_Type=DisplayString
_WanDialerLastDialed_Object=MibTableColumn
wanDialerLastDialed=_WanDialerLastDialed_Object((1,3,6,1,4,1,6889,2,1,6,2,5,1,1,12),_WanDialerLastDialed_Type())
wanDialerLastDialed.setMaxAccess(_E)
if mibBuilder.loadTexts:wanDialerLastDialed.setStatus(_A)
class _WanDialerWaitForIpcp_Type(Integer32):defaultValue=45
_WanDialerWaitForIpcp_Type.__name__=_D
_WanDialerWaitForIpcp_Object=MibTableColumn
wanDialerWaitForIpcp=_WanDialerWaitForIpcp_Object((1,3,6,1,4,1,6889,2,1,6,2,5,1,1,13),_WanDialerWaitForIpcp_Type())
wanDialerWaitForIpcp.setMaxAccess(_C)
if mibBuilder.loadTexts:wanDialerWaitForIpcp.setStatus(_A)
class _WanDialerPersistentInitial_Type(Integer32):defaultValue=10
_WanDialerPersistentInitial_Type.__name__=_D
_WanDialerPersistentInitial_Object=MibTableColumn
wanDialerPersistentInitial=_WanDialerPersistentInitial_Object((1,3,6,1,4,1,6889,2,1,6,2,5,1,1,14),_WanDialerPersistentInitial_Type())
wanDialerPersistentInitial.setMaxAccess(_C)
if mibBuilder.loadTexts:wanDialerPersistentInitial.setStatus(_A)
_AvayaEISWanTraps_ObjectIdentity=ObjectIdentity
avayaEISWanTraps=_AvayaEISWanTraps_ObjectIdentity((1,3,6,1,4,1,6889,2,1,6,4))
_AvayaEISWanGroups_ObjectIdentity=ObjectIdentity
avayaEISWanGroups=_AvayaEISWanGroups_ObjectIdentity((1,3,6,1,4,1,6889,2,1,6,5))
_AvayaEISWanCompliances_ObjectIdentity=ObjectIdentity
avayaEISWanCompliances=_AvayaEISWanCompliances_ObjectIdentity((1,3,6,1,4,1,6889,2,1,6,7))
hostModuleGroup=ObjectGroup((1,3,6,1,4,1,6889,2,1,6,5,1))
hostModuleGroup.setObjects(*((_B,_N),(_B,_O),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m)))
if mibBuilder.loadTexts:hostModuleGroup.setStatus(_A)
wanRouterBladeGroup=ObjectGroup((1,3,6,1,4,1,6889,2,1,6,5,2))
wanRouterBladeGroup.setObjects(*((_B,_n),(_B,_Q),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_R),(_B,_V),(_B,_W),(_B,_X),(_B,_A2),(_B,_U),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_S),(_B,_T),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR)))
if mibBuilder.loadTexts:wanRouterBladeGroup.setStatus(_A)
hostModuleCompliance=ModuleCompliance((1,3,6,1,4,1,6889,2,1,6,7,1))
hostModuleCompliance.setObjects((_B,_AS))
if mibBuilder.loadTexts:hostModuleCompliance.setStatus(_A)
wanRouterBladeCompliance=ModuleCompliance((1,3,6,1,4,1,6889,2,1,6,7,2))
wanRouterBladeCompliance.setObjects((_B,_AT))
if mibBuilder.loadTexts:wanRouterBladeCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_G:OnOff,'avayaEISWan':avayaEISWan,'deviceSpecific':deviceSpecific,'x330wanSpecific':x330wanSpecific,'intWanPortTable':intWanPortTable,'intWanPortEntry':intWanPortEntry,_N:intWanGroupID,_O:intWanPortID,_h:intWanPortSpeed,_i:intWanPortMode,_j:intWanPortAutoNegotiation,_k:intWanPortVLANMode,_l:intWanPortVLANBindingMode,_m:intWanPortVlanList,'ds0BundleMemmbersTable':ds0BundleMemmbersTable,'ds0BundleMemmbersEntry':ds0BundleMemmbersEntry,_A9:ds0BundleMemmbersList,_n:ds0BundleSpeedFactor,'ifs':ifs,'ds1objs':ds1objs,_A8:ds1DeviceMode,'ds1CurrentDeviceMode':ds1CurrentDeviceMode,'ifTablePrivateExtensions':ifTablePrivateExtensions,'ifTableXtndTable':ifTableXtndTable,'ifTableXtndEntry':ifTableXtndEntry,_Q:ifTableXtndIndex,_o:ifTableXtndPeerAddress,_p:ifTableXtndVoIPQueue,_q:ifTableXtndCableLength,_r:ifTableXtndGain,_s:ifTableXtndDescription,_t:ifTableXtndKeepAlive,_u:ifTableXtndMtu,_v:ifTableXtndInvertTxClock,_w:ifTableXtndDTELoopback,_x:ifTableXtndIgnoreDCD,_y:ifTableXtndIdleChars,_z:ifTableXtndBandwidth,_A0:ifTableXtndEncapsulation,_AA:ifTableXtndOperStatus,_A7:ifTableXtndBackupCapabilities,_A6:ifTableXtndBackupIf,_A5:ifTableXtndBackupEnableDelay,_A4:ifTableXtndBackupDisableDelay,_A3:ifTableXtndPrimaryIf,_AR:ifTableXtndCarrierDelay,_AQ:ifTableXtndDtrRestartDelay,_AI:ifTableXtndDtrPulseTime,_AH:ifTableXtndLoadInterval,_AG:ifTableXtndInputRate,_AF:ifTableXtndOutputRate,_AE:ifTableXtndInputLoad,_AD:ifTableXtndOutputLoad,_AC:ifTableXtndReliability,'ifTableXtndTrafficShaperRate':ifTableXtndTrafficShaperRate,'ifTableXtndCacBBL':ifTableXtndCacBBL,'ifTableXtndCacPriority':ifTableXtndCacPriority,'ifTableXtndCacifStatus':ifTableXtndCacifStatus,'ifTableXtndCommonApplifStatus':ifTableXtndCommonApplifStatus,'ifTableXtndIpSecDfBit':ifTableXtndIpSecDfBit,'ifTableXtndMinPmtu':ifTableXtndMinPmtu,'ifTableXtndConfString':ifTableXtndConfString,'ifTableXtndPppIpcpDnsOptionRequest':ifTableXtndPppIpcpDnsOptionRequest,'ifTableXtndKeepaliveTrackId':ifTableXtndKeepaliveTrackId,_AO:ifTableXtndFrTrafficShaping,'ifTableXtndType':ifTableXtndType,'xtndKeepAliveTable':xtndKeepAliveTable,'xtndKeepAliveEntry':xtndKeepAliveEntry,_f:xtndKeepAliveifIndex,'xtndKeepAliveMethod':xtndKeepAliveMethod,'xtndKeepAliveTimeout':xtndKeepAliveTimeout,'xtndKeepAliveUpRetries':xtndKeepAliveUpRetries,'xtndKeepAliveDownRetries':xtndKeepAliveDownRetries,'xtndKeepAliveInterval':xtndKeepAliveInterval,'xtndKeepAliveSrcIPAddr':xtndKeepAliveSrcIPAddr,'xtndKeepAliveIPAddr':xtndKeepAliveIPAddr,'xtndKeepAliveNextHopMAC':xtndKeepAliveNextHopMAC,'xtndKeepAliveStatus':xtndKeepAliveStatus,'xtndKeepAliveMode':xtndKeepAliveMode,_e:frameRelay,'frDlcmiXtndTable':frDlcmiXtndTable,'frDlcmiXtndEntry':frDlcmiXtndEntry,_R:frDlcmiXtndIndex,_A1:frDlcmiXtndLMIAutoSense,'frStaticCircuitTable':frStaticCircuitTable,'frStaticCircuitEntry':frStaticCircuitEntry,_S:frStaticCircuitSubIfIndex,_T:frStaticCircuitDLCI,_U:frStaticCircuitDLCIrole,_AB:frStaticCircuitStatus,_AP:frStaticCircuitMapClass,'frSubIfTable':frSubIfTable,'frSubIfEntry':frSubIfEntry,_V:frSubIfDlcmiIndex,_W:frSubIfSubIndex,_X:frSubIfType,_A2:frSubIfStatus,'frMapClassTable':frMapClassTable,'frMapClassEntry':frMapClassEntry,_g:frMapClassName,_AN:frMapClassBcOut,_AM:frMapClassBeOut,_AL:frMapClassCirOut,_AK:frMapClassFrf12Frag,_AJ:frMapClassRowStatus,'wanDialer':wanDialer,'wanDialerTable':wanDialerTable,'wanDialerEntry':wanDialerEntry,'wanDialerModemIf':wanDialerModemIf,'wanDialerState':wanDialerState,'wanDialerPersistentDelay':wanDialerPersistentDelay,'wanDialerPersistentMaxAttempts':wanDialerPersistentMaxAttempts,'wanDialerPersistentReenable':wanDialerPersistentReenable,'wanDialerOrder':wanDialerOrder,'wanDialerString1':wanDialerString1,'wanDialerString2':wanDialerString2,'wanDialerString3':wanDialerString3,'wanDialerString4':wanDialerString4,'wanDialerString5':wanDialerString5,'wanDialerLastDialed':wanDialerLastDialed,'wanDialerWaitForIpcp':wanDialerWaitForIpcp,'wanDialerPersistentInitial':wanDialerPersistentInitial,'avayaEISWanTraps':avayaEISWanTraps,'avayaEISWanGroups':avayaEISWanGroups,_AS:hostModuleGroup,_AT:wanRouterBladeGroup,'avayaEISWanCompliances':avayaEISWanCompliances,'hostModuleCompliance':hostModuleCompliance,'wanRouterBladeCompliance':wanRouterBladeCompliance})