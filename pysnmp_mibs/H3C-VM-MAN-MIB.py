_k='h3cVMManClientVODFailNumThreshold'
_j='h3cVMManClientVODFailNum'
_i='h3cVMManClientLoginFailNumThreshold'
_h='h3cVMManClientLoginFailNum'
_g='h3cVMManReportContent'
_f='h3cVMManTemperatureThreshold'
_e='h3cVMManTemperature'
_d='h3cVMManHardDiskUsageThreshold'
_c='h3cVMManHardDiskUsage'
_b='h3cVMManMemUsageThreshold'
_a='h3cVMManMemUsage'
_Z='h3cVMManCpuUsageThreshold'
_Y='h3cVMManCpuUsage'
_X='h3cVMManPUExternalInputAlarmChannelID'
_W='h3cVMManClientVideoStreamDiscontinuityIntervalThreshold'
_V='h3cVMManClientVideoStreamDiscontinuityInterval'
_U='h3cVMManIPSANDevIP'
_T='h3cVMManClientVODEnd'
_S='h3cVMManClientVODStart'
_R='h3cVMManRegionCoordinateY2'
_Q='h3cVMManRegionCoordinateX2'
_P='h3cVMManRegionCoordinateY1'
_O='h3cVMManRegionCoordinateX1'
_N='h3cVMManClientStatPeriod'
_M='DisplayString'
_L='Unsigned32'
_K='read-only'
_J='h3cVMManUserName'
_I='h3cVMManClientIP'
_H='h3cVMManPUECVideoChannelName'
_G='h3cVMManRegDevName'
_F='h3cVMManRegDevIP'
_E='entPhysicalAssetID'
_D='ENTITY-MIB'
_C='accessible-for-notify'
_B='current'
_A='H3C-VM-MAN-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entPhysicalAssetID,=mibBuilder.importSymbols(_D,_E)
h3cSurveillanceMIB,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cSurveillanceMIB')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_L,'iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_M,'PhysAddress','TextualConvention')
h3cVMMan=ModuleIdentity((1,3,6,1,4,1,2011,10,9,1))
_H3cVMManMIBObjects_ObjectIdentity=ObjectIdentity
h3cVMManMIBObjects=_H3cVMManMIBObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,9,1,1))
class _H3cVMCapabilitySet_Type(Bits):namedValues=NamedValues(*(('cms',0),('css',1),('dm',2)))
_H3cVMCapabilitySet_Type.__name__='Bits'
_H3cVMCapabilitySet_Object=MibScalar
h3cVMCapabilitySet=_H3cVMCapabilitySet_Object((1,3,6,1,4,1,2011,10,9,1,1,1),_H3cVMCapabilitySet_Type())
h3cVMCapabilitySet.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cVMCapabilitySet.setStatus(_B)
_H3cVMStat_ObjectIdentity=ObjectIdentity
h3cVMStat=_H3cVMStat_ObjectIdentity((1,3,6,1,4,1,2011,10,9,1,1,2))
_H3cVMStatTotalConnEstablishRequests_Type=Counter32
_H3cVMStatTotalConnEstablishRequests_Object=MibScalar
h3cVMStatTotalConnEstablishRequests=_H3cVMStatTotalConnEstablishRequests_Object((1,3,6,1,4,1,2011,10,9,1,1,2,1),_H3cVMStatTotalConnEstablishRequests_Type())
h3cVMStatTotalConnEstablishRequests.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cVMStatTotalConnEstablishRequests.setStatus(_B)
_H3cVMStatSuccConnEstablishRequests_Type=Counter32
_H3cVMStatSuccConnEstablishRequests_Object=MibScalar
h3cVMStatSuccConnEstablishRequests=_H3cVMStatSuccConnEstablishRequests_Object((1,3,6,1,4,1,2011,10,9,1,1,2,2),_H3cVMStatSuccConnEstablishRequests_Type())
h3cVMStatSuccConnEstablishRequests.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cVMStatSuccConnEstablishRequests.setStatus(_B)
_H3cVMStatFailConnEstablishRequests_Type=Counter32
_H3cVMStatFailConnEstablishRequests_Object=MibScalar
h3cVMStatFailConnEstablishRequests=_H3cVMStatFailConnEstablishRequests_Object((1,3,6,1,4,1,2011,10,9,1,1,2,3),_H3cVMStatFailConnEstablishRequests_Type())
h3cVMStatFailConnEstablishRequests.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cVMStatFailConnEstablishRequests.setStatus(_B)
_H3cVMStatTotalConnReleaseRequests_Type=Counter32
_H3cVMStatTotalConnReleaseRequests_Object=MibScalar
h3cVMStatTotalConnReleaseRequests=_H3cVMStatTotalConnReleaseRequests_Object((1,3,6,1,4,1,2011,10,9,1,1,2,4),_H3cVMStatTotalConnReleaseRequests_Type())
h3cVMStatTotalConnReleaseRequests.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cVMStatTotalConnReleaseRequests.setStatus(_B)
_H3cVMStatSuccConnReleaseRequests_Type=Counter32
_H3cVMStatSuccConnReleaseRequests_Object=MibScalar
h3cVMStatSuccConnReleaseRequests=_H3cVMStatSuccConnReleaseRequests_Object((1,3,6,1,4,1,2011,10,9,1,1,2,5),_H3cVMStatSuccConnReleaseRequests_Type())
h3cVMStatSuccConnReleaseRequests.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cVMStatSuccConnReleaseRequests.setStatus(_B)
_H3cVMStatFailConnReleaseRequests_Type=Counter32
_H3cVMStatFailConnReleaseRequests_Object=MibScalar
h3cVMStatFailConnReleaseRequests=_H3cVMStatFailConnReleaseRequests_Object((1,3,6,1,4,1,2011,10,9,1,1,2,6),_H3cVMStatFailConnReleaseRequests_Type())
h3cVMStatFailConnReleaseRequests.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cVMStatFailConnReleaseRequests.setStatus(_B)
_H3cVMStatExceptionTerminationConn_Type=Counter32
_H3cVMStatExceptionTerminationConn_Object=MibScalar
h3cVMStatExceptionTerminationConn=_H3cVMStatExceptionTerminationConn_Object((1,3,6,1,4,1,2011,10,9,1,1,2,7),_H3cVMStatExceptionTerminationConn_Type())
h3cVMStatExceptionTerminationConn.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cVMStatExceptionTerminationConn.setStatus(_B)
_H3cVMManMIBTrap_ObjectIdentity=ObjectIdentity
h3cVMManMIBTrap=_H3cVMManMIBTrap_ObjectIdentity((1,3,6,1,4,1,2011,10,9,1,2))
_H3cVMManTrapPrex_ObjectIdentity=ObjectIdentity
h3cVMManTrapPrex=_H3cVMManTrapPrex_ObjectIdentity((1,3,6,1,4,1,2011,10,9,1,2,0))
_H3cVMManTrapObjects_ObjectIdentity=ObjectIdentity
h3cVMManTrapObjects=_H3cVMManTrapObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,9,1,2,1))
_H3cVMManIPSANDevIP_Type=IpAddress
_H3cVMManIPSANDevIP_Object=MibScalar
h3cVMManIPSANDevIP=_H3cVMManIPSANDevIP_Object((1,3,6,1,4,1,2011,10,9,1,2,1,1),_H3cVMManIPSANDevIP_Type())
h3cVMManIPSANDevIP.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVMManIPSANDevIP.setStatus(_B)
_H3cVMManRegDevIP_Type=IpAddress
_H3cVMManRegDevIP_Object=MibScalar
h3cVMManRegDevIP=_H3cVMManRegDevIP_Object((1,3,6,1,4,1,2011,10,9,1,2,1,2),_H3cVMManRegDevIP_Type())
h3cVMManRegDevIP.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVMManRegDevIP.setStatus(_B)
class _H3cVMManRegDevName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_H3cVMManRegDevName_Type.__name__=_M
_H3cVMManRegDevName_Object=MibScalar
h3cVMManRegDevName=_H3cVMManRegDevName_Object((1,3,6,1,4,1,2011,10,9,1,2,1,3),_H3cVMManRegDevName_Type())
h3cVMManRegDevName.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVMManRegDevName.setStatus(_B)
_H3cVMManRegionCoordinateX1_Type=Unsigned32
_H3cVMManRegionCoordinateX1_Object=MibScalar
h3cVMManRegionCoordinateX1=_H3cVMManRegionCoordinateX1_Object((1,3,6,1,4,1,2011,10,9,1,2,1,4),_H3cVMManRegionCoordinateX1_Type())
h3cVMManRegionCoordinateX1.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVMManRegionCoordinateX1.setStatus(_B)
_H3cVMManRegionCoordinateY1_Type=Unsigned32
_H3cVMManRegionCoordinateY1_Object=MibScalar
h3cVMManRegionCoordinateY1=_H3cVMManRegionCoordinateY1_Object((1,3,6,1,4,1,2011,10,9,1,2,1,5),_H3cVMManRegionCoordinateY1_Type())
h3cVMManRegionCoordinateY1.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVMManRegionCoordinateY1.setStatus(_B)
_H3cVMManRegionCoordinateX2_Type=Unsigned32
_H3cVMManRegionCoordinateX2_Object=MibScalar
h3cVMManRegionCoordinateX2=_H3cVMManRegionCoordinateX2_Object((1,3,6,1,4,1,2011,10,9,1,2,1,6),_H3cVMManRegionCoordinateX2_Type())
h3cVMManRegionCoordinateX2.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVMManRegionCoordinateX2.setStatus(_B)
_H3cVMManRegionCoordinateY2_Type=Unsigned32
_H3cVMManRegionCoordinateY2_Object=MibScalar
h3cVMManRegionCoordinateY2=_H3cVMManRegionCoordinateY2_Object((1,3,6,1,4,1,2011,10,9,1,2,1,7),_H3cVMManRegionCoordinateY2_Type())
h3cVMManRegionCoordinateY2.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVMManRegionCoordinateY2.setStatus(_B)
class _H3cVMManCpuUsage_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cVMManCpuUsage_Type.__name__=_L
_H3cVMManCpuUsage_Object=MibScalar
h3cVMManCpuUsage=_H3cVMManCpuUsage_Object((1,3,6,1,4,1,2011,10,9,1,2,1,8),_H3cVMManCpuUsage_Type())
h3cVMManCpuUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVMManCpuUsage.setStatus(_B)
class _H3cVMManCpuUsageThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cVMManCpuUsageThreshold_Type.__name__=_L
_H3cVMManCpuUsageThreshold_Object=MibScalar
h3cVMManCpuUsageThreshold=_H3cVMManCpuUsageThreshold_Object((1,3,6,1,4,1,2011,10,9,1,2,1,9),_H3cVMManCpuUsageThreshold_Type())
h3cVMManCpuUsageThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVMManCpuUsageThreshold.setStatus(_B)
class _H3cVMManMemUsage_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cVMManMemUsage_Type.__name__=_L
_H3cVMManMemUsage_Object=MibScalar
h3cVMManMemUsage=_H3cVMManMemUsage_Object((1,3,6,1,4,1,2011,10,9,1,2,1,10),_H3cVMManMemUsage_Type())
h3cVMManMemUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVMManMemUsage.setStatus(_B)
class _H3cVMManMemUsageThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cVMManMemUsageThreshold_Type.__name__=_L
_H3cVMManMemUsageThreshold_Object=MibScalar
h3cVMManMemUsageThreshold=_H3cVMManMemUsageThreshold_Object((1,3,6,1,4,1,2011,10,9,1,2,1,11),_H3cVMManMemUsageThreshold_Type())
h3cVMManMemUsageThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVMManMemUsageThreshold.setStatus(_B)
class _H3cVMManHardDiskUsage_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cVMManHardDiskUsage_Type.__name__=_L
_H3cVMManHardDiskUsage_Object=MibScalar
h3cVMManHardDiskUsage=_H3cVMManHardDiskUsage_Object((1,3,6,1,4,1,2011,10,9,1,2,1,12),_H3cVMManHardDiskUsage_Type())
h3cVMManHardDiskUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVMManHardDiskUsage.setStatus(_B)
class _H3cVMManHardDiskUsageThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cVMManHardDiskUsageThreshold_Type.__name__=_L
_H3cVMManHardDiskUsageThreshold_Object=MibScalar
h3cVMManHardDiskUsageThreshold=_H3cVMManHardDiskUsageThreshold_Object((1,3,6,1,4,1,2011,10,9,1,2,1,13),_H3cVMManHardDiskUsageThreshold_Type())
h3cVMManHardDiskUsageThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVMManHardDiskUsageThreshold.setStatus(_B)
_H3cVMManTemperature_Type=Integer32
_H3cVMManTemperature_Object=MibScalar
h3cVMManTemperature=_H3cVMManTemperature_Object((1,3,6,1,4,1,2011,10,9,1,2,1,14),_H3cVMManTemperature_Type())
h3cVMManTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVMManTemperature.setStatus(_B)
_H3cVMManTemperatureThreshold_Type=Integer32
_H3cVMManTemperatureThreshold_Object=MibScalar
h3cVMManTemperatureThreshold=_H3cVMManTemperatureThreshold_Object((1,3,6,1,4,1,2011,10,9,1,2,1,15),_H3cVMManTemperatureThreshold_Type())
h3cVMManTemperatureThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVMManTemperatureThreshold.setStatus(_B)
_H3cVMManClientIP_Type=IpAddress
_H3cVMManClientIP_Object=MibScalar
h3cVMManClientIP=_H3cVMManClientIP_Object((1,3,6,1,4,1,2011,10,9,1,2,1,16),_H3cVMManClientIP_Type())
h3cVMManClientIP.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVMManClientIP.setStatus(_B)
class _H3cVMManUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_H3cVMManUserName_Type.__name__=_M
_H3cVMManUserName_Object=MibScalar
h3cVMManUserName=_H3cVMManUserName_Object((1,3,6,1,4,1,2011,10,9,1,2,1,17),_H3cVMManUserName_Type())
h3cVMManUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVMManUserName.setStatus(_B)
class _H3cVMManReportContent_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_H3cVMManReportContent_Type.__name__=_M
_H3cVMManReportContent_Object=MibScalar
h3cVMManReportContent=_H3cVMManReportContent_Object((1,3,6,1,4,1,2011,10,9,1,2,1,18),_H3cVMManReportContent_Type())
h3cVMManReportContent.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVMManReportContent.setStatus(_B)
_H3cVMManClientVideoStreamDiscontinuityInterval_Type=Unsigned32
_H3cVMManClientVideoStreamDiscontinuityInterval_Object=MibScalar
h3cVMManClientVideoStreamDiscontinuityInterval=_H3cVMManClientVideoStreamDiscontinuityInterval_Object((1,3,6,1,4,1,2011,10,9,1,2,1,19),_H3cVMManClientVideoStreamDiscontinuityInterval_Type())
h3cVMManClientVideoStreamDiscontinuityInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVMManClientVideoStreamDiscontinuityInterval.setStatus(_B)
_H3cVMManClientVideoStreamDiscontinuityIntervalThreshold_Type=Unsigned32
_H3cVMManClientVideoStreamDiscontinuityIntervalThreshold_Object=MibScalar
h3cVMManClientVideoStreamDiscontinuityIntervalThreshold=_H3cVMManClientVideoStreamDiscontinuityIntervalThreshold_Object((1,3,6,1,4,1,2011,10,9,1,2,1,20),_H3cVMManClientVideoStreamDiscontinuityIntervalThreshold_Type())
h3cVMManClientVideoStreamDiscontinuityIntervalThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVMManClientVideoStreamDiscontinuityIntervalThreshold.setStatus(_B)
_H3cVMManClientStatPeriod_Type=Unsigned32
_H3cVMManClientStatPeriod_Object=MibScalar
h3cVMManClientStatPeriod=_H3cVMManClientStatPeriod_Object((1,3,6,1,4,1,2011,10,9,1,2,1,21),_H3cVMManClientStatPeriod_Type())
h3cVMManClientStatPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVMManClientStatPeriod.setStatus(_B)
_H3cVMManClientLoginFailNum_Type=Unsigned32
_H3cVMManClientLoginFailNum_Object=MibScalar
h3cVMManClientLoginFailNum=_H3cVMManClientLoginFailNum_Object((1,3,6,1,4,1,2011,10,9,1,2,1,22),_H3cVMManClientLoginFailNum_Type())
h3cVMManClientLoginFailNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVMManClientLoginFailNum.setStatus(_B)
_H3cVMManClientLoginFailNumThreshold_Type=Unsigned32
_H3cVMManClientLoginFailNumThreshold_Object=MibScalar
h3cVMManClientLoginFailNumThreshold=_H3cVMManClientLoginFailNumThreshold_Object((1,3,6,1,4,1,2011,10,9,1,2,1,23),_H3cVMManClientLoginFailNumThreshold_Type())
h3cVMManClientLoginFailNumThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVMManClientLoginFailNumThreshold.setStatus(_B)
_H3cVMManClientVODFailNum_Type=Unsigned32
_H3cVMManClientVODFailNum_Object=MibScalar
h3cVMManClientVODFailNum=_H3cVMManClientVODFailNum_Object((1,3,6,1,4,1,2011,10,9,1,2,1,24),_H3cVMManClientVODFailNum_Type())
h3cVMManClientVODFailNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVMManClientVODFailNum.setStatus(_B)
_H3cVMManClientVODFailNumThreshold_Type=Unsigned32
_H3cVMManClientVODFailNumThreshold_Object=MibScalar
h3cVMManClientVODFailNumThreshold=_H3cVMManClientVODFailNumThreshold_Object((1,3,6,1,4,1,2011,10,9,1,2,1,25),_H3cVMManClientVODFailNumThreshold_Type())
h3cVMManClientVODFailNumThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVMManClientVODFailNumThreshold.setStatus(_B)
_H3cVMManClientVODStart_Type=DateAndTime
_H3cVMManClientVODStart_Object=MibScalar
h3cVMManClientVODStart=_H3cVMManClientVODStart_Object((1,3,6,1,4,1,2011,10,9,1,2,1,26),_H3cVMManClientVODStart_Type())
h3cVMManClientVODStart.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVMManClientVODStart.setStatus(_B)
_H3cVMManClientVODEnd_Type=DateAndTime
_H3cVMManClientVODEnd_Object=MibScalar
h3cVMManClientVODEnd=_H3cVMManClientVODEnd_Object((1,3,6,1,4,1,2011,10,9,1,2,1,27),_H3cVMManClientVODEnd_Type())
h3cVMManClientVODEnd.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVMManClientVODEnd.setStatus(_B)
_H3cVMManPUExternalInputAlarmChannelID_Type=Unsigned32
_H3cVMManPUExternalInputAlarmChannelID_Object=MibScalar
h3cVMManPUExternalInputAlarmChannelID=_H3cVMManPUExternalInputAlarmChannelID_Object((1,3,6,1,4,1,2011,10,9,1,2,1,28),_H3cVMManPUExternalInputAlarmChannelID_Type())
h3cVMManPUExternalInputAlarmChannelID.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVMManPUExternalInputAlarmChannelID.setStatus(_B)
class _H3cVMManPUECVideoChannelName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_H3cVMManPUECVideoChannelName_Type.__name__=_M
_H3cVMManPUECVideoChannelName_Object=MibScalar
h3cVMManPUECVideoChannelName=_H3cVMManPUECVideoChannelName_Object((1,3,6,1,4,1,2011,10,9,1,2,1,29),_H3cVMManPUECVideoChannelName_Type())
h3cVMManPUECVideoChannelName.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVMManPUECVideoChannelName.setStatus(_B)
h3cVMManDeviceOnlineTrap=NotificationType((1,3,6,1,4,1,2011,10,9,1,2,0,1))
h3cVMManDeviceOnlineTrap.setObjects(*((_D,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:h3cVMManDeviceOnlineTrap.setStatus(_B)
h3cVMManDeviceOfflineTrap=NotificationType((1,3,6,1,4,1,2011,10,9,1,2,0,2))
h3cVMManDeviceOfflineTrap.setObjects(*((_D,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:h3cVMManDeviceOfflineTrap.setStatus(_B)
h3cVMManForwardDeviceExternalSemaphoreTrap=NotificationType((1,3,6,1,4,1,2011,10,9,1,2,0,3))
h3cVMManForwardDeviceExternalSemaphoreTrap.setObjects(*((_D,_E),(_A,_F),(_A,_G),(_A,_X)))
if mibBuilder.loadTexts:h3cVMManForwardDeviceExternalSemaphoreTrap.setStatus(_B)
h3cVMManForwardDeviceVideoLossTrap=NotificationType((1,3,6,1,4,1,2011,10,9,1,2,0,4))
h3cVMManForwardDeviceVideoLossTrap.setObjects(*((_D,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:h3cVMManForwardDeviceVideoLossTrap.setStatus(_B)
h3cVMManForwardDeviceVideoRecoverTrap=NotificationType((1,3,6,1,4,1,2011,10,9,1,2,0,5))
h3cVMManForwardDeviceVideoRecoverTrap.setObjects(*((_D,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:h3cVMManForwardDeviceVideoRecoverTrap.setStatus(_B)
h3cVMManForwardDeviceMotionDetectTrap=NotificationType((1,3,6,1,4,1,2011,10,9,1,2,0,6))
h3cVMManForwardDeviceMotionDetectTrap.setObjects(*((_D,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_O),(_A,_P),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:h3cVMManForwardDeviceMotionDetectTrap.setStatus(_B)
h3cVMManForwardDeviceCoverTrap=NotificationType((1,3,6,1,4,1,2011,10,9,1,2,0,7))
h3cVMManForwardDeviceCoverTrap.setObjects(*((_D,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_O),(_A,_P),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:h3cVMManForwardDeviceCoverTrap.setStatus(_B)
h3cVMManForwardDeviceCpuUsageThresholdTrap=NotificationType((1,3,6,1,4,1,2011,10,9,1,2,0,8))
h3cVMManForwardDeviceCpuUsageThresholdTrap.setObjects(*((_D,_E),(_A,_F),(_A,_G),(_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:h3cVMManForwardDeviceCpuUsageThresholdTrap.setStatus(_B)
h3cVMManForwardDeviceMemUsageThresholdTrap=NotificationType((1,3,6,1,4,1,2011,10,9,1,2,0,9))
h3cVMManForwardDeviceMemUsageThresholdTrap.setObjects(*((_D,_E),(_A,_F),(_A,_G),(_A,_a),(_A,_b)))
if mibBuilder.loadTexts:h3cVMManForwardDeviceMemUsageThresholdTrap.setStatus(_B)
h3cVMManForwardDeviceHardDiskUsageThresholdTrap=NotificationType((1,3,6,1,4,1,2011,10,9,1,2,0,10))
h3cVMManForwardDeviceHardDiskUsageThresholdTrap.setObjects(*((_D,_E),(_A,_F),(_A,_G),(_A,_c),(_A,_d)))
if mibBuilder.loadTexts:h3cVMManForwardDeviceHardDiskUsageThresholdTrap.setStatus(_B)
h3cVMManForwardDeviceTemperatureThresholdTrap=NotificationType((1,3,6,1,4,1,2011,10,9,1,2,0,11))
h3cVMManForwardDeviceTemperatureThresholdTrap.setObjects(*((_D,_E),(_A,_F),(_A,_G),(_A,_e),(_A,_f)))
if mibBuilder.loadTexts:h3cVMManForwardDeviceTemperatureThresholdTrap.setStatus(_B)
h3cVMManForwardDeviceStartKinescopeTrap=NotificationType((1,3,6,1,4,1,2011,10,9,1,2,0,12))
h3cVMManForwardDeviceStartKinescopeTrap.setObjects(*((_D,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:h3cVMManForwardDeviceStartKinescopeTrap.setStatus(_B)
h3cVMManForwardDeviceStopKinescopeTrap=NotificationType((1,3,6,1,4,1,2011,10,9,1,2,0,13))
h3cVMManForwardDeviceStopKinescopeTrap.setObjects(*((_D,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:h3cVMManForwardDeviceStopKinescopeTrap.setStatus(_B)
h3cVMManClientReportTrap=NotificationType((1,3,6,1,4,1,2011,10,9,1,2,0,14))
h3cVMManClientReportTrap.setObjects(*((_D,_E),(_A,_I),(_A,_J),(_A,_g)))
if mibBuilder.loadTexts:h3cVMManClientReportTrap.setStatus(_B)
h3cVMManClientRealtimeSurveillanceNoVideoTrap=NotificationType((1,3,6,1,4,1,2011,10,9,1,2,0,15))
h3cVMManClientRealtimeSurveillanceNoVideoTrap.setObjects(*((_D,_E),(_A,_I),(_A,_J),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:h3cVMManClientRealtimeSurveillanceNoVideoTrap.setStatus(_B)
h3cVMManClientVODNoVideoTrap=NotificationType((1,3,6,1,4,1,2011,10,9,1,2,0,16))
h3cVMManClientVODNoVideoTrap.setObjects(*((_D,_E),(_A,_I),(_A,_J),(_A,_F),(_A,_G),(_A,_H),(_A,_S),(_A,_T),(_A,_U)))
if mibBuilder.loadTexts:h3cVMManClientVODNoVideoTrap.setStatus(_B)
h3cVMManClientRealtimeSurveillanceVideoStreamDiscontinuityTrap=NotificationType((1,3,6,1,4,1,2011,10,9,1,2,0,17))
h3cVMManClientRealtimeSurveillanceVideoStreamDiscontinuityTrap.setObjects(*((_D,_E),(_A,_I),(_A,_J),(_A,_F),(_A,_G),(_A,_H),(_A,_V),(_A,_W),(_A,_N)))
if mibBuilder.loadTexts:h3cVMManClientRealtimeSurveillanceVideoStreamDiscontinuityTrap.setStatus(_B)
h3cVMManClientVODVideoStreamDiscontinuityTrap=NotificationType((1,3,6,1,4,1,2011,10,9,1,2,0,18))
h3cVMManClientVODVideoStreamDiscontinuityTrap.setObjects(*((_D,_E),(_A,_I),(_A,_J),(_A,_F),(_A,_G),(_A,_H),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_N)))
if mibBuilder.loadTexts:h3cVMManClientVODVideoStreamDiscontinuityTrap.setStatus(_B)
h3cVMManClientCtlConnExceptionTerminationTrap=NotificationType((1,3,6,1,4,1,2011,10,9,1,2,0,19))
h3cVMManClientCtlConnExceptionTerminationTrap.setObjects(*((_D,_E),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:h3cVMManClientCtlConnExceptionTerminationTrap.setStatus(_B)
h3cVMManClientFrequencyLoginFailTrap=NotificationType((1,3,6,1,4,1,2011,10,9,1,2,0,20))
h3cVMManClientFrequencyLoginFailTrap.setObjects(*((_D,_E),(_A,_I),(_A,_J),(_A,_h),(_A,_i),(_A,_N)))
if mibBuilder.loadTexts:h3cVMManClientFrequencyLoginFailTrap.setStatus(_B)
h3cVMManClientFrequencyVODFailTrap=NotificationType((1,3,6,1,4,1,2011,10,9,1,2,0,21))
h3cVMManClientFrequencyVODFailTrap.setObjects(*((_D,_E),(_A,_I),(_A,_J),(_A,_j),(_A,_k),(_A,_N)))
if mibBuilder.loadTexts:h3cVMManClientFrequencyVODFailTrap.setStatus(_B)
h3cVMManDMECDisobeyStorageScheduleTrap=NotificationType((1,3,6,1,4,1,2011,10,9,1,2,0,22))
h3cVMManDMECDisobeyStorageScheduleTrap.setObjects(*((_D,_E),(_A,_F),(_A,_H)))
if mibBuilder.loadTexts:h3cVMManDMECDisobeyStorageScheduleTrap.setStatus(_B)
h3cVMManDMECDisobeyStorageScheduleRecoverTrap=NotificationType((1,3,6,1,4,1,2011,10,9,1,2,0,23))
h3cVMManDMECDisobeyStorageScheduleRecoverTrap.setObjects(*((_D,_E),(_A,_F),(_A,_H)))
if mibBuilder.loadTexts:h3cVMManDMECDisobeyStorageScheduleRecoverTrap.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'h3cVMMan':h3cVMMan,'h3cVMManMIBObjects':h3cVMManMIBObjects,'h3cVMCapabilitySet':h3cVMCapabilitySet,'h3cVMStat':h3cVMStat,'h3cVMStatTotalConnEstablishRequests':h3cVMStatTotalConnEstablishRequests,'h3cVMStatSuccConnEstablishRequests':h3cVMStatSuccConnEstablishRequests,'h3cVMStatFailConnEstablishRequests':h3cVMStatFailConnEstablishRequests,'h3cVMStatTotalConnReleaseRequests':h3cVMStatTotalConnReleaseRequests,'h3cVMStatSuccConnReleaseRequests':h3cVMStatSuccConnReleaseRequests,'h3cVMStatFailConnReleaseRequests':h3cVMStatFailConnReleaseRequests,'h3cVMStatExceptionTerminationConn':h3cVMStatExceptionTerminationConn,'h3cVMManMIBTrap':h3cVMManMIBTrap,'h3cVMManTrapPrex':h3cVMManTrapPrex,'h3cVMManDeviceOnlineTrap':h3cVMManDeviceOnlineTrap,'h3cVMManDeviceOfflineTrap':h3cVMManDeviceOfflineTrap,'h3cVMManForwardDeviceExternalSemaphoreTrap':h3cVMManForwardDeviceExternalSemaphoreTrap,'h3cVMManForwardDeviceVideoLossTrap':h3cVMManForwardDeviceVideoLossTrap,'h3cVMManForwardDeviceVideoRecoverTrap':h3cVMManForwardDeviceVideoRecoverTrap,'h3cVMManForwardDeviceMotionDetectTrap':h3cVMManForwardDeviceMotionDetectTrap,'h3cVMManForwardDeviceCoverTrap':h3cVMManForwardDeviceCoverTrap,'h3cVMManForwardDeviceCpuUsageThresholdTrap':h3cVMManForwardDeviceCpuUsageThresholdTrap,'h3cVMManForwardDeviceMemUsageThresholdTrap':h3cVMManForwardDeviceMemUsageThresholdTrap,'h3cVMManForwardDeviceHardDiskUsageThresholdTrap':h3cVMManForwardDeviceHardDiskUsageThresholdTrap,'h3cVMManForwardDeviceTemperatureThresholdTrap':h3cVMManForwardDeviceTemperatureThresholdTrap,'h3cVMManForwardDeviceStartKinescopeTrap':h3cVMManForwardDeviceStartKinescopeTrap,'h3cVMManForwardDeviceStopKinescopeTrap':h3cVMManForwardDeviceStopKinescopeTrap,'h3cVMManClientReportTrap':h3cVMManClientReportTrap,'h3cVMManClientRealtimeSurveillanceNoVideoTrap':h3cVMManClientRealtimeSurveillanceNoVideoTrap,'h3cVMManClientVODNoVideoTrap':h3cVMManClientVODNoVideoTrap,'h3cVMManClientRealtimeSurveillanceVideoStreamDiscontinuityTrap':h3cVMManClientRealtimeSurveillanceVideoStreamDiscontinuityTrap,'h3cVMManClientVODVideoStreamDiscontinuityTrap':h3cVMManClientVODVideoStreamDiscontinuityTrap,'h3cVMManClientCtlConnExceptionTerminationTrap':h3cVMManClientCtlConnExceptionTerminationTrap,'h3cVMManClientFrequencyLoginFailTrap':h3cVMManClientFrequencyLoginFailTrap,'h3cVMManClientFrequencyVODFailTrap':h3cVMManClientFrequencyVODFailTrap,'h3cVMManDMECDisobeyStorageScheduleTrap':h3cVMManDMECDisobeyStorageScheduleTrap,'h3cVMManDMECDisobeyStorageScheduleRecoverTrap':h3cVMManDMECDisobeyStorageScheduleRecoverTrap,'h3cVMManTrapObjects':h3cVMManTrapObjects,_U:h3cVMManIPSANDevIP,_F:h3cVMManRegDevIP,_G:h3cVMManRegDevName,_O:h3cVMManRegionCoordinateX1,_P:h3cVMManRegionCoordinateY1,_Q:h3cVMManRegionCoordinateX2,_R:h3cVMManRegionCoordinateY2,_Y:h3cVMManCpuUsage,_Z:h3cVMManCpuUsageThreshold,_a:h3cVMManMemUsage,_b:h3cVMManMemUsageThreshold,_c:h3cVMManHardDiskUsage,_d:h3cVMManHardDiskUsageThreshold,_e:h3cVMManTemperature,_f:h3cVMManTemperatureThreshold,_I:h3cVMManClientIP,_J:h3cVMManUserName,_g:h3cVMManReportContent,_V:h3cVMManClientVideoStreamDiscontinuityInterval,_W:h3cVMManClientVideoStreamDiscontinuityIntervalThreshold,_N:h3cVMManClientStatPeriod,_h:h3cVMManClientLoginFailNum,_i:h3cVMManClientLoginFailNumThreshold,_j:h3cVMManClientVODFailNum,_k:h3cVMManClientVODFailNumThreshold,_S:h3cVMManClientVODStart,_T:h3cVMManClientVODEnd,_X:h3cVMManPUExternalInputAlarmChannelID,_H:h3cVMManPUECVideoChannelName})