_B5='nbsCmmcSlotModuleStatus'
_B4='nbsCmmcPortSelectLink'
_B3='nbsCmmcSlotModelInserted'
_B2='nbsCmmcSlotModelLocked'
_B1='nbsCmmcTrapErrorInfo'
_B0='nbsCmmcSlotTemperatureLimit'
_A_='nbsCmmcSlotTemperatureMin'
_Az='nbsCmmcTrapPortName'
_Ay='nbsCmmcTrapPortIndex'
_Ax='nbsCmmcPortWavelength'
_Aw='nbsCmmcPortConnector'
_Av='nbsCmmcPortValue'
_Au='nbsCmmcPortLink'
_At='nbsCmmcChassisTemperatureMin'
_As='nbsCmmcChassisTemperatureLimit'
_Ar='nbsCmmcSysAuditLogIndex'
_Aq='nbsCmmcSysNvramLogMessageIndex'
_Ap='nbsCmmcSysRunningLogMessageIndex'
_Ao='nbsCmmcSysLogMessageType'
_An='nbsCmmcSmtpRcvrIndex'
_Am='deprecatedAuto'
_Al='nbsCmmcPortSlotIndex'
_Ak='nbsCmmcPortChassisIndex'
_Aj='nbsCmmcSlotFaceRowIndex'
_Ai='nbsCmmcSlotFaceSlotIndex'
_Ah='nbsCmmcSlotFaceChassisIndex'
_Ag='nbsCmmcLedIndex'
_Af='nbsCmmcLedSlotIndex'
_Ae='nbsCmmcLedChassisIndex'
_Ad='nbsCmmcSlotChassisIndex'
_Ac='nbsCmmcTftpSessIndex'
_Ab='deprecated6'
_Aa='nbsCmmcSysTrapTblEntIndex'
_AZ='nbsCmmcSysPingSessionIndex'
_AY='nbsCmmcSysTelnetSessionIndex'
_AX='nbsCmmcSysNVAreaBank'
_AW='nbsCmmcSysNVAreaIfIndex'
_AV='completed'
_AU='transferring'
_AT='nbsCmmcSysLoaderIndex'
_AS='nbsCmmcSysTimeZoneIndex'
_AR='nbsCmmcSysProtoIndex'
_AQ='nbsCmmcSysFirmwareIndex'
_AP='nbsCmmcSysDiscoveryHostMACAddress'
_AO='nbsCmmcSysNvramIndex'
_AN='NbsCmmcEnumSlotOperationType'
_AM='InterfaceIndex'
_AL='nbsCmmcPortSupplyVoltsLevel'
_AK='nbsCmmcPortBiasAmpsLevel'
_AJ='nbsCmmcPortTxPowerLevel'
_AI='nbsCmmcPortRxPowerLevel'
_AH='nbsCmmcPortTemperatureLevel'
_AG='nbsCmmcSlotType'
_AF='enable'
_AE='deprecated5'
_AD='active'
_AC='b38400'
_AB='b19200'
_AA='b9600'
_A9='00000000'
_A8='nbsCmmcSlotTemperature'
_A7='nbsCmmcPortSupplyVolts'
_A6='nbsCmmcPortBiasAmps'
_A5='nbsCmmcPortTxPower'
_A4='nbsCmmcPortRxPower'
_A3='nbsCmmcPortTemperature'
_A2='nbsCmmcChassisTemperature'
_A1='nbsCmmcTrapShutdownReason'
_A0='info'
_z='disable'
_y='yes'
_x='no'
_w='other'
_v='dcGood'
_u='acGood'
_t='dcBad'
_s='acBad'
_r='counting'
_q='invalid'
_p='supported'
_o='Unsigned32'
_n='nbsCmmcTrapFanId'
_m='nbsCmmcTrapPowerSupplyId'
_l='highAlarm'
_k='highWarning'
_j='ok'
_i='lowWarning'
_h='lowAlarm'
_g='alarm'
_f='fatal'
_e='IpAddress'
_d='warning'
_c='error'
_b='InetAddressType'
_a='operating'
_Z='accessible-for-notify'
_Y='clearing'
_X='nbsCmmcPortThreshold'
_W='bad'
_V='good'
_U='notInstalled'
_T='OctetString'
_S='on'
_R='off'
_Q='enabled'
_P='disabled'
_O='nbsCmmcPortName'
_N='nbsCmmcPortIndex'
_M='nbsCmmcSlotName'
_L='nbsCmmcSlotIndex'
_K='deprecated'
_J='DisplayString'
_I='nbsCmmcChassisName'
_H='nbsCmmcChassisIndex'
_G='nbsCmmcTrapLastMessage'
_F='notSupported'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='NBS-CMMC-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_T,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB',_AM)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress',_b)
NbsCmmcEnumChassisType,NbsCmmcEnumPortConnector,NbsCmmcEnumSlotOperationType,NbsCmmcEnumSlotType=mibBuilder.importSymbols('NBS-CMMCENUM-MIB','NbsCmmcEnumChassisType','NbsCmmcEnumPortConnector',_AN,'NbsCmmcEnumSlotType')
nbs,=mibBuilder.importSymbols('NBS-MIB','nbs')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,_e,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_o,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_J,'PhysAddress','TextualConvention')
nbsCmmcMib=ModuleIdentity((1,3,6,1,4,1,629,200))
_NbsCmmcObjects_ObjectIdentity=ObjectIdentity
nbsCmmcObjects=_NbsCmmcObjects_ObjectIdentity((1,3,6,1,4,1,629,200,1))
if mibBuilder.loadTexts:nbsCmmcObjects.setStatus(_A)
_NbsCmmcSystemGrp_ObjectIdentity=ObjectIdentity
nbsCmmcSystemGrp=_NbsCmmcSystemGrp_ObjectIdentity((1,3,6,1,4,1,629,200,2))
if mibBuilder.loadTexts:nbsCmmcSystemGrp.setStatus(_A)
class _NbsCmmcSysFwDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NbsCmmcSysFwDescr_Type.__name__=_J
_NbsCmmcSysFwDescr_Object=MibScalar
nbsCmmcSysFwDescr=_NbsCmmcSysFwDescr_Object((1,3,6,1,4,1,629,200,2,1),_NbsCmmcSysFwDescr_Type())
nbsCmmcSysFwDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysFwDescr.setStatus(_A)
class _NbsCmmcSysFwVers_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_NbsCmmcSysFwVers_Type.__name__=_J
_NbsCmmcSysFwVers_Object=MibScalar
nbsCmmcSysFwVers=_NbsCmmcSysFwVers_Object((1,3,6,1,4,1,629,200,2,2),_NbsCmmcSysFwVers_Type())
nbsCmmcSysFwVers.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysFwVers.setStatus(_A)
class _NbsCmmcSysRestart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('running',1),('coldRestart',2),('warmRestart',3),('upgrRestart',4)))
_NbsCmmcSysRestart_Type.__name__=_D
_NbsCmmcSysRestart_Object=MibScalar
nbsCmmcSysRestart=_NbsCmmcSysRestart_Object((1,3,6,1,4,1,629,200,2,3),_NbsCmmcSysRestart_Type())
nbsCmmcSysRestart.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysRestart.setStatus(_A)
_NbsCmmcSysNumRestarts_Type=Counter32
_NbsCmmcSysNumRestarts_Object=MibScalar
nbsCmmcSysNumRestarts=_NbsCmmcSysNumRestarts_Object((1,3,6,1,4,1,629,200,2,4),_NbsCmmcSysNumRestarts_Type())
nbsCmmcSysNumRestarts.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysNumRestarts.setStatus(_A)
_NbsCmmcSysErrUptime_Type=TimeTicks
_NbsCmmcSysErrUptime_Object=MibScalar
nbsCmmcSysErrUptime=_NbsCmmcSysErrUptime_Object((1,3,6,1,4,1,629,200,2,5),_NbsCmmcSysErrUptime_Type())
nbsCmmcSysErrUptime.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysErrUptime.setStatus(_A)
class _NbsCmmcSysSetNvramDefaults_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('setDefaults',1))
_NbsCmmcSysSetNvramDefaults_Type.__name__=_D
_NbsCmmcSysSetNvramDefaults_Object=MibScalar
nbsCmmcSysSetNvramDefaults=_NbsCmmcSysSetNvramDefaults_Object((1,3,6,1,4,1,629,200,2,6),_NbsCmmcSysSetNvramDefaults_Type())
nbsCmmcSysSetNvramDefaults.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysSetNvramDefaults.setStatus(_A)
class _NbsCmmcSysSelftestLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('ststNone',1),('ststShort',2),('ststLong',3),('ststDiagnostics',4)))
_NbsCmmcSysSelftestLevel_Type.__name__=_D
_NbsCmmcSysSelftestLevel_Object=MibScalar
nbsCmmcSysSelftestLevel=_NbsCmmcSysSelftestLevel_Object((1,3,6,1,4,1,629,200,2,7),_NbsCmmcSysSelftestLevel_Type())
nbsCmmcSysSelftestLevel.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysSelftestLevel.setStatus(_K)
class _NbsCmmcSysCurrentTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2208988800,4294967295))
_NbsCmmcSysCurrentTime_Type.__name__=_o
_NbsCmmcSysCurrentTime_Object=MibScalar
nbsCmmcSysCurrentTime=_NbsCmmcSysCurrentTime_Object((1,3,6,1,4,1,629,200,2,8),_NbsCmmcSysCurrentTime_Type())
nbsCmmcSysCurrentTime.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysCurrentTime.setStatus(_A)
class _NbsCmmcSysCurrentDateTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_NbsCmmcSysCurrentDateTime_Type.__name__=_J
_NbsCmmcSysCurrentDateTime_Object=MibScalar
nbsCmmcSysCurrentDateTime=_NbsCmmcSysCurrentDateTime_Object((1,3,6,1,4,1,629,200,2,9),_NbsCmmcSysCurrentDateTime_Type())
nbsCmmcSysCurrentDateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysCurrentDateTime.setStatus(_A)
_NbsCmmcSysNvramTable_Object=MibTable
nbsCmmcSysNvramTable=_NbsCmmcSysNvramTable_Object((1,3,6,1,4,1,629,200,2,10))
if mibBuilder.loadTexts:nbsCmmcSysNvramTable.setStatus(_A)
_NbsCmmcSysNvramEntry_Object=MibTableRow
nbsCmmcSysNvramEntry=_NbsCmmcSysNvramEntry_Object((1,3,6,1,4,1,629,200,2,10,1))
nbsCmmcSysNvramEntry.setIndexNames((0,_B,_AO))
if mibBuilder.loadTexts:nbsCmmcSysNvramEntry.setStatus(_A)
_NbsCmmcSysNvramIndex_Type=Integer32
_NbsCmmcSysNvramIndex_Object=MibTableColumn
nbsCmmcSysNvramIndex=_NbsCmmcSysNvramIndex_Object((1,3,6,1,4,1,629,200,2,10,1,1),_NbsCmmcSysNvramIndex_Type())
nbsCmmcSysNvramIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysNvramIndex.setStatus(_A)
class _NbsCmmcSysNvramBlock_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,250))
_NbsCmmcSysNvramBlock_Type.__name__=_T
_NbsCmmcSysNvramBlock_Object=MibTableColumn
nbsCmmcSysNvramBlock=_NbsCmmcSysNvramBlock_Object((1,3,6,1,4,1,629,200,2,10,1,2),_NbsCmmcSysNvramBlock_Type())
nbsCmmcSysNvramBlock.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysNvramBlock.setStatus(_A)
class _NbsCmmcSysWriteConfig_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_p,2),('write',3),('copyTempFile',4)))
_NbsCmmcSysWriteConfig_Type.__name__=_D
_NbsCmmcSysWriteConfig_Object=MibScalar
nbsCmmcSysWriteConfig=_NbsCmmcSysWriteConfig_Object((1,3,6,1,4,1,629,200,2,11),_NbsCmmcSysWriteConfig_Type())
nbsCmmcSysWriteConfig.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysWriteConfig.setStatus(_A)
_NbsCmmcSysUpgrade_Type=DisplayString
_NbsCmmcSysUpgrade_Object=MibScalar
nbsCmmcSysUpgrade=_NbsCmmcSysUpgrade_Object((1,3,6,1,4,1,629,200,2,12),_NbsCmmcSysUpgrade_Type())
nbsCmmcSysUpgrade.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysUpgrade.setStatus(_K)
class _NbsCmmcSysLoginIdleTimeout_Type(Integer32):defaultValue=15;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,400000))
_NbsCmmcSysLoginIdleTimeout_Type.__name__=_D
_NbsCmmcSysLoginIdleTimeout_Object=MibScalar
nbsCmmcSysLoginIdleTimeout=_NbsCmmcSysLoginIdleTimeout_Object((1,3,6,1,4,1,629,200,2,13),_NbsCmmcSysLoginIdleTimeout_Type())
nbsCmmcSysLoginIdleTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysLoginIdleTimeout.setStatus(_A)
class _NbsCmmcSysDiscoveryAdmin_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_P,2),(_Q,3)))
_NbsCmmcSysDiscoveryAdmin_Type.__name__=_D
_NbsCmmcSysDiscoveryAdmin_Object=MibScalar
nbsCmmcSysDiscoveryAdmin=_NbsCmmcSysDiscoveryAdmin_Object((1,3,6,1,4,1,629,200,2,14),_NbsCmmcSysDiscoveryAdmin_Type())
nbsCmmcSysDiscoveryAdmin.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysDiscoveryAdmin.setStatus(_A)
_NbsCmmcSysDiscoveryHostTable_Object=MibTable
nbsCmmcSysDiscoveryHostTable=_NbsCmmcSysDiscoveryHostTable_Object((1,3,6,1,4,1,629,200,2,15))
if mibBuilder.loadTexts:nbsCmmcSysDiscoveryHostTable.setStatus(_A)
_NbsCmmcSysDiscoveryHostEntry_Object=MibTableRow
nbsCmmcSysDiscoveryHostEntry=_NbsCmmcSysDiscoveryHostEntry_Object((1,3,6,1,4,1,629,200,2,15,1))
nbsCmmcSysDiscoveryHostEntry.setIndexNames((0,_B,_AP))
if mibBuilder.loadTexts:nbsCmmcSysDiscoveryHostEntry.setStatus(_A)
class _NbsCmmcSysDiscoveryHostMACAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_NbsCmmcSysDiscoveryHostMACAddress_Type.__name__=_T
_NbsCmmcSysDiscoveryHostMACAddress_Object=MibTableColumn
nbsCmmcSysDiscoveryHostMACAddress=_NbsCmmcSysDiscoveryHostMACAddress_Object((1,3,6,1,4,1,629,200,2,15,1,1),_NbsCmmcSysDiscoveryHostMACAddress_Type())
nbsCmmcSysDiscoveryHostMACAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysDiscoveryHostMACAddress.setStatus(_A)
class _NbsCmmcSysDiscoveryHostDistance_Type(Integer32):defaultValue=0
_NbsCmmcSysDiscoveryHostDistance_Type.__name__=_D
_NbsCmmcSysDiscoveryHostDistance_Object=MibTableColumn
nbsCmmcSysDiscoveryHostDistance=_NbsCmmcSysDiscoveryHostDistance_Object((1,3,6,1,4,1,629,200,2,15,1,2),_NbsCmmcSysDiscoveryHostDistance_Type())
nbsCmmcSysDiscoveryHostDistance.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysDiscoveryHostDistance.setStatus(_A)
class _NbsCmmcSysDiscoveryHostIPAddress_Type(IpAddress):defaultHexValue=_A9
_NbsCmmcSysDiscoveryHostIPAddress_Type.__name__=_e
_NbsCmmcSysDiscoveryHostIPAddress_Object=MibTableColumn
nbsCmmcSysDiscoveryHostIPAddress=_NbsCmmcSysDiscoveryHostIPAddress_Object((1,3,6,1,4,1,629,200,2,15,1,3),_NbsCmmcSysDiscoveryHostIPAddress_Type())
nbsCmmcSysDiscoveryHostIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysDiscoveryHostIPAddress.setStatus(_A)
_NbsCmmcSysDiscoveryHostAddressType_Type=InetAddressType
_NbsCmmcSysDiscoveryHostAddressType_Object=MibTableColumn
nbsCmmcSysDiscoveryHostAddressType=_NbsCmmcSysDiscoveryHostAddressType_Object((1,3,6,1,4,1,629,200,2,15,1,4),_NbsCmmcSysDiscoveryHostAddressType_Type())
nbsCmmcSysDiscoveryHostAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysDiscoveryHostAddressType.setStatus(_A)
_NbsCmmcSysDiscoveryHostAddress_Type=InetAddress
_NbsCmmcSysDiscoveryHostAddress_Object=MibTableColumn
nbsCmmcSysDiscoveryHostAddress=_NbsCmmcSysDiscoveryHostAddress_Object((1,3,6,1,4,1,629,200,2,15,1,5),_NbsCmmcSysDiscoveryHostAddress_Type())
nbsCmmcSysDiscoveryHostAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysDiscoveryHostAddress.setStatus(_A)
_NbsCmmcSysDiscoveryHostSourceIfIndex_Type=InterfaceIndex
_NbsCmmcSysDiscoveryHostSourceIfIndex_Object=MibTableColumn
nbsCmmcSysDiscoveryHostSourceIfIndex=_NbsCmmcSysDiscoveryHostSourceIfIndex_Object((1,3,6,1,4,1,629,200,2,15,1,6),_NbsCmmcSysDiscoveryHostSourceIfIndex_Type())
nbsCmmcSysDiscoveryHostSourceIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysDiscoveryHostSourceIfIndex.setStatus(_A)
class _NbsCmmcSysLastSetFailure_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NbsCmmcSysLastSetFailure_Type.__name__=_J
_NbsCmmcSysLastSetFailure_Object=MibScalar
nbsCmmcSysLastSetFailure=_NbsCmmcSysLastSetFailure_Object((1,3,6,1,4,1,629,200,2,16),_NbsCmmcSysLastSetFailure_Type())
nbsCmmcSysLastSetFailure.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysLastSetFailure.setStatus(_A)
class _NbsCmmcSysTimeProtocol_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_P,2),(_Q,3)))
_NbsCmmcSysTimeProtocol_Type.__name__=_D
_NbsCmmcSysTimeProtocol_Object=MibScalar
nbsCmmcSysTimeProtocol=_NbsCmmcSysTimeProtocol_Object((1,3,6,1,4,1,629,200,2,17),_NbsCmmcSysTimeProtocol_Type())
nbsCmmcSysTimeProtocol.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysTimeProtocol.setStatus(_A)
_NbsCmmcSysTimeServer_Type=IpAddress
_NbsCmmcSysTimeServer_Object=MibScalar
nbsCmmcSysTimeServer=_NbsCmmcSysTimeServer_Object((1,3,6,1,4,1,629,200,2,18),_NbsCmmcSysTimeServer_Type())
nbsCmmcSysTimeServer.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysTimeServer.setStatus(_A)
_NbsCmmcSysFirmwareTable_Object=MibTable
nbsCmmcSysFirmwareTable=_NbsCmmcSysFirmwareTable_Object((1,3,6,1,4,1,629,200,2,19))
if mibBuilder.loadTexts:nbsCmmcSysFirmwareTable.setStatus(_A)
_NbsCmmcSysFirmwareEntry_Object=MibTableRow
nbsCmmcSysFirmwareEntry=_NbsCmmcSysFirmwareEntry_Object((1,3,6,1,4,1,629,200,2,19,1))
nbsCmmcSysFirmwareEntry.setIndexNames((0,_B,_AQ))
if mibBuilder.loadTexts:nbsCmmcSysFirmwareEntry.setStatus(_A)
_NbsCmmcSysFirmwareIndex_Type=Integer32
_NbsCmmcSysFirmwareIndex_Object=MibTableColumn
nbsCmmcSysFirmwareIndex=_NbsCmmcSysFirmwareIndex_Object((1,3,6,1,4,1,629,200,2,19,1,1),_NbsCmmcSysFirmwareIndex_Type())
nbsCmmcSysFirmwareIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysFirmwareIndex.setStatus(_A)
class _NbsCmmcSysFirmwareDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NbsCmmcSysFirmwareDescr_Type.__name__=_J
_NbsCmmcSysFirmwareDescr_Object=MibTableColumn
nbsCmmcSysFirmwareDescr=_NbsCmmcSysFirmwareDescr_Object((1,3,6,1,4,1,629,200,2,19,1,2),_NbsCmmcSysFirmwareDescr_Type())
nbsCmmcSysFirmwareDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysFirmwareDescr.setStatus(_A)
class _NbsCmmcSysFirmwareFilename_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NbsCmmcSysFirmwareFilename_Type.__name__=_J
_NbsCmmcSysFirmwareFilename_Object=MibTableColumn
nbsCmmcSysFirmwareFilename=_NbsCmmcSysFirmwareFilename_Object((1,3,6,1,4,1,629,200,2,19,1,3),_NbsCmmcSysFirmwareFilename_Type())
nbsCmmcSysFirmwareFilename.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysFirmwareFilename.setStatus(_A)
_NbsCmmcSysFirmwareSize_Type=Integer32
_NbsCmmcSysFirmwareSize_Object=MibTableColumn
nbsCmmcSysFirmwareSize=_NbsCmmcSysFirmwareSize_Object((1,3,6,1,4,1,629,200,2,19,1,4),_NbsCmmcSysFirmwareSize_Type())
nbsCmmcSysFirmwareSize.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysFirmwareSize.setStatus(_A)
_NbsCmmcSysFirmwareMTime_Type=Integer32
_NbsCmmcSysFirmwareMTime_Object=MibTableColumn
nbsCmmcSysFirmwareMTime=_NbsCmmcSysFirmwareMTime_Object((1,3,6,1,4,1,629,200,2,19,1,5),_NbsCmmcSysFirmwareMTime_Type())
nbsCmmcSysFirmwareMTime.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysFirmwareMTime.setStatus(_A)
class _NbsCmmcSysFirmwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NbsCmmcSysFirmwareVersion_Type.__name__=_J
_NbsCmmcSysFirmwareVersion_Object=MibTableColumn
nbsCmmcSysFirmwareVersion=_NbsCmmcSysFirmwareVersion_Object((1,3,6,1,4,1,629,200,2,19,1,6),_NbsCmmcSysFirmwareVersion_Type())
nbsCmmcSysFirmwareVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysFirmwareVersion.setStatus(_A)
class _NbsCmmcSysFirmwareDate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NbsCmmcSysFirmwareDate_Type.__name__=_J
_NbsCmmcSysFirmwareDate_Object=MibTableColumn
nbsCmmcSysFirmwareDate=_NbsCmmcSysFirmwareDate_Object((1,3,6,1,4,1,629,200,2,19,1,7),_NbsCmmcSysFirmwareDate_Type())
nbsCmmcSysFirmwareDate.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysFirmwareDate.setStatus(_A)
class _NbsCmmcSysFirmwareType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_q,1),('chassis',2),('slot',3),('port',4),('deleted',5)))
_NbsCmmcSysFirmwareType_Type.__name__=_D
_NbsCmmcSysFirmwareType_Object=MibTableColumn
nbsCmmcSysFirmwareType=_NbsCmmcSysFirmwareType_Object((1,3,6,1,4,1,629,200,2,19,1,8),_NbsCmmcSysFirmwareType_Type())
nbsCmmcSysFirmwareType.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysFirmwareType.setStatus(_A)
class _NbsCmmcSysFirmwareIDCs_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NbsCmmcSysFirmwareIDCs_Type.__name__=_J
_NbsCmmcSysFirmwareIDCs_Object=MibTableColumn
nbsCmmcSysFirmwareIDCs=_NbsCmmcSysFirmwareIDCs_Object((1,3,6,1,4,1,629,200,2,19,1,9),_NbsCmmcSysFirmwareIDCs_Type())
nbsCmmcSysFirmwareIDCs.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysFirmwareIDCs.setStatus(_A)
class _NbsCmmcSysFirmwareCksum_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_NbsCmmcSysFirmwareCksum_Type.__name__=_o
_NbsCmmcSysFirmwareCksum_Object=MibTableColumn
nbsCmmcSysFirmwareCksum=_NbsCmmcSysFirmwareCksum_Object((1,3,6,1,4,1,629,200,2,19,1,10),_NbsCmmcSysFirmwareCksum_Type())
nbsCmmcSysFirmwareCksum.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysFirmwareCksum.setStatus(_A)
class _NbsCmmcSysFirmwareMd5_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_NbsCmmcSysFirmwareMd5_Type.__name__=_T
_NbsCmmcSysFirmwareMd5_Object=MibTableColumn
nbsCmmcSysFirmwareMd5=_NbsCmmcSysFirmwareMd5_Object((1,3,6,1,4,1,629,200,2,19,1,11),_NbsCmmcSysFirmwareMd5_Type())
nbsCmmcSysFirmwareMd5.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysFirmwareMd5.setStatus(_A)
class _NbsCmmcSysTimeZone_Type(Integer32):defaultValue=14;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26)));namedValues=NamedValues(*((_F,1),('gmtMinus1200',2),('gmtMinus1100',3),('gmtMinus1000',4),('gmtMinus0900',5),('gmtMinus0800',6),('gmtMinus0700',7),('gmtMinus0600',8),('gmtMinus0500',9),('gmtMinus0400',10),('gmtMinus0300',11),('gmtMinus0200',12),('gmtMinus0100',13),('gmt',14),('gmtPlus0100',15),('gmtPlus0200',16),('gmtPlus0300',17),('gmtPlus0400',18),('gmtPlus0500',19),('gmtPlus0600',20),('gmtPlus0700',21),('gmtPlus0800',22),('gmtPlus0900',23),('gmtPlus1000',24),('gmtPlus1100',25),('gmtPlus1200',26)))
_NbsCmmcSysTimeZone_Type.__name__=_D
_NbsCmmcSysTimeZone_Object=MibScalar
nbsCmmcSysTimeZone=_NbsCmmcSysTimeZone_Object((1,3,6,1,4,1,629,200,2,20),_NbsCmmcSysTimeZone_Type())
nbsCmmcSysTimeZone.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysTimeZone.setStatus(_A)
class _NbsCmmcSysSnmpV1_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_P,2),(_Q,3)))
_NbsCmmcSysSnmpV1_Type.__name__=_D
_NbsCmmcSysSnmpV1_Object=MibScalar
nbsCmmcSysSnmpV1=_NbsCmmcSysSnmpV1_Object((1,3,6,1,4,1,629,200,2,21),_NbsCmmcSysSnmpV1_Type())
nbsCmmcSysSnmpV1.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysSnmpV1.setStatus(_A)
class _NbsCmmcSysSnmpV2c_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_P,2),(_Q,3)))
_NbsCmmcSysSnmpV2c_Type.__name__=_D
_NbsCmmcSysSnmpV2c_Object=MibScalar
nbsCmmcSysSnmpV2c=_NbsCmmcSysSnmpV2c_Object((1,3,6,1,4,1,629,200,2,22),_NbsCmmcSysSnmpV2c_Type())
nbsCmmcSysSnmpV2c.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysSnmpV2c.setStatus(_A)
class _NbsCmmcSysSnmpV3_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_P,2),(_Q,3)))
_NbsCmmcSysSnmpV3_Type.__name__=_D
_NbsCmmcSysSnmpV3_Object=MibScalar
nbsCmmcSysSnmpV3=_NbsCmmcSysSnmpV3_Object((1,3,6,1,4,1,629,200,2,23),_NbsCmmcSysSnmpV3_Type())
nbsCmmcSysSnmpV3.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysSnmpV3.setStatus(_A)
class _NbsCmmcSysStpAdmin_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_P,2),(_Q,3)))
_NbsCmmcSysStpAdmin_Type.__name__=_D
_NbsCmmcSysStpAdmin_Object=MibScalar
nbsCmmcSysStpAdmin=_NbsCmmcSysStpAdmin_Object((1,3,6,1,4,1,629,200,2,24),_NbsCmmcSysStpAdmin_Type())
nbsCmmcSysStpAdmin.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysStpAdmin.setStatus(_A)
class _NbsCmmcSysLockTypes_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_P,2),(_Q,3)))
_NbsCmmcSysLockTypes_Type.__name__=_D
_NbsCmmcSysLockTypes_Object=MibScalar
nbsCmmcSysLockTypes=_NbsCmmcSysLockTypes_Object((1,3,6,1,4,1,629,200,2,25),_NbsCmmcSysLockTypes_Type())
nbsCmmcSysLockTypes.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysLockTypes.setStatus(_A)
class _NbsCmmcSysSerialTerminalType_Type(DisplayString):defaultValue=OctetString('vt102');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NbsCmmcSysSerialTerminalType_Type.__name__=_J
_NbsCmmcSysSerialTerminalType_Object=MibScalar
nbsCmmcSysSerialTerminalType=_NbsCmmcSysSerialTerminalType_Object((1,3,6,1,4,1,629,200,2,26),_NbsCmmcSysSerialTerminalType_Type())
nbsCmmcSysSerialTerminalType.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysSerialTerminalType.setStatus(_A)
class _NbsCmmcSysCrossConnect_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_a,2),(_Y,3)))
_NbsCmmcSysCrossConnect_Type.__name__=_D
_NbsCmmcSysCrossConnect_Object=MibScalar
nbsCmmcSysCrossConnect=_NbsCmmcSysCrossConnect_Object((1,3,6,1,4,1,629,200,2,27),_NbsCmmcSysCrossConnect_Type())
nbsCmmcSysCrossConnect.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysCrossConnect.setStatus(_A)
class _NbsCmmcSysCountersState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_r,2),(_Y,3)))
_NbsCmmcSysCountersState_Type.__name__=_D
_NbsCmmcSysCountersState_Object=MibScalar
nbsCmmcSysCountersState=_NbsCmmcSysCountersState_Object((1,3,6,1,4,1,629,200,2,28),_NbsCmmcSysCountersState_Type())
nbsCmmcSysCountersState.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysCountersState.setStatus(_A)
class _NbsCmmcSysSerialBaudRateAdmin_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_AA,1),(_AB,2),(_AC,3),('b115200',4)))
_NbsCmmcSysSerialBaudRateAdmin_Type.__name__=_D
_NbsCmmcSysSerialBaudRateAdmin_Object=MibScalar
nbsCmmcSysSerialBaudRateAdmin=_NbsCmmcSysSerialBaudRateAdmin_Object((1,3,6,1,4,1,629,200,2,31),_NbsCmmcSysSerialBaudRateAdmin_Type())
nbsCmmcSysSerialBaudRateAdmin.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysSerialBaudRateAdmin.setStatus(_A)
class _NbsCmmcSysSerialBaudRateOper_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_AA,1),(_AB,2),(_AC,3),('b115200',4)))
_NbsCmmcSysSerialBaudRateOper_Type.__name__=_D
_NbsCmmcSysSerialBaudRateOper_Object=MibScalar
nbsCmmcSysSerialBaudRateOper=_NbsCmmcSysSerialBaudRateOper_Object((1,3,6,1,4,1,629,200,2,32),_NbsCmmcSysSerialBaudRateOper_Type())
nbsCmmcSysSerialBaudRateOper.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysSerialBaudRateOper.setStatus(_A)
class _NbsCmmcSysTimeServAddressType_Type(InetAddressType):defaultValue=0
_NbsCmmcSysTimeServAddressType_Type.__name__=_b
_NbsCmmcSysTimeServAddressType_Object=MibScalar
nbsCmmcSysTimeServAddressType=_NbsCmmcSysTimeServAddressType_Object((1,3,6,1,4,1,629,200,2,33),_NbsCmmcSysTimeServAddressType_Type())
nbsCmmcSysTimeServAddressType.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysTimeServAddressType.setStatus(_A)
_NbsCmmcSysTimeServAddress_Type=InetAddress
_NbsCmmcSysTimeServAddress_Object=MibScalar
nbsCmmcSysTimeServAddress=_NbsCmmcSysTimeServAddress_Object((1,3,6,1,4,1,629,200,2,34),_NbsCmmcSysTimeServAddress_Type())
nbsCmmcSysTimeServAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysTimeServAddress.setStatus(_A)
class _NbsCmmcSysDiscoveryOper_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_P,2),(_Q,3)))
_NbsCmmcSysDiscoveryOper_Type.__name__=_D
_NbsCmmcSysDiscoveryOper_Object=MibScalar
nbsCmmcSysDiscoveryOper=_NbsCmmcSysDiscoveryOper_Object((1,3,6,1,4,1,629,200,2,50),_NbsCmmcSysDiscoveryOper_Type())
nbsCmmcSysDiscoveryOper.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysDiscoveryOper.setStatus(_A)
class _NbsCmmcSysStpOper_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_P,2),(_Q,3)))
_NbsCmmcSysStpOper_Type.__name__=_D
_NbsCmmcSysStpOper_Object=MibScalar
nbsCmmcSysStpOper=_NbsCmmcSysStpOper_Object((1,3,6,1,4,1,629,200,2,60),_NbsCmmcSysStpOper_Type())
nbsCmmcSysStpOper.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysStpOper.setStatus(_A)
_NbsCmmcSysProtoTableSize_Type=Unsigned32
_NbsCmmcSysProtoTableSize_Object=MibScalar
nbsCmmcSysProtoTableSize=_NbsCmmcSysProtoTableSize_Object((1,3,6,1,4,1,629,200,2,1001),_NbsCmmcSysProtoTableSize_Type())
nbsCmmcSysProtoTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysProtoTableSize.setStatus(_A)
_NbsCmmcSysProtoTable_Object=MibTable
nbsCmmcSysProtoTable=_NbsCmmcSysProtoTable_Object((1,3,6,1,4,1,629,200,2,1002))
if mibBuilder.loadTexts:nbsCmmcSysProtoTable.setStatus(_A)
_NbsCmmcSysProtoEntry_Object=MibTableRow
nbsCmmcSysProtoEntry=_NbsCmmcSysProtoEntry_Object((1,3,6,1,4,1,629,200,2,1002,1))
nbsCmmcSysProtoEntry.setIndexNames((0,_B,_AR))
if mibBuilder.loadTexts:nbsCmmcSysProtoEntry.setStatus(_A)
_NbsCmmcSysProtoIndex_Type=Unsigned32
_NbsCmmcSysProtoIndex_Object=MibTableColumn
nbsCmmcSysProtoIndex=_NbsCmmcSysProtoIndex_Object((1,3,6,1,4,1,629,200,2,1002,1,1),_NbsCmmcSysProtoIndex_Type())
nbsCmmcSysProtoIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysProtoIndex.setStatus(_A)
class _NbsCmmcSysProtoFamily_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,16))
_NbsCmmcSysProtoFamily_Type.__name__=_J
_NbsCmmcSysProtoFamily_Object=MibTableColumn
nbsCmmcSysProtoFamily=_NbsCmmcSysProtoFamily_Object((1,3,6,1,4,1,629,200,2,1002,1,2),_NbsCmmcSysProtoFamily_Type())
nbsCmmcSysProtoFamily.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysProtoFamily.setStatus(_A)
class _NbsCmmcSysProtoRate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,60))
_NbsCmmcSysProtoRate_Type.__name__=_J
_NbsCmmcSysProtoRate_Object=MibTableColumn
nbsCmmcSysProtoRate=_NbsCmmcSysProtoRate_Object((1,3,6,1,4,1,629,200,2,1002,1,3),_NbsCmmcSysProtoRate_Type())
nbsCmmcSysProtoRate.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysProtoRate.setStatus(_A)
_NbsCmmcSysTimeZoneTableSize_Type=Unsigned32
_NbsCmmcSysTimeZoneTableSize_Object=MibScalar
nbsCmmcSysTimeZoneTableSize=_NbsCmmcSysTimeZoneTableSize_Object((1,3,6,1,4,1,629,200,2,1003),_NbsCmmcSysTimeZoneTableSize_Type())
nbsCmmcSysTimeZoneTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysTimeZoneTableSize.setStatus(_A)
_NbsCmmcSysTimeZoneTable_Object=MibTable
nbsCmmcSysTimeZoneTable=_NbsCmmcSysTimeZoneTable_Object((1,3,6,1,4,1,629,200,2,1004))
if mibBuilder.loadTexts:nbsCmmcSysTimeZoneTable.setStatus(_A)
_NbsCmmcSysTimeZoneEntry_Object=MibTableRow
nbsCmmcSysTimeZoneEntry=_NbsCmmcSysTimeZoneEntry_Object((1,3,6,1,4,1,629,200,2,1004,1))
nbsCmmcSysTimeZoneEntry.setIndexNames((0,_B,_AS))
if mibBuilder.loadTexts:nbsCmmcSysTimeZoneEntry.setStatus(_A)
_NbsCmmcSysTimeZoneIndex_Type=Unsigned32
_NbsCmmcSysTimeZoneIndex_Object=MibTableColumn
nbsCmmcSysTimeZoneIndex=_NbsCmmcSysTimeZoneIndex_Object((1,3,6,1,4,1,629,200,2,1004,1,1),_NbsCmmcSysTimeZoneIndex_Type())
nbsCmmcSysTimeZoneIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysTimeZoneIndex.setStatus(_A)
class _NbsCmmcSysTimeZoneName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,30))
_NbsCmmcSysTimeZoneName_Type.__name__=_J
_NbsCmmcSysTimeZoneName_Object=MibTableColumn
nbsCmmcSysTimeZoneName=_NbsCmmcSysTimeZoneName_Object((1,3,6,1,4,1,629,200,2,1004,1,2),_NbsCmmcSysTimeZoneName_Type())
nbsCmmcSysTimeZoneName.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysTimeZoneName.setStatus(_A)
_NbsCmmcSysLoaderTableSize_Type=Integer32
_NbsCmmcSysLoaderTableSize_Object=MibScalar
nbsCmmcSysLoaderTableSize=_NbsCmmcSysLoaderTableSize_Object((1,3,6,1,4,1,629,200,2,1010),_NbsCmmcSysLoaderTableSize_Type())
nbsCmmcSysLoaderTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysLoaderTableSize.setStatus(_A)
_NbsCmmcSysLoaderTable_Object=MibTable
nbsCmmcSysLoaderTable=_NbsCmmcSysLoaderTable_Object((1,3,6,1,4,1,629,200,2,1011))
if mibBuilder.loadTexts:nbsCmmcSysLoaderTable.setStatus(_A)
_NbsCmmcSysLoaderEntry_Object=MibTableRow
nbsCmmcSysLoaderEntry=_NbsCmmcSysLoaderEntry_Object((1,3,6,1,4,1,629,200,2,1011,1))
nbsCmmcSysLoaderEntry.setIndexNames((0,_B,_AT))
if mibBuilder.loadTexts:nbsCmmcSysLoaderEntry.setStatus(_A)
_NbsCmmcSysLoaderIndex_Type=Integer32
_NbsCmmcSysLoaderIndex_Object=MibTableColumn
nbsCmmcSysLoaderIndex=_NbsCmmcSysLoaderIndex_Object((1,3,6,1,4,1,629,200,2,1011,1,1),_NbsCmmcSysLoaderIndex_Type())
nbsCmmcSysLoaderIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysLoaderIndex.setStatus(_A)
_NbsCmmcSysLoaderFileId_Type=Integer32
_NbsCmmcSysLoaderFileId_Object=MibTableColumn
nbsCmmcSysLoaderFileId=_NbsCmmcSysLoaderFileId_Object((1,3,6,1,4,1,629,200,2,1011,1,2),_NbsCmmcSysLoaderFileId_Type())
nbsCmmcSysLoaderFileId.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysLoaderFileId.setStatus(_A)
_NbsCmmcSysLoaderProgress_Type=Integer32
_NbsCmmcSysLoaderProgress_Object=MibTableColumn
nbsCmmcSysLoaderProgress=_NbsCmmcSysLoaderProgress_Object((1,3,6,1,4,1,629,200,2,1011,1,3),_NbsCmmcSysLoaderProgress_Type())
nbsCmmcSysLoaderProgress.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysLoaderProgress.setStatus(_A)
class _NbsCmmcSysLoaderStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('idle',1),(_AU,2),(_AV,3),('aborted',4)))
_NbsCmmcSysLoaderStatus_Type.__name__=_D
_NbsCmmcSysLoaderStatus_Object=MibTableColumn
nbsCmmcSysLoaderStatus=_NbsCmmcSysLoaderStatus_Object((1,3,6,1,4,1,629,200,2,1011,1,4),_NbsCmmcSysLoaderStatus_Type())
nbsCmmcSysLoaderStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysLoaderStatus.setStatus(_A)
class _NbsCmmcSysLoaderAbort_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_p,2),('abort',3)))
_NbsCmmcSysLoaderAbort_Type.__name__=_D
_NbsCmmcSysLoaderAbort_Object=MibTableColumn
nbsCmmcSysLoaderAbort=_NbsCmmcSysLoaderAbort_Object((1,3,6,1,4,1,629,200,2,1011,1,5),_NbsCmmcSysLoaderAbort_Type())
nbsCmmcSysLoaderAbort.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysLoaderAbort.setStatus(_A)
class _NbsCmmcSysLoaderAck_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_p,2),('acknowledge',3)))
_NbsCmmcSysLoaderAck_Type.__name__=_D
_NbsCmmcSysLoaderAck_Object=MibTableColumn
nbsCmmcSysLoaderAck=_NbsCmmcSysLoaderAck_Object((1,3,6,1,4,1,629,200,2,1011,1,6),_NbsCmmcSysLoaderAck_Type())
nbsCmmcSysLoaderAck.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysLoaderAck.setStatus(_A)
_NbsCmmcSysLoaderFilename_Type=DisplayString
_NbsCmmcSysLoaderFilename_Object=MibTableColumn
nbsCmmcSysLoaderFilename=_NbsCmmcSysLoaderFilename_Object((1,3,6,1,4,1,629,200,2,1011,1,7),_NbsCmmcSysLoaderFilename_Type())
nbsCmmcSysLoaderFilename.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysLoaderFilename.setStatus(_A)
class _NbsCmmcSysFirmwareURL_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NbsCmmcSysFirmwareURL_Type.__name__=_J
_NbsCmmcSysFirmwareURL_Object=MibScalar
nbsCmmcSysFirmwareURL=_NbsCmmcSysFirmwareURL_Object((1,3,6,1,4,1,629,200,2,1020),_NbsCmmcSysFirmwareURL_Type())
nbsCmmcSysFirmwareURL.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysFirmwareURL.setStatus(_A)
class _NbsCmmcSysFirmwareURLStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),('idle',2),(_AU,3),(_AV,4),('failed',5)))
_NbsCmmcSysFirmwareURLStatus_Type.__name__=_D
_NbsCmmcSysFirmwareURLStatus_Object=MibScalar
nbsCmmcSysFirmwareURLStatus=_NbsCmmcSysFirmwareURLStatus_Object((1,3,6,1,4,1,629,200,2,1021),_NbsCmmcSysFirmwareURLStatus_Type())
nbsCmmcSysFirmwareURLStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysFirmwareURLStatus.setStatus(_A)
_NbsCmmcSysNVAreaTableSize_Type=Integer32
_NbsCmmcSysNVAreaTableSize_Object=MibScalar
nbsCmmcSysNVAreaTableSize=_NbsCmmcSysNVAreaTableSize_Object((1,3,6,1,4,1,629,200,2,3000),_NbsCmmcSysNVAreaTableSize_Type())
nbsCmmcSysNVAreaTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysNVAreaTableSize.setStatus(_A)
_NbsCmmcSysNVAreaTable_Object=MibTable
nbsCmmcSysNVAreaTable=_NbsCmmcSysNVAreaTable_Object((1,3,6,1,4,1,629,200,2,3001))
if mibBuilder.loadTexts:nbsCmmcSysNVAreaTable.setStatus(_A)
_NbsCmmcSysNVAreaEntry_Object=MibTableRow
nbsCmmcSysNVAreaEntry=_NbsCmmcSysNVAreaEntry_Object((1,3,6,1,4,1,629,200,2,3001,1))
nbsCmmcSysNVAreaEntry.setIndexNames((0,_B,_AW),(0,_B,_AX))
if mibBuilder.loadTexts:nbsCmmcSysNVAreaEntry.setStatus(_A)
class _NbsCmmcSysNVAreaIfIndex_Type(InterfaceIndex):subtypeSpec=InterfaceIndex.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100000,9999999))
_NbsCmmcSysNVAreaIfIndex_Type.__name__=_AM
_NbsCmmcSysNVAreaIfIndex_Object=MibTableColumn
nbsCmmcSysNVAreaIfIndex=_NbsCmmcSysNVAreaIfIndex_Object((1,3,6,1,4,1,629,200,2,3001,1,1),_NbsCmmcSysNVAreaIfIndex_Type())
nbsCmmcSysNVAreaIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysNVAreaIfIndex.setStatus(_A)
_NbsCmmcSysNVAreaBank_Type=Integer32
_NbsCmmcSysNVAreaBank_Object=MibTableColumn
nbsCmmcSysNVAreaBank=_NbsCmmcSysNVAreaBank_Object((1,3,6,1,4,1,629,200,2,3001,1,2),_NbsCmmcSysNVAreaBank_Type())
nbsCmmcSysNVAreaBank.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysNVAreaBank.setStatus(_A)
class _NbsCmmcSysNVAreaStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_q,1),('primary',2),('backup',3),('erased',4),('busy',5)))
_NbsCmmcSysNVAreaStatus_Type.__name__=_D
_NbsCmmcSysNVAreaStatus_Object=MibTableColumn
nbsCmmcSysNVAreaStatus=_NbsCmmcSysNVAreaStatus_Object((1,3,6,1,4,1,629,200,2,3001,1,3),_NbsCmmcSysNVAreaStatus_Type())
nbsCmmcSysNVAreaStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysNVAreaStatus.setStatus(_A)
class _NbsCmmcSysNVAreaDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NbsCmmcSysNVAreaDescr_Type.__name__=_J
_NbsCmmcSysNVAreaDescr_Object=MibTableColumn
nbsCmmcSysNVAreaDescr=_NbsCmmcSysNVAreaDescr_Object((1,3,6,1,4,1,629,200,2,3001,1,4),_NbsCmmcSysNVAreaDescr_Type())
nbsCmmcSysNVAreaDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysNVAreaDescr.setStatus(_A)
class _NbsCmmcSysNVAreaVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NbsCmmcSysNVAreaVersion_Type.__name__=_J
_NbsCmmcSysNVAreaVersion_Object=MibTableColumn
nbsCmmcSysNVAreaVersion=_NbsCmmcSysNVAreaVersion_Object((1,3,6,1,4,1,629,200,2,3001,1,5),_NbsCmmcSysNVAreaVersion_Type())
nbsCmmcSysNVAreaVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysNVAreaVersion.setStatus(_A)
class _NbsCmmcSysNVAreaCksum_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_NbsCmmcSysNVAreaCksum_Type.__name__=_o
_NbsCmmcSysNVAreaCksum_Object=MibTableColumn
nbsCmmcSysNVAreaCksum=_NbsCmmcSysNVAreaCksum_Object((1,3,6,1,4,1,629,200,2,3001,1,6),_NbsCmmcSysNVAreaCksum_Type())
nbsCmmcSysNVAreaCksum.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysNVAreaCksum.setStatus(_A)
_NbsCmmcIpSnmpGrp_ObjectIdentity=ObjectIdentity
nbsCmmcIpSnmpGrp=_NbsCmmcIpSnmpGrp_ObjectIdentity((1,3,6,1,4,1,629,200,3))
if mibBuilder.loadTexts:nbsCmmcIpSnmpGrp.setStatus(_A)
_NbsCmmcIpCfg_ObjectIdentity=ObjectIdentity
nbsCmmcIpCfg=_NbsCmmcIpCfg_ObjectIdentity((1,3,6,1,4,1,629,200,3,1))
_NbsCmmcPrvIpAddr_Type=IpAddress
_NbsCmmcPrvIpAddr_Object=MibScalar
nbsCmmcPrvIpAddr=_NbsCmmcPrvIpAddr_Object((1,3,6,1,4,1,629,200,3,1,1),_NbsCmmcPrvIpAddr_Type())
nbsCmmcPrvIpAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcPrvIpAddr.setStatus(_K)
_NbsCmmcPrvNetMask_Type=IpAddress
_NbsCmmcPrvNetMask_Object=MibScalar
nbsCmmcPrvNetMask=_NbsCmmcPrvNetMask_Object((1,3,6,1,4,1,629,200,3,1,2),_NbsCmmcPrvNetMask_Type())
nbsCmmcPrvNetMask.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcPrvNetMask.setStatus(_K)
_NbsCmmcPrvBcastAddr_Type=IpAddress
_NbsCmmcPrvBcastAddr_Object=MibScalar
nbsCmmcPrvBcastAddr=_NbsCmmcPrvBcastAddr_Object((1,3,6,1,4,1,629,200,3,1,3),_NbsCmmcPrvBcastAddr_Type())
nbsCmmcPrvBcastAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcPrvBcastAddr.setStatus(_K)
_NbsCmmcSysIpAddr_Type=IpAddress
_NbsCmmcSysIpAddr_Object=MibScalar
nbsCmmcSysIpAddr=_NbsCmmcSysIpAddr_Object((1,3,6,1,4,1,629,200,3,1,4),_NbsCmmcSysIpAddr_Type())
nbsCmmcSysIpAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysIpAddr.setStatus(_A)
_NbsCmmcSysNetMask_Type=IpAddress
_NbsCmmcSysNetMask_Object=MibScalar
nbsCmmcSysNetMask=_NbsCmmcSysNetMask_Object((1,3,6,1,4,1,629,200,3,1,5),_NbsCmmcSysNetMask_Type())
nbsCmmcSysNetMask.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysNetMask.setStatus(_A)
_NbsCmmcSysBcastAddr_Type=IpAddress
_NbsCmmcSysBcastAddr_Object=MibScalar
nbsCmmcSysBcastAddr=_NbsCmmcSysBcastAddr_Object((1,3,6,1,4,1,629,200,3,1,6),_NbsCmmcSysBcastAddr_Type())
nbsCmmcSysBcastAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysBcastAddr.setStatus(_A)
_NbsCmmcSysObIpAddr_Type=IpAddress
_NbsCmmcSysObIpAddr_Object=MibScalar
nbsCmmcSysObIpAddr=_NbsCmmcSysObIpAddr_Object((1,3,6,1,4,1,629,200,3,1,7),_NbsCmmcSysObIpAddr_Type())
nbsCmmcSysObIpAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysObIpAddr.setStatus(_K)
_NbsCmmcSysObNetMask_Type=IpAddress
_NbsCmmcSysObNetMask_Object=MibScalar
nbsCmmcSysObNetMask=_NbsCmmcSysObNetMask_Object((1,3,6,1,4,1,629,200,3,1,8),_NbsCmmcSysObNetMask_Type())
nbsCmmcSysObNetMask.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysObNetMask.setStatus(_K)
_NbsCmmcSysObBcastAddr_Type=IpAddress
_NbsCmmcSysObBcastAddr_Object=MibScalar
nbsCmmcSysObBcastAddr=_NbsCmmcSysObBcastAddr_Object((1,3,6,1,4,1,629,200,3,1,9),_NbsCmmcSysObBcastAddr_Type())
nbsCmmcSysObBcastAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysObBcastAddr.setStatus(_K)
_NbsCmmcSysDefaultGateway_Type=IpAddress
_NbsCmmcSysDefaultGateway_Object=MibScalar
nbsCmmcSysDefaultGateway=_NbsCmmcSysDefaultGateway_Object((1,3,6,1,4,1,629,200,3,1,10),_NbsCmmcSysDefaultGateway_Type())
nbsCmmcSysDefaultGateway.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysDefaultGateway.setStatus(_A)
class _NbsCmmcSysAdminBootpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_NbsCmmcSysAdminBootpState_Type.__name__=_D
_NbsCmmcSysAdminBootpState_Object=MibScalar
nbsCmmcSysAdminBootpState=_NbsCmmcSysAdminBootpState_Object((1,3,6,1,4,1,629,200,3,1,11),_NbsCmmcSysAdminBootpState_Type())
nbsCmmcSysAdminBootpState.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysAdminBootpState.setStatus(_A)
class _NbsCmmcSysRunBootpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_NbsCmmcSysRunBootpState_Type.__name__=_D
_NbsCmmcSysRunBootpState_Object=MibScalar
nbsCmmcSysRunBootpState=_NbsCmmcSysRunBootpState_Object((1,3,6,1,4,1,629,200,3,1,12),_NbsCmmcSysRunBootpState_Type())
nbsCmmcSysRunBootpState.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysRunBootpState.setStatus(_A)
class _NbsCmmcSysSerialLineMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('adminIf',1),('slipIf',2)))
_NbsCmmcSysSerialLineMode_Type.__name__=_D
_NbsCmmcSysSerialLineMode_Object=MibScalar
nbsCmmcSysSerialLineMode=_NbsCmmcSysSerialLineMode_Object((1,3,6,1,4,1,629,200,3,1,13),_NbsCmmcSysSerialLineMode_Type())
nbsCmmcSysSerialLineMode.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysSerialLineMode.setStatus(_A)
class _NbsCmmcSysSerialSlipBaudRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_AA,1),(_AB,2),(_AC,3)))
_NbsCmmcSysSerialSlipBaudRate_Type.__name__=_D
_NbsCmmcSysSerialSlipBaudRate_Object=MibScalar
nbsCmmcSysSerialSlipBaudRate=_NbsCmmcSysSerialSlipBaudRate_Object((1,3,6,1,4,1,629,200,3,1,14),_NbsCmmcSysSerialSlipBaudRate_Type())
nbsCmmcSysSerialSlipBaudRate.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysSerialSlipBaudRate.setStatus(_K)
class _NbsCmmcSysArpAgingTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_NbsCmmcSysArpAgingTime_Type.__name__=_D
_NbsCmmcSysArpAgingTime_Object=MibScalar
nbsCmmcSysArpAgingTime=_NbsCmmcSysArpAgingTime_Object((1,3,6,1,4,1,629,200,3,1,15),_NbsCmmcSysArpAgingTime_Type())
nbsCmmcSysArpAgingTime.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysArpAgingTime.setStatus(_A)
_NbsCmmcSysMaxTelnetSessions_Type=Integer32
_NbsCmmcSysMaxTelnetSessions_Object=MibScalar
nbsCmmcSysMaxTelnetSessions=_NbsCmmcSysMaxTelnetSessions_Object((1,3,6,1,4,1,629,200,3,1,16),_NbsCmmcSysMaxTelnetSessions_Type())
nbsCmmcSysMaxTelnetSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysMaxTelnetSessions.setStatus(_K)
_NbsCmmcSysTelnetTable_Object=MibTable
nbsCmmcSysTelnetTable=_NbsCmmcSysTelnetTable_Object((1,3,6,1,4,1,629,200,3,1,17))
if mibBuilder.loadTexts:nbsCmmcSysTelnetTable.setStatus(_K)
_NbsCmmcSysTelnetEntry_Object=MibTableRow
nbsCmmcSysTelnetEntry=_NbsCmmcSysTelnetEntry_Object((1,3,6,1,4,1,629,200,3,1,17,1))
nbsCmmcSysTelnetEntry.setIndexNames((0,_B,_AY))
if mibBuilder.loadTexts:nbsCmmcSysTelnetEntry.setStatus(_K)
_NbsCmmcSysTelnetSessionIndex_Type=Integer32
_NbsCmmcSysTelnetSessionIndex_Object=MibTableColumn
nbsCmmcSysTelnetSessionIndex=_NbsCmmcSysTelnetSessionIndex_Object((1,3,6,1,4,1,629,200,3,1,17,1,1),_NbsCmmcSysTelnetSessionIndex_Type())
nbsCmmcSysTelnetSessionIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysTelnetSessionIndex.setStatus(_K)
class _NbsCmmcSysTelnetSessionStat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('connected',1),('disconnect',2)))
_NbsCmmcSysTelnetSessionStat_Type.__name__=_D
_NbsCmmcSysTelnetSessionStat_Object=MibTableColumn
nbsCmmcSysTelnetSessionStat=_NbsCmmcSysTelnetSessionStat_Object((1,3,6,1,4,1,629,200,3,1,17,1,2),_NbsCmmcSysTelnetSessionStat_Type())
nbsCmmcSysTelnetSessionStat.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysTelnetSessionStat.setStatus(_K)
_NbsCmmcSysTelnetHost_Type=IpAddress
_NbsCmmcSysTelnetHost_Object=MibTableColumn
nbsCmmcSysTelnetHost=_NbsCmmcSysTelnetHost_Object((1,3,6,1,4,1,629,200,3,1,17,1,3),_NbsCmmcSysTelnetHost_Type())
nbsCmmcSysTelnetHost.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysTelnetHost.setStatus(_K)
_NbsCmmcSysTelnetHostPort_Type=Integer32
_NbsCmmcSysTelnetHostPort_Object=MibTableColumn
nbsCmmcSysTelnetHostPort=_NbsCmmcSysTelnetHostPort_Object((1,3,6,1,4,1,629,200,3,1,17,1,4),_NbsCmmcSysTelnetHostPort_Type())
nbsCmmcSysTelnetHostPort.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysTelnetHostPort.setStatus(_K)
_NbsCmmcSysTelnetLocal_Type=IpAddress
_NbsCmmcSysTelnetLocal_Object=MibTableColumn
nbsCmmcSysTelnetLocal=_NbsCmmcSysTelnetLocal_Object((1,3,6,1,4,1,629,200,3,1,17,1,5),_NbsCmmcSysTelnetLocal_Type())
nbsCmmcSysTelnetLocal.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysTelnetLocal.setStatus(_K)
_NbsCmmcSysTelnetLocalPort_Type=Integer32
_NbsCmmcSysTelnetLocalPort_Object=MibTableColumn
nbsCmmcSysTelnetLocalPort=_NbsCmmcSysTelnetLocalPort_Object((1,3,6,1,4,1,629,200,3,1,17,1,6),_NbsCmmcSysTelnetLocalPort_Type())
nbsCmmcSysTelnetLocalPort.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysTelnetLocalPort.setStatus(_K)
_NbsCmmcSysTelnetSessionId_Type=Integer32
_NbsCmmcSysTelnetSessionId_Object=MibTableColumn
nbsCmmcSysTelnetSessionId=_NbsCmmcSysTelnetSessionId_Object((1,3,6,1,4,1,629,200,3,1,17,1,7),_NbsCmmcSysTelnetSessionId_Type())
nbsCmmcSysTelnetSessionId.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysTelnetSessionId.setStatus(_K)
class _NbsCmmcSysTelnetConnectTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NbsCmmcSysTelnetConnectTime_Type.__name__=_J
_NbsCmmcSysTelnetConnectTime_Object=MibTableColumn
nbsCmmcSysTelnetConnectTime=_NbsCmmcSysTelnetConnectTime_Object((1,3,6,1,4,1,629,200,3,1,17,1,8),_NbsCmmcSysTelnetConnectTime_Type())
nbsCmmcSysTelnetConnectTime.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysTelnetConnectTime.setStatus(_K)
_NbsCmmcSysTelnetHostAddressType_Type=InetAddressType
_NbsCmmcSysTelnetHostAddressType_Object=MibTableColumn
nbsCmmcSysTelnetHostAddressType=_NbsCmmcSysTelnetHostAddressType_Object((1,3,6,1,4,1,629,200,3,1,17,1,9),_NbsCmmcSysTelnetHostAddressType_Type())
nbsCmmcSysTelnetHostAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysTelnetHostAddressType.setStatus(_K)
_NbsCmmcSysTelnetHostAddress_Type=InetAddress
_NbsCmmcSysTelnetHostAddress_Object=MibTableColumn
nbsCmmcSysTelnetHostAddress=_NbsCmmcSysTelnetHostAddress_Object((1,3,6,1,4,1,629,200,3,1,17,1,10),_NbsCmmcSysTelnetHostAddress_Type())
nbsCmmcSysTelnetHostAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysTelnetHostAddress.setStatus(_K)
_NbsCmmcSysTelnetLocalAddressType_Type=InetAddressType
_NbsCmmcSysTelnetLocalAddressType_Object=MibTableColumn
nbsCmmcSysTelnetLocalAddressType=_NbsCmmcSysTelnetLocalAddressType_Object((1,3,6,1,4,1,629,200,3,1,17,1,11),_NbsCmmcSysTelnetLocalAddressType_Type())
nbsCmmcSysTelnetLocalAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysTelnetLocalAddressType.setStatus(_K)
_NbsCmmcSysTelnetLocalAddress_Type=InetAddress
_NbsCmmcSysTelnetLocalAddress_Object=MibTableColumn
nbsCmmcSysTelnetLocalAddress=_NbsCmmcSysTelnetLocalAddress_Object((1,3,6,1,4,1,629,200,3,1,17,1,12),_NbsCmmcSysTelnetLocalAddress_Type())
nbsCmmcSysTelnetLocalAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysTelnetLocalAddress.setStatus(_K)
_NbsCmmcSysMaxPingSessions_Type=Integer32
_NbsCmmcSysMaxPingSessions_Object=MibScalar
nbsCmmcSysMaxPingSessions=_NbsCmmcSysMaxPingSessions_Object((1,3,6,1,4,1,629,200,3,1,18),_NbsCmmcSysMaxPingSessions_Type())
nbsCmmcSysMaxPingSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysMaxPingSessions.setStatus(_K)
_NbsCmmcSysPingTable_Object=MibTable
nbsCmmcSysPingTable=_NbsCmmcSysPingTable_Object((1,3,6,1,4,1,629,200,3,1,19))
if mibBuilder.loadTexts:nbsCmmcSysPingTable.setStatus(_K)
_NbsCmmcSysPingEntry_Object=MibTableRow
nbsCmmcSysPingEntry=_NbsCmmcSysPingEntry_Object((1,3,6,1,4,1,629,200,3,1,19,1))
nbsCmmcSysPingEntry.setIndexNames((0,_B,_AZ))
if mibBuilder.loadTexts:nbsCmmcSysPingEntry.setStatus(_K)
_NbsCmmcSysPingSessionIndex_Type=Integer32
_NbsCmmcSysPingSessionIndex_Object=MibTableColumn
nbsCmmcSysPingSessionIndex=_NbsCmmcSysPingSessionIndex_Object((1,3,6,1,4,1,629,200,3,1,19,1,1),_NbsCmmcSysPingSessionIndex_Type())
nbsCmmcSysPingSessionIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysPingSessionIndex.setStatus(_K)
class _NbsCmmcSysPingSessionStat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('idlePing',1),('runPing',2)))
_NbsCmmcSysPingSessionStat_Type.__name__=_D
_NbsCmmcSysPingSessionStat_Object=MibTableColumn
nbsCmmcSysPingSessionStat=_NbsCmmcSysPingSessionStat_Object((1,3,6,1,4,1,629,200,3,1,19,1,2),_NbsCmmcSysPingSessionStat_Type())
nbsCmmcSysPingSessionStat.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysPingSessionStat.setStatus(_K)
class _NbsCmmcSysPingAddr_Type(IpAddress):defaultHexValue='7F000001'
_NbsCmmcSysPingAddr_Type.__name__=_e
_NbsCmmcSysPingAddr_Object=MibTableColumn
nbsCmmcSysPingAddr=_NbsCmmcSysPingAddr_Object((1,3,6,1,4,1,629,200,3,1,19,1,3),_NbsCmmcSysPingAddr_Type())
nbsCmmcSysPingAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysPingAddr.setStatus(_K)
_NbsCmmcSysPingNumber_Type=Counter32
_NbsCmmcSysPingNumber_Object=MibTableColumn
nbsCmmcSysPingNumber=_NbsCmmcSysPingNumber_Object((1,3,6,1,4,1,629,200,3,1,19,1,4),_NbsCmmcSysPingNumber_Type())
nbsCmmcSysPingNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysPingNumber.setStatus(_K)
class _NbsCmmcSysPingOwner_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('adminInterface',2),('snmpAgent',3),('webManager',4)))
_NbsCmmcSysPingOwner_Type.__name__=_D
_NbsCmmcSysPingOwner_Object=MibTableColumn
nbsCmmcSysPingOwner=_NbsCmmcSysPingOwner_Object((1,3,6,1,4,1,629,200,3,1,19,1,5),_NbsCmmcSysPingOwner_Type())
nbsCmmcSysPingOwner.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysPingOwner.setStatus(_K)
_NbsCmmcSysPingRequests_Type=Counter32
_NbsCmmcSysPingRequests_Object=MibTableColumn
nbsCmmcSysPingRequests=_NbsCmmcSysPingRequests_Object((1,3,6,1,4,1,629,200,3,1,19,1,6),_NbsCmmcSysPingRequests_Type())
nbsCmmcSysPingRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysPingRequests.setStatus(_K)
_NbsCmmcSysPingResponses_Type=Counter32
_NbsCmmcSysPingResponses_Object=MibTableColumn
nbsCmmcSysPingResponses=_NbsCmmcSysPingResponses_Object((1,3,6,1,4,1,629,200,3,1,19,1,7),_NbsCmmcSysPingResponses_Type())
nbsCmmcSysPingResponses.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysPingResponses.setStatus(_K)
class _NbsCmmcSysPingAddressType_Type(InetAddressType):defaultValue=0
_NbsCmmcSysPingAddressType_Type.__name__=_b
_NbsCmmcSysPingAddressType_Object=MibTableColumn
nbsCmmcSysPingAddressType=_NbsCmmcSysPingAddressType_Object((1,3,6,1,4,1,629,200,3,1,19,1,8),_NbsCmmcSysPingAddressType_Type())
nbsCmmcSysPingAddressType.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysPingAddressType.setStatus(_K)
_NbsCmmcSysPingAddress_Type=InetAddress
_NbsCmmcSysPingAddress_Object=MibTableColumn
nbsCmmcSysPingAddress=_NbsCmmcSysPingAddress_Object((1,3,6,1,4,1,629,200,3,1,19,1,9),_NbsCmmcSysPingAddress_Type())
nbsCmmcSysPingAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysPingAddress.setStatus(_K)
class _NbsCmmcSysTelnetServer_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_P,2),(_Q,3)))
_NbsCmmcSysTelnetServer_Type.__name__=_D
_NbsCmmcSysTelnetServer_Object=MibScalar
nbsCmmcSysTelnetServer=_NbsCmmcSysTelnetServer_Object((1,3,6,1,4,1,629,200,3,1,20),_NbsCmmcSysTelnetServer_Type())
nbsCmmcSysTelnetServer.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysTelnetServer.setStatus(_A)
class _NbsCmmcSysSshServer_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_P,2),(_Q,3)))
_NbsCmmcSysSshServer_Type.__name__=_D
_NbsCmmcSysSshServer_Object=MibScalar
nbsCmmcSysSshServer=_NbsCmmcSysSshServer_Object((1,3,6,1,4,1,629,200,3,1,21),_NbsCmmcSysSshServer_Type())
nbsCmmcSysSshServer.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysSshServer.setStatus(_A)
_NbsCmmcSysIpAddrOper_Type=IpAddress
_NbsCmmcSysIpAddrOper_Object=MibScalar
nbsCmmcSysIpAddrOper=_NbsCmmcSysIpAddrOper_Object((1,3,6,1,4,1,629,200,3,1,22),_NbsCmmcSysIpAddrOper_Type())
nbsCmmcSysIpAddrOper.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysIpAddrOper.setStatus(_A)
_NbsCmmcSysNetMaskOper_Type=IpAddress
_NbsCmmcSysNetMaskOper_Object=MibScalar
nbsCmmcSysNetMaskOper=_NbsCmmcSysNetMaskOper_Object((1,3,6,1,4,1,629,200,3,1,23),_NbsCmmcSysNetMaskOper_Type())
nbsCmmcSysNetMaskOper.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysNetMaskOper.setStatus(_A)
_NbsCmmcSysBcastAddrOper_Type=IpAddress
_NbsCmmcSysBcastAddrOper_Object=MibScalar
nbsCmmcSysBcastAddrOper=_NbsCmmcSysBcastAddrOper_Object((1,3,6,1,4,1,629,200,3,1,24),_NbsCmmcSysBcastAddrOper_Type())
nbsCmmcSysBcastAddrOper.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysBcastAddrOper.setStatus(_A)
_NbsCmmcSysDefaultGatewayOper_Type=IpAddress
_NbsCmmcSysDefaultGatewayOper_Object=MibScalar
nbsCmmcSysDefaultGatewayOper=_NbsCmmcSysDefaultGatewayOper_Object((1,3,6,1,4,1,629,200,3,1,25),_NbsCmmcSysDefaultGatewayOper_Type())
nbsCmmcSysDefaultGatewayOper.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysDefaultGatewayOper.setStatus(_A)
class _NbsCmmcSysWebServer_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_P,2),(_Q,3)))
_NbsCmmcSysWebServer_Type.__name__=_D
_NbsCmmcSysWebServer_Object=MibScalar
nbsCmmcSysWebServer=_NbsCmmcSysWebServer_Object((1,3,6,1,4,1,629,200,3,1,26),_NbsCmmcSysWebServer_Type())
nbsCmmcSysWebServer.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysWebServer.setStatus(_A)
class _NbsCmmcSysWebPort_Type(Integer32):defaultValue=80;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_NbsCmmcSysWebPort_Type.__name__=_D
_NbsCmmcSysWebPort_Object=MibScalar
nbsCmmcSysWebPort=_NbsCmmcSysWebPort_Object((1,3,6,1,4,1,629,200,3,1,27),_NbsCmmcSysWebPort_Type())
nbsCmmcSysWebPort.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysWebPort.setStatus(_A)
class _NbsCmmcSysTelnetPort_Type(Integer32):defaultValue=23;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_NbsCmmcSysTelnetPort_Type.__name__=_D
_NbsCmmcSysTelnetPort_Object=MibScalar
nbsCmmcSysTelnetPort=_NbsCmmcSysTelnetPort_Object((1,3,6,1,4,1,629,200,3,1,28),_NbsCmmcSysTelnetPort_Type())
nbsCmmcSysTelnetPort.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysTelnetPort.setStatus(_A)
class _NbsCmmcSysSshPort_Type(Integer32):defaultValue=22;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_NbsCmmcSysSshPort_Type.__name__=_D
_NbsCmmcSysSshPort_Object=MibScalar
nbsCmmcSysSshPort=_NbsCmmcSysSshPort_Object((1,3,6,1,4,1,629,200,3,1,29),_NbsCmmcSysSshPort_Type())
nbsCmmcSysSshPort.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysSshPort.setStatus(_A)
class _NbsCmmcSysScpServer_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_P,2),(_Q,3)))
_NbsCmmcSysScpServer_Type.__name__=_D
_NbsCmmcSysScpServer_Object=MibScalar
nbsCmmcSysScpServer=_NbsCmmcSysScpServer_Object((1,3,6,1,4,1,629,200,3,1,30),_NbsCmmcSysScpServer_Type())
nbsCmmcSysScpServer.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysScpServer.setStatus(_A)
_NbsCmmcSnmpCfg_ObjectIdentity=ObjectIdentity
nbsCmmcSnmpCfg=_NbsCmmcSnmpCfg_ObjectIdentity((1,3,6,1,4,1,629,200,3,2))
class _NbsCmmcSysWriteCommunity_Type(DisplayString):defaultValue=OctetString('private');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NbsCmmcSysWriteCommunity_Type.__name__=_J
_NbsCmmcSysWriteCommunity_Object=MibScalar
nbsCmmcSysWriteCommunity=_NbsCmmcSysWriteCommunity_Object((1,3,6,1,4,1,629,200,3,2,1),_NbsCmmcSysWriteCommunity_Type())
nbsCmmcSysWriteCommunity.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysWriteCommunity.setStatus(_A)
class _NbsCmmcSysReadCommunity_Type(DisplayString):defaultValue=OctetString('public');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NbsCmmcSysReadCommunity_Type.__name__=_J
_NbsCmmcSysReadCommunity_Object=MibScalar
nbsCmmcSysReadCommunity=_NbsCmmcSysReadCommunity_Object((1,3,6,1,4,1,629,200,3,2,2),_NbsCmmcSysReadCommunity_Type())
nbsCmmcSysReadCommunity.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysReadCommunity.setStatus(_A)
_NbsCmmcSysTrapTblMaxSize_Type=Integer32
_NbsCmmcSysTrapTblMaxSize_Object=MibScalar
nbsCmmcSysTrapTblMaxSize=_NbsCmmcSysTrapTblMaxSize_Object((1,3,6,1,4,1,629,200,3,2,3),_NbsCmmcSysTrapTblMaxSize_Type())
nbsCmmcSysTrapTblMaxSize.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysTrapTblMaxSize.setStatus(_A)
_NbsCmmcSysTrapTable_Object=MibTable
nbsCmmcSysTrapTable=_NbsCmmcSysTrapTable_Object((1,3,6,1,4,1,629,200,3,2,4))
if mibBuilder.loadTexts:nbsCmmcSysTrapTable.setStatus(_A)
_NbsCmmcSysTrapEntry_Object=MibTableRow
nbsCmmcSysTrapEntry=_NbsCmmcSysTrapEntry_Object((1,3,6,1,4,1,629,200,3,2,4,1))
nbsCmmcSysTrapEntry.setIndexNames((0,_B,_Aa))
if mibBuilder.loadTexts:nbsCmmcSysTrapEntry.setStatus(_A)
_NbsCmmcSysTrapTblEntIndex_Type=Integer32
_NbsCmmcSysTrapTblEntIndex_Object=MibTableColumn
nbsCmmcSysTrapTblEntIndex=_NbsCmmcSysTrapTblEntIndex_Object((1,3,6,1,4,1,629,200,3,2,4,1,1),_NbsCmmcSysTrapTblEntIndex_Type())
nbsCmmcSysTrapTblEntIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysTrapTblEntIndex.setStatus(_A)
class _NbsCmmcSysTrapTblEntStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_q,1),(_AD,2)))
_NbsCmmcSysTrapTblEntStatus_Type.__name__=_D
_NbsCmmcSysTrapTblEntStatus_Object=MibTableColumn
nbsCmmcSysTrapTblEntStatus=_NbsCmmcSysTrapTblEntStatus_Object((1,3,6,1,4,1,629,200,3,2,4,1,2),_NbsCmmcSysTrapTblEntStatus_Type())
nbsCmmcSysTrapTblEntStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysTrapTblEntStatus.setStatus(_A)
_NbsCmmcSysTrapTblEntIpAddr_Type=IpAddress
_NbsCmmcSysTrapTblEntIpAddr_Object=MibTableColumn
nbsCmmcSysTrapTblEntIpAddr=_NbsCmmcSysTrapTblEntIpAddr_Object((1,3,6,1,4,1,629,200,3,2,4,1,3),_NbsCmmcSysTrapTblEntIpAddr_Type())
nbsCmmcSysTrapTblEntIpAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysTrapTblEntIpAddr.setStatus(_A)
class _NbsCmmcSysTrapTblEntComm_Type(DisplayString):defaultValue=OctetString('public');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NbsCmmcSysTrapTblEntComm_Type.__name__=_J
_NbsCmmcSysTrapTblEntComm_Object=MibTableColumn
nbsCmmcSysTrapTblEntComm=_NbsCmmcSysTrapTblEntComm_Object((1,3,6,1,4,1,629,200,3,2,4,1,4),_NbsCmmcSysTrapTblEntComm_Type())
nbsCmmcSysTrapTblEntComm.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysTrapTblEntComm.setStatus(_A)
class _NbsCmmcSysTrapTblEntLevel_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_P,1),(_f,2),(_c,3),(_d,4),(_AE,5),(_Ab,6),(_g,7)))
_NbsCmmcSysTrapTblEntLevel_Type.__name__=_D
_NbsCmmcSysTrapTblEntLevel_Object=MibTableColumn
nbsCmmcSysTrapTblEntLevel=_NbsCmmcSysTrapTblEntLevel_Object((1,3,6,1,4,1,629,200,3,2,4,1,5),_NbsCmmcSysTrapTblEntLevel_Type())
nbsCmmcSysTrapTblEntLevel.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysTrapTblEntLevel.setStatus(_A)
class _NbsCmmcSysTrapTblEntPort_Type(Integer32):defaultValue=162;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_NbsCmmcSysTrapTblEntPort_Type.__name__=_D
_NbsCmmcSysTrapTblEntPort_Object=MibTableColumn
nbsCmmcSysTrapTblEntPort=_NbsCmmcSysTrapTblEntPort_Object((1,3,6,1,4,1,629,200,3,2,4,1,6),_NbsCmmcSysTrapTblEntPort_Type())
nbsCmmcSysTrapTblEntPort.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysTrapTblEntPort.setStatus(_A)
class _NbsCmmcSysTrapTblEntAddressType_Type(InetAddressType):defaultValue=0
_NbsCmmcSysTrapTblEntAddressType_Type.__name__=_b
_NbsCmmcSysTrapTblEntAddressType_Object=MibTableColumn
nbsCmmcSysTrapTblEntAddressType=_NbsCmmcSysTrapTblEntAddressType_Object((1,3,6,1,4,1,629,200,3,2,4,1,7),_NbsCmmcSysTrapTblEntAddressType_Type())
nbsCmmcSysTrapTblEntAddressType.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysTrapTblEntAddressType.setStatus(_A)
_NbsCmmcSysTrapTblEntRecipient_Type=InetAddress
_NbsCmmcSysTrapTblEntRecipient_Object=MibTableColumn
nbsCmmcSysTrapTblEntRecipient=_NbsCmmcSysTrapTblEntRecipient_Object((1,3,6,1,4,1,629,200,3,2,4,1,8),_NbsCmmcSysTrapTblEntRecipient_Type())
nbsCmmcSysTrapTblEntRecipient.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysTrapTblEntRecipient.setStatus(_A)
class _NbsCmmcSysEnablePowerSupplyTraps_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_NbsCmmcSysEnablePowerSupplyTraps_Type.__name__=_D
_NbsCmmcSysEnablePowerSupplyTraps_Object=MibScalar
nbsCmmcSysEnablePowerSupplyTraps=_NbsCmmcSysEnablePowerSupplyTraps_Object((1,3,6,1,4,1,629,200,3,2,11),_NbsCmmcSysEnablePowerSupplyTraps_Type())
nbsCmmcSysEnablePowerSupplyTraps.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysEnablePowerSupplyTraps.setStatus(_A)
class _NbsCmmcSysEnableModuleTraps_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_NbsCmmcSysEnableModuleTraps_Type.__name__=_D
_NbsCmmcSysEnableModuleTraps_Object=MibScalar
nbsCmmcSysEnableModuleTraps=_NbsCmmcSysEnableModuleTraps_Object((1,3,6,1,4,1,629,200,3,2,12),_NbsCmmcSysEnableModuleTraps_Type())
nbsCmmcSysEnableModuleTraps.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysEnableModuleTraps.setStatus(_A)
class _NbsCmmcSysEnableBridgeTraps_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_NbsCmmcSysEnableBridgeTraps_Type.__name__=_D
_NbsCmmcSysEnableBridgeTraps_Object=MibScalar
nbsCmmcSysEnableBridgeTraps=_NbsCmmcSysEnableBridgeTraps_Object((1,3,6,1,4,1,629,200,3,2,13),_NbsCmmcSysEnableBridgeTraps_Type())
nbsCmmcSysEnableBridgeTraps.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysEnableBridgeTraps.setStatus(_A)
class _NbsCmmcSysEnableIpAccessTraps_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_NbsCmmcSysEnableIpAccessTraps_Type.__name__=_D
_NbsCmmcSysEnableIpAccessTraps_Object=MibScalar
nbsCmmcSysEnableIpAccessTraps=_NbsCmmcSysEnableIpAccessTraps_Object((1,3,6,1,4,1,629,200,3,2,14),_NbsCmmcSysEnableIpAccessTraps_Type())
nbsCmmcSysEnableIpAccessTraps.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysEnableIpAccessTraps.setStatus(_A)
class _NbsCmmcSysSnmpPortAdmin_Type(Integer32):defaultValue=161;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_NbsCmmcSysSnmpPortAdmin_Type.__name__=_D
_NbsCmmcSysSnmpPortAdmin_Object=MibScalar
nbsCmmcSysSnmpPortAdmin=_NbsCmmcSysSnmpPortAdmin_Object((1,3,6,1,4,1,629,200,3,2,15),_NbsCmmcSysSnmpPortAdmin_Type())
nbsCmmcSysSnmpPortAdmin.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysSnmpPortAdmin.setStatus(_A)
class _NbsCmmcSysSnmpPortOper_Type(Integer32):defaultValue=161;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_NbsCmmcSysSnmpPortOper_Type.__name__=_D
_NbsCmmcSysSnmpPortOper_Object=MibScalar
nbsCmmcSysSnmpPortOper=_NbsCmmcSysSnmpPortOper_Object((1,3,6,1,4,1,629,200,3,2,16),_NbsCmmcSysSnmpPortOper_Type())
nbsCmmcSysSnmpPortOper.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysSnmpPortOper.setStatus(_A)
_NbsCmmcTftpGrp_ObjectIdentity=ObjectIdentity
nbsCmmcTftpGrp=_NbsCmmcTftpGrp_ObjectIdentity((1,3,6,1,4,1,629,200,4))
if mibBuilder.loadTexts:nbsCmmcTftpGrp.setStatus(_A)
class _NbsCmmcSysTftpHostIP_Type(IpAddress):defaultHexValue=_A9
_NbsCmmcSysTftpHostIP_Type.__name__=_e
_NbsCmmcSysTftpHostIP_Object=MibScalar
nbsCmmcSysTftpHostIP=_NbsCmmcSysTftpHostIP_Object((1,3,6,1,4,1,629,200,4,1),_NbsCmmcSysTftpHostIP_Type())
nbsCmmcSysTftpHostIP.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysTftpHostIP.setStatus(_A)
class _NbsCmmcTftpMaxSessionNum_Type(Integer32):defaultValue=5
_NbsCmmcTftpMaxSessionNum_Type.__name__=_D
_NbsCmmcTftpMaxSessionNum_Object=MibScalar
nbsCmmcTftpMaxSessionNum=_NbsCmmcTftpMaxSessionNum_Object((1,3,6,1,4,1,629,200,4,2),_NbsCmmcTftpMaxSessionNum_Type())
nbsCmmcTftpMaxSessionNum.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcTftpMaxSessionNum.setStatus(_A)
_NbsCmmcTftpSessTable_Object=MibTable
nbsCmmcTftpSessTable=_NbsCmmcTftpSessTable_Object((1,3,6,1,4,1,629,200,4,3))
if mibBuilder.loadTexts:nbsCmmcTftpSessTable.setStatus(_A)
_NbsCmmcTftpSessEntry_Object=MibTableRow
nbsCmmcTftpSessEntry=_NbsCmmcTftpSessEntry_Object((1,3,6,1,4,1,629,200,4,3,1))
nbsCmmcTftpSessEntry.setIndexNames((0,_B,_Ac))
if mibBuilder.loadTexts:nbsCmmcTftpSessEntry.setStatus(_A)
_NbsCmmcTftpSessIndex_Type=Integer32
_NbsCmmcTftpSessIndex_Object=MibTableColumn
nbsCmmcTftpSessIndex=_NbsCmmcTftpSessIndex_Object((1,3,6,1,4,1,629,200,4,3,1,1),_NbsCmmcTftpSessIndex_Type())
nbsCmmcTftpSessIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcTftpSessIndex.setStatus(_A)
class _NbsCmmcTftpSessStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('inactive',1),('create',2),('underCreation',3),(_AD,4),('transferEnded',5),('failed',6)))
_NbsCmmcTftpSessStatus_Type.__name__=_D
_NbsCmmcTftpSessStatus_Object=MibTableColumn
nbsCmmcTftpSessStatus=_NbsCmmcTftpSessStatus_Object((1,3,6,1,4,1,629,200,4,3,1,2),_NbsCmmcTftpSessStatus_Type())
nbsCmmcTftpSessStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcTftpSessStatus.setStatus(_A)
class _NbsCmmcTftpSessHostIp_Type(IpAddress):defaultHexValue=_A9
_NbsCmmcTftpSessHostIp_Type.__name__=_e
_NbsCmmcTftpSessHostIp_Object=MibTableColumn
nbsCmmcTftpSessHostIp=_NbsCmmcTftpSessHostIp_Object((1,3,6,1,4,1,629,200,4,3,1,3),_NbsCmmcTftpSessHostIp_Type())
nbsCmmcTftpSessHostIp.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcTftpSessHostIp.setStatus(_A)
_NbsCmmcTftpSessModuleId_Type=Integer32
_NbsCmmcTftpSessModuleId_Object=MibTableColumn
nbsCmmcTftpSessModuleId=_NbsCmmcTftpSessModuleId_Object((1,3,6,1,4,1,629,200,4,3,1,4),_NbsCmmcTftpSessModuleId_Type())
nbsCmmcTftpSessModuleId.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcTftpSessModuleId.setStatus(_K)
class _NbsCmmcTftpSessAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('inactive',1),('downloadNM',2),('uploadNM',3),('downloadPar',4),('uploadPar',5),('downloadFile',6),('uploadFile',7)))
_NbsCmmcTftpSessAction_Type.__name__=_D
_NbsCmmcTftpSessAction_Object=MibTableColumn
nbsCmmcTftpSessAction=_NbsCmmcTftpSessAction_Object((1,3,6,1,4,1,629,200,4,3,1,5),_NbsCmmcTftpSessAction_Type())
nbsCmmcTftpSessAction.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcTftpSessAction.setStatus(_A)
class _NbsCmmcTftpSessFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_NbsCmmcTftpSessFileName_Type.__name__=_J
_NbsCmmcTftpSessFileName_Object=MibTableColumn
nbsCmmcTftpSessFileName=_NbsCmmcTftpSessFileName_Object((1,3,6,1,4,1,629,200,4,3,1,6),_NbsCmmcTftpSessFileName_Type())
nbsCmmcTftpSessFileName.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcTftpSessFileName.setStatus(_A)
class _NbsCmmcTftpSessFileSize_Type(Integer32):defaultValue=-1
_NbsCmmcTftpSessFileSize_Type.__name__=_D
_NbsCmmcTftpSessFileSize_Object=MibTableColumn
nbsCmmcTftpSessFileSize=_NbsCmmcTftpSessFileSize_Object((1,3,6,1,4,1,629,200,4,3,1,7),_NbsCmmcTftpSessFileSize_Type())
nbsCmmcTftpSessFileSize.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcTftpSessFileSize.setStatus(_K)
class _NbsCmmcTftpSessProgress_Type(Integer32):defaultValue=-1
_NbsCmmcTftpSessProgress_Type.__name__=_D
_NbsCmmcTftpSessProgress_Object=MibTableColumn
nbsCmmcTftpSessProgress=_NbsCmmcTftpSessProgress_Object((1,3,6,1,4,1,629,200,4,3,1,8),_NbsCmmcTftpSessProgress_Type())
nbsCmmcTftpSessProgress.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcTftpSessProgress.setStatus(_K)
class _NbsCmmcTftpSessAddressType_Type(InetAddressType):defaultValue=0
_NbsCmmcTftpSessAddressType_Type.__name__=_b
_NbsCmmcTftpSessAddressType_Object=MibTableColumn
nbsCmmcTftpSessAddressType=_NbsCmmcTftpSessAddressType_Object((1,3,6,1,4,1,629,200,4,3,1,9),_NbsCmmcTftpSessAddressType_Type())
nbsCmmcTftpSessAddressType.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcTftpSessAddressType.setStatus(_A)
_NbsCmmcTftpSessAddress_Type=InetAddress
_NbsCmmcTftpSessAddress_Object=MibTableColumn
nbsCmmcTftpSessAddress=_NbsCmmcTftpSessAddress_Object((1,3,6,1,4,1,629,200,4,3,1,10),_NbsCmmcTftpSessAddress_Type())
nbsCmmcTftpSessAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcTftpSessAddress.setStatus(_A)
class _NbsCmmcSysTftpHostAddressType_Type(InetAddressType):defaultValue=0
_NbsCmmcSysTftpHostAddressType_Type.__name__=_b
_NbsCmmcSysTftpHostAddressType_Object=MibScalar
nbsCmmcSysTftpHostAddressType=_NbsCmmcSysTftpHostAddressType_Object((1,3,6,1,4,1,629,200,4,4),_NbsCmmcSysTftpHostAddressType_Type())
nbsCmmcSysTftpHostAddressType.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysTftpHostAddressType.setStatus(_A)
_NbsCmmcSysTftpHostAddress_Type=InetAddress
_NbsCmmcSysTftpHostAddress_Object=MibScalar
nbsCmmcSysTftpHostAddress=_NbsCmmcSysTftpHostAddress_Object((1,3,6,1,4,1,629,200,4,5),_NbsCmmcSysTftpHostAddress_Type())
nbsCmmcSysTftpHostAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysTftpHostAddress.setStatus(_A)
_NbsCmmcChassisGrp_ObjectIdentity=ObjectIdentity
nbsCmmcChassisGrp=_NbsCmmcChassisGrp_ObjectIdentity((1,3,6,1,4,1,629,200,6))
if mibBuilder.loadTexts:nbsCmmcChassisGrp.setStatus(_A)
_NbsCmmcChassisTable_Object=MibTable
nbsCmmcChassisTable=_NbsCmmcChassisTable_Object((1,3,6,1,4,1,629,200,6,1))
if mibBuilder.loadTexts:nbsCmmcChassisTable.setStatus(_A)
_NbsCmmcChassisEntry_Object=MibTableRow
nbsCmmcChassisEntry=_NbsCmmcChassisEntry_Object((1,3,6,1,4,1,629,200,6,1,1))
nbsCmmcChassisEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:nbsCmmcChassisEntry.setStatus(_A)
_NbsCmmcChassisIndex_Type=Integer32
_NbsCmmcChassisIndex_Object=MibTableColumn
nbsCmmcChassisIndex=_NbsCmmcChassisIndex_Object((1,3,6,1,4,1,629,200,6,1,1,1),_NbsCmmcChassisIndex_Type())
nbsCmmcChassisIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcChassisIndex.setStatus(_A)
_NbsCmmcChassisType_Type=NbsCmmcEnumChassisType
_NbsCmmcChassisType_Object=MibTableColumn
nbsCmmcChassisType=_NbsCmmcChassisType_Object((1,3,6,1,4,1,629,200,6,1,1,2),_NbsCmmcChassisType_Type())
nbsCmmcChassisType.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcChassisType.setStatus(_A)
class _NbsCmmcChassisModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_NbsCmmcChassisModel_Type.__name__=_J
_NbsCmmcChassisModel_Object=MibTableColumn
nbsCmmcChassisModel=_NbsCmmcChassisModel_Object((1,3,6,1,4,1,629,200,6,1,1,3),_NbsCmmcChassisModel_Type())
nbsCmmcChassisModel.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcChassisModel.setStatus(_A)
_NbsCmmcChassisObjectId_Type=ObjectIdentifier
_NbsCmmcChassisObjectId_Object=MibTableColumn
nbsCmmcChassisObjectId=_NbsCmmcChassisObjectId_Object((1,3,6,1,4,1,629,200,6,1,1,4),_NbsCmmcChassisObjectId_Type())
nbsCmmcChassisObjectId.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcChassisObjectId.setStatus(_A)
_NbsCmmcChassisNumberOfSlots_Type=Integer32
_NbsCmmcChassisNumberOfSlots_Object=MibTableColumn
nbsCmmcChassisNumberOfSlots=_NbsCmmcChassisNumberOfSlots_Object((1,3,6,1,4,1,629,200,6,1,1,5),_NbsCmmcChassisNumberOfSlots_Type())
nbsCmmcChassisNumberOfSlots.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcChassisNumberOfSlots.setStatus(_A)
class _NbsCmmcChassisHardwareRevision_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_NbsCmmcChassisHardwareRevision_Type.__name__=_J
_NbsCmmcChassisHardwareRevision_Object=MibTableColumn
nbsCmmcChassisHardwareRevision=_NbsCmmcChassisHardwareRevision_Object((1,3,6,1,4,1,629,200,6,1,1,6),_NbsCmmcChassisHardwareRevision_Type())
nbsCmmcChassisHardwareRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcChassisHardwareRevision.setStatus(_A)
class _NbsCmmcChassisPS1Status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_U,1),(_s,2),(_t,3),(_u,4),(_v,5),(_F,6),(_V,7),(_W,8)))
_NbsCmmcChassisPS1Status_Type.__name__=_D
_NbsCmmcChassisPS1Status_Object=MibTableColumn
nbsCmmcChassisPS1Status=_NbsCmmcChassisPS1Status_Object((1,3,6,1,4,1,629,200,6,1,1,7),_NbsCmmcChassisPS1Status_Type())
nbsCmmcChassisPS1Status.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcChassisPS1Status.setStatus(_A)
class _NbsCmmcChassisPS2Status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_U,1),(_s,2),(_t,3),(_u,4),(_v,5),(_F,6),(_V,7),(_W,8)))
_NbsCmmcChassisPS2Status_Type.__name__=_D
_NbsCmmcChassisPS2Status_Object=MibTableColumn
nbsCmmcChassisPS2Status=_NbsCmmcChassisPS2Status_Object((1,3,6,1,4,1,629,200,6,1,1,8),_NbsCmmcChassisPS2Status_Type())
nbsCmmcChassisPS2Status.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcChassisPS2Status.setStatus(_A)
class _NbsCmmcChassisPS3Status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_U,1),(_s,2),(_t,3),(_u,4),(_v,5),(_F,6),(_V,7),(_W,8)))
_NbsCmmcChassisPS3Status_Type.__name__=_D
_NbsCmmcChassisPS3Status_Object=MibTableColumn
nbsCmmcChassisPS3Status=_NbsCmmcChassisPS3Status_Object((1,3,6,1,4,1,629,200,6,1,1,9),_NbsCmmcChassisPS3Status_Type())
nbsCmmcChassisPS3Status.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcChassisPS3Status.setStatus(_A)
class _NbsCmmcChassisPS4Status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_U,1),(_s,2),(_t,3),(_u,4),(_v,5),(_F,6),(_V,7),(_W,8)))
_NbsCmmcChassisPS4Status_Type.__name__=_D
_NbsCmmcChassisPS4Status_Object=MibTableColumn
nbsCmmcChassisPS4Status=_NbsCmmcChassisPS4Status_Object((1,3,6,1,4,1,629,200,6,1,1,10),_NbsCmmcChassisPS4Status_Type())
nbsCmmcChassisPS4Status.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcChassisPS4Status.setStatus(_A)
class _NbsCmmcChassisFan1Status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_W,2),(_V,3),(_U,4)))
_NbsCmmcChassisFan1Status_Type.__name__=_D
_NbsCmmcChassisFan1Status_Object=MibTableColumn
nbsCmmcChassisFan1Status=_NbsCmmcChassisFan1Status_Object((1,3,6,1,4,1,629,200,6,1,1,11),_NbsCmmcChassisFan1Status_Type())
nbsCmmcChassisFan1Status.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcChassisFan1Status.setStatus(_A)
class _NbsCmmcChassisFan2Status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_W,2),(_V,3),(_U,4)))
_NbsCmmcChassisFan2Status_Type.__name__=_D
_NbsCmmcChassisFan2Status_Object=MibTableColumn
nbsCmmcChassisFan2Status=_NbsCmmcChassisFan2Status_Object((1,3,6,1,4,1,629,200,6,1,1,12),_NbsCmmcChassisFan2Status_Type())
nbsCmmcChassisFan2Status.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcChassisFan2Status.setStatus(_A)
class _NbsCmmcChassisFan3Status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_W,2),(_V,3),(_U,4)))
_NbsCmmcChassisFan3Status_Type.__name__=_D
_NbsCmmcChassisFan3Status_Object=MibTableColumn
nbsCmmcChassisFan3Status=_NbsCmmcChassisFan3Status_Object((1,3,6,1,4,1,629,200,6,1,1,13),_NbsCmmcChassisFan3Status_Type())
nbsCmmcChassisFan3Status.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcChassisFan3Status.setStatus(_A)
class _NbsCmmcChassisFan4Status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_W,2),(_V,3),(_U,4)))
_NbsCmmcChassisFan4Status_Type.__name__=_D
_NbsCmmcChassisFan4Status_Object=MibTableColumn
nbsCmmcChassisFan4Status=_NbsCmmcChassisFan4Status_Object((1,3,6,1,4,1,629,200,6,1,1,14),_NbsCmmcChassisFan4Status_Type())
nbsCmmcChassisFan4Status.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcChassisFan4Status.setStatus(_A)
class _NbsCmmcChassisTemperature_Type(Integer32):defaultValue=-2147483648;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsCmmcChassisTemperature_Type.__name__=_D
_NbsCmmcChassisTemperature_Object=MibTableColumn
nbsCmmcChassisTemperature=_NbsCmmcChassisTemperature_Object((1,3,6,1,4,1,629,200,6,1,1,15),_NbsCmmcChassisTemperature_Type())
nbsCmmcChassisTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcChassisTemperature.setStatus(_A)
class _NbsCmmcChassisTemperatureLimit_Type(Integer32):defaultValue=45;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-100,100))
_NbsCmmcChassisTemperatureLimit_Type.__name__=_D
_NbsCmmcChassisTemperatureLimit_Object=MibTableColumn
nbsCmmcChassisTemperatureLimit=_NbsCmmcChassisTemperatureLimit_Object((1,3,6,1,4,1,629,200,6,1,1,16),_NbsCmmcChassisTemperatureLimit_Type())
nbsCmmcChassisTemperatureLimit.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcChassisTemperatureLimit.setStatus(_A)
class _NbsCmmcChassisTemperatureMin_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-100,100))
_NbsCmmcChassisTemperatureMin_Type.__name__=_D
_NbsCmmcChassisTemperatureMin_Object=MibTableColumn
nbsCmmcChassisTemperatureMin=_NbsCmmcChassisTemperatureMin_Object((1,3,6,1,4,1,629,200,6,1,1,17),_NbsCmmcChassisTemperatureMin_Type())
nbsCmmcChassisTemperatureMin.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcChassisTemperatureMin.setStatus(_A)
_NbsCmmcChassisSignalStrength_Type=Integer32
_NbsCmmcChassisSignalStrength_Object=MibTableColumn
nbsCmmcChassisSignalStrength=_NbsCmmcChassisSignalStrength_Object((1,3,6,1,4,1,629,200,6,1,1,18),_NbsCmmcChassisSignalStrength_Type())
nbsCmmcChassisSignalStrength.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcChassisSignalStrength.setStatus(_K)
_NbsCmmcChassisSignalStrengthMinimum_Type=Integer32
_NbsCmmcChassisSignalStrengthMinimum_Object=MibTableColumn
nbsCmmcChassisSignalStrengthMinimum=_NbsCmmcChassisSignalStrengthMinimum_Object((1,3,6,1,4,1,629,200,6,1,1,19),_NbsCmmcChassisSignalStrengthMinimum_Type())
nbsCmmcChassisSignalStrengthMinimum.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcChassisSignalStrengthMinimum.setStatus(_K)
class _NbsCmmcChassisEnableAutoReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('deprecatedoff',2),('deprecatedon',3)))
_NbsCmmcChassisEnableAutoReset_Type.__name__=_D
_NbsCmmcChassisEnableAutoReset_Object=MibTableColumn
nbsCmmcChassisEnableAutoReset=_NbsCmmcChassisEnableAutoReset_Object((1,3,6,1,4,1,629,200,6,1,1,20),_NbsCmmcChassisEnableAutoReset_Type())
nbsCmmcChassisEnableAutoReset.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcChassisEnableAutoReset.setStatus(_A)
class _NbsCmmcChassisEnableLinkTraps_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_R,2),(_S,3)))
_NbsCmmcChassisEnableLinkTraps_Type.__name__=_D
_NbsCmmcChassisEnableLinkTraps_Object=MibTableColumn
nbsCmmcChassisEnableLinkTraps=_NbsCmmcChassisEnableLinkTraps_Object((1,3,6,1,4,1,629,200,6,1,1,21),_NbsCmmcChassisEnableLinkTraps_Type())
nbsCmmcChassisEnableLinkTraps.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcChassisEnableLinkTraps.setStatus(_A)
class _NbsCmmcChassisEnableChassisTraps_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_R,2),(_S,3)))
_NbsCmmcChassisEnableChassisTraps_Type.__name__=_D
_NbsCmmcChassisEnableChassisTraps_Object=MibTableColumn
nbsCmmcChassisEnableChassisTraps=_NbsCmmcChassisEnableChassisTraps_Object((1,3,6,1,4,1,629,200,6,1,1,22),_NbsCmmcChassisEnableChassisTraps_Type())
nbsCmmcChassisEnableChassisTraps.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcChassisEnableChassisTraps.setStatus(_A)
class _NbsCmmcChassisEnableLoopbackTraps_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_R,2),(_S,3)))
_NbsCmmcChassisEnableLoopbackTraps_Type.__name__=_D
_NbsCmmcChassisEnableLoopbackTraps_Object=MibTableColumn
nbsCmmcChassisEnableLoopbackTraps=_NbsCmmcChassisEnableLoopbackTraps_Object((1,3,6,1,4,1,629,200,6,1,1,23),_NbsCmmcChassisEnableLoopbackTraps_Type())
nbsCmmcChassisEnableLoopbackTraps.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcChassisEnableLoopbackTraps.setStatus(_A)
class _NbsCmmcChassisEnableSlotChangeTraps_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_R,2),(_S,3)))
_NbsCmmcChassisEnableSlotChangeTraps_Type.__name__=_D
_NbsCmmcChassisEnableSlotChangeTraps_Object=MibTableColumn
nbsCmmcChassisEnableSlotChangeTraps=_NbsCmmcChassisEnableSlotChangeTraps_Object((1,3,6,1,4,1,629,200,6,1,1,24),_NbsCmmcChassisEnableSlotChangeTraps_Type())
nbsCmmcChassisEnableSlotChangeTraps.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcChassisEnableSlotChangeTraps.setStatus(_A)
class _NbsCmmcChassisEnablePortTraps_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_R,2),(_S,3)))
_NbsCmmcChassisEnablePortTraps_Type.__name__=_D
_NbsCmmcChassisEnablePortTraps_Object=MibTableColumn
nbsCmmcChassisEnablePortTraps=_NbsCmmcChassisEnablePortTraps_Object((1,3,6,1,4,1,629,200,6,1,1,25),_NbsCmmcChassisEnablePortTraps_Type())
nbsCmmcChassisEnablePortTraps.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcChassisEnablePortTraps.setStatus(_A)
class _NbsCmmcChassisResetAllModules_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('deprecatedOperating',2),('deprecatedReset',3)))
_NbsCmmcChassisResetAllModules_Type.__name__=_D
_NbsCmmcChassisResetAllModules_Object=MibTableColumn
nbsCmmcChassisResetAllModules=_NbsCmmcChassisResetAllModules_Object((1,3,6,1,4,1,629,200,6,1,1,26),_NbsCmmcChassisResetAllModules_Type())
nbsCmmcChassisResetAllModules.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcChassisResetAllModules.setStatus(_A)
class _NbsCmmcChassisEnableModuleSpecificTraps_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_R,2),(_S,3)))
_NbsCmmcChassisEnableModuleSpecificTraps_Type.__name__=_D
_NbsCmmcChassisEnableModuleSpecificTraps_Object=MibTableColumn
nbsCmmcChassisEnableModuleSpecificTraps=_NbsCmmcChassisEnableModuleSpecificTraps_Object((1,3,6,1,4,1,629,200,6,1,1,27),_NbsCmmcChassisEnableModuleSpecificTraps_Type())
nbsCmmcChassisEnableModuleSpecificTraps.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcChassisEnableModuleSpecificTraps.setStatus(_A)
class _NbsCmmcChassisLoopbackTimeout_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NbsCmmcChassisLoopbackTimeout_Type.__name__=_D
_NbsCmmcChassisLoopbackTimeout_Object=MibTableColumn
nbsCmmcChassisLoopbackTimeout=_NbsCmmcChassisLoopbackTimeout_Object((1,3,6,1,4,1,629,200,6,1,1,28),_NbsCmmcChassisLoopbackTimeout_Type())
nbsCmmcChassisLoopbackTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcChassisLoopbackTimeout.setStatus(_A)
_NbsCmmcChassisPortInfoBitMap_Type=OctetString
_NbsCmmcChassisPortInfoBitMap_Object=MibTableColumn
nbsCmmcChassisPortInfoBitMap=_NbsCmmcChassisPortInfoBitMap_Object((1,3,6,1,4,1,629,200,6,1,1,29),_NbsCmmcChassisPortInfoBitMap_Type())
nbsCmmcChassisPortInfoBitMap.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcChassisPortInfoBitMap.setStatus(_A)
_NbsCmmcChassisSlotListBitMap_Type=OctetString
_NbsCmmcChassisSlotListBitMap_Object=MibTableColumn
nbsCmmcChassisSlotListBitMap=_NbsCmmcChassisSlotListBitMap_Object((1,3,6,1,4,1,629,200,6,1,1,30),_NbsCmmcChassisSlotListBitMap_Type())
nbsCmmcChassisSlotListBitMap.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcChassisSlotListBitMap.setStatus(_A)
_NbsCmmcChassisNumberOfPortsBitMap_Type=OctetString
_NbsCmmcChassisNumberOfPortsBitMap_Object=MibTableColumn
nbsCmmcChassisNumberOfPortsBitMap=_NbsCmmcChassisNumberOfPortsBitMap_Object((1,3,6,1,4,1,629,200,6,1,1,31),_NbsCmmcChassisNumberOfPortsBitMap_Type())
nbsCmmcChassisNumberOfPortsBitMap.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcChassisNumberOfPortsBitMap.setStatus(_A)
class _NbsCmmcChassisName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_NbsCmmcChassisName_Type.__name__=_J
_NbsCmmcChassisName_Object=MibTableColumn
nbsCmmcChassisName=_NbsCmmcChassisName_Object((1,3,6,1,4,1,629,200,6,1,1,32),_NbsCmmcChassisName_Type())
nbsCmmcChassisName.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcChassisName.setStatus(_A)
class _NbsCmmcChassisEnableLINTraps_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_R,2),(_S,3)))
_NbsCmmcChassisEnableLINTraps_Type.__name__=_D
_NbsCmmcChassisEnableLINTraps_Object=MibTableColumn
nbsCmmcChassisEnableLINTraps=_NbsCmmcChassisEnableLINTraps_Object((1,3,6,1,4,1,629,200,6,1,1,33),_NbsCmmcChassisEnableLINTraps_Type())
nbsCmmcChassisEnableLINTraps.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcChassisEnableLINTraps.setStatus(_A)
class _NbsCmmcChassisEnablePortChangeTraps_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_R,2),(_S,3)))
_NbsCmmcChassisEnablePortChangeTraps_Type.__name__=_D
_NbsCmmcChassisEnablePortChangeTraps_Object=MibTableColumn
nbsCmmcChassisEnablePortChangeTraps=_NbsCmmcChassisEnablePortChangeTraps_Object((1,3,6,1,4,1,629,200,6,1,1,34),_NbsCmmcChassisEnablePortChangeTraps_Type())
nbsCmmcChassisEnablePortChangeTraps.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcChassisEnablePortChangeTraps.setStatus(_A)
class _NbsCmmcChassisEnablePortDiagsTraps_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_R,2),(_S,3)))
_NbsCmmcChassisEnablePortDiagsTraps_Type.__name__=_D
_NbsCmmcChassisEnablePortDiagsTraps_Object=MibTableColumn
nbsCmmcChassisEnablePortDiagsTraps=_NbsCmmcChassisEnablePortDiagsTraps_Object((1,3,6,1,4,1,629,200,6,1,1,35),_NbsCmmcChassisEnablePortDiagsTraps_Type())
nbsCmmcChassisEnablePortDiagsTraps.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcChassisEnablePortDiagsTraps.setStatus(_A)
class _NbsCmmcChassisFan5Status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_W,2),(_V,3),(_U,4)))
_NbsCmmcChassisFan5Status_Type.__name__=_D
_NbsCmmcChassisFan5Status_Object=MibTableColumn
nbsCmmcChassisFan5Status=_NbsCmmcChassisFan5Status_Object((1,3,6,1,4,1,629,200,6,1,1,36),_NbsCmmcChassisFan5Status_Type())
nbsCmmcChassisFan5Status.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcChassisFan5Status.setStatus(_A)
class _NbsCmmcChassisFan6Status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_W,2),(_V,3),(_U,4)))
_NbsCmmcChassisFan6Status_Type.__name__=_D
_NbsCmmcChassisFan6Status_Object=MibTableColumn
nbsCmmcChassisFan6Status=_NbsCmmcChassisFan6Status_Object((1,3,6,1,4,1,629,200,6,1,1,37),_NbsCmmcChassisFan6Status_Type())
nbsCmmcChassisFan6Status.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcChassisFan6Status.setStatus(_A)
class _NbsCmmcChassisFan7Status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_W,2),(_V,3),(_U,4)))
_NbsCmmcChassisFan7Status_Type.__name__=_D
_NbsCmmcChassisFan7Status_Object=MibTableColumn
nbsCmmcChassisFan7Status=_NbsCmmcChassisFan7Status_Object((1,3,6,1,4,1,629,200,6,1,1,38),_NbsCmmcChassisFan7Status_Type())
nbsCmmcChassisFan7Status.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcChassisFan7Status.setStatus(_A)
class _NbsCmmcChassisFan8Status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_W,2),(_V,3),(_U,4)))
_NbsCmmcChassisFan8Status_Type.__name__=_D
_NbsCmmcChassisFan8Status_Object=MibTableColumn
nbsCmmcChassisFan8Status=_NbsCmmcChassisFan8Status_Object((1,3,6,1,4,1,629,200,6,1,1,39),_NbsCmmcChassisFan8Status_Type())
nbsCmmcChassisFan8Status.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcChassisFan8Status.setStatus(_A)
class _NbsCmmcChassisEnableSwitchoverTraps_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_R,2),(_S,3)))
_NbsCmmcChassisEnableSwitchoverTraps_Type.__name__=_D
_NbsCmmcChassisEnableSwitchoverTraps_Object=MibTableColumn
nbsCmmcChassisEnableSwitchoverTraps=_NbsCmmcChassisEnableSwitchoverTraps_Object((1,3,6,1,4,1,629,200,6,1,1,40),_NbsCmmcChassisEnableSwitchoverTraps_Type())
nbsCmmcChassisEnableSwitchoverTraps.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcChassisEnableSwitchoverTraps.setStatus(_A)
class _NbsCmmcChassisCrossConnect_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_a,2),(_Y,3)))
_NbsCmmcChassisCrossConnect_Type.__name__=_D
_NbsCmmcChassisCrossConnect_Object=MibTableColumn
nbsCmmcChassisCrossConnect=_NbsCmmcChassisCrossConnect_Object((1,3,6,1,4,1,629,200,6,1,1,41),_NbsCmmcChassisCrossConnect_Type())
nbsCmmcChassisCrossConnect.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcChassisCrossConnect.setStatus(_A)
class _NbsCmmcChassisNVAreaBanks_Type(Integer32):defaultValue=0
_NbsCmmcChassisNVAreaBanks_Type.__name__=_D
_NbsCmmcChassisNVAreaBanks_Object=MibTableColumn
nbsCmmcChassisNVAreaBanks=_NbsCmmcChassisNVAreaBanks_Object((1,3,6,1,4,1,629,200,6,1,1,42),_NbsCmmcChassisNVAreaBanks_Type())
nbsCmmcChassisNVAreaBanks.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcChassisNVAreaBanks.setStatus(_A)
class _NbsCmmcChassisFirmwareCaps_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_NbsCmmcChassisFirmwareCaps_Type.__name__=_T
_NbsCmmcChassisFirmwareCaps_Object=MibTableColumn
nbsCmmcChassisFirmwareCaps=_NbsCmmcChassisFirmwareCaps_Object((1,3,6,1,4,1,629,200,6,1,1,43),_NbsCmmcChassisFirmwareCaps_Type())
nbsCmmcChassisFirmwareCaps.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcChassisFirmwareCaps.setStatus(_A)
class _NbsCmmcChassisFirmwareLoad_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_NbsCmmcChassisFirmwareLoad_Type.__name__=_T
_NbsCmmcChassisFirmwareLoad_Object=MibTableColumn
nbsCmmcChassisFirmwareLoad=_NbsCmmcChassisFirmwareLoad_Object((1,3,6,1,4,1,629,200,6,1,1,44),_NbsCmmcChassisFirmwareLoad_Type())
nbsCmmcChassisFirmwareLoad.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcChassisFirmwareLoad.setStatus(_A)
class _NbsCmmcChassisNVAreaAdmin_Type(Integer32):defaultValue=0
_NbsCmmcChassisNVAreaAdmin_Type.__name__=_D
_NbsCmmcChassisNVAreaAdmin_Object=MibTableColumn
nbsCmmcChassisNVAreaAdmin=_NbsCmmcChassisNVAreaAdmin_Object((1,3,6,1,4,1,629,200,6,1,1,45),_NbsCmmcChassisNVAreaAdmin_Type())
nbsCmmcChassisNVAreaAdmin.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcChassisNVAreaAdmin.setStatus(_A)
class _NbsCmmcChassisNVAreaOper_Type(Integer32):defaultValue=-1
_NbsCmmcChassisNVAreaOper_Type.__name__=_D
_NbsCmmcChassisNVAreaOper_Object=MibTableColumn
nbsCmmcChassisNVAreaOper=_NbsCmmcChassisNVAreaOper_Object((1,3,6,1,4,1,629,200,6,1,1,46),_NbsCmmcChassisNVAreaOper_Type())
nbsCmmcChassisNVAreaOper.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcChassisNVAreaOper.setStatus(_A)
class _NbsCmmcChassisLoader_Type(Integer32):defaultValue=0
_NbsCmmcChassisLoader_Type.__name__=_D
_NbsCmmcChassisLoader_Object=MibTableColumn
nbsCmmcChassisLoader=_NbsCmmcChassisLoader_Object((1,3,6,1,4,1,629,200,6,1,1,47),_NbsCmmcChassisLoader_Type())
nbsCmmcChassisLoader.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcChassisLoader.setStatus(_A)
class _NbsCmmcChassisSerialNum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_NbsCmmcChassisSerialNum_Type.__name__=_J
_NbsCmmcChassisSerialNum_Object=MibTableColumn
nbsCmmcChassisSerialNum=_NbsCmmcChassisSerialNum_Object((1,3,6,1,4,1,629,200,6,1,1,48),_NbsCmmcChassisSerialNum_Type())
nbsCmmcChassisSerialNum.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcChassisSerialNum.setStatus(_A)
class _NbsCmmcChassisFace_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,500))
_NbsCmmcChassisFace_Type.__name__=_T
_NbsCmmcChassisFace_Object=MibTableColumn
nbsCmmcChassisFace=_NbsCmmcChassisFace_Object((1,3,6,1,4,1,629,200,6,1,1,49),_NbsCmmcChassisFace_Type())
nbsCmmcChassisFace.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcChassisFace.setStatus(_A)
class _NbsCmmcChassisCountersState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_r,2),(_Y,3)))
_NbsCmmcChassisCountersState_Type.__name__=_D
_NbsCmmcChassisCountersState_Object=MibTableColumn
nbsCmmcChassisCountersState=_NbsCmmcChassisCountersState_Object((1,3,6,1,4,1,629,200,6,1,1,50),_NbsCmmcChassisCountersState_Type())
nbsCmmcChassisCountersState.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcChassisCountersState.setStatus(_A)
class _NbsCmmcChassisPowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('sufficient',2),('insufficient',3)))
_NbsCmmcChassisPowerStatus_Type.__name__=_D
_NbsCmmcChassisPowerStatus_Object=MibTableColumn
nbsCmmcChassisPowerStatus=_NbsCmmcChassisPowerStatus_Object((1,3,6,1,4,1,629,200,6,1,1,51),_NbsCmmcChassisPowerStatus_Type())
nbsCmmcChassisPowerStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcChassisPowerStatus.setStatus(_A)
_NbsCmmcChassisIfIndex_Type=InterfaceIndex
_NbsCmmcChassisIfIndex_Object=MibTableColumn
nbsCmmcChassisIfIndex=_NbsCmmcChassisIfIndex_Object((1,3,6,1,4,1,629,200,6,1,1,52),_NbsCmmcChassisIfIndex_Type())
nbsCmmcChassisIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcChassisIfIndex.setStatus(_A)
_NbsCmmcChassisCount_Type=Integer32
_NbsCmmcChassisCount_Object=MibScalar
nbsCmmcChassisCount=_NbsCmmcChassisCount_Object((1,3,6,1,4,1,629,200,6,2),_NbsCmmcChassisCount_Type())
nbsCmmcChassisCount.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcChassisCount.setStatus(_A)
_NbsCmmcSlotGrp_ObjectIdentity=ObjectIdentity
nbsCmmcSlotGrp=_NbsCmmcSlotGrp_ObjectIdentity((1,3,6,1,4,1,629,200,7))
if mibBuilder.loadTexts:nbsCmmcSlotGrp.setStatus(_A)
_NbsCmmcSlotTable_Object=MibTable
nbsCmmcSlotTable=_NbsCmmcSlotTable_Object((1,3,6,1,4,1,629,200,7,1))
if mibBuilder.loadTexts:nbsCmmcSlotTable.setStatus(_A)
_NbsCmmcSlotEntry_Object=MibTableRow
nbsCmmcSlotEntry=_NbsCmmcSlotEntry_Object((1,3,6,1,4,1,629,200,7,1,1))
nbsCmmcSlotEntry.setIndexNames((0,_B,_Ad),(0,_B,_L))
if mibBuilder.loadTexts:nbsCmmcSlotEntry.setStatus(_A)
_NbsCmmcSlotChassisIndex_Type=Integer32
_NbsCmmcSlotChassisIndex_Object=MibTableColumn
nbsCmmcSlotChassisIndex=_NbsCmmcSlotChassisIndex_Object((1,3,6,1,4,1,629,200,7,1,1,1),_NbsCmmcSlotChassisIndex_Type())
nbsCmmcSlotChassisIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSlotChassisIndex.setStatus(_A)
_NbsCmmcSlotIndex_Type=Integer32
_NbsCmmcSlotIndex_Object=MibTableColumn
nbsCmmcSlotIndex=_NbsCmmcSlotIndex_Object((1,3,6,1,4,1,629,200,7,1,1,2),_NbsCmmcSlotIndex_Type())
nbsCmmcSlotIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSlotIndex.setStatus(_A)
_NbsCmmcSlotType_Type=NbsCmmcEnumSlotType
_NbsCmmcSlotType_Object=MibTableColumn
nbsCmmcSlotType=_NbsCmmcSlotType_Object((1,3,6,1,4,1,629,200,7,1,1,3),_NbsCmmcSlotType_Type())
nbsCmmcSlotType.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSlotType.setStatus(_A)
class _NbsCmmcSlotModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_NbsCmmcSlotModel_Type.__name__=_J
_NbsCmmcSlotModel_Object=MibTableColumn
nbsCmmcSlotModel=_NbsCmmcSlotModel_Object((1,3,6,1,4,1,629,200,7,1,1,4),_NbsCmmcSlotModel_Type())
nbsCmmcSlotModel.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSlotModel.setStatus(_A)
_NbsCmmcSlotObjectId_Type=ObjectIdentifier
_NbsCmmcSlotObjectId_Object=MibTableColumn
nbsCmmcSlotObjectId=_NbsCmmcSlotObjectId_Object((1,3,6,1,4,1,629,200,7,1,1,5),_NbsCmmcSlotObjectId_Type())
nbsCmmcSlotObjectId.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSlotObjectId.setStatus(_A)
class _NbsCmmcSlotNumberOfPorts_Type(Integer32):defaultValue=0
_NbsCmmcSlotNumberOfPorts_Type.__name__=_D
_NbsCmmcSlotNumberOfPorts_Object=MibTableColumn
nbsCmmcSlotNumberOfPorts=_NbsCmmcSlotNumberOfPorts_Object((1,3,6,1,4,1,629,200,7,1,1,6),_NbsCmmcSlotNumberOfPorts_Type())
nbsCmmcSlotNumberOfPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSlotNumberOfPorts.setStatus(_A)
class _NbsCmmcSlotHardwareRevision_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_NbsCmmcSlotHardwareRevision_Type.__name__=_J
_NbsCmmcSlotHardwareRevision_Object=MibTableColumn
nbsCmmcSlotHardwareRevision=_NbsCmmcSlotHardwareRevision_Object((1,3,6,1,4,1,629,200,7,1,1,7),_NbsCmmcSlotHardwareRevision_Type())
nbsCmmcSlotHardwareRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSlotHardwareRevision.setStatus(_A)
class _NbsCmmcSlotOperationType_Type(NbsCmmcEnumSlotOperationType):defaultValue=1
_NbsCmmcSlotOperationType_Type.__name__=_AN
_NbsCmmcSlotOperationType_Object=MibTableColumn
nbsCmmcSlotOperationType=_NbsCmmcSlotOperationType_Object((1,3,6,1,4,1,629,200,7,1,1,8),_NbsCmmcSlotOperationType_Type())
nbsCmmcSlotOperationType.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSlotOperationType.setStatus(_A)
class _NbsCmmcSlotReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_F,1),(_a,2),('deprecatedPhy',3),('deprecatedQueue',4),('resetSlot',5),('initSlot',6),('resetWarm',7)))
_NbsCmmcSlotReset_Type.__name__=_D
_NbsCmmcSlotReset_Object=MibTableColumn
nbsCmmcSlotReset=_NbsCmmcSlotReset_Object((1,3,6,1,4,1,629,200,7,1,1,9),_NbsCmmcSlotReset_Type())
nbsCmmcSlotReset.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSlotReset.setStatus(_A)
class _NbsCmmcSlotName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_NbsCmmcSlotName_Type.__name__=_J
_NbsCmmcSlotName_Object=MibTableColumn
nbsCmmcSlotName=_NbsCmmcSlotName_Object((1,3,6,1,4,1,629,200,7,1,1,10),_NbsCmmcSlotName_Type())
nbsCmmcSlotName.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSlotName.setStatus(_A)
_NbsCmmcSlotModuleType_Type=Integer32
_NbsCmmcSlotModuleType_Object=MibTableColumn
nbsCmmcSlotModuleType=_NbsCmmcSlotModuleType_Object((1,3,6,1,4,1,629,200,7,1,1,11),_NbsCmmcSlotModuleType_Type())
nbsCmmcSlotModuleType.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSlotModuleType.setStatus(_A)
class _NbsCmmcSlotModuleSlot_Type(Integer32):defaultValue=1
_NbsCmmcSlotModuleSlot_Type.__name__=_D
_NbsCmmcSlotModuleSlot_Object=MibTableColumn
nbsCmmcSlotModuleSlot=_NbsCmmcSlotModuleSlot_Object((1,3,6,1,4,1,629,200,7,1,1,12),_NbsCmmcSlotModuleSlot_Type())
nbsCmmcSlotModuleSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSlotModuleSlot.setStatus(_A)
class _NbsCmmcSlotSwConfigurable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_w,1),(_x,2),(_y,3)))
_NbsCmmcSlotSwConfigurable_Type.__name__=_D
_NbsCmmcSlotSwConfigurable_Object=MibTableColumn
nbsCmmcSlotSwConfigurable=_NbsCmmcSlotSwConfigurable_Object((1,3,6,1,4,1,629,200,7,1,1,13),_NbsCmmcSlotSwConfigurable_Type())
nbsCmmcSlotSwConfigurable.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSlotSwConfigurable.setStatus(_A)
class _NbsCmmcSlotConfiguration_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,250))
_NbsCmmcSlotConfiguration_Type.__name__=_T
_NbsCmmcSlotConfiguration_Object=MibTableColumn
nbsCmmcSlotConfiguration=_NbsCmmcSlotConfiguration_Object((1,3,6,1,4,1,629,200,7,1,1,14),_NbsCmmcSlotConfiguration_Type())
nbsCmmcSlotConfiguration.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSlotConfiguration.setStatus(_A)
class _NbsCmmcSlotMacAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,6))
_NbsCmmcSlotMacAddress_Type.__name__=_T
_NbsCmmcSlotMacAddress_Object=MibTableColumn
nbsCmmcSlotMacAddress=_NbsCmmcSlotMacAddress_Object((1,3,6,1,4,1,629,200,7,1,1,15),_NbsCmmcSlotMacAddress_Type())
nbsCmmcSlotMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSlotMacAddress.setStatus(_A)
_NbsCmmcSlotIPAddress_Type=IpAddress
_NbsCmmcSlotIPAddress_Object=MibTableColumn
nbsCmmcSlotIPAddress=_NbsCmmcSlotIPAddress_Object((1,3,6,1,4,1,629,200,7,1,1,16),_NbsCmmcSlotIPAddress_Type())
nbsCmmcSlotIPAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSlotIPAddress.setStatus(_A)
_NbsCmmcSlotSubnetMask_Type=IpAddress
_NbsCmmcSlotSubnetMask_Object=MibTableColumn
nbsCmmcSlotSubnetMask=_NbsCmmcSlotSubnetMask_Object((1,3,6,1,4,1,629,200,7,1,1,17),_NbsCmmcSlotSubnetMask_Type())
nbsCmmcSlotSubnetMask.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSlotSubnetMask.setStatus(_A)
_NbsCmmcSlotBroadcastAddr_Type=IpAddress
_NbsCmmcSlotBroadcastAddr_Object=MibTableColumn
nbsCmmcSlotBroadcastAddr=_NbsCmmcSlotBroadcastAddr_Object((1,3,6,1,4,1,629,200,7,1,1,18),_NbsCmmcSlotBroadcastAddr_Type())
nbsCmmcSlotBroadcastAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSlotBroadcastAddr.setStatus(_A)
_NbsCmmcSlotDefGateway_Type=IpAddress
_NbsCmmcSlotDefGateway_Object=MibTableColumn
nbsCmmcSlotDefGateway=_NbsCmmcSlotDefGateway_Object((1,3,6,1,4,1,629,200,7,1,1,19),_NbsCmmcSlotDefGateway_Type())
nbsCmmcSlotDefGateway.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSlotDefGateway.setStatus(_A)
class _NbsCmmcSlotHoming_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('singleCO',2),('dualCOs',3)))
_NbsCmmcSlotHoming_Type.__name__=_D
_NbsCmmcSlotHoming_Object=MibTableColumn
nbsCmmcSlotHoming=_NbsCmmcSlotHoming_Object((1,3,6,1,4,1,629,200,7,1,1,20),_NbsCmmcSlotHoming_Type())
nbsCmmcSlotHoming.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSlotHoming.setStatus(_A)
class _NbsCmmcSlotRedundancyAdmin_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_P,2),(_Q,3)))
_NbsCmmcSlotRedundancyAdmin_Type.__name__=_D
_NbsCmmcSlotRedundancyAdmin_Object=MibTableColumn
nbsCmmcSlotRedundancyAdmin=_NbsCmmcSlotRedundancyAdmin_Object((1,3,6,1,4,1,629,200,7,1,1,21),_NbsCmmcSlotRedundancyAdmin_Type())
nbsCmmcSlotRedundancyAdmin.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSlotRedundancyAdmin.setStatus(_A)
class _NbsCmmcSlotDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_NbsCmmcSlotDescr_Type.__name__=_J
_NbsCmmcSlotDescr_Object=MibTableColumn
nbsCmmcSlotDescr=_NbsCmmcSlotDescr_Object((1,3,6,1,4,1,629,200,7,1,1,22),_NbsCmmcSlotDescr_Type())
nbsCmmcSlotDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSlotDescr.setStatus(_A)
class _NbsCmmcSlotUpgradable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_p,2)))
_NbsCmmcSlotUpgradable_Type.__name__=_D
_NbsCmmcSlotUpgradable_Object=MibTableColumn
nbsCmmcSlotUpgradable=_NbsCmmcSlotUpgradable_Object((1,3,6,1,4,1,629,200,7,1,1,23),_NbsCmmcSlotUpgradable_Type())
nbsCmmcSlotUpgradable.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSlotUpgradable.setStatus(_A)
class _NbsCmmcSlotCrossConnect_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_a,2),(_Y,3)))
_NbsCmmcSlotCrossConnect_Type.__name__=_D
_NbsCmmcSlotCrossConnect_Object=MibTableColumn
nbsCmmcSlotCrossConnect=_NbsCmmcSlotCrossConnect_Object((1,3,6,1,4,1,629,200,7,1,1,24),_NbsCmmcSlotCrossConnect_Type())
nbsCmmcSlotCrossConnect.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSlotCrossConnect.setStatus(_A)
class _NbsCmmcSlotClearType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('idle',2),('clearType',3)))
_NbsCmmcSlotClearType_Type.__name__=_D
_NbsCmmcSlotClearType_Object=MibTableColumn
nbsCmmcSlotClearType=_NbsCmmcSlotClearType_Object((1,3,6,1,4,1,629,200,7,1,1,25),_NbsCmmcSlotClearType_Type())
nbsCmmcSlotClearType.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSlotClearType.setStatus(_A)
class _NbsCmmcSlotNVAreaBanks_Type(Integer32):defaultValue=0
_NbsCmmcSlotNVAreaBanks_Type.__name__=_D
_NbsCmmcSlotNVAreaBanks_Object=MibTableColumn
nbsCmmcSlotNVAreaBanks=_NbsCmmcSlotNVAreaBanks_Object((1,3,6,1,4,1,629,200,7,1,1,26),_NbsCmmcSlotNVAreaBanks_Type())
nbsCmmcSlotNVAreaBanks.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSlotNVAreaBanks.setStatus(_A)
class _NbsCmmcSlotFirmwareCaps_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_NbsCmmcSlotFirmwareCaps_Type.__name__=_T
_NbsCmmcSlotFirmwareCaps_Object=MibTableColumn
nbsCmmcSlotFirmwareCaps=_NbsCmmcSlotFirmwareCaps_Object((1,3,6,1,4,1,629,200,7,1,1,27),_NbsCmmcSlotFirmwareCaps_Type())
nbsCmmcSlotFirmwareCaps.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSlotFirmwareCaps.setStatus(_A)
class _NbsCmmcSlotFirmwareLoad_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_NbsCmmcSlotFirmwareLoad_Type.__name__=_T
_NbsCmmcSlotFirmwareLoad_Object=MibTableColumn
nbsCmmcSlotFirmwareLoad=_NbsCmmcSlotFirmwareLoad_Object((1,3,6,1,4,1,629,200,7,1,1,28),_NbsCmmcSlotFirmwareLoad_Type())
nbsCmmcSlotFirmwareLoad.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSlotFirmwareLoad.setStatus(_A)
class _NbsCmmcSlotNVAreaAdmin_Type(Integer32):defaultValue=0
_NbsCmmcSlotNVAreaAdmin_Type.__name__=_D
_NbsCmmcSlotNVAreaAdmin_Object=MibTableColumn
nbsCmmcSlotNVAreaAdmin=_NbsCmmcSlotNVAreaAdmin_Object((1,3,6,1,4,1,629,200,7,1,1,29),_NbsCmmcSlotNVAreaAdmin_Type())
nbsCmmcSlotNVAreaAdmin.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSlotNVAreaAdmin.setStatus(_A)
class _NbsCmmcSlotNVAreaOper_Type(Integer32):defaultValue=-1
_NbsCmmcSlotNVAreaOper_Type.__name__=_D
_NbsCmmcSlotNVAreaOper_Object=MibTableColumn
nbsCmmcSlotNVAreaOper=_NbsCmmcSlotNVAreaOper_Object((1,3,6,1,4,1,629,200,7,1,1,30),_NbsCmmcSlotNVAreaOper_Type())
nbsCmmcSlotNVAreaOper.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSlotNVAreaOper.setStatus(_A)
class _NbsCmmcSlotLoader_Type(Integer32):defaultValue=0
_NbsCmmcSlotLoader_Type.__name__=_D
_NbsCmmcSlotLoader_Object=MibTableColumn
nbsCmmcSlotLoader=_NbsCmmcSlotLoader_Object((1,3,6,1,4,1,629,200,7,1,1,31),_NbsCmmcSlotLoader_Type())
nbsCmmcSlotLoader.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSlotLoader.setStatus(_A)
class _NbsCmmcSlotSerialNum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_NbsCmmcSlotSerialNum_Type.__name__=_J
_NbsCmmcSlotSerialNum_Object=MibTableColumn
nbsCmmcSlotSerialNum=_NbsCmmcSlotSerialNum_Object((1,3,6,1,4,1,629,200,7,1,1,32),_NbsCmmcSlotSerialNum_Type())
nbsCmmcSlotSerialNum.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSlotSerialNum.setStatus(_A)
class _NbsCmmcSlotToggleRate_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NbsCmmcSlotToggleRate_Type.__name__=_D
_NbsCmmcSlotToggleRate_Object=MibTableColumn
nbsCmmcSlotToggleRate=_NbsCmmcSlotToggleRate_Object((1,3,6,1,4,1,629,200,7,1,1,33),_NbsCmmcSlotToggleRate_Type())
nbsCmmcSlotToggleRate.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSlotToggleRate.setStatus(_A)
class _NbsCmmcSlotTemperature_Type(Integer32):defaultValue=-2147483648;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsCmmcSlotTemperature_Type.__name__=_D
_NbsCmmcSlotTemperature_Object=MibTableColumn
nbsCmmcSlotTemperature=_NbsCmmcSlotTemperature_Object((1,3,6,1,4,1,629,200,7,1,1,34),_NbsCmmcSlotTemperature_Type())
nbsCmmcSlotTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSlotTemperature.setStatus(_A)
class _NbsCmmcSlotCountersState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_r,2),(_Y,3)))
_NbsCmmcSlotCountersState_Type.__name__=_D
_NbsCmmcSlotCountersState_Object=MibTableColumn
nbsCmmcSlotCountersState=_NbsCmmcSlotCountersState_Object((1,3,6,1,4,1,629,200,7,1,1,35),_NbsCmmcSlotCountersState_Type())
nbsCmmcSlotCountersState.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSlotCountersState.setStatus(_A)
class _NbsCmmcSlotRedundancyOper_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_P,2),(_Q,3)))
_NbsCmmcSlotRedundancyOper_Type.__name__=_D
_NbsCmmcSlotRedundancyOper_Object=MibTableColumn
nbsCmmcSlotRedundancyOper=_NbsCmmcSlotRedundancyOper_Object((1,3,6,1,4,1,629,200,7,1,1,36),_NbsCmmcSlotRedundancyOper_Type())
nbsCmmcSlotRedundancyOper.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSlotRedundancyOper.setStatus(_A)
_NbsCmmcSlotIfIndex_Type=InterfaceIndex
_NbsCmmcSlotIfIndex_Object=MibTableColumn
nbsCmmcSlotIfIndex=_NbsCmmcSlotIfIndex_Object((1,3,6,1,4,1,629,200,7,1,1,37),_NbsCmmcSlotIfIndex_Type())
nbsCmmcSlotIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSlotIfIndex.setStatus(_A)
class _NbsCmmcSlotModuleStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),('empty',2),('notReady',3),('ready',4),('standby',5)))
_NbsCmmcSlotModuleStatus_Type.__name__=_D
_NbsCmmcSlotModuleStatus_Object=MibTableColumn
nbsCmmcSlotModuleStatus=_NbsCmmcSlotModuleStatus_Object((1,3,6,1,4,1,629,200,7,1,1,38),_NbsCmmcSlotModuleStatus_Type())
nbsCmmcSlotModuleStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSlotModuleStatus.setStatus(_A)
class _NbsCmmcSlotManagementPort_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NbsCmmcSlotManagementPort_Type.__name__=_D
_NbsCmmcSlotManagementPort_Object=MibTableColumn
nbsCmmcSlotManagementPort=_NbsCmmcSlotManagementPort_Object((1,3,6,1,4,1,629,200,7,1,1,39),_NbsCmmcSlotManagementPort_Type())
nbsCmmcSlotManagementPort.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSlotManagementPort.setStatus(_A)
class _NbsCmmcSlotTemperatureLimit_Type(Integer32):defaultValue=85;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-100,100))
_NbsCmmcSlotTemperatureLimit_Type.__name__=_D
_NbsCmmcSlotTemperatureLimit_Object=MibTableColumn
nbsCmmcSlotTemperatureLimit=_NbsCmmcSlotTemperatureLimit_Object((1,3,6,1,4,1,629,200,7,1,1,40),_NbsCmmcSlotTemperatureLimit_Type())
nbsCmmcSlotTemperatureLimit.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSlotTemperatureLimit.setStatus(_A)
class _NbsCmmcSlotTemperatureMin_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-100,100))
_NbsCmmcSlotTemperatureMin_Type.__name__=_D
_NbsCmmcSlotTemperatureMin_Object=MibTableColumn
nbsCmmcSlotTemperatureMin=_NbsCmmcSlotTemperatureMin_Object((1,3,6,1,4,1,629,200,7,1,1,41),_NbsCmmcSlotTemperatureMin_Type())
nbsCmmcSlotTemperatureMin.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSlotTemperatureMin.setStatus(_A)
_NbsCmmcLedTable_Object=MibTable
nbsCmmcLedTable=_NbsCmmcLedTable_Object((1,3,6,1,4,1,629,200,7,2))
if mibBuilder.loadTexts:nbsCmmcLedTable.setStatus(_A)
_NbsCmmcLedEntry_Object=MibTableRow
nbsCmmcLedEntry=_NbsCmmcLedEntry_Object((1,3,6,1,4,1,629,200,7,2,1))
nbsCmmcLedEntry.setIndexNames((0,_B,_Ae),(0,_B,_Af),(0,_B,_Ag))
if mibBuilder.loadTexts:nbsCmmcLedEntry.setStatus(_A)
_NbsCmmcLedChassisIndex_Type=Integer32
_NbsCmmcLedChassisIndex_Object=MibTableColumn
nbsCmmcLedChassisIndex=_NbsCmmcLedChassisIndex_Object((1,3,6,1,4,1,629,200,7,2,1,1),_NbsCmmcLedChassisIndex_Type())
nbsCmmcLedChassisIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcLedChassisIndex.setStatus(_A)
_NbsCmmcLedSlotIndex_Type=Integer32
_NbsCmmcLedSlotIndex_Object=MibTableColumn
nbsCmmcLedSlotIndex=_NbsCmmcLedSlotIndex_Object((1,3,6,1,4,1,629,200,7,2,1,2),_NbsCmmcLedSlotIndex_Type())
nbsCmmcLedSlotIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcLedSlotIndex.setStatus(_A)
_NbsCmmcLedIndex_Type=Integer32
_NbsCmmcLedIndex_Object=MibTableColumn
nbsCmmcLedIndex=_NbsCmmcLedIndex_Object((1,3,6,1,4,1,629,200,7,2,1,3),_NbsCmmcLedIndex_Type())
nbsCmmcLedIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcLedIndex.setStatus(_A)
class _NbsCmmcLedColor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_R,1),('green',2),('amber',3),(_w,4)))
_NbsCmmcLedColor_Type.__name__=_D
_NbsCmmcLedColor_Object=MibTableColumn
nbsCmmcLedColor=_NbsCmmcLedColor_Object((1,3,6,1,4,1,629,200,7,2,1,4),_NbsCmmcLedColor_Type())
nbsCmmcLedColor.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcLedColor.setStatus(_A)
class _NbsCmmcLedDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_NbsCmmcLedDescription_Type.__name__=_J
_NbsCmmcLedDescription_Object=MibTableColumn
nbsCmmcLedDescription=_NbsCmmcLedDescription_Object((1,3,6,1,4,1,629,200,7,2,1,5),_NbsCmmcLedDescription_Type())
nbsCmmcLedDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcLedDescription.setStatus(_A)
_NbsCmmcSlotFaceTable_Object=MibTable
nbsCmmcSlotFaceTable=_NbsCmmcSlotFaceTable_Object((1,3,6,1,4,1,629,200,7,3))
if mibBuilder.loadTexts:nbsCmmcSlotFaceTable.setStatus(_A)
_NbsCmmcSlotFaceEntry_Object=MibTableRow
nbsCmmcSlotFaceEntry=_NbsCmmcSlotFaceEntry_Object((1,3,6,1,4,1,629,200,7,3,1))
nbsCmmcSlotFaceEntry.setIndexNames((0,_B,_Ah),(0,_B,_Ai),(0,_B,_Aj))
if mibBuilder.loadTexts:nbsCmmcSlotFaceEntry.setStatus(_A)
_NbsCmmcSlotFaceChassisIndex_Type=Integer32
_NbsCmmcSlotFaceChassisIndex_Object=MibTableColumn
nbsCmmcSlotFaceChassisIndex=_NbsCmmcSlotFaceChassisIndex_Object((1,3,6,1,4,1,629,200,7,3,1,1),_NbsCmmcSlotFaceChassisIndex_Type())
nbsCmmcSlotFaceChassisIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSlotFaceChassisIndex.setStatus(_A)
_NbsCmmcSlotFaceSlotIndex_Type=Integer32
_NbsCmmcSlotFaceSlotIndex_Object=MibTableColumn
nbsCmmcSlotFaceSlotIndex=_NbsCmmcSlotFaceSlotIndex_Object((1,3,6,1,4,1,629,200,7,3,1,2),_NbsCmmcSlotFaceSlotIndex_Type())
nbsCmmcSlotFaceSlotIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSlotFaceSlotIndex.setStatus(_A)
_NbsCmmcSlotFaceRowIndex_Type=Integer32
_NbsCmmcSlotFaceRowIndex_Object=MibTableColumn
nbsCmmcSlotFaceRowIndex=_NbsCmmcSlotFaceRowIndex_Object((1,3,6,1,4,1,629,200,7,3,1,3),_NbsCmmcSlotFaceRowIndex_Type())
nbsCmmcSlotFaceRowIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSlotFaceRowIndex.setStatus(_A)
class _NbsCmmcSlotFaceSummary_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,500))
_NbsCmmcSlotFaceSummary_Type.__name__=_T
_NbsCmmcSlotFaceSummary_Object=MibTableColumn
nbsCmmcSlotFaceSummary=_NbsCmmcSlotFaceSummary_Object((1,3,6,1,4,1,629,200,7,3,1,4),_NbsCmmcSlotFaceSummary_Type())
nbsCmmcSlotFaceSummary.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSlotFaceSummary.setStatus(_A)
_NbsCmmcPortGrp_ObjectIdentity=ObjectIdentity
nbsCmmcPortGrp=_NbsCmmcPortGrp_ObjectIdentity((1,3,6,1,4,1,629,200,8))
if mibBuilder.loadTexts:nbsCmmcPortGrp.setStatus(_A)
_NbsCmmcPortTable_Object=MibTable
nbsCmmcPortTable=_NbsCmmcPortTable_Object((1,3,6,1,4,1,629,200,8,1))
if mibBuilder.loadTexts:nbsCmmcPortTable.setStatus(_A)
_NbsCmmcPortEntry_Object=MibTableRow
nbsCmmcPortEntry=_NbsCmmcPortEntry_Object((1,3,6,1,4,1,629,200,8,1,1))
nbsCmmcPortEntry.setIndexNames((0,_B,_Ak),(0,_B,_Al),(0,_B,_N))
if mibBuilder.loadTexts:nbsCmmcPortEntry.setStatus(_A)
_NbsCmmcPortChassisIndex_Type=Integer32
_NbsCmmcPortChassisIndex_Object=MibTableColumn
nbsCmmcPortChassisIndex=_NbsCmmcPortChassisIndex_Object((1,3,6,1,4,1,629,200,8,1,1,1),_NbsCmmcPortChassisIndex_Type())
nbsCmmcPortChassisIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcPortChassisIndex.setStatus(_A)
_NbsCmmcPortSlotIndex_Type=Integer32
_NbsCmmcPortSlotIndex_Object=MibTableColumn
nbsCmmcPortSlotIndex=_NbsCmmcPortSlotIndex_Object((1,3,6,1,4,1,629,200,8,1,1,2),_NbsCmmcPortSlotIndex_Type())
nbsCmmcPortSlotIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcPortSlotIndex.setStatus(_A)
_NbsCmmcPortIndex_Type=Integer32
_NbsCmmcPortIndex_Object=MibTableColumn
nbsCmmcPortIndex=_NbsCmmcPortIndex_Object((1,3,6,1,4,1,629,200,8,1,1,3),_NbsCmmcPortIndex_Type())
nbsCmmcPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcPortIndex.setStatus(_A)
_NbsCmmcPortType_Type=Integer32
_NbsCmmcPortType_Object=MibTableColumn
nbsCmmcPortType=_NbsCmmcPortType_Object((1,3,6,1,4,1,629,200,8,1,1,4),_NbsCmmcPortType_Type())
nbsCmmcPortType.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcPortType.setStatus(_A)
_NbsCmmcPortObjectId_Type=ObjectIdentifier
_NbsCmmcPortObjectId_Object=MibTableColumn
nbsCmmcPortObjectId=_NbsCmmcPortObjectId_Object((1,3,6,1,4,1,629,200,8,1,1,5),_NbsCmmcPortObjectId_Type())
nbsCmmcPortObjectId.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcPortObjectId.setStatus(_A)
class _NbsCmmcPortLink_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_w,1),('noSignal',2),('signalDetect',3),('link',4),('lock',5)))
_NbsCmmcPortLink_Type.__name__=_D
_NbsCmmcPortLink_Object=MibTableColumn
nbsCmmcPortLink=_NbsCmmcPortLink_Object((1,3,6,1,4,1,629,200,8,1,1,6),_NbsCmmcPortLink_Type())
nbsCmmcPortLink.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcPortLink.setStatus(_A)
class _NbsCmmcPortAutoNegotiation_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),(_R,2),(_S,3),('deprecated4',4),(_AE,5)))
_NbsCmmcPortAutoNegotiation_Type.__name__=_D
_NbsCmmcPortAutoNegotiation_Object=MibTableColumn
nbsCmmcPortAutoNegotiation=_NbsCmmcPortAutoNegotiation_Object((1,3,6,1,4,1,629,200,8,1,1,7),_NbsCmmcPortAutoNegotiation_Type())
nbsCmmcPortAutoNegotiation.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcPortAutoNegotiation.setStatus(_A)
class _NbsCmmcPortDuplex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('half',2),('full',3)))
_NbsCmmcPortDuplex_Type.__name__=_D
_NbsCmmcPortDuplex_Object=MibTableColumn
nbsCmmcPortDuplex=_NbsCmmcPortDuplex_Object((1,3,6,1,4,1,629,200,8,1,1,8),_NbsCmmcPortDuplex_Type())
nbsCmmcPortDuplex.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcPortDuplex.setStatus(_A)
class _NbsCmmcPortSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_w,1),('spd10Mbps',2),('spd100Mbps',3),('spdGigabit',4),('spd10Gbps',5)))
_NbsCmmcPortSpeed_Type.__name__=_D
_NbsCmmcPortSpeed_Object=MibTableColumn
nbsCmmcPortSpeed=_NbsCmmcPortSpeed_Object((1,3,6,1,4,1,629,200,8,1,1,9),_NbsCmmcPortSpeed_Type())
nbsCmmcPortSpeed.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcPortSpeed.setStatus(_A)
class _NbsCmmcPortRxActivity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_R,2),(_S,3)))
_NbsCmmcPortRxActivity_Type.__name__=_D
_NbsCmmcPortRxActivity_Object=MibTableColumn
nbsCmmcPortRxActivity=_NbsCmmcPortRxActivity_Object((1,3,6,1,4,1,629,200,8,1,1,10),_NbsCmmcPortRxActivity_Type())
nbsCmmcPortRxActivity.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcPortRxActivity.setStatus(_A)
class _NbsCmmcPortTxActivity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_R,2),(_S,3)))
_NbsCmmcPortTxActivity_Type.__name__=_D
_NbsCmmcPortTxActivity_Object=MibTableColumn
nbsCmmcPortTxActivity=_NbsCmmcPortTxActivity_Object((1,3,6,1,4,1,629,200,8,1,1,11),_NbsCmmcPortTxActivity_Type())
nbsCmmcPortTxActivity.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcPortTxActivity.setStatus(_A)
class _NbsCmmcPortCollisionActivity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_R,2),(_S,3)))
_NbsCmmcPortCollisionActivity_Type.__name__=_D
_NbsCmmcPortCollisionActivity_Object=MibTableColumn
nbsCmmcPortCollisionActivity=_NbsCmmcPortCollisionActivity_Object((1,3,6,1,4,1,629,200,8,1,1,12),_NbsCmmcPortCollisionActivity_Type())
nbsCmmcPortCollisionActivity.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcPortCollisionActivity.setStatus(_A)
class _NbsCmmcPortLoopback_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_R,2),(_S,3)))
_NbsCmmcPortLoopback_Type.__name__=_D
_NbsCmmcPortLoopback_Object=MibTableColumn
nbsCmmcPortLoopback=_NbsCmmcPortLoopback_Object((1,3,6,1,4,1,629,200,8,1,1,13),_NbsCmmcPortLoopback_Type())
nbsCmmcPortLoopback.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcPortLoopback.setStatus(_A)
class _NbsCmmcPortEnableAdmin_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_z,2),(_AF,3),(_Am,4)))
_NbsCmmcPortEnableAdmin_Type.__name__=_D
_NbsCmmcPortEnableAdmin_Object=MibTableColumn
nbsCmmcPortEnableAdmin=_NbsCmmcPortEnableAdmin_Object((1,3,6,1,4,1,629,200,8,1,1,14),_NbsCmmcPortEnableAdmin_Type())
nbsCmmcPortEnableAdmin.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcPortEnableAdmin.setStatus(_A)
class _NbsCmmcPortSelectLink_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_F,1),('standby',2),(_AD,3),(_Am,4),('deprecatedStandbyPreferred',5),('deprecatedActivePreferred',6)))
_NbsCmmcPortSelectLink_Type.__name__=_D
_NbsCmmcPortSelectLink_Object=MibTableColumn
nbsCmmcPortSelectLink=_NbsCmmcPortSelectLink_Object((1,3,6,1,4,1,629,200,8,1,1,15),_NbsCmmcPortSelectLink_Type())
nbsCmmcPortSelectLink.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcPortSelectLink.setStatus(_A)
class _NbsCmmcPortLIN_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_z,2),(_AF,3)))
_NbsCmmcPortLIN_Type.__name__=_D
_NbsCmmcPortLIN_Object=MibTableColumn
nbsCmmcPortLIN=_NbsCmmcPortLIN_Object((1,3,6,1,4,1,629,200,8,1,1,16),_NbsCmmcPortLIN_Type())
nbsCmmcPortLIN.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcPortLIN.setStatus(_A)
class _NbsCmmcPortAging_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_R,2),(_S,3)))
_NbsCmmcPortAging_Type.__name__=_D
_NbsCmmcPortAging_Object=MibTableColumn
nbsCmmcPortAging=_NbsCmmcPortAging_Object((1,3,6,1,4,1,629,200,8,1,1,17),_NbsCmmcPortAging_Type())
nbsCmmcPortAging.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcPortAging.setStatus(_A)
class _NbsCmmcPortMaxPacketSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),('max1518',2),('max1536',3),('max6k',4)))
_NbsCmmcPortMaxPacketSize_Type.__name__=_D
_NbsCmmcPortMaxPacketSize_Object=MibTableColumn
nbsCmmcPortMaxPacketSize=_NbsCmmcPortMaxPacketSize_Object((1,3,6,1,4,1,629,200,8,1,1,18),_NbsCmmcPortMaxPacketSize_Type())
nbsCmmcPortMaxPacketSize.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcPortMaxPacketSize.setStatus(_A)
class _NbsCmmcPortRemoteLoopback_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_R,2),(_S,3)))
_NbsCmmcPortRemoteLoopback_Type.__name__=_D
_NbsCmmcPortRemoteLoopback_Object=MibTableColumn
nbsCmmcPortRemoteLoopback=_NbsCmmcPortRemoteLoopback_Object((1,3,6,1,4,1,629,200,8,1,1,19),_NbsCmmcPortRemoteLoopback_Type())
nbsCmmcPortRemoteLoopback.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcPortRemoteLoopback.setStatus(_A)
class _NbsCmmcPortErrorActivity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_R,2),(_S,3)))
_NbsCmmcPortErrorActivity_Type.__name__=_D
_NbsCmmcPortErrorActivity_Object=MibTableColumn
nbsCmmcPortErrorActivity=_NbsCmmcPortErrorActivity_Object((1,3,6,1,4,1,629,200,8,1,1,20),_NbsCmmcPortErrorActivity_Type())
nbsCmmcPortErrorActivity.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcPortErrorActivity.setStatus(_A)
class _NbsCmmcPortName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_NbsCmmcPortName_Type.__name__=_J
_NbsCmmcPortName_Object=MibTableColumn
nbsCmmcPortName=_NbsCmmcPortName_Object((1,3,6,1,4,1,629,200,8,1,1,21),_NbsCmmcPortName_Type())
nbsCmmcPortName.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcPortName.setStatus(_A)
class _NbsCmmcPortValue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_NbsCmmcPortValue_Type.__name__=_T
_NbsCmmcPortValue_Object=MibTableColumn
nbsCmmcPortValue=_NbsCmmcPortValue_Object((1,3,6,1,4,1,629,200,8,1,1,22),_NbsCmmcPortValue_Type())
nbsCmmcPortValue.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcPortValue.setStatus(_A)
class _NbsCmmcPortThreshold_Type(Integer32):defaultValue=-2147483648;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsCmmcPortThreshold_Type.__name__=_D
_NbsCmmcPortThreshold_Object=MibTableColumn
nbsCmmcPortThreshold=_NbsCmmcPortThreshold_Object((1,3,6,1,4,1,629,200,8,1,1,23),_NbsCmmcPortThreshold_Type())
nbsCmmcPortThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcPortThreshold.setStatus(_A)
class _NbsCmmcPortThresholdAction_Type(Integer32):defaultValue=1
_NbsCmmcPortThresholdAction_Type.__name__=_D
_NbsCmmcPortThresholdAction_Object=MibTableColumn
nbsCmmcPortThresholdAction=_NbsCmmcPortThresholdAction_Object((1,3,6,1,4,1,629,200,8,1,1,24),_NbsCmmcPortThresholdAction_Type())
nbsCmmcPortThresholdAction.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcPortThresholdAction.setStatus(_A)
class _NbsCmmcPortRMChassis_Type(Integer32):defaultValue=0
_NbsCmmcPortRMChassis_Type.__name__=_D
_NbsCmmcPortRMChassis_Object=MibTableColumn
nbsCmmcPortRMChassis=_NbsCmmcPortRMChassis_Object((1,3,6,1,4,1,629,200,8,1,1,25),_NbsCmmcPortRMChassis_Type())
nbsCmmcPortRMChassis.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcPortRMChassis.setStatus(_A)
class _NbsCmmcPortRMSlot_Type(Integer32):defaultValue=0
_NbsCmmcPortRMSlot_Type.__name__=_D
_NbsCmmcPortRMSlot_Object=MibTableColumn
nbsCmmcPortRMSlot=_NbsCmmcPortRMSlot_Object((1,3,6,1,4,1,629,200,8,1,1,26),_NbsCmmcPortRMSlot_Type())
nbsCmmcPortRMSlot.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcPortRMSlot.setStatus(_A)
class _NbsCmmcPortRMPort_Type(Integer32):defaultValue=0
_NbsCmmcPortRMPort_Type.__name__=_D
_NbsCmmcPortRMPort_Object=MibTableColumn
nbsCmmcPortRMPort=_NbsCmmcPortRMPort_Object((1,3,6,1,4,1,629,200,8,1,1,27),_NbsCmmcPortRMPort_Type())
nbsCmmcPortRMPort.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcPortRMPort.setStatus(_A)
class _NbsCmmcPortSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_NbsCmmcPortSerialNumber_Type.__name__=_J
_NbsCmmcPortSerialNumber_Object=MibTableColumn
nbsCmmcPortSerialNumber=_NbsCmmcPortSerialNumber_Object((1,3,6,1,4,1,629,200,8,1,1,28),_NbsCmmcPortSerialNumber_Type())
nbsCmmcPortSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcPortSerialNumber.setStatus(_A)
class _NbsCmmcPortVendorInfo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_NbsCmmcPortVendorInfo_Type.__name__=_J
_NbsCmmcPortVendorInfo_Object=MibTableColumn
nbsCmmcPortVendorInfo=_NbsCmmcPortVendorInfo_Object((1,3,6,1,4,1,629,200,8,1,1,29),_NbsCmmcPortVendorInfo_Type())
nbsCmmcPortVendorInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcPortVendorInfo.setStatus(_A)
class _NbsCmmcPortTemperature_Type(Integer32):defaultValue=-2147483648;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsCmmcPortTemperature_Type.__name__=_D
_NbsCmmcPortTemperature_Object=MibTableColumn
nbsCmmcPortTemperature=_NbsCmmcPortTemperature_Object((1,3,6,1,4,1,629,200,8,1,1,30),_NbsCmmcPortTemperature_Type())
nbsCmmcPortTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcPortTemperature.setStatus(_A)
class _NbsCmmcPortTxPower_Type(Integer32):defaultValue=-2147483648;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsCmmcPortTxPower_Type.__name__=_D
_NbsCmmcPortTxPower_Object=MibTableColumn
nbsCmmcPortTxPower=_NbsCmmcPortTxPower_Object((1,3,6,1,4,1,629,200,8,1,1,31),_NbsCmmcPortTxPower_Type())
nbsCmmcPortTxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcPortTxPower.setStatus(_A)
class _NbsCmmcPortRxPower_Type(Integer32):defaultValue=-2147483648;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsCmmcPortRxPower_Type.__name__=_D
_NbsCmmcPortRxPower_Object=MibTableColumn
nbsCmmcPortRxPower=_NbsCmmcPortRxPower_Object((1,3,6,1,4,1,629,200,8,1,1,32),_NbsCmmcPortRxPower_Type())
nbsCmmcPortRxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcPortRxPower.setStatus(_A)
class _NbsCmmcPortBiasAmps_Type(Integer32):defaultValue=-1
_NbsCmmcPortBiasAmps_Type.__name__=_D
_NbsCmmcPortBiasAmps_Object=MibTableColumn
nbsCmmcPortBiasAmps=_NbsCmmcPortBiasAmps_Object((1,3,6,1,4,1,629,200,8,1,1,33),_NbsCmmcPortBiasAmps_Type())
nbsCmmcPortBiasAmps.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcPortBiasAmps.setStatus(_A)
class _NbsCmmcPortSupplyVolts_Type(Integer32):defaultValue=-1
_NbsCmmcPortSupplyVolts_Type.__name__=_D
_NbsCmmcPortSupplyVolts_Object=MibTableColumn
nbsCmmcPortSupplyVolts=_NbsCmmcPortSupplyVolts_Object((1,3,6,1,4,1,629,200,8,1,1,34),_NbsCmmcPortSupplyVolts_Type())
nbsCmmcPortSupplyVolts.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcPortSupplyVolts.setStatus(_A)
class _NbsCmmcPortMedium_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),('coax',2),('twistedPair',3),('singleMode',4),('multiMode',5)))
_NbsCmmcPortMedium_Type.__name__=_D
_NbsCmmcPortMedium_Object=MibTableColumn
nbsCmmcPortMedium=_NbsCmmcPortMedium_Object((1,3,6,1,4,1,629,200,8,1,1,35),_NbsCmmcPortMedium_Type())
nbsCmmcPortMedium.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcPortMedium.setStatus(_A)
_NbsCmmcPortConnector_Type=NbsCmmcEnumPortConnector
_NbsCmmcPortConnector_Object=MibTableColumn
nbsCmmcPortConnector=_NbsCmmcPortConnector_Object((1,3,6,1,4,1,629,200,8,1,1,36),_NbsCmmcPortConnector_Type())
nbsCmmcPortConnector.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcPortConnector.setStatus(_A)
class _NbsCmmcPortWavelength_Type(Integer32):defaultValue=-1
_NbsCmmcPortWavelength_Type.__name__=_D
_NbsCmmcPortWavelength_Object=MibTableColumn
nbsCmmcPortWavelength=_NbsCmmcPortWavelength_Object((1,3,6,1,4,1,629,200,8,1,1,37),_NbsCmmcPortWavelength_Type())
nbsCmmcPortWavelength.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcPortWavelength.setStatus(_A)
class _NbsCmmcPortDigitalDiags_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),('diagsOk',2),('diagsWarning',3),('diagsAlarm',4)))
_NbsCmmcPortDigitalDiags_Type.__name__=_D
_NbsCmmcPortDigitalDiags_Object=MibTableColumn
nbsCmmcPortDigitalDiags=_NbsCmmcPortDigitalDiags_Object((1,3,6,1,4,1,629,200,8,1,1,38),_NbsCmmcPortDigitalDiags_Type())
nbsCmmcPortDigitalDiags.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcPortDigitalDiags.setStatus(_A)
class _NbsCmmcPortZoneIdAdmin_Type(Integer32):defaultValue=0
_NbsCmmcPortZoneIdAdmin_Type.__name__=_D
_NbsCmmcPortZoneIdAdmin_Object=MibTableColumn
nbsCmmcPortZoneIdAdmin=_NbsCmmcPortZoneIdAdmin_Object((1,3,6,1,4,1,629,200,8,1,1,39),_NbsCmmcPortZoneIdAdmin_Type())
nbsCmmcPortZoneIdAdmin.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcPortZoneIdAdmin.setStatus(_A)
class _NbsCmmcPortNominalBitRate_Type(Integer32):defaultValue=-1
_NbsCmmcPortNominalBitRate_Type.__name__=_D
_NbsCmmcPortNominalBitRate_Object=MibTableColumn
nbsCmmcPortNominalBitRate=_NbsCmmcPortNominalBitRate_Object((1,3,6,1,4,1,629,200,8,1,1,40),_NbsCmmcPortNominalBitRate_Type())
nbsCmmcPortNominalBitRate.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcPortNominalBitRate.setStatus(_A)
_NbsCmmcPortModulePort_Type=Integer32
_NbsCmmcPortModulePort_Object=MibTableColumn
nbsCmmcPortModulePort=_NbsCmmcPortModulePort_Object((1,3,6,1,4,1,629,200,8,1,1,41),_NbsCmmcPortModulePort_Type())
nbsCmmcPortModulePort.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcPortModulePort.setStatus(_A)
class _NbsCmmcPortPartRev_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_NbsCmmcPortPartRev_Type.__name__=_J
_NbsCmmcPortPartRev_Object=MibTableColumn
nbsCmmcPortPartRev=_NbsCmmcPortPartRev_Object((1,3,6,1,4,1,629,200,8,1,1,42),_NbsCmmcPortPartRev_Type())
nbsCmmcPortPartRev.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcPortPartRev.setStatus(_A)
_NbsCmmcPortIfIndex_Type=Integer32
_NbsCmmcPortIfIndex_Object=MibTableColumn
nbsCmmcPortIfIndex=_NbsCmmcPortIfIndex_Object((1,3,6,1,4,1,629,200,8,1,1,43),_NbsCmmcPortIfIndex_Type())
nbsCmmcPortIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcPortIfIndex.setStatus(_A)
class _NbsCmmcPortLinked_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_x,1),(_y,2)))
_NbsCmmcPortLinked_Type.__name__=_D
_NbsCmmcPortLinked_Object=MibTableColumn
nbsCmmcPortLinked=_NbsCmmcPortLinked_Object((1,3,6,1,4,1,629,200,8,1,1,44),_NbsCmmcPortLinked_Type())
nbsCmmcPortLinked.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcPortLinked.setStatus(_A)
class _NbsCmmcPortOperational_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_x,1),(_y,2)))
_NbsCmmcPortOperational_Type.__name__=_D
_NbsCmmcPortOperational_Object=MibTableColumn
nbsCmmcPortOperational=_NbsCmmcPortOperational_Object((1,3,6,1,4,1,629,200,8,1,1,45),_NbsCmmcPortOperational_Type())
nbsCmmcPortOperational.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcPortOperational.setStatus(_A)
class _NbsCmmcPortZoneChassisAdmin_Type(Integer32):defaultValue=0
_NbsCmmcPortZoneChassisAdmin_Type.__name__=_D
_NbsCmmcPortZoneChassisAdmin_Object=MibTableColumn
nbsCmmcPortZoneChassisAdmin=_NbsCmmcPortZoneChassisAdmin_Object((1,3,6,1,4,1,629,200,8,1,1,46),_NbsCmmcPortZoneChassisAdmin_Type())
nbsCmmcPortZoneChassisAdmin.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcPortZoneChassisAdmin.setStatus(_A)
class _NbsCmmcPortZoneSlotAdmin_Type(Integer32):defaultValue=0
_NbsCmmcPortZoneSlotAdmin_Type.__name__=_D
_NbsCmmcPortZoneSlotAdmin_Object=MibTableColumn
nbsCmmcPortZoneSlotAdmin=_NbsCmmcPortZoneSlotAdmin_Object((1,3,6,1,4,1,629,200,8,1,1,47),_NbsCmmcPortZoneSlotAdmin_Type())
nbsCmmcPortZoneSlotAdmin.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcPortZoneSlotAdmin.setStatus(_A)
class _NbsCmmcPortAlarmCause_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_NbsCmmcPortAlarmCause_Type.__name__=_J
_NbsCmmcPortAlarmCause_Object=MibTableColumn
nbsCmmcPortAlarmCause=_NbsCmmcPortAlarmCause_Object((1,3,6,1,4,1,629,200,8,1,1,48),_NbsCmmcPortAlarmCause_Type())
nbsCmmcPortAlarmCause.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcPortAlarmCause.setStatus(_A)
class _NbsCmmcPortFlowControl_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_P,2),(_Q,3)))
_NbsCmmcPortFlowControl_Type.__name__=_D
_NbsCmmcPortFlowControl_Object=MibTableColumn
nbsCmmcPortFlowControl=_NbsCmmcPortFlowControl_Object((1,3,6,1,4,1,629,200,8,1,1,49),_NbsCmmcPortFlowControl_Type())
nbsCmmcPortFlowControl.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcPortFlowControl.setStatus(_A)
class _NbsCmmcPortAutoNegAd_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_NbsCmmcPortAutoNegAd_Type.__name__=_T
_NbsCmmcPortAutoNegAd_Object=MibTableColumn
nbsCmmcPortAutoNegAd=_NbsCmmcPortAutoNegAd_Object((1,3,6,1,4,1,629,200,8,1,1,50),_NbsCmmcPortAutoNegAd_Type())
nbsCmmcPortAutoNegAd.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcPortAutoNegAd.setStatus(_A)
class _NbsCmmcPortAutoNegEditable_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_NbsCmmcPortAutoNegEditable_Type.__name__=_T
_NbsCmmcPortAutoNegEditable_Object=MibTableColumn
nbsCmmcPortAutoNegEditable=_NbsCmmcPortAutoNegEditable_Object((1,3,6,1,4,1,629,200,8,1,1,51),_NbsCmmcPortAutoNegEditable_Type())
nbsCmmcPortAutoNegEditable.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcPortAutoNegEditable.setStatus(_A)
class _NbsCmmcPortWavelengthX_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,150))
_NbsCmmcPortWavelengthX_Type.__name__=_J
_NbsCmmcPortWavelengthX_Object=MibTableColumn
nbsCmmcPortWavelengthX=_NbsCmmcPortWavelengthX_Object((1,3,6,1,4,1,629,200,8,1,1,52),_NbsCmmcPortWavelengthX_Type())
nbsCmmcPortWavelengthX.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcPortWavelengthX.setStatus(_A)
class _NbsCmmcPortZoneIdOper_Type(Integer32):defaultValue=0
_NbsCmmcPortZoneIdOper_Type.__name__=_D
_NbsCmmcPortZoneIdOper_Object=MibTableColumn
nbsCmmcPortZoneIdOper=_NbsCmmcPortZoneIdOper_Object((1,3,6,1,4,1,629,200,8,1,1,53),_NbsCmmcPortZoneIdOper_Type())
nbsCmmcPortZoneIdOper.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcPortZoneIdOper.setStatus(_A)
class _NbsCmmcPortZoneSlotOper_Type(Integer32):defaultValue=0
_NbsCmmcPortZoneSlotOper_Type.__name__=_D
_NbsCmmcPortZoneSlotOper_Object=MibTableColumn
nbsCmmcPortZoneSlotOper=_NbsCmmcPortZoneSlotOper_Object((1,3,6,1,4,1,629,200,8,1,1,54),_NbsCmmcPortZoneSlotOper_Type())
nbsCmmcPortZoneSlotOper.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcPortZoneSlotOper.setStatus(_A)
class _NbsCmmcPortZoneChassisOper_Type(Integer32):defaultValue=0
_NbsCmmcPortZoneChassisOper_Type.__name__=_D
_NbsCmmcPortZoneChassisOper_Object=MibTableColumn
nbsCmmcPortZoneChassisOper=_NbsCmmcPortZoneChassisOper_Object((1,3,6,1,4,1,629,200,8,1,1,55),_NbsCmmcPortZoneChassisOper_Type())
nbsCmmcPortZoneChassisOper.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcPortZoneChassisOper.setStatus(_A)
class _NbsCmmcPortLinkMatch_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_P,2),(_Q,3)))
_NbsCmmcPortLinkMatch_Type.__name__=_D
_NbsCmmcPortLinkMatch_Object=MibTableColumn
nbsCmmcPortLinkMatch=_NbsCmmcPortLinkMatch_Object((1,3,6,1,4,1,629,200,8,1,1,56),_NbsCmmcPortLinkMatch_Type())
nbsCmmcPortLinkMatch.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcPortLinkMatch.setStatus(_A)
class _NbsCmmcPortMDIPinoutAdmin_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),('mdi',2),('mdix',3),('autoSense',4)))
_NbsCmmcPortMDIPinoutAdmin_Type.__name__=_D
_NbsCmmcPortMDIPinoutAdmin_Object=MibTableColumn
nbsCmmcPortMDIPinoutAdmin=_NbsCmmcPortMDIPinoutAdmin_Object((1,3,6,1,4,1,629,200,8,1,1,57),_NbsCmmcPortMDIPinoutAdmin_Type())
nbsCmmcPortMDIPinoutAdmin.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcPortMDIPinoutAdmin.setStatus(_A)
class _NbsCmmcPortMDIPinoutOper_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('mdi',2),('mdix',3)))
_NbsCmmcPortMDIPinoutOper_Type.__name__=_D
_NbsCmmcPortMDIPinoutOper_Object=MibTableColumn
nbsCmmcPortMDIPinoutOper=_NbsCmmcPortMDIPinoutOper_Object((1,3,6,1,4,1,629,200,8,1,1,58),_NbsCmmcPortMDIPinoutOper_Type())
nbsCmmcPortMDIPinoutOper.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcPortMDIPinoutOper.setStatus(_A)
class _NbsCmmcPortFCRecvAdmin_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),('drop',2),('comply',3),('passThru',4)))
_NbsCmmcPortFCRecvAdmin_Type.__name__=_D
_NbsCmmcPortFCRecvAdmin_Object=MibTableColumn
nbsCmmcPortFCRecvAdmin=_NbsCmmcPortFCRecvAdmin_Object((1,3,6,1,4,1,629,200,8,1,1,59),_NbsCmmcPortFCRecvAdmin_Type())
nbsCmmcPortFCRecvAdmin.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcPortFCRecvAdmin.setStatus(_A)
class _NbsCmmcPortFCRecvOper_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),('drop',2),('comply',3),('passThru',4)))
_NbsCmmcPortFCRecvOper_Type.__name__=_D
_NbsCmmcPortFCRecvOper_Object=MibTableColumn
nbsCmmcPortFCRecvOper=_NbsCmmcPortFCRecvOper_Object((1,3,6,1,4,1,629,200,8,1,1,60),_NbsCmmcPortFCRecvOper_Type())
nbsCmmcPortFCRecvOper.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcPortFCRecvOper.setStatus(_A)
class _NbsCmmcPortFCSendAdmin_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_P,2),(_Q,3)))
_NbsCmmcPortFCSendAdmin_Type.__name__=_D
_NbsCmmcPortFCSendAdmin_Object=MibTableColumn
nbsCmmcPortFCSendAdmin=_NbsCmmcPortFCSendAdmin_Object((1,3,6,1,4,1,629,200,8,1,1,61),_NbsCmmcPortFCSendAdmin_Type())
nbsCmmcPortFCSendAdmin.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcPortFCSendAdmin.setStatus(_A)
class _NbsCmmcPortFCSendOper_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_P,2),(_Q,3)))
_NbsCmmcPortFCSendOper_Type.__name__=_D
_NbsCmmcPortFCSendOper_Object=MibTableColumn
nbsCmmcPortFCSendOper=_NbsCmmcPortFCSendOper_Object((1,3,6,1,4,1,629,200,8,1,1,62),_NbsCmmcPortFCSendOper_Type())
nbsCmmcPortFCSendOper.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcPortFCSendOper.setStatus(_A)
class _NbsCmmcPortAutoNegWait_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,254))
_NbsCmmcPortAutoNegWait_Type.__name__=_D
_NbsCmmcPortAutoNegWait_Object=MibTableColumn
nbsCmmcPortAutoNegWait=_NbsCmmcPortAutoNegWait_Object((1,3,6,1,4,1,629,200,8,1,1,63),_NbsCmmcPortAutoNegWait_Type())
nbsCmmcPortAutoNegWait.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcPortAutoNegWait.setStatus(_A)
class _NbsCmmcPortTemperatureLevel_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_F,1),(_h,2),(_i,3),(_j,4),(_k,5),(_l,6)))
_NbsCmmcPortTemperatureLevel_Type.__name__=_D
_NbsCmmcPortTemperatureLevel_Object=MibTableColumn
nbsCmmcPortTemperatureLevel=_NbsCmmcPortTemperatureLevel_Object((1,3,6,1,4,1,629,200,8,1,1,64),_NbsCmmcPortTemperatureLevel_Type())
nbsCmmcPortTemperatureLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcPortTemperatureLevel.setStatus(_A)
class _NbsCmmcPortTxPowerLevel_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_F,1),(_h,2),(_i,3),(_j,4),(_k,5),(_l,6)))
_NbsCmmcPortTxPowerLevel_Type.__name__=_D
_NbsCmmcPortTxPowerLevel_Object=MibTableColumn
nbsCmmcPortTxPowerLevel=_NbsCmmcPortTxPowerLevel_Object((1,3,6,1,4,1,629,200,8,1,1,65),_NbsCmmcPortTxPowerLevel_Type())
nbsCmmcPortTxPowerLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcPortTxPowerLevel.setStatus(_A)
class _NbsCmmcPortRxPowerLevel_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_F,1),(_h,2),(_i,3),(_j,4),(_k,5),(_l,6)))
_NbsCmmcPortRxPowerLevel_Type.__name__=_D
_NbsCmmcPortRxPowerLevel_Object=MibTableColumn
nbsCmmcPortRxPowerLevel=_NbsCmmcPortRxPowerLevel_Object((1,3,6,1,4,1,629,200,8,1,1,66),_NbsCmmcPortRxPowerLevel_Type())
nbsCmmcPortRxPowerLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcPortRxPowerLevel.setStatus(_A)
class _NbsCmmcPortBiasAmpsLevel_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_F,1),(_h,2),(_i,3),(_j,4),(_k,5),(_l,6)))
_NbsCmmcPortBiasAmpsLevel_Type.__name__=_D
_NbsCmmcPortBiasAmpsLevel_Object=MibTableColumn
nbsCmmcPortBiasAmpsLevel=_NbsCmmcPortBiasAmpsLevel_Object((1,3,6,1,4,1,629,200,8,1,1,67),_NbsCmmcPortBiasAmpsLevel_Type())
nbsCmmcPortBiasAmpsLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcPortBiasAmpsLevel.setStatus(_A)
class _NbsCmmcPortSupplyVoltsLevel_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_F,1),(_h,2),(_i,3),(_j,4),(_k,5),(_l,6)))
_NbsCmmcPortSupplyVoltsLevel_Type.__name__=_D
_NbsCmmcPortSupplyVoltsLevel_Object=MibTableColumn
nbsCmmcPortSupplyVoltsLevel=_NbsCmmcPortSupplyVoltsLevel_Object((1,3,6,1,4,1,629,200,8,1,1,68),_NbsCmmcPortSupplyVoltsLevel_Type())
nbsCmmcPortSupplyVoltsLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcPortSupplyVoltsLevel.setStatus(_A)
class _NbsCmmcPortAmpGainOper_Type(Integer32):defaultValue=-1
_NbsCmmcPortAmpGainOper_Type.__name__=_D
_NbsCmmcPortAmpGainOper_Object=MibTableColumn
nbsCmmcPortAmpGainOper=_NbsCmmcPortAmpGainOper_Object((1,3,6,1,4,1,629,200,8,1,1,69),_NbsCmmcPortAmpGainOper_Type())
nbsCmmcPortAmpGainOper.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcPortAmpGainOper.setStatus(_A)
class _NbsCmmcPortAmpGainAdmin_Type(Integer32):defaultValue=-1
_NbsCmmcPortAmpGainAdmin_Type.__name__=_D
_NbsCmmcPortAmpGainAdmin_Object=MibTableColumn
nbsCmmcPortAmpGainAdmin=_NbsCmmcPortAmpGainAdmin_Object((1,3,6,1,4,1,629,200,8,1,1,70),_NbsCmmcPortAmpGainAdmin_Type())
nbsCmmcPortAmpGainAdmin.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcPortAmpGainAdmin.setStatus(_A)
class _NbsCmmcPortAmpOutputPwrAdmin_Type(Integer32):defaultValue=-2147483648;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsCmmcPortAmpOutputPwrAdmin_Type.__name__=_D
_NbsCmmcPortAmpOutputPwrAdmin_Object=MibTableColumn
nbsCmmcPortAmpOutputPwrAdmin=_NbsCmmcPortAmpOutputPwrAdmin_Object((1,3,6,1,4,1,629,200,8,1,1,71),_NbsCmmcPortAmpOutputPwrAdmin_Type())
nbsCmmcPortAmpOutputPwrAdmin.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcPortAmpOutputPwrAdmin.setStatus(_A)
class _NbsCmmcPortProtoCapabilities_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_NbsCmmcPortProtoCapabilities_Type.__name__=_T
_NbsCmmcPortProtoCapabilities_Object=MibTableColumn
nbsCmmcPortProtoCapabilities=_NbsCmmcPortProtoCapabilities_Object((1,3,6,1,4,1,629,200,8,1,1,72),_NbsCmmcPortProtoCapabilities_Type())
nbsCmmcPortProtoCapabilities.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcPortProtoCapabilities.setStatus(_A)
class _NbsCmmcPortProtoAdmin_Type(Integer32):defaultValue=0
_NbsCmmcPortProtoAdmin_Type.__name__=_D
_NbsCmmcPortProtoAdmin_Object=MibTableColumn
nbsCmmcPortProtoAdmin=_NbsCmmcPortProtoAdmin_Object((1,3,6,1,4,1,629,200,8,1,1,73),_NbsCmmcPortProtoAdmin_Type())
nbsCmmcPortProtoAdmin.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcPortProtoAdmin.setStatus(_A)
class _NbsCmmcPortProtoOper_Type(Integer32):defaultValue=0
_NbsCmmcPortProtoOper_Type.__name__=_D
_NbsCmmcPortProtoOper_Object=MibTableColumn
nbsCmmcPortProtoOper=_NbsCmmcPortProtoOper_Object((1,3,6,1,4,1,629,200,8,1,1,74),_NbsCmmcPortProtoOper_Type())
nbsCmmcPortProtoOper.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcPortProtoOper.setStatus(_A)
class _NbsCmmcPortPreambleLen_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('standard',2),('variable',3)))
_NbsCmmcPortPreambleLen_Type.__name__=_D
_NbsCmmcPortPreambleLen_Object=MibTableColumn
nbsCmmcPortPreambleLen=_NbsCmmcPortPreambleLen_Object((1,3,6,1,4,1,629,200,8,1,1,75),_NbsCmmcPortPreambleLen_Type())
nbsCmmcPortPreambleLen.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcPortPreambleLen.setStatus(_A)
class _NbsCmmcPortPreferred_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_x,2),(_y,3)))
_NbsCmmcPortPreferred_Type.__name__=_D
_NbsCmmcPortPreferred_Object=MibTableColumn
nbsCmmcPortPreferred=_NbsCmmcPortPreferred_Object((1,3,6,1,4,1,629,200,8,1,1,76),_NbsCmmcPortPreferred_Type())
nbsCmmcPortPreferred.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcPortPreferred.setStatus(_A)
class _NbsCmmcPortCableLen_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_F,1),('len133',2),('len266',3),('len399',4),('len533',5),('len655',6),('shortHaul',7),('longHaul',8)))
_NbsCmmcPortCableLen_Type.__name__=_D
_NbsCmmcPortCableLen_Object=MibTableColumn
nbsCmmcPortCableLen=_NbsCmmcPortCableLen_Object((1,3,6,1,4,1,629,200,8,1,1,77),_NbsCmmcPortCableLen_Type())
nbsCmmcPortCableLen.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcPortCableLen.setStatus(_A)
class _NbsCmmcPortRedundantTxMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('oneColonOne',2),('onePlusOne',3)))
_NbsCmmcPortRedundantTxMode_Type.__name__=_D
_NbsCmmcPortRedundantTxMode_Object=MibTableColumn
nbsCmmcPortRedundantTxMode=_NbsCmmcPortRedundantTxMode_Object((1,3,6,1,4,1,629,200,8,1,1,78),_NbsCmmcPortRedundantTxMode_Type())
nbsCmmcPortRedundantTxMode.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcPortRedundantTxMode.setStatus(_A)
class _NbsCmmcPortTermination_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),(_z,2),('ohm120',3),('ohm100',4),('ohm75',5)))
_NbsCmmcPortTermination_Type.__name__=_D
_NbsCmmcPortTermination_Object=MibTableColumn
nbsCmmcPortTermination=_NbsCmmcPortTermination_Object((1,3,6,1,4,1,629,200,8,1,1,79),_NbsCmmcPortTermination_Type())
nbsCmmcPortTermination.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcPortTermination.setStatus(_A)
class _NbsCmmcPortDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,240))
_NbsCmmcPortDescription_Type.__name__=_J
_NbsCmmcPortDescription_Object=MibTableColumn
nbsCmmcPortDescription=_NbsCmmcPortDescription_Object((1,3,6,1,4,1,629,200,8,1,1,80),_NbsCmmcPortDescription_Type())
nbsCmmcPortDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcPortDescription.setStatus(_A)
class _NbsCmmcPortTransmitUnmapped_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_P,2),(_Q,3)))
_NbsCmmcPortTransmitUnmapped_Type.__name__=_D
_NbsCmmcPortTransmitUnmapped_Object=MibTableColumn
nbsCmmcPortTransmitUnmapped=_NbsCmmcPortTransmitUnmapped_Object((1,3,6,1,4,1,629,200,8,1,1,81),_NbsCmmcPortTransmitUnmapped_Type())
nbsCmmcPortTransmitUnmapped.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcPortTransmitUnmapped.setStatus(_A)
class _NbsCmmcPortToggleMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_P,2),(_Q,3)))
_NbsCmmcPortToggleMode_Type.__name__=_D
_NbsCmmcPortToggleMode_Object=MibTableColumn
nbsCmmcPortToggleMode=_NbsCmmcPortToggleMode_Object((1,3,6,1,4,1,629,200,8,1,1,82),_NbsCmmcPortToggleMode_Type())
nbsCmmcPortToggleMode.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcPortToggleMode.setStatus(_A)
class _NbsCmmcPortCrossConnect_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_a,2),(_Y,3)))
_NbsCmmcPortCrossConnect_Type.__name__=_D
_NbsCmmcPortCrossConnect_Object=MibTableColumn
nbsCmmcPortCrossConnect=_NbsCmmcPortCrossConnect_Object((1,3,6,1,4,1,629,200,8,1,1,83),_NbsCmmcPortCrossConnect_Type())
nbsCmmcPortCrossConnect.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcPortCrossConnect.setStatus(_A)
class _NbsCmmcPortZoneIfIndexAdmin_Type(Integer32):defaultValue=0
_NbsCmmcPortZoneIfIndexAdmin_Type.__name__=_D
_NbsCmmcPortZoneIfIndexAdmin_Object=MibTableColumn
nbsCmmcPortZoneIfIndexAdmin=_NbsCmmcPortZoneIfIndexAdmin_Object((1,3,6,1,4,1,629,200,8,1,1,84),_NbsCmmcPortZoneIfIndexAdmin_Type())
nbsCmmcPortZoneIfIndexAdmin.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcPortZoneIfIndexAdmin.setStatus(_A)
class _NbsCmmcPortZoneIfIndexOper_Type(Integer32):defaultValue=0
_NbsCmmcPortZoneIfIndexOper_Type.__name__=_D
_NbsCmmcPortZoneIfIndexOper_Object=MibTableColumn
nbsCmmcPortZoneIfIndexOper=_NbsCmmcPortZoneIfIndexOper_Object((1,3,6,1,4,1,629,200,8,1,1,85),_NbsCmmcPortZoneIfIndexOper_Type())
nbsCmmcPortZoneIfIndexOper.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcPortZoneIfIndexOper.setStatus(_A)
class _NbsCmmcPortEnableOper_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_z,2),(_AF,3)))
_NbsCmmcPortEnableOper_Type.__name__=_D
_NbsCmmcPortEnableOper_Object=MibTableColumn
nbsCmmcPortEnableOper=_NbsCmmcPortEnableOper_Object((1,3,6,1,4,1,629,200,8,1,1,86),_NbsCmmcPortEnableOper_Type())
nbsCmmcPortEnableOper.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcPortEnableOper.setStatus(_A)
class _NbsCmmcPortMappingType_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_F,1),('unavailable',2),('open',3),('source',4),('destination',5),('sourceHelper',6),('interChasLink',7)))
_NbsCmmcPortMappingType_Type.__name__=_D
_NbsCmmcPortMappingType_Object=MibTableColumn
nbsCmmcPortMappingType=_NbsCmmcPortMappingType_Object((1,3,6,1,4,1,629,200,8,1,1,87),_NbsCmmcPortMappingType_Type())
nbsCmmcPortMappingType.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcPortMappingType.setStatus(_A)
class _NbsCmmcPortCountersState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_r,2),(_Y,3)))
_NbsCmmcPortCountersState_Type.__name__=_D
_NbsCmmcPortCountersState_Object=MibTableColumn
nbsCmmcPortCountersState=_NbsCmmcPortCountersState_Object((1,3,6,1,4,1,629,200,8,1,1,88),_NbsCmmcPortCountersState_Type())
nbsCmmcPortCountersState.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcPortCountersState.setStatus(_A)
class _NbsCmmcPortAmpGainMinimum_Type(Integer32):defaultValue=0
_NbsCmmcPortAmpGainMinimum_Type.__name__=_D
_NbsCmmcPortAmpGainMinimum_Object=MibTableColumn
nbsCmmcPortAmpGainMinimum=_NbsCmmcPortAmpGainMinimum_Object((1,3,6,1,4,1,629,200,8,1,1,89),_NbsCmmcPortAmpGainMinimum_Type())
nbsCmmcPortAmpGainMinimum.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcPortAmpGainMinimum.setStatus(_A)
class _NbsCmmcPortAmpGainMaximum_Type(Integer32):defaultValue=0
_NbsCmmcPortAmpGainMaximum_Type.__name__=_D
_NbsCmmcPortAmpGainMaximum_Object=MibTableColumn
nbsCmmcPortAmpGainMaximum=_NbsCmmcPortAmpGainMaximum_Object((1,3,6,1,4,1,629,200,8,1,1,90),_NbsCmmcPortAmpGainMaximum_Type())
nbsCmmcPortAmpGainMaximum.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcPortAmpGainMaximum.setStatus(_A)
class _NbsCmmcPortAmpGainStepSize_Type(Integer32):defaultValue=100
_NbsCmmcPortAmpGainStepSize_Type.__name__=_D
_NbsCmmcPortAmpGainStepSize_Object=MibTableColumn
nbsCmmcPortAmpGainStepSize=_NbsCmmcPortAmpGainStepSize_Object((1,3,6,1,4,1,629,200,8,1,1,91),_NbsCmmcPortAmpGainStepSize_Type())
nbsCmmcPortAmpGainStepSize.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcPortAmpGainStepSize.setStatus(_A)
class _NbsCmmcPortSniffer_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_R,2),(_S,3)))
_NbsCmmcPortSniffer_Type.__name__=_D
_NbsCmmcPortSniffer_Object=MibTableColumn
nbsCmmcPortSniffer=_NbsCmmcPortSniffer_Object((1,3,6,1,4,1,629,200,8,1,1,92),_NbsCmmcPortSniffer_Type())
nbsCmmcPortSniffer.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcPortSniffer.setStatus(_A)
_NbsCmmcPortExternalLink1_Type=InterfaceIndex
_NbsCmmcPortExternalLink1_Object=MibTableColumn
nbsCmmcPortExternalLink1=_NbsCmmcPortExternalLink1_Object((1,3,6,1,4,1,629,200,8,1,1,93),_NbsCmmcPortExternalLink1_Type())
nbsCmmcPortExternalLink1.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcPortExternalLink1.setStatus(_A)
_NbsCmmcPortExternalLink2_Type=InterfaceIndex
_NbsCmmcPortExternalLink2_Object=MibTableColumn
nbsCmmcPortExternalLink2=_NbsCmmcPortExternalLink2_Object((1,3,6,1,4,1,629,200,8,1,1,94),_NbsCmmcPortExternalLink2_Type())
nbsCmmcPortExternalLink2.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcPortExternalLink2.setStatus(_A)
class _NbsCmmcPortNVAreaBanks_Type(Integer32):defaultValue=0
_NbsCmmcPortNVAreaBanks_Type.__name__=_D
_NbsCmmcPortNVAreaBanks_Object=MibTableColumn
nbsCmmcPortNVAreaBanks=_NbsCmmcPortNVAreaBanks_Object((1,3,6,1,4,1,629,200,8,1,1,95),_NbsCmmcPortNVAreaBanks_Type())
nbsCmmcPortNVAreaBanks.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcPortNVAreaBanks.setStatus(_A)
class _NbsCmmcPortFirmwareCaps_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_NbsCmmcPortFirmwareCaps_Type.__name__=_T
_NbsCmmcPortFirmwareCaps_Object=MibTableColumn
nbsCmmcPortFirmwareCaps=_NbsCmmcPortFirmwareCaps_Object((1,3,6,1,4,1,629,200,8,1,1,96),_NbsCmmcPortFirmwareCaps_Type())
nbsCmmcPortFirmwareCaps.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcPortFirmwareCaps.setStatus(_A)
class _NbsCmmcPortFirmwareLoad_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_NbsCmmcPortFirmwareLoad_Type.__name__=_T
_NbsCmmcPortFirmwareLoad_Object=MibTableColumn
nbsCmmcPortFirmwareLoad=_NbsCmmcPortFirmwareLoad_Object((1,3,6,1,4,1,629,200,8,1,1,97),_NbsCmmcPortFirmwareLoad_Type())
nbsCmmcPortFirmwareLoad.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcPortFirmwareLoad.setStatus(_A)
class _NbsCmmcPortNVAreaAdmin_Type(Integer32):defaultValue=0
_NbsCmmcPortNVAreaAdmin_Type.__name__=_D
_NbsCmmcPortNVAreaAdmin_Object=MibTableColumn
nbsCmmcPortNVAreaAdmin=_NbsCmmcPortNVAreaAdmin_Object((1,3,6,1,4,1,629,200,8,1,1,98),_NbsCmmcPortNVAreaAdmin_Type())
nbsCmmcPortNVAreaAdmin.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcPortNVAreaAdmin.setStatus(_A)
class _NbsCmmcPortNVAreaOper_Type(Integer32):defaultValue=-1
_NbsCmmcPortNVAreaOper_Type.__name__=_D
_NbsCmmcPortNVAreaOper_Object=MibTableColumn
nbsCmmcPortNVAreaOper=_NbsCmmcPortNVAreaOper_Object((1,3,6,1,4,1,629,200,8,1,1,99),_NbsCmmcPortNVAreaOper_Type())
nbsCmmcPortNVAreaOper.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcPortNVAreaOper.setStatus(_A)
class _NbsCmmcPortLoader_Type(Integer32):defaultValue=0
_NbsCmmcPortLoader_Type.__name__=_D
_NbsCmmcPortLoader_Object=MibTableColumn
nbsCmmcPortLoader=_NbsCmmcPortLoader_Object((1,3,6,1,4,1,629,200,8,1,1,100),_NbsCmmcPortLoader_Type())
nbsCmmcPortLoader.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcPortLoader.setStatus(_A)
_NbsCmmcNtpGrp_ObjectIdentity=ObjectIdentity
nbsCmmcNtpGrp=_NbsCmmcNtpGrp_ObjectIdentity((1,3,6,1,4,1,629,200,9))
if mibBuilder.loadTexts:nbsCmmcNtpGrp.setStatus(_A)
_NbsCmmcSmtpGrp_ObjectIdentity=ObjectIdentity
nbsCmmcSmtpGrp=_NbsCmmcSmtpGrp_ObjectIdentity((1,3,6,1,4,1,629,200,10))
if mibBuilder.loadTexts:nbsCmmcSmtpGrp.setStatus(_A)
class _NbsCmmcSmtpDomainName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_NbsCmmcSmtpDomainName_Type.__name__=_J
_NbsCmmcSmtpDomainName_Object=MibScalar
nbsCmmcSmtpDomainName=_NbsCmmcSmtpDomainName_Object((1,3,6,1,4,1,629,200,10,1),_NbsCmmcSmtpDomainName_Type())
nbsCmmcSmtpDomainName.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSmtpDomainName.setStatus(_K)
_NbsCmmcSmtpServerAddress_Type=IpAddress
_NbsCmmcSmtpServerAddress_Object=MibScalar
nbsCmmcSmtpServerAddress=_NbsCmmcSmtpServerAddress_Object((1,3,6,1,4,1,629,200,10,2),_NbsCmmcSmtpServerAddress_Type())
nbsCmmcSmtpServerAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSmtpServerAddress.setStatus(_K)
class _NbsCmmcSmtpRcvrLevel_Type(Integer32):defaultValue=0
_NbsCmmcSmtpRcvrLevel_Type.__name__=_D
_NbsCmmcSmtpRcvrLevel_Object=MibScalar
nbsCmmcSmtpRcvrLevel=_NbsCmmcSmtpRcvrLevel_Object((1,3,6,1,4,1,629,200,10,3),_NbsCmmcSmtpRcvrLevel_Type())
nbsCmmcSmtpRcvrLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSmtpRcvrLevel.setStatus(_K)
_NbsCmmcSmtpRcvrNum_Type=Integer32
_NbsCmmcSmtpRcvrNum_Object=MibScalar
nbsCmmcSmtpRcvrNum=_NbsCmmcSmtpRcvrNum_Object((1,3,6,1,4,1,629,200,10,4),_NbsCmmcSmtpRcvrNum_Type())
nbsCmmcSmtpRcvrNum.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSmtpRcvrNum.setStatus(_K)
_NbsCmmcSmtpRcvrTable_Object=MibTable
nbsCmmcSmtpRcvrTable=_NbsCmmcSmtpRcvrTable_Object((1,3,6,1,4,1,629,200,10,5))
if mibBuilder.loadTexts:nbsCmmcSmtpRcvrTable.setStatus(_K)
_NbsCmmcSmtpRcvrEntry_Object=MibTableRow
nbsCmmcSmtpRcvrEntry=_NbsCmmcSmtpRcvrEntry_Object((1,3,6,1,4,1,629,200,10,5,1))
nbsCmmcSmtpRcvrEntry.setIndexNames((0,_B,_An))
if mibBuilder.loadTexts:nbsCmmcSmtpRcvrEntry.setStatus(_K)
_NbsCmmcSmtpRcvrIndex_Type=Integer32
_NbsCmmcSmtpRcvrIndex_Object=MibTableColumn
nbsCmmcSmtpRcvrIndex=_NbsCmmcSmtpRcvrIndex_Object((1,3,6,1,4,1,629,200,10,5,1,1),_NbsCmmcSmtpRcvrIndex_Type())
nbsCmmcSmtpRcvrIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSmtpRcvrIndex.setStatus(_K)
class _NbsCmmcSmtpRcvrEmailAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_NbsCmmcSmtpRcvrEmailAddress_Type.__name__=_J
_NbsCmmcSmtpRcvrEmailAddress_Object=MibTableColumn
nbsCmmcSmtpRcvrEmailAddress=_NbsCmmcSmtpRcvrEmailAddress_Object((1,3,6,1,4,1,629,200,10,5,1,2),_NbsCmmcSmtpRcvrEmailAddress_Type())
nbsCmmcSmtpRcvrEmailAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSmtpRcvrEmailAddress.setStatus(_K)
class _NbsCmmcSmtpRcvrStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_q,1),('valid',2)))
_NbsCmmcSmtpRcvrStatus_Type.__name__=_D
_NbsCmmcSmtpRcvrStatus_Object=MibTableColumn
nbsCmmcSmtpRcvrStatus=_NbsCmmcSmtpRcvrStatus_Object((1,3,6,1,4,1,629,200,10,5,1,3),_NbsCmmcSmtpRcvrStatus_Type())
nbsCmmcSmtpRcvrStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSmtpRcvrStatus.setStatus(_K)
_NbsCmmcSysLogGrp_ObjectIdentity=ObjectIdentity
nbsCmmcSysLogGrp=_NbsCmmcSysLogGrp_ObjectIdentity((1,3,6,1,4,1,629,200,11))
if mibBuilder.loadTexts:nbsCmmcSysLogGrp.setStatus(_A)
class _NbsCmmcSysLogRunningLevel_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_P,1),(_f,2),(_c,3),(_d,4),(_A0,5),('memo',6),(_g,7)))
_NbsCmmcSysLogRunningLevel_Type.__name__=_D
_NbsCmmcSysLogRunningLevel_Object=MibScalar
nbsCmmcSysLogRunningLevel=_NbsCmmcSysLogRunningLevel_Object((1,3,6,1,4,1,629,200,11,1),_NbsCmmcSysLogRunningLevel_Type())
nbsCmmcSysLogRunningLevel.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysLogRunningLevel.setStatus(_A)
class _NbsCmmcSysLogNvLevel_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_P,1),(_f,2),(_c,3),(_d,4),(_A0,5),('memo',6),(_g,7)))
_NbsCmmcSysLogNvLevel_Type.__name__=_D
_NbsCmmcSysLogNvLevel_Object=MibScalar
nbsCmmcSysLogNvLevel=_NbsCmmcSysLogNvLevel_Object((1,3,6,1,4,1,629,200,11,2),_NbsCmmcSysLogNvLevel_Type())
nbsCmmcSysLogNvLevel.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysLogNvLevel.setStatus(_A)
class _NbsCmmcSysLogTrapLevel_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_P,1),(_f,2),(_c,3),(_d,4),(_A0,5),('memo',6),(_g,7)))
_NbsCmmcSysLogTrapLevel_Type.__name__=_D
_NbsCmmcSysLogTrapLevel_Object=MibScalar
nbsCmmcSysLogTrapLevel=_NbsCmmcSysLogTrapLevel_Object((1,3,6,1,4,1,629,200,11,3),_NbsCmmcSysLogTrapLevel_Type())
nbsCmmcSysLogTrapLevel.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysLogTrapLevel.setStatus(_A)
class _NbsCmmcSysLogEmailLevel_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_P,1),(_f,2),(_c,3),(_d,4),(_AE,5),(_Ab,6),(_g,7),(_F,8)))
_NbsCmmcSysLogEmailLevel_Type.__name__=_D
_NbsCmmcSysLogEmailLevel_Object=MibScalar
nbsCmmcSysLogEmailLevel=_NbsCmmcSysLogEmailLevel_Object((1,3,6,1,4,1,629,200,11,4),_NbsCmmcSysLogEmailLevel_Type())
nbsCmmcSysLogEmailLevel.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysLogEmailLevel.setStatus(_A)
_NbsCmmcSysLogMessageTable_Object=MibTable
nbsCmmcSysLogMessageTable=_NbsCmmcSysLogMessageTable_Object((1,3,6,1,4,1,629,200,11,5))
if mibBuilder.loadTexts:nbsCmmcSysLogMessageTable.setStatus(_A)
_NbsCmmcSysLogMessageEntry_Object=MibTableRow
nbsCmmcSysLogMessageEntry=_NbsCmmcSysLogMessageEntry_Object((1,3,6,1,4,1,629,200,11,5,1))
nbsCmmcSysLogMessageEntry.setIndexNames((0,_B,_Ao))
if mibBuilder.loadTexts:nbsCmmcSysLogMessageEntry.setStatus(_A)
class _NbsCmmcSysLogMessageType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('sysReset',1),('snmp',2),('physTraps',3),('dot1dBridge',4),('sysAuthentic',5)))
_NbsCmmcSysLogMessageType_Type.__name__=_D
_NbsCmmcSysLogMessageType_Object=MibTableColumn
nbsCmmcSysLogMessageType=_NbsCmmcSysLogMessageType_Object((1,3,6,1,4,1,629,200,11,5,1,1),_NbsCmmcSysLogMessageType_Type())
nbsCmmcSysLogMessageType.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysLogMessageType.setStatus(_A)
class _NbsCmmcSysLogMessageSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,10,100,1000,10000)));namedValues=NamedValues(*(('informational',1),('warnings',10),('errors',100),('emergencies',1000),('debugging',10000)))
_NbsCmmcSysLogMessageSeverity_Type.__name__=_D
_NbsCmmcSysLogMessageSeverity_Object=MibTableColumn
nbsCmmcSysLogMessageSeverity=_NbsCmmcSysLogMessageSeverity_Object((1,3,6,1,4,1,629,200,11,5,1,2),_NbsCmmcSysLogMessageSeverity_Type())
nbsCmmcSysLogMessageSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysLogMessageSeverity.setStatus(_A)
_NbsCmmcSysRunningLogMessageTotal_Type=Integer32
_NbsCmmcSysRunningLogMessageTotal_Object=MibScalar
nbsCmmcSysRunningLogMessageTotal=_NbsCmmcSysRunningLogMessageTotal_Object((1,3,6,1,4,1,629,200,11,6),_NbsCmmcSysRunningLogMessageTotal_Type())
nbsCmmcSysRunningLogMessageTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysRunningLogMessageTotal.setStatus(_A)
_NbsCmmcSysRunningLogMessageTable_Object=MibTable
nbsCmmcSysRunningLogMessageTable=_NbsCmmcSysRunningLogMessageTable_Object((1,3,6,1,4,1,629,200,11,7))
if mibBuilder.loadTexts:nbsCmmcSysRunningLogMessageTable.setStatus(_A)
_NbsCmmcSysRunningLogMessageEntry_Object=MibTableRow
nbsCmmcSysRunningLogMessageEntry=_NbsCmmcSysRunningLogMessageEntry_Object((1,3,6,1,4,1,629,200,11,7,1))
nbsCmmcSysRunningLogMessageEntry.setIndexNames((0,_B,_Ap))
if mibBuilder.loadTexts:nbsCmmcSysRunningLogMessageEntry.setStatus(_A)
_NbsCmmcSysRunningLogMessageIndex_Type=Integer32
_NbsCmmcSysRunningLogMessageIndex_Object=MibTableColumn
nbsCmmcSysRunningLogMessageIndex=_NbsCmmcSysRunningLogMessageIndex_Object((1,3,6,1,4,1,629,200,11,7,1,1),_NbsCmmcSysRunningLogMessageIndex_Type())
nbsCmmcSysRunningLogMessageIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysRunningLogMessageIndex.setStatus(_A)
class _NbsCmmcSysRunningLogMessageSeverity_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NbsCmmcSysRunningLogMessageSeverity_Type.__name__=_J
_NbsCmmcSysRunningLogMessageSeverity_Object=MibTableColumn
nbsCmmcSysRunningLogMessageSeverity=_NbsCmmcSysRunningLogMessageSeverity_Object((1,3,6,1,4,1,629,200,11,7,1,2),_NbsCmmcSysRunningLogMessageSeverity_Type())
nbsCmmcSysRunningLogMessageSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysRunningLogMessageSeverity.setStatus(_A)
_NbsCmmcSysRunningLogMessageErrorID_Type=Integer32
_NbsCmmcSysRunningLogMessageErrorID_Object=MibTableColumn
nbsCmmcSysRunningLogMessageErrorID=_NbsCmmcSysRunningLogMessageErrorID_Object((1,3,6,1,4,1,629,200,11,7,1,3),_NbsCmmcSysRunningLogMessageErrorID_Type())
nbsCmmcSysRunningLogMessageErrorID.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysRunningLogMessageErrorID.setStatus(_A)
_NbsCmmcSysRunningLogMessageSession_Type=Integer32
_NbsCmmcSysRunningLogMessageSession_Object=MibTableColumn
nbsCmmcSysRunningLogMessageSession=_NbsCmmcSysRunningLogMessageSession_Object((1,3,6,1,4,1,629,200,11,7,1,4),_NbsCmmcSysRunningLogMessageSession_Type())
nbsCmmcSysRunningLogMessageSession.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysRunningLogMessageSession.setStatus(_A)
_NbsCmmcSysRunningLogMessageTime_Type=Integer32
_NbsCmmcSysRunningLogMessageTime_Object=MibTableColumn
nbsCmmcSysRunningLogMessageTime=_NbsCmmcSysRunningLogMessageTime_Object((1,3,6,1,4,1,629,200,11,7,1,5),_NbsCmmcSysRunningLogMessageTime_Type())
nbsCmmcSysRunningLogMessageTime.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysRunningLogMessageTime.setStatus(_A)
class _NbsCmmcSysRunningLogMessageModule_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NbsCmmcSysRunningLogMessageModule_Type.__name__=_J
_NbsCmmcSysRunningLogMessageModule_Object=MibTableColumn
nbsCmmcSysRunningLogMessageModule=_NbsCmmcSysRunningLogMessageModule_Object((1,3,6,1,4,1,629,200,11,7,1,6),_NbsCmmcSysRunningLogMessageModule_Type())
nbsCmmcSysRunningLogMessageModule.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysRunningLogMessageModule.setStatus(_A)
class _NbsCmmcSysRunningLogMessageString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NbsCmmcSysRunningLogMessageString_Type.__name__=_J
_NbsCmmcSysRunningLogMessageString_Object=MibTableColumn
nbsCmmcSysRunningLogMessageString=_NbsCmmcSysRunningLogMessageString_Object((1,3,6,1,4,1,629,200,11,7,1,7),_NbsCmmcSysRunningLogMessageString_Type())
nbsCmmcSysRunningLogMessageString.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysRunningLogMessageString.setStatus(_A)
_NbsCmmcSysNvramLogMessageTotal_Type=Integer32
_NbsCmmcSysNvramLogMessageTotal_Object=MibScalar
nbsCmmcSysNvramLogMessageTotal=_NbsCmmcSysNvramLogMessageTotal_Object((1,3,6,1,4,1,629,200,11,8),_NbsCmmcSysNvramLogMessageTotal_Type())
nbsCmmcSysNvramLogMessageTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysNvramLogMessageTotal.setStatus(_A)
_NbsCmmcSysNvramLogMessageTable_Object=MibTable
nbsCmmcSysNvramLogMessageTable=_NbsCmmcSysNvramLogMessageTable_Object((1,3,6,1,4,1,629,200,11,9))
if mibBuilder.loadTexts:nbsCmmcSysNvramLogMessageTable.setStatus(_A)
_NbsCmmcSysNvramLogMessageEntry_Object=MibTableRow
nbsCmmcSysNvramLogMessageEntry=_NbsCmmcSysNvramLogMessageEntry_Object((1,3,6,1,4,1,629,200,11,9,1))
nbsCmmcSysNvramLogMessageEntry.setIndexNames((0,_B,_Aq))
if mibBuilder.loadTexts:nbsCmmcSysNvramLogMessageEntry.setStatus(_A)
_NbsCmmcSysNvramLogMessageIndex_Type=Integer32
_NbsCmmcSysNvramLogMessageIndex_Object=MibTableColumn
nbsCmmcSysNvramLogMessageIndex=_NbsCmmcSysNvramLogMessageIndex_Object((1,3,6,1,4,1,629,200,11,9,1,1),_NbsCmmcSysNvramLogMessageIndex_Type())
nbsCmmcSysNvramLogMessageIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysNvramLogMessageIndex.setStatus(_A)
class _NbsCmmcSysNvramLogMessageSeverity_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NbsCmmcSysNvramLogMessageSeverity_Type.__name__=_J
_NbsCmmcSysNvramLogMessageSeverity_Object=MibTableColumn
nbsCmmcSysNvramLogMessageSeverity=_NbsCmmcSysNvramLogMessageSeverity_Object((1,3,6,1,4,1,629,200,11,9,1,2),_NbsCmmcSysNvramLogMessageSeverity_Type())
nbsCmmcSysNvramLogMessageSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysNvramLogMessageSeverity.setStatus(_A)
_NbsCmmcSysNvramLogMessageErrorID_Type=Integer32
_NbsCmmcSysNvramLogMessageErrorID_Object=MibTableColumn
nbsCmmcSysNvramLogMessageErrorID=_NbsCmmcSysNvramLogMessageErrorID_Object((1,3,6,1,4,1,629,200,11,9,1,3),_NbsCmmcSysNvramLogMessageErrorID_Type())
nbsCmmcSysNvramLogMessageErrorID.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysNvramLogMessageErrorID.setStatus(_A)
_NbsCmmcSysNvramLogMessageSession_Type=Integer32
_NbsCmmcSysNvramLogMessageSession_Object=MibTableColumn
nbsCmmcSysNvramLogMessageSession=_NbsCmmcSysNvramLogMessageSession_Object((1,3,6,1,4,1,629,200,11,9,1,4),_NbsCmmcSysNvramLogMessageSession_Type())
nbsCmmcSysNvramLogMessageSession.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysNvramLogMessageSession.setStatus(_A)
_NbsCmmcSysNvramLogMessageTime_Type=Integer32
_NbsCmmcSysNvramLogMessageTime_Object=MibTableColumn
nbsCmmcSysNvramLogMessageTime=_NbsCmmcSysNvramLogMessageTime_Object((1,3,6,1,4,1,629,200,11,9,1,5),_NbsCmmcSysNvramLogMessageTime_Type())
nbsCmmcSysNvramLogMessageTime.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysNvramLogMessageTime.setStatus(_A)
class _NbsCmmcSysNvramLogMessageModule_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NbsCmmcSysNvramLogMessageModule_Type.__name__=_J
_NbsCmmcSysNvramLogMessageModule_Object=MibTableColumn
nbsCmmcSysNvramLogMessageModule=_NbsCmmcSysNvramLogMessageModule_Object((1,3,6,1,4,1,629,200,11,9,1,6),_NbsCmmcSysNvramLogMessageModule_Type())
nbsCmmcSysNvramLogMessageModule.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysNvramLogMessageModule.setStatus(_A)
class _NbsCmmcSysNvramLogMessageString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NbsCmmcSysNvramLogMessageString_Type.__name__=_J
_NbsCmmcSysNvramLogMessageString_Object=MibTableColumn
nbsCmmcSysNvramLogMessageString=_NbsCmmcSysNvramLogMessageString_Object((1,3,6,1,4,1,629,200,11,9,1,7),_NbsCmmcSysNvramLogMessageString_Type())
nbsCmmcSysNvramLogMessageString.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysNvramLogMessageString.setStatus(_A)
_NbsCmmcSysNvramLogMessagePTime_Type=Integer32
_NbsCmmcSysNvramLogMessagePTime_Object=MibTableColumn
nbsCmmcSysNvramLogMessagePTime=_NbsCmmcSysNvramLogMessagePTime_Object((1,3,6,1,4,1,629,200,11,9,1,8),_NbsCmmcSysNvramLogMessagePTime_Type())
nbsCmmcSysNvramLogMessagePTime.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysNvramLogMessagePTime.setStatus(_A)
class _NbsCmmcSysNvramLogMessageDateTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_NbsCmmcSysNvramLogMessageDateTime_Type.__name__=_J
_NbsCmmcSysNvramLogMessageDateTime_Object=MibTableColumn
nbsCmmcSysNvramLogMessageDateTime=_NbsCmmcSysNvramLogMessageDateTime_Object((1,3,6,1,4,1,629,200,11,9,1,9),_NbsCmmcSysNvramLogMessageDateTime_Type())
nbsCmmcSysNvramLogMessageDateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysNvramLogMessageDateTime.setStatus(_A)
_NbsCmmcSysAuditLogTotal_Type=Integer32
_NbsCmmcSysAuditLogTotal_Object=MibScalar
nbsCmmcSysAuditLogTotal=_NbsCmmcSysAuditLogTotal_Object((1,3,6,1,4,1,629,200,11,10),_NbsCmmcSysAuditLogTotal_Type())
nbsCmmcSysAuditLogTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysAuditLogTotal.setStatus(_A)
_NbsCmmcSysAuditLogTable_Object=MibTable
nbsCmmcSysAuditLogTable=_NbsCmmcSysAuditLogTable_Object((1,3,6,1,4,1,629,200,11,11))
if mibBuilder.loadTexts:nbsCmmcSysAuditLogTable.setStatus(_A)
_NbsCmmcSysAuditLogEntry_Object=MibTableRow
nbsCmmcSysAuditLogEntry=_NbsCmmcSysAuditLogEntry_Object((1,3,6,1,4,1,629,200,11,11,1))
nbsCmmcSysAuditLogEntry.setIndexNames((0,_B,_Ar))
if mibBuilder.loadTexts:nbsCmmcSysAuditLogEntry.setStatus(_A)
_NbsCmmcSysAuditLogIndex_Type=Integer32
_NbsCmmcSysAuditLogIndex_Object=MibTableColumn
nbsCmmcSysAuditLogIndex=_NbsCmmcSysAuditLogIndex_Object((1,3,6,1,4,1,629,200,11,11,1,1),_NbsCmmcSysAuditLogIndex_Type())
nbsCmmcSysAuditLogIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysAuditLogIndex.setStatus(_A)
_NbsCmmcSysAuditLogUpTime_Type=Integer32
_NbsCmmcSysAuditLogUpTime_Object=MibTableColumn
nbsCmmcSysAuditLogUpTime=_NbsCmmcSysAuditLogUpTime_Object((1,3,6,1,4,1,629,200,11,11,1,2),_NbsCmmcSysAuditLogUpTime_Type())
nbsCmmcSysAuditLogUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysAuditLogUpTime.setStatus(_A)
class _NbsCmmcSysAuditLogDateTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_NbsCmmcSysAuditLogDateTime_Type.__name__=_J
_NbsCmmcSysAuditLogDateTime_Object=MibTableColumn
nbsCmmcSysAuditLogDateTime=_NbsCmmcSysAuditLogDateTime_Object((1,3,6,1,4,1,629,200,11,11,1,3),_NbsCmmcSysAuditLogDateTime_Type())
nbsCmmcSysAuditLogDateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysAuditLogDateTime.setStatus(_A)
class _NbsCmmcSysAuditLogString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,250))
_NbsCmmcSysAuditLogString_Type.__name__=_J
_NbsCmmcSysAuditLogString_Object=MibTableColumn
nbsCmmcSysAuditLogString=_NbsCmmcSysAuditLogString_Object((1,3,6,1,4,1,629,200,11,11,1,4),_NbsCmmcSysAuditLogString_Type())
nbsCmmcSysAuditLogString.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsCmmcSysAuditLogString.setStatus(_A)
_NbsCmmcSysLogRemoteServer_Type=IpAddress
_NbsCmmcSysLogRemoteServer_Object=MibScalar
nbsCmmcSysLogRemoteServer=_NbsCmmcSysLogRemoteServer_Object((1,3,6,1,4,1,629,200,11,12),_NbsCmmcSysLogRemoteServer_Type())
nbsCmmcSysLogRemoteServer.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysLogRemoteServer.setStatus(_A)
class _NbsCmmcSysLogRemoteLevel_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_P,1),('emerg',2),('alert',3),('crit',4),(_c,5),(_d,6),('notice',7),(_A0,8),('debug',9)))
_NbsCmmcSysLogRemoteLevel_Type.__name__=_D
_NbsCmmcSysLogRemoteLevel_Object=MibScalar
nbsCmmcSysLogRemoteLevel=_NbsCmmcSysLogRemoteLevel_Object((1,3,6,1,4,1,629,200,11,13),_NbsCmmcSysLogRemoteLevel_Type())
nbsCmmcSysLogRemoteLevel.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysLogRemoteLevel.setStatus(_A)
class _NbsCmmcSysRunningLogMessageClear_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_a,2),(_Y,3)))
_NbsCmmcSysRunningLogMessageClear_Type.__name__=_D
_NbsCmmcSysRunningLogMessageClear_Object=MibScalar
nbsCmmcSysRunningLogMessageClear=_NbsCmmcSysRunningLogMessageClear_Object((1,3,6,1,4,1,629,200,11,14),_NbsCmmcSysRunningLogMessageClear_Type())
nbsCmmcSysRunningLogMessageClear.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysRunningLogMessageClear.setStatus(_A)
class _NbsCmmcSysNvramLogMessageClear_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_a,2),(_Y,3)))
_NbsCmmcSysNvramLogMessageClear_Type.__name__=_D
_NbsCmmcSysNvramLogMessageClear_Object=MibScalar
nbsCmmcSysNvramLogMessageClear=_NbsCmmcSysNvramLogMessageClear_Object((1,3,6,1,4,1,629,200,11,15),_NbsCmmcSysNvramLogMessageClear_Type())
nbsCmmcSysNvramLogMessageClear.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysNvramLogMessageClear.setStatus(_A)
class _NbsCmmcSysAuditLogClear_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_a,2),(_Y,3)))
_NbsCmmcSysAuditLogClear_Type.__name__=_D
_NbsCmmcSysAuditLogClear_Object=MibScalar
nbsCmmcSysAuditLogClear=_NbsCmmcSysAuditLogClear_Object((1,3,6,1,4,1,629,200,11,16),_NbsCmmcSysAuditLogClear_Type())
nbsCmmcSysAuditLogClear.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysAuditLogClear.setStatus(_A)
class _NbsCmmcSysLogNvSize_Type(Integer32):defaultValue=64;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,65535))
_NbsCmmcSysLogNvSize_Type.__name__=_D
_NbsCmmcSysLogNvSize_Object=MibScalar
nbsCmmcSysLogNvSize=_NbsCmmcSysLogNvSize_Object((1,3,6,1,4,1,629,200,11,17),_NbsCmmcSysLogNvSize_Type())
nbsCmmcSysLogNvSize.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsCmmcSysLogNvSize.setStatus(_A)
_NbsCmmcTrapGrp_ObjectIdentity=ObjectIdentity
nbsCmmcTrapGrp=_NbsCmmcTrapGrp_ObjectIdentity((1,3,6,1,4,1,629,200,12))
if mibBuilder.loadTexts:nbsCmmcTrapGrp.setStatus(_A)
class _NbsCmmcTrapLastMessage_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NbsCmmcTrapLastMessage_Type.__name__=_J
_NbsCmmcTrapLastMessage_Object=MibScalar
nbsCmmcTrapLastMessage=_NbsCmmcTrapLastMessage_Object((1,3,6,1,4,1,629,200,12,1),_NbsCmmcTrapLastMessage_Type())
nbsCmmcTrapLastMessage.setMaxAccess(_Z)
if mibBuilder.loadTexts:nbsCmmcTrapLastMessage.setStatus(_A)
_NbsCmmcTrapPowerSupplyId_Type=Integer32
_NbsCmmcTrapPowerSupplyId_Object=MibScalar
nbsCmmcTrapPowerSupplyId=_NbsCmmcTrapPowerSupplyId_Object((1,3,6,1,4,1,629,200,12,2),_NbsCmmcTrapPowerSupplyId_Type())
nbsCmmcTrapPowerSupplyId.setMaxAccess(_Z)
if mibBuilder.loadTexts:nbsCmmcTrapPowerSupplyId.setStatus(_A)
_NbsCmmcTrapFanId_Type=Integer32
_NbsCmmcTrapFanId_Object=MibScalar
nbsCmmcTrapFanId=_NbsCmmcTrapFanId_Object((1,3,6,1,4,1,629,200,12,3),_NbsCmmcTrapFanId_Type())
nbsCmmcTrapFanId.setMaxAccess(_Z)
if mibBuilder.loadTexts:nbsCmmcTrapFanId.setStatus(_A)
_NbsCmmcTrapPortIndex_Type=Integer32
_NbsCmmcTrapPortIndex_Object=MibScalar
nbsCmmcTrapPortIndex=_NbsCmmcTrapPortIndex_Object((1,3,6,1,4,1,629,200,12,4),_NbsCmmcTrapPortIndex_Type())
nbsCmmcTrapPortIndex.setMaxAccess(_Z)
if mibBuilder.loadTexts:nbsCmmcTrapPortIndex.setStatus(_A)
class _NbsCmmcTrapPortName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_NbsCmmcTrapPortName_Type.__name__=_J
_NbsCmmcTrapPortName_Object=MibScalar
nbsCmmcTrapPortName=_NbsCmmcTrapPortName_Object((1,3,6,1,4,1,629,200,12,5),_NbsCmmcTrapPortName_Type())
nbsCmmcTrapPortName.setMaxAccess(_Z)
if mibBuilder.loadTexts:nbsCmmcTrapPortName.setStatus(_A)
class _NbsCmmcTrapShutdownReason_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NbsCmmcTrapShutdownReason_Type.__name__=_J
_NbsCmmcTrapShutdownReason_Object=MibScalar
nbsCmmcTrapShutdownReason=_NbsCmmcTrapShutdownReason_Object((1,3,6,1,4,1,629,200,12,6),_NbsCmmcTrapShutdownReason_Type())
nbsCmmcTrapShutdownReason.setMaxAccess(_Z)
if mibBuilder.loadTexts:nbsCmmcTrapShutdownReason.setStatus(_A)
class _NbsCmmcTrapErrorInfo_Type(DisplayString):defaultValue=OctetString('Ethernet.');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NbsCmmcTrapErrorInfo_Type.__name__=_J
_NbsCmmcTrapErrorInfo_Object=MibScalar
nbsCmmcTrapErrorInfo=_NbsCmmcTrapErrorInfo_Object((1,3,6,1,4,1,629,200,12,7),_NbsCmmcTrapErrorInfo_Type())
nbsCmmcTrapErrorInfo.setMaxAccess(_Z)
if mibBuilder.loadTexts:nbsCmmcTrapErrorInfo.setStatus(_A)
class _NbsCmmcSlotModelLocked_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_NbsCmmcSlotModelLocked_Type.__name__=_J
_NbsCmmcSlotModelLocked_Object=MibScalar
nbsCmmcSlotModelLocked=_NbsCmmcSlotModelLocked_Object((1,3,6,1,4,1,629,200,12,10),_NbsCmmcSlotModelLocked_Type())
nbsCmmcSlotModelLocked.setMaxAccess(_Z)
if mibBuilder.loadTexts:nbsCmmcSlotModelLocked.setStatus(_A)
class _NbsCmmcSlotModelInserted_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_NbsCmmcSlotModelInserted_Type.__name__=_J
_NbsCmmcSlotModelInserted_Object=MibScalar
nbsCmmcSlotModelInserted=_NbsCmmcSlotModelInserted_Object((1,3,6,1,4,1,629,200,12,11),_NbsCmmcSlotModelInserted_Type())
nbsCmmcSlotModelInserted.setMaxAccess(_Z)
if mibBuilder.loadTexts:nbsCmmcSlotModelInserted.setStatus(_A)
_NbsCmmcTraps_ObjectIdentity=ObjectIdentity
nbsCmmcTraps=_NbsCmmcTraps_ObjectIdentity((1,3,6,1,4,1,629,200,13))
if mibBuilder.loadTexts:nbsCmmcTraps.setStatus(_A)
_NbsCmmcTraps0_ObjectIdentity=ObjectIdentity
nbsCmmcTraps0=_NbsCmmcTraps0_ObjectIdentity((1,3,6,1,4,1,629,200,13,0))
if mibBuilder.loadTexts:nbsCmmcTraps0.setStatus(_A)
nbsCmmcTrapGenericTrap=NotificationType((1,3,6,1,4,1,629,200,13,0,1))
nbsCmmcTrapGenericTrap.setObjects((_B,_G))
if mibBuilder.loadTexts:nbsCmmcTrapGenericTrap.setStatus(_K)
nbsCmmcTrapSpecificTrap=NotificationType((1,3,6,1,4,1,629,200,13,0,2))
nbsCmmcTrapSpecificTrap.setObjects((_B,_G))
if mibBuilder.loadTexts:nbsCmmcTrapSpecificTrap.setStatus(_K)
nbsCmmcTrapDeviceRebooted=NotificationType((1,3,6,1,4,1,629,200,13,0,3))
nbsCmmcTrapDeviceRebooted.setObjects(*((_B,_G),(_B,_A1)))
if mibBuilder.loadTexts:nbsCmmcTrapDeviceRebooted.setStatus(_A)
nbsCmmcTrapDeviceOnline=NotificationType((1,3,6,1,4,1,629,200,13,0,4))
nbsCmmcTrapDeviceOnline.setObjects(*((_B,_G),(_B,_H),(_B,_L)))
if mibBuilder.loadTexts:nbsCmmcTrapDeviceOnline.setStatus(_A)
nbsCmmcTrapDeviceShuttingDown=NotificationType((1,3,6,1,4,1,629,200,13,0,5))
nbsCmmcTrapDeviceShuttingDown.setObjects(*((_B,_G),(_B,_A1)))
if mibBuilder.loadTexts:nbsCmmcTrapDeviceShuttingDown.setStatus(_A)
nbsCmmcTrapPowerSupplyFailure=NotificationType((1,3,6,1,4,1,629,200,13,0,6))
nbsCmmcTrapPowerSupplyFailure.setObjects(*((_B,_G),(_B,_H),(_B,_m),(_B,_I)))
if mibBuilder.loadTexts:nbsCmmcTrapPowerSupplyFailure.setStatus(_A)
nbsCmmcTrapPowerSupplyRestored=NotificationType((1,3,6,1,4,1,629,200,13,0,7))
nbsCmmcTrapPowerSupplyRestored.setObjects(*((_B,_G),(_B,_H),(_B,_m),(_B,_I)))
if mibBuilder.loadTexts:nbsCmmcTrapPowerSupplyRestored.setStatus(_A)
nbsCmmcTrapFanFailure=NotificationType((1,3,6,1,4,1,629,200,13,0,8))
nbsCmmcTrapFanFailure.setObjects(*((_B,_G),(_B,_H),(_B,_n),(_B,_I)))
if mibBuilder.loadTexts:nbsCmmcTrapFanFailure.setStatus(_A)
nbsCmmcTrapFanRestored=NotificationType((1,3,6,1,4,1,629,200,13,0,9))
nbsCmmcTrapFanRestored.setObjects(*((_B,_G),(_B,_H),(_B,_n),(_B,_I)))
if mibBuilder.loadTexts:nbsCmmcTrapFanRestored.setStatus(_A)
nbsCmmcTrapChassisTempTooHigh=NotificationType((1,3,6,1,4,1,629,200,13,0,10))
nbsCmmcTrapChassisTempTooHigh.setObjects(*((_B,_G),(_B,_H),(_B,_A2),(_B,_As),(_B,_I)))
if mibBuilder.loadTexts:nbsCmmcTrapChassisTempTooHigh.setStatus(_A)
nbsCmmcTrapChassisTempTooLow=NotificationType((1,3,6,1,4,1,629,200,13,0,11))
nbsCmmcTrapChassisTempTooLow.setObjects(*((_B,_G),(_B,_H),(_B,_A2),(_B,_At),(_B,_I)))
if mibBuilder.loadTexts:nbsCmmcTrapChassisTempTooLow.setStatus(_A)
nbsCmmcTrapChassisTempOk=NotificationType((1,3,6,1,4,1,629,200,13,0,12))
nbsCmmcTrapChassisTempOk.setObjects(*((_B,_G),(_B,_H),(_B,_A2),(_B,_I)))
if mibBuilder.loadTexts:nbsCmmcTrapChassisTempOk.setStatus(_A)
nbsCmmcTrapSlotModuleIn=NotificationType((1,3,6,1,4,1,629,200,13,0,13))
nbsCmmcTrapSlotModuleIn.setObjects(*((_B,_G),(_B,_H),(_B,_L),(_B,_AG),(_B,_I),(_B,_M)))
if mibBuilder.loadTexts:nbsCmmcTrapSlotModuleIn.setStatus(_A)
nbsCmmcTrapSlotModuleOut=NotificationType((1,3,6,1,4,1,629,200,13,0,14))
nbsCmmcTrapSlotModuleOut.setObjects(*((_B,_G),(_B,_H),(_B,_L),(_B,_AG),(_B,_I),(_B,_M)))
if mibBuilder.loadTexts:nbsCmmcTrapSlotModuleOut.setStatus(_A)
nbsCmmcTrapPortEnabled=NotificationType((1,3,6,1,4,1,629,200,13,0,15))
nbsCmmcTrapPortEnabled.setObjects(*((_B,_G),(_B,_H),(_B,_L),(_B,_N),(_B,_I),(_B,_M),(_B,_O)))
if mibBuilder.loadTexts:nbsCmmcTrapPortEnabled.setStatus(_A)
nbsCmmcTrapPortDisabled=NotificationType((1,3,6,1,4,1,629,200,13,0,16))
nbsCmmcTrapPortDisabled.setObjects(*((_B,_G),(_B,_H),(_B,_L),(_B,_N),(_B,_I),(_B,_M),(_B,_O)))
if mibBuilder.loadTexts:nbsCmmcTrapPortDisabled.setStatus(_A)
nbsCmmcTrapPortLinkUp=NotificationType((1,3,6,1,4,1,629,200,13,0,17))
nbsCmmcTrapPortLinkUp.setObjects(*((_B,_G),(_B,_H),(_B,_L),(_B,_N),(_B,_Au),(_B,_I),(_B,_M),(_B,_O)))
if mibBuilder.loadTexts:nbsCmmcTrapPortLinkUp.setStatus(_A)
nbsCmmcTrapPortLinkDown=NotificationType((1,3,6,1,4,1,629,200,13,0,18))
nbsCmmcTrapPortLinkDown.setObjects(*((_B,_G),(_B,_H),(_B,_L),(_B,_N),(_B,_I),(_B,_M),(_B,_O)))
if mibBuilder.loadTexts:nbsCmmcTrapPortLinkDown.setStatus(_A)
nbsCmmcTrapPortLINOn=NotificationType((1,3,6,1,4,1,629,200,13,0,19))
nbsCmmcTrapPortLINOn.setObjects(*((_B,_G),(_B,_H),(_B,_L),(_B,_N),(_B,_I),(_B,_M),(_B,_O)))
if mibBuilder.loadTexts:nbsCmmcTrapPortLINOn.setStatus(_A)
nbsCmmcTrapPortLINOff=NotificationType((1,3,6,1,4,1,629,200,13,0,20))
nbsCmmcTrapPortLINOff.setObjects(*((_B,_G),(_B,_H),(_B,_L),(_B,_N),(_B,_I),(_B,_M),(_B,_O)))
if mibBuilder.loadTexts:nbsCmmcTrapPortLINOff.setStatus(_A)
nbsCmmcTrapPortLoopbackOn=NotificationType((1,3,6,1,4,1,629,200,13,0,21))
nbsCmmcTrapPortLoopbackOn.setObjects(*((_B,_G),(_B,_H),(_B,_L),(_B,_N),(_B,_I),(_B,_M),(_B,_O)))
if mibBuilder.loadTexts:nbsCmmcTrapPortLoopbackOn.setStatus(_A)
nbsCmmcTrapPortLoopbackOff=NotificationType((1,3,6,1,4,1,629,200,13,0,22))
nbsCmmcTrapPortLoopbackOff.setObjects(*((_B,_G),(_B,_H),(_B,_L),(_B,_N),(_B,_I),(_B,_M),(_B,_O)))
if mibBuilder.loadTexts:nbsCmmcTrapPortLoopbackOff.setStatus(_A)
nbsCmmcTrapPortMaximumExceeded=NotificationType((1,3,6,1,4,1,629,200,13,0,23))
nbsCmmcTrapPortMaximumExceeded.setObjects(*((_B,_G),(_B,_H),(_B,_L),(_B,_N),(_B,_X),(_B,_Av),(_B,_I),(_B,_M),(_B,_O)))
if mibBuilder.loadTexts:nbsCmmcTrapPortMaximumExceeded.setStatus(_A)
nbsCmmcTrapPortRemoved=NotificationType((1,3,6,1,4,1,629,200,13,0,24))
nbsCmmcTrapPortRemoved.setObjects(*((_B,_G),(_B,_H),(_B,_L),(_B,_N),(_B,_I),(_B,_M),(_B,_O)))
if mibBuilder.loadTexts:nbsCmmcTrapPortRemoved.setStatus(_A)
nbsCmmcTrapPortInserted=NotificationType((1,3,6,1,4,1,629,200,13,0,25))
nbsCmmcTrapPortInserted.setObjects(*((_B,_G),(_B,_H),(_B,_L),(_B,_N),(_B,_Aw),(_B,_Ax),(_B,_I),(_B,_M),(_B,_O)))
if mibBuilder.loadTexts:nbsCmmcTrapPortInserted.setStatus(_A)
nbsCmmcTrapPortTempTooLow=NotificationType((1,3,6,1,4,1,629,200,13,0,26))
nbsCmmcTrapPortTempTooLow.setObjects(*((_B,_G),(_B,_H),(_B,_L),(_B,_N),(_B,_A3),(_B,_I),(_B,_M),(_B,_O),(_B,_X),(_B,_AH)))
if mibBuilder.loadTexts:nbsCmmcTrapPortTempTooLow.setStatus(_A)
nbsCmmcTrapPortTempTooHigh=NotificationType((1,3,6,1,4,1,629,200,13,0,27))
nbsCmmcTrapPortTempTooHigh.setObjects(*((_B,_G),(_B,_H),(_B,_L),(_B,_N),(_B,_A3),(_B,_I),(_B,_M),(_B,_O),(_B,_X),(_B,_AH)))
if mibBuilder.loadTexts:nbsCmmcTrapPortTempTooHigh.setStatus(_A)
nbsCmmcTrapPortRxPowerTooLow=NotificationType((1,3,6,1,4,1,629,200,13,0,28))
nbsCmmcTrapPortRxPowerTooLow.setObjects(*((_B,_G),(_B,_H),(_B,_L),(_B,_N),(_B,_A4),(_B,_I),(_B,_M),(_B,_O),(_B,_X),(_B,_AI)))
if mibBuilder.loadTexts:nbsCmmcTrapPortRxPowerTooLow.setStatus(_A)
nbsCmmcTrapPortRxPowerTooHigh=NotificationType((1,3,6,1,4,1,629,200,13,0,29))
nbsCmmcTrapPortRxPowerTooHigh.setObjects(*((_B,_G),(_B,_H),(_B,_L),(_B,_N),(_B,_A4),(_B,_I),(_B,_M),(_B,_O),(_B,_X),(_B,_AI)))
if mibBuilder.loadTexts:nbsCmmcTrapPortRxPowerTooHigh.setStatus(_A)
nbsCmmcTrapPortTxPowerTooLow=NotificationType((1,3,6,1,4,1,629,200,13,0,30))
nbsCmmcTrapPortTxPowerTooLow.setObjects(*((_B,_G),(_B,_H),(_B,_L),(_B,_N),(_B,_A5),(_B,_I),(_B,_M),(_B,_O),(_B,_X),(_B,_AJ)))
if mibBuilder.loadTexts:nbsCmmcTrapPortTxPowerTooLow.setStatus(_A)
nbsCmmcTrapPortTxPowerTooHigh=NotificationType((1,3,6,1,4,1,629,200,13,0,31))
nbsCmmcTrapPortTxPowerTooHigh.setObjects(*((_B,_G),(_B,_H),(_B,_L),(_B,_N),(_B,_A5),(_B,_I),(_B,_M),(_B,_O),(_B,_X),(_B,_AJ)))
if mibBuilder.loadTexts:nbsCmmcTrapPortTxPowerTooHigh.setStatus(_A)
nbsCmmcTrapPortAmpsTooLow=NotificationType((1,3,6,1,4,1,629,200,13,0,32))
nbsCmmcTrapPortAmpsTooLow.setObjects(*((_B,_G),(_B,_H),(_B,_L),(_B,_N),(_B,_A6),(_B,_I),(_B,_M),(_B,_O),(_B,_X),(_B,_AK)))
if mibBuilder.loadTexts:nbsCmmcTrapPortAmpsTooLow.setStatus(_A)
nbsCmmcTrapPortAmpsTooHigh=NotificationType((1,3,6,1,4,1,629,200,13,0,33))
nbsCmmcTrapPortAmpsTooHigh.setObjects(*((_B,_G),(_B,_H),(_B,_L),(_B,_N),(_B,_A6),(_B,_I),(_B,_M),(_B,_O),(_B,_X),(_B,_AK)))
if mibBuilder.loadTexts:nbsCmmcTrapPortAmpsTooHigh.setStatus(_A)
nbsCmmcTrapPortVoltsTooLow=NotificationType((1,3,6,1,4,1,629,200,13,0,34))
nbsCmmcTrapPortVoltsTooLow.setObjects(*((_B,_G),(_B,_H),(_B,_L),(_B,_N),(_B,_A7),(_B,_I),(_B,_M),(_B,_O),(_B,_X),(_B,_AL)))
if mibBuilder.loadTexts:nbsCmmcTrapPortVoltsTooLow.setStatus(_A)
nbsCmmcTrapPortVoltsTooHigh=NotificationType((1,3,6,1,4,1,629,200,13,0,35))
nbsCmmcTrapPortVoltsTooHigh.setObjects(*((_B,_G),(_B,_H),(_B,_L),(_B,_N),(_B,_A7),(_B,_I),(_B,_M),(_B,_O),(_B,_X),(_B,_AL)))
if mibBuilder.loadTexts:nbsCmmcTrapPortVoltsTooHigh.setStatus(_A)
nbsCmmcTrapSwitchover=NotificationType((1,3,6,1,4,1,629,200,13,0,36))
nbsCmmcTrapSwitchover.setObjects(*((_B,_G),(_B,_H),(_B,_L),(_B,_N),(_B,_Ay),(_B,_I),(_B,_M),(_B,_O),(_B,_Az)))
if mibBuilder.loadTexts:nbsCmmcTrapSwitchover.setStatus(_A)
nbsCmmcTrapSlotShuttingDown=NotificationType((1,3,6,1,4,1,629,200,13,0,37))
nbsCmmcTrapSlotShuttingDown.setObjects(*((_B,_G),(_B,_H),(_B,_L),(_B,_A1),(_B,_I),(_B,_M)))
if mibBuilder.loadTexts:nbsCmmcTrapSlotShuttingDown.setStatus(_A)
nbsCmmcTrapPortCrcError=NotificationType((1,3,6,1,4,1,629,200,13,0,38))
nbsCmmcTrapPortCrcError.setObjects(*((_B,_G),(_B,_H),(_B,_L),(_B,_N),(_B,_I),(_B,_M),(_B,_O)))
if mibBuilder.loadTexts:nbsCmmcTrapPortCrcError.setStatus(_A)
nbsCmmcTrapCpeInManagedChassis=NotificationType((1,3,6,1,4,1,629,200,13,0,39))
nbsCmmcTrapCpeInManagedChassis.setObjects(*((_B,_G),(_B,_H),(_B,_L),(_B,_I),(_B,_M)))
if mibBuilder.loadTexts:nbsCmmcTrapCpeInManagedChassis.setStatus(_A)
nbsCmmcTrapCoWithoutCpe=NotificationType((1,3,6,1,4,1,629,200,13,0,40))
nbsCmmcTrapCoWithoutCpe.setObjects(*((_B,_G),(_B,_H),(_B,_L),(_B,_I),(_B,_M)))
if mibBuilder.loadTexts:nbsCmmcTrapCoWithoutCpe.setStatus(_A)
nbsCmmcTrapCoTakesControl=NotificationType((1,3,6,1,4,1,629,200,13,0,41))
nbsCmmcTrapCoTakesControl.setObjects(*((_B,_G),(_B,_H),(_B,_L),(_B,_I),(_B,_M)))
if mibBuilder.loadTexts:nbsCmmcTrapCoTakesControl.setStatus(_A)
nbsCmmcTrapCoYieldsControl=NotificationType((1,3,6,1,4,1,629,200,13,0,42))
nbsCmmcTrapCoYieldsControl.setObjects(*((_B,_G),(_B,_H),(_B,_L),(_B,_I),(_B,_M)))
if mibBuilder.loadTexts:nbsCmmcTrapCoYieldsControl.setStatus(_A)
nbsCmmcTrapCoLinkedToCo=NotificationType((1,3,6,1,4,1,629,200,13,0,43))
nbsCmmcTrapCoLinkedToCo.setObjects(*((_B,_G),(_B,_H),(_B,_L),(_B,_I),(_B,_M)))
if mibBuilder.loadTexts:nbsCmmcTrapCoLinkedToCo.setStatus(_A)
nbsCmmcTrapCpeFound=NotificationType((1,3,6,1,4,1,629,200,13,0,44))
nbsCmmcTrapCpeFound.setObjects(*((_B,_G),(_B,_H),(_B,_L),(_B,_I),(_B,_M)))
if mibBuilder.loadTexts:nbsCmmcTrapCpeFound.setStatus(_A)
nbsCmmcTrapPortReflectionDetected=NotificationType((1,3,6,1,4,1,629,200,13,0,45))
nbsCmmcTrapPortReflectionDetected.setObjects(*((_B,_G),(_B,_H),(_B,_L),(_B,_N),(_B,_I),(_B,_M),(_B,_O)))
if mibBuilder.loadTexts:nbsCmmcTrapPortReflectionDetected.setStatus(_A)
nbsCmmcTrapPortReflectionCeased=NotificationType((1,3,6,1,4,1,629,200,13,0,46))
nbsCmmcTrapPortReflectionCeased.setObjects(*((_B,_G),(_B,_H),(_B,_L),(_B,_N),(_B,_I),(_B,_M),(_B,_O)))
if mibBuilder.loadTexts:nbsCmmcTrapPortReflectionCeased.setStatus(_A)
nbsCmmcTrapPortTempOk=NotificationType((1,3,6,1,4,1,629,200,13,0,47))
nbsCmmcTrapPortTempOk.setObjects(*((_B,_G),(_B,_H),(_B,_L),(_B,_N),(_B,_A3),(_B,_I),(_B,_M),(_B,_O)))
if mibBuilder.loadTexts:nbsCmmcTrapPortTempOk.setStatus(_A)
nbsCmmcTrapPortRxPowerOk=NotificationType((1,3,6,1,4,1,629,200,13,0,48))
nbsCmmcTrapPortRxPowerOk.setObjects(*((_B,_G),(_B,_H),(_B,_L),(_B,_N),(_B,_A4),(_B,_I),(_B,_M),(_B,_O)))
if mibBuilder.loadTexts:nbsCmmcTrapPortRxPowerOk.setStatus(_A)
nbsCmmcTrapPortTxPowerOk=NotificationType((1,3,6,1,4,1,629,200,13,0,49))
nbsCmmcTrapPortTxPowerOk.setObjects(*((_B,_G),(_B,_H),(_B,_L),(_B,_N),(_B,_A5),(_B,_I),(_B,_M),(_B,_O)))
if mibBuilder.loadTexts:nbsCmmcTrapPortTxPowerOk.setStatus(_A)
nbsCmmcTrapPortAmpsOk=NotificationType((1,3,6,1,4,1,629,200,13,0,50))
nbsCmmcTrapPortAmpsOk.setObjects(*((_B,_G),(_B,_H),(_B,_L),(_B,_N),(_B,_A6),(_B,_I),(_B,_M),(_B,_O)))
if mibBuilder.loadTexts:nbsCmmcTrapPortAmpsOk.setStatus(_A)
nbsCmmcTrapPortVoltsOk=NotificationType((1,3,6,1,4,1,629,200,13,0,51))
nbsCmmcTrapPortVoltsOk.setObjects(*((_B,_G),(_B,_H),(_B,_L),(_B,_N),(_B,_A7),(_B,_I),(_B,_M),(_B,_O)))
if mibBuilder.loadTexts:nbsCmmcTrapPortVoltsOk.setStatus(_A)
nbsCmmcTrapSlotTempTooLow=NotificationType((1,3,6,1,4,1,629,200,13,0,52))
nbsCmmcTrapSlotTempTooLow.setObjects(*((_B,_G),(_B,_H),(_B,_L),(_B,_A8),(_B,_A_),(_B,_I),(_B,_M)))
if mibBuilder.loadTexts:nbsCmmcTrapSlotTempTooLow.setStatus(_A)
nbsCmmcTrapSlotTempTooHigh=NotificationType((1,3,6,1,4,1,629,200,13,0,53))
nbsCmmcTrapSlotTempTooHigh.setObjects(*((_B,_G),(_B,_H),(_B,_L),(_B,_A8),(_B,_B0),(_B,_I),(_B,_M)))
if mibBuilder.loadTexts:nbsCmmcTrapSlotTempTooHigh.setStatus(_A)
nbsCmmcTrapSlotTempOk=NotificationType((1,3,6,1,4,1,629,200,13,0,54))
nbsCmmcTrapSlotTempOk.setObjects(*((_B,_G),(_B,_H),(_B,_L),(_B,_A8),(_B,_I),(_B,_M)))
if mibBuilder.loadTexts:nbsCmmcTrapSlotTempOk.setStatus(_A)
nbsCmmcTrapPortErrorsDetected=NotificationType((1,3,6,1,4,1,629,200,13,0,55))
nbsCmmcTrapPortErrorsDetected.setObjects(*((_B,_G),(_B,_H),(_B,_L),(_B,_N),(_B,_B1),(_B,_I),(_B,_M),(_B,_O)))
if mibBuilder.loadTexts:nbsCmmcTrapPortErrorsDetected.setStatus(_A)
nbsCmmcTrapPortErrorsStopped=NotificationType((1,3,6,1,4,1,629,200,13,0,56))
nbsCmmcTrapPortErrorsStopped.setObjects(*((_B,_G),(_B,_H),(_B,_L),(_B,_N),(_B,_I),(_B,_M),(_B,_O)))
if mibBuilder.loadTexts:nbsCmmcTrapPortErrorsStopped.setStatus(_A)
nbsCmmcTrapChassisInsufficientPower=NotificationType((1,3,6,1,4,1,629,200,13,0,57))
nbsCmmcTrapChassisInsufficientPower.setObjects(*((_B,_G),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:nbsCmmcTrapChassisInsufficientPower.setStatus(_A)
nbsCmmcTrapChassisSufficientPower=NotificationType((1,3,6,1,4,1,629,200,13,0,58))
nbsCmmcTrapChassisSufficientPower.setObjects(*((_B,_G),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:nbsCmmcTrapChassisSufficientPower.setStatus(_A)
nbsCmmcTrapSlotModuleLocked=NotificationType((1,3,6,1,4,1,629,200,13,0,59))
nbsCmmcTrapSlotModuleLocked.setObjects(*((_B,_G),(_B,_H),(_B,_L),(_B,_I),(_B,_M),(_B,_B2),(_B,_B3)))
if mibBuilder.loadTexts:nbsCmmcTrapSlotModuleLocked.setStatus(_A)
nbsCmmcTrapSelectLinkChanged=NotificationType((1,3,6,1,4,1,629,200,13,0,60))
nbsCmmcTrapSelectLinkChanged.setObjects(*((_B,_G),(_B,_H),(_B,_L),(_B,_N),(_B,_I),(_B,_M),(_B,_O),(_B,_B4)))
if mibBuilder.loadTexts:nbsCmmcTrapSelectLinkChanged.setStatus(_A)
nbsCmmcTrapPowerSupplyRemoved=NotificationType((1,3,6,1,4,1,629,200,13,0,66))
nbsCmmcTrapPowerSupplyRemoved.setObjects(*((_B,_G),(_B,_H),(_B,_m),(_B,_I)))
if mibBuilder.loadTexts:nbsCmmcTrapPowerSupplyRemoved.setStatus(_A)
nbsCmmcTrapPowerSupplyInserted=NotificationType((1,3,6,1,4,1,629,200,13,0,67))
nbsCmmcTrapPowerSupplyInserted.setObjects(*((_B,_G),(_B,_H),(_B,_m),(_B,_I)))
if mibBuilder.loadTexts:nbsCmmcTrapPowerSupplyInserted.setStatus(_A)
nbsCmmcTrapFanRemoved=NotificationType((1,3,6,1,4,1,629,200,13,0,68))
nbsCmmcTrapFanRemoved.setObjects(*((_B,_G),(_B,_H),(_B,_n),(_B,_I)))
if mibBuilder.loadTexts:nbsCmmcTrapFanRemoved.setStatus(_A)
nbsCmmcTrapFanInserted=NotificationType((1,3,6,1,4,1,629,200,13,0,69))
nbsCmmcTrapFanInserted.setObjects(*((_B,_G),(_B,_H),(_B,_n),(_B,_I)))
if mibBuilder.loadTexts:nbsCmmcTrapFanInserted.setStatus(_A)
nbsCmmcTrapModuleStatusChanged=NotificationType((1,3,6,1,4,1,629,200,13,0,70))
nbsCmmcTrapModuleStatusChanged.setObjects(*((_B,_G),(_B,_H),(_B,_L),(_B,_M),(_B,_B5)))
if mibBuilder.loadTexts:nbsCmmcTrapModuleStatusChanged.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'nbsCmmcMib':nbsCmmcMib,'nbsCmmcObjects':nbsCmmcObjects,'nbsCmmcSystemGrp':nbsCmmcSystemGrp,'nbsCmmcSysFwDescr':nbsCmmcSysFwDescr,'nbsCmmcSysFwVers':nbsCmmcSysFwVers,'nbsCmmcSysRestart':nbsCmmcSysRestart,'nbsCmmcSysNumRestarts':nbsCmmcSysNumRestarts,'nbsCmmcSysErrUptime':nbsCmmcSysErrUptime,'nbsCmmcSysSetNvramDefaults':nbsCmmcSysSetNvramDefaults,'nbsCmmcSysSelftestLevel':nbsCmmcSysSelftestLevel,'nbsCmmcSysCurrentTime':nbsCmmcSysCurrentTime,'nbsCmmcSysCurrentDateTime':nbsCmmcSysCurrentDateTime,'nbsCmmcSysNvramTable':nbsCmmcSysNvramTable,'nbsCmmcSysNvramEntry':nbsCmmcSysNvramEntry,_AO:nbsCmmcSysNvramIndex,'nbsCmmcSysNvramBlock':nbsCmmcSysNvramBlock,'nbsCmmcSysWriteConfig':nbsCmmcSysWriteConfig,'nbsCmmcSysUpgrade':nbsCmmcSysUpgrade,'nbsCmmcSysLoginIdleTimeout':nbsCmmcSysLoginIdleTimeout,'nbsCmmcSysDiscoveryAdmin':nbsCmmcSysDiscoveryAdmin,'nbsCmmcSysDiscoveryHostTable':nbsCmmcSysDiscoveryHostTable,'nbsCmmcSysDiscoveryHostEntry':nbsCmmcSysDiscoveryHostEntry,_AP:nbsCmmcSysDiscoveryHostMACAddress,'nbsCmmcSysDiscoveryHostDistance':nbsCmmcSysDiscoveryHostDistance,'nbsCmmcSysDiscoveryHostIPAddress':nbsCmmcSysDiscoveryHostIPAddress,'nbsCmmcSysDiscoveryHostAddressType':nbsCmmcSysDiscoveryHostAddressType,'nbsCmmcSysDiscoveryHostAddress':nbsCmmcSysDiscoveryHostAddress,'nbsCmmcSysDiscoveryHostSourceIfIndex':nbsCmmcSysDiscoveryHostSourceIfIndex,'nbsCmmcSysLastSetFailure':nbsCmmcSysLastSetFailure,'nbsCmmcSysTimeProtocol':nbsCmmcSysTimeProtocol,'nbsCmmcSysTimeServer':nbsCmmcSysTimeServer,'nbsCmmcSysFirmwareTable':nbsCmmcSysFirmwareTable,'nbsCmmcSysFirmwareEntry':nbsCmmcSysFirmwareEntry,_AQ:nbsCmmcSysFirmwareIndex,'nbsCmmcSysFirmwareDescr':nbsCmmcSysFirmwareDescr,'nbsCmmcSysFirmwareFilename':nbsCmmcSysFirmwareFilename,'nbsCmmcSysFirmwareSize':nbsCmmcSysFirmwareSize,'nbsCmmcSysFirmwareMTime':nbsCmmcSysFirmwareMTime,'nbsCmmcSysFirmwareVersion':nbsCmmcSysFirmwareVersion,'nbsCmmcSysFirmwareDate':nbsCmmcSysFirmwareDate,'nbsCmmcSysFirmwareType':nbsCmmcSysFirmwareType,'nbsCmmcSysFirmwareIDCs':nbsCmmcSysFirmwareIDCs,'nbsCmmcSysFirmwareCksum':nbsCmmcSysFirmwareCksum,'nbsCmmcSysFirmwareMd5':nbsCmmcSysFirmwareMd5,'nbsCmmcSysTimeZone':nbsCmmcSysTimeZone,'nbsCmmcSysSnmpV1':nbsCmmcSysSnmpV1,'nbsCmmcSysSnmpV2c':nbsCmmcSysSnmpV2c,'nbsCmmcSysSnmpV3':nbsCmmcSysSnmpV3,'nbsCmmcSysStpAdmin':nbsCmmcSysStpAdmin,'nbsCmmcSysLockTypes':nbsCmmcSysLockTypes,'nbsCmmcSysSerialTerminalType':nbsCmmcSysSerialTerminalType,'nbsCmmcSysCrossConnect':nbsCmmcSysCrossConnect,'nbsCmmcSysCountersState':nbsCmmcSysCountersState,'nbsCmmcSysSerialBaudRateAdmin':nbsCmmcSysSerialBaudRateAdmin,'nbsCmmcSysSerialBaudRateOper':nbsCmmcSysSerialBaudRateOper,'nbsCmmcSysTimeServAddressType':nbsCmmcSysTimeServAddressType,'nbsCmmcSysTimeServAddress':nbsCmmcSysTimeServAddress,'nbsCmmcSysDiscoveryOper':nbsCmmcSysDiscoveryOper,'nbsCmmcSysStpOper':nbsCmmcSysStpOper,'nbsCmmcSysProtoTableSize':nbsCmmcSysProtoTableSize,'nbsCmmcSysProtoTable':nbsCmmcSysProtoTable,'nbsCmmcSysProtoEntry':nbsCmmcSysProtoEntry,_AR:nbsCmmcSysProtoIndex,'nbsCmmcSysProtoFamily':nbsCmmcSysProtoFamily,'nbsCmmcSysProtoRate':nbsCmmcSysProtoRate,'nbsCmmcSysTimeZoneTableSize':nbsCmmcSysTimeZoneTableSize,'nbsCmmcSysTimeZoneTable':nbsCmmcSysTimeZoneTable,'nbsCmmcSysTimeZoneEntry':nbsCmmcSysTimeZoneEntry,_AS:nbsCmmcSysTimeZoneIndex,'nbsCmmcSysTimeZoneName':nbsCmmcSysTimeZoneName,'nbsCmmcSysLoaderTableSize':nbsCmmcSysLoaderTableSize,'nbsCmmcSysLoaderTable':nbsCmmcSysLoaderTable,'nbsCmmcSysLoaderEntry':nbsCmmcSysLoaderEntry,_AT:nbsCmmcSysLoaderIndex,'nbsCmmcSysLoaderFileId':nbsCmmcSysLoaderFileId,'nbsCmmcSysLoaderProgress':nbsCmmcSysLoaderProgress,'nbsCmmcSysLoaderStatus':nbsCmmcSysLoaderStatus,'nbsCmmcSysLoaderAbort':nbsCmmcSysLoaderAbort,'nbsCmmcSysLoaderAck':nbsCmmcSysLoaderAck,'nbsCmmcSysLoaderFilename':nbsCmmcSysLoaderFilename,'nbsCmmcSysFirmwareURL':nbsCmmcSysFirmwareURL,'nbsCmmcSysFirmwareURLStatus':nbsCmmcSysFirmwareURLStatus,'nbsCmmcSysNVAreaTableSize':nbsCmmcSysNVAreaTableSize,'nbsCmmcSysNVAreaTable':nbsCmmcSysNVAreaTable,'nbsCmmcSysNVAreaEntry':nbsCmmcSysNVAreaEntry,_AW:nbsCmmcSysNVAreaIfIndex,_AX:nbsCmmcSysNVAreaBank,'nbsCmmcSysNVAreaStatus':nbsCmmcSysNVAreaStatus,'nbsCmmcSysNVAreaDescr':nbsCmmcSysNVAreaDescr,'nbsCmmcSysNVAreaVersion':nbsCmmcSysNVAreaVersion,'nbsCmmcSysNVAreaCksum':nbsCmmcSysNVAreaCksum,'nbsCmmcIpSnmpGrp':nbsCmmcIpSnmpGrp,'nbsCmmcIpCfg':nbsCmmcIpCfg,'nbsCmmcPrvIpAddr':nbsCmmcPrvIpAddr,'nbsCmmcPrvNetMask':nbsCmmcPrvNetMask,'nbsCmmcPrvBcastAddr':nbsCmmcPrvBcastAddr,'nbsCmmcSysIpAddr':nbsCmmcSysIpAddr,'nbsCmmcSysNetMask':nbsCmmcSysNetMask,'nbsCmmcSysBcastAddr':nbsCmmcSysBcastAddr,'nbsCmmcSysObIpAddr':nbsCmmcSysObIpAddr,'nbsCmmcSysObNetMask':nbsCmmcSysObNetMask,'nbsCmmcSysObBcastAddr':nbsCmmcSysObBcastAddr,'nbsCmmcSysDefaultGateway':nbsCmmcSysDefaultGateway,'nbsCmmcSysAdminBootpState':nbsCmmcSysAdminBootpState,'nbsCmmcSysRunBootpState':nbsCmmcSysRunBootpState,'nbsCmmcSysSerialLineMode':nbsCmmcSysSerialLineMode,'nbsCmmcSysSerialSlipBaudRate':nbsCmmcSysSerialSlipBaudRate,'nbsCmmcSysArpAgingTime':nbsCmmcSysArpAgingTime,'nbsCmmcSysMaxTelnetSessions':nbsCmmcSysMaxTelnetSessions,'nbsCmmcSysTelnetTable':nbsCmmcSysTelnetTable,'nbsCmmcSysTelnetEntry':nbsCmmcSysTelnetEntry,_AY:nbsCmmcSysTelnetSessionIndex,'nbsCmmcSysTelnetSessionStat':nbsCmmcSysTelnetSessionStat,'nbsCmmcSysTelnetHost':nbsCmmcSysTelnetHost,'nbsCmmcSysTelnetHostPort':nbsCmmcSysTelnetHostPort,'nbsCmmcSysTelnetLocal':nbsCmmcSysTelnetLocal,'nbsCmmcSysTelnetLocalPort':nbsCmmcSysTelnetLocalPort,'nbsCmmcSysTelnetSessionId':nbsCmmcSysTelnetSessionId,'nbsCmmcSysTelnetConnectTime':nbsCmmcSysTelnetConnectTime,'nbsCmmcSysTelnetHostAddressType':nbsCmmcSysTelnetHostAddressType,'nbsCmmcSysTelnetHostAddress':nbsCmmcSysTelnetHostAddress,'nbsCmmcSysTelnetLocalAddressType':nbsCmmcSysTelnetLocalAddressType,'nbsCmmcSysTelnetLocalAddress':nbsCmmcSysTelnetLocalAddress,'nbsCmmcSysMaxPingSessions':nbsCmmcSysMaxPingSessions,'nbsCmmcSysPingTable':nbsCmmcSysPingTable,'nbsCmmcSysPingEntry':nbsCmmcSysPingEntry,_AZ:nbsCmmcSysPingSessionIndex,'nbsCmmcSysPingSessionStat':nbsCmmcSysPingSessionStat,'nbsCmmcSysPingAddr':nbsCmmcSysPingAddr,'nbsCmmcSysPingNumber':nbsCmmcSysPingNumber,'nbsCmmcSysPingOwner':nbsCmmcSysPingOwner,'nbsCmmcSysPingRequests':nbsCmmcSysPingRequests,'nbsCmmcSysPingResponses':nbsCmmcSysPingResponses,'nbsCmmcSysPingAddressType':nbsCmmcSysPingAddressType,'nbsCmmcSysPingAddress':nbsCmmcSysPingAddress,'nbsCmmcSysTelnetServer':nbsCmmcSysTelnetServer,'nbsCmmcSysSshServer':nbsCmmcSysSshServer,'nbsCmmcSysIpAddrOper':nbsCmmcSysIpAddrOper,'nbsCmmcSysNetMaskOper':nbsCmmcSysNetMaskOper,'nbsCmmcSysBcastAddrOper':nbsCmmcSysBcastAddrOper,'nbsCmmcSysDefaultGatewayOper':nbsCmmcSysDefaultGatewayOper,'nbsCmmcSysWebServer':nbsCmmcSysWebServer,'nbsCmmcSysWebPort':nbsCmmcSysWebPort,'nbsCmmcSysTelnetPort':nbsCmmcSysTelnetPort,'nbsCmmcSysSshPort':nbsCmmcSysSshPort,'nbsCmmcSysScpServer':nbsCmmcSysScpServer,'nbsCmmcSnmpCfg':nbsCmmcSnmpCfg,'nbsCmmcSysWriteCommunity':nbsCmmcSysWriteCommunity,'nbsCmmcSysReadCommunity':nbsCmmcSysReadCommunity,'nbsCmmcSysTrapTblMaxSize':nbsCmmcSysTrapTblMaxSize,'nbsCmmcSysTrapTable':nbsCmmcSysTrapTable,'nbsCmmcSysTrapEntry':nbsCmmcSysTrapEntry,_Aa:nbsCmmcSysTrapTblEntIndex,'nbsCmmcSysTrapTblEntStatus':nbsCmmcSysTrapTblEntStatus,'nbsCmmcSysTrapTblEntIpAddr':nbsCmmcSysTrapTblEntIpAddr,'nbsCmmcSysTrapTblEntComm':nbsCmmcSysTrapTblEntComm,'nbsCmmcSysTrapTblEntLevel':nbsCmmcSysTrapTblEntLevel,'nbsCmmcSysTrapTblEntPort':nbsCmmcSysTrapTblEntPort,'nbsCmmcSysTrapTblEntAddressType':nbsCmmcSysTrapTblEntAddressType,'nbsCmmcSysTrapTblEntRecipient':nbsCmmcSysTrapTblEntRecipient,'nbsCmmcSysEnablePowerSupplyTraps':nbsCmmcSysEnablePowerSupplyTraps,'nbsCmmcSysEnableModuleTraps':nbsCmmcSysEnableModuleTraps,'nbsCmmcSysEnableBridgeTraps':nbsCmmcSysEnableBridgeTraps,'nbsCmmcSysEnableIpAccessTraps':nbsCmmcSysEnableIpAccessTraps,'nbsCmmcSysSnmpPortAdmin':nbsCmmcSysSnmpPortAdmin,'nbsCmmcSysSnmpPortOper':nbsCmmcSysSnmpPortOper,'nbsCmmcTftpGrp':nbsCmmcTftpGrp,'nbsCmmcSysTftpHostIP':nbsCmmcSysTftpHostIP,'nbsCmmcTftpMaxSessionNum':nbsCmmcTftpMaxSessionNum,'nbsCmmcTftpSessTable':nbsCmmcTftpSessTable,'nbsCmmcTftpSessEntry':nbsCmmcTftpSessEntry,_Ac:nbsCmmcTftpSessIndex,'nbsCmmcTftpSessStatus':nbsCmmcTftpSessStatus,'nbsCmmcTftpSessHostIp':nbsCmmcTftpSessHostIp,'nbsCmmcTftpSessModuleId':nbsCmmcTftpSessModuleId,'nbsCmmcTftpSessAction':nbsCmmcTftpSessAction,'nbsCmmcTftpSessFileName':nbsCmmcTftpSessFileName,'nbsCmmcTftpSessFileSize':nbsCmmcTftpSessFileSize,'nbsCmmcTftpSessProgress':nbsCmmcTftpSessProgress,'nbsCmmcTftpSessAddressType':nbsCmmcTftpSessAddressType,'nbsCmmcTftpSessAddress':nbsCmmcTftpSessAddress,'nbsCmmcSysTftpHostAddressType':nbsCmmcSysTftpHostAddressType,'nbsCmmcSysTftpHostAddress':nbsCmmcSysTftpHostAddress,'nbsCmmcChassisGrp':nbsCmmcChassisGrp,'nbsCmmcChassisTable':nbsCmmcChassisTable,'nbsCmmcChassisEntry':nbsCmmcChassisEntry,_H:nbsCmmcChassisIndex,'nbsCmmcChassisType':nbsCmmcChassisType,'nbsCmmcChassisModel':nbsCmmcChassisModel,'nbsCmmcChassisObjectId':nbsCmmcChassisObjectId,'nbsCmmcChassisNumberOfSlots':nbsCmmcChassisNumberOfSlots,'nbsCmmcChassisHardwareRevision':nbsCmmcChassisHardwareRevision,'nbsCmmcChassisPS1Status':nbsCmmcChassisPS1Status,'nbsCmmcChassisPS2Status':nbsCmmcChassisPS2Status,'nbsCmmcChassisPS3Status':nbsCmmcChassisPS3Status,'nbsCmmcChassisPS4Status':nbsCmmcChassisPS4Status,'nbsCmmcChassisFan1Status':nbsCmmcChassisFan1Status,'nbsCmmcChassisFan2Status':nbsCmmcChassisFan2Status,'nbsCmmcChassisFan3Status':nbsCmmcChassisFan3Status,'nbsCmmcChassisFan4Status':nbsCmmcChassisFan4Status,_A2:nbsCmmcChassisTemperature,_As:nbsCmmcChassisTemperatureLimit,_At:nbsCmmcChassisTemperatureMin,'nbsCmmcChassisSignalStrength':nbsCmmcChassisSignalStrength,'nbsCmmcChassisSignalStrengthMinimum':nbsCmmcChassisSignalStrengthMinimum,'nbsCmmcChassisEnableAutoReset':nbsCmmcChassisEnableAutoReset,'nbsCmmcChassisEnableLinkTraps':nbsCmmcChassisEnableLinkTraps,'nbsCmmcChassisEnableChassisTraps':nbsCmmcChassisEnableChassisTraps,'nbsCmmcChassisEnableLoopbackTraps':nbsCmmcChassisEnableLoopbackTraps,'nbsCmmcChassisEnableSlotChangeTraps':nbsCmmcChassisEnableSlotChangeTraps,'nbsCmmcChassisEnablePortTraps':nbsCmmcChassisEnablePortTraps,'nbsCmmcChassisResetAllModules':nbsCmmcChassisResetAllModules,'nbsCmmcChassisEnableModuleSpecificTraps':nbsCmmcChassisEnableModuleSpecificTraps,'nbsCmmcChassisLoopbackTimeout':nbsCmmcChassisLoopbackTimeout,'nbsCmmcChassisPortInfoBitMap':nbsCmmcChassisPortInfoBitMap,'nbsCmmcChassisSlotListBitMap':nbsCmmcChassisSlotListBitMap,'nbsCmmcChassisNumberOfPortsBitMap':nbsCmmcChassisNumberOfPortsBitMap,_I:nbsCmmcChassisName,'nbsCmmcChassisEnableLINTraps':nbsCmmcChassisEnableLINTraps,'nbsCmmcChassisEnablePortChangeTraps':nbsCmmcChassisEnablePortChangeTraps,'nbsCmmcChassisEnablePortDiagsTraps':nbsCmmcChassisEnablePortDiagsTraps,'nbsCmmcChassisFan5Status':nbsCmmcChassisFan5Status,'nbsCmmcChassisFan6Status':nbsCmmcChassisFan6Status,'nbsCmmcChassisFan7Status':nbsCmmcChassisFan7Status,'nbsCmmcChassisFan8Status':nbsCmmcChassisFan8Status,'nbsCmmcChassisEnableSwitchoverTraps':nbsCmmcChassisEnableSwitchoverTraps,'nbsCmmcChassisCrossConnect':nbsCmmcChassisCrossConnect,'nbsCmmcChassisNVAreaBanks':nbsCmmcChassisNVAreaBanks,'nbsCmmcChassisFirmwareCaps':nbsCmmcChassisFirmwareCaps,'nbsCmmcChassisFirmwareLoad':nbsCmmcChassisFirmwareLoad,'nbsCmmcChassisNVAreaAdmin':nbsCmmcChassisNVAreaAdmin,'nbsCmmcChassisNVAreaOper':nbsCmmcChassisNVAreaOper,'nbsCmmcChassisLoader':nbsCmmcChassisLoader,'nbsCmmcChassisSerialNum':nbsCmmcChassisSerialNum,'nbsCmmcChassisFace':nbsCmmcChassisFace,'nbsCmmcChassisCountersState':nbsCmmcChassisCountersState,'nbsCmmcChassisPowerStatus':nbsCmmcChassisPowerStatus,'nbsCmmcChassisIfIndex':nbsCmmcChassisIfIndex,'nbsCmmcChassisCount':nbsCmmcChassisCount,'nbsCmmcSlotGrp':nbsCmmcSlotGrp,'nbsCmmcSlotTable':nbsCmmcSlotTable,'nbsCmmcSlotEntry':nbsCmmcSlotEntry,_Ad:nbsCmmcSlotChassisIndex,_L:nbsCmmcSlotIndex,_AG:nbsCmmcSlotType,'nbsCmmcSlotModel':nbsCmmcSlotModel,'nbsCmmcSlotObjectId':nbsCmmcSlotObjectId,'nbsCmmcSlotNumberOfPorts':nbsCmmcSlotNumberOfPorts,'nbsCmmcSlotHardwareRevision':nbsCmmcSlotHardwareRevision,'nbsCmmcSlotOperationType':nbsCmmcSlotOperationType,'nbsCmmcSlotReset':nbsCmmcSlotReset,_M:nbsCmmcSlotName,'nbsCmmcSlotModuleType':nbsCmmcSlotModuleType,'nbsCmmcSlotModuleSlot':nbsCmmcSlotModuleSlot,'nbsCmmcSlotSwConfigurable':nbsCmmcSlotSwConfigurable,'nbsCmmcSlotConfiguration':nbsCmmcSlotConfiguration,'nbsCmmcSlotMacAddress':nbsCmmcSlotMacAddress,'nbsCmmcSlotIPAddress':nbsCmmcSlotIPAddress,'nbsCmmcSlotSubnetMask':nbsCmmcSlotSubnetMask,'nbsCmmcSlotBroadcastAddr':nbsCmmcSlotBroadcastAddr,'nbsCmmcSlotDefGateway':nbsCmmcSlotDefGateway,'nbsCmmcSlotHoming':nbsCmmcSlotHoming,'nbsCmmcSlotRedundancyAdmin':nbsCmmcSlotRedundancyAdmin,'nbsCmmcSlotDescr':nbsCmmcSlotDescr,'nbsCmmcSlotUpgradable':nbsCmmcSlotUpgradable,'nbsCmmcSlotCrossConnect':nbsCmmcSlotCrossConnect,'nbsCmmcSlotClearType':nbsCmmcSlotClearType,'nbsCmmcSlotNVAreaBanks':nbsCmmcSlotNVAreaBanks,'nbsCmmcSlotFirmwareCaps':nbsCmmcSlotFirmwareCaps,'nbsCmmcSlotFirmwareLoad':nbsCmmcSlotFirmwareLoad,'nbsCmmcSlotNVAreaAdmin':nbsCmmcSlotNVAreaAdmin,'nbsCmmcSlotNVAreaOper':nbsCmmcSlotNVAreaOper,'nbsCmmcSlotLoader':nbsCmmcSlotLoader,'nbsCmmcSlotSerialNum':nbsCmmcSlotSerialNum,'nbsCmmcSlotToggleRate':nbsCmmcSlotToggleRate,_A8:nbsCmmcSlotTemperature,'nbsCmmcSlotCountersState':nbsCmmcSlotCountersState,'nbsCmmcSlotRedundancyOper':nbsCmmcSlotRedundancyOper,'nbsCmmcSlotIfIndex':nbsCmmcSlotIfIndex,_B5:nbsCmmcSlotModuleStatus,'nbsCmmcSlotManagementPort':nbsCmmcSlotManagementPort,_B0:nbsCmmcSlotTemperatureLimit,_A_:nbsCmmcSlotTemperatureMin,'nbsCmmcLedTable':nbsCmmcLedTable,'nbsCmmcLedEntry':nbsCmmcLedEntry,_Ae:nbsCmmcLedChassisIndex,_Af:nbsCmmcLedSlotIndex,_Ag:nbsCmmcLedIndex,'nbsCmmcLedColor':nbsCmmcLedColor,'nbsCmmcLedDescription':nbsCmmcLedDescription,'nbsCmmcSlotFaceTable':nbsCmmcSlotFaceTable,'nbsCmmcSlotFaceEntry':nbsCmmcSlotFaceEntry,_Ah:nbsCmmcSlotFaceChassisIndex,_Ai:nbsCmmcSlotFaceSlotIndex,_Aj:nbsCmmcSlotFaceRowIndex,'nbsCmmcSlotFaceSummary':nbsCmmcSlotFaceSummary,'nbsCmmcPortGrp':nbsCmmcPortGrp,'nbsCmmcPortTable':nbsCmmcPortTable,'nbsCmmcPortEntry':nbsCmmcPortEntry,_Ak:nbsCmmcPortChassisIndex,_Al:nbsCmmcPortSlotIndex,_N:nbsCmmcPortIndex,'nbsCmmcPortType':nbsCmmcPortType,'nbsCmmcPortObjectId':nbsCmmcPortObjectId,_Au:nbsCmmcPortLink,'nbsCmmcPortAutoNegotiation':nbsCmmcPortAutoNegotiation,'nbsCmmcPortDuplex':nbsCmmcPortDuplex,'nbsCmmcPortSpeed':nbsCmmcPortSpeed,'nbsCmmcPortRxActivity':nbsCmmcPortRxActivity,'nbsCmmcPortTxActivity':nbsCmmcPortTxActivity,'nbsCmmcPortCollisionActivity':nbsCmmcPortCollisionActivity,'nbsCmmcPortLoopback':nbsCmmcPortLoopback,'nbsCmmcPortEnableAdmin':nbsCmmcPortEnableAdmin,_B4:nbsCmmcPortSelectLink,'nbsCmmcPortLIN':nbsCmmcPortLIN,'nbsCmmcPortAging':nbsCmmcPortAging,'nbsCmmcPortMaxPacketSize':nbsCmmcPortMaxPacketSize,'nbsCmmcPortRemoteLoopback':nbsCmmcPortRemoteLoopback,'nbsCmmcPortErrorActivity':nbsCmmcPortErrorActivity,_O:nbsCmmcPortName,_Av:nbsCmmcPortValue,_X:nbsCmmcPortThreshold,'nbsCmmcPortThresholdAction':nbsCmmcPortThresholdAction,'nbsCmmcPortRMChassis':nbsCmmcPortRMChassis,'nbsCmmcPortRMSlot':nbsCmmcPortRMSlot,'nbsCmmcPortRMPort':nbsCmmcPortRMPort,'nbsCmmcPortSerialNumber':nbsCmmcPortSerialNumber,'nbsCmmcPortVendorInfo':nbsCmmcPortVendorInfo,_A3:nbsCmmcPortTemperature,_A5:nbsCmmcPortTxPower,_A4:nbsCmmcPortRxPower,_A6:nbsCmmcPortBiasAmps,_A7:nbsCmmcPortSupplyVolts,'nbsCmmcPortMedium':nbsCmmcPortMedium,_Aw:nbsCmmcPortConnector,_Ax:nbsCmmcPortWavelength,'nbsCmmcPortDigitalDiags':nbsCmmcPortDigitalDiags,'nbsCmmcPortZoneIdAdmin':nbsCmmcPortZoneIdAdmin,'nbsCmmcPortNominalBitRate':nbsCmmcPortNominalBitRate,'nbsCmmcPortModulePort':nbsCmmcPortModulePort,'nbsCmmcPortPartRev':nbsCmmcPortPartRev,'nbsCmmcPortIfIndex':nbsCmmcPortIfIndex,'nbsCmmcPortLinked':nbsCmmcPortLinked,'nbsCmmcPortOperational':nbsCmmcPortOperational,'nbsCmmcPortZoneChassisAdmin':nbsCmmcPortZoneChassisAdmin,'nbsCmmcPortZoneSlotAdmin':nbsCmmcPortZoneSlotAdmin,'nbsCmmcPortAlarmCause':nbsCmmcPortAlarmCause,'nbsCmmcPortFlowControl':nbsCmmcPortFlowControl,'nbsCmmcPortAutoNegAd':nbsCmmcPortAutoNegAd,'nbsCmmcPortAutoNegEditable':nbsCmmcPortAutoNegEditable,'nbsCmmcPortWavelengthX':nbsCmmcPortWavelengthX,'nbsCmmcPortZoneIdOper':nbsCmmcPortZoneIdOper,'nbsCmmcPortZoneSlotOper':nbsCmmcPortZoneSlotOper,'nbsCmmcPortZoneChassisOper':nbsCmmcPortZoneChassisOper,'nbsCmmcPortLinkMatch':nbsCmmcPortLinkMatch,'nbsCmmcPortMDIPinoutAdmin':nbsCmmcPortMDIPinoutAdmin,'nbsCmmcPortMDIPinoutOper':nbsCmmcPortMDIPinoutOper,'nbsCmmcPortFCRecvAdmin':nbsCmmcPortFCRecvAdmin,'nbsCmmcPortFCRecvOper':nbsCmmcPortFCRecvOper,'nbsCmmcPortFCSendAdmin':nbsCmmcPortFCSendAdmin,'nbsCmmcPortFCSendOper':nbsCmmcPortFCSendOper,'nbsCmmcPortAutoNegWait':nbsCmmcPortAutoNegWait,_AH:nbsCmmcPortTemperatureLevel,_AJ:nbsCmmcPortTxPowerLevel,_AI:nbsCmmcPortRxPowerLevel,_AK:nbsCmmcPortBiasAmpsLevel,_AL:nbsCmmcPortSupplyVoltsLevel,'nbsCmmcPortAmpGainOper':nbsCmmcPortAmpGainOper,'nbsCmmcPortAmpGainAdmin':nbsCmmcPortAmpGainAdmin,'nbsCmmcPortAmpOutputPwrAdmin':nbsCmmcPortAmpOutputPwrAdmin,'nbsCmmcPortProtoCapabilities':nbsCmmcPortProtoCapabilities,'nbsCmmcPortProtoAdmin':nbsCmmcPortProtoAdmin,'nbsCmmcPortProtoOper':nbsCmmcPortProtoOper,'nbsCmmcPortPreambleLen':nbsCmmcPortPreambleLen,'nbsCmmcPortPreferred':nbsCmmcPortPreferred,'nbsCmmcPortCableLen':nbsCmmcPortCableLen,'nbsCmmcPortRedundantTxMode':nbsCmmcPortRedundantTxMode,'nbsCmmcPortTermination':nbsCmmcPortTermination,'nbsCmmcPortDescription':nbsCmmcPortDescription,'nbsCmmcPortTransmitUnmapped':nbsCmmcPortTransmitUnmapped,'nbsCmmcPortToggleMode':nbsCmmcPortToggleMode,'nbsCmmcPortCrossConnect':nbsCmmcPortCrossConnect,'nbsCmmcPortZoneIfIndexAdmin':nbsCmmcPortZoneIfIndexAdmin,'nbsCmmcPortZoneIfIndexOper':nbsCmmcPortZoneIfIndexOper,'nbsCmmcPortEnableOper':nbsCmmcPortEnableOper,'nbsCmmcPortMappingType':nbsCmmcPortMappingType,'nbsCmmcPortCountersState':nbsCmmcPortCountersState,'nbsCmmcPortAmpGainMinimum':nbsCmmcPortAmpGainMinimum,'nbsCmmcPortAmpGainMaximum':nbsCmmcPortAmpGainMaximum,'nbsCmmcPortAmpGainStepSize':nbsCmmcPortAmpGainStepSize,'nbsCmmcPortSniffer':nbsCmmcPortSniffer,'nbsCmmcPortExternalLink1':nbsCmmcPortExternalLink1,'nbsCmmcPortExternalLink2':nbsCmmcPortExternalLink2,'nbsCmmcPortNVAreaBanks':nbsCmmcPortNVAreaBanks,'nbsCmmcPortFirmwareCaps':nbsCmmcPortFirmwareCaps,'nbsCmmcPortFirmwareLoad':nbsCmmcPortFirmwareLoad,'nbsCmmcPortNVAreaAdmin':nbsCmmcPortNVAreaAdmin,'nbsCmmcPortNVAreaOper':nbsCmmcPortNVAreaOper,'nbsCmmcPortLoader':nbsCmmcPortLoader,'nbsCmmcNtpGrp':nbsCmmcNtpGrp,'nbsCmmcSmtpGrp':nbsCmmcSmtpGrp,'nbsCmmcSmtpDomainName':nbsCmmcSmtpDomainName,'nbsCmmcSmtpServerAddress':nbsCmmcSmtpServerAddress,'nbsCmmcSmtpRcvrLevel':nbsCmmcSmtpRcvrLevel,'nbsCmmcSmtpRcvrNum':nbsCmmcSmtpRcvrNum,'nbsCmmcSmtpRcvrTable':nbsCmmcSmtpRcvrTable,'nbsCmmcSmtpRcvrEntry':nbsCmmcSmtpRcvrEntry,_An:nbsCmmcSmtpRcvrIndex,'nbsCmmcSmtpRcvrEmailAddress':nbsCmmcSmtpRcvrEmailAddress,'nbsCmmcSmtpRcvrStatus':nbsCmmcSmtpRcvrStatus,'nbsCmmcSysLogGrp':nbsCmmcSysLogGrp,'nbsCmmcSysLogRunningLevel':nbsCmmcSysLogRunningLevel,'nbsCmmcSysLogNvLevel':nbsCmmcSysLogNvLevel,'nbsCmmcSysLogTrapLevel':nbsCmmcSysLogTrapLevel,'nbsCmmcSysLogEmailLevel':nbsCmmcSysLogEmailLevel,'nbsCmmcSysLogMessageTable':nbsCmmcSysLogMessageTable,'nbsCmmcSysLogMessageEntry':nbsCmmcSysLogMessageEntry,_Ao:nbsCmmcSysLogMessageType,'nbsCmmcSysLogMessageSeverity':nbsCmmcSysLogMessageSeverity,'nbsCmmcSysRunningLogMessageTotal':nbsCmmcSysRunningLogMessageTotal,'nbsCmmcSysRunningLogMessageTable':nbsCmmcSysRunningLogMessageTable,'nbsCmmcSysRunningLogMessageEntry':nbsCmmcSysRunningLogMessageEntry,_Ap:nbsCmmcSysRunningLogMessageIndex,'nbsCmmcSysRunningLogMessageSeverity':nbsCmmcSysRunningLogMessageSeverity,'nbsCmmcSysRunningLogMessageErrorID':nbsCmmcSysRunningLogMessageErrorID,'nbsCmmcSysRunningLogMessageSession':nbsCmmcSysRunningLogMessageSession,'nbsCmmcSysRunningLogMessageTime':nbsCmmcSysRunningLogMessageTime,'nbsCmmcSysRunningLogMessageModule':nbsCmmcSysRunningLogMessageModule,'nbsCmmcSysRunningLogMessageString':nbsCmmcSysRunningLogMessageString,'nbsCmmcSysNvramLogMessageTotal':nbsCmmcSysNvramLogMessageTotal,'nbsCmmcSysNvramLogMessageTable':nbsCmmcSysNvramLogMessageTable,'nbsCmmcSysNvramLogMessageEntry':nbsCmmcSysNvramLogMessageEntry,_Aq:nbsCmmcSysNvramLogMessageIndex,'nbsCmmcSysNvramLogMessageSeverity':nbsCmmcSysNvramLogMessageSeverity,'nbsCmmcSysNvramLogMessageErrorID':nbsCmmcSysNvramLogMessageErrorID,'nbsCmmcSysNvramLogMessageSession':nbsCmmcSysNvramLogMessageSession,'nbsCmmcSysNvramLogMessageTime':nbsCmmcSysNvramLogMessageTime,'nbsCmmcSysNvramLogMessageModule':nbsCmmcSysNvramLogMessageModule,'nbsCmmcSysNvramLogMessageString':nbsCmmcSysNvramLogMessageString,'nbsCmmcSysNvramLogMessagePTime':nbsCmmcSysNvramLogMessagePTime,'nbsCmmcSysNvramLogMessageDateTime':nbsCmmcSysNvramLogMessageDateTime,'nbsCmmcSysAuditLogTotal':nbsCmmcSysAuditLogTotal,'nbsCmmcSysAuditLogTable':nbsCmmcSysAuditLogTable,'nbsCmmcSysAuditLogEntry':nbsCmmcSysAuditLogEntry,_Ar:nbsCmmcSysAuditLogIndex,'nbsCmmcSysAuditLogUpTime':nbsCmmcSysAuditLogUpTime,'nbsCmmcSysAuditLogDateTime':nbsCmmcSysAuditLogDateTime,'nbsCmmcSysAuditLogString':nbsCmmcSysAuditLogString,'nbsCmmcSysLogRemoteServer':nbsCmmcSysLogRemoteServer,'nbsCmmcSysLogRemoteLevel':nbsCmmcSysLogRemoteLevel,'nbsCmmcSysRunningLogMessageClear':nbsCmmcSysRunningLogMessageClear,'nbsCmmcSysNvramLogMessageClear':nbsCmmcSysNvramLogMessageClear,'nbsCmmcSysAuditLogClear':nbsCmmcSysAuditLogClear,'nbsCmmcSysLogNvSize':nbsCmmcSysLogNvSize,'nbsCmmcTrapGrp':nbsCmmcTrapGrp,_G:nbsCmmcTrapLastMessage,_m:nbsCmmcTrapPowerSupplyId,_n:nbsCmmcTrapFanId,_Ay:nbsCmmcTrapPortIndex,_Az:nbsCmmcTrapPortName,_A1:nbsCmmcTrapShutdownReason,_B1:nbsCmmcTrapErrorInfo,_B2:nbsCmmcSlotModelLocked,_B3:nbsCmmcSlotModelInserted,'nbsCmmcTraps':nbsCmmcTraps,'nbsCmmcTraps0':nbsCmmcTraps0,'nbsCmmcTrapGenericTrap':nbsCmmcTrapGenericTrap,'nbsCmmcTrapSpecificTrap':nbsCmmcTrapSpecificTrap,'nbsCmmcTrapDeviceRebooted':nbsCmmcTrapDeviceRebooted,'nbsCmmcTrapDeviceOnline':nbsCmmcTrapDeviceOnline,'nbsCmmcTrapDeviceShuttingDown':nbsCmmcTrapDeviceShuttingDown,'nbsCmmcTrapPowerSupplyFailure':nbsCmmcTrapPowerSupplyFailure,'nbsCmmcTrapPowerSupplyRestored':nbsCmmcTrapPowerSupplyRestored,'nbsCmmcTrapFanFailure':nbsCmmcTrapFanFailure,'nbsCmmcTrapFanRestored':nbsCmmcTrapFanRestored,'nbsCmmcTrapChassisTempTooHigh':nbsCmmcTrapChassisTempTooHigh,'nbsCmmcTrapChassisTempTooLow':nbsCmmcTrapChassisTempTooLow,'nbsCmmcTrapChassisTempOk':nbsCmmcTrapChassisTempOk,'nbsCmmcTrapSlotModuleIn':nbsCmmcTrapSlotModuleIn,'nbsCmmcTrapSlotModuleOut':nbsCmmcTrapSlotModuleOut,'nbsCmmcTrapPortEnabled':nbsCmmcTrapPortEnabled,'nbsCmmcTrapPortDisabled':nbsCmmcTrapPortDisabled,'nbsCmmcTrapPortLinkUp':nbsCmmcTrapPortLinkUp,'nbsCmmcTrapPortLinkDown':nbsCmmcTrapPortLinkDown,'nbsCmmcTrapPortLINOn':nbsCmmcTrapPortLINOn,'nbsCmmcTrapPortLINOff':nbsCmmcTrapPortLINOff,'nbsCmmcTrapPortLoopbackOn':nbsCmmcTrapPortLoopbackOn,'nbsCmmcTrapPortLoopbackOff':nbsCmmcTrapPortLoopbackOff,'nbsCmmcTrapPortMaximumExceeded':nbsCmmcTrapPortMaximumExceeded,'nbsCmmcTrapPortRemoved':nbsCmmcTrapPortRemoved,'nbsCmmcTrapPortInserted':nbsCmmcTrapPortInserted,'nbsCmmcTrapPortTempTooLow':nbsCmmcTrapPortTempTooLow,'nbsCmmcTrapPortTempTooHigh':nbsCmmcTrapPortTempTooHigh,'nbsCmmcTrapPortRxPowerTooLow':nbsCmmcTrapPortRxPowerTooLow,'nbsCmmcTrapPortRxPowerTooHigh':nbsCmmcTrapPortRxPowerTooHigh,'nbsCmmcTrapPortTxPowerTooLow':nbsCmmcTrapPortTxPowerTooLow,'nbsCmmcTrapPortTxPowerTooHigh':nbsCmmcTrapPortTxPowerTooHigh,'nbsCmmcTrapPortAmpsTooLow':nbsCmmcTrapPortAmpsTooLow,'nbsCmmcTrapPortAmpsTooHigh':nbsCmmcTrapPortAmpsTooHigh,'nbsCmmcTrapPortVoltsTooLow':nbsCmmcTrapPortVoltsTooLow,'nbsCmmcTrapPortVoltsTooHigh':nbsCmmcTrapPortVoltsTooHigh,'nbsCmmcTrapSwitchover':nbsCmmcTrapSwitchover,'nbsCmmcTrapSlotShuttingDown':nbsCmmcTrapSlotShuttingDown,'nbsCmmcTrapPortCrcError':nbsCmmcTrapPortCrcError,'nbsCmmcTrapCpeInManagedChassis':nbsCmmcTrapCpeInManagedChassis,'nbsCmmcTrapCoWithoutCpe':nbsCmmcTrapCoWithoutCpe,'nbsCmmcTrapCoTakesControl':nbsCmmcTrapCoTakesControl,'nbsCmmcTrapCoYieldsControl':nbsCmmcTrapCoYieldsControl,'nbsCmmcTrapCoLinkedToCo':nbsCmmcTrapCoLinkedToCo,'nbsCmmcTrapCpeFound':nbsCmmcTrapCpeFound,'nbsCmmcTrapPortReflectionDetected':nbsCmmcTrapPortReflectionDetected,'nbsCmmcTrapPortReflectionCeased':nbsCmmcTrapPortReflectionCeased,'nbsCmmcTrapPortTempOk':nbsCmmcTrapPortTempOk,'nbsCmmcTrapPortRxPowerOk':nbsCmmcTrapPortRxPowerOk,'nbsCmmcTrapPortTxPowerOk':nbsCmmcTrapPortTxPowerOk,'nbsCmmcTrapPortAmpsOk':nbsCmmcTrapPortAmpsOk,'nbsCmmcTrapPortVoltsOk':nbsCmmcTrapPortVoltsOk,'nbsCmmcTrapSlotTempTooLow':nbsCmmcTrapSlotTempTooLow,'nbsCmmcTrapSlotTempTooHigh':nbsCmmcTrapSlotTempTooHigh,'nbsCmmcTrapSlotTempOk':nbsCmmcTrapSlotTempOk,'nbsCmmcTrapPortErrorsDetected':nbsCmmcTrapPortErrorsDetected,'nbsCmmcTrapPortErrorsStopped':nbsCmmcTrapPortErrorsStopped,'nbsCmmcTrapChassisInsufficientPower':nbsCmmcTrapChassisInsufficientPower,'nbsCmmcTrapChassisSufficientPower':nbsCmmcTrapChassisSufficientPower,'nbsCmmcTrapSlotModuleLocked':nbsCmmcTrapSlotModuleLocked,'nbsCmmcTrapSelectLinkChanged':nbsCmmcTrapSelectLinkChanged,'nbsCmmcTrapPowerSupplyRemoved':nbsCmmcTrapPowerSupplyRemoved,'nbsCmmcTrapPowerSupplyInserted':nbsCmmcTrapPowerSupplyInserted,'nbsCmmcTrapFanRemoved':nbsCmmcTrapFanRemoved,'nbsCmmcTrapFanInserted':nbsCmmcTrapFanInserted,'nbsCmmcTrapModuleStatusChanged':nbsCmmcTrapModuleStatusChanged})