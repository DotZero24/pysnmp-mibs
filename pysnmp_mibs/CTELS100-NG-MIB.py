_L='els100SwitchPriorityPortId'
_K='els100SwitchVlanPortId'
_J='els100SwitchVlanId'
_I='els100Port'
_H='CTELS100-NG-MIB'
_G='DisplayString'
_F='read-only'
_E='enable'
_D='disable'
_C='Integer32'
_B='read-write'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso,mgmt=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso','mgmt')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','TextualConvention')
_Mib_2_ObjectIdentity=ObjectIdentity
mib_2=_Mib_2_ObjectIdentity((1,3,6,1,2,1))
_Cabletron_ObjectIdentity=ObjectIdentity
cabletron=_Cabletron_ObjectIdentity((1,3,6,1,4,1,52))
_Els100_ObjectIdentity=ObjectIdentity
els100=_Els100_ObjectIdentity((1,3,6,1,4,1,52,1011))
_Els100SystemConfig_ObjectIdentity=ObjectIdentity
els100SystemConfig=_Els100SystemConfig_ObjectIdentity((1,3,6,1,4,1,52,1011,1))
class _Els100SysSerialno_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Els100SysSerialno_Type.__name__=_G
_Els100SysSerialno_Object=MibScalar
els100SysSerialno=_Els100SysSerialno_Object((1,3,6,1,4,1,52,1011,1,1),_Els100SysSerialno_Type())
els100SysSerialno.setMaxAccess(_F)
if mibBuilder.loadTexts:els100SysSerialno.setStatus(_A)
_Els100SysTftpIPAddress_Type=IpAddress
_Els100SysTftpIPAddress_Object=MibScalar
els100SysTftpIPAddress=_Els100SysTftpIPAddress_Object((1,3,6,1,4,1,52,1011,1,2),_Els100SysTftpIPAddress_Type())
els100SysTftpIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:els100SysTftpIPAddress.setStatus(_A)
class _Els100SysTftpFilename_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Els100SysTftpFilename_Type.__name__=_G
_Els100SysTftpFilename_Object=MibScalar
els100SysTftpFilename=_Els100SysTftpFilename_Object((1,3,6,1,4,1,52,1011,1,3),_Els100SysTftpFilename_Type())
els100SysTftpFilename.setMaxAccess(_B)
if mibBuilder.loadTexts:els100SysTftpFilename.setStatus(_A)
_Els100SysPowerupCount_Type=Integer32
_Els100SysPowerupCount_Object=MibScalar
els100SysPowerupCount=_Els100SysPowerupCount_Object((1,3,6,1,4,1,52,1011,1,4),_Els100SysPowerupCount_Type())
els100SysPowerupCount.setMaxAccess(_F)
if mibBuilder.loadTexts:els100SysPowerupCount.setStatus(_A)
_Els100SysBrcastCutoffRate_Type=Integer32
_Els100SysBrcastCutoffRate_Object=MibScalar
els100SysBrcastCutoffRate=_Els100SysBrcastCutoffRate_Object((1,3,6,1,4,1,52,1011,1,5),_Els100SysBrcastCutoffRate_Type())
els100SysBrcastCutoffRate.setMaxAccess(_B)
if mibBuilder.loadTexts:els100SysBrcastCutoffRate.setStatus(_A)
_Els100SysGatewayIPAddress_Type=IpAddress
_Els100SysGatewayIPAddress_Object=MibScalar
els100SysGatewayIPAddress=_Els100SysGatewayIPAddress_Object((1,3,6,1,4,1,52,1011,1,6),_Els100SysGatewayIPAddress_Type())
els100SysGatewayIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:els100SysGatewayIPAddress.setStatus(_A)
class _Els100SysTftpStartDownload_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('download',1),('noDownload',2)))
_Els100SysTftpStartDownload_Type.__name__=_C
_Els100SysTftpStartDownload_Object=MibScalar
els100SysTftpStartDownload=_Els100SysTftpStartDownload_Object((1,3,6,1,4,1,52,1011,1,7),_Els100SysTftpStartDownload_Type())
els100SysTftpStartDownload.setMaxAccess(_B)
if mibBuilder.loadTexts:els100SysTftpStartDownload.setStatus(_A)
class _Els100SysBootPDhcpEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_Els100SysBootPDhcpEnable_Type.__name__=_C
_Els100SysBootPDhcpEnable_Object=MibScalar
els100SysBootPDhcpEnable=_Els100SysBootPDhcpEnable_Object((1,3,6,1,4,1,52,1011,1,8),_Els100SysBootPDhcpEnable_Type())
els100SysBootPDhcpEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:els100SysBootPDhcpEnable.setStatus(_A)
class _Els100SysReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noReset',1),('reset',2)))
_Els100SysReset_Type.__name__=_C
_Els100SysReset_Object=MibScalar
els100SysReset=_Els100SysReset_Object((1,3,6,1,4,1,52,1011,1,10),_Els100SysReset_Type())
els100SysReset.setMaxAccess(_B)
if mibBuilder.loadTexts:els100SysReset.setStatus(_A)
_Els100SysSyslogServer_Type=IpAddress
_Els100SysSyslogServer_Object=MibScalar
els100SysSyslogServer=_Els100SysSyslogServer_Object((1,3,6,1,4,1,52,1011,1,11),_Els100SysSyslogServer_Type())
els100SysSyslogServer.setMaxAccess(_B)
if mibBuilder.loadTexts:els100SysSyslogServer.setStatus(_A)
class _Els100SysLowestSyslogSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('emergency',0),('alert',1),('critical',2),('error',3),('warning',4),('notice',5),('info',6),('debug',7)))
_Els100SysLowestSyslogSeverity_Type.__name__=_C
_Els100SysLowestSyslogSeverity_Object=MibScalar
els100SysLowestSyslogSeverity=_Els100SysLowestSyslogSeverity_Object((1,3,6,1,4,1,52,1011,1,12),_Els100SysLowestSyslogSeverity_Type())
els100SysLowestSyslogSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:els100SysLowestSyslogSeverity.setStatus(_A)
class _Els100SysComPortEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disabled',1),('enabled',2)))
_Els100SysComPortEnable_Type.__name__=_C
_Els100SysComPortEnable_Object=MibScalar
els100SysComPortEnable=_Els100SysComPortEnable_Object((1,3,6,1,4,1,52,1011,1,13),_Els100SysComPortEnable_Type())
els100SysComPortEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:els100SysComPortEnable.setStatus(_A)
_Els100SysBoardID_Type=Integer32
_Els100SysBoardID_Object=MibScalar
els100SysBoardID=_Els100SysBoardID_Object((1,3,6,1,4,1,52,1011,1,14),_Els100SysBoardID_Type())
els100SysBoardID.setMaxAccess(_F)
if mibBuilder.loadTexts:els100SysBoardID.setStatus(_A)
_Els100PortTable_Object=MibTable
els100PortTable=_Els100PortTable_Object((1,3,6,1,4,1,52,1011,2))
if mibBuilder.loadTexts:els100PortTable.setStatus(_A)
_Els100PortEntry_Object=MibTableRow
els100PortEntry=_Els100PortEntry_Object((1,3,6,1,4,1,52,1011,2,1))
els100PortEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:els100PortEntry.setStatus(_A)
_Els100Port_Type=Integer32
_Els100Port_Object=MibTableColumn
els100Port=_Els100Port_Object((1,3,6,1,4,1,52,1011,2,1,1),_Els100Port_Type())
els100Port.setMaxAccess(_F)
if mibBuilder.loadTexts:els100Port.setStatus(_A)
class _Els100PortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_Els100PortStatus_Type.__name__=_C
_Els100PortStatus_Object=MibTableColumn
els100PortStatus=_Els100PortStatus_Object((1,3,6,1,4,1,52,1011,2,1,2),_Els100PortStatus_Type())
els100PortStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:els100PortStatus.setStatus(_A)
class _Els100PortDuplexStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('half',1),('full',2)))
_Els100PortDuplexStatus_Type.__name__=_C
_Els100PortDuplexStatus_Object=MibTableColumn
els100PortDuplexStatus=_Els100PortDuplexStatus_Object((1,3,6,1,4,1,52,1011,2,1,3),_Els100PortDuplexStatus_Type())
els100PortDuplexStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:els100PortDuplexStatus.setStatus(_A)
_Els100PortForwardedFrames_Type=Counter32
_Els100PortForwardedFrames_Object=MibTableColumn
els100PortForwardedFrames=_Els100PortForwardedFrames_Object((1,3,6,1,4,1,52,1011,2,1,4),_Els100PortForwardedFrames_Type())
els100PortForwardedFrames.setMaxAccess(_F)
if mibBuilder.loadTexts:els100PortForwardedFrames.setStatus(_A)
_Els100PortRcvdLocalFrames_Type=Counter32
_Els100PortRcvdLocalFrames_Object=MibTableColumn
els100PortRcvdLocalFrames=_Els100PortRcvdLocalFrames_Object((1,3,6,1,4,1,52,1011,2,1,5),_Els100PortRcvdLocalFrames_Type())
els100PortRcvdLocalFrames.setMaxAccess(_F)
if mibBuilder.loadTexts:els100PortRcvdLocalFrames.setStatus(_A)
class _Els100PortName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,60))
_Els100PortName_Type.__name__=_G
_Els100PortName_Object=MibTableColumn
els100PortName=_Els100PortName_Object((1,3,6,1,4,1,52,1011,2,1,6),_Els100PortName_Type())
els100PortName.setMaxAccess(_B)
if mibBuilder.loadTexts:els100PortName.setStatus(_A)
class _Els100PortEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_Els100PortEnable_Type.__name__=_C
_Els100PortEnable_Object=MibTableColumn
els100PortEnable=_Els100PortEnable_Object((1,3,6,1,4,1,52,1011,2,1,7),_Els100PortEnable_Type())
els100PortEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:els100PortEnable.setStatus(_A)
class _Els100PortSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('tenMbps',1),('oneHundredMbps',2),('oneThousandMbps',3)))
_Els100PortSpeed_Type.__name__=_C
_Els100PortSpeed_Object=MibTableColumn
els100PortSpeed=_Els100PortSpeed_Object((1,3,6,1,4,1,52,1011,2,1,8),_Els100PortSpeed_Type())
els100PortSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:els100PortSpeed.setStatus(_A)
class _Els100PortAutonegEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_Els100PortAutonegEnable_Type.__name__=_C
_Els100PortAutonegEnable_Object=MibTableColumn
els100PortAutonegEnable=_Els100PortAutonegEnable_Object((1,3,6,1,4,1,52,1011,2,1,9),_Els100PortAutonegEnable_Type())
els100PortAutonegEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:els100PortAutonegEnable.setStatus(_A)
class _Els100PortFlowControlEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_Els100PortFlowControlEnable_Type.__name__=_C
_Els100PortFlowControlEnable_Object=MibTableColumn
els100PortFlowControlEnable=_Els100PortFlowControlEnable_Object((1,3,6,1,4,1,52,1011,2,1,10),_Els100PortFlowControlEnable_Type())
els100PortFlowControlEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:els100PortFlowControlEnable.setStatus(_A)
class _Els100PortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('unknown',1),('ieee10BaseT',2),('ieee100BaseTx',3),('ieee100BaseFx-MM',4),('ieee100BaseFx-SM',5),('ieee1000BaseCx',6),('ieee1000BaseLx',7),('ieee1000BaseSx',8),('ieee1000BaseT',9),('ieee1000BaseX',10)))
_Els100PortType_Type.__name__=_C
_Els100PortType_Object=MibTableColumn
els100PortType=_Els100PortType_Object((1,3,6,1,4,1,52,1011,2,1,11),_Els100PortType_Type())
els100PortType.setMaxAccess(_F)
if mibBuilder.loadTexts:els100PortType.setStatus(_A)
_Els100Switch_ObjectIdentity=ObjectIdentity
els100Switch=_Els100Switch_ObjectIdentity((1,3,6,1,4,1,52,1011,3))
_Els100SwitchIPAddress_Type=IpAddress
_Els100SwitchIPAddress_Object=MibScalar
els100SwitchIPAddress=_Els100SwitchIPAddress_Object((1,3,6,1,4,1,52,1011,3,1),_Els100SwitchIPAddress_Type())
els100SwitchIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:els100SwitchIPAddress.setStatus(_A)
_Els100SwitchSubnetMask_Type=IpAddress
_Els100SwitchSubnetMask_Object=MibScalar
els100SwitchSubnetMask=_Els100SwitchSubnetMask_Object((1,3,6,1,4,1,52,1011,3,2),_Els100SwitchSubnetMask_Type())
els100SwitchSubnetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:els100SwitchSubnetMask.setStatus(_A)
_Els100ActiveAgingTime_Type=Integer32
_Els100ActiveAgingTime_Object=MibScalar
els100ActiveAgingTime=_Els100ActiveAgingTime_Object((1,3,6,1,4,1,52,1011,3,3),_Els100ActiveAgingTime_Type())
els100ActiveAgingTime.setMaxAccess(_B)
if mibBuilder.loadTexts:els100ActiveAgingTime.setStatus(_A)
class _Els100SwitchSTPStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_Els100SwitchSTPStatus_Type.__name__=_C
_Els100SwitchSTPStatus_Object=MibScalar
els100SwitchSTPStatus=_Els100SwitchSTPStatus_Object((1,3,6,1,4,1,52,1011,3,5),_Els100SwitchSTPStatus_Type())
els100SwitchSTPStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:els100SwitchSTPStatus.setStatus(_A)
_Els100SwitchManager_ObjectIdentity=ObjectIdentity
els100SwitchManager=_Els100SwitchManager_ObjectIdentity((1,3,6,1,4,1,52,1011,3,6))
_Els100SwitchTrapRcvr1_Type=IpAddress
_Els100SwitchTrapRcvr1_Object=MibScalar
els100SwitchTrapRcvr1=_Els100SwitchTrapRcvr1_Object((1,3,6,1,4,1,52,1011,3,6,1),_Els100SwitchTrapRcvr1_Type())
els100SwitchTrapRcvr1.setMaxAccess(_B)
if mibBuilder.loadTexts:els100SwitchTrapRcvr1.setStatus(_A)
class _Els100SwitchTrapCommunity1_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,60))
_Els100SwitchTrapCommunity1_Type.__name__=_G
_Els100SwitchTrapCommunity1_Object=MibScalar
els100SwitchTrapCommunity1=_Els100SwitchTrapCommunity1_Object((1,3,6,1,4,1,52,1011,3,6,2),_Els100SwitchTrapCommunity1_Type())
els100SwitchTrapCommunity1.setMaxAccess(_B)
if mibBuilder.loadTexts:els100SwitchTrapCommunity1.setStatus(_A)
_Els100SwitchTrapRcvr2_Type=IpAddress
_Els100SwitchTrapRcvr2_Object=MibScalar
els100SwitchTrapRcvr2=_Els100SwitchTrapRcvr2_Object((1,3,6,1,4,1,52,1011,3,6,3),_Els100SwitchTrapRcvr2_Type())
els100SwitchTrapRcvr2.setMaxAccess(_B)
if mibBuilder.loadTexts:els100SwitchTrapRcvr2.setStatus(_A)
class _Els100SwitchTrapCommunity2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,60))
_Els100SwitchTrapCommunity2_Type.__name__=_G
_Els100SwitchTrapCommunity2_Object=MibScalar
els100SwitchTrapCommunity2=_Els100SwitchTrapCommunity2_Object((1,3,6,1,4,1,52,1011,3,6,4),_Els100SwitchTrapCommunity2_Type())
els100SwitchTrapCommunity2.setMaxAccess(_B)
if mibBuilder.loadTexts:els100SwitchTrapCommunity2.setStatus(_A)
_Els100SwitchTrapRcvr3_Type=IpAddress
_Els100SwitchTrapRcvr3_Object=MibScalar
els100SwitchTrapRcvr3=_Els100SwitchTrapRcvr3_Object((1,3,6,1,4,1,52,1011,3,6,5),_Els100SwitchTrapRcvr3_Type())
els100SwitchTrapRcvr3.setMaxAccess(_B)
if mibBuilder.loadTexts:els100SwitchTrapRcvr3.setStatus(_A)
class _Els100SwitchTrapCommunity3_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,60))
_Els100SwitchTrapCommunity3_Type.__name__=_G
_Els100SwitchTrapCommunity3_Object=MibScalar
els100SwitchTrapCommunity3=_Els100SwitchTrapCommunity3_Object((1,3,6,1,4,1,52,1011,3,6,6),_Els100SwitchTrapCommunity3_Type())
els100SwitchTrapCommunity3.setMaxAccess(_B)
if mibBuilder.loadTexts:els100SwitchTrapCommunity3.setStatus(_A)
_Els100SwitchTrapRcvr4_Type=IpAddress
_Els100SwitchTrapRcvr4_Object=MibScalar
els100SwitchTrapRcvr4=_Els100SwitchTrapRcvr4_Object((1,3,6,1,4,1,52,1011,3,6,7),_Els100SwitchTrapRcvr4_Type())
els100SwitchTrapRcvr4.setMaxAccess(_B)
if mibBuilder.loadTexts:els100SwitchTrapRcvr4.setStatus(_A)
class _Els100SwitchTrapCommunity4_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,60))
_Els100SwitchTrapCommunity4_Type.__name__=_G
_Els100SwitchTrapCommunity4_Object=MibScalar
els100SwitchTrapCommunity4=_Els100SwitchTrapCommunity4_Object((1,3,6,1,4,1,52,1011,3,6,8),_Els100SwitchTrapCommunity4_Type())
els100SwitchTrapCommunity4.setMaxAccess(_B)
if mibBuilder.loadTexts:els100SwitchTrapCommunity4.setStatus(_A)
class _Els100SwitchPortMirroringStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_Els100SwitchPortMirroringStatus_Type.__name__=_C
_Els100SwitchPortMirroringStatus_Object=MibScalar
els100SwitchPortMirroringStatus=_Els100SwitchPortMirroringStatus_Object((1,3,6,1,4,1,52,1011,3,7),_Els100SwitchPortMirroringStatus_Type())
els100SwitchPortMirroringStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:els100SwitchPortMirroringStatus.setStatus(_A)
_Els100SwitchMirroredPort_Type=Integer32
_Els100SwitchMirroredPort_Object=MibScalar
els100SwitchMirroredPort=_Els100SwitchMirroredPort_Object((1,3,6,1,4,1,52,1011,3,8),_Els100SwitchMirroredPort_Type())
els100SwitchMirroredPort.setMaxAccess(_B)
if mibBuilder.loadTexts:els100SwitchMirroredPort.setStatus(_A)
_Els100SwitchMirroringPort_Type=Integer32
_Els100SwitchMirroringPort_Object=MibScalar
els100SwitchMirroringPort=_Els100SwitchMirroringPort_Object((1,3,6,1,4,1,52,1011,3,9),_Els100SwitchMirroringPort_Type())
els100SwitchMirroringPort.setMaxAccess(_B)
if mibBuilder.loadTexts:els100SwitchMirroringPort.setStatus(_A)
class _Els100SwitchXmitMirrorEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_Els100SwitchXmitMirrorEnable_Type.__name__=_C
_Els100SwitchXmitMirrorEnable_Object=MibScalar
els100SwitchXmitMirrorEnable=_Els100SwitchXmitMirrorEnable_Object((1,3,6,1,4,1,52,1011,3,10),_Els100SwitchXmitMirrorEnable_Type())
els100SwitchXmitMirrorEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:els100SwitchXmitMirrorEnable.setStatus(_A)
class _Els100SwitchRcvMirrorEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_Els100SwitchRcvMirrorEnable_Type.__name__=_C
_Els100SwitchRcvMirrorEnable_Object=MibScalar
els100SwitchRcvMirrorEnable=_Els100SwitchRcvMirrorEnable_Object((1,3,6,1,4,1,52,1011,3,11),_Els100SwitchRcvMirrorEnable_Type())
els100SwitchRcvMirrorEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:els100SwitchRcvMirrorEnable.setStatus(_A)
class _Els100SwitchVlanEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_Els100SwitchVlanEnable_Type.__name__=_C
_Els100SwitchVlanEnable_Object=MibScalar
els100SwitchVlanEnable=_Els100SwitchVlanEnable_Object((1,3,6,1,4,1,52,1011,3,12),_Els100SwitchVlanEnable_Type())
els100SwitchVlanEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:els100SwitchVlanEnable.setStatus(_A)
_Els100SwitchVlanConfigTable_Object=MibTable
els100SwitchVlanConfigTable=_Els100SwitchVlanConfigTable_Object((1,3,6,1,4,1,52,1011,3,13))
if mibBuilder.loadTexts:els100SwitchVlanConfigTable.setStatus(_A)
_Els100SwitchVlanEntry_Object=MibTableRow
els100SwitchVlanEntry=_Els100SwitchVlanEntry_Object((1,3,6,1,4,1,52,1011,3,13,1))
els100SwitchVlanEntry.setIndexNames((0,_H,_J))
if mibBuilder.loadTexts:els100SwitchVlanEntry.setStatus(_A)
_Els100SwitchVlanId_Type=Integer32
_Els100SwitchVlanId_Object=MibTableColumn
els100SwitchVlanId=_Els100SwitchVlanId_Object((1,3,6,1,4,1,52,1011,3,13,1,1),_Els100SwitchVlanId_Type())
els100SwitchVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:els100SwitchVlanId.setStatus(_A)
class _Els100SwitchVlanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,60))
_Els100SwitchVlanName_Type.__name__=_G
_Els100SwitchVlanName_Object=MibTableColumn
els100SwitchVlanName=_Els100SwitchVlanName_Object((1,3,6,1,4,1,52,1011,3,13,1,2),_Els100SwitchVlanName_Type())
els100SwitchVlanName.setMaxAccess(_B)
if mibBuilder.loadTexts:els100SwitchVlanName.setStatus(_A)
_Els100SwitchVlanPorts_Type=OctetString
_Els100SwitchVlanPorts_Object=MibTableColumn
els100SwitchVlanPorts=_Els100SwitchVlanPorts_Object((1,3,6,1,4,1,52,1011,3,13,1,3),_Els100SwitchVlanPorts_Type())
els100SwitchVlanPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:els100SwitchVlanPorts.setStatus(_A)
_Els100SwitchVlanEgressPorts_Type=OctetString
_Els100SwitchVlanEgressPorts_Object=MibTableColumn
els100SwitchVlanEgressPorts=_Els100SwitchVlanEgressPorts_Object((1,3,6,1,4,1,52,1011,3,13,1,4),_Els100SwitchVlanEgressPorts_Type())
els100SwitchVlanEgressPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:els100SwitchVlanEgressPorts.setStatus(_A)
class _Els100SwitchVlanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_Els100SwitchVlanStatus_Type.__name__=_C
_Els100SwitchVlanStatus_Object=MibTableColumn
els100SwitchVlanStatus=_Els100SwitchVlanStatus_Object((1,3,6,1,4,1,52,1011,3,13,1,5),_Els100SwitchVlanStatus_Type())
els100SwitchVlanStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:els100SwitchVlanStatus.setStatus(_A)
_Els100SwitchVlanPortTable_Object=MibTable
els100SwitchVlanPortTable=_Els100SwitchVlanPortTable_Object((1,3,6,1,4,1,52,1011,3,14))
if mibBuilder.loadTexts:els100SwitchVlanPortTable.setStatus(_A)
_Els100SwitchVlanPortEntry_Object=MibTableRow
els100SwitchVlanPortEntry=_Els100SwitchVlanPortEntry_Object((1,3,6,1,4,1,52,1011,3,14,1))
els100SwitchVlanPortEntry.setIndexNames((0,_H,_K))
if mibBuilder.loadTexts:els100SwitchVlanPortEntry.setStatus(_A)
class _Els100SwitchVlanPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_Els100SwitchVlanPortId_Type.__name__=_C
_Els100SwitchVlanPortId_Object=MibTableColumn
els100SwitchVlanPortId=_Els100SwitchVlanPortId_Object((1,3,6,1,4,1,52,1011,3,14,1,1),_Els100SwitchVlanPortId_Type())
els100SwitchVlanPortId.setMaxAccess(_F)
if mibBuilder.loadTexts:els100SwitchVlanPortId.setStatus(_A)
class _Els100SwitchVlanPvid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Els100SwitchVlanPvid_Type.__name__=_C
_Els100SwitchVlanPvid_Object=MibTableColumn
els100SwitchVlanPvid=_Els100SwitchVlanPvid_Object((1,3,6,1,4,1,52,1011,3,14,1,2),_Els100SwitchVlanPvid_Type())
els100SwitchVlanPvid.setMaxAccess(_B)
if mibBuilder.loadTexts:els100SwitchVlanPvid.setStatus(_A)
class _Els100SwitchVlanPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('hybrid',1),('access',2)))
_Els100SwitchVlanPortType_Type.__name__=_C
_Els100SwitchVlanPortType_Object=MibTableColumn
els100SwitchVlanPortType=_Els100SwitchVlanPortType_Object((1,3,6,1,4,1,52,1011,3,14,1,3),_Els100SwitchVlanPortType_Type())
els100SwitchVlanPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:els100SwitchVlanPortType.setStatus(_A)
class _Els100SwitchPriorityEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_Els100SwitchPriorityEnable_Type.__name__=_C
_Els100SwitchPriorityEnable_Object=MibScalar
els100SwitchPriorityEnable=_Els100SwitchPriorityEnable_Object((1,3,6,1,4,1,52,1011,3,15),_Els100SwitchPriorityEnable_Type())
els100SwitchPriorityEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:els100SwitchPriorityEnable.setStatus(_A)
_Els100SwitchPriorityThreshold_Type=Integer32
_Els100SwitchPriorityThreshold_Object=MibScalar
els100SwitchPriorityThreshold=_Els100SwitchPriorityThreshold_Object((1,3,6,1,4,1,52,1011,3,16),_Els100SwitchPriorityThreshold_Type())
els100SwitchPriorityThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:els100SwitchPriorityThreshold.setStatus(_A)
_Els100SwitchPriorityPortTable_Object=MibTable
els100SwitchPriorityPortTable=_Els100SwitchPriorityPortTable_Object((1,3,6,1,4,1,52,1011,3,17))
if mibBuilder.loadTexts:els100SwitchPriorityPortTable.setStatus(_A)
_Els100SwitchPriorityPortEntry_Object=MibTableRow
els100SwitchPriorityPortEntry=_Els100SwitchPriorityPortEntry_Object((1,3,6,1,4,1,52,1011,3,17,1))
els100SwitchPriorityPortEntry.setIndexNames((0,_H,_L))
if mibBuilder.loadTexts:els100SwitchPriorityPortEntry.setStatus(_A)
_Els100SwitchPriorityPortId_Type=Integer32
_Els100SwitchPriorityPortId_Object=MibTableColumn
els100SwitchPriorityPortId=_Els100SwitchPriorityPortId_Object((1,3,6,1,4,1,52,1011,3,17,1,1),_Els100SwitchPriorityPortId_Type())
els100SwitchPriorityPortId.setMaxAccess(_F)
if mibBuilder.loadTexts:els100SwitchPriorityPortId.setStatus(_A)
_Els100SwitchPriorityDefault_Type=Integer32
_Els100SwitchPriorityDefault_Object=MibTableColumn
els100SwitchPriorityDefault=_Els100SwitchPriorityDefault_Object((1,3,6,1,4,1,52,1011,3,17,1,2),_Els100SwitchPriorityDefault_Type())
els100SwitchPriorityDefault.setMaxAccess(_B)
if mibBuilder.loadTexts:els100SwitchPriorityDefault.setStatus(_A)
class _Els100SwitchSpanningTreeStandby_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_Els100SwitchSpanningTreeStandby_Type.__name__=_C
_Els100SwitchSpanningTreeStandby_Object=MibScalar
els100SwitchSpanningTreeStandby=_Els100SwitchSpanningTreeStandby_Object((1,3,6,1,4,1,52,1011,3,18),_Els100SwitchSpanningTreeStandby_Type())
els100SwitchSpanningTreeStandby.setMaxAccess(_B)
if mibBuilder.loadTexts:els100SwitchSpanningTreeStandby.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'mib-2':mib_2,'cabletron':cabletron,'els100':els100,'els100SystemConfig':els100SystemConfig,'els100SysSerialno':els100SysSerialno,'els100SysTftpIPAddress':els100SysTftpIPAddress,'els100SysTftpFilename':els100SysTftpFilename,'els100SysPowerupCount':els100SysPowerupCount,'els100SysBrcastCutoffRate':els100SysBrcastCutoffRate,'els100SysGatewayIPAddress':els100SysGatewayIPAddress,'els100SysTftpStartDownload':els100SysTftpStartDownload,'els100SysBootPDhcpEnable':els100SysBootPDhcpEnable,'els100SysReset':els100SysReset,'els100SysSyslogServer':els100SysSyslogServer,'els100SysLowestSyslogSeverity':els100SysLowestSyslogSeverity,'els100SysComPortEnable':els100SysComPortEnable,'els100SysBoardID':els100SysBoardID,'els100PortTable':els100PortTable,'els100PortEntry':els100PortEntry,_I:els100Port,'els100PortStatus':els100PortStatus,'els100PortDuplexStatus':els100PortDuplexStatus,'els100PortForwardedFrames':els100PortForwardedFrames,'els100PortRcvdLocalFrames':els100PortRcvdLocalFrames,'els100PortName':els100PortName,'els100PortEnable':els100PortEnable,'els100PortSpeed':els100PortSpeed,'els100PortAutonegEnable':els100PortAutonegEnable,'els100PortFlowControlEnable':els100PortFlowControlEnable,'els100PortType':els100PortType,'els100Switch':els100Switch,'els100SwitchIPAddress':els100SwitchIPAddress,'els100SwitchSubnetMask':els100SwitchSubnetMask,'els100ActiveAgingTime':els100ActiveAgingTime,'els100SwitchSTPStatus':els100SwitchSTPStatus,'els100SwitchManager':els100SwitchManager,'els100SwitchTrapRcvr1':els100SwitchTrapRcvr1,'els100SwitchTrapCommunity1':els100SwitchTrapCommunity1,'els100SwitchTrapRcvr2':els100SwitchTrapRcvr2,'els100SwitchTrapCommunity2':els100SwitchTrapCommunity2,'els100SwitchTrapRcvr3':els100SwitchTrapRcvr3,'els100SwitchTrapCommunity3':els100SwitchTrapCommunity3,'els100SwitchTrapRcvr4':els100SwitchTrapRcvr4,'els100SwitchTrapCommunity4':els100SwitchTrapCommunity4,'els100SwitchPortMirroringStatus':els100SwitchPortMirroringStatus,'els100SwitchMirroredPort':els100SwitchMirroredPort,'els100SwitchMirroringPort':els100SwitchMirroringPort,'els100SwitchXmitMirrorEnable':els100SwitchXmitMirrorEnable,'els100SwitchRcvMirrorEnable':els100SwitchRcvMirrorEnable,'els100SwitchVlanEnable':els100SwitchVlanEnable,'els100SwitchVlanConfigTable':els100SwitchVlanConfigTable,'els100SwitchVlanEntry':els100SwitchVlanEntry,_J:els100SwitchVlanId,'els100SwitchVlanName':els100SwitchVlanName,'els100SwitchVlanPorts':els100SwitchVlanPorts,'els100SwitchVlanEgressPorts':els100SwitchVlanEgressPorts,'els100SwitchVlanStatus':els100SwitchVlanStatus,'els100SwitchVlanPortTable':els100SwitchVlanPortTable,'els100SwitchVlanPortEntry':els100SwitchVlanPortEntry,_K:els100SwitchVlanPortId,'els100SwitchVlanPvid':els100SwitchVlanPvid,'els100SwitchVlanPortType':els100SwitchVlanPortType,'els100SwitchPriorityEnable':els100SwitchPriorityEnable,'els100SwitchPriorityThreshold':els100SwitchPriorityThreshold,'els100SwitchPriorityPortTable':els100SwitchPriorityPortTable,'els100SwitchPriorityPortEntry':els100SwitchPriorityPortEntry,_L:els100SwitchPriorityPortId,'els100SwitchPriorityDefault':els100SwitchPriorityDefault,'els100SwitchSpanningTreeStandby':els100SwitchSpanningTreeStandby})