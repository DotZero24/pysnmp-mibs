_Z='cat2600TsUFCSlotNum'
_Y='cat2600TsFilterType'
_X='cat2600TsFilterStationAddress'
_W='cat2600TsPipeNumber'
_V='cat2600TsOptDmnStaPos'
_U='cat2600TsDmnStationDmnIndex'
_T='cat2600TsDmnStationAddress'
_S='cat2600TsPortStnAddress'
_R='cat2600TsPortStnPortNum'
_Q='cat2600TsOptPortStaPos'
_P='softReset'
_O='hardReset'
_N='invalid'
_M='cat2600TsTrapRcvrIndex'
_L='cat2600TsDmnIndex'
_K='not-accessible'
_J='cat2600TsPortIndex'
_I='running'
_H='other'
_G='OctetString'
_F='DisplayString'
_E='CAT2600-MIB'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
class MacAddr(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_Cisco_ObjectIdentity=ObjectIdentity
cisco=_Cisco_ObjectIdentity((1,3,6,1,4,1,9))
_CatProd_ObjectIdentity=ObjectIdentity
catProd=_CatProd_ObjectIdentity((1,3,6,1,4,1,9,1))
_Cat2600_ObjectIdentity=ObjectIdentity
cat2600=_Cat2600_ObjectIdentity((1,3,6,1,4,1,9,1,111))
_Cat2600Ts_ObjectIdentity=ObjectIdentity
cat2600Ts=_Cat2600Ts_ObjectIdentity((1,3,6,1,4,1,9,1,111,1))
_Cat2600TsObjectID_ObjectIdentity=ObjectIdentity
cat2600TsObjectID=_Cat2600TsObjectID_ObjectIdentity((1,3,6,1,4,1,9,1,111,1,1))
_Cat2600TsSysObjectID_ObjectIdentity=ObjectIdentity
cat2600TsSysObjectID=_Cat2600TsSysObjectID_ObjectIdentity((1,3,6,1,4,1,9,1,111,1,1,1))
_Cat2600TsObjects_ObjectIdentity=ObjectIdentity
cat2600TsObjects=_Cat2600TsObjects_ObjectIdentity((1,3,6,1,4,1,9,1,111,1,2))
_Cat2600TsMain_ObjectIdentity=ObjectIdentity
cat2600TsMain=_Cat2600TsMain_ObjectIdentity((1,3,6,1,4,1,9,1,111,1,2,1))
_Cat2600TsConfig_ObjectIdentity=ObjectIdentity
cat2600TsConfig=_Cat2600TsConfig_ObjectIdentity((1,3,6,1,4,1,9,1,111,1,2,1,1))
class _Cat2600TsFwVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_Cat2600TsFwVer_Type.__name__=_F
_Cat2600TsFwVer_Object=MibScalar
cat2600TsFwVer=_Cat2600TsFwVer_Object((1,3,6,1,4,1,9,1,111,1,2,1,1,1),_Cat2600TsFwVer_Type())
cat2600TsFwVer.setMaxAccess(_B)
if mibBuilder.loadTexts:cat2600TsFwVer.setStatus(_A)
class _Cat2600TsHwVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_Cat2600TsHwVer_Type.__name__=_F
_Cat2600TsHwVer_Object=MibScalar
cat2600TsHwVer=_Cat2600TsHwVer_Object((1,3,6,1,4,1,9,1,111,1,2,1,1,2),_Cat2600TsHwVer_Type())
cat2600TsHwVer.setMaxAccess(_B)
if mibBuilder.loadTexts:cat2600TsHwVer.setStatus(_A)
class _Cat2600TsSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_Cat2600TsSerialNumber_Type.__name__=_F
_Cat2600TsSerialNumber_Object=MibScalar
cat2600TsSerialNumber=_Cat2600TsSerialNumber_Object((1,3,6,1,4,1,9,1,111,1,2,1,1,3),_Cat2600TsSerialNumber_Type())
cat2600TsSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:cat2600TsSerialNumber.setStatus(_A)
class _Cat2600TsInstallationDate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_Cat2600TsInstallationDate_Type.__name__=_F
_Cat2600TsInstallationDate_Object=MibScalar
cat2600TsInstallationDate=_Cat2600TsInstallationDate_Object((1,3,6,1,4,1,9,1,111,1,2,1,1,4),_Cat2600TsInstallationDate_Type())
cat2600TsInstallationDate.setMaxAccess(_C)
if mibBuilder.loadTexts:cat2600TsInstallationDate.setStatus(_A)
_Cat2600TsFwSize_Type=Integer32
_Cat2600TsFwSize_Object=MibScalar
cat2600TsFwSize=_Cat2600TsFwSize_Object((1,3,6,1,4,1,9,1,111,1,2,1,1,5),_Cat2600TsFwSize_Type())
cat2600TsFwSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cat2600TsFwSize.setStatus(_A)
_Cat2600TsFwCRC_Type=Integer32
_Cat2600TsFwCRC_Object=MibScalar
cat2600TsFwCRC=_Cat2600TsFwCRC_Object((1,3,6,1,4,1,9,1,111,1,2,1,1,6),_Cat2600TsFwCRC_Type())
cat2600TsFwCRC.setMaxAccess(_B)
if mibBuilder.loadTexts:cat2600TsFwCRC.setStatus(_A)
class _Cat2600TsFwManufacturer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_Cat2600TsFwManufacturer_Type.__name__=_F
_Cat2600TsFwManufacturer_Object=MibScalar
cat2600TsFwManufacturer=_Cat2600TsFwManufacturer_Object((1,3,6,1,4,1,9,1,111,1,2,1,1,7),_Cat2600TsFwManufacturer_Type())
cat2600TsFwManufacturer.setMaxAccess(_B)
if mibBuilder.loadTexts:cat2600TsFwManufacturer.setStatus(_A)
_Cat2600TsIpAddr_Type=IpAddress
_Cat2600TsIpAddr_Object=MibScalar
cat2600TsIpAddr=_Cat2600TsIpAddr_Object((1,3,6,1,4,1,9,1,111,1,2,1,1,8),_Cat2600TsIpAddr_Type())
cat2600TsIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cat2600TsIpAddr.setStatus(_A)
_Cat2600TsNetMask_Type=IpAddress
_Cat2600TsNetMask_Object=MibScalar
cat2600TsNetMask=_Cat2600TsNetMask_Object((1,3,6,1,4,1,9,1,111,1,2,1,1,9),_Cat2600TsNetMask_Type())
cat2600TsNetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:cat2600TsNetMask.setStatus(_A)
_Cat2600TsDefaultGateway_Type=IpAddress
_Cat2600TsDefaultGateway_Object=MibScalar
cat2600TsDefaultGateway=_Cat2600TsDefaultGateway_Object((1,3,6,1,4,1,9,1,111,1,2,1,1,10),_Cat2600TsDefaultGateway_Type())
cat2600TsDefaultGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:cat2600TsDefaultGateway.setStatus(_A)
_Cat2600TsTrapRcvrTable_Object=MibTable
cat2600TsTrapRcvrTable=_Cat2600TsTrapRcvrTable_Object((1,3,6,1,4,1,9,1,111,1,2,1,1,14))
if mibBuilder.loadTexts:cat2600TsTrapRcvrTable.setStatus(_A)
_Cat2600TsTrapRcvrEntry_Object=MibTableRow
cat2600TsTrapRcvrEntry=_Cat2600TsTrapRcvrEntry_Object((1,3,6,1,4,1,9,1,111,1,2,1,1,14,1))
cat2600TsTrapRcvrEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:cat2600TsTrapRcvrEntry.setStatus(_A)
class _Cat2600TsTrapRcvrIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Cat2600TsTrapRcvrIndex_Type.__name__=_D
_Cat2600TsTrapRcvrIndex_Object=MibTableColumn
cat2600TsTrapRcvrIndex=_Cat2600TsTrapRcvrIndex_Object((1,3,6,1,4,1,9,1,111,1,2,1,1,14,1,1),_Cat2600TsTrapRcvrIndex_Type())
cat2600TsTrapRcvrIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cat2600TsTrapRcvrIndex.setStatus(_A)
class _Cat2600TsTrapRcvrStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_H,1),('valid',2),(_N,3),('create',4)))
_Cat2600TsTrapRcvrStatus_Type.__name__=_D
_Cat2600TsTrapRcvrStatus_Object=MibTableColumn
cat2600TsTrapRcvrStatus=_Cat2600TsTrapRcvrStatus_Object((1,3,6,1,4,1,9,1,111,1,2,1,1,14,1,2),_Cat2600TsTrapRcvrStatus_Type())
cat2600TsTrapRcvrStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cat2600TsTrapRcvrStatus.setStatus(_A)
_Cat2600TsTrapRcvrIpAddress_Type=IpAddress
_Cat2600TsTrapRcvrIpAddress_Object=MibTableColumn
cat2600TsTrapRcvrIpAddress=_Cat2600TsTrapRcvrIpAddress_Object((1,3,6,1,4,1,9,1,111,1,2,1,1,14,1,3),_Cat2600TsTrapRcvrIpAddress_Type())
cat2600TsTrapRcvrIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cat2600TsTrapRcvrIpAddress.setStatus(_A)
class _Cat2600TsTrapRcvrComm_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Cat2600TsTrapRcvrComm_Type.__name__=_F
_Cat2600TsTrapRcvrComm_Object=MibTableColumn
cat2600TsTrapRcvrComm=_Cat2600TsTrapRcvrComm_Object((1,3,6,1,4,1,9,1,111,1,2,1,1,14,1,4),_Cat2600TsTrapRcvrComm_Type())
cat2600TsTrapRcvrComm.setMaxAccess(_C)
if mibBuilder.loadTexts:cat2600TsTrapRcvrComm.setStatus(_A)
class _Cat2600TsTrapRcvrDmns_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_Cat2600TsTrapRcvrDmns_Type.__name__=_G
_Cat2600TsTrapRcvrDmns_Object=MibTableColumn
cat2600TsTrapRcvrDmns=_Cat2600TsTrapRcvrDmns_Object((1,3,6,1,4,1,9,1,111,1,2,1,1,14,1,5),_Cat2600TsTrapRcvrDmns_Type())
cat2600TsTrapRcvrDmns.setMaxAccess(_C)
if mibBuilder.loadTexts:cat2600TsTrapRcvrDmns.setStatus(_A)
class _Cat2600TsPingInterval_Type(Integer32):defaultValue=600
_Cat2600TsPingInterval_Type.__name__=_D
_Cat2600TsPingInterval_Object=MibScalar
cat2600TsPingInterval=_Cat2600TsPingInterval_Object((1,3,6,1,4,1,9,1,111,1,2,1,1,19),_Cat2600TsPingInterval_Type())
cat2600TsPingInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:cat2600TsPingInterval.setStatus(_A)
_Cat2600TsTapPort_Type=Integer32
_Cat2600TsTapPort_Object=MibScalar
cat2600TsTapPort=_Cat2600TsTapPort_Object((1,3,6,1,4,1,9,1,111,1,2,1,1,20),_Cat2600TsTapPort_Type())
cat2600TsTapPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cat2600TsTapPort.setStatus(_A)
_Cat2600TsTapMonitoredPort_Type=Integer32
_Cat2600TsTapMonitoredPort_Object=MibScalar
cat2600TsTapMonitoredPort=_Cat2600TsTapMonitoredPort_Object((1,3,6,1,4,1,9,1,111,1,2,1,1,21),_Cat2600TsTapMonitoredPort_Type())
cat2600TsTapMonitoredPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cat2600TsTapMonitoredPort.setStatus(_A)
_Cat2600TsCrcThresholdHi_Type=Integer32
_Cat2600TsCrcThresholdHi_Object=MibScalar
cat2600TsCrcThresholdHi=_Cat2600TsCrcThresholdHi_Object((1,3,6,1,4,1,9,1,111,1,2,1,1,22),_Cat2600TsCrcThresholdHi_Type())
cat2600TsCrcThresholdHi.setMaxAccess(_C)
if mibBuilder.loadTexts:cat2600TsCrcThresholdHi.setStatus(_A)
_Cat2600TsCrcThresholdLow_Type=Integer32
_Cat2600TsCrcThresholdLow_Object=MibScalar
cat2600TsCrcThresholdLow=_Cat2600TsCrcThresholdLow_Object((1,3,6,1,4,1,9,1,111,1,2,1,1,23),_Cat2600TsCrcThresholdLow_Type())
cat2600TsCrcThresholdLow.setMaxAccess(_C)
if mibBuilder.loadTexts:cat2600TsCrcThresholdLow.setStatus(_A)
class _Cat2600TsPortSwitchModeChangeTrapEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_Cat2600TsPortSwitchModeChangeTrapEnable_Type.__name__=_D
_Cat2600TsPortSwitchModeChangeTrapEnable_Object=MibScalar
cat2600TsPortSwitchModeChangeTrapEnable=_Cat2600TsPortSwitchModeChangeTrapEnable_Object((1,3,6,1,4,1,9,1,111,1,2,1,1,24),_Cat2600TsPortSwitchModeChangeTrapEnable_Type())
cat2600TsPortSwitchModeChangeTrapEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:cat2600TsPortSwitchModeChangeTrapEnable.setStatus(_A)
_Cat2600TsTrendThreshold_Type=Integer32
_Cat2600TsTrendThreshold_Object=MibScalar
cat2600TsTrendThreshold=_Cat2600TsTrendThreshold_Object((1,3,6,1,4,1,9,1,111,1,2,1,1,25),_Cat2600TsTrendThreshold_Type())
cat2600TsTrendThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:cat2600TsTrendThreshold.setStatus(_A)
class _Cat2600TsSamplingPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,120))
_Cat2600TsSamplingPeriod_Type.__name__=_D
_Cat2600TsSamplingPeriod_Object=MibScalar
cat2600TsSamplingPeriod=_Cat2600TsSamplingPeriod_Object((1,3,6,1,4,1,9,1,111,1,2,1,1,26),_Cat2600TsSamplingPeriod_Type())
cat2600TsSamplingPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:cat2600TsSamplingPeriod.setStatus(_A)
_Cat2600TsNumberUFC_Type=Integer32
_Cat2600TsNumberUFC_Object=MibScalar
cat2600TsNumberUFC=_Cat2600TsNumberUFC_Object((1,3,6,1,4,1,9,1,111,1,2,1,1,27),_Cat2600TsNumberUFC_Type())
cat2600TsNumberUFC.setMaxAccess(_B)
if mibBuilder.loadTexts:cat2600TsNumberUFC.setStatus(_A)
_Cat2600TsSys_ObjectIdentity=ObjectIdentity
cat2600TsSys=_Cat2600TsSys_ObjectIdentity((1,3,6,1,4,1,9,1,111,1,2,1,2))
_Cat2600TsNumPorts_Type=Integer32
_Cat2600TsNumPorts_Object=MibScalar
cat2600TsNumPorts=_Cat2600TsNumPorts_Object((1,3,6,1,4,1,9,1,111,1,2,1,2,1),_Cat2600TsNumPorts_Type())
cat2600TsNumPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:cat2600TsNumPorts.setStatus(_A)
_Cat2600TsNumStations_Type=Integer32
_Cat2600TsNumStations_Object=MibScalar
cat2600TsNumStations=_Cat2600TsNumStations_Object((1,3,6,1,4,1,9,1,111,1,2,1,2,2),_Cat2600TsNumStations_Type())
cat2600TsNumStations.setMaxAccess(_B)
if mibBuilder.loadTexts:cat2600TsNumStations.setStatus(_A)
_Cat2600TsMostStations_Type=Integer32
_Cat2600TsMostStations_Object=MibScalar
cat2600TsMostStations=_Cat2600TsMostStations_Object((1,3,6,1,4,1,9,1,111,1,2,1,2,3),_Cat2600TsMostStations_Type())
cat2600TsMostStations.setMaxAccess(_B)
if mibBuilder.loadTexts:cat2600TsMostStations.setStatus(_A)
_Cat2600TsMaxStations_Type=Integer32
_Cat2600TsMaxStations_Object=MibScalar
cat2600TsMaxStations=_Cat2600TsMaxStations_Object((1,3,6,1,4,1,9,1,111,1,2,1,2,4),_Cat2600TsMaxStations_Type())
cat2600TsMaxStations.setMaxAccess(_B)
if mibBuilder.loadTexts:cat2600TsMaxStations.setStatus(_A)
class _Cat2600TsReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_O,2),(_P,3)))
_Cat2600TsReset_Type.__name__=_D
_Cat2600TsReset_Object=MibScalar
cat2600TsReset=_Cat2600TsReset_Object((1,3,6,1,4,1,9,1,111,1,2,1,2,5),_Cat2600TsReset_Type())
cat2600TsReset.setMaxAccess(_C)
if mibBuilder.loadTexts:cat2600TsReset.setStatus(_A)
_Cat2600TsNumResets_Type=Counter32
_Cat2600TsNumResets_Object=MibScalar
cat2600TsNumResets=_Cat2600TsNumResets_Object((1,3,6,1,4,1,9,1,111,1,2,1,2,6),_Cat2600TsNumResets_Type())
cat2600TsNumResets.setMaxAccess(_B)
if mibBuilder.loadTexts:cat2600TsNumResets.setStatus(_A)
class _Cat2600TsAddrAgingTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9999))
_Cat2600TsAddrAgingTime_Type.__name__=_D
_Cat2600TsAddrAgingTime_Object=MibScalar
cat2600TsAddrAgingTime=_Cat2600TsAddrAgingTime_Object((1,3,6,1,4,1,9,1,111,1,2,1,2,7),_Cat2600TsAddrAgingTime_Type())
cat2600TsAddrAgingTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cat2600TsAddrAgingTime.setStatus(_A)
class _Cat2600TsSysTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('normal',1),('toohigh',2)))
_Cat2600TsSysTemperature_Type.__name__=_D
_Cat2600TsSysTemperature_Object=MibScalar
cat2600TsSysTemperature=_Cat2600TsSysTemperature_Object((1,3,6,1,4,1,9,1,111,1,2,1,2,11),_Cat2600TsSysTemperature_Type())
cat2600TsSysTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:cat2600TsSysTemperature.setStatus(_A)
_Cat2600TsInstalledMemory_Type=Integer32
_Cat2600TsInstalledMemory_Object=MibScalar
cat2600TsInstalledMemory=_Cat2600TsInstalledMemory_Object((1,3,6,1,4,1,9,1,111,1,2,1,2,12),_Cat2600TsInstalledMemory_Type())
cat2600TsInstalledMemory.setMaxAccess(_B)
if mibBuilder.loadTexts:cat2600TsInstalledMemory.setStatus(_A)
class _Cat2600TsSysCurTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_Cat2600TsSysCurTime_Type.__name__=_F
_Cat2600TsSysCurTime_Object=MibScalar
cat2600TsSysCurTime=_Cat2600TsSysCurTime_Object((1,3,6,1,4,1,9,1,111,1,2,1,2,13),_Cat2600TsSysCurTime_Type())
cat2600TsSysCurTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cat2600TsSysCurTime.setStatus(_A)
_Cat2600TsPort_ObjectIdentity=ObjectIdentity
cat2600TsPort=_Cat2600TsPort_ObjectIdentity((1,3,6,1,4,1,9,1,111,1,2,2))
_Cat2600TsPortTable_Object=MibTable
cat2600TsPortTable=_Cat2600TsPortTable_Object((1,3,6,1,4,1,9,1,111,1,2,2,1))
if mibBuilder.loadTexts:cat2600TsPortTable.setStatus(_A)
_Cat2600TsPortEntry_Object=MibTableRow
cat2600TsPortEntry=_Cat2600TsPortEntry_Object((1,3,6,1,4,1,9,1,111,1,2,2,1,1))
cat2600TsPortEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:cat2600TsPortEntry.setStatus(_A)
class _Cat2600TsPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Cat2600TsPortIndex_Type.__name__=_D
_Cat2600TsPortIndex_Object=MibTableColumn
cat2600TsPortIndex=_Cat2600TsPortIndex_Object((1,3,6,1,4,1,9,1,111,1,2,2,1,1,1),_Cat2600TsPortIndex_Type())
cat2600TsPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cat2600TsPortIndex.setStatus(_A)
_Cat2600TsPortRcvLocalFrames_Type=Counter32
_Cat2600TsPortRcvLocalFrames_Object=MibTableColumn
cat2600TsPortRcvLocalFrames=_Cat2600TsPortRcvLocalFrames_Object((1,3,6,1,4,1,9,1,111,1,2,2,1,1,2),_Cat2600TsPortRcvLocalFrames_Type())
cat2600TsPortRcvLocalFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:cat2600TsPortRcvLocalFrames.setStatus(_A)
_Cat2600TsPortForwardedFrames_Type=Counter32
_Cat2600TsPortForwardedFrames_Object=MibTableColumn
cat2600TsPortForwardedFrames=_Cat2600TsPortForwardedFrames_Object((1,3,6,1,4,1,9,1,111,1,2,2,1,1,3),_Cat2600TsPortForwardedFrames_Type())
cat2600TsPortForwardedFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:cat2600TsPortForwardedFrames.setStatus(_A)
_Cat2600TsPortMostStations_Type=Counter32
_Cat2600TsPortMostStations_Object=MibTableColumn
cat2600TsPortMostStations=_Cat2600TsPortMostStations_Object((1,3,6,1,4,1,9,1,111,1,2,2,1,1,4),_Cat2600TsPortMostStations_Type())
cat2600TsPortMostStations.setMaxAccess(_B)
if mibBuilder.loadTexts:cat2600TsPortMostStations.setStatus(_A)
_Cat2600TsPortMaxStations_Type=Counter32
_Cat2600TsPortMaxStations_Object=MibTableColumn
cat2600TsPortMaxStations=_Cat2600TsPortMaxStations_Object((1,3,6,1,4,1,9,1,111,1,2,2,1,1,5),_Cat2600TsPortMaxStations_Type())
cat2600TsPortMaxStations.setMaxAccess(_B)
if mibBuilder.loadTexts:cat2600TsPortMaxStations.setStatus(_A)
_Cat2600TsPortSWHandledFrames_Type=Counter32
_Cat2600TsPortSWHandledFrames_Object=MibTableColumn
cat2600TsPortSWHandledFrames=_Cat2600TsPortSWHandledFrames_Object((1,3,6,1,4,1,9,1,111,1,2,2,1,1,6),_Cat2600TsPortSWHandledFrames_Type())
cat2600TsPortSWHandledFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:cat2600TsPortSWHandledFrames.setStatus(_A)
_Cat2600TsPortLocalStations_Type=Counter32
_Cat2600TsPortLocalStations_Object=MibTableColumn
cat2600TsPortLocalStations=_Cat2600TsPortLocalStations_Object((1,3,6,1,4,1,9,1,111,1,2,2,1,1,7),_Cat2600TsPortLocalStations_Type())
cat2600TsPortLocalStations.setMaxAccess(_B)
if mibBuilder.loadTexts:cat2600TsPortLocalStations.setStatus(_A)
_Cat2600TsPortRemoteStations_Type=Counter32
_Cat2600TsPortRemoteStations_Object=MibTableColumn
cat2600TsPortRemoteStations=_Cat2600TsPortRemoteStations_Object((1,3,6,1,4,1,9,1,111,1,2,2,1,1,8),_Cat2600TsPortRemoteStations_Type())
cat2600TsPortRemoteStations.setMaxAccess(_B)
if mibBuilder.loadTexts:cat2600TsPortRemoteStations.setStatus(_A)
_Cat2600TsPortUnknownStaFrames_Type=Counter32
_Cat2600TsPortUnknownStaFrames_Object=MibTableColumn
cat2600TsPortUnknownStaFrames=_Cat2600TsPortUnknownStaFrames_Object((1,3,6,1,4,1,9,1,111,1,2,2,1,1,9),_Cat2600TsPortUnknownStaFrames_Type())
cat2600TsPortUnknownStaFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:cat2600TsPortUnknownStaFrames.setStatus(_A)
class _Cat2600TsPortResetStats_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_I,2),('reset',3)))
_Cat2600TsPortResetStats_Type.__name__=_D
_Cat2600TsPortResetStats_Object=MibTableColumn
cat2600TsPortResetStats=_Cat2600TsPortResetStats_Object((1,3,6,1,4,1,9,1,111,1,2,2,1,1,10),_Cat2600TsPortResetStats_Type())
cat2600TsPortResetStats.setMaxAccess(_C)
if mibBuilder.loadTexts:cat2600TsPortResetStats.setStatus(_A)
_Cat2600TsPortResetTimer_Type=TimeTicks
_Cat2600TsPortResetTimer_Object=MibTableColumn
cat2600TsPortResetTimer=_Cat2600TsPortResetTimer_Object((1,3,6,1,4,1,9,1,111,1,2,2,1,1,11),_Cat2600TsPortResetTimer_Type())
cat2600TsPortResetTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:cat2600TsPortResetTimer.setStatus(_A)
class _Cat2600TsPortResetAddrs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_I,2),('reset',3)))
_Cat2600TsPortResetAddrs_Type.__name__=_D
_Cat2600TsPortResetAddrs_Object=MibTableColumn
cat2600TsPortResetAddrs=_Cat2600TsPortResetAddrs_Object((1,3,6,1,4,1,9,1,111,1,2,2,1,1,12),_Cat2600TsPortResetAddrs_Type())
cat2600TsPortResetAddrs.setMaxAccess(_C)
if mibBuilder.loadTexts:cat2600TsPortResetAddrs.setStatus(_A)
_Cat2600TsPortRcvBcasts_Type=Counter32
_Cat2600TsPortRcvBcasts_Object=MibTableColumn
cat2600TsPortRcvBcasts=_Cat2600TsPortRcvBcasts_Object((1,3,6,1,4,1,9,1,111,1,2,2,1,1,13),_Cat2600TsPortRcvBcasts_Type())
cat2600TsPortRcvBcasts.setMaxAccess(_B)
if mibBuilder.loadTexts:cat2600TsPortRcvBcasts.setStatus(_A)
_Cat2600TsPortSwitchedFrames_Type=Counter32
_Cat2600TsPortSwitchedFrames_Object=MibTableColumn
cat2600TsPortSwitchedFrames=_Cat2600TsPortSwitchedFrames_Object((1,3,6,1,4,1,9,1,111,1,2,2,1,1,14),_Cat2600TsPortSwitchedFrames_Type())
cat2600TsPortSwitchedFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:cat2600TsPortSwitchedFrames.setStatus(_A)
class _Cat2600TsPortLinkState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_Cat2600TsPortLinkState_Type.__name__=_D
_Cat2600TsPortLinkState_Object=MibTableColumn
cat2600TsPortLinkState=_Cat2600TsPortLinkState_Object((1,3,6,1,4,1,9,1,111,1,2,2,1,1,15),_Cat2600TsPortLinkState_Type())
cat2600TsPortLinkState.setMaxAccess(_B)
if mibBuilder.loadTexts:cat2600TsPortLinkState.setStatus(_A)
_Cat2600TsPortHashOverflows_Type=Counter32
_Cat2600TsPortHashOverflows_Object=MibTableColumn
cat2600TsPortHashOverflows=_Cat2600TsPortHashOverflows_Object((1,3,6,1,4,1,9,1,111,1,2,2,1,1,16),_Cat2600TsPortHashOverflows_Type())
cat2600TsPortHashOverflows.setMaxAccess(_B)
if mibBuilder.loadTexts:cat2600TsPortHashOverflows.setStatus(_A)
_Cat2600TsPortAddrAgingTime_Type=Integer32
_Cat2600TsPortAddrAgingTime_Object=MibTableColumn
cat2600TsPortAddrAgingTime=_Cat2600TsPortAddrAgingTime_Object((1,3,6,1,4,1,9,1,111,1,2,2,1,1,17),_Cat2600TsPortAddrAgingTime_Type())
cat2600TsPortAddrAgingTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cat2600TsPortAddrAgingTime.setStatus(_A)
class _Cat2600TsPortSwitchMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('storeandforward',1),('cutthru',2),('auto',3)))
_Cat2600TsPortSwitchMode_Type.__name__=_D
_Cat2600TsPortSwitchMode_Object=MibTableColumn
cat2600TsPortSwitchMode=_Cat2600TsPortSwitchMode_Object((1,3,6,1,4,1,9,1,111,1,2,2,1,1,18),_Cat2600TsPortSwitchMode_Type())
cat2600TsPortSwitchMode.setMaxAccess(_C)
if mibBuilder.loadTexts:cat2600TsPortSwitchMode.setStatus(_A)
class _Cat2600TsPortFixedCfg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('auto-detect',1),('fixed',2)))
_Cat2600TsPortFixedCfg_Type.__name__=_D
_Cat2600TsPortFixedCfg_Object=MibTableColumn
cat2600TsPortFixedCfg=_Cat2600TsPortFixedCfg_Object((1,3,6,1,4,1,9,1,111,1,2,2,1,1,19),_Cat2600TsPortFixedCfg_Type())
cat2600TsPortFixedCfg.setMaxAccess(_C)
if mibBuilder.loadTexts:cat2600TsPortFixedCfg.setStatus(_A)
class _Cat2600TsPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('adapter',1),('port',2)))
_Cat2600TsPortMode_Type.__name__=_D
_Cat2600TsPortMode_Object=MibTableColumn
cat2600TsPortMode=_Cat2600TsPortMode_Object((1,3,6,1,4,1,9,1,111,1,2,2,1,1,20),_Cat2600TsPortMode_Type())
cat2600TsPortMode.setMaxAccess(_C)
if mibBuilder.loadTexts:cat2600TsPortMode.setStatus(_A)
class _Cat2600TsPortDuplex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('half-duplex',1),('full-duplex',2)))
_Cat2600TsPortDuplex_Type.__name__=_D
_Cat2600TsPortDuplex_Object=MibTableColumn
cat2600TsPortDuplex=_Cat2600TsPortDuplex_Object((1,3,6,1,4,1,9,1,111,1,2,2,1,1,21),_Cat2600TsPortDuplex_Type())
cat2600TsPortDuplex.setMaxAccess(_C)
if mibBuilder.loadTexts:cat2600TsPortDuplex.setStatus(_A)
_Cat2600TsPortCfgLoss_Type=Integer32
_Cat2600TsPortCfgLoss_Object=MibTableColumn
cat2600TsPortCfgLoss=_Cat2600TsPortCfgLoss_Object((1,3,6,1,4,1,9,1,111,1,2,2,1,1,22),_Cat2600TsPortCfgLoss_Type())
cat2600TsPortCfgLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:cat2600TsPortCfgLoss.setStatus(_A)
class _Cat2600TsPortCfgLossRC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('wire-fault',1),('beacon-auto-removal',2),('force-remove-macaddr',3),('connection-lost',4),('adapter-check',5),('close-srb',6),('fdx-protocol-failure',7)))
_Cat2600TsPortCfgLossRC_Type.__name__=_D
_Cat2600TsPortCfgLossRC_Object=MibTableColumn
cat2600TsPortCfgLossRC=_Cat2600TsPortCfgLossRC_Object((1,3,6,1,4,1,9,1,111,1,2,2,1,1,23),_Cat2600TsPortCfgLossRC_Type())
cat2600TsPortCfgLossRC.setMaxAccess(_B)
if mibBuilder.loadTexts:cat2600TsPortCfgLossRC.setStatus(_A)
_Cat2600TsPortCRCCount_Type=Counter32
_Cat2600TsPortCRCCount_Object=MibTableColumn
cat2600TsPortCRCCount=_Cat2600TsPortCRCCount_Object((1,3,6,1,4,1,9,1,111,1,2,2,1,1,24),_Cat2600TsPortCRCCount_Type())
cat2600TsPortCRCCount.setMaxAccess(_B)
if mibBuilder.loadTexts:cat2600TsPortCRCCount.setStatus(_A)
_Cat2600TsPortHPChannelFrames_Type=Counter32
_Cat2600TsPortHPChannelFrames_Object=MibTableColumn
cat2600TsPortHPChannelFrames=_Cat2600TsPortHPChannelFrames_Object((1,3,6,1,4,1,9,1,111,1,2,2,1,1,25),_Cat2600TsPortHPChannelFrames_Type())
cat2600TsPortHPChannelFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:cat2600TsPortHPChannelFrames.setStatus(_A)
_Cat2600TsPortLPChannelFrames_Type=Counter32
_Cat2600TsPortLPChannelFrames_Object=MibTableColumn
cat2600TsPortLPChannelFrames=_Cat2600TsPortLPChannelFrames_Object((1,3,6,1,4,1,9,1,111,1,2,2,1,1,26),_Cat2600TsPortLPChannelFrames_Type())
cat2600TsPortLPChannelFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:cat2600TsPortLPChannelFrames.setStatus(_A)
class _Cat2600TsPortHPThreshold_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,6))
_Cat2600TsPortHPThreshold_Type.__name__=_D
_Cat2600TsPortHPThreshold_Object=MibTableColumn
cat2600TsPortHPThreshold=_Cat2600TsPortHPThreshold_Object((1,3,6,1,4,1,9,1,111,1,2,2,1,1,27),_Cat2600TsPortHPThreshold_Type())
cat2600TsPortHPThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:cat2600TsPortHPThreshold.setStatus(_A)
class _Cat2600TsPortCfgRingSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('speed-16megabit',1),('speed-4megabit',2)))
_Cat2600TsPortCfgRingSpeed_Type.__name__=_D
_Cat2600TsPortCfgRingSpeed_Object=MibTableColumn
cat2600TsPortCfgRingSpeed=_Cat2600TsPortCfgRingSpeed_Object((1,3,6,1,4,1,9,1,111,1,2,2,1,1,28),_Cat2600TsPortCfgRingSpeed_Type())
cat2600TsPortCfgRingSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:cat2600TsPortCfgRingSpeed.setStatus(_A)
class _Cat2600TsPortCfgRSA_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('rsa',1),('fixed',2)))
_Cat2600TsPortCfgRSA_Type.__name__=_D
_Cat2600TsPortCfgRSA_Object=MibTableColumn
cat2600TsPortCfgRSA=_Cat2600TsPortCfgRSA_Object((1,3,6,1,4,1,9,1,111,1,2,2,1,1,29),_Cat2600TsPortCfgRSA_Type())
cat2600TsPortCfgRSA.setMaxAccess(_C)
if mibBuilder.loadTexts:cat2600TsPortCfgRSA.setStatus(_A)
_Cat2600TsPortDomain_Type=Integer32
_Cat2600TsPortDomain_Object=MibTableColumn
cat2600TsPortDomain=_Cat2600TsPortDomain_Object((1,3,6,1,4,1,9,1,111,1,2,2,1,1,30),_Cat2600TsPortDomain_Type())
cat2600TsPortDomain.setMaxAccess(_B)
if mibBuilder.loadTexts:cat2600TsPortDomain.setStatus(_A)
_Cat2600TsPortCfgLossThreshold_Type=Integer32
_Cat2600TsPortCfgLossThreshold_Object=MibTableColumn
cat2600TsPortCfgLossThreshold=_Cat2600TsPortCfgLossThreshold_Object((1,3,6,1,4,1,9,1,111,1,2,2,1,1,31),_Cat2600TsPortCfgLossThreshold_Type())
cat2600TsPortCfgLossThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:cat2600TsPortCfgLossThreshold.setStatus(_A)
_Cat2600TsPortCfgLossSamplingPeriod_Type=Integer32
_Cat2600TsPortCfgLossSamplingPeriod_Object=MibTableColumn
cat2600TsPortCfgLossSamplingPeriod=_Cat2600TsPortCfgLossSamplingPeriod_Object((1,3,6,1,4,1,9,1,111,1,2,2,1,1,32),_Cat2600TsPortCfgLossSamplingPeriod_Type())
cat2600TsPortCfgLossSamplingPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:cat2600TsPortCfgLossSamplingPeriod.setStatus(_A)
_Cat2600TsPortBeaconStationAddress_Type=MacAddr
_Cat2600TsPortBeaconStationAddress_Object=MibTableColumn
cat2600TsPortBeaconStationAddress=_Cat2600TsPortBeaconStationAddress_Object((1,3,6,1,4,1,9,1,111,1,2,2,1,1,33),_Cat2600TsPortBeaconStationAddress_Type())
cat2600TsPortBeaconStationAddress.setMaxAccess(_K)
if mibBuilder.loadTexts:cat2600TsPortBeaconStationAddress.setStatus(_A)
_Cat2600TsPortBeaconNAUN_Type=MacAddr
_Cat2600TsPortBeaconNAUN_Object=MibTableColumn
cat2600TsPortBeaconNAUN=_Cat2600TsPortBeaconNAUN_Object((1,3,6,1,4,1,9,1,111,1,2,2,1,1,34),_Cat2600TsPortBeaconNAUN_Type())
cat2600TsPortBeaconNAUN.setMaxAccess(_K)
if mibBuilder.loadTexts:cat2600TsPortBeaconNAUN.setStatus(_A)
_Cat2600TsPortBeaconType_Type=Integer32
_Cat2600TsPortBeaconType_Object=MibTableColumn
cat2600TsPortBeaconType=_Cat2600TsPortBeaconType_Object((1,3,6,1,4,1,9,1,111,1,2,2,1,1,35),_Cat2600TsPortBeaconType_Type())
cat2600TsPortBeaconType.setMaxAccess(_K)
if mibBuilder.loadTexts:cat2600TsPortBeaconType.setStatus(_A)
_Cat2600TsOptPortStaTable_Object=MibTable
cat2600TsOptPortStaTable=_Cat2600TsOptPortStaTable_Object((1,3,6,1,4,1,9,1,111,1,2,2,2))
if mibBuilder.loadTexts:cat2600TsOptPortStaTable.setStatus(_A)
_Cat2600TsOptPortStaEntry_Object=MibTableRow
cat2600TsOptPortStaEntry=_Cat2600TsOptPortStaEntry_Object((1,3,6,1,4,1,9,1,111,1,2,2,2,1))
cat2600TsOptPortStaEntry.setIndexNames((0,_E,_J),(0,_E,_Q))
if mibBuilder.loadTexts:cat2600TsOptPortStaEntry.setStatus(_A)
class _Cat2600TsOptPortStaPos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Cat2600TsOptPortStaPos_Type.__name__=_D
_Cat2600TsOptPortStaPos_Object=MibTableColumn
cat2600TsOptPortStaPos=_Cat2600TsOptPortStaPos_Object((1,3,6,1,4,1,9,1,111,1,2,2,2,1,1),_Cat2600TsOptPortStaPos_Type())
cat2600TsOptPortStaPos.setMaxAccess(_B)
if mibBuilder.loadTexts:cat2600TsOptPortStaPos.setStatus(_A)
_Cat2600TsOptPortStaVal_Type=OctetString
_Cat2600TsOptPortStaVal_Object=MibTableColumn
cat2600TsOptPortStaVal=_Cat2600TsOptPortStaVal_Object((1,3,6,1,4,1,9,1,111,1,2,2,2,1,2),_Cat2600TsOptPortStaVal_Type())
cat2600TsOptPortStaVal.setMaxAccess(_B)
if mibBuilder.loadTexts:cat2600TsOptPortStaVal.setStatus(_A)
_Cat2600TsPortStnTable_Object=MibTable
cat2600TsPortStnTable=_Cat2600TsPortStnTable_Object((1,3,6,1,4,1,9,1,111,1,2,2,3))
if mibBuilder.loadTexts:cat2600TsPortStnTable.setStatus(_A)
_Cat2600TsPortStnEntry_Object=MibTableRow
cat2600TsPortStnEntry=_Cat2600TsPortStnEntry_Object((1,3,6,1,4,1,9,1,111,1,2,2,3,1))
cat2600TsPortStnEntry.setIndexNames((0,_E,_R),(0,_E,_S))
if mibBuilder.loadTexts:cat2600TsPortStnEntry.setStatus(_A)
_Cat2600TsPortStnPortNum_Type=Integer32
_Cat2600TsPortStnPortNum_Object=MibTableColumn
cat2600TsPortStnPortNum=_Cat2600TsPortStnPortNum_Object((1,3,6,1,4,1,9,1,111,1,2,2,3,1,1),_Cat2600TsPortStnPortNum_Type())
cat2600TsPortStnPortNum.setMaxAccess(_B)
if mibBuilder.loadTexts:cat2600TsPortStnPortNum.setStatus(_A)
_Cat2600TsPortStnAddress_Type=MacAddr
_Cat2600TsPortStnAddress_Object=MibTableColumn
cat2600TsPortStnAddress=_Cat2600TsPortStnAddress_Object((1,3,6,1,4,1,9,1,111,1,2,2,3,1,2),_Cat2600TsPortStnAddress_Type())
cat2600TsPortStnAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:cat2600TsPortStnAddress.setStatus(_A)
class _Cat2600TsPortStnLocation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('local',1),('remote',2)))
_Cat2600TsPortStnLocation_Type.__name__=_D
_Cat2600TsPortStnLocation_Object=MibTableColumn
cat2600TsPortStnLocation=_Cat2600TsPortStnLocation_Object((1,3,6,1,4,1,9,1,111,1,2,2,3,1,3),_Cat2600TsPortStnLocation_Type())
cat2600TsPortStnLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:cat2600TsPortStnLocation.setStatus(_A)
_Cat2600TsPortStnSrcFrames_Type=Counter32
_Cat2600TsPortStnSrcFrames_Object=MibTableColumn
cat2600TsPortStnSrcFrames=_Cat2600TsPortStnSrcFrames_Object((1,3,6,1,4,1,9,1,111,1,2,2,3,1,4),_Cat2600TsPortStnSrcFrames_Type())
cat2600TsPortStnSrcFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:cat2600TsPortStnSrcFrames.setStatus(_A)
_Cat2600TsPortStnSrcBytes_Type=Counter32
_Cat2600TsPortStnSrcBytes_Object=MibTableColumn
cat2600TsPortStnSrcBytes=_Cat2600TsPortStnSrcBytes_Object((1,3,6,1,4,1,9,1,111,1,2,2,3,1,5),_Cat2600TsPortStnSrcBytes_Type())
cat2600TsPortStnSrcBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:cat2600TsPortStnSrcBytes.setStatus(_A)
_Cat2600TsPortStnDestnFrames_Type=Counter32
_Cat2600TsPortStnDestnFrames_Object=MibTableColumn
cat2600TsPortStnDestnFrames=_Cat2600TsPortStnDestnFrames_Object((1,3,6,1,4,1,9,1,111,1,2,2,3,1,6),_Cat2600TsPortStnDestnFrames_Type())
cat2600TsPortStnDestnFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:cat2600TsPortStnDestnFrames.setStatus(_A)
_Cat2600TsPortStnDestnBytes_Type=Counter32
_Cat2600TsPortStnDestnBytes_Object=MibTableColumn
cat2600TsPortStnDestnBytes=_Cat2600TsPortStnDestnBytes_Object((1,3,6,1,4,1,9,1,111,1,2,2,3,1,7),_Cat2600TsPortStnDestnBytes_Type())
cat2600TsPortStnDestnBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:cat2600TsPortStnDestnBytes.setStatus(_A)
_Cat2600TsDmns_ObjectIdentity=ObjectIdentity
cat2600TsDmns=_Cat2600TsDmns_ObjectIdentity((1,3,6,1,4,1,9,1,111,1,2,3))
_Cat2600TsDmnTable_Object=MibTable
cat2600TsDmnTable=_Cat2600TsDmnTable_Object((1,3,6,1,4,1,9,1,111,1,2,3,1))
if mibBuilder.loadTexts:cat2600TsDmnTable.setStatus(_A)
_Cat2600TsDmnEntry_Object=MibTableRow
cat2600TsDmnEntry=_Cat2600TsDmnEntry_Object((1,3,6,1,4,1,9,1,111,1,2,3,1,1))
cat2600TsDmnEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:cat2600TsDmnEntry.setStatus(_A)
class _Cat2600TsDmnIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_Cat2600TsDmnIndex_Type.__name__=_D
_Cat2600TsDmnIndex_Object=MibTableColumn
cat2600TsDmnIndex=_Cat2600TsDmnIndex_Object((1,3,6,1,4,1,9,1,111,1,2,3,1,1,1),_Cat2600TsDmnIndex_Type())
cat2600TsDmnIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cat2600TsDmnIndex.setStatus(_A)
_Cat2600TsDmnPorts_Type=OctetString
_Cat2600TsDmnPorts_Object=MibTableColumn
cat2600TsDmnPorts=_Cat2600TsDmnPorts_Object((1,3,6,1,4,1,9,1,111,1,2,3,1,1,2),_Cat2600TsDmnPorts_Type())
cat2600TsDmnPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:cat2600TsDmnPorts.setStatus(_A)
class _Cat2600TsDmnIpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('disabled',1),('auto-bootp',2),('always-bootp',3)))
_Cat2600TsDmnIpState_Type.__name__=_D
_Cat2600TsDmnIpState_Object=MibTableColumn
cat2600TsDmnIpState=_Cat2600TsDmnIpState_Object((1,3,6,1,4,1,9,1,111,1,2,3,1,1,3),_Cat2600TsDmnIpState_Type())
cat2600TsDmnIpState.setMaxAccess(_C)
if mibBuilder.loadTexts:cat2600TsDmnIpState.setStatus(_A)
_Cat2600TsDmnIpAddress_Type=IpAddress
_Cat2600TsDmnIpAddress_Object=MibTableColumn
cat2600TsDmnIpAddress=_Cat2600TsDmnIpAddress_Object((1,3,6,1,4,1,9,1,111,1,2,3,1,1,4),_Cat2600TsDmnIpAddress_Type())
cat2600TsDmnIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cat2600TsDmnIpAddress.setStatus(_A)
_Cat2600TsDmnIpSubnetMask_Type=IpAddress
_Cat2600TsDmnIpSubnetMask_Object=MibTableColumn
cat2600TsDmnIpSubnetMask=_Cat2600TsDmnIpSubnetMask_Object((1,3,6,1,4,1,9,1,111,1,2,3,1,1,5),_Cat2600TsDmnIpSubnetMask_Type())
cat2600TsDmnIpSubnetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:cat2600TsDmnIpSubnetMask.setStatus(_A)
_Cat2600TsDmnIpDefaultGateway_Type=IpAddress
_Cat2600TsDmnIpDefaultGateway_Object=MibTableColumn
cat2600TsDmnIpDefaultGateway=_Cat2600TsDmnIpDefaultGateway_Object((1,3,6,1,4,1,9,1,111,1,2,3,1,1,6),_Cat2600TsDmnIpDefaultGateway_Type())
cat2600TsDmnIpDefaultGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:cat2600TsDmnIpDefaultGateway.setStatus(_A)
class _Cat2600TsDmnStp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_Cat2600TsDmnStp_Type.__name__=_D
_Cat2600TsDmnStp_Object=MibTableColumn
cat2600TsDmnStp=_Cat2600TsDmnStp_Object((1,3,6,1,4,1,9,1,111,1,2,3,1,1,7),_Cat2600TsDmnStp_Type())
cat2600TsDmnStp.setMaxAccess(_C)
if mibBuilder.loadTexts:cat2600TsDmnStp.setStatus(_A)
class _Cat2600TsDmnName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,48))
_Cat2600TsDmnName_Type.__name__=_F
_Cat2600TsDmnName_Object=MibTableColumn
cat2600TsDmnName=_Cat2600TsDmnName_Object((1,3,6,1,4,1,9,1,111,1,2,3,1,1,8),_Cat2600TsDmnName_Type())
cat2600TsDmnName.setMaxAccess(_C)
if mibBuilder.loadTexts:cat2600TsDmnName.setStatus(_A)
class _Cat2600TsDmnIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_Cat2600TsDmnIfIndex_Type.__name__=_D
_Cat2600TsDmnIfIndex_Object=MibTableColumn
cat2600TsDmnIfIndex=_Cat2600TsDmnIfIndex_Object((1,3,6,1,4,1,9,1,111,1,2,3,1,1,9),_Cat2600TsDmnIfIndex_Type())
cat2600TsDmnIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cat2600TsDmnIfIndex.setStatus(_A)
_Cat2600TsDmnBaseBridgeAddr_Type=MacAddr
_Cat2600TsDmnBaseBridgeAddr_Object=MibTableColumn
cat2600TsDmnBaseBridgeAddr=_Cat2600TsDmnBaseBridgeAddr_Object((1,3,6,1,4,1,9,1,111,1,2,3,1,1,10),_Cat2600TsDmnBaseBridgeAddr_Type())
cat2600TsDmnBaseBridgeAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cat2600TsDmnBaseBridgeAddr.setStatus(_A)
_Cat2600TsDmnNumStations_Type=Integer32
_Cat2600TsDmnNumStations_Object=MibTableColumn
cat2600TsDmnNumStations=_Cat2600TsDmnNumStations_Object((1,3,6,1,4,1,9,1,111,1,2,3,1,1,11),_Cat2600TsDmnNumStations_Type())
cat2600TsDmnNumStations.setMaxAccess(_B)
if mibBuilder.loadTexts:cat2600TsDmnNumStations.setStatus(_A)
_Cat2600TsDmnMostStations_Type=Integer32
_Cat2600TsDmnMostStations_Object=MibTableColumn
cat2600TsDmnMostStations=_Cat2600TsDmnMostStations_Object((1,3,6,1,4,1,9,1,111,1,2,3,1,1,12),_Cat2600TsDmnMostStations_Type())
cat2600TsDmnMostStations.setMaxAccess(_B)
if mibBuilder.loadTexts:cat2600TsDmnMostStations.setStatus(_A)
_Cat2600TsDmnStationTable_Object=MibTable
cat2600TsDmnStationTable=_Cat2600TsDmnStationTable_Object((1,3,6,1,4,1,9,1,111,1,2,3,5))
if mibBuilder.loadTexts:cat2600TsDmnStationTable.setStatus(_A)
_Cat2600TsDmnStationEntry_Object=MibTableRow
cat2600TsDmnStationEntry=_Cat2600TsDmnStationEntry_Object((1,3,6,1,4,1,9,1,111,1,2,3,5,1))
cat2600TsDmnStationEntry.setIndexNames((0,_E,_L),(0,_E,_T))
if mibBuilder.loadTexts:cat2600TsDmnStationEntry.setStatus(_A)
class _Cat2600TsDmnStationDmnIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Cat2600TsDmnStationDmnIndex_Type.__name__=_D
_Cat2600TsDmnStationDmnIndex_Object=MibTableColumn
cat2600TsDmnStationDmnIndex=_Cat2600TsDmnStationDmnIndex_Object((1,3,6,1,4,1,9,1,111,1,2,3,5,1,1),_Cat2600TsDmnStationDmnIndex_Type())
cat2600TsDmnStationDmnIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cat2600TsDmnStationDmnIndex.setStatus(_A)
class _Cat2600TsDmnStationAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_Cat2600TsDmnStationAddress_Type.__name__=_G
_Cat2600TsDmnStationAddress_Object=MibTableColumn
cat2600TsDmnStationAddress=_Cat2600TsDmnStationAddress_Object((1,3,6,1,4,1,9,1,111,1,2,3,5,1,2),_Cat2600TsDmnStationAddress_Type())
cat2600TsDmnStationAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:cat2600TsDmnStationAddress.setStatus(_A)
_Cat2600TsDmnStationPort_Type=Integer32
_Cat2600TsDmnStationPort_Object=MibTableColumn
cat2600TsDmnStationPort=_Cat2600TsDmnStationPort_Object((1,3,6,1,4,1,9,1,111,1,2,3,5,1,3),_Cat2600TsDmnStationPort_Type())
cat2600TsDmnStationPort.setMaxAccess(_B)
if mibBuilder.loadTexts:cat2600TsDmnStationPort.setStatus(_A)
_Cat2600TsDmnStationTraffic_Type=OctetString
_Cat2600TsDmnStationTraffic_Object=MibTableColumn
cat2600TsDmnStationTraffic=_Cat2600TsDmnStationTraffic_Object((1,3,6,1,4,1,9,1,111,1,2,3,5,1,4),_Cat2600TsDmnStationTraffic_Type())
cat2600TsDmnStationTraffic.setMaxAccess(_B)
if mibBuilder.loadTexts:cat2600TsDmnStationTraffic.setStatus(_A)
_Cat2600TsOptDmnStaTable_Object=MibTable
cat2600TsOptDmnStaTable=_Cat2600TsOptDmnStaTable_Object((1,3,6,1,4,1,9,1,111,1,2,3,6))
if mibBuilder.loadTexts:cat2600TsOptDmnStaTable.setStatus(_A)
_Cat2600TsOptDmnStaEntry_Object=MibTableRow
cat2600TsOptDmnStaEntry=_Cat2600TsOptDmnStaEntry_Object((1,3,6,1,4,1,9,1,111,1,2,3,6,1))
cat2600TsOptDmnStaEntry.setIndexNames((0,_E,_U),(0,_E,_V))
if mibBuilder.loadTexts:cat2600TsOptDmnStaEntry.setStatus(_A)
class _Cat2600TsOptDmnStaPos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Cat2600TsOptDmnStaPos_Type.__name__=_D
_Cat2600TsOptDmnStaPos_Object=MibTableColumn
cat2600TsOptDmnStaPos=_Cat2600TsOptDmnStaPos_Object((1,3,6,1,4,1,9,1,111,1,2,3,6,1,1),_Cat2600TsOptDmnStaPos_Type())
cat2600TsOptDmnStaPos.setMaxAccess(_B)
if mibBuilder.loadTexts:cat2600TsOptDmnStaPos.setStatus(_A)
_Cat2600TsOptDmnStaVal_Type=OctetString
_Cat2600TsOptDmnStaVal_Object=MibTableColumn
cat2600TsOptDmnStaVal=_Cat2600TsOptDmnStaVal_Object((1,3,6,1,4,1,9,1,111,1,2,3,6,1,2),_Cat2600TsOptDmnStaVal_Type())
cat2600TsOptDmnStaVal.setMaxAccess(_B)
if mibBuilder.loadTexts:cat2600TsOptDmnStaVal.setStatus(_A)
_Cat2600TsPipe_ObjectIdentity=ObjectIdentity
cat2600TsPipe=_Cat2600TsPipe_ObjectIdentity((1,3,6,1,4,1,9,1,111,1,2,4))
_Cat2600TsPipeTable_Object=MibTable
cat2600TsPipeTable=_Cat2600TsPipeTable_Object((1,3,6,1,4,1,9,1,111,1,2,4,1))
if mibBuilder.loadTexts:cat2600TsPipeTable.setStatus(_A)
_Cat2600TsPipeEntry_Object=MibTableRow
cat2600TsPipeEntry=_Cat2600TsPipeEntry_Object((1,3,6,1,4,1,9,1,111,1,2,4,1,1))
cat2600TsPipeEntry.setIndexNames((0,_E,_W))
if mibBuilder.loadTexts:cat2600TsPipeEntry.setStatus(_A)
class _Cat2600TsPipeNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_Cat2600TsPipeNumber_Type.__name__=_D
_Cat2600TsPipeNumber_Object=MibTableColumn
cat2600TsPipeNumber=_Cat2600TsPipeNumber_Object((1,3,6,1,4,1,9,1,111,1,2,4,1,1,1),_Cat2600TsPipeNumber_Type())
cat2600TsPipeNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:cat2600TsPipeNumber.setStatus(_A)
class _Cat2600TsPipePorts_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_Cat2600TsPipePorts_Type.__name__=_G
_Cat2600TsPipePorts_Object=MibTableColumn
cat2600TsPipePorts=_Cat2600TsPipePorts_Object((1,3,6,1,4,1,9,1,111,1,2,4,1,1,2),_Cat2600TsPipePorts_Type())
cat2600TsPipePorts.setMaxAccess(_C)
if mibBuilder.loadTexts:cat2600TsPipePorts.setStatus(_A)
_Cat2600TsFilter_ObjectIdentity=ObjectIdentity
cat2600TsFilter=_Cat2600TsFilter_ObjectIdentity((1,3,6,1,4,1,9,1,111,1,2,5))
_Cat2600TsFilterTable_Object=MibTable
cat2600TsFilterTable=_Cat2600TsFilterTable_Object((1,3,6,1,4,1,9,1,111,1,2,5,1))
if mibBuilder.loadTexts:cat2600TsFilterTable.setStatus(_A)
_Cat2600TsFilterEntry_Object=MibTableRow
cat2600TsFilterEntry=_Cat2600TsFilterEntry_Object((1,3,6,1,4,1,9,1,111,1,2,5,1,1))
cat2600TsFilterEntry.setIndexNames((0,_E,_X),(0,_E,_Y))
if mibBuilder.loadTexts:cat2600TsFilterEntry.setStatus(_A)
_Cat2600TsFilterStationAddress_Type=MacAddr
_Cat2600TsFilterStationAddress_Object=MibTableColumn
cat2600TsFilterStationAddress=_Cat2600TsFilterStationAddress_Object((1,3,6,1,4,1,9,1,111,1,2,5,1,1,1),_Cat2600TsFilterStationAddress_Type())
cat2600TsFilterStationAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:cat2600TsFilterStationAddress.setStatus(_A)
class _Cat2600TsFilterType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('source-filter',1),('destination-filter',2)))
_Cat2600TsFilterType_Type.__name__=_D
_Cat2600TsFilterType_Object=MibTableColumn
cat2600TsFilterType=_Cat2600TsFilterType_Object((1,3,6,1,4,1,9,1,111,1,2,5,1,1,2),_Cat2600TsFilterType_Type())
cat2600TsFilterType.setMaxAccess(_B)
if mibBuilder.loadTexts:cat2600TsFilterType.setStatus(_A)
class _Cat2600TsFilterStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),(_N,2)))
_Cat2600TsFilterStatus_Type.__name__=_D
_Cat2600TsFilterStatus_Object=MibTableColumn
cat2600TsFilterStatus=_Cat2600TsFilterStatus_Object((1,3,6,1,4,1,9,1,111,1,2,5,1,1,3),_Cat2600TsFilterStatus_Type())
cat2600TsFilterStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cat2600TsFilterStatus.setStatus(_A)
_Cat2600TsFilterPorts_Type=OctetString
_Cat2600TsFilterPorts_Object=MibTableColumn
cat2600TsFilterPorts=_Cat2600TsFilterPorts_Object((1,3,6,1,4,1,9,1,111,1,2,5,1,1,4),_Cat2600TsFilterPorts_Type())
cat2600TsFilterPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:cat2600TsFilterPorts.setStatus(_A)
class _Cat2600TsFilterMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_Cat2600TsFilterMask_Type.__name__=_G
_Cat2600TsFilterMask_Object=MibTableColumn
cat2600TsFilterMask=_Cat2600TsFilterMask_Object((1,3,6,1,4,1,9,1,111,1,2,5,1,1,5),_Cat2600TsFilterMask_Type())
cat2600TsFilterMask.setMaxAccess(_C)
if mibBuilder.loadTexts:cat2600TsFilterMask.setStatus(_A)
_Cat2600TsUFC_ObjectIdentity=ObjectIdentity
cat2600TsUFC=_Cat2600TsUFC_ObjectIdentity((1,3,6,1,4,1,9,1,111,1,2,6))
_Cat2600TsUFCTable_Object=MibTable
cat2600TsUFCTable=_Cat2600TsUFCTable_Object((1,3,6,1,4,1,9,1,111,1,2,6,1))
if mibBuilder.loadTexts:cat2600TsUFCTable.setStatus(_A)
_Cat2600TsUFCEntry_Object=MibTableRow
cat2600TsUFCEntry=_Cat2600TsUFCEntry_Object((1,3,6,1,4,1,9,1,111,1,2,6,1,1))
cat2600TsUFCEntry.setIndexNames((0,_E,_Z))
if mibBuilder.loadTexts:cat2600TsUFCEntry.setStatus(_A)
class _Cat2600TsUFCSlotNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_Cat2600TsUFCSlotNum_Type.__name__=_D
_Cat2600TsUFCSlotNum_Object=MibTableColumn
cat2600TsUFCSlotNum=_Cat2600TsUFCSlotNum_Object((1,3,6,1,4,1,9,1,111,1,2,6,1,1,1),_Cat2600TsUFCSlotNum_Type())
cat2600TsUFCSlotNum.setMaxAccess(_B)
if mibBuilder.loadTexts:cat2600TsUFCSlotNum.setStatus(_A)
class _Cat2600TsUFCNumPhysIfs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Cat2600TsUFCNumPhysIfs_Type.__name__=_D
_Cat2600TsUFCNumPhysIfs_Object=MibTableColumn
cat2600TsUFCNumPhysIfs=_Cat2600TsUFCNumPhysIfs_Object((1,3,6,1,4,1,9,1,111,1,2,6,1,1,2),_Cat2600TsUFCNumPhysIfs_Type())
cat2600TsUFCNumPhysIfs.setMaxAccess(_B)
if mibBuilder.loadTexts:cat2600TsUFCNumPhysIfs.setStatus(_A)
class _Cat2600TsUFCManufacturer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_Cat2600TsUFCManufacturer_Type.__name__=_F
_Cat2600TsUFCManufacturer_Object=MibTableColumn
cat2600TsUFCManufacturer=_Cat2600TsUFCManufacturer_Object((1,3,6,1,4,1,9,1,111,1,2,6,1,1,3),_Cat2600TsUFCManufacturer_Type())
cat2600TsUFCManufacturer.setMaxAccess(_B)
if mibBuilder.loadTexts:cat2600TsUFCManufacturer.setStatus(_A)
class _Cat2600TsUFCType_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_Cat2600TsUFCType_Type.__name__=_G
_Cat2600TsUFCType_Object=MibTableColumn
cat2600TsUFCType=_Cat2600TsUFCType_Object((1,3,6,1,4,1,9,1,111,1,2,6,1,1,4),_Cat2600TsUFCType_Type())
cat2600TsUFCType.setMaxAccess(_B)
if mibBuilder.loadTexts:cat2600TsUFCType.setStatus(_A)
class _Cat2600TsUFCTypeDesc_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_Cat2600TsUFCTypeDesc_Type.__name__=_F
_Cat2600TsUFCTypeDesc_Object=MibTableColumn
cat2600TsUFCTypeDesc=_Cat2600TsUFCTypeDesc_Object((1,3,6,1,4,1,9,1,111,1,2,6,1,1,5),_Cat2600TsUFCTypeDesc_Type())
cat2600TsUFCTypeDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:cat2600TsUFCTypeDesc.setStatus(_A)
class _Cat2600TsUFCHwVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_Cat2600TsUFCHwVer_Type.__name__=_F
_Cat2600TsUFCHwVer_Object=MibTableColumn
cat2600TsUFCHwVer=_Cat2600TsUFCHwVer_Object((1,3,6,1,4,1,9,1,111,1,2,6,1,1,6),_Cat2600TsUFCHwVer_Type())
cat2600TsUFCHwVer.setMaxAccess(_B)
if mibBuilder.loadTexts:cat2600TsUFCHwVer.setStatus(_A)
class _Cat2600TsUFCFwVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_Cat2600TsUFCFwVer_Type.__name__=_F
_Cat2600TsUFCFwVer_Object=MibTableColumn
cat2600TsUFCFwVer=_Cat2600TsUFCFwVer_Object((1,3,6,1,4,1,9,1,111,1,2,6,1,1,7),_Cat2600TsUFCFwVer_Type())
cat2600TsUFCFwVer.setMaxAccess(_B)
if mibBuilder.loadTexts:cat2600TsUFCFwVer.setStatus(_A)
class _Cat2600TsUFCStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),(_H,3)))
_Cat2600TsUFCStatus_Type.__name__=_D
_Cat2600TsUFCStatus_Object=MibTableColumn
cat2600TsUFCStatus=_Cat2600TsUFCStatus_Object((1,3,6,1,4,1,9,1,111,1,2,6,1,1,8),_Cat2600TsUFCStatus_Type())
cat2600TsUFCStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cat2600TsUFCStatus.setStatus(_A)
class _Cat2600TsUFCReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_O,2),(_P,3)))
_Cat2600TsUFCReset_Type.__name__=_D
_Cat2600TsUFCReset_Object=MibTableColumn
cat2600TsUFCReset=_Cat2600TsUFCReset_Object((1,3,6,1,4,1,9,1,111,1,2,6,1,1,9),_Cat2600TsUFCReset_Type())
cat2600TsUFCReset.setMaxAccess(_C)
if mibBuilder.loadTexts:cat2600TsUFCReset.setStatus(_A)
_DtrMIBs_ObjectIdentity=ObjectIdentity
dtrMIBs=_DtrMIBs_ObjectIdentity((1,3,6,1,4,1,9,1,111,1,3))
_DtrConcMIB_ObjectIdentity=ObjectIdentity
dtrConcMIB=_DtrConcMIB_ObjectIdentity((1,3,6,1,4,1,9,1,111,1,3,1))
_DtrMacMIB_ObjectIdentity=ObjectIdentity
dtrMacMIB=_DtrMacMIB_ObjectIdentity((1,3,6,1,4,1,9,1,111,1,3,2))
mibBuilder.exportSymbols(_E,**{'MacAddr':MacAddr,'cisco':cisco,'catProd':catProd,'cat2600':cat2600,'cat2600Ts':cat2600Ts,'cat2600TsObjectID':cat2600TsObjectID,'cat2600TsSysObjectID':cat2600TsSysObjectID,'cat2600TsObjects':cat2600TsObjects,'cat2600TsMain':cat2600TsMain,'cat2600TsConfig':cat2600TsConfig,'cat2600TsFwVer':cat2600TsFwVer,'cat2600TsHwVer':cat2600TsHwVer,'cat2600TsSerialNumber':cat2600TsSerialNumber,'cat2600TsInstallationDate':cat2600TsInstallationDate,'cat2600TsFwSize':cat2600TsFwSize,'cat2600TsFwCRC':cat2600TsFwCRC,'cat2600TsFwManufacturer':cat2600TsFwManufacturer,'cat2600TsIpAddr':cat2600TsIpAddr,'cat2600TsNetMask':cat2600TsNetMask,'cat2600TsDefaultGateway':cat2600TsDefaultGateway,'cat2600TsTrapRcvrTable':cat2600TsTrapRcvrTable,'cat2600TsTrapRcvrEntry':cat2600TsTrapRcvrEntry,_M:cat2600TsTrapRcvrIndex,'cat2600TsTrapRcvrStatus':cat2600TsTrapRcvrStatus,'cat2600TsTrapRcvrIpAddress':cat2600TsTrapRcvrIpAddress,'cat2600TsTrapRcvrComm':cat2600TsTrapRcvrComm,'cat2600TsTrapRcvrDmns':cat2600TsTrapRcvrDmns,'cat2600TsPingInterval':cat2600TsPingInterval,'cat2600TsTapPort':cat2600TsTapPort,'cat2600TsTapMonitoredPort':cat2600TsTapMonitoredPort,'cat2600TsCrcThresholdHi':cat2600TsCrcThresholdHi,'cat2600TsCrcThresholdLow':cat2600TsCrcThresholdLow,'cat2600TsPortSwitchModeChangeTrapEnable':cat2600TsPortSwitchModeChangeTrapEnable,'cat2600TsTrendThreshold':cat2600TsTrendThreshold,'cat2600TsSamplingPeriod':cat2600TsSamplingPeriod,'cat2600TsNumberUFC':cat2600TsNumberUFC,'cat2600TsSys':cat2600TsSys,'cat2600TsNumPorts':cat2600TsNumPorts,'cat2600TsNumStations':cat2600TsNumStations,'cat2600TsMostStations':cat2600TsMostStations,'cat2600TsMaxStations':cat2600TsMaxStations,'cat2600TsReset':cat2600TsReset,'cat2600TsNumResets':cat2600TsNumResets,'cat2600TsAddrAgingTime':cat2600TsAddrAgingTime,'cat2600TsSysTemperature':cat2600TsSysTemperature,'cat2600TsInstalledMemory':cat2600TsInstalledMemory,'cat2600TsSysCurTime':cat2600TsSysCurTime,'cat2600TsPort':cat2600TsPort,'cat2600TsPortTable':cat2600TsPortTable,'cat2600TsPortEntry':cat2600TsPortEntry,_J:cat2600TsPortIndex,'cat2600TsPortRcvLocalFrames':cat2600TsPortRcvLocalFrames,'cat2600TsPortForwardedFrames':cat2600TsPortForwardedFrames,'cat2600TsPortMostStations':cat2600TsPortMostStations,'cat2600TsPortMaxStations':cat2600TsPortMaxStations,'cat2600TsPortSWHandledFrames':cat2600TsPortSWHandledFrames,'cat2600TsPortLocalStations':cat2600TsPortLocalStations,'cat2600TsPortRemoteStations':cat2600TsPortRemoteStations,'cat2600TsPortUnknownStaFrames':cat2600TsPortUnknownStaFrames,'cat2600TsPortResetStats':cat2600TsPortResetStats,'cat2600TsPortResetTimer':cat2600TsPortResetTimer,'cat2600TsPortResetAddrs':cat2600TsPortResetAddrs,'cat2600TsPortRcvBcasts':cat2600TsPortRcvBcasts,'cat2600TsPortSwitchedFrames':cat2600TsPortSwitchedFrames,'cat2600TsPortLinkState':cat2600TsPortLinkState,'cat2600TsPortHashOverflows':cat2600TsPortHashOverflows,'cat2600TsPortAddrAgingTime':cat2600TsPortAddrAgingTime,'cat2600TsPortSwitchMode':cat2600TsPortSwitchMode,'cat2600TsPortFixedCfg':cat2600TsPortFixedCfg,'cat2600TsPortMode':cat2600TsPortMode,'cat2600TsPortDuplex':cat2600TsPortDuplex,'cat2600TsPortCfgLoss':cat2600TsPortCfgLoss,'cat2600TsPortCfgLossRC':cat2600TsPortCfgLossRC,'cat2600TsPortCRCCount':cat2600TsPortCRCCount,'cat2600TsPortHPChannelFrames':cat2600TsPortHPChannelFrames,'cat2600TsPortLPChannelFrames':cat2600TsPortLPChannelFrames,'cat2600TsPortHPThreshold':cat2600TsPortHPThreshold,'cat2600TsPortCfgRingSpeed':cat2600TsPortCfgRingSpeed,'cat2600TsPortCfgRSA':cat2600TsPortCfgRSA,'cat2600TsPortDomain':cat2600TsPortDomain,'cat2600TsPortCfgLossThreshold':cat2600TsPortCfgLossThreshold,'cat2600TsPortCfgLossSamplingPeriod':cat2600TsPortCfgLossSamplingPeriod,'cat2600TsPortBeaconStationAddress':cat2600TsPortBeaconStationAddress,'cat2600TsPortBeaconNAUN':cat2600TsPortBeaconNAUN,'cat2600TsPortBeaconType':cat2600TsPortBeaconType,'cat2600TsOptPortStaTable':cat2600TsOptPortStaTable,'cat2600TsOptPortStaEntry':cat2600TsOptPortStaEntry,_Q:cat2600TsOptPortStaPos,'cat2600TsOptPortStaVal':cat2600TsOptPortStaVal,'cat2600TsPortStnTable':cat2600TsPortStnTable,'cat2600TsPortStnEntry':cat2600TsPortStnEntry,_R:cat2600TsPortStnPortNum,_S:cat2600TsPortStnAddress,'cat2600TsPortStnLocation':cat2600TsPortStnLocation,'cat2600TsPortStnSrcFrames':cat2600TsPortStnSrcFrames,'cat2600TsPortStnSrcBytes':cat2600TsPortStnSrcBytes,'cat2600TsPortStnDestnFrames':cat2600TsPortStnDestnFrames,'cat2600TsPortStnDestnBytes':cat2600TsPortStnDestnBytes,'cat2600TsDmns':cat2600TsDmns,'cat2600TsDmnTable':cat2600TsDmnTable,'cat2600TsDmnEntry':cat2600TsDmnEntry,_L:cat2600TsDmnIndex,'cat2600TsDmnPorts':cat2600TsDmnPorts,'cat2600TsDmnIpState':cat2600TsDmnIpState,'cat2600TsDmnIpAddress':cat2600TsDmnIpAddress,'cat2600TsDmnIpSubnetMask':cat2600TsDmnIpSubnetMask,'cat2600TsDmnIpDefaultGateway':cat2600TsDmnIpDefaultGateway,'cat2600TsDmnStp':cat2600TsDmnStp,'cat2600TsDmnName':cat2600TsDmnName,'cat2600TsDmnIfIndex':cat2600TsDmnIfIndex,'cat2600TsDmnBaseBridgeAddr':cat2600TsDmnBaseBridgeAddr,'cat2600TsDmnNumStations':cat2600TsDmnNumStations,'cat2600TsDmnMostStations':cat2600TsDmnMostStations,'cat2600TsDmnStationTable':cat2600TsDmnStationTable,'cat2600TsDmnStationEntry':cat2600TsDmnStationEntry,_U:cat2600TsDmnStationDmnIndex,_T:cat2600TsDmnStationAddress,'cat2600TsDmnStationPort':cat2600TsDmnStationPort,'cat2600TsDmnStationTraffic':cat2600TsDmnStationTraffic,'cat2600TsOptDmnStaTable':cat2600TsOptDmnStaTable,'cat2600TsOptDmnStaEntry':cat2600TsOptDmnStaEntry,_V:cat2600TsOptDmnStaPos,'cat2600TsOptDmnStaVal':cat2600TsOptDmnStaVal,'cat2600TsPipe':cat2600TsPipe,'cat2600TsPipeTable':cat2600TsPipeTable,'cat2600TsPipeEntry':cat2600TsPipeEntry,_W:cat2600TsPipeNumber,'cat2600TsPipePorts':cat2600TsPipePorts,'cat2600TsFilter':cat2600TsFilter,'cat2600TsFilterTable':cat2600TsFilterTable,'cat2600TsFilterEntry':cat2600TsFilterEntry,_X:cat2600TsFilterStationAddress,_Y:cat2600TsFilterType,'cat2600TsFilterStatus':cat2600TsFilterStatus,'cat2600TsFilterPorts':cat2600TsFilterPorts,'cat2600TsFilterMask':cat2600TsFilterMask,'cat2600TsUFC':cat2600TsUFC,'cat2600TsUFCTable':cat2600TsUFCTable,'cat2600TsUFCEntry':cat2600TsUFCEntry,_Z:cat2600TsUFCSlotNum,'cat2600TsUFCNumPhysIfs':cat2600TsUFCNumPhysIfs,'cat2600TsUFCManufacturer':cat2600TsUFCManufacturer,'cat2600TsUFCType':cat2600TsUFCType,'cat2600TsUFCTypeDesc':cat2600TsUFCTypeDesc,'cat2600TsUFCHwVer':cat2600TsUFCHwVer,'cat2600TsUFCFwVer':cat2600TsUFCFwVer,'cat2600TsUFCStatus':cat2600TsUFCStatus,'cat2600TsUFCReset':cat2600TsUFCReset,'dtrMIBs':dtrMIBs,'dtrConcMIB':dtrConcMIB,'dtrMacMIB':dtrMacMIB})