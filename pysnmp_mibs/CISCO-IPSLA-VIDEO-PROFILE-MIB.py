_a='ciscoIpslaVideoProfileIsrg2Pvdm3Group'
_Z='ciscoIpslaVideoProfileBaseGroup'
_Y='cipslaVideoProfileRtpJitterPattern'
_X='cipslaVideoProfileRtpAvgSize'
_W='cipslaVideoProfileIframeRefreshInterval'
_V='cipslaVideoProfileIframeMaxSize'
_U='cipslaVideoProfileBitrateWindowSize'
_T='cipslaVideoProfileMinBitrate'
_S='cipslaVideoProfileMaxBitrate'
_R='cipslaVideoProfileAvgBitrate'
_Q='cipslaVideoProfileResolution'
_P='cipslaVideoProfileFrameRate'
_O='cipslaVideoProfileVideoContents'
_N='cipslaVideoProfileCodec'
_M='cipslaVideoProfileEndpointType'
_L='cipslaVideoProfileName'
_K='cipslaVideoProfileDescription'
_J='cipslaVideoProfileStorageType'
_I='cipslaVideoProfileRowStatus'
_H='cipslaVideoProfileID'
_G='CvcVideoProfile'
_F='kbps'
_E='Integer32'
_D='Unsigned32'
_C='read-create'
_B='CISCO-IPSLA-VIDEO-PROFILE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CvcVideoProfile,=mibBuilder.importSymbols('CISCO-VIDEO-SESSION-MIB',_G)
CvcVideoResolution,=mibBuilder.importSymbols('CISCO-VIDEO-TC','CvcVideoResolution')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','StorageType','TextualConvention')
ciscoIpslaVideoProfileMIB=ModuleIdentity((1,3,6,1,4,1,9,9,766))
if mibBuilder.loadTexts:ciscoIpslaVideoProfileMIB.setRevisions(('2011-01-24 00:00',))
_CiscoIpslaVideoProfileMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoIpslaVideoProfileMIBNotifs=_CiscoIpslaVideoProfileMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,766,0))
_CiscoIpslaVideoProfileMIBObjects_ObjectIdentity=ObjectIdentity
ciscoIpslaVideoProfileMIBObjects=_CiscoIpslaVideoProfileMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,766,1))
_CipslaVideoProfile_ObjectIdentity=ObjectIdentity
cipslaVideoProfile=_CipslaVideoProfile_ObjectIdentity((1,3,6,1,4,1,9,9,766,1,1))
_CipslaVideoProfileTable_Object=MibTable
cipslaVideoProfileTable=_CipslaVideoProfileTable_Object((1,3,6,1,4,1,9,9,766,1,1,1))
if mibBuilder.loadTexts:cipslaVideoProfileTable.setStatus(_A)
_CipslaVideoProfileEntry_Object=MibTableRow
cipslaVideoProfileEntry=_CipslaVideoProfileEntry_Object((1,3,6,1,4,1,9,9,766,1,1,1,1))
cipslaVideoProfileEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:cipslaVideoProfileEntry.setStatus(_A)
class _CipslaVideoProfileID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CipslaVideoProfileID_Type.__name__=_D
_CipslaVideoProfileID_Object=MibTableColumn
cipslaVideoProfileID=_CipslaVideoProfileID_Object((1,3,6,1,4,1,9,9,766,1,1,1,1,1),_CipslaVideoProfileID_Type())
cipslaVideoProfileID.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cipslaVideoProfileID.setStatus(_A)
_CipslaVideoProfileRowStatus_Type=RowStatus
_CipslaVideoProfileRowStatus_Object=MibTableColumn
cipslaVideoProfileRowStatus=_CipslaVideoProfileRowStatus_Object((1,3,6,1,4,1,9,9,766,1,1,1,1,2),_CipslaVideoProfileRowStatus_Type())
cipslaVideoProfileRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaVideoProfileRowStatus.setStatus(_A)
_CipslaVideoProfileStorageType_Type=StorageType
_CipslaVideoProfileStorageType_Object=MibTableColumn
cipslaVideoProfileStorageType=_CipslaVideoProfileStorageType_Object((1,3,6,1,4,1,9,9,766,1,1,1,1,3),_CipslaVideoProfileStorageType_Type())
cipslaVideoProfileStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaVideoProfileStorageType.setStatus(_A)
_CipslaVideoProfileName_Type=SnmpAdminString
_CipslaVideoProfileName_Object=MibTableColumn
cipslaVideoProfileName=_CipslaVideoProfileName_Object((1,3,6,1,4,1,9,9,766,1,1,1,1,4),_CipslaVideoProfileName_Type())
cipslaVideoProfileName.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaVideoProfileName.setStatus(_A)
_CipslaVideoProfileDescription_Type=SnmpAdminString
_CipslaVideoProfileDescription_Object=MibTableColumn
cipslaVideoProfileDescription=_CipslaVideoProfileDescription_Object((1,3,6,1,4,1,9,9,766,1,1,1,1,5),_CipslaVideoProfileDescription_Type())
cipslaVideoProfileDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaVideoProfileDescription.setStatus(_A)
class _CipslaVideoProfileEndpointType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,21,22,31,9999)));namedValues=NamedValues(*(('custom',1),('cts1k',21),('cts3k',22),('cp99xx',31),('unknown',9999)))
_CipslaVideoProfileEndpointType_Type.__name__=_E
_CipslaVideoProfileEndpointType_Object=MibTableColumn
cipslaVideoProfileEndpointType=_CipslaVideoProfileEndpointType_Object((1,3,6,1,4,1,9,9,766,1,1,1,1,6),_CipslaVideoProfileEndpointType_Type())
cipslaVideoProfileEndpointType.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaVideoProfileEndpointType.setStatus(_A)
class _CipslaVideoProfileCodec_Type(CvcVideoProfile):defaultValue=100
_CipslaVideoProfileCodec_Type.__name__=_G
_CipslaVideoProfileCodec_Object=MibTableColumn
cipslaVideoProfileCodec=_CipslaVideoProfileCodec_Object((1,3,6,1,4,1,9,9,766,1,1,1,1,7),_CipslaVideoProfileCodec_Type())
cipslaVideoProfileCodec.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaVideoProfileCodec.setStatus(_A)
class _CipslaVideoProfileVideoContents_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,255)));namedValues=NamedValues(*(('conferenceRoom',1),('singlePerson',2),('presentation',3),('sports',4),('streetView',5),('other',255)))
_CipslaVideoProfileVideoContents_Type.__name__=_E
_CipslaVideoProfileVideoContents_Object=MibTableColumn
cipslaVideoProfileVideoContents=_CipslaVideoProfileVideoContents_Object((1,3,6,1,4,1,9,9,766,1,1,1,1,8),_CipslaVideoProfileVideoContents_Type())
cipslaVideoProfileVideoContents.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaVideoProfileVideoContents.setStatus(_A)
class _CipslaVideoProfileFrameRate_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,120000))
_CipslaVideoProfileFrameRate_Type.__name__=_D
_CipslaVideoProfileFrameRate_Object=MibTableColumn
cipslaVideoProfileFrameRate=_CipslaVideoProfileFrameRate_Object((1,3,6,1,4,1,9,9,766,1,1,1,1,9),_CipslaVideoProfileFrameRate_Type())
cipslaVideoProfileFrameRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaVideoProfileFrameRate.setStatus(_A)
if mibBuilder.loadTexts:cipslaVideoProfileFrameRate.setUnits('fpks')
_CipslaVideoProfileResolution_Type=CvcVideoResolution
_CipslaVideoProfileResolution_Object=MibTableColumn
cipslaVideoProfileResolution=_CipslaVideoProfileResolution_Object((1,3,6,1,4,1,9,9,766,1,1,1,1,10),_CipslaVideoProfileResolution_Type())
cipslaVideoProfileResolution.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaVideoProfileResolution.setStatus(_A)
class _CipslaVideoProfileAvgBitrate_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24000))
_CipslaVideoProfileAvgBitrate_Type.__name__=_D
_CipslaVideoProfileAvgBitrate_Object=MibTableColumn
cipslaVideoProfileAvgBitrate=_CipslaVideoProfileAvgBitrate_Object((1,3,6,1,4,1,9,9,766,1,1,1,1,11),_CipslaVideoProfileAvgBitrate_Type())
cipslaVideoProfileAvgBitrate.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaVideoProfileAvgBitrate.setStatus(_A)
if mibBuilder.loadTexts:cipslaVideoProfileAvgBitrate.setUnits(_F)
class _CipslaVideoProfileMaxBitrate_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,240000))
_CipslaVideoProfileMaxBitrate_Type.__name__=_D
_CipslaVideoProfileMaxBitrate_Object=MibTableColumn
cipslaVideoProfileMaxBitrate=_CipslaVideoProfileMaxBitrate_Object((1,3,6,1,4,1,9,9,766,1,1,1,1,12),_CipslaVideoProfileMaxBitrate_Type())
cipslaVideoProfileMaxBitrate.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaVideoProfileMaxBitrate.setStatus(_A)
if mibBuilder.loadTexts:cipslaVideoProfileMaxBitrate.setUnits(_F)
class _CipslaVideoProfileMinBitrate_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24000))
_CipslaVideoProfileMinBitrate_Type.__name__=_D
_CipslaVideoProfileMinBitrate_Object=MibTableColumn
cipslaVideoProfileMinBitrate=_CipslaVideoProfileMinBitrate_Object((1,3,6,1,4,1,9,9,766,1,1,1,1,13),_CipslaVideoProfileMinBitrate_Type())
cipslaVideoProfileMinBitrate.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaVideoProfileMinBitrate.setStatus(_A)
if mibBuilder.loadTexts:cipslaVideoProfileMinBitrate.setUnits(_F)
class _CipslaVideoProfileBitrateWindowSize_Type(Unsigned32):defaultValue=500;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_CipslaVideoProfileBitrateWindowSize_Type.__name__=_D
_CipslaVideoProfileBitrateWindowSize_Object=MibTableColumn
cipslaVideoProfileBitrateWindowSize=_CipslaVideoProfileBitrateWindowSize_Object((1,3,6,1,4,1,9,9,766,1,1,1,1,14),_CipslaVideoProfileBitrateWindowSize_Type())
cipslaVideoProfileBitrateWindowSize.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaVideoProfileBitrateWindowSize.setStatus(_A)
if mibBuilder.loadTexts:cipslaVideoProfileBitrateWindowSize.setUnits('ms')
class _CipslaVideoProfileIframeMaxSize_Type(Unsigned32):defaultValue=50;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_CipslaVideoProfileIframeMaxSize_Type.__name__=_D
_CipslaVideoProfileIframeMaxSize_Object=MibTableColumn
cipslaVideoProfileIframeMaxSize=_CipslaVideoProfileIframeMaxSize_Object((1,3,6,1,4,1,9,9,766,1,1,1,1,15),_CipslaVideoProfileIframeMaxSize_Type())
cipslaVideoProfileIframeMaxSize.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaVideoProfileIframeMaxSize.setStatus(_A)
if mibBuilder.loadTexts:cipslaVideoProfileIframeMaxSize.setUnits('kB')
class _CipslaVideoProfileIframeRefreshInterval_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_CipslaVideoProfileIframeRefreshInterval_Type.__name__=_D
_CipslaVideoProfileIframeRefreshInterval_Object=MibTableColumn
cipslaVideoProfileIframeRefreshInterval=_CipslaVideoProfileIframeRefreshInterval_Object((1,3,6,1,4,1,9,9,766,1,1,1,1,16),_CipslaVideoProfileIframeRefreshInterval_Type())
cipslaVideoProfileIframeRefreshInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaVideoProfileIframeRefreshInterval.setStatus(_A)
if mibBuilder.loadTexts:cipslaVideoProfileIframeRefreshInterval.setUnits('ms')
class _CipslaVideoProfileRtpAvgSize_Type(Unsigned32):defaultValue=1000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,1600))
_CipslaVideoProfileRtpAvgSize_Type.__name__=_D
_CipslaVideoProfileRtpAvgSize_Object=MibTableColumn
cipslaVideoProfileRtpAvgSize=_CipslaVideoProfileRtpAvgSize_Object((1,3,6,1,4,1,9,9,766,1,1,1,1,17),_CipslaVideoProfileRtpAvgSize_Type())
cipslaVideoProfileRtpAvgSize.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaVideoProfileRtpAvgSize.setStatus(_A)
if mibBuilder.loadTexts:cipslaVideoProfileRtpAvgSize.setUnits('byte')
class _CipslaVideoProfileRtpJitterPattern_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,99)));namedValues=NamedValues(*(('bursty',1),('shaped',2),('other',99)))
_CipslaVideoProfileRtpJitterPattern_Type.__name__=_E
_CipslaVideoProfileRtpJitterPattern_Object=MibTableColumn
cipslaVideoProfileRtpJitterPattern=_CipslaVideoProfileRtpJitterPattern_Object((1,3,6,1,4,1,9,9,766,1,1,1,1,18),_CipslaVideoProfileRtpJitterPattern_Type())
cipslaVideoProfileRtpJitterPattern.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaVideoProfileRtpJitterPattern.setStatus(_A)
_CiscoIpslaVideoProfileMIBConform_ObjectIdentity=ObjectIdentity
ciscoIpslaVideoProfileMIBConform=_CiscoIpslaVideoProfileMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,766,2))
_CiscoIpslaVideoProfileMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoIpslaVideoProfileMIBCompliances=_CiscoIpslaVideoProfileMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,766,2,1))
_CiscoIpslaVideoProfileMIBGroups_ObjectIdentity=ObjectIdentity
ciscoIpslaVideoProfileMIBGroups=_CiscoIpslaVideoProfileMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,766,2,2))
ciscoIpslaVideoProfileBaseGroup=ObjectGroup((1,3,6,1,4,1,9,9,766,2,2,1))
ciscoIpslaVideoProfileBaseGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:ciscoIpslaVideoProfileBaseGroup.setStatus(_A)
ciscoIpslaVideoProfileIsrg2Pvdm3Group=ObjectGroup((1,3,6,1,4,1,9,9,766,2,2,2))
ciscoIpslaVideoProfileIsrg2Pvdm3Group.setObjects(*((_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:ciscoIpslaVideoProfileIsrg2Pvdm3Group.setStatus(_A)
ciscoIpslaVideoProfileMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,766,2,1,1))
ciscoIpslaVideoProfileMIBCompliance.setObjects(*((_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:ciscoIpslaVideoProfileMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoIpslaVideoProfileMIB':ciscoIpslaVideoProfileMIB,'ciscoIpslaVideoProfileMIBNotifs':ciscoIpslaVideoProfileMIBNotifs,'ciscoIpslaVideoProfileMIBObjects':ciscoIpslaVideoProfileMIBObjects,'cipslaVideoProfile':cipslaVideoProfile,'cipslaVideoProfileTable':cipslaVideoProfileTable,'cipslaVideoProfileEntry':cipslaVideoProfileEntry,_H:cipslaVideoProfileID,_I:cipslaVideoProfileRowStatus,_J:cipslaVideoProfileStorageType,_L:cipslaVideoProfileName,_K:cipslaVideoProfileDescription,_M:cipslaVideoProfileEndpointType,_N:cipslaVideoProfileCodec,_O:cipslaVideoProfileVideoContents,_P:cipslaVideoProfileFrameRate,_Q:cipslaVideoProfileResolution,_R:cipslaVideoProfileAvgBitrate,_S:cipslaVideoProfileMaxBitrate,_T:cipslaVideoProfileMinBitrate,_U:cipslaVideoProfileBitrateWindowSize,_V:cipslaVideoProfileIframeMaxSize,_W:cipslaVideoProfileIframeRefreshInterval,_X:cipslaVideoProfileRtpAvgSize,_Y:cipslaVideoProfileRtpJitterPattern,'ciscoIpslaVideoProfileMIBConform':ciscoIpslaVideoProfileMIBConform,'ciscoIpslaVideoProfileMIBCompliances':ciscoIpslaVideoProfileMIBCompliances,'ciscoIpslaVideoProfileMIBCompliance':ciscoIpslaVideoProfileMIBCompliance,'ciscoIpslaVideoProfileMIBGroups':ciscoIpslaVideoProfileMIBGroups,_Z:ciscoIpslaVideoProfileBaseGroup,_a:ciscoIpslaVideoProfileIsrg2Pvdm3Group})