_q='rtpConfigBasicGroupVer1'
_p='rtpStatsBasicGroupVer1'
_o='rtpConfigBasePort'
_n='rtpStatsCumulatedTotalLatencyAvg'
_m='rtpStatsCumulatedTotalLatencyMax'
_l='rtpStatsCumulatedTotalLatencyMin'
_k='rtpStatsCumulatedTotalInterarrivalJitterAvg'
_j='rtpStatsCumulatedTotalInterarrivalJitterMax'
_i='rtpStatsCumulatedTotalInterarrivalJitterMin'
_h='rtpStatsCumulatedTotalPercentPacketsLost'
_g='rtpStatsCumulatedTotalPacketsLost'
_f='rtpStatsCumulatedTotalPacketsReceived'
_e='rtpStatsCumulatedTotalPacketsTransmitted'
_d='rtpStatsCumulatedTotalOctetsReceived'
_c='rtpStatsCumulatedTotalOctetsTransmitted'
_b='rtpStatsCurrentTotalLatencyAvg'
_a='rtpStatsCurrentTotalLatencyMax'
_Z='rtpStatsCurrentTotalLatencyMin'
_Y='rtpStatsCurrentTotalInterarrivalJitterAvg'
_X='rtpStatsCurrentTotalInterarrivalJitterMax'
_W='rtpStatsCurrentTotalInterarrivalJitterMin'
_V='rtpStatsCurrentTotalPercentPacketsLost'
_U='rtpStatsCurrentTotalPacketsLost'
_T='rtpStatsCurrentTotalPacketsReceived'
_S='rtpStatsCurrentTotalPacketsTransmitted'
_R='rtpStatsCurrentTotalOctetsReceived'
_Q='rtpStatsCurrentTotalOctetsTransmitted'
_P='rtpStatsLastConnLatencyAvg'
_O='rtpStatsLastConnLatencyMax'
_N='rtpStatsLastConnLatencyMin'
_M='rtpStatsLastConnInterarrivalJitterAvg'
_L='rtpStatsLastConnInterarrivalJitterMax'
_K='rtpStatsLastConnInterarrivalJitterMin'
_J='rtpStatsLastConnPercentPacketsLost'
_I='rtpStatsLastConnNumberPacketsLost'
_H='rtpStatsLastConnNumberPacketsReceived'
_G='rtpStatsLastConnNumberPacketsTransmitted'
_F='rtpStatsLastConnNumberOctetsReceived'
_E='rtpStatsLastConnNumberOctetsTransmitted'
_D='Unsigned32'
_C='read-only'
_B='MX-RTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mediatrixConfig,mediatrixMgmt=mibBuilder.importSymbols('MX-SMI','mediatrixConfig','mediatrixMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
rtpMIB=ModuleIdentity((1,3,6,1,4,1,4935,10,50))
if mibBuilder.loadTexts:rtpMIB.setRevisions(('1903-10-27 00:00',))
_RtpMIBObjects_ObjectIdentity=ObjectIdentity
rtpMIBObjects=_RtpMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,10,50,1))
_RtpStats_ObjectIdentity=ObjectIdentity
rtpStats=_RtpStats_ObjectIdentity((1,3,6,1,4,1,4935,10,50,1,2))
_RtpStatsLastConnectionStatistics_ObjectIdentity=ObjectIdentity
rtpStatsLastConnectionStatistics=_RtpStatsLastConnectionStatistics_ObjectIdentity((1,3,6,1,4,1,4935,10,50,1,2,5))
_RtpStatsLastConnNumberOctetsTransmitted_Type=Unsigned32
_RtpStatsLastConnNumberOctetsTransmitted_Object=MibScalar
rtpStatsLastConnNumberOctetsTransmitted=_RtpStatsLastConnNumberOctetsTransmitted_Object((1,3,6,1,4,1,4935,10,50,1,2,5,1),_RtpStatsLastConnNumberOctetsTransmitted_Type())
rtpStatsLastConnNumberOctetsTransmitted.setMaxAccess(_C)
if mibBuilder.loadTexts:rtpStatsLastConnNumberOctetsTransmitted.setStatus(_A)
_RtpStatsLastConnNumberOctetsReceived_Type=Unsigned32
_RtpStatsLastConnNumberOctetsReceived_Object=MibScalar
rtpStatsLastConnNumberOctetsReceived=_RtpStatsLastConnNumberOctetsReceived_Object((1,3,6,1,4,1,4935,10,50,1,2,5,2),_RtpStatsLastConnNumberOctetsReceived_Type())
rtpStatsLastConnNumberOctetsReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:rtpStatsLastConnNumberOctetsReceived.setStatus(_A)
_RtpStatsLastConnNumberPacketsTransmitted_Type=Unsigned32
_RtpStatsLastConnNumberPacketsTransmitted_Object=MibScalar
rtpStatsLastConnNumberPacketsTransmitted=_RtpStatsLastConnNumberPacketsTransmitted_Object((1,3,6,1,4,1,4935,10,50,1,2,5,3),_RtpStatsLastConnNumberPacketsTransmitted_Type())
rtpStatsLastConnNumberPacketsTransmitted.setMaxAccess(_C)
if mibBuilder.loadTexts:rtpStatsLastConnNumberPacketsTransmitted.setStatus(_A)
_RtpStatsLastConnNumberPacketsReceived_Type=Unsigned32
_RtpStatsLastConnNumberPacketsReceived_Object=MibScalar
rtpStatsLastConnNumberPacketsReceived=_RtpStatsLastConnNumberPacketsReceived_Object((1,3,6,1,4,1,4935,10,50,1,2,5,4),_RtpStatsLastConnNumberPacketsReceived_Type())
rtpStatsLastConnNumberPacketsReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:rtpStatsLastConnNumberPacketsReceived.setStatus(_A)
_RtpStatsLastConnNumberPacketsLost_Type=Integer32
_RtpStatsLastConnNumberPacketsLost_Object=MibScalar
rtpStatsLastConnNumberPacketsLost=_RtpStatsLastConnNumberPacketsLost_Object((1,3,6,1,4,1,4935,10,50,1,2,5,5),_RtpStatsLastConnNumberPacketsLost_Type())
rtpStatsLastConnNumberPacketsLost.setMaxAccess(_C)
if mibBuilder.loadTexts:rtpStatsLastConnNumberPacketsLost.setStatus(_A)
class _RtpStatsLastConnPercentPacketsLost_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_RtpStatsLastConnPercentPacketsLost_Type.__name__=_D
_RtpStatsLastConnPercentPacketsLost_Object=MibScalar
rtpStatsLastConnPercentPacketsLost=_RtpStatsLastConnPercentPacketsLost_Object((1,3,6,1,4,1,4935,10,50,1,2,5,6),_RtpStatsLastConnPercentPacketsLost_Type())
rtpStatsLastConnPercentPacketsLost.setMaxAccess(_C)
if mibBuilder.loadTexts:rtpStatsLastConnPercentPacketsLost.setStatus(_A)
_RtpStatsLastConnInterarrivalJitterMin_Type=Unsigned32
_RtpStatsLastConnInterarrivalJitterMin_Object=MibScalar
rtpStatsLastConnInterarrivalJitterMin=_RtpStatsLastConnInterarrivalJitterMin_Object((1,3,6,1,4,1,4935,10,50,1,2,5,7),_RtpStatsLastConnInterarrivalJitterMin_Type())
rtpStatsLastConnInterarrivalJitterMin.setMaxAccess(_C)
if mibBuilder.loadTexts:rtpStatsLastConnInterarrivalJitterMin.setStatus(_A)
_RtpStatsLastConnInterarrivalJitterMax_Type=Unsigned32
_RtpStatsLastConnInterarrivalJitterMax_Object=MibScalar
rtpStatsLastConnInterarrivalJitterMax=_RtpStatsLastConnInterarrivalJitterMax_Object((1,3,6,1,4,1,4935,10,50,1,2,5,8),_RtpStatsLastConnInterarrivalJitterMax_Type())
rtpStatsLastConnInterarrivalJitterMax.setMaxAccess(_C)
if mibBuilder.loadTexts:rtpStatsLastConnInterarrivalJitterMax.setStatus(_A)
_RtpStatsLastConnInterarrivalJitterAvg_Type=Unsigned32
_RtpStatsLastConnInterarrivalJitterAvg_Object=MibScalar
rtpStatsLastConnInterarrivalJitterAvg=_RtpStatsLastConnInterarrivalJitterAvg_Object((1,3,6,1,4,1,4935,10,50,1,2,5,9),_RtpStatsLastConnInterarrivalJitterAvg_Type())
rtpStatsLastConnInterarrivalJitterAvg.setMaxAccess(_C)
if mibBuilder.loadTexts:rtpStatsLastConnInterarrivalJitterAvg.setStatus(_A)
_RtpStatsLastConnLatencyMin_Type=Unsigned32
_RtpStatsLastConnLatencyMin_Object=MibScalar
rtpStatsLastConnLatencyMin=_RtpStatsLastConnLatencyMin_Object((1,3,6,1,4,1,4935,10,50,1,2,5,10),_RtpStatsLastConnLatencyMin_Type())
rtpStatsLastConnLatencyMin.setMaxAccess(_C)
if mibBuilder.loadTexts:rtpStatsLastConnLatencyMin.setStatus(_A)
_RtpStatsLastConnLatencyMax_Type=Unsigned32
_RtpStatsLastConnLatencyMax_Object=MibScalar
rtpStatsLastConnLatencyMax=_RtpStatsLastConnLatencyMax_Object((1,3,6,1,4,1,4935,10,50,1,2,5,11),_RtpStatsLastConnLatencyMax_Type())
rtpStatsLastConnLatencyMax.setMaxAccess(_C)
if mibBuilder.loadTexts:rtpStatsLastConnLatencyMax.setStatus(_A)
_RtpStatsLastConnLatencyAvg_Type=Unsigned32
_RtpStatsLastConnLatencyAvg_Object=MibScalar
rtpStatsLastConnLatencyAvg=_RtpStatsLastConnLatencyAvg_Object((1,3,6,1,4,1,4935,10,50,1,2,5,12),_RtpStatsLastConnLatencyAvg_Type())
rtpStatsLastConnLatencyAvg.setMaxAccess(_C)
if mibBuilder.loadTexts:rtpStatsLastConnLatencyAvg.setStatus(_A)
_RtpStatsCurrentStatistics_ObjectIdentity=ObjectIdentity
rtpStatsCurrentStatistics=_RtpStatsCurrentStatistics_ObjectIdentity((1,3,6,1,4,1,4935,10,50,1,2,10))
_RtpStatsCurrentTotalOctetsTransmitted_Type=Unsigned32
_RtpStatsCurrentTotalOctetsTransmitted_Object=MibScalar
rtpStatsCurrentTotalOctetsTransmitted=_RtpStatsCurrentTotalOctetsTransmitted_Object((1,3,6,1,4,1,4935,10,50,1,2,10,1),_RtpStatsCurrentTotalOctetsTransmitted_Type())
rtpStatsCurrentTotalOctetsTransmitted.setMaxAccess(_C)
if mibBuilder.loadTexts:rtpStatsCurrentTotalOctetsTransmitted.setStatus(_A)
_RtpStatsCurrentTotalOctetsReceived_Type=Unsigned32
_RtpStatsCurrentTotalOctetsReceived_Object=MibScalar
rtpStatsCurrentTotalOctetsReceived=_RtpStatsCurrentTotalOctetsReceived_Object((1,3,6,1,4,1,4935,10,50,1,2,10,2),_RtpStatsCurrentTotalOctetsReceived_Type())
rtpStatsCurrentTotalOctetsReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:rtpStatsCurrentTotalOctetsReceived.setStatus(_A)
_RtpStatsCurrentTotalPacketsTransmitted_Type=Unsigned32
_RtpStatsCurrentTotalPacketsTransmitted_Object=MibScalar
rtpStatsCurrentTotalPacketsTransmitted=_RtpStatsCurrentTotalPacketsTransmitted_Object((1,3,6,1,4,1,4935,10,50,1,2,10,3),_RtpStatsCurrentTotalPacketsTransmitted_Type())
rtpStatsCurrentTotalPacketsTransmitted.setMaxAccess(_C)
if mibBuilder.loadTexts:rtpStatsCurrentTotalPacketsTransmitted.setStatus(_A)
_RtpStatsCurrentTotalPacketsReceived_Type=Unsigned32
_RtpStatsCurrentTotalPacketsReceived_Object=MibScalar
rtpStatsCurrentTotalPacketsReceived=_RtpStatsCurrentTotalPacketsReceived_Object((1,3,6,1,4,1,4935,10,50,1,2,10,4),_RtpStatsCurrentTotalPacketsReceived_Type())
rtpStatsCurrentTotalPacketsReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:rtpStatsCurrentTotalPacketsReceived.setStatus(_A)
_RtpStatsCurrentTotalPacketsLost_Type=Integer32
_RtpStatsCurrentTotalPacketsLost_Object=MibScalar
rtpStatsCurrentTotalPacketsLost=_RtpStatsCurrentTotalPacketsLost_Object((1,3,6,1,4,1,4935,10,50,1,2,10,5),_RtpStatsCurrentTotalPacketsLost_Type())
rtpStatsCurrentTotalPacketsLost.setMaxAccess(_C)
if mibBuilder.loadTexts:rtpStatsCurrentTotalPacketsLost.setStatus(_A)
class _RtpStatsCurrentTotalPercentPacketsLost_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_RtpStatsCurrentTotalPercentPacketsLost_Type.__name__=_D
_RtpStatsCurrentTotalPercentPacketsLost_Object=MibScalar
rtpStatsCurrentTotalPercentPacketsLost=_RtpStatsCurrentTotalPercentPacketsLost_Object((1,3,6,1,4,1,4935,10,50,1,2,10,6),_RtpStatsCurrentTotalPercentPacketsLost_Type())
rtpStatsCurrentTotalPercentPacketsLost.setMaxAccess(_C)
if mibBuilder.loadTexts:rtpStatsCurrentTotalPercentPacketsLost.setStatus(_A)
_RtpStatsCurrentTotalInterarrivalJitterMin_Type=Unsigned32
_RtpStatsCurrentTotalInterarrivalJitterMin_Object=MibScalar
rtpStatsCurrentTotalInterarrivalJitterMin=_RtpStatsCurrentTotalInterarrivalJitterMin_Object((1,3,6,1,4,1,4935,10,50,1,2,10,7),_RtpStatsCurrentTotalInterarrivalJitterMin_Type())
rtpStatsCurrentTotalInterarrivalJitterMin.setMaxAccess(_C)
if mibBuilder.loadTexts:rtpStatsCurrentTotalInterarrivalJitterMin.setStatus(_A)
_RtpStatsCurrentTotalInterarrivalJitterMax_Type=Unsigned32
_RtpStatsCurrentTotalInterarrivalJitterMax_Object=MibScalar
rtpStatsCurrentTotalInterarrivalJitterMax=_RtpStatsCurrentTotalInterarrivalJitterMax_Object((1,3,6,1,4,1,4935,10,50,1,2,10,8),_RtpStatsCurrentTotalInterarrivalJitterMax_Type())
rtpStatsCurrentTotalInterarrivalJitterMax.setMaxAccess(_C)
if mibBuilder.loadTexts:rtpStatsCurrentTotalInterarrivalJitterMax.setStatus(_A)
_RtpStatsCurrentTotalInterarrivalJitterAvg_Type=Unsigned32
_RtpStatsCurrentTotalInterarrivalJitterAvg_Object=MibScalar
rtpStatsCurrentTotalInterarrivalJitterAvg=_RtpStatsCurrentTotalInterarrivalJitterAvg_Object((1,3,6,1,4,1,4935,10,50,1,2,10,9),_RtpStatsCurrentTotalInterarrivalJitterAvg_Type())
rtpStatsCurrentTotalInterarrivalJitterAvg.setMaxAccess(_C)
if mibBuilder.loadTexts:rtpStatsCurrentTotalInterarrivalJitterAvg.setStatus(_A)
_RtpStatsCurrentTotalLatencyMin_Type=Unsigned32
_RtpStatsCurrentTotalLatencyMin_Object=MibScalar
rtpStatsCurrentTotalLatencyMin=_RtpStatsCurrentTotalLatencyMin_Object((1,3,6,1,4,1,4935,10,50,1,2,10,10),_RtpStatsCurrentTotalLatencyMin_Type())
rtpStatsCurrentTotalLatencyMin.setMaxAccess(_C)
if mibBuilder.loadTexts:rtpStatsCurrentTotalLatencyMin.setStatus(_A)
_RtpStatsCurrentTotalLatencyMax_Type=Unsigned32
_RtpStatsCurrentTotalLatencyMax_Object=MibScalar
rtpStatsCurrentTotalLatencyMax=_RtpStatsCurrentTotalLatencyMax_Object((1,3,6,1,4,1,4935,10,50,1,2,10,11),_RtpStatsCurrentTotalLatencyMax_Type())
rtpStatsCurrentTotalLatencyMax.setMaxAccess(_C)
if mibBuilder.loadTexts:rtpStatsCurrentTotalLatencyMax.setStatus(_A)
_RtpStatsCurrentTotalLatencyAvg_Type=Unsigned32
_RtpStatsCurrentTotalLatencyAvg_Object=MibScalar
rtpStatsCurrentTotalLatencyAvg=_RtpStatsCurrentTotalLatencyAvg_Object((1,3,6,1,4,1,4935,10,50,1,2,10,12),_RtpStatsCurrentTotalLatencyAvg_Type())
rtpStatsCurrentTotalLatencyAvg.setMaxAccess(_C)
if mibBuilder.loadTexts:rtpStatsCurrentTotalLatencyAvg.setStatus(_A)
_RtpStatsCumulatedStatistics_ObjectIdentity=ObjectIdentity
rtpStatsCumulatedStatistics=_RtpStatsCumulatedStatistics_ObjectIdentity((1,3,6,1,4,1,4935,10,50,1,2,15))
_RtpStatsCumulatedTotalOctetsTransmitted_Type=Unsigned32
_RtpStatsCumulatedTotalOctetsTransmitted_Object=MibScalar
rtpStatsCumulatedTotalOctetsTransmitted=_RtpStatsCumulatedTotalOctetsTransmitted_Object((1,3,6,1,4,1,4935,10,50,1,2,15,1),_RtpStatsCumulatedTotalOctetsTransmitted_Type())
rtpStatsCumulatedTotalOctetsTransmitted.setMaxAccess(_C)
if mibBuilder.loadTexts:rtpStatsCumulatedTotalOctetsTransmitted.setStatus(_A)
_RtpStatsCumulatedTotalOctetsReceived_Type=Unsigned32
_RtpStatsCumulatedTotalOctetsReceived_Object=MibScalar
rtpStatsCumulatedTotalOctetsReceived=_RtpStatsCumulatedTotalOctetsReceived_Object((1,3,6,1,4,1,4935,10,50,1,2,15,2),_RtpStatsCumulatedTotalOctetsReceived_Type())
rtpStatsCumulatedTotalOctetsReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:rtpStatsCumulatedTotalOctetsReceived.setStatus(_A)
_RtpStatsCumulatedTotalPacketsTransmitted_Type=Unsigned32
_RtpStatsCumulatedTotalPacketsTransmitted_Object=MibScalar
rtpStatsCumulatedTotalPacketsTransmitted=_RtpStatsCumulatedTotalPacketsTransmitted_Object((1,3,6,1,4,1,4935,10,50,1,2,15,3),_RtpStatsCumulatedTotalPacketsTransmitted_Type())
rtpStatsCumulatedTotalPacketsTransmitted.setMaxAccess(_C)
if mibBuilder.loadTexts:rtpStatsCumulatedTotalPacketsTransmitted.setStatus(_A)
_RtpStatsCumulatedTotalPacketsReceived_Type=Unsigned32
_RtpStatsCumulatedTotalPacketsReceived_Object=MibScalar
rtpStatsCumulatedTotalPacketsReceived=_RtpStatsCumulatedTotalPacketsReceived_Object((1,3,6,1,4,1,4935,10,50,1,2,15,4),_RtpStatsCumulatedTotalPacketsReceived_Type())
rtpStatsCumulatedTotalPacketsReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:rtpStatsCumulatedTotalPacketsReceived.setStatus(_A)
_RtpStatsCumulatedTotalPacketsLost_Type=Integer32
_RtpStatsCumulatedTotalPacketsLost_Object=MibScalar
rtpStatsCumulatedTotalPacketsLost=_RtpStatsCumulatedTotalPacketsLost_Object((1,3,6,1,4,1,4935,10,50,1,2,15,5),_RtpStatsCumulatedTotalPacketsLost_Type())
rtpStatsCumulatedTotalPacketsLost.setMaxAccess(_C)
if mibBuilder.loadTexts:rtpStatsCumulatedTotalPacketsLost.setStatus(_A)
class _RtpStatsCumulatedTotalPercentPacketsLost_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_RtpStatsCumulatedTotalPercentPacketsLost_Type.__name__=_D
_RtpStatsCumulatedTotalPercentPacketsLost_Object=MibScalar
rtpStatsCumulatedTotalPercentPacketsLost=_RtpStatsCumulatedTotalPercentPacketsLost_Object((1,3,6,1,4,1,4935,10,50,1,2,15,6),_RtpStatsCumulatedTotalPercentPacketsLost_Type())
rtpStatsCumulatedTotalPercentPacketsLost.setMaxAccess(_C)
if mibBuilder.loadTexts:rtpStatsCumulatedTotalPercentPacketsLost.setStatus(_A)
_RtpStatsCumulatedTotalInterarrivalJitterMin_Type=Unsigned32
_RtpStatsCumulatedTotalInterarrivalJitterMin_Object=MibScalar
rtpStatsCumulatedTotalInterarrivalJitterMin=_RtpStatsCumulatedTotalInterarrivalJitterMin_Object((1,3,6,1,4,1,4935,10,50,1,2,15,7),_RtpStatsCumulatedTotalInterarrivalJitterMin_Type())
rtpStatsCumulatedTotalInterarrivalJitterMin.setMaxAccess(_C)
if mibBuilder.loadTexts:rtpStatsCumulatedTotalInterarrivalJitterMin.setStatus(_A)
_RtpStatsCumulatedTotalInterarrivalJitterMax_Type=Unsigned32
_RtpStatsCumulatedTotalInterarrivalJitterMax_Object=MibScalar
rtpStatsCumulatedTotalInterarrivalJitterMax=_RtpStatsCumulatedTotalInterarrivalJitterMax_Object((1,3,6,1,4,1,4935,10,50,1,2,15,8),_RtpStatsCumulatedTotalInterarrivalJitterMax_Type())
rtpStatsCumulatedTotalInterarrivalJitterMax.setMaxAccess(_C)
if mibBuilder.loadTexts:rtpStatsCumulatedTotalInterarrivalJitterMax.setStatus(_A)
_RtpStatsCumulatedTotalInterarrivalJitterAvg_Type=Unsigned32
_RtpStatsCumulatedTotalInterarrivalJitterAvg_Object=MibScalar
rtpStatsCumulatedTotalInterarrivalJitterAvg=_RtpStatsCumulatedTotalInterarrivalJitterAvg_Object((1,3,6,1,4,1,4935,10,50,1,2,15,9),_RtpStatsCumulatedTotalInterarrivalJitterAvg_Type())
rtpStatsCumulatedTotalInterarrivalJitterAvg.setMaxAccess(_C)
if mibBuilder.loadTexts:rtpStatsCumulatedTotalInterarrivalJitterAvg.setStatus(_A)
_RtpStatsCumulatedTotalLatencyMin_Type=Unsigned32
_RtpStatsCumulatedTotalLatencyMin_Object=MibScalar
rtpStatsCumulatedTotalLatencyMin=_RtpStatsCumulatedTotalLatencyMin_Object((1,3,6,1,4,1,4935,10,50,1,2,15,10),_RtpStatsCumulatedTotalLatencyMin_Type())
rtpStatsCumulatedTotalLatencyMin.setMaxAccess(_C)
if mibBuilder.loadTexts:rtpStatsCumulatedTotalLatencyMin.setStatus(_A)
_RtpStatsCumulatedTotalLatencyMax_Type=Unsigned32
_RtpStatsCumulatedTotalLatencyMax_Object=MibScalar
rtpStatsCumulatedTotalLatencyMax=_RtpStatsCumulatedTotalLatencyMax_Object((1,3,6,1,4,1,4935,10,50,1,2,15,11),_RtpStatsCumulatedTotalLatencyMax_Type())
rtpStatsCumulatedTotalLatencyMax.setMaxAccess(_C)
if mibBuilder.loadTexts:rtpStatsCumulatedTotalLatencyMax.setStatus(_A)
_RtpStatsCumulatedTotalLatencyAvg_Type=Unsigned32
_RtpStatsCumulatedTotalLatencyAvg_Object=MibScalar
rtpStatsCumulatedTotalLatencyAvg=_RtpStatsCumulatedTotalLatencyAvg_Object((1,3,6,1,4,1,4935,10,50,1,2,15,12),_RtpStatsCumulatedTotalLatencyAvg_Type())
rtpStatsCumulatedTotalLatencyAvg.setMaxAccess(_C)
if mibBuilder.loadTexts:rtpStatsCumulatedTotalLatencyAvg.setStatus(_A)
_RtpConformance_ObjectIdentity=ObjectIdentity
rtpConformance=_RtpConformance_ObjectIdentity((1,3,6,1,4,1,4935,10,50,2))
_RtpCompliances_ObjectIdentity=ObjectIdentity
rtpCompliances=_RtpCompliances_ObjectIdentity((1,3,6,1,4,1,4935,10,50,2,1))
_RtpGroups_ObjectIdentity=ObjectIdentity
rtpGroups=_RtpGroups_ObjectIdentity((1,3,6,1,4,1,4935,10,50,2,2))
_RtpConfig_ObjectIdentity=ObjectIdentity
rtpConfig=_RtpConfig_ObjectIdentity((1,3,6,1,4,1,4935,15,115))
if mibBuilder.loadTexts:rtpConfig.setStatus(_A)
class _RtpConfigBasePort_Type(Unsigned32):defaultValue=5004;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1025,64535))
_RtpConfigBasePort_Type.__name__=_D
_RtpConfigBasePort_Object=MibScalar
rtpConfigBasePort=_RtpConfigBasePort_Object((1,3,6,1,4,1,4935,15,115,5),_RtpConfigBasePort_Type())
rtpConfigBasePort.setMaxAccess('read-write')
if mibBuilder.loadTexts:rtpConfigBasePort.setStatus(_A)
rtpStatsBasicGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,10,50,2,2,1))
rtpStatsBasicGroupVer1.setObjects(*((_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n)))
if mibBuilder.loadTexts:rtpStatsBasicGroupVer1.setStatus(_A)
rtpConfigBasicGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,10,50,2,2,2))
rtpConfigBasicGroupVer1.setObjects((_B,_o))
if mibBuilder.loadTexts:rtpConfigBasicGroupVer1.setStatus(_A)
rtpBasicComplVer1=ModuleCompliance((1,3,6,1,4,1,4935,10,50,2,1,1))
rtpBasicComplVer1.setObjects(*((_B,_p),(_B,_q)))
if mibBuilder.loadTexts:rtpBasicComplVer1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'rtpMIB':rtpMIB,'rtpMIBObjects':rtpMIBObjects,'rtpStats':rtpStats,'rtpStatsLastConnectionStatistics':rtpStatsLastConnectionStatistics,_E:rtpStatsLastConnNumberOctetsTransmitted,_F:rtpStatsLastConnNumberOctetsReceived,_G:rtpStatsLastConnNumberPacketsTransmitted,_H:rtpStatsLastConnNumberPacketsReceived,_I:rtpStatsLastConnNumberPacketsLost,_J:rtpStatsLastConnPercentPacketsLost,_K:rtpStatsLastConnInterarrivalJitterMin,_L:rtpStatsLastConnInterarrivalJitterMax,_M:rtpStatsLastConnInterarrivalJitterAvg,_N:rtpStatsLastConnLatencyMin,_O:rtpStatsLastConnLatencyMax,_P:rtpStatsLastConnLatencyAvg,'rtpStatsCurrentStatistics':rtpStatsCurrentStatistics,_Q:rtpStatsCurrentTotalOctetsTransmitted,_R:rtpStatsCurrentTotalOctetsReceived,_S:rtpStatsCurrentTotalPacketsTransmitted,_T:rtpStatsCurrentTotalPacketsReceived,_U:rtpStatsCurrentTotalPacketsLost,_V:rtpStatsCurrentTotalPercentPacketsLost,_W:rtpStatsCurrentTotalInterarrivalJitterMin,_X:rtpStatsCurrentTotalInterarrivalJitterMax,_Y:rtpStatsCurrentTotalInterarrivalJitterAvg,_Z:rtpStatsCurrentTotalLatencyMin,_a:rtpStatsCurrentTotalLatencyMax,_b:rtpStatsCurrentTotalLatencyAvg,'rtpStatsCumulatedStatistics':rtpStatsCumulatedStatistics,_c:rtpStatsCumulatedTotalOctetsTransmitted,_d:rtpStatsCumulatedTotalOctetsReceived,_e:rtpStatsCumulatedTotalPacketsTransmitted,_f:rtpStatsCumulatedTotalPacketsReceived,_g:rtpStatsCumulatedTotalPacketsLost,_h:rtpStatsCumulatedTotalPercentPacketsLost,_i:rtpStatsCumulatedTotalInterarrivalJitterMin,_j:rtpStatsCumulatedTotalInterarrivalJitterMax,_k:rtpStatsCumulatedTotalInterarrivalJitterAvg,_l:rtpStatsCumulatedTotalLatencyMin,_m:rtpStatsCumulatedTotalLatencyMax,_n:rtpStatsCumulatedTotalLatencyAvg,'rtpConformance':rtpConformance,'rtpCompliances':rtpCompliances,'rtpBasicComplVer1':rtpBasicComplVer1,'rtpGroups':rtpGroups,_p:rtpStatsBasicGroupVer1,_q:rtpConfigBasicGroupVer1,'rtpConfig':rtpConfig,_o:rtpConfigBasePort})