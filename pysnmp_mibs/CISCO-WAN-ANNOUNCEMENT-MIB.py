_T='cwAnnounceTableGroup'
_S='cwAnnounceControlGroup'
_R='cwAnnRowStatus'
_Q='cwAnnFileCodec'
_P='cwAnnFileName'
_O='cwAnnFileStatus'
_N='cwAnnReqTimeout'
_M='cwAnnPrefixPath'
_L='cwAnnPreferenceCodec'
_K='cwAnnAgeTime'
_J='cwAnnFileServerName'
_I='cwAnnMaximumSize'
_H='cwAnnounceNumber'
_G='read-only'
_F='read-create'
_E='DisplayString'
_D='read-write'
_C='Integer32'
_B='CISCO-WAN-ANNOUNCEMENT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoWan,=mibBuilder.importSymbols('CISCOWAN-SMI','ciscoWan')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','RowStatus','TextualConvention')
ciscoWanAnnouncementMIB=ModuleIdentity((1,3,6,1,4,1,351,150,25))
if mibBuilder.loadTexts:ciscoWanAnnouncementMIB.setRevisions(('2003-12-22 00:00','2001-12-26 00:00'))
class AnnCodecType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,7,8,9,11,12,13,14)));namedValues=NamedValues(*(('g711u',1),('g711a',2),('g726r32000',3),('g729a',4),('g729ab',5),('g726r16000',7),('g726r24000',8),('g726r40000',9),('g723h',11),('g723ah',12),('g723l',13),('g723al',14)))
_CwAnnounceGrpMIBObjects_ObjectIdentity=ObjectIdentity
cwAnnounceGrpMIBObjects=_CwAnnounceGrpMIBObjects_ObjectIdentity((1,3,6,1,4,1,351,150,25,1))
_CwAnnounceGeneric_ObjectIdentity=ObjectIdentity
cwAnnounceGeneric=_CwAnnounceGeneric_ObjectIdentity((1,3,6,1,4,1,351,150,25,1,1))
_CwAnnounceControlGrp_ObjectIdentity=ObjectIdentity
cwAnnounceControlGrp=_CwAnnounceControlGrp_ObjectIdentity((1,3,6,1,4,1,351,150,25,1,1,1))
class _CwAnnMaximumSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwAnnMaximumSize_Type.__name__=_C
_CwAnnMaximumSize_Object=MibScalar
cwAnnMaximumSize=_CwAnnMaximumSize_Object((1,3,6,1,4,1,351,150,25,1,1,1,1),_CwAnnMaximumSize_Type())
cwAnnMaximumSize.setMaxAccess(_G)
if mibBuilder.loadTexts:cwAnnMaximumSize.setStatus(_A)
class _CwAnnFileServerName_Type(DisplayString):defaultValue=OctetString(' ');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CwAnnFileServerName_Type.__name__=_E
_CwAnnFileServerName_Object=MibScalar
cwAnnFileServerName=_CwAnnFileServerName_Object((1,3,6,1,4,1,351,150,25,1,1,1,2),_CwAnnFileServerName_Type())
cwAnnFileServerName.setMaxAccess(_D)
if mibBuilder.loadTexts:cwAnnFileServerName.setStatus(_A)
class _CwAnnAgeTime_Type(Integer32):defaultValue=10080;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwAnnAgeTime_Type.__name__=_C
_CwAnnAgeTime_Object=MibScalar
cwAnnAgeTime=_CwAnnAgeTime_Object((1,3,6,1,4,1,351,150,25,1,1,1,3),_CwAnnAgeTime_Type())
cwAnnAgeTime.setMaxAccess(_D)
if mibBuilder.loadTexts:cwAnnAgeTime.setStatus(_A)
if mibBuilder.loadTexts:cwAnnAgeTime.setUnits('minutes')
_CwAnnPreferenceCodec_Type=AnnCodecType
_CwAnnPreferenceCodec_Object=MibScalar
cwAnnPreferenceCodec=_CwAnnPreferenceCodec_Object((1,3,6,1,4,1,351,150,25,1,1,1,4),_CwAnnPreferenceCodec_Type())
cwAnnPreferenceCodec.setMaxAccess(_D)
if mibBuilder.loadTexts:cwAnnPreferenceCodec.setStatus(_A)
class _CwAnnPrefixPath_Type(DisplayString):defaultValue=OctetString(' ');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CwAnnPrefixPath_Type.__name__=_E
_CwAnnPrefixPath_Object=MibScalar
cwAnnPrefixPath=_CwAnnPrefixPath_Object((1,3,6,1,4,1,351,150,25,1,1,1,5),_CwAnnPrefixPath_Type())
cwAnnPrefixPath.setMaxAccess(_D)
if mibBuilder.loadTexts:cwAnnPrefixPath.setStatus(_A)
class _CwAnnReqTimeout_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwAnnReqTimeout_Type.__name__=_C
_CwAnnReqTimeout_Object=MibScalar
cwAnnReqTimeout=_CwAnnReqTimeout_Object((1,3,6,1,4,1,351,150,25,1,1,1,6),_CwAnnReqTimeout_Type())
cwAnnReqTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:cwAnnReqTimeout.setStatus(_A)
if mibBuilder.loadTexts:cwAnnReqTimeout.setUnits('seconds')
_CwAnnounceTableGrp_ObjectIdentity=ObjectIdentity
cwAnnounceTableGrp=_CwAnnounceTableGrp_ObjectIdentity((1,3,6,1,4,1,351,150,25,1,1,2))
_CwAnnounceTable_Object=MibTable
cwAnnounceTable=_CwAnnounceTable_Object((1,3,6,1,4,1,351,150,25,1,1,2,1))
if mibBuilder.loadTexts:cwAnnounceTable.setStatus(_A)
_CwAnnounceEntry_Object=MibTableRow
cwAnnounceEntry=_CwAnnounceEntry_Object((1,3,6,1,4,1,351,150,25,1,1,2,1,1))
cwAnnounceEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:cwAnnounceEntry.setStatus(_A)
class _CwAnnounceNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwAnnounceNumber_Type.__name__=_C
_CwAnnounceNumber_Object=MibTableColumn
cwAnnounceNumber=_CwAnnounceNumber_Object((1,3,6,1,4,1,351,150,25,1,1,2,1,1,1),_CwAnnounceNumber_Type())
cwAnnounceNumber.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cwAnnounceNumber.setStatus(_A)
class _CwAnnFileStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('loaded',1),('loading',2),('invalidFile',3),('loadFailed',4)))
_CwAnnFileStatus_Type.__name__=_C
_CwAnnFileStatus_Object=MibTableColumn
cwAnnFileStatus=_CwAnnFileStatus_Object((1,3,6,1,4,1,351,150,25,1,1,2,1,1,2),_CwAnnFileStatus_Type())
cwAnnFileStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:cwAnnFileStatus.setStatus(_A)
class _CwAnnFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CwAnnFileName_Type.__name__=_E
_CwAnnFileName_Object=MibTableColumn
cwAnnFileName=_CwAnnFileName_Object((1,3,6,1,4,1,351,150,25,1,1,2,1,1,3),_CwAnnFileName_Type())
cwAnnFileName.setMaxAccess(_F)
if mibBuilder.loadTexts:cwAnnFileName.setStatus(_A)
_CwAnnFileCodec_Type=AnnCodecType
_CwAnnFileCodec_Object=MibTableColumn
cwAnnFileCodec=_CwAnnFileCodec_Object((1,3,6,1,4,1,351,150,25,1,1,2,1,1,4),_CwAnnFileCodec_Type())
cwAnnFileCodec.setMaxAccess(_F)
if mibBuilder.loadTexts:cwAnnFileCodec.setStatus(_A)
_CwAnnRowStatus_Type=RowStatus
_CwAnnRowStatus_Object=MibTableColumn
cwAnnRowStatus=_CwAnnRowStatus_Object((1,3,6,1,4,1,351,150,25,1,1,2,1,1,5),_CwAnnRowStatus_Type())
cwAnnRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:cwAnnRowStatus.setStatus(_A)
_CwAnnounceNotificationPrefix_ObjectIdentity=ObjectIdentity
cwAnnounceNotificationPrefix=_CwAnnounceNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,351,150,25,2))
_CwAnnounceNotifications_ObjectIdentity=ObjectIdentity
cwAnnounceNotifications=_CwAnnounceNotifications_ObjectIdentity((1,3,6,1,4,1,351,150,25,2,0))
_CwAnnounceMIBConformance_ObjectIdentity=ObjectIdentity
cwAnnounceMIBConformance=_CwAnnounceMIBConformance_ObjectIdentity((1,3,6,1,4,1,351,150,25,3))
_CwAnnounceMIBCompliances_ObjectIdentity=ObjectIdentity
cwAnnounceMIBCompliances=_CwAnnounceMIBCompliances_ObjectIdentity((1,3,6,1,4,1,351,150,25,3,1))
_CwAnnounceMIBGroups_ObjectIdentity=ObjectIdentity
cwAnnounceMIBGroups=_CwAnnounceMIBGroups_ObjectIdentity((1,3,6,1,4,1,351,150,25,3,2))
cwAnnounceControlGroup=ObjectGroup((1,3,6,1,4,1,351,150,25,3,2,1))
cwAnnounceControlGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:cwAnnounceControlGroup.setStatus(_A)
cwAnnounceTableGroup=ObjectGroup((1,3,6,1,4,1,351,150,25,3,2,2))
cwAnnounceTableGroup.setObjects(*((_B,_O),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:cwAnnounceTableGroup.setStatus(_A)
announceMIBCompliance=ModuleCompliance((1,3,6,1,4,1,351,150,25,3,1,1))
announceMIBCompliance.setObjects(*((_B,_S),(_B,_T)))
if mibBuilder.loadTexts:announceMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'AnnCodecType':AnnCodecType,'ciscoWanAnnouncementMIB':ciscoWanAnnouncementMIB,'cwAnnounceGrpMIBObjects':cwAnnounceGrpMIBObjects,'cwAnnounceGeneric':cwAnnounceGeneric,'cwAnnounceControlGrp':cwAnnounceControlGrp,_I:cwAnnMaximumSize,_J:cwAnnFileServerName,_K:cwAnnAgeTime,_L:cwAnnPreferenceCodec,_M:cwAnnPrefixPath,_N:cwAnnReqTimeout,'cwAnnounceTableGrp':cwAnnounceTableGrp,'cwAnnounceTable':cwAnnounceTable,'cwAnnounceEntry':cwAnnounceEntry,_H:cwAnnounceNumber,_O:cwAnnFileStatus,_P:cwAnnFileName,_Q:cwAnnFileCodec,_R:cwAnnRowStatus,'cwAnnounceNotificationPrefix':cwAnnounceNotificationPrefix,'cwAnnounceNotifications':cwAnnounceNotifications,'cwAnnounceMIBConformance':cwAnnounceMIBConformance,'cwAnnounceMIBCompliances':cwAnnounceMIBCompliances,'announceMIBCompliance':announceMIBCompliance,'cwAnnounceMIBGroups':cwAnnounceMIBGroups,_S:cwAnnounceControlGroup,_T:cwAnnounceTableGroup})