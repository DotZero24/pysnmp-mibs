_AK='ubntAFLTUStatusGroup'
_AJ='afLTUStaRemoteRegistrationAttempts'
_AI='afLTUStaRemoteLastIp'
_AH='afLTUStaRemoteConnectionTime'
_AG='afLTUStaRemoteDistance'
_AF='afLTUStaRemoteLatency'
_AE='afLTUStaRemoteRxPowerLevel1'
_AD='afLTUStaRemoteRxPowerLevel0'
_AC='afLTUStaRemoteIdealRxPower1'
_AB='afLTUStaRemoteIdealRxPower0'
_AA='afLTUStaRemoteRxPower1'
_A9='afLTUStaRemoteRxPower0'
_A8='afLTUStaRemoteTxEIRP'
_A7='afLTUStaRemoteFirmwareVersion'
_A6='afLTUStaRemoteDevName'
_A5='afLTUStaRemoteDevModel'
_A4='afLTUStaRxPowerLevel1'
_A3='afLTUStaRxPowerLevel0'
_A2='afLTUStaIdealRxPower1'
_A1='afLTUStaIdealRxPower0'
_A0='afLTUStaRxPower1'
_z='afLTUStaRxPower0'
_y='afLTUStaRxCapacity'
_x='afLTUStaTxCapacity'
_w='afLTUStaRxRate'
_v='afLTUStaTxRate'
_u='afLTUgpsHDOP'
_t='afLTUgpsSatsTracked'
_s='afLTUgpsSatsVisible'
_r='afLTUgpsAltFeet'
_q='afLTUgpsAltMeter'
_p='afLTUgpsLon'
_o='afLTUgpsLat'
_n='afLTUgpsDimensions'
_m='afLTUgpsStatus'
_l='afLTUethConnected'
_k='afLTUethRxPps'
_j='afLTUethRxBytes'
_i='afLTUethTxPps'
_h='afLTUethTxBytes'
_g='afLTUConnected'
_f='afLTURxPps'
_e='afLTURxBytes'
_d='afLTUTxPps'
_c='afLTUTxBytes'
_b='afLTUUptime'
_a='afLTUCpuUsage'
_Z='afLTUMemoryUsage'
_Y='afLTUFirmwareVersion'
_X='afLTUDevName'
_W='afLTUDevModel'
_V='afLTUMac'
_U='afLTUDistanceScale'
_T='afLTUTxRateAuto'
_S='afLTUTxRate'
_R='afLTUCableLoss'
_Q='afLTUAntennaGain'
_P='afLTUTxEIRP'
_O='afLTUSsid'
_N='afLTUBandwidth'
_M='afLTUAltFreqList'
_L='afLTUFrequency'
_K='afLTURole'
_J='connected'
_I='disconnected'
_H='afLTUStaRemoteMac'
_G='DisplayString'
_F='dBm'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='UBNT-AFLTU-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,'MacAddress','PhysAddress','TextualConvention')
ubntAFLTU,ubntAFLTUGroups=mibBuilder.importSymbols('UBNT-MIB','ubntAFLTU','ubntAFLTUGroups')
afLTUMIB=ModuleIdentity((1,3,6,1,4,1,41112,1,10,1))
if mibBuilder.loadTexts:afLTUMIB.setRevisions(('2018-06-05 00:00',))
_AfLTUCompliances_ObjectIdentity=ObjectIdentity
afLTUCompliances=_AfLTUCompliances_ObjectIdentity((1,3,6,1,4,1,41112,1,2,9,1))
_AfLTUGroups_ObjectIdentity=ObjectIdentity
afLTUGroups=_AfLTUGroups_ObjectIdentity((1,3,6,1,4,1,41112,1,2,9,2))
_AfLTUConfig_ObjectIdentity=ObjectIdentity
afLTUConfig=_AfLTUConfig_ObjectIdentity((1,3,6,1,4,1,41112,1,10,1,2))
class _AfLTURole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('ap',0),('cpe',1)))
_AfLTURole_Type.__name__=_D
_AfLTURole_Object=MibScalar
afLTURole=_AfLTURole_Object((1,3,6,1,4,1,41112,1,10,1,2,1),_AfLTURole_Type())
afLTURole.setMaxAccess(_E)
if mibBuilder.loadTexts:afLTURole.setStatus(_A)
_AfLTUFrequency_Type=Integer32
_AfLTUFrequency_Object=MibScalar
afLTUFrequency=_AfLTUFrequency_Object((1,3,6,1,4,1,41112,1,10,1,2,2),_AfLTUFrequency_Type())
afLTUFrequency.setMaxAccess(_E)
if mibBuilder.loadTexts:afLTUFrequency.setStatus(_A)
if mibBuilder.loadTexts:afLTUFrequency.setUnits('MHz')
class _AfLTUAltFreqList_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,100))
_AfLTUAltFreqList_Type.__name__=_G
_AfLTUAltFreqList_Object=MibScalar
afLTUAltFreqList=_AfLTUAltFreqList_Object((1,3,6,1,4,1,41112,1,10,1,2,3),_AfLTUAltFreqList_Type())
afLTUAltFreqList.setMaxAccess(_E)
if mibBuilder.loadTexts:afLTUAltFreqList.setStatus(_A)
class _AfLTUBandwidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(10,20,30,40,50,60,80,100)));namedValues=NamedValues(*(('bw10M',10),('bw20M',20),('bw30M',30),('bw40M',40),('bw50M',50),('bw60M',60),('bw80M',80),('bw100M',100)))
_AfLTUBandwidth_Type.__name__=_D
_AfLTUBandwidth_Object=MibScalar
afLTUBandwidth=_AfLTUBandwidth_Object((1,3,6,1,4,1,41112,1,10,1,2,4),_AfLTUBandwidth_Type())
afLTUBandwidth.setMaxAccess(_E)
if mibBuilder.loadTexts:afLTUBandwidth.setStatus(_A)
if mibBuilder.loadTexts:afLTUBandwidth.setUnits('MHz')
class _AfLTUSsid_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
_AfLTUSsid_Type.__name__=_G
_AfLTUSsid_Object=MibScalar
afLTUSsid=_AfLTUSsid_Object((1,3,6,1,4,1,41112,1,10,1,2,5),_AfLTUSsid_Type())
afLTUSsid.setMaxAccess(_E)
if mibBuilder.loadTexts:afLTUSsid.setStatus(_A)
class _AfLTUTxEIRP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-10,100))
_AfLTUTxEIRP_Type.__name__=_D
_AfLTUTxEIRP_Object=MibScalar
afLTUTxEIRP=_AfLTUTxEIRP_Object((1,3,6,1,4,1,41112,1,10,1,2,6),_AfLTUTxEIRP_Type())
afLTUTxEIRP.setMaxAccess(_E)
if mibBuilder.loadTexts:afLTUTxEIRP.setStatus(_A)
class _AfLTUAntennaGain_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,40))
_AfLTUAntennaGain_Type.__name__=_D
_AfLTUAntennaGain_Object=MibScalar
afLTUAntennaGain=_AfLTUAntennaGain_Object((1,3,6,1,4,1,41112,1,10,1,2,7),_AfLTUAntennaGain_Type())
afLTUAntennaGain.setMaxAccess(_E)
if mibBuilder.loadTexts:afLTUAntennaGain.setStatus(_A)
class _AfLTUCableLoss_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_AfLTUCableLoss_Type.__name__=_D
_AfLTUCableLoss_Object=MibScalar
afLTUCableLoss=_AfLTUCableLoss_Object((1,3,6,1,4,1,41112,1,10,1,2,8),_AfLTUCableLoss_Type())
afLTUCableLoss.setMaxAccess(_E)
if mibBuilder.loadTexts:afLTUCableLoss.setStatus(_A)
_AfLTUTxRate_Type=Integer32
_AfLTUTxRate_Object=MibScalar
afLTUTxRate=_AfLTUTxRate_Object((1,3,6,1,4,1,41112,1,10,1,2,9),_AfLTUTxRate_Type())
afLTUTxRate.setMaxAccess(_E)
if mibBuilder.loadTexts:afLTUTxRate.setStatus(_A)
if mibBuilder.loadTexts:afLTUTxRate.setUnits('x')
class _AfLTUTxRateAuto_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disabled',0),('enabled',1)))
_AfLTUTxRateAuto_Type.__name__=_D
_AfLTUTxRateAuto_Object=MibScalar
afLTUTxRateAuto=_AfLTUTxRateAuto_Object((1,3,6,1,4,1,41112,1,10,1,2,10),_AfLTUTxRateAuto_Type())
afLTUTxRateAuto.setMaxAccess(_E)
if mibBuilder.loadTexts:afLTUTxRateAuto.setStatus(_A)
class _AfLTUDistanceScale_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_AfLTUDistanceScale_Type.__name__=_D
_AfLTUDistanceScale_Object=MibScalar
afLTUDistanceScale=_AfLTUDistanceScale_Object((1,3,6,1,4,1,41112,1,10,1,2,11),_AfLTUDistanceScale_Type())
afLTUDistanceScale.setMaxAccess(_E)
if mibBuilder.loadTexts:afLTUDistanceScale.setStatus(_A)
_AfLTUStatus_ObjectIdentity=ObjectIdentity
afLTUStatus=_AfLTUStatus_ObjectIdentity((1,3,6,1,4,1,41112,1,10,1,3))
_AfLTUMac_Type=MacAddress
_AfLTUMac_Object=MibScalar
afLTUMac=_AfLTUMac_Object((1,3,6,1,4,1,41112,1,10,1,3,1),_AfLTUMac_Type())
afLTUMac.setMaxAccess(_C)
if mibBuilder.loadTexts:afLTUMac.setStatus(_A)
_AfLTUDevModel_Type=DisplayString
_AfLTUDevModel_Object=MibScalar
afLTUDevModel=_AfLTUDevModel_Object((1,3,6,1,4,1,41112,1,10,1,3,2),_AfLTUDevModel_Type())
afLTUDevModel.setMaxAccess(_C)
if mibBuilder.loadTexts:afLTUDevModel.setStatus(_A)
_AfLTUDevName_Type=DisplayString
_AfLTUDevName_Object=MibScalar
afLTUDevName=_AfLTUDevName_Object((1,3,6,1,4,1,41112,1,10,1,3,3),_AfLTUDevName_Type())
afLTUDevName.setMaxAccess(_C)
if mibBuilder.loadTexts:afLTUDevName.setStatus(_A)
_AfLTUFirmwareVersion_Type=DisplayString
_AfLTUFirmwareVersion_Object=MibScalar
afLTUFirmwareVersion=_AfLTUFirmwareVersion_Object((1,3,6,1,4,1,41112,1,10,1,3,4),_AfLTUFirmwareVersion_Type())
afLTUFirmwareVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:afLTUFirmwareVersion.setStatus(_A)
_AfLTUMemoryUsage_Type=Integer32
_AfLTUMemoryUsage_Object=MibScalar
afLTUMemoryUsage=_AfLTUMemoryUsage_Object((1,3,6,1,4,1,41112,1,10,1,3,5),_AfLTUMemoryUsage_Type())
afLTUMemoryUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:afLTUMemoryUsage.setStatus(_A)
if mibBuilder.loadTexts:afLTUMemoryUsage.setUnits('%')
_AfLTUCpuUsage_Type=Integer32
_AfLTUCpuUsage_Object=MibScalar
afLTUCpuUsage=_AfLTUCpuUsage_Object((1,3,6,1,4,1,41112,1,10,1,3,6),_AfLTUCpuUsage_Type())
afLTUCpuUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:afLTUCpuUsage.setStatus(_A)
if mibBuilder.loadTexts:afLTUCpuUsage.setUnits('%')
_AfLTUUptime_Type=Counter64
_AfLTUUptime_Object=MibScalar
afLTUUptime=_AfLTUUptime_Object((1,3,6,1,4,1,41112,1,10,1,3,7),_AfLTUUptime_Type())
afLTUUptime.setMaxAccess(_C)
if mibBuilder.loadTexts:afLTUUptime.setStatus(_A)
if mibBuilder.loadTexts:afLTUUptime.setUnits('s')
_AfLTUStationTable_Object=MibTable
afLTUStationTable=_AfLTUStationTable_Object((1,3,6,1,4,1,41112,1,10,1,4))
if mibBuilder.loadTexts:afLTUStationTable.setStatus(_A)
_AfLTUStationEntry_Object=MibTableRow
afLTUStationEntry=_AfLTUStationEntry_Object((1,3,6,1,4,1,41112,1,10,1,4,1))
afLTUStationEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:afLTUStationEntry.setStatus(_A)
_AfLTUStaTxRate_Type=Integer32
_AfLTUStaTxRate_Object=MibTableColumn
afLTUStaTxRate=_AfLTUStaTxRate_Object((1,3,6,1,4,1,41112,1,10,1,4,1,1),_AfLTUStaTxRate_Type())
afLTUStaTxRate.setMaxAccess(_E)
if mibBuilder.loadTexts:afLTUStaTxRate.setStatus(_A)
if mibBuilder.loadTexts:afLTUStaTxRate.setUnits('x')
_AfLTUStaRxRate_Type=Integer32
_AfLTUStaRxRate_Object=MibTableColumn
afLTUStaRxRate=_AfLTUStaRxRate_Object((1,3,6,1,4,1,41112,1,10,1,4,1,2),_AfLTUStaRxRate_Type())
afLTUStaRxRate.setMaxAccess(_E)
if mibBuilder.loadTexts:afLTUStaRxRate.setStatus(_A)
if mibBuilder.loadTexts:afLTUStaRxRate.setUnits('x')
_AfLTUStaTxCapacity_Type=Integer32
_AfLTUStaTxCapacity_Object=MibTableColumn
afLTUStaTxCapacity=_AfLTUStaTxCapacity_Object((1,3,6,1,4,1,41112,1,10,1,4,1,3),_AfLTUStaTxCapacity_Type())
afLTUStaTxCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:afLTUStaTxCapacity.setStatus(_A)
if mibBuilder.loadTexts:afLTUStaTxCapacity.setUnits('Kbps')
_AfLTUStaRxCapacity_Type=Integer32
_AfLTUStaRxCapacity_Object=MibTableColumn
afLTUStaRxCapacity=_AfLTUStaRxCapacity_Object((1,3,6,1,4,1,41112,1,10,1,4,1,4),_AfLTUStaRxCapacity_Type())
afLTUStaRxCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:afLTUStaRxCapacity.setStatus(_A)
if mibBuilder.loadTexts:afLTUStaRxCapacity.setUnits('Kbps')
_AfLTUStaRxPower0_Type=Integer32
_AfLTUStaRxPower0_Object=MibTableColumn
afLTUStaRxPower0=_AfLTUStaRxPower0_Object((1,3,6,1,4,1,41112,1,10,1,4,1,5),_AfLTUStaRxPower0_Type())
afLTUStaRxPower0.setMaxAccess(_C)
if mibBuilder.loadTexts:afLTUStaRxPower0.setStatus(_A)
if mibBuilder.loadTexts:afLTUStaRxPower0.setUnits(_F)
_AfLTUStaRxPower1_Type=Integer32
_AfLTUStaRxPower1_Object=MibTableColumn
afLTUStaRxPower1=_AfLTUStaRxPower1_Object((1,3,6,1,4,1,41112,1,10,1,4,1,6),_AfLTUStaRxPower1_Type())
afLTUStaRxPower1.setMaxAccess(_C)
if mibBuilder.loadTexts:afLTUStaRxPower1.setStatus(_A)
if mibBuilder.loadTexts:afLTUStaRxPower1.setUnits(_F)
_AfLTUStaIdealRxPower0_Type=Integer32
_AfLTUStaIdealRxPower0_Object=MibTableColumn
afLTUStaIdealRxPower0=_AfLTUStaIdealRxPower0_Object((1,3,6,1,4,1,41112,1,10,1,4,1,7),_AfLTUStaIdealRxPower0_Type())
afLTUStaIdealRxPower0.setMaxAccess(_C)
if mibBuilder.loadTexts:afLTUStaIdealRxPower0.setStatus(_A)
if mibBuilder.loadTexts:afLTUStaIdealRxPower0.setUnits(_F)
_AfLTUStaIdealRxPower1_Type=Integer32
_AfLTUStaIdealRxPower1_Object=MibTableColumn
afLTUStaIdealRxPower1=_AfLTUStaIdealRxPower1_Object((1,3,6,1,4,1,41112,1,10,1,4,1,8),_AfLTUStaIdealRxPower1_Type())
afLTUStaIdealRxPower1.setMaxAccess(_C)
if mibBuilder.loadTexts:afLTUStaIdealRxPower1.setStatus(_A)
if mibBuilder.loadTexts:afLTUStaIdealRxPower1.setUnits(_F)
class _AfLTUStaRxPowerLevel0_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,100))
_AfLTUStaRxPowerLevel0_Type.__name__=_D
_AfLTUStaRxPowerLevel0_Object=MibTableColumn
afLTUStaRxPowerLevel0=_AfLTUStaRxPowerLevel0_Object((1,3,6,1,4,1,41112,1,10,1,4,1,9),_AfLTUStaRxPowerLevel0_Type())
afLTUStaRxPowerLevel0.setMaxAccess(_C)
if mibBuilder.loadTexts:afLTUStaRxPowerLevel0.setStatus(_A)
if mibBuilder.loadTexts:afLTUStaRxPowerLevel0.setUnits('%')
class _AfLTUStaRxPowerLevel1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,100))
_AfLTUStaRxPowerLevel1_Type.__name__=_D
_AfLTUStaRxPowerLevel1_Object=MibTableColumn
afLTUStaRxPowerLevel1=_AfLTUStaRxPowerLevel1_Object((1,3,6,1,4,1,41112,1,10,1,4,1,10),_AfLTUStaRxPowerLevel1_Type())
afLTUStaRxPowerLevel1.setMaxAccess(_C)
if mibBuilder.loadTexts:afLTUStaRxPowerLevel1.setStatus(_A)
if mibBuilder.loadTexts:afLTUStaRxPowerLevel1.setUnits('%')
_AfLTUStaRemoteMac_Type=MacAddress
_AfLTUStaRemoteMac_Object=MibTableColumn
afLTUStaRemoteMac=_AfLTUStaRemoteMac_Object((1,3,6,1,4,1,41112,1,10,1,4,1,11),_AfLTUStaRemoteMac_Type())
afLTUStaRemoteMac.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:afLTUStaRemoteMac.setStatus(_A)
_AfLTUStaRemoteDevModel_Type=DisplayString
_AfLTUStaRemoteDevModel_Object=MibTableColumn
afLTUStaRemoteDevModel=_AfLTUStaRemoteDevModel_Object((1,3,6,1,4,1,41112,1,10,1,4,1,12),_AfLTUStaRemoteDevModel_Type())
afLTUStaRemoteDevModel.setMaxAccess(_C)
if mibBuilder.loadTexts:afLTUStaRemoteDevModel.setStatus(_A)
_AfLTUStaRemoteDevName_Type=DisplayString
_AfLTUStaRemoteDevName_Object=MibTableColumn
afLTUStaRemoteDevName=_AfLTUStaRemoteDevName_Object((1,3,6,1,4,1,41112,1,10,1,4,1,13),_AfLTUStaRemoteDevName_Type())
afLTUStaRemoteDevName.setMaxAccess(_C)
if mibBuilder.loadTexts:afLTUStaRemoteDevName.setStatus(_A)
_AfLTUStaRemoteFirmwareVersion_Type=DisplayString
_AfLTUStaRemoteFirmwareVersion_Object=MibTableColumn
afLTUStaRemoteFirmwareVersion=_AfLTUStaRemoteFirmwareVersion_Object((1,3,6,1,4,1,41112,1,10,1,4,1,14),_AfLTUStaRemoteFirmwareVersion_Type())
afLTUStaRemoteFirmwareVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:afLTUStaRemoteFirmwareVersion.setStatus(_A)
_AfLTUStaRemoteTxEIRP_Type=Integer32
_AfLTUStaRemoteTxEIRP_Object=MibTableColumn
afLTUStaRemoteTxEIRP=_AfLTUStaRemoteTxEIRP_Object((1,3,6,1,4,1,41112,1,10,1,4,1,15),_AfLTUStaRemoteTxEIRP_Type())
afLTUStaRemoteTxEIRP.setMaxAccess(_C)
if mibBuilder.loadTexts:afLTUStaRemoteTxEIRP.setStatus(_A)
if mibBuilder.loadTexts:afLTUStaRemoteTxEIRP.setUnits(_F)
_AfLTUStaRemoteRxPower0_Type=Integer32
_AfLTUStaRemoteRxPower0_Object=MibTableColumn
afLTUStaRemoteRxPower0=_AfLTUStaRemoteRxPower0_Object((1,3,6,1,4,1,41112,1,10,1,4,1,16),_AfLTUStaRemoteRxPower0_Type())
afLTUStaRemoteRxPower0.setMaxAccess(_C)
if mibBuilder.loadTexts:afLTUStaRemoteRxPower0.setStatus(_A)
if mibBuilder.loadTexts:afLTUStaRemoteRxPower0.setUnits(_F)
_AfLTUStaRemoteRxPower1_Type=Integer32
_AfLTUStaRemoteRxPower1_Object=MibTableColumn
afLTUStaRemoteRxPower1=_AfLTUStaRemoteRxPower1_Object((1,3,6,1,4,1,41112,1,10,1,4,1,17),_AfLTUStaRemoteRxPower1_Type())
afLTUStaRemoteRxPower1.setMaxAccess(_C)
if mibBuilder.loadTexts:afLTUStaRemoteRxPower1.setStatus(_A)
if mibBuilder.loadTexts:afLTUStaRemoteRxPower1.setUnits(_F)
_AfLTUStaRemoteIdealRxPower0_Type=Integer32
_AfLTUStaRemoteIdealRxPower0_Object=MibTableColumn
afLTUStaRemoteIdealRxPower0=_AfLTUStaRemoteIdealRxPower0_Object((1,3,6,1,4,1,41112,1,10,1,4,1,18),_AfLTUStaRemoteIdealRxPower0_Type())
afLTUStaRemoteIdealRxPower0.setMaxAccess(_C)
if mibBuilder.loadTexts:afLTUStaRemoteIdealRxPower0.setStatus(_A)
if mibBuilder.loadTexts:afLTUStaRemoteIdealRxPower0.setUnits(_F)
_AfLTUStaRemoteIdealRxPower1_Type=Integer32
_AfLTUStaRemoteIdealRxPower1_Object=MibTableColumn
afLTUStaRemoteIdealRxPower1=_AfLTUStaRemoteIdealRxPower1_Object((1,3,6,1,4,1,41112,1,10,1,4,1,19),_AfLTUStaRemoteIdealRxPower1_Type())
afLTUStaRemoteIdealRxPower1.setMaxAccess(_C)
if mibBuilder.loadTexts:afLTUStaRemoteIdealRxPower1.setStatus(_A)
if mibBuilder.loadTexts:afLTUStaRemoteIdealRxPower1.setUnits(_F)
class _AfLTUStaRemoteRxPowerLevel0_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,100))
_AfLTUStaRemoteRxPowerLevel0_Type.__name__=_D
_AfLTUStaRemoteRxPowerLevel0_Object=MibTableColumn
afLTUStaRemoteRxPowerLevel0=_AfLTUStaRemoteRxPowerLevel0_Object((1,3,6,1,4,1,41112,1,10,1,4,1,20),_AfLTUStaRemoteRxPowerLevel0_Type())
afLTUStaRemoteRxPowerLevel0.setMaxAccess(_C)
if mibBuilder.loadTexts:afLTUStaRemoteRxPowerLevel0.setStatus(_A)
if mibBuilder.loadTexts:afLTUStaRemoteRxPowerLevel0.setUnits('%')
class _AfLTUStaRemoteRxPowerLevel1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,100))
_AfLTUStaRemoteRxPowerLevel1_Type.__name__=_D
_AfLTUStaRemoteRxPowerLevel1_Object=MibTableColumn
afLTUStaRemoteRxPowerLevel1=_AfLTUStaRemoteRxPowerLevel1_Object((1,3,6,1,4,1,41112,1,10,1,4,1,21),_AfLTUStaRemoteRxPowerLevel1_Type())
afLTUStaRemoteRxPowerLevel1.setMaxAccess(_C)
if mibBuilder.loadTexts:afLTUStaRemoteRxPowerLevel1.setStatus(_A)
if mibBuilder.loadTexts:afLTUStaRemoteRxPowerLevel1.setUnits('%')
_AfLTUStaRemoteLatency_Type=Integer32
_AfLTUStaRemoteLatency_Object=MibTableColumn
afLTUStaRemoteLatency=_AfLTUStaRemoteLatency_Object((1,3,6,1,4,1,41112,1,10,1,4,1,22),_AfLTUStaRemoteLatency_Type())
afLTUStaRemoteLatency.setMaxAccess(_C)
if mibBuilder.loadTexts:afLTUStaRemoteLatency.setStatus(_A)
if mibBuilder.loadTexts:afLTUStaRemoteLatency.setUnits('ms')
_AfLTUStaRemoteDistance_Type=Integer32
_AfLTUStaRemoteDistance_Object=MibTableColumn
afLTUStaRemoteDistance=_AfLTUStaRemoteDistance_Object((1,3,6,1,4,1,41112,1,10,1,4,1,23),_AfLTUStaRemoteDistance_Type())
afLTUStaRemoteDistance.setMaxAccess(_C)
if mibBuilder.loadTexts:afLTUStaRemoteDistance.setStatus(_A)
if mibBuilder.loadTexts:afLTUStaRemoteDistance.setUnits('km')
_AfLTUStaRemoteConnectionTime_Type=Counter64
_AfLTUStaRemoteConnectionTime_Object=MibTableColumn
afLTUStaRemoteConnectionTime=_AfLTUStaRemoteConnectionTime_Object((1,3,6,1,4,1,41112,1,10,1,4,1,24),_AfLTUStaRemoteConnectionTime_Type())
afLTUStaRemoteConnectionTime.setMaxAccess(_C)
if mibBuilder.loadTexts:afLTUStaRemoteConnectionTime.setStatus(_A)
_AfLTUStaRemoteLastIp_Type=IpAddress
_AfLTUStaRemoteLastIp_Object=MibTableColumn
afLTUStaRemoteLastIp=_AfLTUStaRemoteLastIp_Object((1,3,6,1,4,1,41112,1,10,1,4,1,25),_AfLTUStaRemoteLastIp_Type())
afLTUStaRemoteLastIp.setMaxAccess(_C)
if mibBuilder.loadTexts:afLTUStaRemoteLastIp.setStatus(_A)
_AfLTUStaRemoteRegistrationAttempts_Type=Integer32
_AfLTUStaRemoteRegistrationAttempts_Object=MibTableColumn
afLTUStaRemoteRegistrationAttempts=_AfLTUStaRemoteRegistrationAttempts_Object((1,3,6,1,4,1,41112,1,10,1,4,1,26),_AfLTUStaRemoteRegistrationAttempts_Type())
afLTUStaRemoteRegistrationAttempts.setMaxAccess(_C)
if mibBuilder.loadTexts:afLTUStaRemoteRegistrationAttempts.setStatus(_A)
_AfLTUStats_ObjectIdentity=ObjectIdentity
afLTUStats=_AfLTUStats_ObjectIdentity((1,3,6,1,4,1,41112,1,10,1,5))
_AfLTUTxBytes_Type=Counter64
_AfLTUTxBytes_Object=MibScalar
afLTUTxBytes=_AfLTUTxBytes_Object((1,3,6,1,4,1,41112,1,10,1,5,1),_AfLTUTxBytes_Type())
afLTUTxBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:afLTUTxBytes.setStatus(_A)
_AfLTUTxPps_Type=Integer32
_AfLTUTxPps_Object=MibScalar
afLTUTxPps=_AfLTUTxPps_Object((1,3,6,1,4,1,41112,1,10,1,5,2),_AfLTUTxPps_Type())
afLTUTxPps.setMaxAccess(_C)
if mibBuilder.loadTexts:afLTUTxPps.setStatus(_A)
_AfLTURxBytes_Type=Counter64
_AfLTURxBytes_Object=MibScalar
afLTURxBytes=_AfLTURxBytes_Object((1,3,6,1,4,1,41112,1,10,1,5,3),_AfLTURxBytes_Type())
afLTURxBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:afLTURxBytes.setStatus(_A)
_AfLTURxPps_Type=Integer32
_AfLTURxPps_Object=MibScalar
afLTURxPps=_AfLTURxPps_Object((1,3,6,1,4,1,41112,1,10,1,5,4),_AfLTURxPps_Type())
afLTURxPps.setMaxAccess(_C)
if mibBuilder.loadTexts:afLTURxPps.setStatus(_A)
class _AfLTUConnected_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_AfLTUConnected_Type.__name__=_D
_AfLTUConnected_Object=MibScalar
afLTUConnected=_AfLTUConnected_Object((1,3,6,1,4,1,41112,1,10,1,5,5),_AfLTUConnected_Type())
afLTUConnected.setMaxAccess(_C)
if mibBuilder.loadTexts:afLTUConnected.setStatus(_A)
_AfLTUethStats_ObjectIdentity=ObjectIdentity
afLTUethStats=_AfLTUethStats_ObjectIdentity((1,3,6,1,4,1,41112,1,10,1,6))
_AfLTUethTxBytes_Type=Counter64
_AfLTUethTxBytes_Object=MibScalar
afLTUethTxBytes=_AfLTUethTxBytes_Object((1,3,6,1,4,1,41112,1,10,1,6,1),_AfLTUethTxBytes_Type())
afLTUethTxBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:afLTUethTxBytes.setStatus(_A)
_AfLTUethTxPps_Type=Integer32
_AfLTUethTxPps_Object=MibScalar
afLTUethTxPps=_AfLTUethTxPps_Object((1,3,6,1,4,1,41112,1,10,1,6,2),_AfLTUethTxPps_Type())
afLTUethTxPps.setMaxAccess(_C)
if mibBuilder.loadTexts:afLTUethTxPps.setStatus(_A)
_AfLTUethRxBytes_Type=Counter64
_AfLTUethRxBytes_Object=MibScalar
afLTUethRxBytes=_AfLTUethRxBytes_Object((1,3,6,1,4,1,41112,1,10,1,6,3),_AfLTUethRxBytes_Type())
afLTUethRxBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:afLTUethRxBytes.setStatus(_A)
_AfLTUethRxPps_Type=Integer32
_AfLTUethRxPps_Object=MibScalar
afLTUethRxPps=_AfLTUethRxPps_Object((1,3,6,1,4,1,41112,1,10,1,6,4),_AfLTUethRxPps_Type())
afLTUethRxPps.setMaxAccess(_C)
if mibBuilder.loadTexts:afLTUethRxPps.setStatus(_A)
class _AfLTUethConnected_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_AfLTUethConnected_Type.__name__=_D
_AfLTUethConnected_Object=MibScalar
afLTUethConnected=_AfLTUethConnected_Object((1,3,6,1,4,1,41112,1,10,1,6,5),_AfLTUethConnected_Type())
afLTUethConnected.setMaxAccess(_C)
if mibBuilder.loadTexts:afLTUethConnected.setStatus(_A)
_AfLTUgpsStats_ObjectIdentity=ObjectIdentity
afLTUgpsStats=_AfLTUgpsStats_ObjectIdentity((1,3,6,1,4,1,41112,1,10,1,7))
class _AfLTUgpsStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('absent',0),('off',1),('on',2)))
_AfLTUgpsStatus_Type.__name__=_D
_AfLTUgpsStatus_Object=MibScalar
afLTUgpsStatus=_AfLTUgpsStatus_Object((1,3,6,1,4,1,41112,1,10,1,7,1),_AfLTUgpsStatus_Type())
afLTUgpsStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:afLTUgpsStatus.setStatus(_A)
class _AfLTUgpsDimensions_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('unknown',0),('nofix',1),('fix2d',2),('fix3d',3)))
_AfLTUgpsDimensions_Type.__name__=_D
_AfLTUgpsDimensions_Object=MibScalar
afLTUgpsDimensions=_AfLTUgpsDimensions_Object((1,3,6,1,4,1,41112,1,10,1,7,2),_AfLTUgpsDimensions_Type())
afLTUgpsDimensions.setMaxAccess(_C)
if mibBuilder.loadTexts:afLTUgpsDimensions.setStatus(_A)
_AfLTUgpsLat_Type=DisplayString
_AfLTUgpsLat_Object=MibScalar
afLTUgpsLat=_AfLTUgpsLat_Object((1,3,6,1,4,1,41112,1,10,1,7,3),_AfLTUgpsLat_Type())
afLTUgpsLat.setMaxAccess(_C)
if mibBuilder.loadTexts:afLTUgpsLat.setStatus(_A)
_AfLTUgpsLon_Type=DisplayString
_AfLTUgpsLon_Object=MibScalar
afLTUgpsLon=_AfLTUgpsLon_Object((1,3,6,1,4,1,41112,1,10,1,7,4),_AfLTUgpsLon_Type())
afLTUgpsLon.setMaxAccess(_C)
if mibBuilder.loadTexts:afLTUgpsLon.setStatus(_A)
_AfLTUgpsAltMeter_Type=DisplayString
_AfLTUgpsAltMeter_Object=MibScalar
afLTUgpsAltMeter=_AfLTUgpsAltMeter_Object((1,3,6,1,4,1,41112,1,10,1,7,5),_AfLTUgpsAltMeter_Type())
afLTUgpsAltMeter.setMaxAccess(_C)
if mibBuilder.loadTexts:afLTUgpsAltMeter.setStatus(_A)
if mibBuilder.loadTexts:afLTUgpsAltMeter.setUnits('(m)')
_AfLTUgpsAltFeet_Type=DisplayString
_AfLTUgpsAltFeet_Object=MibScalar
afLTUgpsAltFeet=_AfLTUgpsAltFeet_Object((1,3,6,1,4,1,41112,1,10,1,7,6),_AfLTUgpsAltFeet_Type())
afLTUgpsAltFeet.setMaxAccess(_C)
if mibBuilder.loadTexts:afLTUgpsAltFeet.setStatus(_A)
if mibBuilder.loadTexts:afLTUgpsAltFeet.setUnits('(ft)')
_AfLTUgpsSatsVisible_Type=Integer32
_AfLTUgpsSatsVisible_Object=MibScalar
afLTUgpsSatsVisible=_AfLTUgpsSatsVisible_Object((1,3,6,1,4,1,41112,1,10,1,7,7),_AfLTUgpsSatsVisible_Type())
afLTUgpsSatsVisible.setMaxAccess(_C)
if mibBuilder.loadTexts:afLTUgpsSatsVisible.setStatus(_A)
_AfLTUgpsSatsTracked_Type=Integer32
_AfLTUgpsSatsTracked_Object=MibScalar
afLTUgpsSatsTracked=_AfLTUgpsSatsTracked_Object((1,3,6,1,4,1,41112,1,10,1,7,8),_AfLTUgpsSatsTracked_Type())
afLTUgpsSatsTracked.setMaxAccess(_C)
if mibBuilder.loadTexts:afLTUgpsSatsTracked.setStatus(_A)
_AfLTUgpsHDOP_Type=DisplayString
_AfLTUgpsHDOP_Object=MibScalar
afLTUgpsHDOP=_AfLTUgpsHDOP_Object((1,3,6,1,4,1,41112,1,10,1,7,9),_AfLTUgpsHDOP_Type())
afLTUgpsHDOP.setMaxAccess(_C)
if mibBuilder.loadTexts:afLTUgpsHDOP.setStatus(_A)
ubntAFLTUStatusGroup=ObjectGroup((1,3,6,1,4,1,41112,1,2,9,2,1))
ubntAFLTUStatusGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ)))
if mibBuilder.loadTexts:ubntAFLTUStatusGroup.setStatus(_A)
ubntAFLTUStatusCompliance=ModuleCompliance((1,3,6,1,4,1,41112,1,2,9,2,2))
ubntAFLTUStatusCompliance.setObjects((_B,_AK))
if mibBuilder.loadTexts:ubntAFLTUStatusCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'afLTUCompliances':afLTUCompliances,'afLTUGroups':afLTUGroups,_AK:ubntAFLTUStatusGroup,'ubntAFLTUStatusCompliance':ubntAFLTUStatusCompliance,'afLTUMIB':afLTUMIB,'afLTUConfig':afLTUConfig,_K:afLTURole,_L:afLTUFrequency,_M:afLTUAltFreqList,_N:afLTUBandwidth,_O:afLTUSsid,_P:afLTUTxEIRP,_Q:afLTUAntennaGain,_R:afLTUCableLoss,_S:afLTUTxRate,_T:afLTUTxRateAuto,_U:afLTUDistanceScale,'afLTUStatus':afLTUStatus,_V:afLTUMac,_W:afLTUDevModel,_X:afLTUDevName,_Y:afLTUFirmwareVersion,_Z:afLTUMemoryUsage,_a:afLTUCpuUsage,_b:afLTUUptime,'afLTUStationTable':afLTUStationTable,'afLTUStationEntry':afLTUStationEntry,_v:afLTUStaTxRate,_w:afLTUStaRxRate,_x:afLTUStaTxCapacity,_y:afLTUStaRxCapacity,_z:afLTUStaRxPower0,_A0:afLTUStaRxPower1,_A1:afLTUStaIdealRxPower0,_A2:afLTUStaIdealRxPower1,_A3:afLTUStaRxPowerLevel0,_A4:afLTUStaRxPowerLevel1,_H:afLTUStaRemoteMac,_A5:afLTUStaRemoteDevModel,_A6:afLTUStaRemoteDevName,_A7:afLTUStaRemoteFirmwareVersion,_A8:afLTUStaRemoteTxEIRP,_A9:afLTUStaRemoteRxPower0,_AA:afLTUStaRemoteRxPower1,_AB:afLTUStaRemoteIdealRxPower0,_AC:afLTUStaRemoteIdealRxPower1,_AD:afLTUStaRemoteRxPowerLevel0,_AE:afLTUStaRemoteRxPowerLevel1,_AF:afLTUStaRemoteLatency,_AG:afLTUStaRemoteDistance,_AH:afLTUStaRemoteConnectionTime,_AI:afLTUStaRemoteLastIp,_AJ:afLTUStaRemoteRegistrationAttempts,'afLTUStats':afLTUStats,_c:afLTUTxBytes,_d:afLTUTxPps,_e:afLTURxBytes,_f:afLTURxPps,_g:afLTUConnected,'afLTUethStats':afLTUethStats,_h:afLTUethTxBytes,_i:afLTUethTxPps,_j:afLTUethRxBytes,_k:afLTUethRxPps,_l:afLTUethConnected,'afLTUgpsStats':afLTUgpsStats,_m:afLTUgpsStatus,_n:afLTUgpsDimensions,_o:afLTUgpsLat,_p:afLTUgpsLon,_q:afLTUgpsAltMeter,_r:afLTUgpsAltFeet,_s:afLTUgpsSatsVisible,_t:afLTUgpsSatsTracked,_u:afLTUgpsHDOP})