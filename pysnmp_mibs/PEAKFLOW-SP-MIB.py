_Au='spSightlineSignalingMessage'
_At='spSightlineSignalingClientName'
_As='spMitOrchestrationDestTMSGroup'
_Ar='spMitOrchestrationSrcTMSGroup'
_Aq='spTMSMultiDiversionPrefix'
_Ap='spLicenseErrLimit'
_Ao='spLicenseErrCount'
_An='spRoutingFailoverInterfaces'
_Am='spServiceElement'
_Al='spApplicationName'
_Ak='spFlowspecTimeout'
_Aj='spFlowspecCommunity'
_Ai='spBlackholeNexthop'
_Ah='spBlackholePrefix'
_Ag='spBlackholeTimeout'
_Af='spBlackholeCommunity'
_Ae='spThirdPartyAddr'
_Ad='spThirdPartyZone'
_Ac='spScriptStart'
_Ab='spScriptPort'
_Aa='spScriptHost'
_AZ='spScriptCommand'
_AY='spDNSObservedMax'
_AX='spDNSObservedMean'
_AW='spDNSObserved'
_AV='spFingerprintMessage'
_AU='spFingerprintSender'
_AT='spFingerprintFeedback'
_AS='spHijackLocal'
_AR='spHijackAttr'
_AQ='spHijackRoute'
_AP='spReportURL'
_AO='spReportID'
_AN='spReportName'
_AM='spVersion'
_AL='spInterfaceUsageHC'
_AK='spInterfaceSpeedHC'
_AJ='spInterfaceUsage'
_AI='spInterfaceSpeed'
_AH='spBGPTrapNewAttributes'
_AG='spBGPTrapOldAttributes'
_AF='spBGPTrapPrefix'
_AE='spBGPTrapEvent'
_AD='spBGPTrapName'
_AC='spBGPInstability'
_AB='spDetector'
_AA='deprecated'
_A9='spImportance'
_A8='spSmartAlertObserved'
_A7='spSmartAlertThreshold'
_A6='spSmartAlertSettingName'
_A5='spCloudSignalFaultDescription'
_A4='spLicenseErrDescription'
_A3='spLicenseErrType'
_A2='spDetectedCountries'
_A1='spServiceName'
_A0='spSystemErrorDescription'
_z='spSystemErrorType'
_y='spGreTunnelName'
_x='spGreTunnelDestination'
_w='spCommFailureDescription'
_v='spCommFailureDestination'
_u='spTMSMultiPrefix'
_t='spTMSTimeout'
_s='spTMSCommunity'
_r='spTMSPrefix'
_q='spDNSExpected'
_p='spDNSName'
_o='spHardwareFailureDescription'
_n='spManagedObjectFamily'
_m='spUsername'
_l='spInterfaceIndex'
_k='spInterface'
_j='spPravail'
_i='spManagedObjects'
_h='spInetAddressType'
_g='spInetAddress'
_f='spAlertDetectionSignatures'
_e='spUsageHC'
_d='spThresholdHC'
_c='spUsage'
_b='obsolete'
_a='Integer32'
_Z='spImpactPpsHC'
_Y='spImpactBpsHC'
_X='spImpactPps'
_W='spImpactBps'
_V='spFingerprintName'
_U='pdosAnomalyStart'
_T='pdosAnomalyDuration'
_S='pdosAnomalyDirection'
_R='pdosAnomalyClassification'
_Q='spMitigationStart'
_P='spUnit'
_O='spMitigationName'
_N='spThreshold'
_M='spUsageType'
_L='pdosUrl'
_K='spMitigationID'
_J='spManagedObject'
_I='spRouter'
_H='read-only'
_G='spCollector'
_F='PEAKFLOW-DOS-MIB'
_E='spAlertID'
_D='DisplayString'
_C='accessible-for-notify'
_B='current'
_A='PEAKFLOW-SP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
arbornetworksProducts,=mibBuilder.importSymbols('ARBOR-SMI','arbornetworksProducts')
CounterBasedGauge64,=mibBuilder.importSymbols('HCNUM-TC','CounterBasedGauge64')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
pdosAnomalyClassification,pdosAnomalyDirection,pdosAnomalyDuration,pdosAnomalyStart,pdosUrl=mibBuilder.importSymbols(_F,_R,_S,_T,_U,_L)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_a,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
peakflowSPMIB=ModuleIdentity((1,3,6,1,4,1,9694,1,4))
if mibBuilder.loadTexts:peakflowSPMIB.setRevisions(('2019-09-17 00:00','2019-08-27 00:00','2019-01-23 00:00','2018-12-05 00:00','2018-09-07 00:00','2018-08-06 00:00','2018-08-01 00:00','2018-07-31 00:00','2018-07-13 00:00','2018-06-26 00:00','2018-02-01 00:00','2016-12-06 00:00','2016-01-11 00:00','2015-11-20 00:00','2014-04-04 00:00','2013-12-04 00:00','2013-10-03 00:00','2013-08-19 00:00','2013-01-15 00:00','2012-07-30 00:00','2012-05-13 00:00','2011-06-03 00:00','2010-06-08 00:00','2010-05-20 00:00','2009-09-24 00:00','2009-04-01 00:00','2009-03-30 00:00','2009-02-02 00:00','2008-12-16 00:00','2008-11-13 00:00','2008-05-19 00:00','2008-02-19 00:00','2008-02-11 00:00','2007-08-07 00:00','2006-04-26 00:00','2006-03-23 00:00','2005-11-14 00:00','2005-10-19 00:00','2005-09-12 00:00','2005-08-23 00:00','2005-05-17 01:00','2005-05-17 00:00','2005-02-11 00:00','2004-12-10 00:00','2004-03-30 00:00','2002-08-28 00:00'))
_PeakflowSPCMI_ObjectIdentity=ObjectIdentity
peakflowSPCMI=_PeakflowSPCMI_ObjectIdentity((1,3,6,1,4,1,9694,1,4,1))
class _SpCollector_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_SpCollector_Type.__name__=_D
_SpCollector_Object=MibScalar
spCollector=_SpCollector_Object((1,3,6,1,4,1,9694,1,4,1,1),_SpCollector_Type())
spCollector.setMaxAccess(_C)
if mibBuilder.loadTexts:spCollector.setStatus(_B)
class _SpRouter_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_SpRouter_Type.__name__=_D
_SpRouter_Object=MibScalar
spRouter=_SpRouter_Object((1,3,6,1,4,1,9694,1,4,1,2),_SpRouter_Type())
spRouter.setMaxAccess(_C)
if mibBuilder.loadTexts:spRouter.setStatus(_B)
class _SpInterface_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,256))
_SpInterface_Type.__name__=_D
_SpInterface_Object=MibScalar
spInterface=_SpInterface_Object((1,3,6,1,4,1,9694,1,4,1,3),_SpInterface_Type())
spInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:spInterface.setStatus(_B)
_SpInterfaceIndex_Type=Unsigned32
_SpInterfaceIndex_Object=MibScalar
spInterfaceIndex=_SpInterfaceIndex_Object((1,3,6,1,4,1,9694,1,4,1,4),_SpInterfaceIndex_Type())
spInterfaceIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:spInterfaceIndex.setStatus(_B)
_SpDuration_Type=TimeTicks
_SpDuration_Object=MibScalar
spDuration=_SpDuration_Object((1,3,6,1,4,1,9694,1,4,1,5),_SpDuration_Type())
spDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:spDuration.setStatus(_B)
class _SpBGPEvent_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_SpBGPEvent_Type.__name__=_D
_SpBGPEvent_Object=MibScalar
spBGPEvent=_SpBGPEvent_Object((1,3,6,1,4,1,9694,1,4,1,6),_SpBGPEvent_Type())
spBGPEvent.setMaxAccess(_C)
if mibBuilder.loadTexts:spBGPEvent.setStatus(_B)
_SpBGPInstability_Type=Unsigned32
_SpBGPInstability_Object=MibScalar
spBGPInstability=_SpBGPInstability_Object((1,3,6,1,4,1,9694,1,4,1,7),_SpBGPInstability_Type())
spBGPInstability.setMaxAccess(_C)
if mibBuilder.loadTexts:spBGPInstability.setStatus(_B)
class _SpBGPTrapName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_SpBGPTrapName_Type.__name__=_D
_SpBGPTrapName_Object=MibScalar
spBGPTrapName=_SpBGPTrapName_Object((1,3,6,1,4,1,9694,1,4,1,8),_SpBGPTrapName_Type())
spBGPTrapName.setMaxAccess(_C)
if mibBuilder.loadTexts:spBGPTrapName.setStatus(_B)
class _SpBGPTrapEvent_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_SpBGPTrapEvent_Type.__name__=_D
_SpBGPTrapEvent_Object=MibScalar
spBGPTrapEvent=_SpBGPTrapEvent_Object((1,3,6,1,4,1,9694,1,4,1,9),_SpBGPTrapEvent_Type())
spBGPTrapEvent.setMaxAccess(_C)
if mibBuilder.loadTexts:spBGPTrapEvent.setStatus(_B)
class _SpBGPTrapPrefix_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_SpBGPTrapPrefix_Type.__name__=_D
_SpBGPTrapPrefix_Object=MibScalar
spBGPTrapPrefix=_SpBGPTrapPrefix_Object((1,3,6,1,4,1,9694,1,4,1,10),_SpBGPTrapPrefix_Type())
spBGPTrapPrefix.setMaxAccess(_C)
if mibBuilder.loadTexts:spBGPTrapPrefix.setStatus(_B)
_SpBGPTrapOldAttributes_Type=DisplayString
_SpBGPTrapOldAttributes_Object=MibScalar
spBGPTrapOldAttributes=_SpBGPTrapOldAttributes_Object((1,3,6,1,4,1,9694,1,4,1,11),_SpBGPTrapOldAttributes_Type())
spBGPTrapOldAttributes.setMaxAccess(_C)
if mibBuilder.loadTexts:spBGPTrapOldAttributes.setStatus(_B)
_SpBGPTrapNewAttributes_Type=DisplayString
_SpBGPTrapNewAttributes_Object=MibScalar
spBGPTrapNewAttributes=_SpBGPTrapNewAttributes_Object((1,3,6,1,4,1,9694,1,4,1,12),_SpBGPTrapNewAttributes_Type())
spBGPTrapNewAttributes.setMaxAccess(_C)
if mibBuilder.loadTexts:spBGPTrapNewAttributes.setStatus(_B)
_SpInterfaceSpeed_Type=Unsigned32
_SpInterfaceSpeed_Object=MibScalar
spInterfaceSpeed=_SpInterfaceSpeed_Object((1,3,6,1,4,1,9694,1,4,1,13),_SpInterfaceSpeed_Type())
spInterfaceSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:spInterfaceSpeed.setStatus(_B)
_SpInterfaceUsage_Type=Unsigned32
_SpInterfaceUsage_Object=MibScalar
spInterfaceUsage=_SpInterfaceUsage_Object((1,3,6,1,4,1,9694,1,4,1,14),_SpInterfaceUsage_Type())
spInterfaceUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:spInterfaceUsage.setStatus(_B)
_SpReportURL_Type=DisplayString
_SpReportURL_Object=MibScalar
spReportURL=_SpReportURL_Object((1,3,6,1,4,1,9694,1,4,1,15),_SpReportURL_Type())
spReportURL.setMaxAccess(_C)
if mibBuilder.loadTexts:spReportURL.setStatus(_B)
class _SpReportName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_SpReportName_Type.__name__=_D
_SpReportName_Object=MibScalar
spReportName=_SpReportName_Object((1,3,6,1,4,1,9694,1,4,1,16),_SpReportName_Type())
spReportName.setMaxAccess(_C)
if mibBuilder.loadTexts:spReportName.setStatus(_B)
class _SpReportID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_SpReportID_Type.__name__=_D
_SpReportID_Object=MibScalar
spReportID=_SpReportID_Object((1,3,6,1,4,1,9694,1,4,1,17),_SpReportID_Type())
spReportID.setMaxAccess(_C)
if mibBuilder.loadTexts:spReportID.setStatus(_B)
_SpAlertID_Type=Unsigned32
_SpAlertID_Object=MibScalar
spAlertID=_SpAlertID_Object((1,3,6,1,4,1,9694,1,4,1,18),_SpAlertID_Type())
spAlertID.setMaxAccess(_C)
if mibBuilder.loadTexts:spAlertID.setStatus(_B)
class _SpHijackRoute_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_SpHijackRoute_Type.__name__=_D
_SpHijackRoute_Object=MibScalar
spHijackRoute=_SpHijackRoute_Object((1,3,6,1,4,1,9694,1,4,1,19),_SpHijackRoute_Type())
spHijackRoute.setMaxAccess(_C)
if mibBuilder.loadTexts:spHijackRoute.setStatus(_B)
class _SpHijackAttr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_SpHijackAttr_Type.__name__=_D
_SpHijackAttr_Object=MibScalar
spHijackAttr=_SpHijackAttr_Object((1,3,6,1,4,1,9694,1,4,1,20),_SpHijackAttr_Type())
spHijackAttr.setMaxAccess(_C)
if mibBuilder.loadTexts:spHijackAttr.setStatus(_B)
class _SpHijackLocal_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_SpHijackLocal_Type.__name__=_D
_SpHijackLocal_Object=MibScalar
spHijackLocal=_SpHijackLocal_Object((1,3,6,1,4,1,9694,1,4,1,21),_SpHijackLocal_Type())
spHijackLocal.setMaxAccess(_C)
if mibBuilder.loadTexts:spHijackLocal.setStatus(_B)
class _SpUsername_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_SpUsername_Type.__name__=_D
_SpUsername_Object=MibScalar
spUsername=_SpUsername_Object((1,3,6,1,4,1,9694,1,4,1,22),_SpUsername_Type())
spUsername.setMaxAccess(_C)
if mibBuilder.loadTexts:spUsername.setStatus(_B)
class _SpVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_SpVersion_Type.__name__=_D
_SpVersion_Object=MibScalar
spVersion=_SpVersion_Object((1,3,6,1,4,1,9694,1,4,1,23),_SpVersion_Type())
spVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:spVersion.setStatus(_B)
class _SpUsageType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_SpUsageType_Type.__name__=_D
_SpUsageType_Object=MibScalar
spUsageType=_SpUsageType_Object((1,3,6,1,4,1,9694,1,4,1,24),_SpUsageType_Type())
spUsageType.setMaxAccess(_C)
if mibBuilder.loadTexts:spUsageType.setStatus(_B)
class _SpManagedObject_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_SpManagedObject_Type.__name__=_D
_SpManagedObject_Object=MibScalar
spManagedObject=_SpManagedObject_Object((1,3,6,1,4,1,9694,1,4,1,25),_SpManagedObject_Type())
spManagedObject.setMaxAccess(_C)
if mibBuilder.loadTexts:spManagedObject.setStatus(_B)
class _SpManagedObjectFamily_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_SpManagedObjectFamily_Type.__name__=_D
_SpManagedObjectFamily_Object=MibScalar
spManagedObjectFamily=_SpManagedObjectFamily_Object((1,3,6,1,4,1,9694,1,4,1,26),_SpManagedObjectFamily_Type())
spManagedObjectFamily.setMaxAccess(_C)
if mibBuilder.loadTexts:spManagedObjectFamily.setStatus(_B)
_SpThreshold_Type=Unsigned32
_SpThreshold_Object=MibScalar
spThreshold=_SpThreshold_Object((1,3,6,1,4,1,9694,1,4,1,27),_SpThreshold_Type())
spThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:spThreshold.setStatus(_B)
_SpUsage_Type=Unsigned32
_SpUsage_Object=MibScalar
spUsage=_SpUsage_Object((1,3,6,1,4,1,9694,1,4,1,28),_SpUsage_Type())
spUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:spUsage.setStatus(_B)
class _SpUnit_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_SpUnit_Type.__name__=_D
_SpUnit_Object=MibScalar
spUnit=_SpUnit_Object((1,3,6,1,4,1,9694,1,4,1,29),_SpUnit_Type())
spUnit.setMaxAccess(_C)
if mibBuilder.loadTexts:spUnit.setStatus(_B)
class _SpHardwareFailureDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,256))
_SpHardwareFailureDescription_Type.__name__=_D
_SpHardwareFailureDescription_Object=MibScalar
spHardwareFailureDescription=_SpHardwareFailureDescription_Object((1,3,6,1,4,1,9694,1,4,1,30),_SpHardwareFailureDescription_Type())
spHardwareFailureDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:spHardwareFailureDescription.setStatus(_B)
class _SpFingerprintName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_SpFingerprintName_Type.__name__=_D
_SpFingerprintName_Object=MibScalar
spFingerprintName=_SpFingerprintName_Object((1,3,6,1,4,1,9694,1,4,1,31),_SpFingerprintName_Type())
spFingerprintName.setMaxAccess(_C)
if mibBuilder.loadTexts:spFingerprintName.setStatus(_B)
class _SpFingerprintFeedback_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,256))
_SpFingerprintFeedback_Type.__name__=_D
_SpFingerprintFeedback_Object=MibScalar
spFingerprintFeedback=_SpFingerprintFeedback_Object((1,3,6,1,4,1,9694,1,4,1,32),_SpFingerprintFeedback_Type())
spFingerprintFeedback.setMaxAccess(_C)
if mibBuilder.loadTexts:spFingerprintFeedback.setStatus(_B)
class _SpFingerprintSender_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_SpFingerprintSender_Type.__name__=_D
_SpFingerprintSender_Object=MibScalar
spFingerprintSender=_SpFingerprintSender_Object((1,3,6,1,4,1,9694,1,4,1,33),_SpFingerprintSender_Type())
spFingerprintSender.setMaxAccess(_C)
if mibBuilder.loadTexts:spFingerprintSender.setStatus(_B)
class _SpFingerprintMessage_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,256))
_SpFingerprintMessage_Type.__name__=_D
_SpFingerprintMessage_Object=MibScalar
spFingerprintMessage=_SpFingerprintMessage_Object((1,3,6,1,4,1,9694,1,4,1,34),_SpFingerprintMessage_Type())
spFingerprintMessage.setMaxAccess(_C)
if mibBuilder.loadTexts:spFingerprintMessage.setStatus(_B)
_SpMitigationID_Type=Unsigned32
_SpMitigationID_Object=MibScalar
spMitigationID=_SpMitigationID_Object((1,3,6,1,4,1,9694,1,4,1,35),_SpMitigationID_Type())
spMitigationID.setMaxAccess(_C)
if mibBuilder.loadTexts:spMitigationID.setStatus(_B)
class _SpDNSName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,256))
_SpDNSName_Type.__name__=_D
_SpDNSName_Object=MibScalar
spDNSName=_SpDNSName_Object((1,3,6,1,4,1,9694,1,4,1,36),_SpDNSName_Type())
spDNSName.setMaxAccess(_C)
if mibBuilder.loadTexts:spDNSName.setStatus(_B)
_SpDNSExpected_Type=Unsigned32
_SpDNSExpected_Object=MibScalar
spDNSExpected=_SpDNSExpected_Object((1,3,6,1,4,1,9694,1,4,1,37),_SpDNSExpected_Type())
spDNSExpected.setMaxAccess(_C)
if mibBuilder.loadTexts:spDNSExpected.setStatus(_B)
_SpDNSObserved_Type=Unsigned32
_SpDNSObserved_Object=MibScalar
spDNSObserved=_SpDNSObserved_Object((1,3,6,1,4,1,9694,1,4,1,38),_SpDNSObserved_Type())
spDNSObserved.setMaxAccess(_C)
if mibBuilder.loadTexts:spDNSObserved.setStatus(_B)
_SpDNSObservedMean_Type=Unsigned32
_SpDNSObservedMean_Object=MibScalar
spDNSObservedMean=_SpDNSObservedMean_Object((1,3,6,1,4,1,9694,1,4,1,39),_SpDNSObservedMean_Type())
spDNSObservedMean.setMaxAccess(_C)
if mibBuilder.loadTexts:spDNSObservedMean.setStatus(_B)
_SpDNSObservedMax_Type=Unsigned32
_SpDNSObservedMax_Object=MibScalar
spDNSObservedMax=_SpDNSObservedMax_Object((1,3,6,1,4,1,9694,1,4,1,40),_SpDNSObservedMax_Type())
spDNSObservedMax.setMaxAccess(_C)
if mibBuilder.loadTexts:spDNSObservedMax.setStatus(_B)
class _SpMitigationName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_SpMitigationName_Type.__name__=_D
_SpMitigationName_Object=MibScalar
spMitigationName=_SpMitigationName_Object((1,3,6,1,4,1,9694,1,4,1,41),_SpMitigationName_Type())
spMitigationName.setMaxAccess(_C)
if mibBuilder.loadTexts:spMitigationName.setStatus(_B)
class _SpScriptCommand_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_SpScriptCommand_Type.__name__=_D
_SpScriptCommand_Object=MibScalar
spScriptCommand=_SpScriptCommand_Object((1,3,6,1,4,1,9694,1,4,1,42),_SpScriptCommand_Type())
spScriptCommand.setMaxAccess(_C)
if mibBuilder.loadTexts:spScriptCommand.setStatus(_B)
class _SpScriptHost_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,256))
_SpScriptHost_Type.__name__=_D
_SpScriptHost_Object=MibScalar
spScriptHost=_SpScriptHost_Object((1,3,6,1,4,1,9694,1,4,1,43),_SpScriptHost_Type())
spScriptHost.setMaxAccess(_C)
if mibBuilder.loadTexts:spScriptHost.setStatus(_B)
class _SpScriptPort_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,5))
_SpScriptPort_Type.__name__=_D
_SpScriptPort_Object=MibScalar
spScriptPort=_SpScriptPort_Object((1,3,6,1,4,1,9694,1,4,1,44),_SpScriptPort_Type())
spScriptPort.setMaxAccess(_C)
if mibBuilder.loadTexts:spScriptPort.setStatus(_B)
class _SpScriptStart_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_SpScriptStart_Type.__name__=_D
_SpScriptStart_Object=MibScalar
spScriptStart=_SpScriptStart_Object((1,3,6,1,4,1,9694,1,4,1,45),_SpScriptStart_Type())
spScriptStart.setMaxAccess(_C)
if mibBuilder.loadTexts:spScriptStart.setStatus(_B)
class _SpTMSPrefix_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SpTMSPrefix_Type.__name__=_D
_SpTMSPrefix_Object=MibScalar
spTMSPrefix=_SpTMSPrefix_Object((1,3,6,1,4,1,9694,1,4,1,46),_SpTMSPrefix_Type())
spTMSPrefix.setMaxAccess(_C)
if mibBuilder.loadTexts:spTMSPrefix.setStatus(_B)
class _SpTMSCommunity_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SpTMSCommunity_Type.__name__=_D
_SpTMSCommunity_Object=MibScalar
spTMSCommunity=_SpTMSCommunity_Object((1,3,6,1,4,1,9694,1,4,1,47),_SpTMSCommunity_Type())
spTMSCommunity.setMaxAccess(_C)
if mibBuilder.loadTexts:spTMSCommunity.setStatus(_B)
class _SpTMSTimeout_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SpTMSTimeout_Type.__name__=_D
_SpTMSTimeout_Object=MibScalar
spTMSTimeout=_SpTMSTimeout_Object((1,3,6,1,4,1,9694,1,4,1,48),_SpTMSTimeout_Type())
spTMSTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:spTMSTimeout.setStatus(_B)
class _SpThirdPartyZone_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SpThirdPartyZone_Type.__name__=_D
_SpThirdPartyZone_Object=MibScalar
spThirdPartyZone=_SpThirdPartyZone_Object((1,3,6,1,4,1,9694,1,4,1,49),_SpThirdPartyZone_Type())
spThirdPartyZone.setMaxAccess(_C)
if mibBuilder.loadTexts:spThirdPartyZone.setStatus(_B)
class _SpThirdPartyAddr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SpThirdPartyAddr_Type.__name__=_D
_SpThirdPartyAddr_Object=MibScalar
spThirdPartyAddr=_SpThirdPartyAddr_Object((1,3,6,1,4,1,9694,1,4,1,50),_SpThirdPartyAddr_Type())
spThirdPartyAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:spThirdPartyAddr.setStatus(_B)
class _SpMitigationStart_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SpMitigationStart_Type.__name__=_D
_SpMitigationStart_Object=MibScalar
spMitigationStart=_SpMitigationStart_Object((1,3,6,1,4,1,9694,1,4,1,51),_SpMitigationStart_Type())
spMitigationStart.setMaxAccess(_C)
if mibBuilder.loadTexts:spMitigationStart.setStatus(_B)
class _SpBlackholeCommunity_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SpBlackholeCommunity_Type.__name__=_D
_SpBlackholeCommunity_Object=MibScalar
spBlackholeCommunity=_SpBlackholeCommunity_Object((1,3,6,1,4,1,9694,1,4,1,52),_SpBlackholeCommunity_Type())
spBlackholeCommunity.setMaxAccess(_C)
if mibBuilder.loadTexts:spBlackholeCommunity.setStatus(_B)
class _SpBlackholeTimeout_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SpBlackholeTimeout_Type.__name__=_D
_SpBlackholeTimeout_Object=MibScalar
spBlackholeTimeout=_SpBlackholeTimeout_Object((1,3,6,1,4,1,9694,1,4,1,53),_SpBlackholeTimeout_Type())
spBlackholeTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:spBlackholeTimeout.setStatus(_B)
class _SpBlackholePrefix_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SpBlackholePrefix_Type.__name__=_D
_SpBlackholePrefix_Object=MibScalar
spBlackholePrefix=_SpBlackholePrefix_Object((1,3,6,1,4,1,9694,1,4,1,54),_SpBlackholePrefix_Type())
spBlackholePrefix.setMaxAccess(_C)
if mibBuilder.loadTexts:spBlackholePrefix.setStatus(_B)
class _SpBlackholeNexthop_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SpBlackholeNexthop_Type.__name__=_D
_SpBlackholeNexthop_Object=MibScalar
spBlackholeNexthop=_SpBlackholeNexthop_Object((1,3,6,1,4,1,9694,1,4,1,55),_SpBlackholeNexthop_Type())
spBlackholeNexthop.setMaxAccess(_C)
if mibBuilder.loadTexts:spBlackholeNexthop.setStatus(_B)
class _SpFlowspecCommunity_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SpFlowspecCommunity_Type.__name__=_D
_SpFlowspecCommunity_Object=MibScalar
spFlowspecCommunity=_SpFlowspecCommunity_Object((1,3,6,1,4,1,9694,1,4,1,56),_SpFlowspecCommunity_Type())
spFlowspecCommunity.setMaxAccess(_C)
if mibBuilder.loadTexts:spFlowspecCommunity.setStatus(_B)
class _SpFlowspecTimeout_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SpFlowspecTimeout_Type.__name__=_D
_SpFlowspecTimeout_Object=MibScalar
spFlowspecTimeout=_SpFlowspecTimeout_Object((1,3,6,1,4,1,9694,1,4,1,57),_SpFlowspecTimeout_Type())
spFlowspecTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:spFlowspecTimeout.setStatus(_B)
class _SpCommFailureDestination_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,256))
_SpCommFailureDestination_Type.__name__=_D
_SpCommFailureDestination_Object=MibScalar
spCommFailureDestination=_SpCommFailureDestination_Object((1,3,6,1,4,1,9694,1,4,1,58),_SpCommFailureDestination_Type())
spCommFailureDestination.setMaxAccess(_C)
if mibBuilder.loadTexts:spCommFailureDestination.setStatus(_B)
class _SpCommFailureDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,256))
_SpCommFailureDescription_Type.__name__=_D
_SpCommFailureDescription_Object=MibScalar
spCommFailureDescription=_SpCommFailureDescription_Object((1,3,6,1,4,1,9694,1,4,1,59),_SpCommFailureDescription_Type())
spCommFailureDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:spCommFailureDescription.setStatus(_B)
_SpGreTunnelDestination_Type=IpAddress
_SpGreTunnelDestination_Object=MibScalar
spGreTunnelDestination=_SpGreTunnelDestination_Object((1,3,6,1,4,1,9694,1,4,1,60),_SpGreTunnelDestination_Type())
spGreTunnelDestination.setMaxAccess(_C)
if mibBuilder.loadTexts:spGreTunnelDestination.setStatus(_B)
class _SpSystemErrorType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_SpSystemErrorType_Type.__name__=_D
_SpSystemErrorType_Object=MibScalar
spSystemErrorType=_SpSystemErrorType_Object((1,3,6,1,4,1,9694,1,4,1,61),_SpSystemErrorType_Type())
spSystemErrorType.setMaxAccess(_C)
if mibBuilder.loadTexts:spSystemErrorType.setStatus(_B)
class _SpSystemErrorDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,256))
_SpSystemErrorDescription_Type.__name__=_D
_SpSystemErrorDescription_Object=MibScalar
spSystemErrorDescription=_SpSystemErrorDescription_Object((1,3,6,1,4,1,9694,1,4,1,62),_SpSystemErrorDescription_Type())
spSystemErrorDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:spSystemErrorDescription.setStatus(_B)
class _SpServiceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_SpServiceName_Type.__name__=_D
_SpServiceName_Object=MibScalar
spServiceName=_SpServiceName_Object((1,3,6,1,4,1,9694,1,4,1,63),_SpServiceName_Type())
spServiceName.setMaxAccess(_C)
if mibBuilder.loadTexts:spServiceName.setStatus(_B)
class _SpServiceElement_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_SpServiceElement_Type.__name__=_D
_SpServiceElement_Object=MibScalar
spServiceElement=_SpServiceElement_Object((1,3,6,1,4,1,9694,1,4,1,64),_SpServiceElement_Type())
spServiceElement.setMaxAccess(_C)
if mibBuilder.loadTexts:spServiceElement.setStatus(_B)
class _SpApplicationName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_SpApplicationName_Type.__name__=_D
_SpApplicationName_Object=MibScalar
spApplicationName=_SpApplicationName_Object((1,3,6,1,4,1,9694,1,4,1,65),_SpApplicationName_Type())
spApplicationName.setMaxAccess(_C)
if mibBuilder.loadTexts:spApplicationName.setStatus(_B)
class _SpAlertDetectionSignatures_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_SpAlertDetectionSignatures_Type.__name__=_D
_SpAlertDetectionSignatures_Object=MibScalar
spAlertDetectionSignatures=_SpAlertDetectionSignatures_Object((1,3,6,1,4,1,9694,1,4,1,66),_SpAlertDetectionSignatures_Type())
spAlertDetectionSignatures.setMaxAccess(_C)
if mibBuilder.loadTexts:spAlertDetectionSignatures.setStatus(_B)
class _SpManagedObjects_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1024))
_SpManagedObjects_Type.__name__=_D
_SpManagedObjects_Object=MibScalar
spManagedObjects=_SpManagedObjects_Object((1,3,6,1,4,1,9694,1,4,1,67),_SpManagedObjects_Type())
spManagedObjects.setMaxAccess(_C)
if mibBuilder.loadTexts:spManagedObjects.setStatus(_B)
_SpInetAddressType_Type=InetAddressType
_SpInetAddressType_Object=MibScalar
spInetAddressType=_SpInetAddressType_Object((1,3,6,1,4,1,9694,1,4,1,68),_SpInetAddressType_Type())
spInetAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:spInetAddressType.setStatus(_B)
_SpInetAddress_Type=InetAddress
_SpInetAddress_Object=MibScalar
spInetAddress=_SpInetAddress_Object((1,3,6,1,4,1,9694,1,4,1,69),_SpInetAddress_Type())
spInetAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:spInetAddress.setStatus(_B)
_SpImpactBps_Type=Unsigned32
_SpImpactBps_Object=MibScalar
spImpactBps=_SpImpactBps_Object((1,3,6,1,4,1,9694,1,4,1,70),_SpImpactBps_Type())
spImpactBps.setMaxAccess(_C)
if mibBuilder.loadTexts:spImpactBps.setStatus(_B)
_SpImpactPps_Type=Unsigned32
_SpImpactPps_Object=MibScalar
spImpactPps=_SpImpactPps_Object((1,3,6,1,4,1,9694,1,4,1,71),_SpImpactPps_Type())
spImpactPps.setMaxAccess(_C)
if mibBuilder.loadTexts:spImpactPps.setStatus(_B)
class _SpDetectedCountries_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,152))
_SpDetectedCountries_Type.__name__=_D
_SpDetectedCountries_Object=MibScalar
spDetectedCountries=_SpDetectedCountries_Object((1,3,6,1,4,1,9694,1,4,1,72),_SpDetectedCountries_Type())
spDetectedCountries.setMaxAccess(_C)
if mibBuilder.loadTexts:spDetectedCountries.setStatus(_B)
_SpRoutingFailoverInterfaces_Type=DisplayString
_SpRoutingFailoverInterfaces_Object=MibScalar
spRoutingFailoverInterfaces=_SpRoutingFailoverInterfaces_Object((1,3,6,1,4,1,9694,1,4,1,73),_SpRoutingFailoverInterfaces_Type())
spRoutingFailoverInterfaces.setMaxAccess(_C)
if mibBuilder.loadTexts:spRoutingFailoverInterfaces.setStatus(_B)
class _SpPravail_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_SpPravail_Type.__name__=_D
_SpPravail_Object=MibScalar
spPravail=_SpPravail_Object((1,3,6,1,4,1,9694,1,4,1,74),_SpPravail_Type())
spPravail.setMaxAccess(_C)
if mibBuilder.loadTexts:spPravail.setStatus(_B)
class _SpDetector_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_SpDetector_Type.__name__=_D
_SpDetector_Object=MibScalar
spDetector=_SpDetector_Object((1,3,6,1,4,1,9694,1,4,1,75),_SpDetector_Type())
spDetector.setMaxAccess(_C)
if mibBuilder.loadTexts:spDetector.setStatus(_B)
class _SpTMSMultiPrefix_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SpTMSMultiPrefix_Type.__name__=_D
_SpTMSMultiPrefix_Object=MibScalar
spTMSMultiPrefix=_SpTMSMultiPrefix_Object((1,3,6,1,4,1,9694,1,4,1,76),_SpTMSMultiPrefix_Type())
spTMSMultiPrefix.setMaxAccess(_C)
if mibBuilder.loadTexts:spTMSMultiPrefix.setStatus(_B)
class _SpLicenseErrType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_SpLicenseErrType_Type.__name__=_D
_SpLicenseErrType_Object=MibScalar
spLicenseErrType=_SpLicenseErrType_Object((1,3,6,1,4,1,9694,1,4,1,77),_SpLicenseErrType_Type())
spLicenseErrType.setMaxAccess(_C)
if mibBuilder.loadTexts:spLicenseErrType.setStatus(_B)
_SpLicenseErrCount_Type=Unsigned32
_SpLicenseErrCount_Object=MibScalar
spLicenseErrCount=_SpLicenseErrCount_Object((1,3,6,1,4,1,9694,1,4,1,78),_SpLicenseErrCount_Type())
spLicenseErrCount.setMaxAccess(_C)
if mibBuilder.loadTexts:spLicenseErrCount.setStatus(_B)
_SpLicenseErrLimit_Type=Unsigned32
_SpLicenseErrLimit_Object=MibScalar
spLicenseErrLimit=_SpLicenseErrLimit_Object((1,3,6,1,4,1,9694,1,4,1,79),_SpLicenseErrLimit_Type())
spLicenseErrLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:spLicenseErrLimit.setStatus(_B)
class _SpLicenseErrDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1023))
_SpLicenseErrDescription_Type.__name__=_D
_SpLicenseErrDescription_Object=MibScalar
spLicenseErrDescription=_SpLicenseErrDescription_Object((1,3,6,1,4,1,9694,1,4,1,80),_SpLicenseErrDescription_Type())
spLicenseErrDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:spLicenseErrDescription.setStatus(_B)
_SpInterfaceSpeedHC_Type=CounterBasedGauge64
_SpInterfaceSpeedHC_Object=MibScalar
spInterfaceSpeedHC=_SpInterfaceSpeedHC_Object((1,3,6,1,4,1,9694,1,4,1,81),_SpInterfaceSpeedHC_Type())
spInterfaceSpeedHC.setMaxAccess(_C)
if mibBuilder.loadTexts:spInterfaceSpeedHC.setStatus(_B)
_SpInterfaceUsageHC_Type=CounterBasedGauge64
_SpInterfaceUsageHC_Object=MibScalar
spInterfaceUsageHC=_SpInterfaceUsageHC_Object((1,3,6,1,4,1,9694,1,4,1,82),_SpInterfaceUsageHC_Type())
spInterfaceUsageHC.setMaxAccess(_C)
if mibBuilder.loadTexts:spInterfaceUsageHC.setStatus(_B)
class _SpGreTunnelName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,256))
_SpGreTunnelName_Type.__name__=_D
_SpGreTunnelName_Object=MibScalar
spGreTunnelName=_SpGreTunnelName_Object((1,3,6,1,4,1,9694,1,4,1,83),_SpGreTunnelName_Type())
spGreTunnelName.setMaxAccess(_C)
if mibBuilder.loadTexts:spGreTunnelName.setStatus(_B)
class _SpCloudSignalFaultDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,256))
_SpCloudSignalFaultDescription_Type.__name__=_D
_SpCloudSignalFaultDescription_Object=MibScalar
spCloudSignalFaultDescription=_SpCloudSignalFaultDescription_Object((1,3,6,1,4,1,9694,1,4,1,84),_SpCloudSignalFaultDescription_Type())
spCloudSignalFaultDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:spCloudSignalFaultDescription.setStatus(_B)
class _SpTMSMultiDiversionPrefix_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SpTMSMultiDiversionPrefix_Type.__name__=_D
_SpTMSMultiDiversionPrefix_Object=MibScalar
spTMSMultiDiversionPrefix=_SpTMSMultiDiversionPrefix_Object((1,3,6,1,4,1,9694,1,4,1,85),_SpTMSMultiDiversionPrefix_Type())
spTMSMultiDiversionPrefix.setMaxAccess(_C)
if mibBuilder.loadTexts:spTMSMultiDiversionPrefix.setStatus(_B)
class _SpSmartAlertSettingName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_SpSmartAlertSettingName_Type.__name__=_D
_SpSmartAlertSettingName_Object=MibScalar
spSmartAlertSettingName=_SpSmartAlertSettingName_Object((1,3,6,1,4,1,9694,1,4,1,86),_SpSmartAlertSettingName_Type())
spSmartAlertSettingName.setMaxAccess(_C)
if mibBuilder.loadTexts:spSmartAlertSettingName.setStatus(_B)
_SpSmartAlertThreshold_Type=CounterBasedGauge64
_SpSmartAlertThreshold_Object=MibScalar
spSmartAlertThreshold=_SpSmartAlertThreshold_Object((1,3,6,1,4,1,9694,1,4,1,87),_SpSmartAlertThreshold_Type())
spSmartAlertThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:spSmartAlertThreshold.setStatus(_B)
_SpSmartAlertObserved_Type=CounterBasedGauge64
_SpSmartAlertObserved_Object=MibScalar
spSmartAlertObserved=_SpSmartAlertObserved_Object((1,3,6,1,4,1,9694,1,4,1,88),_SpSmartAlertObserved_Type())
spSmartAlertObserved.setMaxAccess(_C)
if mibBuilder.loadTexts:spSmartAlertObserved.setStatus(_B)
class _SpImportance_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_SpImportance_Type.__name__=_D
_SpImportance_Object=MibScalar
spImportance=_SpImportance_Object((1,3,6,1,4,1,9694,1,4,1,89),_SpImportance_Type())
spImportance.setMaxAccess(_C)
if mibBuilder.loadTexts:spImportance.setStatus(_B)
_SpThresholdHC_Type=CounterBasedGauge64
_SpThresholdHC_Object=MibScalar
spThresholdHC=_SpThresholdHC_Object((1,3,6,1,4,1,9694,1,4,1,90),_SpThresholdHC_Type())
spThresholdHC.setMaxAccess(_C)
if mibBuilder.loadTexts:spThresholdHC.setStatus(_B)
_SpUsageHC_Type=CounterBasedGauge64
_SpUsageHC_Object=MibScalar
spUsageHC=_SpUsageHC_Object((1,3,6,1,4,1,9694,1,4,1,91),_SpUsageHC_Type())
spUsageHC.setMaxAccess(_C)
if mibBuilder.loadTexts:spUsageHC.setStatus(_B)
_SpImpactBpsHC_Type=CounterBasedGauge64
_SpImpactBpsHC_Object=MibScalar
spImpactBpsHC=_SpImpactBpsHC_Object((1,3,6,1,4,1,9694,1,4,1,92),_SpImpactBpsHC_Type())
spImpactBpsHC.setMaxAccess(_C)
if mibBuilder.loadTexts:spImpactBpsHC.setStatus(_B)
_SpImpactPpsHC_Type=CounterBasedGauge64
_SpImpactPpsHC_Object=MibScalar
spImpactPpsHC=_SpImpactPpsHC_Object((1,3,6,1,4,1,9694,1,4,1,93),_SpImpactPpsHC_Type())
spImpactPpsHC.setMaxAccess(_C)
if mibBuilder.loadTexts:spImpactPpsHC.setStatus(_B)
class _SpMitOrchestrationSrcTMSGroup_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_SpMitOrchestrationSrcTMSGroup_Type.__name__=_D
_SpMitOrchestrationSrcTMSGroup_Object=MibScalar
spMitOrchestrationSrcTMSGroup=_SpMitOrchestrationSrcTMSGroup_Object((1,3,6,1,4,1,9694,1,4,1,94),_SpMitOrchestrationSrcTMSGroup_Type())
spMitOrchestrationSrcTMSGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:spMitOrchestrationSrcTMSGroup.setStatus(_B)
class _SpMitOrchestrationDestTMSGroup_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_SpMitOrchestrationDestTMSGroup_Type.__name__=_D
_SpMitOrchestrationDestTMSGroup_Object=MibScalar
spMitOrchestrationDestTMSGroup=_SpMitOrchestrationDestTMSGroup_Object((1,3,6,1,4,1,9694,1,4,1,95),_SpMitOrchestrationDestTMSGroup_Type())
spMitOrchestrationDestTMSGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:spMitOrchestrationDestTMSGroup.setStatus(_B)
class _SpSightlineSignalingClientName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_SpSightlineSignalingClientName_Type.__name__=_D
_SpSightlineSignalingClientName_Object=MibScalar
spSightlineSignalingClientName=_SpSightlineSignalingClientName_Object((1,3,6,1,4,1,9694,1,4,1,96),_SpSightlineSignalingClientName_Type())
spSightlineSignalingClientName.setMaxAccess(_C)
if mibBuilder.loadTexts:spSightlineSignalingClientName.setStatus(_B)
class _SpSightlineSignalingMessage_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1024))
_SpSightlineSignalingMessage_Type.__name__=_D
_SpSightlineSignalingMessage_Object=MibScalar
spSightlineSignalingMessage=_SpSightlineSignalingMessage_Object((1,3,6,1,4,1,9694,1,4,1,97),_SpSightlineSignalingMessage_Type())
spSightlineSignalingMessage.setMaxAccess(_C)
if mibBuilder.loadTexts:spSightlineSignalingMessage.setStatus(_B)
_PeakflowSPMgr_ObjectIdentity=ObjectIdentity
peakflowSPMgr=_PeakflowSPMgr_ObjectIdentity((1,3,6,1,4,1,9694,1,4,2))
_DeviceHealth_ObjectIdentity=ObjectIdentity
deviceHealth=_DeviceHealth_ObjectIdentity((1,3,6,1,4,1,9694,1,4,2,1))
_DeviceCpuLoadAvg1min_Type=Integer32
_DeviceCpuLoadAvg1min_Object=MibScalar
deviceCpuLoadAvg1min=_DeviceCpuLoadAvg1min_Object((1,3,6,1,4,1,9694,1,4,2,1,1),_DeviceCpuLoadAvg1min_Type())
deviceCpuLoadAvg1min.setMaxAccess(_H)
if mibBuilder.loadTexts:deviceCpuLoadAvg1min.setStatus(_B)
_DeviceCpuLoadAvg5min_Type=Integer32
_DeviceCpuLoadAvg5min_Object=MibScalar
deviceCpuLoadAvg5min=_DeviceCpuLoadAvg5min_Object((1,3,6,1,4,1,9694,1,4,2,1,2),_DeviceCpuLoadAvg5min_Type())
deviceCpuLoadAvg5min.setMaxAccess(_H)
if mibBuilder.loadTexts:deviceCpuLoadAvg5min.setStatus(_B)
_DeviceCpuLoadAvg15min_Type=Integer32
_DeviceCpuLoadAvg15min_Object=MibScalar
deviceCpuLoadAvg15min=_DeviceCpuLoadAvg15min_Object((1,3,6,1,4,1,9694,1,4,2,1,3),_DeviceCpuLoadAvg15min_Type())
deviceCpuLoadAvg15min.setMaxAccess(_H)
if mibBuilder.loadTexts:deviceCpuLoadAvg15min.setStatus(_B)
class _DeviceDiskUsage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_DeviceDiskUsage_Type.__name__=_a
_DeviceDiskUsage_Object=MibScalar
deviceDiskUsage=_DeviceDiskUsage_Object((1,3,6,1,4,1,9694,1,4,2,1,4),_DeviceDiskUsage_Type())
deviceDiskUsage.setMaxAccess(_H)
if mibBuilder.loadTexts:deviceDiskUsage.setStatus(_B)
_DevicePhysicalMemory_Type=Integer32
_DevicePhysicalMemory_Object=MibScalar
devicePhysicalMemory=_DevicePhysicalMemory_Object((1,3,6,1,4,1,9694,1,4,2,1,5),_DevicePhysicalMemory_Type())
devicePhysicalMemory.setMaxAccess(_H)
if mibBuilder.loadTexts:devicePhysicalMemory.setStatus(_B)
_DevicePhysicalMemoryInUse_Type=Integer32
_DevicePhysicalMemoryInUse_Object=MibScalar
devicePhysicalMemoryInUse=_DevicePhysicalMemoryInUse_Object((1,3,6,1,4,1,9694,1,4,2,1,6),_DevicePhysicalMemoryInUse_Type())
devicePhysicalMemoryInUse.setMaxAccess(_H)
if mibBuilder.loadTexts:devicePhysicalMemoryInUse.setStatus(_B)
class _DevicePhysicalMemoryUsage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_DevicePhysicalMemoryUsage_Type.__name__=_a
_DevicePhysicalMemoryUsage_Object=MibScalar
devicePhysicalMemoryUsage=_DevicePhysicalMemoryUsage_Object((1,3,6,1,4,1,9694,1,4,2,1,7),_DevicePhysicalMemoryUsage_Type())
devicePhysicalMemoryUsage.setMaxAccess(_H)
if mibBuilder.loadTexts:devicePhysicalMemoryUsage.setStatus(_B)
_DeviceSwapSpace_Type=Integer32
_DeviceSwapSpace_Object=MibScalar
deviceSwapSpace=_DeviceSwapSpace_Object((1,3,6,1,4,1,9694,1,4,2,1,8),_DeviceSwapSpace_Type())
deviceSwapSpace.setMaxAccess(_H)
if mibBuilder.loadTexts:deviceSwapSpace.setStatus(_B)
_DeviceSwapSpaceInUse_Type=Integer32
_DeviceSwapSpaceInUse_Object=MibScalar
deviceSwapSpaceInUse=_DeviceSwapSpaceInUse_Object((1,3,6,1,4,1,9694,1,4,2,1,9),_DeviceSwapSpaceInUse_Type())
deviceSwapSpaceInUse.setMaxAccess(_H)
if mibBuilder.loadTexts:deviceSwapSpaceInUse.setStatus(_B)
class _DeviceSwapSpaceUsage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_DeviceSwapSpaceUsage_Type.__name__=_a
_DeviceSwapSpaceUsage_Object=MibScalar
deviceSwapSpaceUsage=_DeviceSwapSpaceUsage_Object((1,3,6,1,4,1,9694,1,4,2,1,10),_DeviceSwapSpaceUsage_Type())
deviceSwapSpaceUsage.setMaxAccess(_H)
if mibBuilder.loadTexts:deviceSwapSpaceUsage.setStatus(_B)
_DeviceTotalFlows_Type=Counter32
_DeviceTotalFlows_Object=MibScalar
deviceTotalFlows=_DeviceTotalFlows_Object((1,3,6,1,4,1,9694,1,4,2,1,11),_DeviceTotalFlows_Type())
deviceTotalFlows.setMaxAccess(_H)
if mibBuilder.loadTexts:deviceTotalFlows.setStatus(_AA)
_DeviceTotalFlowsHC_Type=Counter64
_DeviceTotalFlowsHC_Object=MibScalar
deviceTotalFlowsHC=_DeviceTotalFlowsHC_Object((1,3,6,1,4,1,9694,1,4,2,1,12),_DeviceTotalFlowsHC_Type())
deviceTotalFlowsHC.setMaxAccess(_H)
if mibBuilder.loadTexts:deviceTotalFlowsHC.setStatus(_B)
_PeakflowSPTraps_ObjectIdentity=ObjectIdentity
peakflowSPTraps=_PeakflowSPTraps_ObjectIdentity((1,3,6,1,4,1,9694,1,4,3))
_PeakflowSPTrapsEnumerate_ObjectIdentity=ObjectIdentity
peakflowSPTrapsEnumerate=_PeakflowSPTrapsEnumerate_ObjectIdentity((1,3,6,1,4,1,9694,1,4,3,0))
flowDown=NotificationType((1,3,6,1,4,1,9694,1,4,3,0,1))
flowDown.setObjects(*((_A,_E),(_A,_I)))
if mibBuilder.loadTexts:flowDown.setStatus(_B)
flowUp=NotificationType((1,3,6,1,4,1,9694,1,4,3,0,2))
flowUp.setObjects(*((_A,_E),(_A,_I)))
if mibBuilder.loadTexts:flowUp.setStatus(_B)
snmpDown=NotificationType((1,3,6,1,4,1,9694,1,4,3,0,3))
snmpDown.setObjects(*((_A,_E),(_A,_I)))
if mibBuilder.loadTexts:snmpDown.setStatus(_B)
snmpUp=NotificationType((1,3,6,1,4,1,9694,1,4,3,0,4))
snmpUp.setObjects(*((_A,_E),(_A,_I)))
if mibBuilder.loadTexts:snmpUp.setStatus(_B)
bgpDown=NotificationType((1,3,6,1,4,1,9694,1,4,3,0,5))
bgpDown.setObjects(*((_A,_E),(_A,_I)))
if mibBuilder.loadTexts:bgpDown.setStatus(_B)
bgpUp=NotificationType((1,3,6,1,4,1,9694,1,4,3,0,6))
bgpUp.setObjects(*((_A,_E),(_A,_I)))
if mibBuilder.loadTexts:bgpUp.setStatus(_B)
collectorDown=NotificationType((1,3,6,1,4,1,9694,1,4,3,0,7))
collectorDown.setObjects(*((_A,_E),(_A,_G),(_A,_AB)))
if mibBuilder.loadTexts:collectorDown.setStatus(_B)
collectorUp=NotificationType((1,3,6,1,4,1,9694,1,4,3,0,8))
collectorUp.setObjects(*((_A,_E),(_A,_G)))
if mibBuilder.loadTexts:collectorUp.setStatus(_B)
collectorStart=NotificationType((1,3,6,1,4,1,9694,1,4,3,0,9))
collectorStart.setObjects(*((_A,_E),(_A,_G)))
if mibBuilder.loadTexts:collectorStart.setStatus(_b)
bgpInstability=NotificationType((1,3,6,1,4,1,9694,1,4,3,0,10))
bgpInstability.setObjects(*((_A,_E),(_A,_I),(_A,_AC)))
if mibBuilder.loadTexts:bgpInstability.setStatus(_B)
bgpInstabilityDone=NotificationType((1,3,6,1,4,1,9694,1,4,3,0,11))
bgpInstabilityDone.setObjects(*((_A,_E),(_A,_I)))
if mibBuilder.loadTexts:bgpInstabilityDone.setStatus(_B)
bgpTrap=NotificationType((1,3,6,1,4,1,9694,1,4,3,0,12))
bgpTrap.setObjects(*((_A,_E),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH)))
if mibBuilder.loadTexts:bgpTrap.setStatus(_B)
interfaceUsage=NotificationType((1,3,6,1,4,1,9694,1,4,3,0,13))
interfaceUsage.setObjects(*((_A,_E),(_A,_I),(_A,_k),(_A,_l),(_A,_AI),(_A,_M),(_A,_AJ),(_A,_AK),(_A,_AL)))
if mibBuilder.loadTexts:interfaceUsage.setStatus(_B)
interfaceUsageDone=NotificationType((1,3,6,1,4,1,9694,1,4,3,0,14))
interfaceUsageDone.setObjects(*((_A,_E),(_A,_I),(_A,_k),(_A,_l),(_A,_M)))
if mibBuilder.loadTexts:interfaceUsageDone.setStatus(_B)
autoclassifyStart=NotificationType((1,3,6,1,4,1,9694,1,4,3,0,15))
autoclassifyStart.setObjects(*((_A,_E),(_A,_G),(_A,_m)))
if mibBuilder.loadTexts:autoclassifyStart.setStatus(_b)
configChange=NotificationType((1,3,6,1,4,1,9694,1,4,3,0,16))
configChange.setObjects(*((_A,_E),(_A,_G),(_A,_m),(_A,_AM)))
if mibBuilder.loadTexts:configChange.setStatus(_B)
notificationLimit=NotificationType((1,3,6,1,4,1,9694,1,4,3,0,17))
notificationLimit.setObjects(*((_A,_E),(_A,_G)))
if mibBuilder.loadTexts:notificationLimit.setStatus(_b)
reportDone=NotificationType((1,3,6,1,4,1,9694,1,4,3,0,18))
reportDone.setObjects(*((_A,_AN),(_A,_AO),(_A,_AP)))
if mibBuilder.loadTexts:reportDone.setStatus(_b)
bgpHijack=NotificationType((1,3,6,1,4,1,9694,1,4,3,0,19))
bgpHijack.setObjects(*((_A,_E),(_A,_I),(_A,_AQ),(_A,_AR),(_A,_AS)))
if mibBuilder.loadTexts:bgpHijack.setStatus(_B)
managedObjectUsage=NotificationType((1,3,6,1,4,1,9694,1,4,3,0,20))
managedObjectUsage.setObjects(*((_A,_E),(_A,_J),(_A,_n),(_A,_M),(_A,_N),(_A,_c),(_A,_d),(_A,_e),(_A,_P)))
if mibBuilder.loadTexts:managedObjectUsage.setStatus(_B)
managedObjectUsageDone=NotificationType((1,3,6,1,4,1,9694,1,4,3,0,21))
managedObjectUsageDone.setObjects(*((_A,_E),(_A,_J),(_A,_n),(_A,_M),(_A,_P)))
if mibBuilder.loadTexts:managedObjectUsageDone.setStatus(_B)
hardwareFailure=NotificationType((1,3,6,1,4,1,9694,1,4,3,0,22))
hardwareFailure.setObjects(*((_A,_E),(_A,_G),(_A,_o)))
if mibBuilder.loadTexts:hardwareFailure.setStatus(_B)
hardwareFailureDone=NotificationType((1,3,6,1,4,1,9694,1,4,3,0,23))
hardwareFailureDone.setObjects(*((_A,_E),(_A,_G),(_A,_o)))
if mibBuilder.loadTexts:hardwareFailureDone.setStatus(_B)
fingerprintFeedback=NotificationType((1,3,6,1,4,1,9694,1,4,3,0,24))
fingerprintFeedback.setObjects(*((_A,_K),(_A,_V),(_A,_AT)))
if mibBuilder.loadTexts:fingerprintFeedback.setStatus(_B)
fingerprintReceive=NotificationType((1,3,6,1,4,1,9694,1,4,3,0,25))
fingerprintReceive.setObjects(*((_A,_K),(_A,_V),(_A,_AU),(_A,_AV)))
if mibBuilder.loadTexts:fingerprintReceive.setStatus(_B)
dnsBaseline=NotificationType((1,3,6,1,4,1,9694,1,4,3,0,26))
dnsBaseline.setObjects(*((_A,_E),(_A,_G),(_A,_p),(_A,_q),(_A,_AW)))
if mibBuilder.loadTexts:dnsBaseline.setStatus(_B)
dnsBaselineDone=NotificationType((1,3,6,1,4,1,9694,1,4,3,0,27))
dnsBaselineDone.setObjects(*((_A,_E),(_A,_G),(_A,_p),(_A,_q),(_A,_AX),(_A,_AY)))
if mibBuilder.loadTexts:dnsBaselineDone.setStatus(_B)
alertScript=NotificationType((1,3,6,1,4,1,9694,1,4,3,0,28))
alertScript.setObjects(*((_A,_K),(_A,_G),(_A,_O),(_A,_AZ),(_A,_Aa),(_A,_Ab),(_A,_Ac)))
if mibBuilder.loadTexts:alertScript.setStatus(_B)
mitigationDone=NotificationType((1,3,6,1,4,1,9694,1,4,3,0,29))
mitigationDone.setObjects(*((_A,_K),(_A,_E),(_A,_G)))
if mibBuilder.loadTexts:mitigationDone.setStatus(_B)
mitigationTMSStart=NotificationType((1,3,6,1,4,1,9694,1,4,3,0,30))
mitigationTMSStart.setObjects(*((_A,_K),(_A,_O),(_A,_E),(_A,_J),(_A,_r),(_A,_s),(_A,_t),(_A,_Q),(_A,_u)))
if mibBuilder.loadTexts:mitigationTMSStart.setStatus(_AA)
mitigationThirdPartyStart=NotificationType((1,3,6,1,4,1,9694,1,4,3,0,31))
mitigationThirdPartyStart.setObjects(*((_A,_K),(_A,_O),(_A,_E),(_A,_J),(_A,_Ad),(_A,_Ae),(_A,_Q)))
if mibBuilder.loadTexts:mitigationThirdPartyStart.setStatus(_B)
mitigationBlackholeStart=NotificationType((1,3,6,1,4,1,9694,1,4,3,0,32))
mitigationBlackholeStart.setObjects(*((_A,_K),(_A,_O),(_A,_E),(_A,_Af),(_A,_Ag),(_A,_Ah),(_A,_Ai),(_A,_Q)))
if mibBuilder.loadTexts:mitigationBlackholeStart.setStatus(_B)
mitigationFlowspecStart=NotificationType((1,3,6,1,4,1,9694,1,4,3,0,33))
mitigationFlowspecStart.setObjects(*((_A,_K),(_A,_O),(_A,_E),(_A,_Aj),(_A,_Ak),(_A,_Q)))
if mibBuilder.loadTexts:mitigationFlowspecStart.setStatus(_B)
spcommFailure=NotificationType((1,3,6,1,4,1,9694,1,4,3,0,34))
spcommFailure.setObjects(*((_A,_E),(_A,_G),(_A,_v),(_A,_w)))
if mibBuilder.loadTexts:spcommFailure.setStatus(_B)
spcommFailureDone=NotificationType((1,3,6,1,4,1,9694,1,4,3,0,35))
spcommFailureDone.setObjects(*((_A,_E),(_A,_G),(_A,_v),(_A,_w)))
if mibBuilder.loadTexts:spcommFailureDone.setStatus(_B)
greDown=NotificationType((1,3,6,1,4,1,9694,1,4,3,0,36))
greDown.setObjects(*((_A,_E),(_A,_x),(_A,_y)))
if mibBuilder.loadTexts:greDown.setStatus(_B)
greDownDone=NotificationType((1,3,6,1,4,1,9694,1,4,3,0,37))
greDownDone.setObjects(*((_A,_E),(_A,_x),(_A,_y)))
if mibBuilder.loadTexts:greDownDone.setStatus(_B)
deviceSystemError=NotificationType((1,3,6,1,4,1,9694,1,4,3,0,38))
deviceSystemError.setObjects(*((_A,_E),(_A,_G),(_A,_z),(_A,_N),(_A,_A0)))
if mibBuilder.loadTexts:deviceSystemError.setStatus(_B)
deviceSystemErrorDone=NotificationType((1,3,6,1,4,1,9694,1,4,3,0,39))
deviceSystemErrorDone.setObjects(*((_A,_E),(_A,_G),(_A,_z),(_A,_N),(_A,_A0)))
if mibBuilder.loadTexts:deviceSystemErrorDone.setStatus(_B)
fingerprintUsage=NotificationType((1,3,6,1,4,1,9694,1,4,3,0,40))
fingerprintUsage.setObjects(*((_A,_E),(_A,_V),(_A,_M),(_A,_N),(_A,_c),(_A,_d),(_A,_e),(_A,_P)))
if mibBuilder.loadTexts:fingerprintUsage.setStatus(_B)
fingerprintUsageDone=NotificationType((1,3,6,1,4,1,9694,1,4,3,0,41))
fingerprintUsageDone.setObjects(*((_A,_E),(_A,_V),(_A,_M),(_A,_P)))
if mibBuilder.loadTexts:fingerprintUsageDone.setStatus(_B)
serviceUsage=NotificationType((1,3,6,1,4,1,9694,1,4,3,0,42))
serviceUsage.setObjects(*((_A,_E),(_A,_A1),(_A,_M),(_A,_Al),(_A,_Am),(_A,_N),(_A,_c),(_A,_d),(_A,_e)))
if mibBuilder.loadTexts:serviceUsage.setStatus(_B)
serviceUsageDone=NotificationType((1,3,6,1,4,1,9694,1,4,3,0,43))
serviceUsageDone.setObjects(*((_A,_E),(_A,_A1)))
if mibBuilder.loadTexts:serviceUsageDone.setStatus(_B)
dosNetworkProfiledAlert=NotificationType((1,3,6,1,4,1,9694,1,4,3,0,44))
dosNetworkProfiledAlert.setObjects(*((_A,_E),(_F,_R),(_F,_S),(_F,_U),(_F,_T),(_F,_L),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_J),(_A,_A2)))
if mibBuilder.loadTexts:dosNetworkProfiledAlert.setStatus(_B)
dosNetworkProfiledAlertDone=NotificationType((1,3,6,1,4,1,9694,1,4,3,0,45))
dosNetworkProfiledAlertDone.setObjects(*((_A,_E),(_F,_R),(_F,_S),(_F,_U),(_F,_T),(_F,_L),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_J),(_A,_A2)))
if mibBuilder.loadTexts:dosNetworkProfiledAlertDone.setStatus(_B)
dosHostDetectionAlert=NotificationType((1,3,6,1,4,1,9694,1,4,3,0,46))
dosHostDetectionAlert.setObjects(*((_A,_E),(_A,_f),(_F,_S),(_F,_U),(_F,_T),(_F,_L),(_A,_g),(_A,_h),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_F,_R),(_A,_i)))
if mibBuilder.loadTexts:dosHostDetectionAlert.setStatus(_B)
dosHostDetectionAlertDone=NotificationType((1,3,6,1,4,1,9694,1,4,3,0,47))
dosHostDetectionAlertDone.setObjects(*((_A,_E),(_A,_f),(_F,_S),(_F,_U),(_F,_T),(_F,_L),(_A,_g),(_A,_h),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_F,_R),(_A,_i)))
if mibBuilder.loadTexts:dosHostDetectionAlertDone.setStatus(_B)
routingFailover=NotificationType((1,3,6,1,4,1,9694,1,4,3,0,48))
routingFailover.setObjects(*((_A,_E),(_F,_L),(_A,_G)))
if mibBuilder.loadTexts:routingFailover.setStatus(_B)
routingFailoverInterfaceDownAlert=NotificationType((1,3,6,1,4,1,9694,1,4,3,0,49))
routingFailoverInterfaceDownAlert.setObjects(*((_A,_E),(_F,_L),(_A,_G),(_A,_An)))
if mibBuilder.loadTexts:routingFailoverInterfaceDownAlert.setStatus(_B)
routingFailoverInterfaceDownAlertDone=NotificationType((1,3,6,1,4,1,9694,1,4,3,0,50))
routingFailoverInterfaceDownAlertDone.setObjects(*((_A,_E),(_F,_L),(_A,_G)))
if mibBuilder.loadTexts:routingFailoverInterfaceDownAlertDone.setStatus(_B)
trafficAutoMitigation=NotificationType((1,3,6,1,4,1,9694,1,4,3,0,51))
trafficAutoMitigation.setObjects((_A,_J))
if mibBuilder.loadTexts:trafficAutoMitigation.setStatus(_B)
cloudSignalingMitigationRequest=NotificationType((1,3,6,1,4,1,9694,1,4,3,0,52))
cloudSignalingMitigationRequest.setObjects(*((_A,_J),(_A,_j)))
if mibBuilder.loadTexts:cloudSignalingMitigationRequest.setStatus(_B)
licenseError=NotificationType((1,3,6,1,4,1,9694,1,4,3,0,53))
licenseError.setObjects(*((_A,_E),(_A,_A3),(_A,_Ao),(_A,_N),(_A,_A4)))
if mibBuilder.loadTexts:licenseError.setStatus(_B)
licenseErrorDone=NotificationType((1,3,6,1,4,1,9694,1,4,3,0,54))
licenseErrorDone.setObjects(*((_A,_E),(_A,_A3),(_A,_N),(_A,_Ap),(_A,_A4)))
if mibBuilder.loadTexts:licenseErrorDone.setStatus(_B)
cloudSignalingFault=NotificationType((1,3,6,1,4,1,9694,1,4,3,0,55))
cloudSignalingFault.setObjects(*((_A,_E),(_A,_j),(_A,_A5)))
if mibBuilder.loadTexts:cloudSignalingFault.setStatus(_B)
cloudSignalingFaultDone=NotificationType((1,3,6,1,4,1,9694,1,4,3,0,56))
cloudSignalingFaultDone.setObjects(*((_A,_E),(_A,_j),(_A,_A5)))
if mibBuilder.loadTexts:cloudSignalingFaultDone.setStatus(_B)
mitigationTMSStartV2=NotificationType((1,3,6,1,4,1,9694,1,4,3,0,57))
mitigationTMSStartV2.setObjects(*((_A,_K),(_A,_O),(_A,_E),(_A,_J),(_A,_r),(_A,_s),(_A,_t),(_A,_Q),(_A,_u),(_A,_Aq)))
if mibBuilder.loadTexts:mitigationTMSStartV2.setStatus(_B)
aifTemplatesUpdated=NotificationType((1,3,6,1,4,1,9694,1,4,3,0,58))
if mibBuilder.loadTexts:aifTemplatesUpdated.setStatus(_B)
smartThresholdAlert=NotificationType((1,3,6,1,4,1,9694,1,4,3,0,59))
smartThresholdAlert.setObjects(*((_A,_E),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_P),(_A,_A9)))
if mibBuilder.loadTexts:smartThresholdAlert.setStatus(_B)
smartThresholdAlertDone=NotificationType((1,3,6,1,4,1,9694,1,4,3,0,60))
smartThresholdAlertDone.setObjects(*((_A,_E),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_P),(_A,_A9)))
if mibBuilder.loadTexts:smartThresholdAlertDone.setStatus(_B)
mitigationOrchestrationAlert=NotificationType((1,3,6,1,4,1,9694,1,4,3,0,61))
mitigationOrchestrationAlert.setObjects(*((_A,_E),(_A,_G),(_A,_O),(_A,_Ar),(_A,_As)))
if mibBuilder.loadTexts:mitigationOrchestrationAlert.setStatus(_B)
sightlineSignalingAlert=NotificationType((1,3,6,1,4,1,9694,1,4,3,0,62))
sightlineSignalingAlert.setObjects(*((_A,_E),(_A,_At),(_A,_i),(_A,_f),(_A,_g),(_A,_h),(_A,_Au)))
if mibBuilder.loadTexts:sightlineSignalingAlert.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'peakflowSPMIB':peakflowSPMIB,'peakflowSPCMI':peakflowSPCMI,_G:spCollector,_I:spRouter,_k:spInterface,_l:spInterfaceIndex,'spDuration':spDuration,'spBGPEvent':spBGPEvent,_AC:spBGPInstability,_AD:spBGPTrapName,_AE:spBGPTrapEvent,_AF:spBGPTrapPrefix,_AG:spBGPTrapOldAttributes,_AH:spBGPTrapNewAttributes,_AI:spInterfaceSpeed,_AJ:spInterfaceUsage,_AP:spReportURL,_AN:spReportName,_AO:spReportID,_E:spAlertID,_AQ:spHijackRoute,_AR:spHijackAttr,_AS:spHijackLocal,_m:spUsername,_AM:spVersion,_M:spUsageType,_J:spManagedObject,_n:spManagedObjectFamily,_N:spThreshold,_c:spUsage,_P:spUnit,_o:spHardwareFailureDescription,_V:spFingerprintName,_AT:spFingerprintFeedback,_AU:spFingerprintSender,_AV:spFingerprintMessage,_K:spMitigationID,_p:spDNSName,_q:spDNSExpected,_AW:spDNSObserved,_AX:spDNSObservedMean,_AY:spDNSObservedMax,_O:spMitigationName,_AZ:spScriptCommand,_Aa:spScriptHost,_Ab:spScriptPort,_Ac:spScriptStart,_r:spTMSPrefix,_s:spTMSCommunity,_t:spTMSTimeout,_Ad:spThirdPartyZone,_Ae:spThirdPartyAddr,_Q:spMitigationStart,_Af:spBlackholeCommunity,_Ag:spBlackholeTimeout,_Ah:spBlackholePrefix,_Ai:spBlackholeNexthop,_Aj:spFlowspecCommunity,_Ak:spFlowspecTimeout,_v:spCommFailureDestination,_w:spCommFailureDescription,_x:spGreTunnelDestination,_z:spSystemErrorType,_A0:spSystemErrorDescription,_A1:spServiceName,_Am:spServiceElement,_Al:spApplicationName,_f:spAlertDetectionSignatures,_i:spManagedObjects,_h:spInetAddressType,_g:spInetAddress,_W:spImpactBps,_X:spImpactPps,_A2:spDetectedCountries,_An:spRoutingFailoverInterfaces,_j:spPravail,_AB:spDetector,_u:spTMSMultiPrefix,_A3:spLicenseErrType,_Ao:spLicenseErrCount,_Ap:spLicenseErrLimit,_A4:spLicenseErrDescription,_AK:spInterfaceSpeedHC,_AL:spInterfaceUsageHC,_y:spGreTunnelName,_A5:spCloudSignalFaultDescription,_Aq:spTMSMultiDiversionPrefix,_A6:spSmartAlertSettingName,_A7:spSmartAlertThreshold,_A8:spSmartAlertObserved,_A9:spImportance,_d:spThresholdHC,_e:spUsageHC,_Y:spImpactBpsHC,_Z:spImpactPpsHC,_Ar:spMitOrchestrationSrcTMSGroup,_As:spMitOrchestrationDestTMSGroup,_At:spSightlineSignalingClientName,_Au:spSightlineSignalingMessage,'peakflowSPMgr':peakflowSPMgr,'deviceHealth':deviceHealth,'deviceCpuLoadAvg1min':deviceCpuLoadAvg1min,'deviceCpuLoadAvg5min':deviceCpuLoadAvg5min,'deviceCpuLoadAvg15min':deviceCpuLoadAvg15min,'deviceDiskUsage':deviceDiskUsage,'devicePhysicalMemory':devicePhysicalMemory,'devicePhysicalMemoryInUse':devicePhysicalMemoryInUse,'devicePhysicalMemoryUsage':devicePhysicalMemoryUsage,'deviceSwapSpace':deviceSwapSpace,'deviceSwapSpaceInUse':deviceSwapSpaceInUse,'deviceSwapSpaceUsage':deviceSwapSpaceUsage,'deviceTotalFlows':deviceTotalFlows,'deviceTotalFlowsHC':deviceTotalFlowsHC,'peakflowSPTraps':peakflowSPTraps,'peakflowSPTrapsEnumerate':peakflowSPTrapsEnumerate,'flowDown':flowDown,'flowUp':flowUp,'snmpDown':snmpDown,'snmpUp':snmpUp,'bgpDown':bgpDown,'bgpUp':bgpUp,'collectorDown':collectorDown,'collectorUp':collectorUp,'collectorStart':collectorStart,'bgpInstability':bgpInstability,'bgpInstabilityDone':bgpInstabilityDone,'bgpTrap':bgpTrap,'interfaceUsage':interfaceUsage,'interfaceUsageDone':interfaceUsageDone,'autoclassifyStart':autoclassifyStart,'configChange':configChange,'notificationLimit':notificationLimit,'reportDone':reportDone,'bgpHijack':bgpHijack,'managedObjectUsage':managedObjectUsage,'managedObjectUsageDone':managedObjectUsageDone,'hardwareFailure':hardwareFailure,'hardwareFailureDone':hardwareFailureDone,'fingerprintFeedback':fingerprintFeedback,'fingerprintReceive':fingerprintReceive,'dnsBaseline':dnsBaseline,'dnsBaselineDone':dnsBaselineDone,'alertScript':alertScript,'mitigationDone':mitigationDone,'mitigationTMSStart':mitigationTMSStart,'mitigationThirdPartyStart':mitigationThirdPartyStart,'mitigationBlackholeStart':mitigationBlackholeStart,'mitigationFlowspecStart':mitigationFlowspecStart,'spcommFailure':spcommFailure,'spcommFailureDone':spcommFailureDone,'greDown':greDown,'greDownDone':greDownDone,'deviceSystemError':deviceSystemError,'deviceSystemErrorDone':deviceSystemErrorDone,'fingerprintUsage':fingerprintUsage,'fingerprintUsageDone':fingerprintUsageDone,'serviceUsage':serviceUsage,'serviceUsageDone':serviceUsageDone,'dosNetworkProfiledAlert':dosNetworkProfiledAlert,'dosNetworkProfiledAlertDone':dosNetworkProfiledAlertDone,'dosHostDetectionAlert':dosHostDetectionAlert,'dosHostDetectionAlertDone':dosHostDetectionAlertDone,'routingFailover':routingFailover,'routingFailoverInterfaceDownAlert':routingFailoverInterfaceDownAlert,'routingFailoverInterfaceDownAlertDone':routingFailoverInterfaceDownAlertDone,'trafficAutoMitigation':trafficAutoMitigation,'cloudSignalingMitigationRequest':cloudSignalingMitigationRequest,'licenseError':licenseError,'licenseErrorDone':licenseErrorDone,'cloudSignalingFault':cloudSignalingFault,'cloudSignalingFaultDone':cloudSignalingFaultDone,'mitigationTMSStartV2':mitigationTMSStartV2,'aifTemplatesUpdated':aifTemplatesUpdated,'smartThresholdAlert':smartThresholdAlert,'smartThresholdAlertDone':smartThresholdAlertDone,'mitigationOrchestrationAlert':mitigationOrchestrationAlert,'sightlineSignalingAlert':sightlineSignalingAlert})