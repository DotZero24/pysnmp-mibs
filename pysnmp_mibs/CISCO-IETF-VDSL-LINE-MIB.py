_AM='cvdslSCMGroup'
_AL='cvdslMCMGroup'
_AK='cvdslGroup'
_AJ='cvdslInitFailureNotification'
_AI='cvdslSCMConfProfileRowStatus'
_AH='cvdslSCMConfProfileCenterFrequency'
_AG='cvdslSCMConfProfileConstellationSize'
_AF='cvdslSCMConfProfileSymbolRateProfile'
_AE='cvdslSCMConfProfileTransmitPSDLevel'
_AD='cvdslSCMConfProfileTransmitPSDMask'
_AC='cvdslSCMConfProfileFastCodewordSize'
_AB='cvdslSCMConfProfileInterleaveDepth'
_AA='cvdslMCMConfProfileMaxRxPSDRowStatus'
_A9='cvdslMCMConfProfileMaxRxPSDPSD'
_A8='cvdslMCMConfProfileMaxRxPSDTone'
_A7='cvdslMCMConfProfileMaxTxPSDRowStatus'
_A6='cvdslMCMConfProfileMaxTxPSDPSD'
_A5='cvdslMCMConfProfileMaxTxPSDTone'
_A4='cvdslMCMConfProfileTxPSDRowStatus'
_A3='cvdslMCMConfProfileTxPSDPSD'
_A2='cvdslMCMConfProfileTxPSDTone'
_A1='cvdslMCMConfProfileRxBandRowStatus'
_A0='cvdslMCMConfProfileRxBandStop'
_z='cvdslMCMConfProfileRxBandStart'
_y='cvdslMCMConfProfileTxBandRowStatus'
_x='cvdslMCMConfProfileTxBandStop'
_w='cvdslMCMConfProfileTxBandStart'
_v='cvdslMCMConfProfileRowStatus'
_u='cvdslMCMConfProfileTxWindowLength'
_t='cvdslLineAlarmConfProfileRowStatus'
_s='cvdslInitFailureNotificationEnable'
_r='cvdslLineAlarmConfProfileName'
_q='cvdslLineConfProfileRowStatus'
_p='cvdslLineConfRxSpeed'
_o='cvdslLineConfTxSpeed'
_n='cvdslLineConfTargetSnrMgn'
_m='cvdslLineConfProfileName'
_l='cvdslChanCrcBlockLength'
_k='cvdslChanInterleaveDelay'
_j='cvdslCurrAttainableRate'
_i='cvdslCurrOutputPwr'
_h='cvdslCurrAtn'
_g='cvdslCurrSnrMgn'
_f='cvdslInvVersionNumber'
_e='cvdslInvVendorID'
_d='cvdslInvSerialNumber'
_c='cvdslLineAlarmConfProfile'
_b='cvdslLineConfProfile'
_a='cvdslLineType'
_Z='cvdslLineCoding'
_Y='cvdslLineAlarmConfProfileIndex'
_X='octets'
_W='cvdslMCMConfProfileMaxRxPSDNumber'
_V='cvdslMCMConfProfileMaxTxPSDNumber'
_U='cvdslMCMConfProfileTxPSDNumber'
_T='cvdslMCMConfProfileRxBandNumber'
_S='cvdslMCMConfProfileTxBandNumber'
_R='bits per second'
_Q='read-write'
_P='Gauge32'
_O='cvdslCurrStatus'
_N='0.5dB'
_M='tenth dB'
_L='Bits'
_K='ifIndex'
_J='IF-MIB'
_I='SnmpAdminString'
_H='not-accessible'
_G='cvdslLineConfProfileIndex'
_F='cvdslPhysSide'
_E='read-only'
_D='Integer32'
_C='read-create'
_B='CISCO-IETF-VDSL-LINE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
ifIndex,=mibBuilder.importSymbols(_J,_K)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_I)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_L,'Counter32','Counter64',_P,_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
ciscoIetfVdslMIB=ModuleIdentity((1,3,6,1,4,1,9,10,87))
if mibBuilder.loadTexts:ciscoIetfVdslMIB.setRevisions(('2002-04-18 00:00',))
class CVdslLineCodingType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('other',1),('mcm',2),('scm',3)))
class CVdslLineEntity(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('vtuc',1),('vtur',2)))
_CvdslLineMib_ObjectIdentity=ObjectIdentity
cvdslLineMib=_CvdslLineMib_ObjectIdentity((1,3,6,1,4,1,9,10,87,1))
_CvdslNotifications_ObjectIdentity=ObjectIdentity
cvdslNotifications=_CvdslNotifications_ObjectIdentity((1,3,6,1,4,1,9,10,87,1,0))
_CvdslMibObjects_ObjectIdentity=ObjectIdentity
cvdslMibObjects=_CvdslMibObjects_ObjectIdentity((1,3,6,1,4,1,9,10,87,1,1))
_CvdslLineTable_Object=MibTable
cvdslLineTable=_CvdslLineTable_Object((1,3,6,1,4,1,9,10,87,1,1,1))
if mibBuilder.loadTexts:cvdslLineTable.setStatus(_A)
_CvdslLineEntry_Object=MibTableRow
cvdslLineEntry=_CvdslLineEntry_Object((1,3,6,1,4,1,9,10,87,1,1,1,1))
cvdslLineEntry.setIndexNames((0,_J,_K))
if mibBuilder.loadTexts:cvdslLineEntry.setStatus(_A)
_CvdslLineCoding_Type=CVdslLineCodingType
_CvdslLineCoding_Object=MibTableColumn
cvdslLineCoding=_CvdslLineCoding_Object((1,3,6,1,4,1,9,10,87,1,1,1,1,1),_CvdslLineCoding_Type())
cvdslLineCoding.setMaxAccess(_E)
if mibBuilder.loadTexts:cvdslLineCoding.setStatus(_A)
class _CvdslLineType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('noChannel',1),('fastOnly',2),('slowOnly',3),('either',4),('both',5)))
_CvdslLineType_Type.__name__=_D
_CvdslLineType_Object=MibTableColumn
cvdslLineType=_CvdslLineType_Object((1,3,6,1,4,1,9,10,87,1,1,1,1,2),_CvdslLineType_Type())
cvdslLineType.setMaxAccess(_E)
if mibBuilder.loadTexts:cvdslLineType.setStatus(_A)
_CvdslLineConfProfile_Type=Integer32
_CvdslLineConfProfile_Object=MibTableColumn
cvdslLineConfProfile=_CvdslLineConfProfile_Object((1,3,6,1,4,1,9,10,87,1,1,1,1,3),_CvdslLineConfProfile_Type())
cvdslLineConfProfile.setMaxAccess(_Q)
if mibBuilder.loadTexts:cvdslLineConfProfile.setStatus(_A)
_CvdslLineAlarmConfProfile_Type=Integer32
_CvdslLineAlarmConfProfile_Object=MibTableColumn
cvdslLineAlarmConfProfile=_CvdslLineAlarmConfProfile_Object((1,3,6,1,4,1,9,10,87,1,1,1,1,4),_CvdslLineAlarmConfProfile_Type())
cvdslLineAlarmConfProfile.setMaxAccess(_Q)
if mibBuilder.loadTexts:cvdslLineAlarmConfProfile.setStatus(_A)
_CvdslPhysTable_Object=MibTable
cvdslPhysTable=_CvdslPhysTable_Object((1,3,6,1,4,1,9,10,87,1,1,2))
if mibBuilder.loadTexts:cvdslPhysTable.setStatus(_A)
_CvdslPhysEntry_Object=MibTableRow
cvdslPhysEntry=_CvdslPhysEntry_Object((1,3,6,1,4,1,9,10,87,1,1,2,1))
cvdslPhysEntry.setIndexNames((0,_J,_K),(0,_B,_F))
if mibBuilder.loadTexts:cvdslPhysEntry.setStatus(_A)
_CvdslPhysSide_Type=CVdslLineEntity
_CvdslPhysSide_Object=MibTableColumn
cvdslPhysSide=_CvdslPhysSide_Object((1,3,6,1,4,1,9,10,87,1,1,2,1,1),_CvdslPhysSide_Type())
cvdslPhysSide.setMaxAccess(_H)
if mibBuilder.loadTexts:cvdslPhysSide.setStatus(_A)
class _CvdslInvSerialNumber_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CvdslInvSerialNumber_Type.__name__=_I
_CvdslInvSerialNumber_Object=MibTableColumn
cvdslInvSerialNumber=_CvdslInvSerialNumber_Object((1,3,6,1,4,1,9,10,87,1,1,2,1,2),_CvdslInvSerialNumber_Type())
cvdslInvSerialNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:cvdslInvSerialNumber.setStatus(_A)
class _CvdslInvVendorID_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_CvdslInvVendorID_Type.__name__=_I
_CvdslInvVendorID_Object=MibTableColumn
cvdslInvVendorID=_CvdslInvVendorID_Object((1,3,6,1,4,1,9,10,87,1,1,2,1,3),_CvdslInvVendorID_Type())
cvdslInvVendorID.setMaxAccess(_E)
if mibBuilder.loadTexts:cvdslInvVendorID.setStatus(_A)
class _CvdslInvVersionNumber_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_CvdslInvVersionNumber_Type.__name__=_I
_CvdslInvVersionNumber_Object=MibTableColumn
cvdslInvVersionNumber=_CvdslInvVersionNumber_Object((1,3,6,1,4,1,9,10,87,1,1,2,1,4),_CvdslInvVersionNumber_Type())
cvdslInvVersionNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:cvdslInvVersionNumber.setStatus(_A)
class _CvdslCurrSnrMgn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-640,640))
_CvdslCurrSnrMgn_Type.__name__=_D
_CvdslCurrSnrMgn_Object=MibTableColumn
cvdslCurrSnrMgn=_CvdslCurrSnrMgn_Object((1,3,6,1,4,1,9,10,87,1,1,2,1,5),_CvdslCurrSnrMgn_Type())
cvdslCurrSnrMgn.setMaxAccess(_E)
if mibBuilder.loadTexts:cvdslCurrSnrMgn.setStatus(_A)
if mibBuilder.loadTexts:cvdslCurrSnrMgn.setUnits(_M)
class _CvdslCurrAtn_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,630))
_CvdslCurrAtn_Type.__name__=_P
_CvdslCurrAtn_Object=MibTableColumn
cvdslCurrAtn=_CvdslCurrAtn_Object((1,3,6,1,4,1,9,10,87,1,1,2,1,6),_CvdslCurrAtn_Type())
cvdslCurrAtn.setMaxAccess(_E)
if mibBuilder.loadTexts:cvdslCurrAtn.setStatus(_A)
if mibBuilder.loadTexts:cvdslCurrAtn.setUnits(_M)
class _CvdslCurrStatus_Type(Bits):namedValues=NamedValues(*(('noDefect',0),('lossOfFraming',1),('lossOfSignal',2),('lossOfPower',3),('lossOfSignalQuality',4),('lossOfLink',5),('dataInitFailure',6),('configInitFailure',7),('protocolInitFailure',8),('noPeerVtuPresent',9)))
_CvdslCurrStatus_Type.__name__=_L
_CvdslCurrStatus_Object=MibTableColumn
cvdslCurrStatus=_CvdslCurrStatus_Object((1,3,6,1,4,1,9,10,87,1,1,2,1,7),_CvdslCurrStatus_Type())
cvdslCurrStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cvdslCurrStatus.setStatus(_A)
class _CvdslCurrOutputPwr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-310,310))
_CvdslCurrOutputPwr_Type.__name__=_D
_CvdslCurrOutputPwr_Object=MibTableColumn
cvdslCurrOutputPwr=_CvdslCurrOutputPwr_Object((1,3,6,1,4,1,9,10,87,1,1,2,1,8),_CvdslCurrOutputPwr_Type())
cvdslCurrOutputPwr.setMaxAccess(_E)
if mibBuilder.loadTexts:cvdslCurrOutputPwr.setStatus(_A)
if mibBuilder.loadTexts:cvdslCurrOutputPwr.setUnits('tenth dBm')
_CvdslCurrAttainableRate_Type=Gauge32
_CvdslCurrAttainableRate_Object=MibTableColumn
cvdslCurrAttainableRate=_CvdslCurrAttainableRate_Object((1,3,6,1,4,1,9,10,87,1,1,2,1,9),_CvdslCurrAttainableRate_Type())
cvdslCurrAttainableRate.setMaxAccess(_E)
if mibBuilder.loadTexts:cvdslCurrAttainableRate.setStatus(_A)
if mibBuilder.loadTexts:cvdslCurrAttainableRate.setUnits('bps')
_CvdslChanTable_Object=MibTable
cvdslChanTable=_CvdslChanTable_Object((1,3,6,1,4,1,9,10,87,1,1,3))
if mibBuilder.loadTexts:cvdslChanTable.setStatus(_A)
_CvdslChanEntry_Object=MibTableRow
cvdslChanEntry=_CvdslChanEntry_Object((1,3,6,1,4,1,9,10,87,1,1,3,1))
cvdslChanEntry.setIndexNames((0,_J,_K),(0,_B,_F))
if mibBuilder.loadTexts:cvdslChanEntry.setStatus(_A)
_CvdslChanInterleaveDelay_Type=Gauge32
_CvdslChanInterleaveDelay_Object=MibTableColumn
cvdslChanInterleaveDelay=_CvdslChanInterleaveDelay_Object((1,3,6,1,4,1,9,10,87,1,1,3,1,1),_CvdslChanInterleaveDelay_Type())
cvdslChanInterleaveDelay.setMaxAccess(_E)
if mibBuilder.loadTexts:cvdslChanInterleaveDelay.setStatus(_A)
if mibBuilder.loadTexts:cvdslChanInterleaveDelay.setUnits('milli-seconds')
_CvdslChanCrcBlockLength_Type=Gauge32
_CvdslChanCrcBlockLength_Object=MibTableColumn
cvdslChanCrcBlockLength=_CvdslChanCrcBlockLength_Object((1,3,6,1,4,1,9,10,87,1,1,3,1,2),_CvdslChanCrcBlockLength_Type())
cvdslChanCrcBlockLength.setMaxAccess(_E)
if mibBuilder.loadTexts:cvdslChanCrcBlockLength.setStatus(_A)
if mibBuilder.loadTexts:cvdslChanCrcBlockLength.setUnits('byte')
_CvdslLineConfProfileTable_Object=MibTable
cvdslLineConfProfileTable=_CvdslLineConfProfileTable_Object((1,3,6,1,4,1,9,10,87,1,1,8))
if mibBuilder.loadTexts:cvdslLineConfProfileTable.setStatus(_A)
_CvdslLineConfProfileEntry_Object=MibTableRow
cvdslLineConfProfileEntry=_CvdslLineConfProfileEntry_Object((1,3,6,1,4,1,9,10,87,1,1,8,1))
cvdslLineConfProfileEntry.setIndexNames((0,_B,_F),(0,_B,_G))
if mibBuilder.loadTexts:cvdslLineConfProfileEntry.setStatus(_A)
class _CvdslLineConfProfileIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CvdslLineConfProfileIndex_Type.__name__=_D
_CvdslLineConfProfileIndex_Object=MibTableColumn
cvdslLineConfProfileIndex=_CvdslLineConfProfileIndex_Object((1,3,6,1,4,1,9,10,87,1,1,8,1,1),_CvdslLineConfProfileIndex_Type())
cvdslLineConfProfileIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:cvdslLineConfProfileIndex.setStatus(_A)
class _CvdslLineConfProfileName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CvdslLineConfProfileName_Type.__name__=_I
_CvdslLineConfProfileName_Object=MibTableColumn
cvdslLineConfProfileName=_CvdslLineConfProfileName_Object((1,3,6,1,4,1,9,10,87,1,1,8,1,2),_CvdslLineConfProfileName_Type())
cvdslLineConfProfileName.setMaxAccess(_C)
if mibBuilder.loadTexts:cvdslLineConfProfileName.setStatus(_A)
class _CvdslLineConfTargetSnrMgn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,310))
_CvdslLineConfTargetSnrMgn_Type.__name__=_D
_CvdslLineConfTargetSnrMgn_Object=MibTableColumn
cvdslLineConfTargetSnrMgn=_CvdslLineConfTargetSnrMgn_Object((1,3,6,1,4,1,9,10,87,1,1,8,1,3),_CvdslLineConfTargetSnrMgn_Type())
cvdslLineConfTargetSnrMgn.setMaxAccess(_C)
if mibBuilder.loadTexts:cvdslLineConfTargetSnrMgn.setStatus(_A)
if mibBuilder.loadTexts:cvdslLineConfTargetSnrMgn.setUnits(_M)
class _CvdslLineConfTxSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CvdslLineConfTxSpeed_Type.__name__=_D
_CvdslLineConfTxSpeed_Object=MibTableColumn
cvdslLineConfTxSpeed=_CvdslLineConfTxSpeed_Object((1,3,6,1,4,1,9,10,87,1,1,8,1,4),_CvdslLineConfTxSpeed_Type())
cvdslLineConfTxSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:cvdslLineConfTxSpeed.setStatus(_A)
if mibBuilder.loadTexts:cvdslLineConfTxSpeed.setUnits(_R)
class _CvdslLineConfRxSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CvdslLineConfRxSpeed_Type.__name__=_D
_CvdslLineConfRxSpeed_Object=MibTableColumn
cvdslLineConfRxSpeed=_CvdslLineConfRxSpeed_Object((1,3,6,1,4,1,9,10,87,1,1,8,1,5),_CvdslLineConfRxSpeed_Type())
cvdslLineConfRxSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:cvdslLineConfRxSpeed.setStatus(_A)
if mibBuilder.loadTexts:cvdslLineConfRxSpeed.setUnits(_R)
_CvdslLineConfProfileRowStatus_Type=RowStatus
_CvdslLineConfProfileRowStatus_Object=MibTableColumn
cvdslLineConfProfileRowStatus=_CvdslLineConfProfileRowStatus_Object((1,3,6,1,4,1,9,10,87,1,1,8,1,6),_CvdslLineConfProfileRowStatus_Type())
cvdslLineConfProfileRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cvdslLineConfProfileRowStatus.setStatus(_A)
_CvdslLineMCMConfProfileTable_Object=MibTable
cvdslLineMCMConfProfileTable=_CvdslLineMCMConfProfileTable_Object((1,3,6,1,4,1,9,10,87,1,1,9))
if mibBuilder.loadTexts:cvdslLineMCMConfProfileTable.setStatus(_A)
_CvdslLineMCMConfProfileEntry_Object=MibTableRow
cvdslLineMCMConfProfileEntry=_CvdslLineMCMConfProfileEntry_Object((1,3,6,1,4,1,9,10,87,1,1,9,1))
cvdslLineMCMConfProfileEntry.setIndexNames((0,_B,_F),(0,_B,_G))
if mibBuilder.loadTexts:cvdslLineMCMConfProfileEntry.setStatus(_A)
class _CvdslMCMConfProfileTxWindowLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_CvdslMCMConfProfileTxWindowLength_Type.__name__=_D
_CvdslMCMConfProfileTxWindowLength_Object=MibTableColumn
cvdslMCMConfProfileTxWindowLength=_CvdslMCMConfProfileTxWindowLength_Object((1,3,6,1,4,1,9,10,87,1,1,9,1,1),_CvdslMCMConfProfileTxWindowLength_Type())
cvdslMCMConfProfileTxWindowLength.setMaxAccess(_C)
if mibBuilder.loadTexts:cvdslMCMConfProfileTxWindowLength.setStatus(_A)
if mibBuilder.loadTexts:cvdslMCMConfProfileTxWindowLength.setUnits('samples')
_CvdslMCMConfProfileRowStatus_Type=RowStatus
_CvdslMCMConfProfileRowStatus_Object=MibTableColumn
cvdslMCMConfProfileRowStatus=_CvdslMCMConfProfileRowStatus_Object((1,3,6,1,4,1,9,10,87,1,1,9,1,2),_CvdslMCMConfProfileRowStatus_Type())
cvdslMCMConfProfileRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cvdslMCMConfProfileRowStatus.setStatus(_A)
_CvdslLineMCMConfProfileTxBandTable_Object=MibTable
cvdslLineMCMConfProfileTxBandTable=_CvdslLineMCMConfProfileTxBandTable_Object((1,3,6,1,4,1,9,10,87,1,1,10))
if mibBuilder.loadTexts:cvdslLineMCMConfProfileTxBandTable.setStatus(_A)
_CvdslLineMCMConfProfileTxBandEntry_Object=MibTableRow
cvdslLineMCMConfProfileTxBandEntry=_CvdslLineMCMConfProfileTxBandEntry_Object((1,3,6,1,4,1,9,10,87,1,1,10,1))
cvdslLineMCMConfProfileTxBandEntry.setIndexNames((0,_B,_F),(0,_B,_G),(0,_B,_S))
if mibBuilder.loadTexts:cvdslLineMCMConfProfileTxBandEntry.setStatus(_A)
class _CvdslMCMConfProfileTxBandNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CvdslMCMConfProfileTxBandNumber_Type.__name__=_D
_CvdslMCMConfProfileTxBandNumber_Object=MibTableColumn
cvdslMCMConfProfileTxBandNumber=_CvdslMCMConfProfileTxBandNumber_Object((1,3,6,1,4,1,9,10,87,1,1,10,1,1),_CvdslMCMConfProfileTxBandNumber_Type())
cvdslMCMConfProfileTxBandNumber.setMaxAccess(_H)
if mibBuilder.loadTexts:cvdslMCMConfProfileTxBandNumber.setStatus(_A)
class _CvdslMCMConfProfileTxBandStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CvdslMCMConfProfileTxBandStart_Type.__name__=_D
_CvdslMCMConfProfileTxBandStart_Object=MibTableColumn
cvdslMCMConfProfileTxBandStart=_CvdslMCMConfProfileTxBandStart_Object((1,3,6,1,4,1,9,10,87,1,1,10,1,2),_CvdslMCMConfProfileTxBandStart_Type())
cvdslMCMConfProfileTxBandStart.setMaxAccess(_C)
if mibBuilder.loadTexts:cvdslMCMConfProfileTxBandStart.setStatus(_A)
class _CvdslMCMConfProfileTxBandStop_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CvdslMCMConfProfileTxBandStop_Type.__name__=_D
_CvdslMCMConfProfileTxBandStop_Object=MibTableColumn
cvdslMCMConfProfileTxBandStop=_CvdslMCMConfProfileTxBandStop_Object((1,3,6,1,4,1,9,10,87,1,1,10,1,3),_CvdslMCMConfProfileTxBandStop_Type())
cvdslMCMConfProfileTxBandStop.setMaxAccess(_C)
if mibBuilder.loadTexts:cvdslMCMConfProfileTxBandStop.setStatus(_A)
_CvdslMCMConfProfileTxBandRowStatus_Type=RowStatus
_CvdslMCMConfProfileTxBandRowStatus_Object=MibTableColumn
cvdslMCMConfProfileTxBandRowStatus=_CvdslMCMConfProfileTxBandRowStatus_Object((1,3,6,1,4,1,9,10,87,1,1,10,1,4),_CvdslMCMConfProfileTxBandRowStatus_Type())
cvdslMCMConfProfileTxBandRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cvdslMCMConfProfileTxBandRowStatus.setStatus(_A)
_CvdslLineMCMConfProfileRxBandTable_Object=MibTable
cvdslLineMCMConfProfileRxBandTable=_CvdslLineMCMConfProfileRxBandTable_Object((1,3,6,1,4,1,9,10,87,1,1,11))
if mibBuilder.loadTexts:cvdslLineMCMConfProfileRxBandTable.setStatus(_A)
_CvdslLineMCMConfProfileRxBandEntry_Object=MibTableRow
cvdslLineMCMConfProfileRxBandEntry=_CvdslLineMCMConfProfileRxBandEntry_Object((1,3,6,1,4,1,9,10,87,1,1,11,1))
cvdslLineMCMConfProfileRxBandEntry.setIndexNames((0,_B,_F),(0,_B,_G),(0,_B,_T))
if mibBuilder.loadTexts:cvdslLineMCMConfProfileRxBandEntry.setStatus(_A)
class _CvdslMCMConfProfileRxBandNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CvdslMCMConfProfileRxBandNumber_Type.__name__=_D
_CvdslMCMConfProfileRxBandNumber_Object=MibTableColumn
cvdslMCMConfProfileRxBandNumber=_CvdslMCMConfProfileRxBandNumber_Object((1,3,6,1,4,1,9,10,87,1,1,11,1,1),_CvdslMCMConfProfileRxBandNumber_Type())
cvdslMCMConfProfileRxBandNumber.setMaxAccess(_H)
if mibBuilder.loadTexts:cvdslMCMConfProfileRxBandNumber.setStatus(_A)
class _CvdslMCMConfProfileRxBandStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CvdslMCMConfProfileRxBandStart_Type.__name__=_D
_CvdslMCMConfProfileRxBandStart_Object=MibTableColumn
cvdslMCMConfProfileRxBandStart=_CvdslMCMConfProfileRxBandStart_Object((1,3,6,1,4,1,9,10,87,1,1,11,1,2),_CvdslMCMConfProfileRxBandStart_Type())
cvdslMCMConfProfileRxBandStart.setMaxAccess(_C)
if mibBuilder.loadTexts:cvdslMCMConfProfileRxBandStart.setStatus(_A)
class _CvdslMCMConfProfileRxBandStop_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CvdslMCMConfProfileRxBandStop_Type.__name__=_D
_CvdslMCMConfProfileRxBandStop_Object=MibTableColumn
cvdslMCMConfProfileRxBandStop=_CvdslMCMConfProfileRxBandStop_Object((1,3,6,1,4,1,9,10,87,1,1,11,1,3),_CvdslMCMConfProfileRxBandStop_Type())
cvdslMCMConfProfileRxBandStop.setMaxAccess(_C)
if mibBuilder.loadTexts:cvdslMCMConfProfileRxBandStop.setStatus(_A)
_CvdslMCMConfProfileRxBandRowStatus_Type=RowStatus
_CvdslMCMConfProfileRxBandRowStatus_Object=MibTableColumn
cvdslMCMConfProfileRxBandRowStatus=_CvdslMCMConfProfileRxBandRowStatus_Object((1,3,6,1,4,1,9,10,87,1,1,11,1,4),_CvdslMCMConfProfileRxBandRowStatus_Type())
cvdslMCMConfProfileRxBandRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cvdslMCMConfProfileRxBandRowStatus.setStatus(_A)
_CvdslLineMCMConfProfileTxPSDTable_Object=MibTable
cvdslLineMCMConfProfileTxPSDTable=_CvdslLineMCMConfProfileTxPSDTable_Object((1,3,6,1,4,1,9,10,87,1,1,12))
if mibBuilder.loadTexts:cvdslLineMCMConfProfileTxPSDTable.setStatus(_A)
_CvdslLineMCMConfProfileTxPSDEntry_Object=MibTableRow
cvdslLineMCMConfProfileTxPSDEntry=_CvdslLineMCMConfProfileTxPSDEntry_Object((1,3,6,1,4,1,9,10,87,1,1,12,1))
cvdslLineMCMConfProfileTxPSDEntry.setIndexNames((0,_B,_F),(0,_B,_G),(0,_B,_U))
if mibBuilder.loadTexts:cvdslLineMCMConfProfileTxPSDEntry.setStatus(_A)
class _CvdslMCMConfProfileTxPSDNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CvdslMCMConfProfileTxPSDNumber_Type.__name__=_D
_CvdslMCMConfProfileTxPSDNumber_Object=MibTableColumn
cvdslMCMConfProfileTxPSDNumber=_CvdslMCMConfProfileTxPSDNumber_Object((1,3,6,1,4,1,9,10,87,1,1,12,1,1),_CvdslMCMConfProfileTxPSDNumber_Type())
cvdslMCMConfProfileTxPSDNumber.setMaxAccess(_H)
if mibBuilder.loadTexts:cvdslMCMConfProfileTxPSDNumber.setStatus(_A)
class _CvdslMCMConfProfileTxPSDTone_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CvdslMCMConfProfileTxPSDTone_Type.__name__=_D
_CvdslMCMConfProfileTxPSDTone_Object=MibTableColumn
cvdslMCMConfProfileTxPSDTone=_CvdslMCMConfProfileTxPSDTone_Object((1,3,6,1,4,1,9,10,87,1,1,12,1,2),_CvdslMCMConfProfileTxPSDTone_Type())
cvdslMCMConfProfileTxPSDTone.setMaxAccess(_C)
if mibBuilder.loadTexts:cvdslMCMConfProfileTxPSDTone.setStatus(_A)
class _CvdslMCMConfProfileTxPSDPSD_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CvdslMCMConfProfileTxPSDPSD_Type.__name__=_D
_CvdslMCMConfProfileTxPSDPSD_Object=MibTableColumn
cvdslMCMConfProfileTxPSDPSD=_CvdslMCMConfProfileTxPSDPSD_Object((1,3,6,1,4,1,9,10,87,1,1,12,1,3),_CvdslMCMConfProfileTxPSDPSD_Type())
cvdslMCMConfProfileTxPSDPSD.setMaxAccess(_C)
if mibBuilder.loadTexts:cvdslMCMConfProfileTxPSDPSD.setStatus(_A)
if mibBuilder.loadTexts:cvdslMCMConfProfileTxPSDPSD.setUnits(_N)
_CvdslMCMConfProfileTxPSDRowStatus_Type=RowStatus
_CvdslMCMConfProfileTxPSDRowStatus_Object=MibTableColumn
cvdslMCMConfProfileTxPSDRowStatus=_CvdslMCMConfProfileTxPSDRowStatus_Object((1,3,6,1,4,1,9,10,87,1,1,12,1,4),_CvdslMCMConfProfileTxPSDRowStatus_Type())
cvdslMCMConfProfileTxPSDRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cvdslMCMConfProfileTxPSDRowStatus.setStatus(_A)
_CvdslLineMCMConfProfileMaxTxPSDTable_Object=MibTable
cvdslLineMCMConfProfileMaxTxPSDTable=_CvdslLineMCMConfProfileMaxTxPSDTable_Object((1,3,6,1,4,1,9,10,87,1,1,13))
if mibBuilder.loadTexts:cvdslLineMCMConfProfileMaxTxPSDTable.setStatus(_A)
_CvdslLineMCMConfProfileMaxTxPSDEntry_Object=MibTableRow
cvdslLineMCMConfProfileMaxTxPSDEntry=_CvdslLineMCMConfProfileMaxTxPSDEntry_Object((1,3,6,1,4,1,9,10,87,1,1,13,1))
cvdslLineMCMConfProfileMaxTxPSDEntry.setIndexNames((0,_B,_F),(0,_B,_G),(0,_B,_V))
if mibBuilder.loadTexts:cvdslLineMCMConfProfileMaxTxPSDEntry.setStatus(_A)
class _CvdslMCMConfProfileMaxTxPSDNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CvdslMCMConfProfileMaxTxPSDNumber_Type.__name__=_D
_CvdslMCMConfProfileMaxTxPSDNumber_Object=MibTableColumn
cvdslMCMConfProfileMaxTxPSDNumber=_CvdslMCMConfProfileMaxTxPSDNumber_Object((1,3,6,1,4,1,9,10,87,1,1,13,1,1),_CvdslMCMConfProfileMaxTxPSDNumber_Type())
cvdslMCMConfProfileMaxTxPSDNumber.setMaxAccess(_H)
if mibBuilder.loadTexts:cvdslMCMConfProfileMaxTxPSDNumber.setStatus(_A)
class _CvdslMCMConfProfileMaxTxPSDTone_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CvdslMCMConfProfileMaxTxPSDTone_Type.__name__=_D
_CvdslMCMConfProfileMaxTxPSDTone_Object=MibTableColumn
cvdslMCMConfProfileMaxTxPSDTone=_CvdslMCMConfProfileMaxTxPSDTone_Object((1,3,6,1,4,1,9,10,87,1,1,13,1,2),_CvdslMCMConfProfileMaxTxPSDTone_Type())
cvdslMCMConfProfileMaxTxPSDTone.setMaxAccess(_C)
if mibBuilder.loadTexts:cvdslMCMConfProfileMaxTxPSDTone.setStatus(_A)
class _CvdslMCMConfProfileMaxTxPSDPSD_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CvdslMCMConfProfileMaxTxPSDPSD_Type.__name__=_D
_CvdslMCMConfProfileMaxTxPSDPSD_Object=MibTableColumn
cvdslMCMConfProfileMaxTxPSDPSD=_CvdslMCMConfProfileMaxTxPSDPSD_Object((1,3,6,1,4,1,9,10,87,1,1,13,1,3),_CvdslMCMConfProfileMaxTxPSDPSD_Type())
cvdslMCMConfProfileMaxTxPSDPSD.setMaxAccess(_C)
if mibBuilder.loadTexts:cvdslMCMConfProfileMaxTxPSDPSD.setStatus(_A)
if mibBuilder.loadTexts:cvdslMCMConfProfileMaxTxPSDPSD.setUnits(_N)
_CvdslMCMConfProfileMaxTxPSDRowStatus_Type=RowStatus
_CvdslMCMConfProfileMaxTxPSDRowStatus_Object=MibTableColumn
cvdslMCMConfProfileMaxTxPSDRowStatus=_CvdslMCMConfProfileMaxTxPSDRowStatus_Object((1,3,6,1,4,1,9,10,87,1,1,13,1,4),_CvdslMCMConfProfileMaxTxPSDRowStatus_Type())
cvdslMCMConfProfileMaxTxPSDRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cvdslMCMConfProfileMaxTxPSDRowStatus.setStatus(_A)
_CvdslLineMCMConfProfileMaxRxPSDTable_Object=MibTable
cvdslLineMCMConfProfileMaxRxPSDTable=_CvdslLineMCMConfProfileMaxRxPSDTable_Object((1,3,6,1,4,1,9,10,87,1,1,14))
if mibBuilder.loadTexts:cvdslLineMCMConfProfileMaxRxPSDTable.setStatus(_A)
_CvdslLineMCMConfProfileMaxRxPSDEntry_Object=MibTableRow
cvdslLineMCMConfProfileMaxRxPSDEntry=_CvdslLineMCMConfProfileMaxRxPSDEntry_Object((1,3,6,1,4,1,9,10,87,1,1,14,1))
cvdslLineMCMConfProfileMaxRxPSDEntry.setIndexNames((0,_B,_F),(0,_B,_G),(0,_B,_W))
if mibBuilder.loadTexts:cvdslLineMCMConfProfileMaxRxPSDEntry.setStatus(_A)
class _CvdslMCMConfProfileMaxRxPSDNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CvdslMCMConfProfileMaxRxPSDNumber_Type.__name__=_D
_CvdslMCMConfProfileMaxRxPSDNumber_Object=MibTableColumn
cvdslMCMConfProfileMaxRxPSDNumber=_CvdslMCMConfProfileMaxRxPSDNumber_Object((1,3,6,1,4,1,9,10,87,1,1,14,1,1),_CvdslMCMConfProfileMaxRxPSDNumber_Type())
cvdslMCMConfProfileMaxRxPSDNumber.setMaxAccess(_H)
if mibBuilder.loadTexts:cvdslMCMConfProfileMaxRxPSDNumber.setStatus(_A)
class _CvdslMCMConfProfileMaxRxPSDTone_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CvdslMCMConfProfileMaxRxPSDTone_Type.__name__=_D
_CvdslMCMConfProfileMaxRxPSDTone_Object=MibTableColumn
cvdslMCMConfProfileMaxRxPSDTone=_CvdslMCMConfProfileMaxRxPSDTone_Object((1,3,6,1,4,1,9,10,87,1,1,14,1,2),_CvdslMCMConfProfileMaxRxPSDTone_Type())
cvdslMCMConfProfileMaxRxPSDTone.setMaxAccess(_C)
if mibBuilder.loadTexts:cvdslMCMConfProfileMaxRxPSDTone.setStatus(_A)
class _CvdslMCMConfProfileMaxRxPSDPSD_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CvdslMCMConfProfileMaxRxPSDPSD_Type.__name__=_D
_CvdslMCMConfProfileMaxRxPSDPSD_Object=MibTableColumn
cvdslMCMConfProfileMaxRxPSDPSD=_CvdslMCMConfProfileMaxRxPSDPSD_Object((1,3,6,1,4,1,9,10,87,1,1,14,1,3),_CvdslMCMConfProfileMaxRxPSDPSD_Type())
cvdslMCMConfProfileMaxRxPSDPSD.setMaxAccess(_C)
if mibBuilder.loadTexts:cvdslMCMConfProfileMaxRxPSDPSD.setStatus(_A)
if mibBuilder.loadTexts:cvdslMCMConfProfileMaxRxPSDPSD.setUnits(_N)
_CvdslMCMConfProfileMaxRxPSDRowStatus_Type=RowStatus
_CvdslMCMConfProfileMaxRxPSDRowStatus_Object=MibTableColumn
cvdslMCMConfProfileMaxRxPSDRowStatus=_CvdslMCMConfProfileMaxRxPSDRowStatus_Object((1,3,6,1,4,1,9,10,87,1,1,14,1,4),_CvdslMCMConfProfileMaxRxPSDRowStatus_Type())
cvdslMCMConfProfileMaxRxPSDRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cvdslMCMConfProfileMaxRxPSDRowStatus.setStatus(_A)
_CvdslLineSCMConfProfileTable_Object=MibTable
cvdslLineSCMConfProfileTable=_CvdslLineSCMConfProfileTable_Object((1,3,6,1,4,1,9,10,87,1,1,15))
if mibBuilder.loadTexts:cvdslLineSCMConfProfileTable.setStatus(_A)
_CvdslLineSCMConfProfileEntry_Object=MibTableRow
cvdslLineSCMConfProfileEntry=_CvdslLineSCMConfProfileEntry_Object((1,3,6,1,4,1,9,10,87,1,1,15,1))
cvdslLineSCMConfProfileEntry.setIndexNames((0,_B,_F),(0,_B,_G))
if mibBuilder.loadTexts:cvdslLineSCMConfProfileEntry.setStatus(_A)
class _CvdslSCMConfProfileInterleaveDepth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CvdslSCMConfProfileInterleaveDepth_Type.__name__=_D
_CvdslSCMConfProfileInterleaveDepth_Object=MibTableColumn
cvdslSCMConfProfileInterleaveDepth=_CvdslSCMConfProfileInterleaveDepth_Object((1,3,6,1,4,1,9,10,87,1,1,15,1,1),_CvdslSCMConfProfileInterleaveDepth_Type())
cvdslSCMConfProfileInterleaveDepth.setMaxAccess(_C)
if mibBuilder.loadTexts:cvdslSCMConfProfileInterleaveDepth.setStatus(_A)
if mibBuilder.loadTexts:cvdslSCMConfProfileInterleaveDepth.setUnits(_X)
class _CvdslSCMConfProfileFastCodewordSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,180))
_CvdslSCMConfProfileFastCodewordSize_Type.__name__=_D
_CvdslSCMConfProfileFastCodewordSize_Object=MibTableColumn
cvdslSCMConfProfileFastCodewordSize=_CvdslSCMConfProfileFastCodewordSize_Object((1,3,6,1,4,1,9,10,87,1,1,15,1,2),_CvdslSCMConfProfileFastCodewordSize_Type())
cvdslSCMConfProfileFastCodewordSize.setMaxAccess(_C)
if mibBuilder.loadTexts:cvdslSCMConfProfileFastCodewordSize.setStatus(_A)
if mibBuilder.loadTexts:cvdslSCMConfProfileFastCodewordSize.setUnits(_X)
class _CvdslSCMConfProfileTransmitPSDMask_Type(Bits):namedValues=NamedValues(*(('vendorNotch1',0),('vendorNotch2',1),('amateurBand30m',2),('amateurBand40m',3),('amateurBand80m',4),('amateurBand160m',5)))
_CvdslSCMConfProfileTransmitPSDMask_Type.__name__=_L
_CvdslSCMConfProfileTransmitPSDMask_Object=MibTableColumn
cvdslSCMConfProfileTransmitPSDMask=_CvdslSCMConfProfileTransmitPSDMask_Object((1,3,6,1,4,1,9,10,87,1,1,15,1,3),_CvdslSCMConfProfileTransmitPSDMask_Type())
cvdslSCMConfProfileTransmitPSDMask.setMaxAccess(_C)
if mibBuilder.loadTexts:cvdslSCMConfProfileTransmitPSDMask.setStatus(_A)
class _CvdslSCMConfProfileTransmitPSDLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CvdslSCMConfProfileTransmitPSDLevel_Type.__name__=_D
_CvdslSCMConfProfileTransmitPSDLevel_Object=MibTableColumn
cvdslSCMConfProfileTransmitPSDLevel=_CvdslSCMConfProfileTransmitPSDLevel_Object((1,3,6,1,4,1,9,10,87,1,1,15,1,4),_CvdslSCMConfProfileTransmitPSDLevel_Type())
cvdslSCMConfProfileTransmitPSDLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:cvdslSCMConfProfileTransmitPSDLevel.setStatus(_A)
if mibBuilder.loadTexts:cvdslSCMConfProfileTransmitPSDLevel.setUnits('dBm/Hz')
class _CvdslSCMConfProfileSymbolRateProfile_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CvdslSCMConfProfileSymbolRateProfile_Type.__name__=_D
_CvdslSCMConfProfileSymbolRateProfile_Object=MibTableColumn
cvdslSCMConfProfileSymbolRateProfile=_CvdslSCMConfProfileSymbolRateProfile_Object((1,3,6,1,4,1,9,10,87,1,1,15,1,5),_CvdslSCMConfProfileSymbolRateProfile_Type())
cvdslSCMConfProfileSymbolRateProfile.setMaxAccess(_C)
if mibBuilder.loadTexts:cvdslSCMConfProfileSymbolRateProfile.setStatus(_A)
if mibBuilder.loadTexts:cvdslSCMConfProfileSymbolRateProfile.setUnits('kbaud')
class _CvdslSCMConfProfileConstellationSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_CvdslSCMConfProfileConstellationSize_Type.__name__=_D
_CvdslSCMConfProfileConstellationSize_Object=MibTableColumn
cvdslSCMConfProfileConstellationSize=_CvdslSCMConfProfileConstellationSize_Object((1,3,6,1,4,1,9,10,87,1,1,15,1,6),_CvdslSCMConfProfileConstellationSize_Type())
cvdslSCMConfProfileConstellationSize.setMaxAccess(_C)
if mibBuilder.loadTexts:cvdslSCMConfProfileConstellationSize.setStatus(_A)
if mibBuilder.loadTexts:cvdslSCMConfProfileConstellationSize.setUnits('log2')
class _CvdslSCMConfProfileCenterFrequency_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,511))
_CvdslSCMConfProfileCenterFrequency_Type.__name__=_D
_CvdslSCMConfProfileCenterFrequency_Object=MibTableColumn
cvdslSCMConfProfileCenterFrequency=_CvdslSCMConfProfileCenterFrequency_Object((1,3,6,1,4,1,9,10,87,1,1,15,1,7),_CvdslSCMConfProfileCenterFrequency_Type())
cvdslSCMConfProfileCenterFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:cvdslSCMConfProfileCenterFrequency.setStatus(_A)
if mibBuilder.loadTexts:cvdslSCMConfProfileCenterFrequency.setUnits('kHz')
_CvdslSCMConfProfileRowStatus_Type=RowStatus
_CvdslSCMConfProfileRowStatus_Object=MibTableColumn
cvdslSCMConfProfileRowStatus=_CvdslSCMConfProfileRowStatus_Object((1,3,6,1,4,1,9,10,87,1,1,15,1,8),_CvdslSCMConfProfileRowStatus_Type())
cvdslSCMConfProfileRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cvdslSCMConfProfileRowStatus.setStatus(_A)
_CvdslLineAlarmConfProfileTable_Object=MibTable
cvdslLineAlarmConfProfileTable=_CvdslLineAlarmConfProfileTable_Object((1,3,6,1,4,1,9,10,87,1,1,16))
if mibBuilder.loadTexts:cvdslLineAlarmConfProfileTable.setStatus(_A)
_CvdslLineAlarmConfProfileEntry_Object=MibTableRow
cvdslLineAlarmConfProfileEntry=_CvdslLineAlarmConfProfileEntry_Object((1,3,6,1,4,1,9,10,87,1,1,16,1))
cvdslLineAlarmConfProfileEntry.setIndexNames((0,_B,_F),(0,_B,_Y))
if mibBuilder.loadTexts:cvdslLineAlarmConfProfileEntry.setStatus(_A)
class _CvdslLineAlarmConfProfileIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CvdslLineAlarmConfProfileIndex_Type.__name__=_D
_CvdslLineAlarmConfProfileIndex_Object=MibTableColumn
cvdslLineAlarmConfProfileIndex=_CvdslLineAlarmConfProfileIndex_Object((1,3,6,1,4,1,9,10,87,1,1,16,1,1),_CvdslLineAlarmConfProfileIndex_Type())
cvdslLineAlarmConfProfileIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:cvdslLineAlarmConfProfileIndex.setStatus(_A)
class _CvdslLineAlarmConfProfileName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CvdslLineAlarmConfProfileName_Type.__name__=_I
_CvdslLineAlarmConfProfileName_Object=MibTableColumn
cvdslLineAlarmConfProfileName=_CvdslLineAlarmConfProfileName_Object((1,3,6,1,4,1,9,10,87,1,1,16,1,2),_CvdslLineAlarmConfProfileName_Type())
cvdslLineAlarmConfProfileName.setMaxAccess(_C)
if mibBuilder.loadTexts:cvdslLineAlarmConfProfileName.setStatus(_A)
_CvdslInitFailureNotificationEnable_Type=TruthValue
_CvdslInitFailureNotificationEnable_Object=MibTableColumn
cvdslInitFailureNotificationEnable=_CvdslInitFailureNotificationEnable_Object((1,3,6,1,4,1,9,10,87,1,1,16,1,3),_CvdslInitFailureNotificationEnable_Type())
cvdslInitFailureNotificationEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:cvdslInitFailureNotificationEnable.setStatus(_A)
_CvdslLineAlarmConfProfileRowStatus_Type=RowStatus
_CvdslLineAlarmConfProfileRowStatus_Object=MibTableColumn
cvdslLineAlarmConfProfileRowStatus=_CvdslLineAlarmConfProfileRowStatus_Object((1,3,6,1,4,1,9,10,87,1,1,16,1,4),_CvdslLineAlarmConfProfileRowStatus_Type())
cvdslLineAlarmConfProfileRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cvdslLineAlarmConfProfileRowStatus.setStatus(_A)
_CvdslConformance_ObjectIdentity=ObjectIdentity
cvdslConformance=_CvdslConformance_ObjectIdentity((1,3,6,1,4,1,9,10,87,1,3))
_CvdslGroups_ObjectIdentity=ObjectIdentity
cvdslGroups=_CvdslGroups_ObjectIdentity((1,3,6,1,4,1,9,10,87,1,3,1))
_CvdslCompliances_ObjectIdentity=ObjectIdentity
cvdslCompliances=_CvdslCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,87,1,3,2))
cvdslGroup=ObjectGroup((1,3,6,1,4,1,9,10,87,1,3,1,1))
cvdslGroup.setObjects(*((_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_O),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t)))
if mibBuilder.loadTexts:cvdslGroup.setStatus(_A)
cvdslMCMGroup=ObjectGroup((1,3,6,1,4,1,9,10,87,1,3,1,2))
cvdslMCMGroup.setObjects(*((_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA)))
if mibBuilder.loadTexts:cvdslMCMGroup.setStatus(_A)
cvdslSCMGroup=ObjectGroup((1,3,6,1,4,1,9,10,87,1,3,1,3))
cvdslSCMGroup.setObjects(*((_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI)))
if mibBuilder.loadTexts:cvdslSCMGroup.setStatus(_A)
cvdslInitFailureNotification=NotificationType((1,3,6,1,4,1,9,10,87,1,0,1))
cvdslInitFailureNotification.setObjects((_B,_O))
if mibBuilder.loadTexts:cvdslInitFailureNotification.setStatus(_A)
cvdslNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,10,87,1,3,1,4))
cvdslNotificationGroup.setObjects((_B,_AJ))
if mibBuilder.loadTexts:cvdslNotificationGroup.setStatus(_A)
cvdslLineMibCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,87,1,3,2,1))
cvdslLineMibCompliance.setObjects(*((_B,_AK),(_B,_AL),(_B,_AM)))
if mibBuilder.loadTexts:cvdslLineMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CVdslLineCodingType':CVdslLineCodingType,'CVdslLineEntity':CVdslLineEntity,'ciscoIetfVdslMIB':ciscoIetfVdslMIB,'cvdslLineMib':cvdslLineMib,'cvdslNotifications':cvdslNotifications,_AJ:cvdslInitFailureNotification,'cvdslMibObjects':cvdslMibObjects,'cvdslLineTable':cvdslLineTable,'cvdslLineEntry':cvdslLineEntry,_Z:cvdslLineCoding,_a:cvdslLineType,_b:cvdslLineConfProfile,_c:cvdslLineAlarmConfProfile,'cvdslPhysTable':cvdslPhysTable,'cvdslPhysEntry':cvdslPhysEntry,_F:cvdslPhysSide,_d:cvdslInvSerialNumber,_e:cvdslInvVendorID,_f:cvdslInvVersionNumber,_g:cvdslCurrSnrMgn,_h:cvdslCurrAtn,_O:cvdslCurrStatus,_i:cvdslCurrOutputPwr,_j:cvdslCurrAttainableRate,'cvdslChanTable':cvdslChanTable,'cvdslChanEntry':cvdslChanEntry,_k:cvdslChanInterleaveDelay,_l:cvdslChanCrcBlockLength,'cvdslLineConfProfileTable':cvdslLineConfProfileTable,'cvdslLineConfProfileEntry':cvdslLineConfProfileEntry,_G:cvdslLineConfProfileIndex,_m:cvdslLineConfProfileName,_n:cvdslLineConfTargetSnrMgn,_o:cvdslLineConfTxSpeed,_p:cvdslLineConfRxSpeed,_q:cvdslLineConfProfileRowStatus,'cvdslLineMCMConfProfileTable':cvdslLineMCMConfProfileTable,'cvdslLineMCMConfProfileEntry':cvdslLineMCMConfProfileEntry,_u:cvdslMCMConfProfileTxWindowLength,_v:cvdslMCMConfProfileRowStatus,'cvdslLineMCMConfProfileTxBandTable':cvdslLineMCMConfProfileTxBandTable,'cvdslLineMCMConfProfileTxBandEntry':cvdslLineMCMConfProfileTxBandEntry,_S:cvdslMCMConfProfileTxBandNumber,_w:cvdslMCMConfProfileTxBandStart,_x:cvdslMCMConfProfileTxBandStop,_y:cvdslMCMConfProfileTxBandRowStatus,'cvdslLineMCMConfProfileRxBandTable':cvdslLineMCMConfProfileRxBandTable,'cvdslLineMCMConfProfileRxBandEntry':cvdslLineMCMConfProfileRxBandEntry,_T:cvdslMCMConfProfileRxBandNumber,_z:cvdslMCMConfProfileRxBandStart,_A0:cvdslMCMConfProfileRxBandStop,_A1:cvdslMCMConfProfileRxBandRowStatus,'cvdslLineMCMConfProfileTxPSDTable':cvdslLineMCMConfProfileTxPSDTable,'cvdslLineMCMConfProfileTxPSDEntry':cvdslLineMCMConfProfileTxPSDEntry,_U:cvdslMCMConfProfileTxPSDNumber,_A2:cvdslMCMConfProfileTxPSDTone,_A3:cvdslMCMConfProfileTxPSDPSD,_A4:cvdslMCMConfProfileTxPSDRowStatus,'cvdslLineMCMConfProfileMaxTxPSDTable':cvdslLineMCMConfProfileMaxTxPSDTable,'cvdslLineMCMConfProfileMaxTxPSDEntry':cvdslLineMCMConfProfileMaxTxPSDEntry,_V:cvdslMCMConfProfileMaxTxPSDNumber,_A5:cvdslMCMConfProfileMaxTxPSDTone,_A6:cvdslMCMConfProfileMaxTxPSDPSD,_A7:cvdslMCMConfProfileMaxTxPSDRowStatus,'cvdslLineMCMConfProfileMaxRxPSDTable':cvdslLineMCMConfProfileMaxRxPSDTable,'cvdslLineMCMConfProfileMaxRxPSDEntry':cvdslLineMCMConfProfileMaxRxPSDEntry,_W:cvdslMCMConfProfileMaxRxPSDNumber,_A8:cvdslMCMConfProfileMaxRxPSDTone,_A9:cvdslMCMConfProfileMaxRxPSDPSD,_AA:cvdslMCMConfProfileMaxRxPSDRowStatus,'cvdslLineSCMConfProfileTable':cvdslLineSCMConfProfileTable,'cvdslLineSCMConfProfileEntry':cvdslLineSCMConfProfileEntry,_AB:cvdslSCMConfProfileInterleaveDepth,_AC:cvdslSCMConfProfileFastCodewordSize,_AD:cvdslSCMConfProfileTransmitPSDMask,_AE:cvdslSCMConfProfileTransmitPSDLevel,_AF:cvdslSCMConfProfileSymbolRateProfile,_AG:cvdslSCMConfProfileConstellationSize,_AH:cvdslSCMConfProfileCenterFrequency,_AI:cvdslSCMConfProfileRowStatus,'cvdslLineAlarmConfProfileTable':cvdslLineAlarmConfProfileTable,'cvdslLineAlarmConfProfileEntry':cvdslLineAlarmConfProfileEntry,_Y:cvdslLineAlarmConfProfileIndex,_r:cvdslLineAlarmConfProfileName,_s:cvdslInitFailureNotificationEnable,_t:cvdslLineAlarmConfProfileRowStatus,'cvdslConformance':cvdslConformance,'cvdslGroups':cvdslGroups,_AK:cvdslGroup,_AL:cvdslMCMGroup,_AM:cvdslSCMGroup,'cvdslNotificationGroup':cvdslNotificationGroup,'cvdslCompliances':cvdslCompliances,'cvdslLineMibCompliance':cvdslLineMibCompliance})