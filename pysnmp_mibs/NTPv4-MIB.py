_AB='ntpEntNotifGroup'
_AA='ntpEntObjectsGroup2'
_A9='ntpEntNotifHeartbeat'
_A8='ntpEntNotifLeapSecondAnnounced'
_A7='ntpEntNotifConfigChanged'
_A6='ntpEntNotifRemoveAssociation'
_A5='ntpEntNotifAddAssociation'
_A4='ntpEntNotifSyspeerChanged'
_A3='ntpEntNotifStratumChange'
_A2='ntpEntNotifModeChange'
_A1='ntpEntNotifBits'
_A0='ntpAssocStatProtocolError'
_z='ntpAssocStatOutPkts'
_y='ntpAssocStatInPkts'
_x='ntpAssocStatusDispersion'
_w='ntpAssocStatusDelay'
_v='ntpAssocStatusJitter'
_u='ntpAssocStratum'
_t='ntpAssocOffset'
_s='ntpEntStatPktReceived'
_r='ntpEntStatPktSent'
_q='ntpEntStatusNotifications'
_p='ntpEntStatusProtocolError'
_o='ntpEntStatusBadVersion'
_n='ntpEntStatusOutPkts'
_m='ntpEntStatusInPkts'
_l='ntpEntStatusLeapSecDirection'
_k='ntpEntStatusLeapSecond'
_j='ntpEntStatusDispersion'
_i='ntpEntStatusNumberOfRefSources'
_h='ntpEntStatusActiveOffset'
_g='ntpEntStatusActiveRefSourceName'
_f='ntpEntTimeDistance'
_e='ntpEntTimePrecision'
_d='ntpEntTimeResolution'
_c='ntpAssocAddress'
_b='ntpAssocAddressType'
_a='ntpAssocRefId'
_Z='ntpEntStatusEntityUptime'
_Y='ntpEntSystemType'
_X='ntpEntSoftwareVendor'
_W='ntpEntSoftwareVersion'
_V='ntpEntSoftwareName'
_U='read-write'
_T='not-accessible'
_S='ntpEntStatPktMode'
_R='Utf8String'
_Q='InetAddressType'
_P='InetAddress'
_O='ntpEntObjectsGroup1'
_N='ntpEntHeartbeatInterval'
_M='ntpEntStatusActiveRefSourceId'
_L='ntpEntStatusStratum'
_K='ntpAssocId'
_J='ntpEntStatusCurrentMode'
_I='ntpAssocName'
_H='Integer32'
_G='Unsigned32'
_F='ntpEntNotifMessage'
_E='ntpEntStatusDateTime'
_D='packets'
_C='read-only'
_B='current'
_A='NTPv4-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_P,_Q)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso','mib-2')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
Utf8String,=mibBuilder.importSymbols('SYSAPPL-MIB',_R)
ntpSnmpMIB=ModuleIdentity((1,3,6,1,2,1,197))
if mibBuilder.loadTexts:ntpSnmpMIB.setRevisions(('2010-05-17 00:00',))
class NtpStratum(TextualConvention,Unsigned32):status=_B;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
class NtpDateTime(TextualConvention,OctetString):status=_B;displayHint='4d:4d:4d.4d';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(16,16))
_NtpEntNotifications_ObjectIdentity=ObjectIdentity
ntpEntNotifications=_NtpEntNotifications_ObjectIdentity((1,3,6,1,2,1,197,0))
_NtpSnmpMIBObjects_ObjectIdentity=ObjectIdentity
ntpSnmpMIBObjects=_NtpSnmpMIBObjects_ObjectIdentity((1,3,6,1,2,1,197,1))
_NtpEntInfo_ObjectIdentity=ObjectIdentity
ntpEntInfo=_NtpEntInfo_ObjectIdentity((1,3,6,1,2,1,197,1,1))
_NtpEntSoftwareName_Type=Utf8String
_NtpEntSoftwareName_Object=MibScalar
ntpEntSoftwareName=_NtpEntSoftwareName_Object((1,3,6,1,2,1,197,1,1,1),_NtpEntSoftwareName_Type())
ntpEntSoftwareName.setMaxAccess(_C)
if mibBuilder.loadTexts:ntpEntSoftwareName.setStatus(_B)
_NtpEntSoftwareVersion_Type=Utf8String
_NtpEntSoftwareVersion_Object=MibScalar
ntpEntSoftwareVersion=_NtpEntSoftwareVersion_Object((1,3,6,1,2,1,197,1,1,2),_NtpEntSoftwareVersion_Type())
ntpEntSoftwareVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:ntpEntSoftwareVersion.setStatus(_B)
_NtpEntSoftwareVendor_Type=Utf8String
_NtpEntSoftwareVendor_Object=MibScalar
ntpEntSoftwareVendor=_NtpEntSoftwareVendor_Object((1,3,6,1,2,1,197,1,1,3),_NtpEntSoftwareVendor_Type())
ntpEntSoftwareVendor.setMaxAccess(_C)
if mibBuilder.loadTexts:ntpEntSoftwareVendor.setStatus(_B)
_NtpEntSystemType_Type=Utf8String
_NtpEntSystemType_Object=MibScalar
ntpEntSystemType=_NtpEntSystemType_Object((1,3,6,1,2,1,197,1,1,4),_NtpEntSystemType_Type())
ntpEntSystemType.setMaxAccess(_C)
if mibBuilder.loadTexts:ntpEntSystemType.setStatus(_B)
_NtpEntTimeResolution_Type=Unsigned32
_NtpEntTimeResolution_Object=MibScalar
ntpEntTimeResolution=_NtpEntTimeResolution_Object((1,3,6,1,2,1,197,1,1,5),_NtpEntTimeResolution_Type())
ntpEntTimeResolution.setMaxAccess(_C)
if mibBuilder.loadTexts:ntpEntTimeResolution.setStatus(_B)
_NtpEntTimePrecision_Type=Integer32
_NtpEntTimePrecision_Object=MibScalar
ntpEntTimePrecision=_NtpEntTimePrecision_Object((1,3,6,1,2,1,197,1,1,6),_NtpEntTimePrecision_Type())
ntpEntTimePrecision.setMaxAccess(_C)
if mibBuilder.loadTexts:ntpEntTimePrecision.setStatus(_B)
_NtpEntTimeDistance_Type=DisplayString
_NtpEntTimeDistance_Object=MibScalar
ntpEntTimeDistance=_NtpEntTimeDistance_Object((1,3,6,1,2,1,197,1,1,7),_NtpEntTimeDistance_Type())
ntpEntTimeDistance.setMaxAccess(_C)
if mibBuilder.loadTexts:ntpEntTimeDistance.setStatus(_B)
_NtpEntStatus_ObjectIdentity=ObjectIdentity
ntpEntStatus=_NtpEntStatus_ObjectIdentity((1,3,6,1,2,1,197,1,2))
class _NtpEntStatusCurrentMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,99)));namedValues=NamedValues(*(('notRunning',1),('notSynchronized',2),('noneConfigured',3),('syncToLocal',4),('syncToRefclock',5),('syncToRemoteServer',6),('unknown',99)))
_NtpEntStatusCurrentMode_Type.__name__=_H
_NtpEntStatusCurrentMode_Object=MibScalar
ntpEntStatusCurrentMode=_NtpEntStatusCurrentMode_Object((1,3,6,1,2,1,197,1,2,1),_NtpEntStatusCurrentMode_Type())
ntpEntStatusCurrentMode.setMaxAccess(_C)
if mibBuilder.loadTexts:ntpEntStatusCurrentMode.setStatus(_B)
_NtpEntStatusStratum_Type=NtpStratum
_NtpEntStatusStratum_Object=MibScalar
ntpEntStatusStratum=_NtpEntStatusStratum_Object((1,3,6,1,2,1,197,1,2,2),_NtpEntStatusStratum_Type())
ntpEntStatusStratum.setMaxAccess(_C)
if mibBuilder.loadTexts:ntpEntStatusStratum.setStatus(_B)
class _NtpEntStatusActiveRefSourceId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99999))
_NtpEntStatusActiveRefSourceId_Type.__name__=_G
_NtpEntStatusActiveRefSourceId_Object=MibScalar
ntpEntStatusActiveRefSourceId=_NtpEntStatusActiveRefSourceId_Object((1,3,6,1,2,1,197,1,2,3),_NtpEntStatusActiveRefSourceId_Type())
ntpEntStatusActiveRefSourceId.setMaxAccess(_C)
if mibBuilder.loadTexts:ntpEntStatusActiveRefSourceId.setStatus(_B)
_NtpEntStatusActiveRefSourceName_Type=Utf8String
_NtpEntStatusActiveRefSourceName_Object=MibScalar
ntpEntStatusActiveRefSourceName=_NtpEntStatusActiveRefSourceName_Object((1,3,6,1,2,1,197,1,2,4),_NtpEntStatusActiveRefSourceName_Type())
ntpEntStatusActiveRefSourceName.setMaxAccess(_C)
if mibBuilder.loadTexts:ntpEntStatusActiveRefSourceName.setStatus(_B)
_NtpEntStatusActiveOffset_Type=DisplayString
_NtpEntStatusActiveOffset_Object=MibScalar
ntpEntStatusActiveOffset=_NtpEntStatusActiveOffset_Object((1,3,6,1,2,1,197,1,2,5),_NtpEntStatusActiveOffset_Type())
ntpEntStatusActiveOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:ntpEntStatusActiveOffset.setStatus(_B)
class _NtpEntStatusNumberOfRefSources_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_NtpEntStatusNumberOfRefSources_Type.__name__=_G
_NtpEntStatusNumberOfRefSources_Object=MibScalar
ntpEntStatusNumberOfRefSources=_NtpEntStatusNumberOfRefSources_Object((1,3,6,1,2,1,197,1,2,6),_NtpEntStatusNumberOfRefSources_Type())
ntpEntStatusNumberOfRefSources.setMaxAccess(_C)
if mibBuilder.loadTexts:ntpEntStatusNumberOfRefSources.setStatus(_B)
_NtpEntStatusDispersion_Type=DisplayString
_NtpEntStatusDispersion_Object=MibScalar
ntpEntStatusDispersion=_NtpEntStatusDispersion_Object((1,3,6,1,2,1,197,1,2,7),_NtpEntStatusDispersion_Type())
ntpEntStatusDispersion.setMaxAccess(_C)
if mibBuilder.loadTexts:ntpEntStatusDispersion.setStatus(_B)
_NtpEntStatusEntityUptime_Type=TimeTicks
_NtpEntStatusEntityUptime_Object=MibScalar
ntpEntStatusEntityUptime=_NtpEntStatusEntityUptime_Object((1,3,6,1,2,1,197,1,2,8),_NtpEntStatusEntityUptime_Type())
ntpEntStatusEntityUptime.setMaxAccess(_C)
if mibBuilder.loadTexts:ntpEntStatusEntityUptime.setStatus(_B)
_NtpEntStatusDateTime_Type=NtpDateTime
_NtpEntStatusDateTime_Object=MibScalar
ntpEntStatusDateTime=_NtpEntStatusDateTime_Object((1,3,6,1,2,1,197,1,2,9),_NtpEntStatusDateTime_Type())
ntpEntStatusDateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ntpEntStatusDateTime.setStatus(_B)
_NtpEntStatusLeapSecond_Type=NtpDateTime
_NtpEntStatusLeapSecond_Object=MibScalar
ntpEntStatusLeapSecond=_NtpEntStatusLeapSecond_Object((1,3,6,1,2,1,197,1,2,10),_NtpEntStatusLeapSecond_Type())
ntpEntStatusLeapSecond.setMaxAccess(_C)
if mibBuilder.loadTexts:ntpEntStatusLeapSecond.setStatus(_B)
class _NtpEntStatusLeapSecDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,1))
_NtpEntStatusLeapSecDirection_Type.__name__=_H
_NtpEntStatusLeapSecDirection_Object=MibScalar
ntpEntStatusLeapSecDirection=_NtpEntStatusLeapSecDirection_Object((1,3,6,1,2,1,197,1,2,11),_NtpEntStatusLeapSecDirection_Type())
ntpEntStatusLeapSecDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:ntpEntStatusLeapSecDirection.setStatus(_B)
_NtpEntStatusInPkts_Type=Counter32
_NtpEntStatusInPkts_Object=MibScalar
ntpEntStatusInPkts=_NtpEntStatusInPkts_Object((1,3,6,1,2,1,197,1,2,12),_NtpEntStatusInPkts_Type())
ntpEntStatusInPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:ntpEntStatusInPkts.setStatus(_B)
if mibBuilder.loadTexts:ntpEntStatusInPkts.setUnits(_D)
_NtpEntStatusOutPkts_Type=Counter32
_NtpEntStatusOutPkts_Object=MibScalar
ntpEntStatusOutPkts=_NtpEntStatusOutPkts_Object((1,3,6,1,2,1,197,1,2,13),_NtpEntStatusOutPkts_Type())
ntpEntStatusOutPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:ntpEntStatusOutPkts.setStatus(_B)
if mibBuilder.loadTexts:ntpEntStatusOutPkts.setUnits(_D)
_NtpEntStatusBadVersion_Type=Counter32
_NtpEntStatusBadVersion_Object=MibScalar
ntpEntStatusBadVersion=_NtpEntStatusBadVersion_Object((1,3,6,1,2,1,197,1,2,14),_NtpEntStatusBadVersion_Type())
ntpEntStatusBadVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:ntpEntStatusBadVersion.setStatus(_B)
if mibBuilder.loadTexts:ntpEntStatusBadVersion.setUnits(_D)
_NtpEntStatusProtocolError_Type=Counter32
_NtpEntStatusProtocolError_Object=MibScalar
ntpEntStatusProtocolError=_NtpEntStatusProtocolError_Object((1,3,6,1,2,1,197,1,2,15),_NtpEntStatusProtocolError_Type())
ntpEntStatusProtocolError.setMaxAccess(_C)
if mibBuilder.loadTexts:ntpEntStatusProtocolError.setStatus(_B)
if mibBuilder.loadTexts:ntpEntStatusProtocolError.setUnits(_D)
_NtpEntStatusNotifications_Type=Counter32
_NtpEntStatusNotifications_Object=MibScalar
ntpEntStatusNotifications=_NtpEntStatusNotifications_Object((1,3,6,1,2,1,197,1,2,16),_NtpEntStatusNotifications_Type())
ntpEntStatusNotifications.setMaxAccess(_C)
if mibBuilder.loadTexts:ntpEntStatusNotifications.setStatus(_B)
if mibBuilder.loadTexts:ntpEntStatusNotifications.setUnits('notifications')
_NtpEntStatPktModeTable_Object=MibTable
ntpEntStatPktModeTable=_NtpEntStatPktModeTable_Object((1,3,6,1,2,1,197,1,2,17))
if mibBuilder.loadTexts:ntpEntStatPktModeTable.setStatus(_B)
_NtpEntStatPktModeEntry_Object=MibTableRow
ntpEntStatPktModeEntry=_NtpEntStatPktModeEntry_Object((1,3,6,1,2,1,197,1,2,17,1))
ntpEntStatPktModeEntry.setIndexNames((0,_A,_S))
if mibBuilder.loadTexts:ntpEntStatPktModeEntry.setStatus(_B)
class _NtpEntStatPktMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('symetricactive',1),('symetricpassive',2),('client',3),('server',4),('broadcastserver',5),('broadcastclient',6)))
_NtpEntStatPktMode_Type.__name__=_H
_NtpEntStatPktMode_Object=MibTableColumn
ntpEntStatPktMode=_NtpEntStatPktMode_Object((1,3,6,1,2,1,197,1,2,17,1,1),_NtpEntStatPktMode_Type())
ntpEntStatPktMode.setMaxAccess(_T)
if mibBuilder.loadTexts:ntpEntStatPktMode.setStatus(_B)
_NtpEntStatPktSent_Type=Counter32
_NtpEntStatPktSent_Object=MibTableColumn
ntpEntStatPktSent=_NtpEntStatPktSent_Object((1,3,6,1,2,1,197,1,2,17,1,2),_NtpEntStatPktSent_Type())
ntpEntStatPktSent.setMaxAccess(_C)
if mibBuilder.loadTexts:ntpEntStatPktSent.setStatus(_B)
if mibBuilder.loadTexts:ntpEntStatPktSent.setUnits(_D)
_NtpEntStatPktReceived_Type=Counter32
_NtpEntStatPktReceived_Object=MibTableColumn
ntpEntStatPktReceived=_NtpEntStatPktReceived_Object((1,3,6,1,2,1,197,1,2,17,1,3),_NtpEntStatPktReceived_Type())
ntpEntStatPktReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:ntpEntStatPktReceived.setStatus(_B)
if mibBuilder.loadTexts:ntpEntStatPktReceived.setUnits(_D)
_NtpAssociation_ObjectIdentity=ObjectIdentity
ntpAssociation=_NtpAssociation_ObjectIdentity((1,3,6,1,2,1,197,1,3))
_NtpAssociationTable_Object=MibTable
ntpAssociationTable=_NtpAssociationTable_Object((1,3,6,1,2,1,197,1,3,1))
if mibBuilder.loadTexts:ntpAssociationTable.setStatus(_B)
_NtpAssociationEntry_Object=MibTableRow
ntpAssociationEntry=_NtpAssociationEntry_Object((1,3,6,1,2,1,197,1,3,1,1))
ntpAssociationEntry.setIndexNames((0,_A,_K))
if mibBuilder.loadTexts:ntpAssociationEntry.setStatus(_B)
class _NtpAssocId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,99999))
_NtpAssocId_Type.__name__=_G
_NtpAssocId_Object=MibTableColumn
ntpAssocId=_NtpAssocId_Object((1,3,6,1,2,1,197,1,3,1,1,1),_NtpAssocId_Type())
ntpAssocId.setMaxAccess(_T)
if mibBuilder.loadTexts:ntpAssocId.setStatus(_B)
_NtpAssocName_Type=Utf8String
_NtpAssocName_Object=MibTableColumn
ntpAssocName=_NtpAssocName_Object((1,3,6,1,2,1,197,1,3,1,1,2),_NtpAssocName_Type())
ntpAssocName.setMaxAccess(_C)
if mibBuilder.loadTexts:ntpAssocName.setStatus(_B)
_NtpAssocRefId_Type=DisplayString
_NtpAssocRefId_Object=MibTableColumn
ntpAssocRefId=_NtpAssocRefId_Object((1,3,6,1,2,1,197,1,3,1,1,3),_NtpAssocRefId_Type())
ntpAssocRefId.setMaxAccess(_C)
if mibBuilder.loadTexts:ntpAssocRefId.setStatus(_B)
class _NtpAssocAddressType_Type(InetAddressType):subtypeSpec=InetAddressType.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('ipv4',1),('ipv6',2),('ipv4z',3),('ipv6z',4)))
_NtpAssocAddressType_Type.__name__=_Q
_NtpAssocAddressType_Object=MibTableColumn
ntpAssocAddressType=_NtpAssocAddressType_Object((1,3,6,1,2,1,197,1,3,1,1,4),_NtpAssocAddressType_Type())
ntpAssocAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:ntpAssocAddressType.setStatus(_B)
class _NtpAssocAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(8,8),ValueSizeConstraint(16,16),ValueSizeConstraint(20,20))
_NtpAssocAddress_Type.__name__=_P
_NtpAssocAddress_Object=MibTableColumn
ntpAssocAddress=_NtpAssocAddress_Object((1,3,6,1,2,1,197,1,3,1,1,5),_NtpAssocAddress_Type())
ntpAssocAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ntpAssocAddress.setStatus(_B)
_NtpAssocOffset_Type=DisplayString
_NtpAssocOffset_Object=MibTableColumn
ntpAssocOffset=_NtpAssocOffset_Object((1,3,6,1,2,1,197,1,3,1,1,6),_NtpAssocOffset_Type())
ntpAssocOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:ntpAssocOffset.setStatus(_B)
_NtpAssocStratum_Type=NtpStratum
_NtpAssocStratum_Object=MibTableColumn
ntpAssocStratum=_NtpAssocStratum_Object((1,3,6,1,2,1,197,1,3,1,1,7),_NtpAssocStratum_Type())
ntpAssocStratum.setMaxAccess(_C)
if mibBuilder.loadTexts:ntpAssocStratum.setStatus(_B)
_NtpAssocStatusJitter_Type=DisplayString
_NtpAssocStatusJitter_Object=MibTableColumn
ntpAssocStatusJitter=_NtpAssocStatusJitter_Object((1,3,6,1,2,1,197,1,3,1,1,8),_NtpAssocStatusJitter_Type())
ntpAssocStatusJitter.setMaxAccess(_C)
if mibBuilder.loadTexts:ntpAssocStatusJitter.setStatus(_B)
_NtpAssocStatusDelay_Type=DisplayString
_NtpAssocStatusDelay_Object=MibTableColumn
ntpAssocStatusDelay=_NtpAssocStatusDelay_Object((1,3,6,1,2,1,197,1,3,1,1,9),_NtpAssocStatusDelay_Type())
ntpAssocStatusDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:ntpAssocStatusDelay.setStatus(_B)
_NtpAssocStatusDispersion_Type=DisplayString
_NtpAssocStatusDispersion_Object=MibTableColumn
ntpAssocStatusDispersion=_NtpAssocStatusDispersion_Object((1,3,6,1,2,1,197,1,3,1,1,10),_NtpAssocStatusDispersion_Type())
ntpAssocStatusDispersion.setMaxAccess(_C)
if mibBuilder.loadTexts:ntpAssocStatusDispersion.setStatus(_B)
_NtpAssociationStatisticsTable_Object=MibTable
ntpAssociationStatisticsTable=_NtpAssociationStatisticsTable_Object((1,3,6,1,2,1,197,1,3,2))
if mibBuilder.loadTexts:ntpAssociationStatisticsTable.setStatus(_B)
_NtpAssociationStatisticsEntry_Object=MibTableRow
ntpAssociationStatisticsEntry=_NtpAssociationStatisticsEntry_Object((1,3,6,1,2,1,197,1,3,2,1))
ntpAssociationStatisticsEntry.setIndexNames((0,_A,_K))
if mibBuilder.loadTexts:ntpAssociationStatisticsEntry.setStatus(_B)
_NtpAssocStatInPkts_Type=Counter32
_NtpAssocStatInPkts_Object=MibTableColumn
ntpAssocStatInPkts=_NtpAssocStatInPkts_Object((1,3,6,1,2,1,197,1,3,2,1,1),_NtpAssocStatInPkts_Type())
ntpAssocStatInPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:ntpAssocStatInPkts.setStatus(_B)
if mibBuilder.loadTexts:ntpAssocStatInPkts.setUnits(_D)
_NtpAssocStatOutPkts_Type=Counter32
_NtpAssocStatOutPkts_Object=MibTableColumn
ntpAssocStatOutPkts=_NtpAssocStatOutPkts_Object((1,3,6,1,2,1,197,1,3,2,1,2),_NtpAssocStatOutPkts_Type())
ntpAssocStatOutPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:ntpAssocStatOutPkts.setStatus(_B)
if mibBuilder.loadTexts:ntpAssocStatOutPkts.setUnits(_D)
_NtpAssocStatProtocolError_Type=Counter32
_NtpAssocStatProtocolError_Object=MibTableColumn
ntpAssocStatProtocolError=_NtpAssocStatProtocolError_Object((1,3,6,1,2,1,197,1,3,2,1,3),_NtpAssocStatProtocolError_Type())
ntpAssocStatProtocolError.setMaxAccess(_C)
if mibBuilder.loadTexts:ntpAssocStatProtocolError.setStatus(_B)
if mibBuilder.loadTexts:ntpAssocStatProtocolError.setUnits(_D)
_NtpEntControl_ObjectIdentity=ObjectIdentity
ntpEntControl=_NtpEntControl_ObjectIdentity((1,3,6,1,2,1,197,1,4))
class _NtpEntHeartbeatInterval_Type(Unsigned32):defaultValue=60
_NtpEntHeartbeatInterval_Type.__name__=_G
_NtpEntHeartbeatInterval_Object=MibScalar
ntpEntHeartbeatInterval=_NtpEntHeartbeatInterval_Object((1,3,6,1,2,1,197,1,4,1),_NtpEntHeartbeatInterval_Type())
ntpEntHeartbeatInterval.setMaxAccess(_U)
if mibBuilder.loadTexts:ntpEntHeartbeatInterval.setStatus(_B)
if mibBuilder.loadTexts:ntpEntHeartbeatInterval.setUnits('seconds')
class _NtpEntNotifBits_Type(Bits):namedValues=NamedValues(*(('notUsed',0),('entNotifModeChange',1),('entNotifStratumChange',2),('entNotifSyspeerChanged',3),('entNotifAddAssociation',4),('entNotifRemoveAssociation',5),('entNotifConfigChanged',6),('entNotifLeapSecondAnnounced',7),('entNotifHeartbeat',8)))
_NtpEntNotifBits_Type.__name__='Bits'
_NtpEntNotifBits_Object=MibScalar
ntpEntNotifBits=_NtpEntNotifBits_Object((1,3,6,1,2,1,197,1,4,2),_NtpEntNotifBits_Type())
ntpEntNotifBits.setMaxAccess(_U)
if mibBuilder.loadTexts:ntpEntNotifBits.setStatus(_B)
_NtpEntNotifObjects_ObjectIdentity=ObjectIdentity
ntpEntNotifObjects=_NtpEntNotifObjects_ObjectIdentity((1,3,6,1,2,1,197,1,5))
class _NtpEntNotifMessage_Type(Utf8String):defaultValue=OctetString('no event')
_NtpEntNotifMessage_Type.__name__=_R
_NtpEntNotifMessage_Object=MibScalar
ntpEntNotifMessage=_NtpEntNotifMessage_Object((1,3,6,1,2,1,197,1,5,1),_NtpEntNotifMessage_Type())
ntpEntNotifMessage.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:ntpEntNotifMessage.setStatus(_B)
_NtpEntConformance_ObjectIdentity=ObjectIdentity
ntpEntConformance=_NtpEntConformance_ObjectIdentity((1,3,6,1,2,1,197,2))
_NtpEntCompliances_ObjectIdentity=ObjectIdentity
ntpEntCompliances=_NtpEntCompliances_ObjectIdentity((1,3,6,1,2,1,197,2,1))
_NtpEntGroups_ObjectIdentity=ObjectIdentity
ntpEntGroups=_NtpEntGroups_ObjectIdentity((1,3,6,1,2,1,197,2,2))
ntpEntObjectsGroup1=ObjectGroup((1,3,6,1,2,1,197,2,2,1))
ntpEntObjectsGroup1.setObjects(*((_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_E),(_A,_I),(_A,_a),(_A,_b),(_A,_c)))
if mibBuilder.loadTexts:ntpEntObjectsGroup1.setStatus(_B)
ntpEntObjectsGroup2=ObjectGroup((1,3,6,1,2,1,197,2,2,2))
ntpEntObjectsGroup2.setObjects(*((_A,_d),(_A,_e),(_A,_f),(_A,_J),(_A,_L),(_A,_M),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_N),(_A,_A1),(_A,_F)))
if mibBuilder.loadTexts:ntpEntObjectsGroup2.setStatus(_B)
ntpEntNotifModeChange=NotificationType((1,3,6,1,2,1,197,0,1))
ntpEntNotifModeChange.setObjects((_A,_J))
if mibBuilder.loadTexts:ntpEntNotifModeChange.setStatus(_B)
ntpEntNotifStratumChange=NotificationType((1,3,6,1,2,1,197,0,2))
ntpEntNotifStratumChange.setObjects(*((_A,_E),(_A,_L),(_A,_F)))
if mibBuilder.loadTexts:ntpEntNotifStratumChange.setStatus(_B)
ntpEntNotifSyspeerChanged=NotificationType((1,3,6,1,2,1,197,0,3))
ntpEntNotifSyspeerChanged.setObjects(*((_A,_E),(_A,_M),(_A,_F)))
if mibBuilder.loadTexts:ntpEntNotifSyspeerChanged.setStatus(_B)
ntpEntNotifAddAssociation=NotificationType((1,3,6,1,2,1,197,0,4))
ntpEntNotifAddAssociation.setObjects(*((_A,_E),(_A,_I),(_A,_F)))
if mibBuilder.loadTexts:ntpEntNotifAddAssociation.setStatus(_B)
ntpEntNotifRemoveAssociation=NotificationType((1,3,6,1,2,1,197,0,5))
ntpEntNotifRemoveAssociation.setObjects(*((_A,_E),(_A,_I),(_A,_F)))
if mibBuilder.loadTexts:ntpEntNotifRemoveAssociation.setStatus(_B)
ntpEntNotifConfigChanged=NotificationType((1,3,6,1,2,1,197,0,6))
ntpEntNotifConfigChanged.setObjects(*((_A,_E),(_A,_F)))
if mibBuilder.loadTexts:ntpEntNotifConfigChanged.setStatus(_B)
ntpEntNotifLeapSecondAnnounced=NotificationType((1,3,6,1,2,1,197,0,7))
ntpEntNotifLeapSecondAnnounced.setObjects(*((_A,_E),(_A,_F)))
if mibBuilder.loadTexts:ntpEntNotifLeapSecondAnnounced.setStatus(_B)
ntpEntNotifHeartbeat=NotificationType((1,3,6,1,2,1,197,0,8))
ntpEntNotifHeartbeat.setObjects(*((_A,_E),(_A,_J),(_A,_N),(_A,_F)))
if mibBuilder.loadTexts:ntpEntNotifHeartbeat.setStatus(_B)
ntpEntNotifGroup=NotificationGroup((1,3,6,1,2,1,197,2,2,3))
ntpEntNotifGroup.setObjects(*((_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9)))
if mibBuilder.loadTexts:ntpEntNotifGroup.setStatus(_B)
ntpEntNTPCompliance=ModuleCompliance((1,3,6,1,2,1,197,2,1,1))
ntpEntNTPCompliance.setObjects((_A,_O))
if mibBuilder.loadTexts:ntpEntNTPCompliance.setStatus(_B)
ntpEntSNTPCompliance=ModuleCompliance((1,3,6,1,2,1,197,2,1,2))
ntpEntSNTPCompliance.setObjects(*((_A,_O),(_A,_AA),(_A,_AB)))
if mibBuilder.loadTexts:ntpEntSNTPCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'NtpStratum':NtpStratum,'NtpDateTime':NtpDateTime,'ntpSnmpMIB':ntpSnmpMIB,'ntpEntNotifications':ntpEntNotifications,_A2:ntpEntNotifModeChange,_A3:ntpEntNotifStratumChange,_A4:ntpEntNotifSyspeerChanged,_A5:ntpEntNotifAddAssociation,_A6:ntpEntNotifRemoveAssociation,_A7:ntpEntNotifConfigChanged,_A8:ntpEntNotifLeapSecondAnnounced,_A9:ntpEntNotifHeartbeat,'ntpSnmpMIBObjects':ntpSnmpMIBObjects,'ntpEntInfo':ntpEntInfo,_V:ntpEntSoftwareName,_W:ntpEntSoftwareVersion,_X:ntpEntSoftwareVendor,_Y:ntpEntSystemType,_d:ntpEntTimeResolution,_e:ntpEntTimePrecision,_f:ntpEntTimeDistance,'ntpEntStatus':ntpEntStatus,_J:ntpEntStatusCurrentMode,_L:ntpEntStatusStratum,_M:ntpEntStatusActiveRefSourceId,_g:ntpEntStatusActiveRefSourceName,_h:ntpEntStatusActiveOffset,_i:ntpEntStatusNumberOfRefSources,_j:ntpEntStatusDispersion,_Z:ntpEntStatusEntityUptime,_E:ntpEntStatusDateTime,_k:ntpEntStatusLeapSecond,_l:ntpEntStatusLeapSecDirection,_m:ntpEntStatusInPkts,_n:ntpEntStatusOutPkts,_o:ntpEntStatusBadVersion,_p:ntpEntStatusProtocolError,_q:ntpEntStatusNotifications,'ntpEntStatPktModeTable':ntpEntStatPktModeTable,'ntpEntStatPktModeEntry':ntpEntStatPktModeEntry,_S:ntpEntStatPktMode,_r:ntpEntStatPktSent,_s:ntpEntStatPktReceived,'ntpAssociation':ntpAssociation,'ntpAssociationTable':ntpAssociationTable,'ntpAssociationEntry':ntpAssociationEntry,_K:ntpAssocId,_I:ntpAssocName,_a:ntpAssocRefId,_b:ntpAssocAddressType,_c:ntpAssocAddress,_t:ntpAssocOffset,_u:ntpAssocStratum,_v:ntpAssocStatusJitter,_w:ntpAssocStatusDelay,_x:ntpAssocStatusDispersion,'ntpAssociationStatisticsTable':ntpAssociationStatisticsTable,'ntpAssociationStatisticsEntry':ntpAssociationStatisticsEntry,_y:ntpAssocStatInPkts,_z:ntpAssocStatOutPkts,_A0:ntpAssocStatProtocolError,'ntpEntControl':ntpEntControl,_N:ntpEntHeartbeatInterval,_A1:ntpEntNotifBits,'ntpEntNotifObjects':ntpEntNotifObjects,_F:ntpEntNotifMessage,'ntpEntConformance':ntpEntConformance,'ntpEntCompliances':ntpEntCompliances,'ntpEntNTPCompliance':ntpEntNTPCompliance,'ntpEntSNTPCompliance':ntpEntSNTPCompliance,'ntpEntGroups':ntpEntGroups,_O:ntpEntObjectsGroup1,_AA:ntpEntObjectsGroup2,_AB:ntpEntNotifGroup})