_U='internalErrorReason'
_T='internalErrorLocation'
_S='pdosAnomalyRouter'
_R='pdosHeartbeatSource'
_Q='pdosAnomalyTcpFlags'
_P='pdosAnomalyProto'
_O='obsolete'
_N='DisplayString'
_M='pdosUrl'
_L='pdosAnomalyRouterInterfaces'
_K='pdosAnomalyDuration'
_J='pdosAnomalyStart'
_I='pdosAnomalyClassification'
_H='pdosAnomalyLinkPercent'
_G='pdosAnomalyResource'
_F='pdosAnomalyIpVersion'
_E='pdosAnomalyDirection'
_D='pdosAnomalyId'
_C='accessible-for-notify'
_B='current'
_A='PEAKFLOW-DOS-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
arbornetworksProducts,=mibBuilder.importSymbols('ARBOR-SMI','arbornetworksProducts')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_N,'PhysAddress','TextualConvention')
peakflowDosMIB=ModuleIdentity((1,3,6,1,4,1,9694,1,1))
if mibBuilder.loadTexts:peakflowDosMIB.setRevisions(('2019-08-27 00:00','2015-11-17 00:00','2014-06-24 00:00','2013-08-19 00:00','2010-05-20 00:00','2009-03-30 00:00','2008-11-13 00:00','2008-05-08 00:00','2008-04-24 00:00','2008-01-08 00:00','2007-12-14 00:00','2005-11-23 00:00','2005-09-12 00:00','2005-08-26 00:00','2005-05-09 00:00','2005-02-11 00:00','2004-11-10 00:00','2004-10-26 00:00','2001-05-01 00:00'))
_PeakflowDosCMI_ObjectIdentity=ObjectIdentity
peakflowDosCMI=_PeakflowDosCMI_ObjectIdentity((1,3,6,1,4,1,9694,1,1,1))
class _PdosUrl_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,256))
_PdosUrl_Type.__name__=_N
_PdosUrl_Object=MibScalar
pdosUrl=_PdosUrl_Object((1,3,6,1,4,1,9694,1,1,1,1),_PdosUrl_Type())
pdosUrl.setMaxAccess(_C)
if mibBuilder.loadTexts:pdosUrl.setStatus(_B)
_PdosAnomalyId_Type=Integer32
_PdosAnomalyId_Object=MibScalar
pdosAnomalyId=_PdosAnomalyId_Object((1,3,6,1,4,1,9694,1,1,1,2),_PdosAnomalyId_Type())
pdosAnomalyId.setMaxAccess(_C)
if mibBuilder.loadTexts:pdosAnomalyId.setStatus(_B)
class _PdosAnomalyDirection_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_PdosAnomalyDirection_Type.__name__=_N
_PdosAnomalyDirection_Object=MibScalar
pdosAnomalyDirection=_PdosAnomalyDirection_Object((1,3,6,1,4,1,9694,1,1,1,3),_PdosAnomalyDirection_Type())
pdosAnomalyDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:pdosAnomalyDirection.setStatus(_B)
class _PdosAnomalyResource_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,256))
_PdosAnomalyResource_Type.__name__=_N
_PdosAnomalyResource_Object=MibScalar
pdosAnomalyResource=_PdosAnomalyResource_Object((1,3,6,1,4,1,9694,1,1,1,4),_PdosAnomalyResource_Type())
pdosAnomalyResource.setMaxAccess(_C)
if mibBuilder.loadTexts:pdosAnomalyResource.setStatus(_B)
class _PdosHeartbeatSource_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,256))
_PdosHeartbeatSource_Type.__name__=_N
_PdosHeartbeatSource_Object=MibScalar
pdosHeartbeatSource=_PdosHeartbeatSource_Object((1,3,6,1,4,1,9694,1,1,1,5),_PdosHeartbeatSource_Type())
pdosHeartbeatSource.setMaxAccess(_C)
if mibBuilder.loadTexts:pdosHeartbeatSource.setStatus(_O)
class _InternalErrorLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,256))
_InternalErrorLocation_Type.__name__=_N
_InternalErrorLocation_Object=MibScalar
internalErrorLocation=_InternalErrorLocation_Object((1,3,6,1,4,1,9694,1,1,1,6),_InternalErrorLocation_Type())
internalErrorLocation.setMaxAccess(_C)
if mibBuilder.loadTexts:internalErrorLocation.setStatus(_O)
class _InternalErrorReason_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,256))
_InternalErrorReason_Type.__name__=_N
_InternalErrorReason_Object=MibScalar
internalErrorReason=_InternalErrorReason_Object((1,3,6,1,4,1,9694,1,1,1,7),_InternalErrorReason_Type())
internalErrorReason.setMaxAccess(_C)
if mibBuilder.loadTexts:internalErrorReason.setStatus(_O)
class _PdosAnomalyProto_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,256))
_PdosAnomalyProto_Type.__name__=_N
_PdosAnomalyProto_Object=MibScalar
pdosAnomalyProto=_PdosAnomalyProto_Object((1,3,6,1,4,1,9694,1,1,1,8),_PdosAnomalyProto_Type())
pdosAnomalyProto.setMaxAccess(_C)
if mibBuilder.loadTexts:pdosAnomalyProto.setStatus(_B)
_PdosAnomalyLinkPercent_Type=Unsigned32
_PdosAnomalyLinkPercent_Object=MibScalar
pdosAnomalyLinkPercent=_PdosAnomalyLinkPercent_Object((1,3,6,1,4,1,9694,1,1,1,9),_PdosAnomalyLinkPercent_Type())
pdosAnomalyLinkPercent.setMaxAccess(_C)
if mibBuilder.loadTexts:pdosAnomalyLinkPercent.setStatus(_B)
_PdosAnomalyAlertCnt_Type=Integer32
_PdosAnomalyAlertCnt_Object=MibScalar
pdosAnomalyAlertCnt=_PdosAnomalyAlertCnt_Object((1,3,6,1,4,1,9694,1,1,1,10),_PdosAnomalyAlertCnt_Type())
pdosAnomalyAlertCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:pdosAnomalyAlertCnt.setStatus(_O)
class _PdosAnomalyStart_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_PdosAnomalyStart_Type.__name__=_N
_PdosAnomalyStart_Object=MibScalar
pdosAnomalyStart=_PdosAnomalyStart_Object((1,3,6,1,4,1,9694,1,1,1,11),_PdosAnomalyStart_Type())
pdosAnomalyStart.setMaxAccess(_C)
if mibBuilder.loadTexts:pdosAnomalyStart.setStatus(_B)
_PdosAnomalyDuration_Type=TimeTicks
_PdosAnomalyDuration_Object=MibScalar
pdosAnomalyDuration=_PdosAnomalyDuration_Object((1,3,6,1,4,1,9694,1,1,1,12),_PdosAnomalyDuration_Type())
pdosAnomalyDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:pdosAnomalyDuration.setStatus(_B)
class _PdosAnomalyTcpFlags_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_PdosAnomalyTcpFlags_Type.__name__=_N
_PdosAnomalyTcpFlags_Object=MibScalar
pdosAnomalyTcpFlags=_PdosAnomalyTcpFlags_Object((1,3,6,1,4,1,9694,1,1,1,13),_PdosAnomalyTcpFlags_Type())
pdosAnomalyTcpFlags.setMaxAccess(_C)
if mibBuilder.loadTexts:pdosAnomalyTcpFlags.setStatus(_B)
_PdosAnomalyRouter_Type=IpAddress
_PdosAnomalyRouter_Object=MibScalar
pdosAnomalyRouter=_PdosAnomalyRouter_Object((1,3,6,1,4,1,9694,1,1,1,14),_PdosAnomalyRouter_Type())
pdosAnomalyRouter.setMaxAccess(_C)
if mibBuilder.loadTexts:pdosAnomalyRouter.setStatus(_B)
class _PdosAnomalyRouterInterfaces_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1024))
_PdosAnomalyRouterInterfaces_Type.__name__=_N
_PdosAnomalyRouterInterfaces_Object=MibScalar
pdosAnomalyRouterInterfaces=_PdosAnomalyRouterInterfaces_Object((1,3,6,1,4,1,9694,1,1,1,15),_PdosAnomalyRouterInterfaces_Type())
pdosAnomalyRouterInterfaces.setMaxAccess(_C)
if mibBuilder.loadTexts:pdosAnomalyRouterInterfaces.setStatus(_B)
class _PdosAnomalyClassification_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_PdosAnomalyClassification_Type.__name__=_N
_PdosAnomalyClassification_Object=MibScalar
pdosAnomalyClassification=_PdosAnomalyClassification_Object((1,3,6,1,4,1,9694,1,1,1,16),_PdosAnomalyClassification_Type())
pdosAnomalyClassification.setMaxAccess(_C)
if mibBuilder.loadTexts:pdosAnomalyClassification.setStatus(_B)
_PdosAnomalyIpVersion_Type=Integer32
_PdosAnomalyIpVersion_Object=MibScalar
pdosAnomalyIpVersion=_PdosAnomalyIpVersion_Object((1,3,6,1,4,1,9694,1,1,1,17),_PdosAnomalyIpVersion_Type())
pdosAnomalyIpVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:pdosAnomalyIpVersion.setStatus(_B)
_PeakflowDosMgr_ObjectIdentity=ObjectIdentity
peakflowDosMgr=_PeakflowDosMgr_ObjectIdentity((1,3,6,1,4,1,9694,1,1,2))
_PeakflowDosTraps_ObjectIdentity=ObjectIdentity
peakflowDosTraps=_PeakflowDosTraps_ObjectIdentity((1,3,6,1,4,1,9694,1,1,3))
_PeakflowDosTrapsEnumerate_ObjectIdentity=ObjectIdentity
peakflowDosTrapsEnumerate=_PeakflowDosTrapsEnumerate_ObjectIdentity((1,3,6,1,4,1,9694,1,1,3,0))
bandwidthAnomaly=NotificationType((1,3,6,1,4,1,9694,1,1,3,0,1))
bandwidthAnomaly.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:bandwidthAnomaly.setStatus(_B)
tcpflagsAnomaly=NotificationType((1,3,6,1,4,1,9694,1,1,3,0,2))
tcpflagsAnomaly.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_Q)))
if mibBuilder.loadTexts:tcpflagsAnomaly.setStatus(_O)
protocolAnomaly=NotificationType((1,3,6,1,4,1,9694,1,1,3,0,3))
protocolAnomaly.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_P)))
if mibBuilder.loadTexts:protocolAnomaly.setStatus(_B)
heartbeatLoss=NotificationType((1,3,6,1,4,1,9694,1,1,3,0,4))
heartbeatLoss.setObjects((_A,_R))
if mibBuilder.loadTexts:heartbeatLoss.setStatus(_O)
internalError=NotificationType((1,3,6,1,4,1,9694,1,1,3,0,5))
internalError.setObjects(*((_A,_T),(_A,_U)))
if mibBuilder.loadTexts:internalError.setStatus(_O)
anomalyDone=NotificationType((1,3,6,1,4,1,9694,1,1,3,0,6))
anomalyDone.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:anomalyDone.setStatus(_B)
netflowMissing=NotificationType((1,3,6,1,4,1,9694,1,1,3,0,7))
netflowMissing.setObjects((_A,_S))
if mibBuilder.loadTexts:netflowMissing.setStatus(_O)
netflowMissingDone=NotificationType((1,3,6,1,4,1,9694,1,1,3,0,8))
netflowMissingDone.setObjects((_A,_S))
if mibBuilder.loadTexts:netflowMissingDone.setStatus(_O)
icmpMisuseAnomaly=NotificationType((1,3,6,1,4,1,9694,1,1,3,0,9))
icmpMisuseAnomaly.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_P)))
if mibBuilder.loadTexts:icmpMisuseAnomaly.setStatus(_B)
tcpNullMisuseAnomaly=NotificationType((1,3,6,1,4,1,9694,1,1,3,0,10))
tcpNullMisuseAnomaly.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_P),(_A,_Q)))
if mibBuilder.loadTexts:tcpNullMisuseAnomaly.setStatus(_B)
tcpSynMisuseAnomaly=NotificationType((1,3,6,1,4,1,9694,1,1,3,0,11))
tcpSynMisuseAnomaly.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_P),(_A,_Q)))
if mibBuilder.loadTexts:tcpSynMisuseAnomaly.setStatus(_B)
ipNullMisuseAnomaly=NotificationType((1,3,6,1,4,1,9694,1,1,3,0,12))
ipNullMisuseAnomaly.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:ipNullMisuseAnomaly.setStatus(_B)
ipFragMisuseAnomaly=NotificationType((1,3,6,1,4,1,9694,1,1,3,0,13))
ipFragMisuseAnomaly.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_P)))
if mibBuilder.loadTexts:ipFragMisuseAnomaly.setStatus(_B)
ipPrivateMisuseAnomaly=NotificationType((1,3,6,1,4,1,9694,1,1,3,0,14))
ipPrivateMisuseAnomaly.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:ipPrivateMisuseAnomaly.setStatus(_B)
heartbeatLossDone=NotificationType((1,3,6,1,4,1,9694,1,1,3,0,15))
heartbeatLossDone.setObjects((_A,_R))
if mibBuilder.loadTexts:heartbeatLossDone.setStatus(_O)
tcpRstMisuseAnomaly=NotificationType((1,3,6,1,4,1,9694,1,1,3,0,16))
tcpRstMisuseAnomaly.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_P),(_A,_Q)))
if mibBuilder.loadTexts:tcpRstMisuseAnomaly.setStatus(_B)
totalTrafficMisuseAnomaly=NotificationType((1,3,6,1,4,1,9694,1,1,3,0,17))
totalTrafficMisuseAnomaly.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:totalTrafficMisuseAnomaly.setStatus(_B)
fingerprintAnomaly=NotificationType((1,3,6,1,4,1,9694,1,1,3,0,18))
fingerprintAnomaly.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:fingerprintAnomaly.setStatus(_B)
dnsMisuseAnomaly=NotificationType((1,3,6,1,4,1,9694,1,1,3,0,19))
dnsMisuseAnomaly.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_P)))
if mibBuilder.loadTexts:dnsMisuseAnomaly.setStatus(_B)
udpMisuseAnomaly=NotificationType((1,3,6,1,4,1,9694,1,1,3,0,20))
udpMisuseAnomaly.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_P)))
if mibBuilder.loadTexts:udpMisuseAnomaly.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'peakflowDosMIB':peakflowDosMIB,'peakflowDosCMI':peakflowDosCMI,_M:pdosUrl,_D:pdosAnomalyId,_E:pdosAnomalyDirection,_G:pdosAnomalyResource,_R:pdosHeartbeatSource,_T:internalErrorLocation,_U:internalErrorReason,_P:pdosAnomalyProto,_H:pdosAnomalyLinkPercent,'pdosAnomalyAlertCnt':pdosAnomalyAlertCnt,_J:pdosAnomalyStart,_K:pdosAnomalyDuration,_Q:pdosAnomalyTcpFlags,_S:pdosAnomalyRouter,_L:pdosAnomalyRouterInterfaces,_I:pdosAnomalyClassification,_F:pdosAnomalyIpVersion,'peakflowDosMgr':peakflowDosMgr,'peakflowDosTraps':peakflowDosTraps,'peakflowDosTrapsEnumerate':peakflowDosTrapsEnumerate,'bandwidthAnomaly':bandwidthAnomaly,'tcpflagsAnomaly':tcpflagsAnomaly,'protocolAnomaly':protocolAnomaly,'heartbeatLoss':heartbeatLoss,'internalError':internalError,'anomalyDone':anomalyDone,'netflowMissing':netflowMissing,'netflowMissingDone':netflowMissingDone,'icmpMisuseAnomaly':icmpMisuseAnomaly,'tcpNullMisuseAnomaly':tcpNullMisuseAnomaly,'tcpSynMisuseAnomaly':tcpSynMisuseAnomaly,'ipNullMisuseAnomaly':ipNullMisuseAnomaly,'ipFragMisuseAnomaly':ipFragMisuseAnomaly,'ipPrivateMisuseAnomaly':ipPrivateMisuseAnomaly,'heartbeatLossDone':heartbeatLossDone,'tcpRstMisuseAnomaly':tcpRstMisuseAnomaly,'totalTrafficMisuseAnomaly':totalTrafficMisuseAnomaly,'fingerprintAnomaly':fingerprintAnomaly,'dnsMisuseAnomaly':dnsMisuseAnomaly,'udpMisuseAnomaly':udpMisuseAnomaly})