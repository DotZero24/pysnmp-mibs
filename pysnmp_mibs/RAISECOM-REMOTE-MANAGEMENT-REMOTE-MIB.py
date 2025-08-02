_S='raisecomRemoteStatsPortIfindex'
_R='unknown'
_Q='full-1000'
_P='half-1000'
_O='full-100'
_N='half-100'
_M='full-10'
_L='half-10'
_K='not-accessible'
_J='raisecomRemotePortIfindex'
_I='unavailable'
_H='RAISECOM-REMOTE-MANAGEMENT-REMOTE-MIB'
_G='normal'
_F='down'
_E='OctetString'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
raisecomAgent,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','raisecomAgent')
EntryStatus,=mibBuilder.importSymbols('RMON-MIB','EntryStatus')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
EnableVar,PortList=mibBuilder.importSymbols('SWITCH-TC','EnableVar','PortList')
raisecomRemoteManagementRemote=ModuleIdentity((1,3,6,1,4,1,8886,1,13))
_RaisecomRemoteManagementRemoteHideMibObjects_ObjectIdentity=ObjectIdentity
raisecomRemoteManagementRemoteHideMibObjects=_RaisecomRemoteManagementRemoteHideMibObjects_ObjectIdentity((1,3,6,1,4,1,8886,1,13,1))
class _RaisecomRemoteTemperature_Type(Integer32):defaultValue=65535
_RaisecomRemoteTemperature_Type.__name__=_C
_RaisecomRemoteTemperature_Object=MibScalar
raisecomRemoteTemperature=_RaisecomRemoteTemperature_Object((1,3,6,1,4,1,8886,1,13,1,1),_RaisecomRemoteTemperature_Type())
raisecomRemoteTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemoteTemperature.setStatus(_A)
class _RaisecomRemoteVolt3300_Type(Integer32):defaultValue=65535
_RaisecomRemoteVolt3300_Type.__name__=_C
_RaisecomRemoteVolt3300_Object=MibScalar
raisecomRemoteVolt3300=_RaisecomRemoteVolt3300_Object((1,3,6,1,4,1,8886,1,13,1,2),_RaisecomRemoteVolt3300_Type())
raisecomRemoteVolt3300.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemoteVolt3300.setStatus(_A)
class _RaisecomRemoteVolt2500_Type(Integer32):defaultValue=65535
_RaisecomRemoteVolt2500_Type.__name__=_C
_RaisecomRemoteVolt2500_Object=MibScalar
raisecomRemoteVolt2500=_RaisecomRemoteVolt2500_Object((1,3,6,1,4,1,8886,1,13,1,3),_RaisecomRemoteVolt2500_Type())
raisecomRemoteVolt2500.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemoteVolt2500.setStatus(_A)
class _RaisecomRemoteVolt1800_Type(Integer32):defaultValue=65535
_RaisecomRemoteVolt1800_Type.__name__=_C
_RaisecomRemoteVolt1800_Object=MibScalar
raisecomRemoteVolt1800=_RaisecomRemoteVolt1800_Object((1,3,6,1,4,1,8886,1,13,1,4),_RaisecomRemoteVolt1800_Type())
raisecomRemoteVolt1800.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemoteVolt1800.setStatus(_A)
class _RaisecomRemoteVolt1200_Type(Integer32):defaultValue=65535
_RaisecomRemoteVolt1200_Type.__name__=_C
_RaisecomRemoteVolt1200_Object=MibScalar
raisecomRemoteVolt1200=_RaisecomRemoteVolt1200_Object((1,3,6,1,4,1,8886,1,13,1,5),_RaisecomRemoteVolt1200_Type())
raisecomRemoteVolt1200.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemoteVolt1200.setStatus(_A)
class _RaisecomRemoteSysOperation_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('ready',1),('write',2),('erase',3),('reboot',4)))
_RaisecomRemoteSysOperation_Type.__name__=_C
_RaisecomRemoteSysOperation_Object=MibScalar
raisecomRemoteSysOperation=_RaisecomRemoteSysOperation_Object((1,3,6,1,4,1,8886,1,13,1,6),_RaisecomRemoteSysOperation_Type())
raisecomRemoteSysOperation.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomRemoteSysOperation.setStatus(_A)
class _RaisecomRemoteSysOperationState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('ready',1),('running',2),('successful',3),('failed',4)))
_RaisecomRemoteSysOperationState_Type.__name__=_C
_RaisecomRemoteSysOperationState_Object=MibScalar
raisecomRemoteSysOperationState=_RaisecomRemoteSysOperationState_Object((1,3,6,1,4,1,8886,1,13,1,7),_RaisecomRemoteSysOperationState_Type())
raisecomRemoteSysOperationState.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemoteSysOperationState.setStatus(_A)
class _RaisecomRemoteHostName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_RaisecomRemoteHostName_Type.__name__=_E
_RaisecomRemoteHostName_Object=MibScalar
raisecomRemoteHostName=_RaisecomRemoteHostName_Object((1,3,6,1,4,1,8886,1,13,1,8),_RaisecomRemoteHostName_Type())
raisecomRemoteHostName.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomRemoteHostName.setStatus(_A)
_RaisecomRemoteOamNotificationEnable_Type=EnableVar
_RaisecomRemoteOamNotificationEnable_Object=MibScalar
raisecomRemoteOamNotificationEnable=_RaisecomRemoteOamNotificationEnable_Object((1,3,6,1,4,1,8886,1,13,1,9),_RaisecomRemoteOamNotificationEnable_Type())
raisecomRemoteOamNotificationEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomRemoteOamNotificationEnable.setStatus(_A)
class _RaisecomRemoteCommunityName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_RaisecomRemoteCommunityName_Type.__name__=_E
_RaisecomRemoteCommunityName_Object=MibScalar
raisecomRemoteCommunityName=_RaisecomRemoteCommunityName_Object((1,3,6,1,4,1,8886,1,13,1,10),_RaisecomRemoteCommunityName_Type())
raisecomRemoteCommunityName.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomRemoteCommunityName.setStatus(_A)
class _RaisecomRemoteCommunityPermission_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('readOnly',1),('readWrite',2),('invalid',3)))
_RaisecomRemoteCommunityPermission_Type.__name__=_C
_RaisecomRemoteCommunityPermission_Object=MibScalar
raisecomRemoteCommunityPermission=_RaisecomRemoteCommunityPermission_Object((1,3,6,1,4,1,8886,1,13,1,11),_RaisecomRemoteCommunityPermission_Type())
raisecomRemoteCommunityPermission.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomRemoteCommunityPermission.setStatus(_A)
_RaisecomRemoteL3IpAddr_Type=IpAddress
_RaisecomRemoteL3IpAddr_Object=MibScalar
raisecomRemoteL3IpAddr=_RaisecomRemoteL3IpAddr_Object((1,3,6,1,4,1,8886,1,13,1,12),_RaisecomRemoteL3IpAddr_Type())
raisecomRemoteL3IpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomRemoteL3IpAddr.setStatus(_A)
_RaisecomRemoteL3Mask_Type=IpAddress
_RaisecomRemoteL3Mask_Object=MibScalar
raisecomRemoteL3Mask=_RaisecomRemoteL3Mask_Object((1,3,6,1,4,1,8886,1,13,1,13),_RaisecomRemoteL3Mask_Type())
raisecomRemoteL3Mask.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomRemoteL3Mask.setStatus(_A)
class _RaisecomRemoteL3VidIface_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_RaisecomRemoteL3VidIface_Type.__name__=_C
_RaisecomRemoteL3VidIface_Object=MibScalar
raisecomRemoteL3VidIface=_RaisecomRemoteL3VidIface_Object((1,3,6,1,4,1,8886,1,13,1,14),_RaisecomRemoteL3VidIface_Type())
raisecomRemoteL3VidIface.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomRemoteL3VidIface.setStatus(_A)
_RaisecomRemoteL3VidMemberPorts_Type=PortList
_RaisecomRemoteL3VidMemberPorts_Object=MibScalar
raisecomRemoteL3VidMemberPorts=_RaisecomRemoteL3VidMemberPorts_Object((1,3,6,1,4,1,8886,1,13,1,15),_RaisecomRemoteL3VidMemberPorts_Type())
raisecomRemoteL3VidMemberPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemoteL3VidMemberPorts.setStatus(_A)
_RaisecomRemoteL3VidUntaggedPorts_Type=PortList
_RaisecomRemoteL3VidUntaggedPorts_Object=MibScalar
raisecomRemoteL3VidUntaggedPorts=_RaisecomRemoteL3VidUntaggedPorts_Object((1,3,6,1,4,1,8886,1,13,1,16),_RaisecomRemoteL3VidUntaggedPorts_Type())
raisecomRemoteL3VidUntaggedPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemoteL3VidUntaggedPorts.setStatus(_A)
_RaisecomRemoteL3DefaultGateway_Type=IpAddress
_RaisecomRemoteL3DefaultGateway_Object=MibScalar
raisecomRemoteL3DefaultGateway=_RaisecomRemoteL3DefaultGateway_Object((1,3,6,1,4,1,8886,1,13,1,17),_RaisecomRemoteL3DefaultGateway_Type())
raisecomRemoteL3DefaultGateway.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomRemoteL3DefaultGateway.setStatus(_A)
_RaisecomRemotePortTable_Object=MibTable
raisecomRemotePortTable=_RaisecomRemotePortTable_Object((1,3,6,1,4,1,8886,1,13,1,18))
if mibBuilder.loadTexts:raisecomRemotePortTable.setStatus(_A)
_RaisecomRemotePortEntry_Object=MibTableRow
raisecomRemotePortEntry=_RaisecomRemotePortEntry_Object((1,3,6,1,4,1,8886,1,13,1,18,1))
raisecomRemotePortEntry.setIndexNames((0,_H,_J))
if mibBuilder.loadTexts:raisecomRemotePortEntry.setStatus(_A)
_RaisecomRemotePortIfindex_Type=Integer32
_RaisecomRemotePortIfindex_Object=MibTableColumn
raisecomRemotePortIfindex=_RaisecomRemotePortIfindex_Object((1,3,6,1,4,1,8886,1,13,1,18,1,2),_RaisecomRemotePortIfindex_Type())
raisecomRemotePortIfindex.setMaxAccess(_K)
if mibBuilder.loadTexts:raisecomRemotePortIfindex.setStatus(_A)
class _RaisecomRemotePortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('inexistence',0),('fx-DulMode-1000M',1),('tx-1000M',2),('fx-SigMode-1000M',3),('fx-DulMode-100M',4),('fx-SigMode-100M',5),('tx-100M',6)))
_RaisecomRemotePortType_Type.__name__=_C
_RaisecomRemotePortType_Object=MibTableColumn
raisecomRemotePortType=_RaisecomRemotePortType_Object((1,3,6,1,4,1,8886,1,13,1,18,1,3),_RaisecomRemotePortType_Type())
raisecomRemotePortType.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemotePortType.setStatus(_A)
class _RaisecomRemotePortName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_RaisecomRemotePortName_Type.__name__=_E
_RaisecomRemotePortName_Object=MibTableColumn
raisecomRemotePortName=_RaisecomRemotePortName_Object((1,3,6,1,4,1,8886,1,13,1,18,1,4),_RaisecomRemotePortName_Type())
raisecomRemotePortName.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemotePortName.setStatus(_A)
class _RaisecomRemotePortAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),(_F,2)))
_RaisecomRemotePortAdminStatus_Type.__name__=_C
_RaisecomRemotePortAdminStatus_Object=MibTableColumn
raisecomRemotePortAdminStatus=_RaisecomRemotePortAdminStatus_Object((1,3,6,1,4,1,8886,1,13,1,18,1,5),_RaisecomRemotePortAdminStatus_Type())
raisecomRemotePortAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomRemotePortAdminStatus.setStatus(_A)
class _RaisecomRemotePortOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),(_F,2)))
_RaisecomRemotePortOperStatus_Type.__name__=_C
_RaisecomRemotePortOperStatus_Object=MibTableColumn
raisecomRemotePortOperStatus=_RaisecomRemotePortOperStatus_Object((1,3,6,1,4,1,8886,1,13,1,18,1,6),_RaisecomRemotePortOperStatus_Type())
raisecomRemotePortOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemotePortOperStatus.setStatus(_A)
class _RaisecomRemotePortDuplexSpeedSet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('autonegotiate',1),(_L,2),(_M,3),(_N,4),(_O,5),(_P,6),(_Q,7)))
_RaisecomRemotePortDuplexSpeedSet_Type.__name__=_C
_RaisecomRemotePortDuplexSpeedSet_Object=MibTableColumn
raisecomRemotePortDuplexSpeedSet=_RaisecomRemotePortDuplexSpeedSet_Object((1,3,6,1,4,1,8886,1,13,1,18,1,7),_RaisecomRemotePortDuplexSpeedSet_Type())
raisecomRemotePortDuplexSpeedSet.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomRemotePortDuplexSpeedSet.setStatus(_A)
class _RaisecomRemotePortDuplexSpeedGet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,99)));namedValues=NamedValues(*((_R,1),(_L,2),(_M,3),(_N,4),(_O,5),(_P,6),(_Q,7),('illegal',99)))
_RaisecomRemotePortDuplexSpeedGet_Type.__name__=_C
_RaisecomRemotePortDuplexSpeedGet_Object=MibTableColumn
raisecomRemotePortDuplexSpeedGet=_RaisecomRemotePortDuplexSpeedGet_Object((1,3,6,1,4,1,8886,1,13,1,18,1,8),_RaisecomRemotePortDuplexSpeedGet_Type())
raisecomRemotePortDuplexSpeedGet.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemotePortDuplexSpeedGet.setStatus(_A)
_RaisecomRemotePortFlowControlEnable_Type=EnableVar
_RaisecomRemotePortFlowControlEnable_Object=MibTableColumn
raisecomRemotePortFlowControlEnable=_RaisecomRemotePortFlowControlEnable_Object((1,3,6,1,4,1,8886,1,13,1,18,1,9),_RaisecomRemotePortFlowControlEnable_Type())
raisecomRemotePortFlowControlEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomRemotePortFlowControlEnable.setStatus(_A)
_RaisecomRemotePortFlowControlStatus_Type=EnableVar
_RaisecomRemotePortFlowControlStatus_Object=MibTableColumn
raisecomRemotePortFlowControlStatus=_RaisecomRemotePortFlowControlStatus_Object((1,3,6,1,4,1,8886,1,13,1,18,1,10),_RaisecomRemotePortFlowControlStatus_Type())
raisecomRemotePortFlowControlStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemotePortFlowControlStatus.setStatus(_A)
class _RaisecomRemotePortIngressRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1048576))
_RaisecomRemotePortIngressRate_Type.__name__=_C
_RaisecomRemotePortIngressRate_Object=MibTableColumn
raisecomRemotePortIngressRate=_RaisecomRemotePortIngressRate_Object((1,3,6,1,4,1,8886,1,13,1,18,1,11),_RaisecomRemotePortIngressRate_Type())
raisecomRemotePortIngressRate.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomRemotePortIngressRate.setStatus(_A)
class _RaisecomRemotePortEgressRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1048576))
_RaisecomRemotePortEgressRate_Type.__name__=_C
_RaisecomRemotePortEgressRate_Object=MibTableColumn
raisecomRemotePortEgressRate=_RaisecomRemotePortEgressRate_Object((1,3,6,1,4,1,8886,1,13,1,18,1,12),_RaisecomRemotePortEgressRate_Type())
raisecomRemotePortEgressRate.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomRemotePortEgressRate.setStatus(_A)
_RaisecomRemotePortFaultPassEnable_Type=EnableVar
_RaisecomRemotePortFaultPassEnable_Object=MibTableColumn
raisecomRemotePortFaultPassEnable=_RaisecomRemotePortFaultPassEnable_Object((1,3,6,1,4,1,8886,1,13,1,18,1,13),_RaisecomRemotePortFaultPassEnable_Type())
raisecomRemotePortFaultPassEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomRemotePortFaultPassEnable.setStatus(_A)
_RaisecomRemotePortFaultPassPorts_Type=PortList
_RaisecomRemotePortFaultPassPorts_Object=MibTableColumn
raisecomRemotePortFaultPassPorts=_RaisecomRemotePortFaultPassPorts_Object((1,3,6,1,4,1,8886,1,13,1,18,1,14),_RaisecomRemotePortFaultPassPorts_Type())
raisecomRemotePortFaultPassPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomRemotePortFaultPassPorts.setStatus(_A)
class _RaisecomRemotePortFaultPassStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_RaisecomRemotePortFaultPassStatus_Type.__name__=_C
_RaisecomRemotePortFaultPassStatus_Object=MibTableColumn
raisecomRemotePortFaultPassStatus=_RaisecomRemotePortFaultPassStatus_Object((1,3,6,1,4,1,8886,1,13,1,18,1,15),_RaisecomRemotePortFaultPassStatus_Type())
raisecomRemotePortFaultPassStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemotePortFaultPassStatus.setStatus(_A)
class _RaisecomRemotePortFaultReturnEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('enable',1),('disable',2),(_I,3)))
_RaisecomRemotePortFaultReturnEnable_Type.__name__=_C
_RaisecomRemotePortFaultReturnEnable_Object=MibTableColumn
raisecomRemotePortFaultReturnEnable=_RaisecomRemotePortFaultReturnEnable_Object((1,3,6,1,4,1,8886,1,13,1,18,1,16),_RaisecomRemotePortFaultReturnEnable_Type())
raisecomRemotePortFaultReturnEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomRemotePortFaultReturnEnable.setStatus(_A)
class _RaisecomRemotePortFaultReturnStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_F,2),(_I,3)))
_RaisecomRemotePortFaultReturnStatus_Type.__name__=_C
_RaisecomRemotePortFaultReturnStatus_Object=MibTableColumn
raisecomRemotePortFaultReturnStatus=_RaisecomRemotePortFaultReturnStatus_Object((1,3,6,1,4,1,8886,1,13,1,18,1,17),_RaisecomRemotePortFaultReturnStatus_Type())
raisecomRemotePortFaultReturnStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemotePortFaultReturnStatus.setStatus(_A)
class _RaisecomRemotePortSD_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),('sd',2),(_I,3)))
_RaisecomRemotePortSD_Type.__name__=_C
_RaisecomRemotePortSD_Object=MibTableColumn
raisecomRemotePortSD=_RaisecomRemotePortSD_Object((1,3,6,1,4,1,8886,1,13,1,18,1,18),_RaisecomRemotePortSD_Type())
raisecomRemotePortSD.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemotePortSD.setStatus(_A)
class _RaisecomRemoteOptModuleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('optical-M',1),('optical-S1',2),('optical-S2',3),('optical-S3',4),('optical-SS13',5),('optical-SS15',6),('optical-SS23',7),('optical-SS25',8),('optical-SS35',9),(_R,10)))
_RaisecomRemoteOptModuleType_Type.__name__=_C
_RaisecomRemoteOptModuleType_Object=MibTableColumn
raisecomRemoteOptModuleType=_RaisecomRemoteOptModuleType_Object((1,3,6,1,4,1,8886,1,13,1,18,1,19),_RaisecomRemoteOptModuleType_Type())
raisecomRemoteOptModuleType.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemoteOptModuleType.setStatus(_A)
class _RaisecomRemotePortDescr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_RaisecomRemotePortDescr_Type.__name__=_E
_RaisecomRemotePortDescr_Object=MibTableColumn
raisecomRemotePortDescr=_RaisecomRemotePortDescr_Object((1,3,6,1,4,1,8886,1,13,1,18,1,20),_RaisecomRemotePortDescr_Type())
raisecomRemotePortDescr.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomRemotePortDescr.setStatus(_A)
_RaisecomRemotePortStatsTable_Object=MibTable
raisecomRemotePortStatsTable=_RaisecomRemotePortStatsTable_Object((1,3,6,1,4,1,8886,1,13,1,19))
if mibBuilder.loadTexts:raisecomRemotePortStatsTable.setStatus(_A)
_RaisecomRemotePortStatsEntry_Object=MibTableRow
raisecomRemotePortStatsEntry=_RaisecomRemotePortStatsEntry_Object((1,3,6,1,4,1,8886,1,13,1,19,1))
raisecomRemotePortStatsEntry.setIndexNames((0,_H,_S))
if mibBuilder.loadTexts:raisecomRemotePortStatsEntry.setStatus(_A)
_RaisecomRemoteStatsPortIfindex_Type=Integer32
_RaisecomRemoteStatsPortIfindex_Object=MibTableColumn
raisecomRemoteStatsPortIfindex=_RaisecomRemoteStatsPortIfindex_Object((1,3,6,1,4,1,8886,1,13,1,19,1,1),_RaisecomRemoteStatsPortIfindex_Type())
raisecomRemoteStatsPortIfindex.setMaxAccess(_K)
if mibBuilder.loadTexts:raisecomRemoteStatsPortIfindex.setStatus(_A)
_RaisecomRemotePortInOctets_Type=Counter64
_RaisecomRemotePortInOctets_Object=MibTableColumn
raisecomRemotePortInOctets=_RaisecomRemotePortInOctets_Object((1,3,6,1,4,1,8886,1,13,1,19,1,2),_RaisecomRemotePortInOctets_Type())
raisecomRemotePortInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemotePortInOctets.setStatus(_A)
_RaisecomRemotePortInPkts_Type=Counter64
_RaisecomRemotePortInPkts_Object=MibTableColumn
raisecomRemotePortInPkts=_RaisecomRemotePortInPkts_Object((1,3,6,1,4,1,8886,1,13,1,19,1,3),_RaisecomRemotePortInPkts_Type())
raisecomRemotePortInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemotePortInPkts.setStatus(_A)
_RaisecomRemotePortInUcastPkts_Type=Counter64
_RaisecomRemotePortInUcastPkts_Object=MibTableColumn
raisecomRemotePortInUcastPkts=_RaisecomRemotePortInUcastPkts_Object((1,3,6,1,4,1,8886,1,13,1,19,1,4),_RaisecomRemotePortInUcastPkts_Type())
raisecomRemotePortInUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemotePortInUcastPkts.setStatus(_A)
_RaisecomRemotePortInMulticastPkts_Type=Counter64
_RaisecomRemotePortInMulticastPkts_Object=MibTableColumn
raisecomRemotePortInMulticastPkts=_RaisecomRemotePortInMulticastPkts_Object((1,3,6,1,4,1,8886,1,13,1,19,1,5),_RaisecomRemotePortInMulticastPkts_Type())
raisecomRemotePortInMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemotePortInMulticastPkts.setStatus(_A)
_RaisecomRemotePortInBroadcastPkts_Type=Counter64
_RaisecomRemotePortInBroadcastPkts_Object=MibTableColumn
raisecomRemotePortInBroadcastPkts=_RaisecomRemotePortInBroadcastPkts_Object((1,3,6,1,4,1,8886,1,13,1,19,1,6),_RaisecomRemotePortInBroadcastPkts_Type())
raisecomRemotePortInBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemotePortInBroadcastPkts.setStatus(_A)
_RaisecomRemotePortOutOctets_Type=Counter64
_RaisecomRemotePortOutOctets_Object=MibTableColumn
raisecomRemotePortOutOctets=_RaisecomRemotePortOutOctets_Object((1,3,6,1,4,1,8886,1,13,1,19,1,7),_RaisecomRemotePortOutOctets_Type())
raisecomRemotePortOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemotePortOutOctets.setStatus(_A)
_RaisecomRemotePortOutPkts_Type=Counter64
_RaisecomRemotePortOutPkts_Object=MibTableColumn
raisecomRemotePortOutPkts=_RaisecomRemotePortOutPkts_Object((1,3,6,1,4,1,8886,1,13,1,19,1,8),_RaisecomRemotePortOutPkts_Type())
raisecomRemotePortOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemotePortOutPkts.setStatus(_A)
_RaisecomRemotePortOutUcastPkts_Type=Counter64
_RaisecomRemotePortOutUcastPkts_Object=MibTableColumn
raisecomRemotePortOutUcastPkts=_RaisecomRemotePortOutUcastPkts_Object((1,3,6,1,4,1,8886,1,13,1,19,1,9),_RaisecomRemotePortOutUcastPkts_Type())
raisecomRemotePortOutUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemotePortOutUcastPkts.setStatus(_A)
_RaisecomRemotePortOutMulticastPkts_Type=Counter64
_RaisecomRemotePortOutMulticastPkts_Object=MibTableColumn
raisecomRemotePortOutMulticastPkts=_RaisecomRemotePortOutMulticastPkts_Object((1,3,6,1,4,1,8886,1,13,1,19,1,10),_RaisecomRemotePortOutMulticastPkts_Type())
raisecomRemotePortOutMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemotePortOutMulticastPkts.setStatus(_A)
_RaisecomRemotePortOutBroadcastPkts_Type=Counter64
_RaisecomRemotePortOutBroadcastPkts_Object=MibTableColumn
raisecomRemotePortOutBroadcastPkts=_RaisecomRemotePortOutBroadcastPkts_Object((1,3,6,1,4,1,8886,1,13,1,19,1,11),_RaisecomRemotePortOutBroadcastPkts_Type())
raisecomRemotePortOutBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemotePortOutBroadcastPkts.setStatus(_A)
_RaisecomRemotePortErrorPkts_Type=Counter32
_RaisecomRemotePortErrorPkts_Object=MibTableColumn
raisecomRemotePortErrorPkts=_RaisecomRemotePortErrorPkts_Object((1,3,6,1,4,1,8886,1,13,1,19,1,12),_RaisecomRemotePortErrorPkts_Type())
raisecomRemotePortErrorPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemotePortErrorPkts.setStatus(_A)
_RaisecomRemotePortDropEvents_Type=Counter32
_RaisecomRemotePortDropEvents_Object=MibTableColumn
raisecomRemotePortDropEvents=_RaisecomRemotePortDropEvents_Object((1,3,6,1,4,1,8886,1,13,1,19,1,13),_RaisecomRemotePortDropEvents_Type())
raisecomRemotePortDropEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemotePortDropEvents.setStatus(_A)
_RaisecomRemotePortCRCAlignErrors_Type=Counter32
_RaisecomRemotePortCRCAlignErrors_Object=MibTableColumn
raisecomRemotePortCRCAlignErrors=_RaisecomRemotePortCRCAlignErrors_Object((1,3,6,1,4,1,8886,1,13,1,19,1,14),_RaisecomRemotePortCRCAlignErrors_Type())
raisecomRemotePortCRCAlignErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemotePortCRCAlignErrors.setStatus(_A)
_RaisecomRemotePortUndersizePkts_Type=Counter32
_RaisecomRemotePortUndersizePkts_Object=MibTableColumn
raisecomRemotePortUndersizePkts=_RaisecomRemotePortUndersizePkts_Object((1,3,6,1,4,1,8886,1,13,1,19,1,15),_RaisecomRemotePortUndersizePkts_Type())
raisecomRemotePortUndersizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemotePortUndersizePkts.setStatus(_A)
_RaisecomRemotePortOversizePkts_Type=Counter32
_RaisecomRemotePortOversizePkts_Object=MibTableColumn
raisecomRemotePortOversizePkts=_RaisecomRemotePortOversizePkts_Object((1,3,6,1,4,1,8886,1,13,1,19,1,16),_RaisecomRemotePortOversizePkts_Type())
raisecomRemotePortOversizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemotePortOversizePkts.setStatus(_A)
_RaisecomRemotePortFragments_Type=Counter32
_RaisecomRemotePortFragments_Object=MibTableColumn
raisecomRemotePortFragments=_RaisecomRemotePortFragments_Object((1,3,6,1,4,1,8886,1,13,1,19,1,17),_RaisecomRemotePortFragments_Type())
raisecomRemotePortFragments.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemotePortFragments.setStatus(_A)
_RaisecomRemotePortJabbers_Type=Counter32
_RaisecomRemotePortJabbers_Object=MibTableColumn
raisecomRemotePortJabbers=_RaisecomRemotePortJabbers_Object((1,3,6,1,4,1,8886,1,13,1,19,1,18),_RaisecomRemotePortJabbers_Type())
raisecomRemotePortJabbers.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemotePortJabbers.setStatus(_A)
_RaisecomRemotePortCollisions_Type=Counter32
_RaisecomRemotePortCollisions_Object=MibTableColumn
raisecomRemotePortCollisions=_RaisecomRemotePortCollisions_Object((1,3,6,1,4,1,8886,1,13,1,19,1,19),_RaisecomRemotePortCollisions_Type())
raisecomRemotePortCollisions.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemotePortCollisions.setStatus(_A)
class _RaisecomRemoteVoltNormal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),('high',2),('low',3)))
_RaisecomRemoteVoltNormal_Type.__name__=_C
_RaisecomRemoteVoltNormal_Object=MibScalar
raisecomRemoteVoltNormal=_RaisecomRemoteVoltNormal_Object((1,3,6,1,4,1,8886,1,13,1,20),_RaisecomRemoteVoltNormal_Type())
raisecomRemoteVoltNormal.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemoteVoltNormal.setStatus(_A)
_RaisecomRemoteMaxAllowedFrameLength_Type=Integer32
_RaisecomRemoteMaxAllowedFrameLength_Object=MibScalar
raisecomRemoteMaxAllowedFrameLength=_RaisecomRemoteMaxAllowedFrameLength_Object((1,3,6,1,4,1,8886,1,13,1,21),_RaisecomRemoteMaxAllowedFrameLength_Type())
raisecomRemoteMaxAllowedFrameLength.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomRemoteMaxAllowedFrameLength.setStatus(_A)
_RaisecomRemoteL3ObPortIpAddr_Type=IpAddress
_RaisecomRemoteL3ObPortIpAddr_Object=MibScalar
raisecomRemoteL3ObPortIpAddr=_RaisecomRemoteL3ObPortIpAddr_Object((1,3,6,1,4,1,8886,1,13,1,22),_RaisecomRemoteL3ObPortIpAddr_Type())
raisecomRemoteL3ObPortIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomRemoteL3ObPortIpAddr.setStatus(_A)
_RaisecomRemoteL3ObPortMask_Type=IpAddress
_RaisecomRemoteL3ObPortMask_Object=MibScalar
raisecomRemoteL3ObPortMask=_RaisecomRemoteL3ObPortMask_Object((1,3,6,1,4,1,8886,1,13,1,23),_RaisecomRemoteL3ObPortMask_Type())
raisecomRemoteL3ObPortMask.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomRemoteL3ObPortMask.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'raisecomRemoteManagementRemote':raisecomRemoteManagementRemote,'raisecomRemoteManagementRemoteHideMibObjects':raisecomRemoteManagementRemoteHideMibObjects,'raisecomRemoteTemperature':raisecomRemoteTemperature,'raisecomRemoteVolt3300':raisecomRemoteVolt3300,'raisecomRemoteVolt2500':raisecomRemoteVolt2500,'raisecomRemoteVolt1800':raisecomRemoteVolt1800,'raisecomRemoteVolt1200':raisecomRemoteVolt1200,'raisecomRemoteSysOperation':raisecomRemoteSysOperation,'raisecomRemoteSysOperationState':raisecomRemoteSysOperationState,'raisecomRemoteHostName':raisecomRemoteHostName,'raisecomRemoteOamNotificationEnable':raisecomRemoteOamNotificationEnable,'raisecomRemoteCommunityName':raisecomRemoteCommunityName,'raisecomRemoteCommunityPermission':raisecomRemoteCommunityPermission,'raisecomRemoteL3IpAddr':raisecomRemoteL3IpAddr,'raisecomRemoteL3Mask':raisecomRemoteL3Mask,'raisecomRemoteL3VidIface':raisecomRemoteL3VidIface,'raisecomRemoteL3VidMemberPorts':raisecomRemoteL3VidMemberPorts,'raisecomRemoteL3VidUntaggedPorts':raisecomRemoteL3VidUntaggedPorts,'raisecomRemoteL3DefaultGateway':raisecomRemoteL3DefaultGateway,'raisecomRemotePortTable':raisecomRemotePortTable,'raisecomRemotePortEntry':raisecomRemotePortEntry,_J:raisecomRemotePortIfindex,'raisecomRemotePortType':raisecomRemotePortType,'raisecomRemotePortName':raisecomRemotePortName,'raisecomRemotePortAdminStatus':raisecomRemotePortAdminStatus,'raisecomRemotePortOperStatus':raisecomRemotePortOperStatus,'raisecomRemotePortDuplexSpeedSet':raisecomRemotePortDuplexSpeedSet,'raisecomRemotePortDuplexSpeedGet':raisecomRemotePortDuplexSpeedGet,'raisecomRemotePortFlowControlEnable':raisecomRemotePortFlowControlEnable,'raisecomRemotePortFlowControlStatus':raisecomRemotePortFlowControlStatus,'raisecomRemotePortIngressRate':raisecomRemotePortIngressRate,'raisecomRemotePortEgressRate':raisecomRemotePortEgressRate,'raisecomRemotePortFaultPassEnable':raisecomRemotePortFaultPassEnable,'raisecomRemotePortFaultPassPorts':raisecomRemotePortFaultPassPorts,'raisecomRemotePortFaultPassStatus':raisecomRemotePortFaultPassStatus,'raisecomRemotePortFaultReturnEnable':raisecomRemotePortFaultReturnEnable,'raisecomRemotePortFaultReturnStatus':raisecomRemotePortFaultReturnStatus,'raisecomRemotePortSD':raisecomRemotePortSD,'raisecomRemoteOptModuleType':raisecomRemoteOptModuleType,'raisecomRemotePortDescr':raisecomRemotePortDescr,'raisecomRemotePortStatsTable':raisecomRemotePortStatsTable,'raisecomRemotePortStatsEntry':raisecomRemotePortStatsEntry,_S:raisecomRemoteStatsPortIfindex,'raisecomRemotePortInOctets':raisecomRemotePortInOctets,'raisecomRemotePortInPkts':raisecomRemotePortInPkts,'raisecomRemotePortInUcastPkts':raisecomRemotePortInUcastPkts,'raisecomRemotePortInMulticastPkts':raisecomRemotePortInMulticastPkts,'raisecomRemotePortInBroadcastPkts':raisecomRemotePortInBroadcastPkts,'raisecomRemotePortOutOctets':raisecomRemotePortOutOctets,'raisecomRemotePortOutPkts':raisecomRemotePortOutPkts,'raisecomRemotePortOutUcastPkts':raisecomRemotePortOutUcastPkts,'raisecomRemotePortOutMulticastPkts':raisecomRemotePortOutMulticastPkts,'raisecomRemotePortOutBroadcastPkts':raisecomRemotePortOutBroadcastPkts,'raisecomRemotePortErrorPkts':raisecomRemotePortErrorPkts,'raisecomRemotePortDropEvents':raisecomRemotePortDropEvents,'raisecomRemotePortCRCAlignErrors':raisecomRemotePortCRCAlignErrors,'raisecomRemotePortUndersizePkts':raisecomRemotePortUndersizePkts,'raisecomRemotePortOversizePkts':raisecomRemotePortOversizePkts,'raisecomRemotePortFragments':raisecomRemotePortFragments,'raisecomRemotePortJabbers':raisecomRemotePortJabbers,'raisecomRemotePortCollisions':raisecomRemotePortCollisions,'raisecomRemoteVoltNormal':raisecomRemoteVoltNormal,'raisecomRemoteMaxAllowedFrameLength':raisecomRemoteMaxAllowedFrameLength,'raisecomRemoteL3ObPortIpAddr':raisecomRemoteL3ObPortIpAddr,'raisecomRemoteL3ObPortMask':raisecomRemoteL3ObPortMask})