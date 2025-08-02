_h='cannoAudioFileGroup'
_g='cannoControlGroup'
_f='cannoAudioFileRowStatus'
_e='cannoAudioFileAdminDeletion'
_d='cannoAudioFileAge'
_c='cannoAudioFileType'
_b='cannoAudioFileDuration'
_a='cannoAudioFilePlayNoc'
_Z='cannoAudioFileOperStatus'
_Y='cannoAudioFileStatus'
_X='cannoAudioFileName'
_W='cannoAudioFileDescr'
_V='cannoMaxPermanent'
_U='cannoReqTimeout'
_T='cannoSubDirPath'
_S='cannoAgeTime'
_R='cannoIpAddress'
_Q='cannoIpAddressType'
_P='cannoDnResolution'
_O='cannoAudioFileServerName'
_N='cannoAudioFileNumber'
_M='minutes'
_L='InetAddressType'
_K='InetAddress'
_J='read-only'
_I='cmgwIndex'
_H='CISCO-MEDIA-GATEWAY-MIB'
_G='SnmpAdminString'
_F='Integer32'
_E='read-create'
_D='read-write'
_C='Unsigned32'
_B='CISCO-ANNOUNCEMENT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cmgwIndex,=mibBuilder.importSymbols(_H,_I)
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_K,_L)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_C,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
ciscoAnnouncementMIB=ModuleIdentity((1,3,6,1,4,1,9,9,8888))
if mibBuilder.loadTexts:ciscoAnnouncementMIB.setRevisions(('2003-03-25 00:00',))
_CiscoAnnouncementMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoAnnouncementMIBNotifs=_CiscoAnnouncementMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,8888,0))
_CiscoAnnouncementMIBObjects_ObjectIdentity=ObjectIdentity
ciscoAnnouncementMIBObjects=_CiscoAnnouncementMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,8888,1))
_CannoGeneric_ObjectIdentity=ObjectIdentity
cannoGeneric=_CannoGeneric_ObjectIdentity((1,3,6,1,4,1,9,9,8888,1,1))
_CannoControlConfig_ObjectIdentity=ObjectIdentity
cannoControlConfig=_CannoControlConfig_ObjectIdentity((1,3,6,1,4,1,9,9,8888,1,1,1))
_CannoControlTable_Object=MibTable
cannoControlTable=_CannoControlTable_Object((1,3,6,1,4,1,9,9,8888,1,1,1,1))
if mibBuilder.loadTexts:cannoControlTable.setStatus(_A)
_CannoControlEntry_Object=MibTableRow
cannoControlEntry=_CannoControlEntry_Object((1,3,6,1,4,1,9,9,8888,1,1,1,1,1))
cannoControlEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:cannoControlEntry.setStatus(_A)
class _CannoAudioFileServerName_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CannoAudioFileServerName_Type.__name__=_G
_CannoAudioFileServerName_Object=MibTableColumn
cannoAudioFileServerName=_CannoAudioFileServerName_Object((1,3,6,1,4,1,9,9,8888,1,1,1,1,1,1),_CannoAudioFileServerName_Type())
cannoAudioFileServerName.setMaxAccess(_D)
if mibBuilder.loadTexts:cannoAudioFileServerName.setStatus(_A)
class _CannoDnResolution_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('internalOnly',1),('externalOnly',2)))
_CannoDnResolution_Type.__name__=_F
_CannoDnResolution_Object=MibTableColumn
cannoDnResolution=_CannoDnResolution_Object((1,3,6,1,4,1,9,9,8888,1,1,1,1,1,2),_CannoDnResolution_Type())
cannoDnResolution.setMaxAccess(_D)
if mibBuilder.loadTexts:cannoDnResolution.setStatus(_A)
class _CannoIpAddressType_Type(InetAddressType):defaultValue=1
_CannoIpAddressType_Type.__name__=_L
_CannoIpAddressType_Object=MibTableColumn
cannoIpAddressType=_CannoIpAddressType_Object((1,3,6,1,4,1,9,9,8888,1,1,1,1,1,3),_CannoIpAddressType_Type())
cannoIpAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:cannoIpAddressType.setStatus(_A)
class _CannoIpAddress_Type(InetAddress):defaultHexValue='00000000'
_CannoIpAddress_Type.__name__=_K
_CannoIpAddress_Object=MibTableColumn
cannoIpAddress=_CannoIpAddress_Object((1,3,6,1,4,1,9,9,8888,1,1,1,1,1,4),_CannoIpAddress_Type())
cannoIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:cannoIpAddress.setStatus(_A)
class _CannoAgeTime_Type(Unsigned32):defaultValue=10080;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CannoAgeTime_Type.__name__=_C
_CannoAgeTime_Object=MibTableColumn
cannoAgeTime=_CannoAgeTime_Object((1,3,6,1,4,1,9,9,8888,1,1,1,1,1,5),_CannoAgeTime_Type())
cannoAgeTime.setMaxAccess(_D)
if mibBuilder.loadTexts:cannoAgeTime.setStatus(_A)
if mibBuilder.loadTexts:cannoAgeTime.setUnits(_M)
class _CannoSubDirPath_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CannoSubDirPath_Type.__name__=_G
_CannoSubDirPath_Object=MibTableColumn
cannoSubDirPath=_CannoSubDirPath_Object((1,3,6,1,4,1,9,9,8888,1,1,1,1,1,6),_CannoSubDirPath_Type())
cannoSubDirPath.setMaxAccess(_D)
if mibBuilder.loadTexts:cannoSubDirPath.setStatus(_A)
class _CannoReqTimeout_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,50))
_CannoReqTimeout_Type.__name__=_C
_CannoReqTimeout_Object=MibTableColumn
cannoReqTimeout=_CannoReqTimeout_Object((1,3,6,1,4,1,9,9,8888,1,1,1,1,1,7),_CannoReqTimeout_Type())
cannoReqTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:cannoReqTimeout.setStatus(_A)
if mibBuilder.loadTexts:cannoReqTimeout.setUnits('seconds')
class _CannoMaxPermanent_Type(Unsigned32):defaultValue=41;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,500))
_CannoMaxPermanent_Type.__name__=_C
_CannoMaxPermanent_Object=MibTableColumn
cannoMaxPermanent=_CannoMaxPermanent_Object((1,3,6,1,4,1,9,9,8888,1,1,1,1,1,8),_CannoMaxPermanent_Type())
cannoMaxPermanent.setMaxAccess(_D)
if mibBuilder.loadTexts:cannoMaxPermanent.setStatus(_A)
_CannoAudioFileConfig_ObjectIdentity=ObjectIdentity
cannoAudioFileConfig=_CannoAudioFileConfig_ObjectIdentity((1,3,6,1,4,1,9,9,8888,1,1,2))
_CannoAudioFileTable_Object=MibTable
cannoAudioFileTable=_CannoAudioFileTable_Object((1,3,6,1,4,1,9,9,8888,1,1,2,1))
if mibBuilder.loadTexts:cannoAudioFileTable.setStatus(_A)
_CannoAudioFileEntry_Object=MibTableRow
cannoAudioFileEntry=_CannoAudioFileEntry_Object((1,3,6,1,4,1,9,9,8888,1,1,2,1,1))
cannoAudioFileEntry.setIndexNames((0,_H,_I),(0,_B,_N))
if mibBuilder.loadTexts:cannoAudioFileEntry.setStatus(_A)
class _CannoAudioFileNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,9999))
_CannoAudioFileNumber_Type.__name__=_C
_CannoAudioFileNumber_Object=MibTableColumn
cannoAudioFileNumber=_CannoAudioFileNumber_Object((1,3,6,1,4,1,9,9,8888,1,1,2,1,1,1),_CannoAudioFileNumber_Type())
cannoAudioFileNumber.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cannoAudioFileNumber.setStatus(_A)
class _CannoAudioFileDescr_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CannoAudioFileDescr_Type.__name__=_G
_CannoAudioFileDescr_Object=MibTableColumn
cannoAudioFileDescr=_CannoAudioFileDescr_Object((1,3,6,1,4,1,9,9,8888,1,1,2,1,1,2),_CannoAudioFileDescr_Type())
cannoAudioFileDescr.setMaxAccess(_E)
if mibBuilder.loadTexts:cannoAudioFileDescr.setStatus(_A)
class _CannoAudioFileName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CannoAudioFileName_Type.__name__=_G
_CannoAudioFileName_Object=MibTableColumn
cannoAudioFileName=_CannoAudioFileName_Object((1,3,6,1,4,1,9,9,8888,1,1,2,1,1,3),_CannoAudioFileName_Type())
cannoAudioFileName.setMaxAccess(_E)
if mibBuilder.loadTexts:cannoAudioFileName.setStatus(_A)
class _CannoAudioFileStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('cached',1),('loading',2),('invalidFile',3),('loadFailed',4),('notCached',5)))
_CannoAudioFileStatus_Type.__name__=_F
_CannoAudioFileStatus_Object=MibTableColumn
cannoAudioFileStatus=_CannoAudioFileStatus_Object((1,3,6,1,4,1,9,9,8888,1,1,2,1,1,4),_CannoAudioFileStatus_Type())
cannoAudioFileStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:cannoAudioFileStatus.setStatus(_A)
class _CannoAudioFileOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('inPlaying',1),('notPlaying',2),('delPending',3)))
_CannoAudioFileOperStatus_Type.__name__=_F
_CannoAudioFileOperStatus_Object=MibTableColumn
cannoAudioFileOperStatus=_CannoAudioFileOperStatus_Object((1,3,6,1,4,1,9,9,8888,1,1,2,1,1,5),_CannoAudioFileOperStatus_Type())
cannoAudioFileOperStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:cannoAudioFileOperStatus.setStatus(_A)
class _CannoAudioFilePlayNoc_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CannoAudioFilePlayNoc_Type.__name__=_C
_CannoAudioFilePlayNoc_Object=MibTableColumn
cannoAudioFilePlayNoc=_CannoAudioFilePlayNoc_Object((1,3,6,1,4,1,9,9,8888,1,1,2,1,1,6),_CannoAudioFilePlayNoc_Type())
cannoAudioFilePlayNoc.setMaxAccess(_E)
if mibBuilder.loadTexts:cannoAudioFilePlayNoc.setStatus(_A)
class _CannoAudioFileDuration_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CannoAudioFileDuration_Type.__name__=_C
_CannoAudioFileDuration_Object=MibTableColumn
cannoAudioFileDuration=_CannoAudioFileDuration_Object((1,3,6,1,4,1,9,9,8888,1,1,2,1,1,7),_CannoAudioFileDuration_Type())
cannoAudioFileDuration.setMaxAccess(_E)
if mibBuilder.loadTexts:cannoAudioFileDuration.setStatus(_A)
if mibBuilder.loadTexts:cannoAudioFileDuration.setUnits('10 milliseconds')
class _CannoAudioFileType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dynamic',1),('permanent',2)))
_CannoAudioFileType_Type.__name__=_F
_CannoAudioFileType_Object=MibTableColumn
cannoAudioFileType=_CannoAudioFileType_Object((1,3,6,1,4,1,9,9,8888,1,1,2,1,1,8),_CannoAudioFileType_Type())
cannoAudioFileType.setMaxAccess(_E)
if mibBuilder.loadTexts:cannoAudioFileType.setStatus(_A)
class _CannoAudioFileAge_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CannoAudioFileAge_Type.__name__=_C
_CannoAudioFileAge_Object=MibTableColumn
cannoAudioFileAge=_CannoAudioFileAge_Object((1,3,6,1,4,1,9,9,8888,1,1,2,1,1,9),_CannoAudioFileAge_Type())
cannoAudioFileAge.setMaxAccess(_J)
if mibBuilder.loadTexts:cannoAudioFileAge.setStatus(_A)
if mibBuilder.loadTexts:cannoAudioFileAge.setUnits(_M)
class _CannoAudioFileAdminDeletion_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('gracefully',1),('forcefully',2)))
_CannoAudioFileAdminDeletion_Type.__name__=_F
_CannoAudioFileAdminDeletion_Object=MibTableColumn
cannoAudioFileAdminDeletion=_CannoAudioFileAdminDeletion_Object((1,3,6,1,4,1,9,9,8888,1,1,2,1,1,10),_CannoAudioFileAdminDeletion_Type())
cannoAudioFileAdminDeletion.setMaxAccess(_E)
if mibBuilder.loadTexts:cannoAudioFileAdminDeletion.setStatus(_A)
_CannoAudioFileRowStatus_Type=RowStatus
_CannoAudioFileRowStatus_Object=MibTableColumn
cannoAudioFileRowStatus=_CannoAudioFileRowStatus_Object((1,3,6,1,4,1,9,9,8888,1,1,2,1,1,11),_CannoAudioFileRowStatus_Type())
cannoAudioFileRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cannoAudioFileRowStatus.setStatus(_A)
_CiscoAnnouncementMIBConformance_ObjectIdentity=ObjectIdentity
ciscoAnnouncementMIBConformance=_CiscoAnnouncementMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,8888,2))
_CannoMIBCompliances_ObjectIdentity=ObjectIdentity
cannoMIBCompliances=_CannoMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,8888,2,1))
_CannoMIBGroups_ObjectIdentity=ObjectIdentity
cannoMIBGroups=_CannoMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,8888,2,2))
cannoControlGroup=ObjectGroup((1,3,6,1,4,1,9,9,8888,2,2,1))
cannoControlGroup.setObjects(*((_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:cannoControlGroup.setStatus(_A)
cannoAudioFileGroup=ObjectGroup((1,3,6,1,4,1,9,9,8888,2,2,2))
cannoAudioFileGroup.setObjects(*((_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f)))
if mibBuilder.loadTexts:cannoAudioFileGroup.setStatus(_A)
cannoMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,8888,2,1,1))
cannoMIBCompliance.setObjects(*((_B,_g),(_B,_h)))
if mibBuilder.loadTexts:cannoMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoAnnouncementMIB':ciscoAnnouncementMIB,'ciscoAnnouncementMIBNotifs':ciscoAnnouncementMIBNotifs,'ciscoAnnouncementMIBObjects':ciscoAnnouncementMIBObjects,'cannoGeneric':cannoGeneric,'cannoControlConfig':cannoControlConfig,'cannoControlTable':cannoControlTable,'cannoControlEntry':cannoControlEntry,_O:cannoAudioFileServerName,_P:cannoDnResolution,_Q:cannoIpAddressType,_R:cannoIpAddress,_S:cannoAgeTime,_T:cannoSubDirPath,_U:cannoReqTimeout,_V:cannoMaxPermanent,'cannoAudioFileConfig':cannoAudioFileConfig,'cannoAudioFileTable':cannoAudioFileTable,'cannoAudioFileEntry':cannoAudioFileEntry,_N:cannoAudioFileNumber,_W:cannoAudioFileDescr,_X:cannoAudioFileName,_Y:cannoAudioFileStatus,_Z:cannoAudioFileOperStatus,_a:cannoAudioFilePlayNoc,_b:cannoAudioFileDuration,_c:cannoAudioFileType,_d:cannoAudioFileAge,_e:cannoAudioFileAdminDeletion,_f:cannoAudioFileRowStatus,'ciscoAnnouncementMIBConformance':ciscoAnnouncementMIBConformance,'cannoMIBCompliances':cannoMIBCompliances,'cannoMIBCompliance':cannoMIBCompliance,'cannoMIBGroups':cannoMIBGroups,_g:cannoControlGroup,_h:cannoAudioFileGroup})