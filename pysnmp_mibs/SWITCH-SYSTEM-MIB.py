_r='rcMacMoveLastVlan'
_q='rcMacMoveLastMacaddress'
_p='rcMacMoveLastPortIndex'
_o='rcPortLoopbackDetectDownTime'
_n='rcPortLoopbackDetectSrcPort'
_m='rcComboPortIndex'
_l='rcComboIndex'
_k='normal'
_j='fiber-100M'
_i='fiber-1000M'
_h='copper-100M'
_g='copper-1000M'
_f='copper'
_e='full-1000'
_d='half-1000'
_c='full-100'
_b='half-100'
_a='full-10'
_Z='half-10'
_Y='obsolete'
_X='percent'
_W='px-1000M'
_V='rcSlotIndex'
_U='rcPortMediaAttachCapability'
_T='rcPortMediaAttachType'
_S='rcPortType'
_R='second'
_Q='tx-100M'
_P='fx-SigMode-100M'
_O='fx-DulMode-100M'
_N='fx-SigMode-1000M'
_M='tx-1000M'
_L='fx-DulMode-1000M'
_K='not-accessible'
_J='deprecated'
_I='inexistence'
_H='rcPortIndex'
_G='EnableVar'
_F='SWITCH-SYSTEM-MIB'
_E='mandatory'
_D='Integer32'
_C='read-only'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
iscomSwitch,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','iscomSwitch')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
EnableVar,PortList,Vlanset=mibBuilder.importSymbols('SWITCH-TC',_G,'PortList','Vlanset')
rcSystem=ModuleIdentity((1,3,6,1,4,1,8886,6,1,1))
if mibBuilder.loadTexts:rcSystem.setRevisions(('1904-12-17 00:00',))
_RcSwitchInformation_ObjectIdentity=ObjectIdentity
rcSwitchInformation=_RcSwitchInformation_ObjectIdentity((1,3,6,1,4,1,8886,6,1,1,1))
_RcSwitchRoseVersion_Type=OctetString
_RcSwitchRoseVersion_Object=MibScalar
rcSwitchRoseVersion=_RcSwitchRoseVersion_Object((1,3,6,1,4,1,8886,6,1,1,1,1),_RcSwitchRoseVersion_Type())
rcSwitchRoseVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:rcSwitchRoseVersion.setStatus(_A)
_RcSwitchHardwareVersion_Type=OctetString
_RcSwitchHardwareVersion_Object=MibScalar
rcSwitchHardwareVersion=_RcSwitchHardwareVersion_Object((1,3,6,1,4,1,8886,6,1,1,1,2),_RcSwitchHardwareVersion_Type())
rcSwitchHardwareVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:rcSwitchHardwareVersion.setStatus(_A)
_RcSwitchServiceInfo_Type=Integer32
_RcSwitchServiceInfo_Object=MibScalar
rcSwitchServiceInfo=_RcSwitchServiceInfo_Object((1,3,6,1,4,1,8886,6,1,1,1,3),_RcSwitchServiceInfo_Type())
rcSwitchServiceInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:rcSwitchServiceInfo.setStatus(_J)
class _RcSwitchLastErrorCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_RcSwitchLastErrorCode_Type.__name__=_D
_RcSwitchLastErrorCode_Object=MibScalar
rcSwitchLastErrorCode=_RcSwitchLastErrorCode_Object((1,3,6,1,4,1,8886,6,1,1,1,4),_RcSwitchLastErrorCode_Type())
rcSwitchLastErrorCode.setMaxAccess(_C)
if mibBuilder.loadTexts:rcSwitchLastErrorCode.setStatus(_J)
_RcSwitchMaxPhysicalPortNum_Type=Integer32
_RcSwitchMaxPhysicalPortNum_Object=MibScalar
rcSwitchMaxPhysicalPortNum=_RcSwitchMaxPhysicalPortNum_Object((1,3,6,1,4,1,8886,6,1,1,1,5),_RcSwitchMaxPhysicalPortNum_Type())
rcSwitchMaxPhysicalPortNum.setMaxAccess(_C)
if mibBuilder.loadTexts:rcSwitchMaxPhysicalPortNum.setStatus(_A)
_RcSwitchMaxAggregationPortNum_Type=Integer32
_RcSwitchMaxAggregationPortNum_Object=MibScalar
rcSwitchMaxAggregationPortNum=_RcSwitchMaxAggregationPortNum_Object((1,3,6,1,4,1,8886,6,1,1,1,6),_RcSwitchMaxAggregationPortNum_Type())
rcSwitchMaxAggregationPortNum.setMaxAccess(_C)
if mibBuilder.loadTexts:rcSwitchMaxAggregationPortNum.setStatus(_A)
_RcSwitchMaxL3IpSubnetNum_Type=Integer32
_RcSwitchMaxL3IpSubnetNum_Object=MibScalar
rcSwitchMaxL3IpSubnetNum=_RcSwitchMaxL3IpSubnetNum_Object((1,3,6,1,4,1,8886,6,1,1,1,7),_RcSwitchMaxL3IpSubnetNum_Type())
rcSwitchMaxL3IpSubnetNum.setMaxAccess(_C)
if mibBuilder.loadTexts:rcSwitchMaxL3IpSubnetNum.setStatus(_A)
_RcSwitchMacTableCapability_Type=Integer32
_RcSwitchMacTableCapability_Object=MibScalar
rcSwitchMacTableCapability=_RcSwitchMacTableCapability_Object((1,3,6,1,4,1,8886,6,1,1,1,8),_RcSwitchMacTableCapability_Type())
rcSwitchMacTableCapability.setMaxAccess(_C)
if mibBuilder.loadTexts:rcSwitchMacTableCapability.setStatus(_A)
_RcSwitchMacAddress_Type=MacAddress
_RcSwitchMacAddress_Object=MibScalar
rcSwitchMacAddress=_RcSwitchMacAddress_Object((1,3,6,1,4,1,8886,6,1,1,1,9),_RcSwitchMacAddress_Type())
rcSwitchMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:rcSwitchMacAddress.setStatus(_A)
_RcSwitchVlanSpaceSize_Type=Integer32
_RcSwitchVlanSpaceSize_Object=MibScalar
rcSwitchVlanSpaceSize=_RcSwitchVlanSpaceSize_Object((1,3,6,1,4,1,8886,6,1,1,1,10),_RcSwitchVlanSpaceSize_Type())
rcSwitchVlanSpaceSize.setMaxAccess(_C)
if mibBuilder.loadTexts:rcSwitchVlanSpaceSize.setStatus(_A)
_RcSwitchPvidSpaceSize_Type=Integer32
_RcSwitchPvidSpaceSize_Object=MibScalar
rcSwitchPvidSpaceSize=_RcSwitchPvidSpaceSize_Object((1,3,6,1,4,1,8886,6,1,1,1,11),_RcSwitchPvidSpaceSize_Type())
rcSwitchPvidSpaceSize.setMaxAccess(_C)
if mibBuilder.loadTexts:rcSwitchPvidSpaceSize.setStatus(_A)
_RcSwitchDefaultVlan_Type=Integer32
_RcSwitchDefaultVlan_Object=MibScalar
rcSwitchDefaultVlan=_RcSwitchDefaultVlan_Object((1,3,6,1,4,1,8886,6,1,1,1,12),_RcSwitchDefaultVlan_Type())
rcSwitchDefaultVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:rcSwitchDefaultVlan.setStatus(_A)
_RcSwitchBootstrapVersion_Type=OctetString
_RcSwitchBootstrapVersion_Object=MibScalar
rcSwitchBootstrapVersion=_RcSwitchBootstrapVersion_Object((1,3,6,1,4,1,8886,6,1,1,1,13),_RcSwitchBootstrapVersion_Type())
rcSwitchBootstrapVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:rcSwitchBootstrapVersion.setStatus(_A)
_RcSwitchSerialNumber_Type=OctetString
_RcSwitchSerialNumber_Object=MibScalar
rcSwitchSerialNumber=_RcSwitchSerialNumber_Object((1,3,6,1,4,1,8886,6,1,1,1,14),_RcSwitchSerialNumber_Type())
rcSwitchSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:rcSwitchSerialNumber.setStatus(_A)
_RcSwitchFpgaVersion_Type=OctetString
_RcSwitchFpgaVersion_Object=MibScalar
rcSwitchFpgaVersion=_RcSwitchFpgaVersion_Object((1,3,6,1,4,1,8886,6,1,1,1,15),_RcSwitchFpgaVersion_Type())
rcSwitchFpgaVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:rcSwitchFpgaVersion.setStatus(_A)
_RcSwitchProductVersion_Type=OctetString
_RcSwitchProductVersion_Object=MibScalar
rcSwitchProductVersion=_RcSwitchProductVersion_Object((1,3,6,1,4,1,8886,6,1,1,1,16),_RcSwitchProductVersion_Type())
rcSwitchProductVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:rcSwitchProductVersion.setStatus(_A)
_RcSwitchCmpAbName_Type=OctetString
_RcSwitchCmpAbName_Object=MibScalar
rcSwitchCmpAbName=_RcSwitchCmpAbName_Object((1,3,6,1,4,1,8886,6,1,1,1,17),_RcSwitchCmpAbName_Type())
rcSwitchCmpAbName.setMaxAccess(_C)
if mibBuilder.loadTexts:rcSwitchCmpAbName.setStatus(_A)
_RcSwitchCmpFullName_Type=OctetString
_RcSwitchCmpFullName_Object=MibScalar
rcSwitchCmpFullName=_RcSwitchCmpFullName_Object((1,3,6,1,4,1,8886,6,1,1,1,18),_RcSwitchCmpFullName_Type())
rcSwitchCmpFullName.setMaxAccess(_C)
if mibBuilder.loadTexts:rcSwitchCmpFullName.setStatus(_A)
_RcSwitchDeviceName_Type=OctetString
_RcSwitchDeviceName_Object=MibScalar
rcSwitchDeviceName=_RcSwitchDeviceName_Object((1,3,6,1,4,1,8886,6,1,1,1,19),_RcSwitchDeviceName_Type())
rcSwitchDeviceName.setMaxAccess(_C)
if mibBuilder.loadTexts:rcSwitchDeviceName.setStatus(_A)
_RcSlotInformation_ObjectIdentity=ObjectIdentity
rcSlotInformation=_RcSlotInformation_ObjectIdentity((1,3,6,1,4,1,8886,6,1,1,2))
_RcSlotNum_Type=Integer32
_RcSlotNum_Object=MibScalar
rcSlotNum=_RcSlotNum_Object((1,3,6,1,4,1,8886,6,1,1,2,1),_RcSlotNum_Type())
rcSlotNum.setMaxAccess(_C)
if mibBuilder.loadTexts:rcSlotNum.setStatus(_A)
_RcSlotStateTable_Object=MibTable
rcSlotStateTable=_RcSlotStateTable_Object((1,3,6,1,4,1,8886,6,1,1,2,2))
if mibBuilder.loadTexts:rcSlotStateTable.setStatus(_A)
_RcSlotStateEntry_Object=MibTableRow
rcSlotStateEntry=_RcSlotStateEntry_Object((1,3,6,1,4,1,8886,6,1,1,2,2,1))
rcSlotStateEntry.setIndexNames((0,_F,_V))
if mibBuilder.loadTexts:rcSlotStateEntry.setStatus(_A)
_RcSlotIndex_Type=Integer32
_RcSlotIndex_Object=MibTableColumn
rcSlotIndex=_RcSlotIndex_Object((1,3,6,1,4,1,8886,6,1,1,2,2,1,1),_RcSlotIndex_Type())
rcSlotIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:rcSlotIndex.setStatus(_A)
_RcSlotPortStart_Type=Integer32
_RcSlotPortStart_Object=MibTableColumn
rcSlotPortStart=_RcSlotPortStart_Object((1,3,6,1,4,1,8886,6,1,1,2,2,1,2),_RcSlotPortStart_Type())
rcSlotPortStart.setMaxAccess(_C)
if mibBuilder.loadTexts:rcSlotPortStart.setStatus(_A)
_RcSlotPortNum_Type=Integer32
_RcSlotPortNum_Object=MibTableColumn
rcSlotPortNum=_RcSlotPortNum_Object((1,3,6,1,4,1,8886,6,1,1,2,2,1,3),_RcSlotPortNum_Type())
rcSlotPortNum.setMaxAccess(_C)
if mibBuilder.loadTexts:rcSlotPortNum.setStatus(_A)
class _RcSlotType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_I,0),(_L,1),(_M,2),(_N,3),(_O,4),(_P,5),(_Q,6),(_W,7)))
_RcSlotType_Type.__name__=_D
_RcSlotType_Object=MibTableColumn
rcSlotType=_RcSlotType_Object((1,3,6,1,4,1,8886,6,1,1,2,2,1,4),_RcSlotType_Type())
rcSlotType.setMaxAccess(_C)
if mibBuilder.loadTexts:rcSlotType.setStatus(_A)
_RcSwitchConfig_ObjectIdentity=ObjectIdentity
rcSwitchConfig=_RcSwitchConfig_ObjectIdentity((1,3,6,1,4,1,8886,6,1,1,3))
class _RcMacAgingTime_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_RcMacAgingTime_Type.__name__=_D
_RcMacAgingTime_Object=MibScalar
rcMacAgingTime=_RcMacAgingTime_Object((1,3,6,1,4,1,8886,6,1,1,3,1),_RcMacAgingTime_Type())
rcMacAgingTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMacAgingTime.setStatus(_A)
if mibBuilder.loadTexts:rcMacAgingTime.setUnits(_R)
class _RcStormControlBcastEnable_Type(EnableVar):defaultValue=1
_RcStormControlBcastEnable_Type.__name__=_G
_RcStormControlBcastEnable_Object=MibScalar
rcStormControlBcastEnable=_RcStormControlBcastEnable_Object((1,3,6,1,4,1,8886,6,1,1,3,2),_RcStormControlBcastEnable_Type())
rcStormControlBcastEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:rcStormControlBcastEnable.setStatus(_E)
class _RcStormControlMcastEnable_Type(EnableVar):defaultValue=2
_RcStormControlMcastEnable_Type.__name__=_G
_RcStormControlMcastEnable_Object=MibScalar
rcStormControlMcastEnable=_RcStormControlMcastEnable_Object((1,3,6,1,4,1,8886,6,1,1,3,3),_RcStormControlMcastEnable_Type())
rcStormControlMcastEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:rcStormControlMcastEnable.setStatus(_E)
class _RcStormControlDlfEnable_Type(EnableVar):defaultValue=2
_RcStormControlDlfEnable_Type.__name__=_G
_RcStormControlDlfEnable_Object=MibScalar
rcStormControlDlfEnable=_RcStormControlDlfEnable_Object((1,3,6,1,4,1,8886,6,1,1,3,4),_RcStormControlDlfEnable_Type())
rcStormControlDlfEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:rcStormControlDlfEnable.setStatus(_E)
class _RcStormControlpps_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,262143))
_RcStormControlpps_Type.__name__=_D
_RcStormControlpps_Object=MibScalar
rcStormControlpps=_RcStormControlpps_Object((1,3,6,1,4,1,8886,6,1,1,3,5),_RcStormControlpps_Type())
rcStormControlpps.setMaxAccess(_B)
if mibBuilder.loadTexts:rcStormControlpps.setStatus(_E)
if mibBuilder.loadTexts:rcStormControlpps.setUnits('pps')
class _RcStormControlbps_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1073741823))
_RcStormControlbps_Type.__name__=_D
_RcStormControlbps_Object=MibScalar
rcStormControlbps=_RcStormControlbps_Object((1,3,6,1,4,1,8886,6,1,1,3,6),_RcStormControlbps_Type())
rcStormControlbps.setMaxAccess(_B)
if mibBuilder.loadTexts:rcStormControlbps.setStatus(_E)
if mibBuilder.loadTexts:rcStormControlbps.setUnits('bps')
class _RcStormControlRatio_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_RcStormControlRatio_Type.__name__=_D
_RcStormControlRatio_Object=MibScalar
rcStormControlRatio=_RcStormControlRatio_Object((1,3,6,1,4,1,8886,6,1,1,3,7),_RcStormControlRatio_Type())
rcStormControlRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:rcStormControlRatio.setStatus(_E)
if mibBuilder.loadTexts:rcStormControlRatio.setUnits(_X)
class _RcStormControlBurst_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,512))
_RcStormControlBurst_Type.__name__=_D
_RcStormControlBurst_Object=MibScalar
rcStormControlBurst=_RcStormControlBurst_Object((1,3,6,1,4,1,8886,6,1,1,3,8),_RcStormControlBurst_Type())
rcStormControlBurst.setMaxAccess(_B)
if mibBuilder.loadTexts:rcStormControlBurst.setStatus(_E)
if mibBuilder.loadTexts:rcStormControlBurst.setUnits('kB')
class _RcStpEnable_Type(EnableVar):defaultValue=1
_RcStpEnable_Type.__name__=_G
_RcStpEnable_Object=MibScalar
rcStpEnable=_RcStpEnable_Object((1,3,6,1,4,1,8886,6,1,1,3,9),_RcStpEnable_Type())
rcStpEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:rcStpEnable.setStatus(_E)
class _RcSvlEnable_Type(EnableVar):defaultValue=2
_RcSvlEnable_Type.__name__=_G
_RcSvlEnable_Object=MibScalar
rcSvlEnable=_RcSvlEnable_Object((1,3,6,1,4,1,8886,6,1,1,3,10),_RcSvlEnable_Type())
rcSvlEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:rcSvlEnable.setStatus(_E)
class _RcGarpEnable_Type(EnableVar):defaultValue=2
_RcGarpEnable_Type.__name__=_G
_RcGarpEnable_Object=MibScalar
rcGarpEnable=_RcGarpEnable_Object((1,3,6,1,4,1,8886,6,1,1,3,11),_RcGarpEnable_Type())
rcGarpEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:rcGarpEnable.setStatus(_E)
class _RcLacpEnable_Type(EnableVar):defaultValue=2
_RcLacpEnable_Type.__name__=_G
_RcLacpEnable_Object=MibScalar
rcLacpEnable=_RcLacpEnable_Object((1,3,6,1,4,1,8886,6,1,1,3,12),_RcLacpEnable_Type())
rcLacpEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:rcLacpEnable.setStatus(_E)
class _RcVlanSpaceNum_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4093))
_RcVlanSpaceNum_Type.__name__=_D
_RcVlanSpaceNum_Object=MibScalar
rcVlanSpaceNum=_RcVlanSpaceNum_Object((1,3,6,1,4,1,8886,6,1,1,3,13),_RcVlanSpaceNum_Type())
rcVlanSpaceNum.setMaxAccess(_B)
if mibBuilder.loadTexts:rcVlanSpaceNum.setStatus(_Y)
class _RcPvidSpaceNum_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4093))
_RcPvidSpaceNum_Type.__name__=_D
_RcPvidSpaceNum_Object=MibScalar
rcPvidSpaceNum=_RcPvidSpaceNum_Object((1,3,6,1,4,1,8886,6,1,1,3,14),_RcPvidSpaceNum_Type())
rcPvidSpaceNum.setMaxAccess(_B)
if mibBuilder.loadTexts:rcPvidSpaceNum.setStatus(_Y)
class _RcLoopbackDetectInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_RcLoopbackDetectInterval_Type.__name__=_D
_RcLoopbackDetectInterval_Object=MibScalar
rcLoopbackDetectInterval=_RcLoopbackDetectInterval_Object((1,3,6,1,4,1,8886,6,1,1,3,15),_RcLoopbackDetectInterval_Type())
rcLoopbackDetectInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:rcLoopbackDetectInterval.setStatus(_A)
if mibBuilder.loadTexts:rcLoopbackDetectInterval.setUnits(_R)
class _RcArpAgingTime_Type(Integer32):defaultValue=1200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_RcArpAgingTime_Type.__name__=_D
_RcArpAgingTime_Object=MibScalar
rcArpAgingTime=_RcArpAgingTime_Object((1,3,6,1,4,1,8886,6,1,1,3,16),_RcArpAgingTime_Type())
rcArpAgingTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rcArpAgingTime.setStatus(_J)
if mibBuilder.loadTexts:rcArpAgingTime.setUnits(_R)
_RcBpduTransPorts_Type=PortList
_RcBpduTransPorts_Object=MibScalar
rcBpduTransPorts=_RcBpduTransPorts_Object((1,3,6,1,4,1,8886,6,1,1,3,17),_RcBpduTransPorts_Type())
rcBpduTransPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:rcBpduTransPorts.setStatus(_A)
_RcDot1xTransPorts_Type=PortList
_RcDot1xTransPorts_Object=MibScalar
rcDot1xTransPorts=_RcDot1xTransPorts_Object((1,3,6,1,4,1,8886,6,1,1,3,18),_RcDot1xTransPorts_Type())
rcDot1xTransPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:rcDot1xTransPorts.setStatus(_A)
_RcLacpTransPorts_Type=PortList
_RcLacpTransPorts_Object=MibScalar
rcLacpTransPorts=_RcLacpTransPorts_Object((1,3,6,1,4,1,8886,6,1,1,3,19),_RcLacpTransPorts_Type())
rcLacpTransPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:rcLacpTransPorts.setStatus(_A)
_RcGarpTransPorts_Type=PortList
_RcGarpTransPorts_Object=MibScalar
rcGarpTransPorts=_RcGarpTransPorts_Object((1,3,6,1,4,1,8886,6,1,1,3,20),_RcGarpTransPorts_Type())
rcGarpTransPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:rcGarpTransPorts.setStatus(_A)
_RcGmrpTransPorts_Type=PortList
_RcGmrpTransPorts_Object=MibScalar
rcGmrpTransPorts=_RcGmrpTransPorts_Object((1,3,6,1,4,1,8886,6,1,1,3,21),_RcGmrpTransPorts_Type())
rcGmrpTransPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:rcGmrpTransPorts.setStatus(_A)
_RcGvrpTransPorts_Type=PortList
_RcGvrpTransPorts_Object=MibScalar
rcGvrpTransPorts=_RcGvrpTransPorts_Object((1,3,6,1,4,1,8886,6,1,1,3,22),_RcGvrpTransPorts_Type())
rcGvrpTransPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:rcGvrpTransPorts.setStatus(_A)
class _RcIpRouting_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('startIpRouting',1),('stopIpRouting',2)))
_RcIpRouting_Type.__name__=_D
_RcIpRouting_Object=MibScalar
rcIpRouting=_RcIpRouting_Object((1,3,6,1,4,1,8886,6,1,1,3,23),_RcIpRouting_Type())
rcIpRouting.setMaxAccess(_B)
if mibBuilder.loadTexts:rcIpRouting.setStatus(_A)
class _RcStaticRouteDistance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_RcStaticRouteDistance_Type.__name__=_D
_RcStaticRouteDistance_Object=MibScalar
rcStaticRouteDistance=_RcStaticRouteDistance_Object((1,3,6,1,4,1,8886,6,1,1,3,24),_RcStaticRouteDistance_Type())
rcStaticRouteDistance.setMaxAccess(_B)
if mibBuilder.loadTexts:rcStaticRouteDistance.setStatus(_A)
_RcFastRoute_Type=TruthValue
_RcFastRoute_Object=MibScalar
rcFastRoute=_RcFastRoute_Object((1,3,6,1,4,1,8886,6,1,1,3,25),_RcFastRoute_Type())
rcFastRoute.setMaxAccess(_B)
if mibBuilder.loadTexts:rcFastRoute.setStatus(_A)
_RcDlfForwardingEnable_Type=EnableVar
_RcDlfForwardingEnable_Object=MibScalar
rcDlfForwardingEnable=_RcDlfForwardingEnable_Object((1,3,6,1,4,1,8886,6,1,1,3,26),_RcDlfForwardingEnable_Type())
rcDlfForwardingEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:rcDlfForwardingEnable.setStatus(_E)
class _RcLoopbackDetectVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_RcLoopbackDetectVlan_Type.__name__=_D
_RcLoopbackDetectVlan_Object=MibScalar
rcLoopbackDetectVlan=_RcLoopbackDetectVlan_Object((1,3,6,1,4,1,8886,6,1,1,3,27),_RcLoopbackDetectVlan_Type())
rcLoopbackDetectVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:rcLoopbackDetectVlan.setStatus(_E)
_RcLoopbackDetectDestAddr_Type=MacAddress
_RcLoopbackDetectDestAddr_Object=MibScalar
rcLoopbackDetectDestAddr=_RcLoopbackDetectDestAddr_Object((1,3,6,1,4,1,8886,6,1,1,3,28),_RcLoopbackDetectDestAddr_Type())
rcLoopbackDetectDestAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:rcLoopbackDetectDestAddr.setStatus(_E)
class _RcMaxAllowedFrameLength_Type(Integer32):defaultValue=1522;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1500,65535))
_RcMaxAllowedFrameLength_Type.__name__=_D
_RcMaxAllowedFrameLength_Object=MibScalar
rcMaxAllowedFrameLength=_RcMaxAllowedFrameLength_Object((1,3,6,1,4,1,8886,6,1,1,3,29),_RcMaxAllowedFrameLength_Type())
rcMaxAllowedFrameLength.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMaxAllowedFrameLength.setStatus(_E)
class _RcSvlDefaultVlan_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_RcSvlDefaultVlan_Type.__name__=_D
_RcSvlDefaultVlan_Object=MibScalar
rcSvlDefaultVlan=_RcSvlDefaultVlan_Object((1,3,6,1,4,1,8886,6,1,1,3,30),_RcSvlDefaultVlan_Type())
rcSvlDefaultVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:rcSvlDefaultVlan.setStatus(_E)
class _RcTelnetMaxSessions_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_RcTelnetMaxSessions_Type.__name__=_D
_RcTelnetMaxSessions_Object=MibScalar
rcTelnetMaxSessions=_RcTelnetMaxSessions_Object((1,3,6,1,4,1,8886,6,1,1,3,31),_RcTelnetMaxSessions_Type())
rcTelnetMaxSessions.setMaxAccess(_B)
if mibBuilder.loadTexts:rcTelnetMaxSessions.setStatus(_A)
_RcTelnetAcceptPorts_Type=PortList
_RcTelnetAcceptPorts_Object=MibScalar
rcTelnetAcceptPorts=_RcTelnetAcceptPorts_Object((1,3,6,1,4,1,8886,6,1,1,3,32),_RcTelnetAcceptPorts_Type())
rcTelnetAcceptPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:rcTelnetAcceptPorts.setStatus(_A)
_RcVlanMacLearning_Type=Vlanset
_RcVlanMacLearning_Object=MibScalar
rcVlanMacLearning=_RcVlanMacLearning_Object((1,3,6,1,4,1,8886,6,1,1,3,33),_RcVlanMacLearning_Type())
rcVlanMacLearning.setMaxAccess(_B)
if mibBuilder.loadTexts:rcVlanMacLearning.setStatus(_A)
_RcConsoleEnable_Type=EnableVar
_RcConsoleEnable_Object=MibScalar
rcConsoleEnable=_RcConsoleEnable_Object((1,3,6,1,4,1,8886,6,1,1,3,34),_RcConsoleEnable_Type())
rcConsoleEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:rcConsoleEnable.setStatus(_A)
_RcMacTrapEnable_Type=EnableVar
_RcMacTrapEnable_Object=MibScalar
rcMacTrapEnable=_RcMacTrapEnable_Object((1,3,6,1,4,1,8886,6,1,1,3,35),_RcMacTrapEnable_Type())
rcMacTrapEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMacTrapEnable.setStatus(_A)
_RcMacMoveEnable_Type=EnableVar
_RcMacMoveEnable_Object=MibScalar
rcMacMoveEnable=_RcMacMoveEnable_Object((1,3,6,1,4,1,8886,6,1,1,3,36),_RcMacMoveEnable_Type())
rcMacMoveEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMacMoveEnable.setStatus(_A)
_RcMacMoveLastPortIndex_Type=Integer32
_RcMacMoveLastPortIndex_Object=MibScalar
rcMacMoveLastPortIndex=_RcMacMoveLastPortIndex_Object((1,3,6,1,4,1,8886,6,1,1,3,37),_RcMacMoveLastPortIndex_Type())
rcMacMoveLastPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:rcMacMoveLastPortIndex.setStatus(_A)
_RcMacMoveLastMacaddress_Type=MacAddress
_RcMacMoveLastMacaddress_Object=MibScalar
rcMacMoveLastMacaddress=_RcMacMoveLastMacaddress_Object((1,3,6,1,4,1,8886,6,1,1,3,38),_RcMacMoveLastMacaddress_Type())
rcMacMoveLastMacaddress.setMaxAccess(_C)
if mibBuilder.loadTexts:rcMacMoveLastMacaddress.setStatus(_A)
class _RcMacMoveLastVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_RcMacMoveLastVlan_Type.__name__=_D
_RcMacMoveLastVlan_Object=MibScalar
rcMacMoveLastVlan=_RcMacMoveLastVlan_Object((1,3,6,1,4,1,8886,6,1,1,3,39),_RcMacMoveLastVlan_Type())
rcMacMoveLastVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:rcMacMoveLastVlan.setStatus(_A)
_RcPortInfoConfig_ObjectIdentity=ObjectIdentity
rcPortInfoConfig=_RcPortInfoConfig_ObjectIdentity((1,3,6,1,4,1,8886,6,1,1,4))
_RcPortTable_Object=MibTable
rcPortTable=_RcPortTable_Object((1,3,6,1,4,1,8886,6,1,1,4,1))
if mibBuilder.loadTexts:rcPortTable.setStatus(_A)
_RcPortEntry_Object=MibTableRow
rcPortEntry=_RcPortEntry_Object((1,3,6,1,4,1,8886,6,1,1,4,1,1))
rcPortEntry.setIndexNames((0,_F,_H))
if mibBuilder.loadTexts:rcPortEntry.setStatus(_A)
_RcPortIndex_Type=Integer32
_RcPortIndex_Object=MibTableColumn
rcPortIndex=_RcPortIndex_Object((1,3,6,1,4,1,8886,6,1,1,4,1,1,1),_RcPortIndex_Type())
rcPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:rcPortIndex.setStatus(_A)
class _RcPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_I,0),(_L,1),(_M,2),(_N,3),(_O,4),(_P,5),(_Q,6),(_W,7)))
_RcPortType_Type.__name__=_D
_RcPortType_Object=MibTableColumn
rcPortType=_RcPortType_Object((1,3,6,1,4,1,8886,6,1,1,4,1,1,2),_RcPortType_Type())
rcPortType.setMaxAccess(_C)
if mibBuilder.loadTexts:rcPortType.setStatus(_A)
_RcSlotTableIndex_Type=Integer32
_RcSlotTableIndex_Object=MibTableColumn
rcSlotTableIndex=_RcSlotTableIndex_Object((1,3,6,1,4,1,8886,6,1,1,4,1,1,3),_RcSlotTableIndex_Type())
rcSlotTableIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:rcSlotTableIndex.setStatus(_A)
_RcSlotPortIndex_Type=Integer32
_RcSlotPortIndex_Object=MibTableColumn
rcSlotPortIndex=_RcSlotPortIndex_Object((1,3,6,1,4,1,8886,6,1,1,4,1,1,4),_RcSlotPortIndex_Type())
rcSlotPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:rcSlotPortIndex.setStatus(_A)
class _RcPortAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_RcPortAdminStatus_Type.__name__=_D
_RcPortAdminStatus_Object=MibTableColumn
rcPortAdminStatus=_RcPortAdminStatus_Object((1,3,6,1,4,1,8886,6,1,1,4,1,1,5),_RcPortAdminStatus_Type())
rcPortAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcPortAdminStatus.setStatus(_A)
class _RcPortOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_RcPortOperStatus_Type.__name__=_D
_RcPortOperStatus_Object=MibTableColumn
rcPortOperStatus=_RcPortOperStatus_Object((1,3,6,1,4,1,8886,6,1,1,4,1,1,6),_RcPortOperStatus_Type())
rcPortOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rcPortOperStatus.setStatus(_A)
class _RcPortDuplexSpeedSet_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('autonegotiate',1),(_Z,2),(_a,3),(_b,4),(_c,5),(_d,6),(_e,7)))
_RcPortDuplexSpeedSet_Type.__name__=_D
_RcPortDuplexSpeedSet_Object=MibTableColumn
rcPortDuplexSpeedSet=_RcPortDuplexSpeedSet_Object((1,3,6,1,4,1,8886,6,1,1,4,1,1,7),_RcPortDuplexSpeedSet_Type())
rcPortDuplexSpeedSet.setMaxAccess(_B)
if mibBuilder.loadTexts:rcPortDuplexSpeedSet.setStatus(_A)
class _RcPortDuplexSpeedGet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,99)));namedValues=NamedValues(*(('unknown',1),(_Z,2),(_a,3),(_b,4),(_c,5),(_d,6),(_e,7),('illegal',99)))
_RcPortDuplexSpeedGet_Type.__name__=_D
_RcPortDuplexSpeedGet_Object=MibTableColumn
rcPortDuplexSpeedGet=_RcPortDuplexSpeedGet_Object((1,3,6,1,4,1,8886,6,1,1,4,1,1,8),_RcPortDuplexSpeedGet_Type())
rcPortDuplexSpeedGet.setMaxAccess(_C)
if mibBuilder.loadTexts:rcPortDuplexSpeedGet.setStatus(_A)
class _RcPortFlowControlEnable_Type(EnableVar):defaultValue=2
_RcPortFlowControlEnable_Type.__name__=_G
_RcPortFlowControlEnable_Object=MibTableColumn
rcPortFlowControlEnable=_RcPortFlowControlEnable_Object((1,3,6,1,4,1,8886,6,1,1,4,1,1,9),_RcPortFlowControlEnable_Type())
rcPortFlowControlEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:rcPortFlowControlEnable.setStatus(_E)
class _RcPortMacLearningEnable_Type(EnableVar):defaultValue=1
_RcPortMacLearningEnable_Type.__name__=_G
_RcPortMacLearningEnable_Object=MibTableColumn
rcPortMacLearningEnable=_RcPortMacLearningEnable_Object((1,3,6,1,4,1,8886,6,1,1,4,1,1,10),_RcPortMacLearningEnable_Type())
rcPortMacLearningEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:rcPortMacLearningEnable.setStatus(_E)
class _RcPortMacThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_RcPortMacThreshold_Type.__name__=_D
_RcPortMacThreshold_Object=MibTableColumn
rcPortMacThreshold=_RcPortMacThreshold_Object((1,3,6,1,4,1,8886,6,1,1,4,1,1,11),_RcPortMacThreshold_Type())
rcPortMacThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:rcPortMacThreshold.setStatus(_E)
class _RcPortStormControlBcastEnable_Type(EnableVar):defaultValue=2
_RcPortStormControlBcastEnable_Type.__name__=_G
_RcPortStormControlBcastEnable_Object=MibTableColumn
rcPortStormControlBcastEnable=_RcPortStormControlBcastEnable_Object((1,3,6,1,4,1,8886,6,1,1,4,1,1,12),_RcPortStormControlBcastEnable_Type())
rcPortStormControlBcastEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:rcPortStormControlBcastEnable.setStatus(_E)
class _RcPortStormControlMcastEnable_Type(EnableVar):defaultValue=2
_RcPortStormControlMcastEnable_Type.__name__=_G
_RcPortStormControlMcastEnable_Object=MibTableColumn
rcPortStormControlMcastEnable=_RcPortStormControlMcastEnable_Object((1,3,6,1,4,1,8886,6,1,1,4,1,1,13),_RcPortStormControlMcastEnable_Type())
rcPortStormControlMcastEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:rcPortStormControlMcastEnable.setStatus(_E)
class _RcPortStormControlDlfEnable_Type(EnableVar):defaultValue=2
_RcPortStormControlDlfEnable_Type.__name__=_G
_RcPortStormControlDlfEnable_Object=MibTableColumn
rcPortStormControlDlfEnable=_RcPortStormControlDlfEnable_Object((1,3,6,1,4,1,8886,6,1,1,4,1,1,14),_RcPortStormControlDlfEnable_Type())
rcPortStormControlDlfEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:rcPortStormControlDlfEnable.setStatus(_E)
class _RcPortStormControlBurst_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,512))
_RcPortStormControlBurst_Type.__name__=_D
_RcPortStormControlBurst_Object=MibTableColumn
rcPortStormControlBurst=_RcPortStormControlBurst_Object((1,3,6,1,4,1,8886,6,1,1,4,1,1,15),_RcPortStormControlBurst_Type())
rcPortStormControlBurst.setMaxAccess(_B)
if mibBuilder.loadTexts:rcPortStormControlBurst.setStatus(_E)
if mibBuilder.loadTexts:rcPortStormControlBurst.setUnits('kB')
class _RcPortStormControlLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2621430))
_RcPortStormControlLimit_Type.__name__=_D
_RcPortStormControlLimit_Object=MibTableColumn
rcPortStormControlLimit=_RcPortStormControlLimit_Object((1,3,6,1,4,1,8886,6,1,1,4,1,1,16),_RcPortStormControlLimit_Type())
rcPortStormControlLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:rcPortStormControlLimit.setStatus(_E)
if mibBuilder.loadTexts:rcPortStormControlLimit.setUnits('pps')
class _RcPortStormControlLimitRatio_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_RcPortStormControlLimitRatio_Type.__name__=_D
_RcPortStormControlLimitRatio_Object=MibTableColumn
rcPortStormControlLimitRatio=_RcPortStormControlLimitRatio_Object((1,3,6,1,4,1,8886,6,1,1,4,1,1,17),_RcPortStormControlLimitRatio_Type())
rcPortStormControlLimitRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:rcPortStormControlLimitRatio.setStatus(_E)
if mibBuilder.loadTexts:rcPortStormControlLimitRatio.setUnits(_X)
class _RcPortDefaultPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_RcPortDefaultPriority_Type.__name__=_D
_RcPortDefaultPriority_Object=MibTableColumn
rcPortDefaultPriority=_RcPortDefaultPriority_Object((1,3,6,1,4,1,8886,6,1,1,4,1,1,18),_RcPortDefaultPriority_Type())
rcPortDefaultPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:rcPortDefaultPriority.setStatus(_E)
_RcPortLoopbackDetectEnable_Type=EnableVar
_RcPortLoopbackDetectEnable_Object=MibTableColumn
rcPortLoopbackDetectEnable=_RcPortLoopbackDetectEnable_Object((1,3,6,1,4,1,8886,6,1,1,4,1,1,19),_RcPortLoopbackDetectEnable_Type())
rcPortLoopbackDetectEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:rcPortLoopbackDetectEnable.setStatus(_A)
_RcPortLoopbackDetectSrcPort_Type=Integer32
_RcPortLoopbackDetectSrcPort_Object=MibTableColumn
rcPortLoopbackDetectSrcPort=_RcPortLoopbackDetectSrcPort_Object((1,3,6,1,4,1,8886,6,1,1,4,1,1,20),_RcPortLoopbackDetectSrcPort_Type())
rcPortLoopbackDetectSrcPort.setMaxAccess(_C)
if mibBuilder.loadTexts:rcPortLoopbackDetectSrcPort.setStatus(_A)
class _RcPortProtected_Type(EnableVar):defaultValue=2
_RcPortProtected_Type.__name__=_G
_RcPortProtected_Object=MibTableColumn
rcPortProtected=_RcPortProtected_Object((1,3,6,1,4,1,8886,6,1,1,4,1,1,21),_RcPortProtected_Type())
rcPortProtected.setMaxAccess(_B)
if mibBuilder.loadTexts:rcPortProtected.setStatus(_E)
class _RcPortFlowControlRecvEnable_Type(EnableVar):defaultValue=2
_RcPortFlowControlRecvEnable_Type.__name__=_G
_RcPortFlowControlRecvEnable_Object=MibTableColumn
rcPortFlowControlRecvEnable=_RcPortFlowControlRecvEnable_Object((1,3,6,1,4,1,8886,6,1,1,4,1,1,22),_RcPortFlowControlRecvEnable_Type())
rcPortFlowControlRecvEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:rcPortFlowControlRecvEnable.setStatus(_E)
class _RcPortFlowControlSendEnable_Type(EnableVar):defaultValue=2
_RcPortFlowControlSendEnable_Type.__name__=_G
_RcPortFlowControlSendEnable_Object=MibTableColumn
rcPortFlowControlSendEnable=_RcPortFlowControlSendEnable_Object((1,3,6,1,4,1,8886,6,1,1,4,1,1,23),_RcPortFlowControlSendEnable_Type())
rcPortFlowControlSendEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:rcPortFlowControlSendEnable.setStatus(_E)
class _RcPortFlowControlRecvStatus_Type(EnableVar):defaultValue=2
_RcPortFlowControlRecvStatus_Type.__name__=_G
_RcPortFlowControlRecvStatus_Object=MibTableColumn
rcPortFlowControlRecvStatus=_RcPortFlowControlRecvStatus_Object((1,3,6,1,4,1,8886,6,1,1,4,1,1,24),_RcPortFlowControlRecvStatus_Type())
rcPortFlowControlRecvStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rcPortFlowControlRecvStatus.setStatus(_E)
class _RcPortFlowControlSendStatus_Type(EnableVar):defaultValue=2
_RcPortFlowControlSendStatus_Type.__name__=_G
_RcPortFlowControlSendStatus_Object=MibTableColumn
rcPortFlowControlSendStatus=_RcPortFlowControlSendStatus_Object((1,3,6,1,4,1,8886,6,1,1,4,1,1,25),_RcPortFlowControlSendStatus_Type())
rcPortFlowControlSendStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rcPortFlowControlSendStatus.setStatus(_E)
class _RcPortLoopbackDetectDownTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RcPortLoopbackDetectDownTime_Type.__name__=_D
_RcPortLoopbackDetectDownTime_Object=MibTableColumn
rcPortLoopbackDetectDownTime=_RcPortLoopbackDetectDownTime_Object((1,3,6,1,4,1,8886,6,1,1,4,1,1,26),_RcPortLoopbackDetectDownTime_Type())
rcPortLoopbackDetectDownTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rcPortLoopbackDetectDownTime.setStatus(_E)
class _RcPortMediaAttachType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_f,1),('fiber',2),('card',3),('sfp',4),('combo-sfp',5),('combo-copper',6)))
_RcPortMediaAttachType_Type.__name__=_D
_RcPortMediaAttachType_Object=MibTableColumn
rcPortMediaAttachType=_RcPortMediaAttachType_Object((1,3,6,1,4,1,8886,6,1,1,4,1,1,27),_RcPortMediaAttachType_Type())
rcPortMediaAttachType.setMaxAccess(_C)
if mibBuilder.loadTexts:rcPortMediaAttachType.setStatus(_A)
class _RcPortMediaAttachCapability_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_I,0),(_g,1),(_h,2),(_i,3),(_j,4),('unlimited',5)))
_RcPortMediaAttachCapability_Type.__name__=_D
_RcPortMediaAttachCapability_Object=MibTableColumn
rcPortMediaAttachCapability=_RcPortMediaAttachCapability_Object((1,3,6,1,4,1,8886,6,1,1,4,1,1,28),_RcPortMediaAttachCapability_Type())
rcPortMediaAttachCapability.setMaxAccess(_C)
if mibBuilder.loadTexts:rcPortMediaAttachCapability.setStatus(_A)
class _RcPortMDIXMode_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_k,1),('xover',2),('auto',3)))
_RcPortMDIXMode_Type.__name__=_D
_RcPortMDIXMode_Object=MibTableColumn
rcPortMDIXMode=_RcPortMDIXMode_Object((1,3,6,1,4,1,8886,6,1,1,4,1,1,29),_RcPortMDIXMode_Type())
rcPortMDIXMode.setMaxAccess(_B)
if mibBuilder.loadTexts:rcPortMDIXMode.setStatus(_A)
class _RcPortMDIXStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_k,1),('xover',2)))
_RcPortMDIXStatus_Type.__name__=_D
_RcPortMDIXStatus_Object=MibTableColumn
rcPortMDIXStatus=_RcPortMDIXStatus_Object((1,3,6,1,4,1,8886,6,1,1,4,1,1,30),_RcPortMDIXStatus_Type())
rcPortMDIXStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcPortMDIXStatus.setStatus(_A)
_RcportDiscPKts_Type=Counter32
_RcportDiscPKts_Object=MibTableColumn
rcportDiscPKts=_RcportDiscPKts_Object((1,3,6,1,4,1,8886,6,1,1,4,1,1,31),_RcportDiscPKts_Type())
rcportDiscPKts.setMaxAccess(_C)
if mibBuilder.loadTexts:rcportDiscPKts.setStatus(_A)
class _RcPortMacThresholdVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_RcPortMacThresholdVlan_Type.__name__=_D
_RcPortMacThresholdVlan_Object=MibTableColumn
rcPortMacThresholdVlan=_RcPortMacThresholdVlan_Object((1,3,6,1,4,1,8886,6,1,1,4,1,1,32),_RcPortMacThresholdVlan_Type())
rcPortMacThresholdVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:rcPortMacThresholdVlan.setStatus(_E)
_RcComboPortTable_Object=MibTable
rcComboPortTable=_RcComboPortTable_Object((1,3,6,1,4,1,8886,6,1,1,4,2))
if mibBuilder.loadTexts:rcComboPortTable.setStatus(_A)
_RcComboPortEntry_Object=MibTableRow
rcComboPortEntry=_RcComboPortEntry_Object((1,3,6,1,4,1,8886,6,1,1,4,2,1))
rcComboPortEntry.setIndexNames((0,_F,_l),(0,_F,_m))
if mibBuilder.loadTexts:rcComboPortEntry.setStatus(_A)
_RcComboIndex_Type=Integer32
_RcComboIndex_Object=MibTableColumn
rcComboIndex=_RcComboIndex_Object((1,3,6,1,4,1,8886,6,1,1,4,2,1,1),_RcComboIndex_Type())
rcComboIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:rcComboIndex.setStatus(_A)
_RcComboPortIndex_Type=Integer32
_RcComboPortIndex_Object=MibTableColumn
rcComboPortIndex=_RcComboPortIndex_Object((1,3,6,1,4,1,8886,6,1,1,4,2,1,2),_RcComboPortIndex_Type())
rcComboPortIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:rcComboPortIndex.setStatus(_A)
class _RcComboPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_I,0),(_L,1),(_M,2),(_N,3),(_O,4),(_P,5),(_Q,6)))
_RcComboPortType_Type.__name__=_D
_RcComboPortType_Object=MibTableColumn
rcComboPortType=_RcComboPortType_Object((1,3,6,1,4,1,8886,6,1,1,4,2,1,3),_RcComboPortType_Type())
rcComboPortType.setMaxAccess(_C)
if mibBuilder.loadTexts:rcComboPortType.setStatus(_A)
class _RcComboPortMediaAttachType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('sfp',1),(_f,2)))
_RcComboPortMediaAttachType_Type.__name__=_D
_RcComboPortMediaAttachType_Object=MibTableColumn
rcComboPortMediaAttachType=_RcComboPortMediaAttachType_Object((1,3,6,1,4,1,8886,6,1,1,4,2,1,4),_RcComboPortMediaAttachType_Type())
rcComboPortMediaAttachType.setMaxAccess(_C)
if mibBuilder.loadTexts:rcComboPortMediaAttachType.setStatus(_A)
class _RcComboPortActiveStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('inactive',2)))
_RcComboPortActiveStatus_Type.__name__=_D
_RcComboPortActiveStatus_Object=MibTableColumn
rcComboPortActiveStatus=_RcComboPortActiveStatus_Object((1,3,6,1,4,1,8886,6,1,1,4,2,1,5),_RcComboPortActiveStatus_Type())
rcComboPortActiveStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rcComboPortActiveStatus.setStatus(_A)
class _RcComboPortMediaAttachCapability_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_I,0),(_g,1),(_h,2),(_i,3),(_j,4)))
_RcComboPortMediaAttachCapability_Type.__name__=_D
_RcComboPortMediaAttachCapability_Object=MibTableColumn
rcComboPortMediaAttachCapability=_RcComboPortMediaAttachCapability_Object((1,3,6,1,4,1,8886,6,1,1,4,2,1,6),_RcComboPortMediaAttachCapability_Type())
rcComboPortMediaAttachCapability.setMaxAccess(_C)
if mibBuilder.loadTexts:rcComboPortMediaAttachCapability.setStatus(_A)
_RcLoopbackTrap_ObjectIdentity=ObjectIdentity
rcLoopbackTrap=_RcLoopbackTrap_ObjectIdentity((1,3,6,1,4,1,8886,6,1,1,5))
_RcPorConnectorChangeTrap_ObjectIdentity=ObjectIdentity
rcPorConnectorChangeTrap=_RcPorConnectorChangeTrap_ObjectIdentity((1,3,6,1,4,1,8886,6,1,1,6))
_RcMacMoveTrap_ObjectIdentity=ObjectIdentity
rcMacMoveTrap=_RcMacMoveTrap_ObjectIdentity((1,3,6,1,4,1,8886,6,1,1,8))
rcLoopbackLinkUpTrap=NotificationType((1,3,6,1,4,1,8886,6,1,1,5,1))
rcLoopbackLinkUpTrap.setObjects((_F,_H))
if mibBuilder.loadTexts:rcLoopbackLinkUpTrap.setStatus(_A)
rcLoopbackLinkDownTrap=NotificationType((1,3,6,1,4,1,8886,6,1,1,5,2))
rcLoopbackLinkDownTrap.setObjects(*((_F,_H),(_F,_n),(_F,_o)))
if mibBuilder.loadTexts:rcLoopbackLinkDownTrap.setStatus(_A)
rcPortConnectorInsertTrap=NotificationType((1,3,6,1,4,1,8886,6,1,1,6,1))
rcPortConnectorInsertTrap.setObjects(*((_F,_H),(_F,_S),(_F,_T),(_F,_U)))
if mibBuilder.loadTexts:rcPortConnectorInsertTrap.setStatus(_A)
rcPortConnectorRemoveTrap=NotificationType((1,3,6,1,4,1,8886,6,1,1,6,2))
rcPortConnectorRemoveTrap.setObjects(*((_F,_H),(_F,_S),(_F,_T),(_F,_U)))
if mibBuilder.loadTexts:rcPortConnectorRemoveTrap.setStatus(_A)
rcMacMoveVioTrap=NotificationType((1,3,6,1,4,1,8886,6,1,1,8,1))
rcMacMoveVioTrap.setObjects(*((_F,_p),(_F,_q),(_F,_r)))
if mibBuilder.loadTexts:rcMacMoveVioTrap.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'rcSystem':rcSystem,'rcSwitchInformation':rcSwitchInformation,'rcSwitchRoseVersion':rcSwitchRoseVersion,'rcSwitchHardwareVersion':rcSwitchHardwareVersion,'rcSwitchServiceInfo':rcSwitchServiceInfo,'rcSwitchLastErrorCode':rcSwitchLastErrorCode,'rcSwitchMaxPhysicalPortNum':rcSwitchMaxPhysicalPortNum,'rcSwitchMaxAggregationPortNum':rcSwitchMaxAggregationPortNum,'rcSwitchMaxL3IpSubnetNum':rcSwitchMaxL3IpSubnetNum,'rcSwitchMacTableCapability':rcSwitchMacTableCapability,'rcSwitchMacAddress':rcSwitchMacAddress,'rcSwitchVlanSpaceSize':rcSwitchVlanSpaceSize,'rcSwitchPvidSpaceSize':rcSwitchPvidSpaceSize,'rcSwitchDefaultVlan':rcSwitchDefaultVlan,'rcSwitchBootstrapVersion':rcSwitchBootstrapVersion,'rcSwitchSerialNumber':rcSwitchSerialNumber,'rcSwitchFpgaVersion':rcSwitchFpgaVersion,'rcSwitchProductVersion':rcSwitchProductVersion,'rcSwitchCmpAbName':rcSwitchCmpAbName,'rcSwitchCmpFullName':rcSwitchCmpFullName,'rcSwitchDeviceName':rcSwitchDeviceName,'rcSlotInformation':rcSlotInformation,'rcSlotNum':rcSlotNum,'rcSlotStateTable':rcSlotStateTable,'rcSlotStateEntry':rcSlotStateEntry,_V:rcSlotIndex,'rcSlotPortStart':rcSlotPortStart,'rcSlotPortNum':rcSlotPortNum,'rcSlotType':rcSlotType,'rcSwitchConfig':rcSwitchConfig,'rcMacAgingTime':rcMacAgingTime,'rcStormControlBcastEnable':rcStormControlBcastEnable,'rcStormControlMcastEnable':rcStormControlMcastEnable,'rcStormControlDlfEnable':rcStormControlDlfEnable,'rcStormControlpps':rcStormControlpps,'rcStormControlbps':rcStormControlbps,'rcStormControlRatio':rcStormControlRatio,'rcStormControlBurst':rcStormControlBurst,'rcStpEnable':rcStpEnable,'rcSvlEnable':rcSvlEnable,'rcGarpEnable':rcGarpEnable,'rcLacpEnable':rcLacpEnable,'rcVlanSpaceNum':rcVlanSpaceNum,'rcPvidSpaceNum':rcPvidSpaceNum,'rcLoopbackDetectInterval':rcLoopbackDetectInterval,'rcArpAgingTime':rcArpAgingTime,'rcBpduTransPorts':rcBpduTransPorts,'rcDot1xTransPorts':rcDot1xTransPorts,'rcLacpTransPorts':rcLacpTransPorts,'rcGarpTransPorts':rcGarpTransPorts,'rcGmrpTransPorts':rcGmrpTransPorts,'rcGvrpTransPorts':rcGvrpTransPorts,'rcIpRouting':rcIpRouting,'rcStaticRouteDistance':rcStaticRouteDistance,'rcFastRoute':rcFastRoute,'rcDlfForwardingEnable':rcDlfForwardingEnable,'rcLoopbackDetectVlan':rcLoopbackDetectVlan,'rcLoopbackDetectDestAddr':rcLoopbackDetectDestAddr,'rcMaxAllowedFrameLength':rcMaxAllowedFrameLength,'rcSvlDefaultVlan':rcSvlDefaultVlan,'rcTelnetMaxSessions':rcTelnetMaxSessions,'rcTelnetAcceptPorts':rcTelnetAcceptPorts,'rcVlanMacLearning':rcVlanMacLearning,'rcConsoleEnable':rcConsoleEnable,'rcMacTrapEnable':rcMacTrapEnable,'rcMacMoveEnable':rcMacMoveEnable,_p:rcMacMoveLastPortIndex,_q:rcMacMoveLastMacaddress,_r:rcMacMoveLastVlan,'rcPortInfoConfig':rcPortInfoConfig,'rcPortTable':rcPortTable,'rcPortEntry':rcPortEntry,_H:rcPortIndex,_S:rcPortType,'rcSlotTableIndex':rcSlotTableIndex,'rcSlotPortIndex':rcSlotPortIndex,'rcPortAdminStatus':rcPortAdminStatus,'rcPortOperStatus':rcPortOperStatus,'rcPortDuplexSpeedSet':rcPortDuplexSpeedSet,'rcPortDuplexSpeedGet':rcPortDuplexSpeedGet,'rcPortFlowControlEnable':rcPortFlowControlEnable,'rcPortMacLearningEnable':rcPortMacLearningEnable,'rcPortMacThreshold':rcPortMacThreshold,'rcPortStormControlBcastEnable':rcPortStormControlBcastEnable,'rcPortStormControlMcastEnable':rcPortStormControlMcastEnable,'rcPortStormControlDlfEnable':rcPortStormControlDlfEnable,'rcPortStormControlBurst':rcPortStormControlBurst,'rcPortStormControlLimit':rcPortStormControlLimit,'rcPortStormControlLimitRatio':rcPortStormControlLimitRatio,'rcPortDefaultPriority':rcPortDefaultPriority,'rcPortLoopbackDetectEnable':rcPortLoopbackDetectEnable,_n:rcPortLoopbackDetectSrcPort,'rcPortProtected':rcPortProtected,'rcPortFlowControlRecvEnable':rcPortFlowControlRecvEnable,'rcPortFlowControlSendEnable':rcPortFlowControlSendEnable,'rcPortFlowControlRecvStatus':rcPortFlowControlRecvStatus,'rcPortFlowControlSendStatus':rcPortFlowControlSendStatus,_o:rcPortLoopbackDetectDownTime,_T:rcPortMediaAttachType,_U:rcPortMediaAttachCapability,'rcPortMDIXMode':rcPortMDIXMode,'rcPortMDIXStatus':rcPortMDIXStatus,'rcportDiscPKts':rcportDiscPKts,'rcPortMacThresholdVlan':rcPortMacThresholdVlan,'rcComboPortTable':rcComboPortTable,'rcComboPortEntry':rcComboPortEntry,_l:rcComboIndex,_m:rcComboPortIndex,'rcComboPortType':rcComboPortType,'rcComboPortMediaAttachType':rcComboPortMediaAttachType,'rcComboPortActiveStatus':rcComboPortActiveStatus,'rcComboPortMediaAttachCapability':rcComboPortMediaAttachCapability,'rcLoopbackTrap':rcLoopbackTrap,'rcLoopbackLinkUpTrap':rcLoopbackLinkUpTrap,'rcLoopbackLinkDownTrap':rcLoopbackLinkDownTrap,'rcPorConnectorChangeTrap':rcPorConnectorChangeTrap,'rcPortConnectorInsertTrap':rcPortConnectorInsertTrap,'rcPortConnectorRemoveTrap':rcPortConnectorRemoveTrap,'rcMacMoveTrap':rcMacMoveTrap,'rcMacMoveVioTrap':rcMacMoveVioTrap})