_b='me1200IcfgControlCopyConfigInfoGroup'
_a='me1200IcfgControlGlobalsInfoGroup'
_Z='me1200IcfgStatusCopyConfigInfoGroup'
_Y='me1200IcfgStatusFileTableInfoGroup'
_X='me1200IcfgStatusFileStatisticsInfoGroup'
_W='me1200IcfgControlCopyConfigMerge'
_V='me1200IcfgControlCopyConfigDestinationConfigFile'
_U='me1200IcfgControlCopyConfigDestinationConfigType'
_T='me1200IcfgControlCopyConfigSourceConfigFile'
_S='me1200IcfgControlCopyConfigSourceConfigType'
_R='me1200IcfgControlCopyConfigCopy'
_Q='me1200IcfgControlGlobalsDeleteFile'
_P='me1200IcfgControlGlobalsReloadDefault'
_O='me1200IcfgStatusCopyConfigStatus'
_N='me1200IcfgStatusFileAttribute'
_M='me1200IcfgStatusFileModifiedTime'
_L='me1200IcfgStatusFileBytes'
_K='me1200IcfgStatusFileFileName'
_J='me1200IcfgStatusFileStatisticsTotalBytes'
_I='me1200IcfgStatusFileStatisticsNumberOfFiles'
_H='me1200IcfgStatusFileFileNo'
_G='Integer32'
_F='none'
_E='read-only'
_D='ME1200DisplayString'
_C='read-write'
_B='ME1200-ICFG-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
me1200SwitchMgmt,=mibBuilder.importSymbols('CISCOME1200-MIB','me1200SwitchMgmt')
ME1200DisplayString,=mibBuilder.importSymbols('ME1200-TC',_D)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
me1200IcfgMIB=ModuleIdentity((1,3,6,1,4,1,9,9,815,1,101))
if mibBuilder.loadTexts:me1200IcfgMIB.setRevisions(('2014-02-18 00:00','2014-01-29 00:00','2014-01-09 00:00'))
class ME1200ConfigStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_F,0),('success',1),('inProgress',2),('errOtherInProcessing',3),('errNoSuchFile',4),('errSameSrcDst',5),('errPermissionDenied',6),('errLoadSrc',7),('errSaveDst',8)))
class ME1200ConfigType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_F,0),('runningConfig',1),('startupConfig',2),('configFile',3)))
class ME1200ReloadDefault(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),('default',1),('defaultKeepIp',2)))
_Me1200IcfgMIBObjects_ObjectIdentity=ObjectIdentity
me1200IcfgMIBObjects=_Me1200IcfgMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,101,1))
_Me1200IcfgStatus_ObjectIdentity=ObjectIdentity
me1200IcfgStatus=_Me1200IcfgStatus_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,101,1,3))
_Me1200IcfgStatusFileStatistics_ObjectIdentity=ObjectIdentity
me1200IcfgStatusFileStatistics=_Me1200IcfgStatusFileStatistics_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,101,1,3,1))
_Me1200IcfgStatusFileStatisticsNumberOfFiles_Type=Unsigned32
_Me1200IcfgStatusFileStatisticsNumberOfFiles_Object=MibScalar
me1200IcfgStatusFileStatisticsNumberOfFiles=_Me1200IcfgStatusFileStatisticsNumberOfFiles_Object((1,3,6,1,4,1,9,9,815,1,101,1,3,1,1),_Me1200IcfgStatusFileStatisticsNumberOfFiles_Type())
me1200IcfgStatusFileStatisticsNumberOfFiles.setMaxAccess(_E)
if mibBuilder.loadTexts:me1200IcfgStatusFileStatisticsNumberOfFiles.setStatus(_A)
_Me1200IcfgStatusFileStatisticsTotalBytes_Type=Unsigned32
_Me1200IcfgStatusFileStatisticsTotalBytes_Object=MibScalar
me1200IcfgStatusFileStatisticsTotalBytes=_Me1200IcfgStatusFileStatisticsTotalBytes_Object((1,3,6,1,4,1,9,9,815,1,101,1,3,1,2),_Me1200IcfgStatusFileStatisticsTotalBytes_Type())
me1200IcfgStatusFileStatisticsTotalBytes.setMaxAccess(_E)
if mibBuilder.loadTexts:me1200IcfgStatusFileStatisticsTotalBytes.setStatus(_A)
_Me1200IcfgStatusFileTable_Object=MibTable
me1200IcfgStatusFileTable=_Me1200IcfgStatusFileTable_Object((1,3,6,1,4,1,9,9,815,1,101,1,3,2))
if mibBuilder.loadTexts:me1200IcfgStatusFileTable.setStatus(_A)
_Me1200IcfgStatusFileEntry_Object=MibTableRow
me1200IcfgStatusFileEntry=_Me1200IcfgStatusFileEntry_Object((1,3,6,1,4,1,9,9,815,1,101,1,3,2,1))
me1200IcfgStatusFileEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:me1200IcfgStatusFileEntry.setStatus(_A)
class _Me1200IcfgStatusFileFileNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Me1200IcfgStatusFileFileNo_Type.__name__=_G
_Me1200IcfgStatusFileFileNo_Object=MibTableColumn
me1200IcfgStatusFileFileNo=_Me1200IcfgStatusFileFileNo_Object((1,3,6,1,4,1,9,9,815,1,101,1,3,2,1,1),_Me1200IcfgStatusFileFileNo_Type())
me1200IcfgStatusFileFileNo.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:me1200IcfgStatusFileFileNo.setStatus(_A)
class _Me1200IcfgStatusFileFileName_Type(ME1200DisplayString):subtypeSpec=ME1200DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_Me1200IcfgStatusFileFileName_Type.__name__=_D
_Me1200IcfgStatusFileFileName_Object=MibTableColumn
me1200IcfgStatusFileFileName=_Me1200IcfgStatusFileFileName_Object((1,3,6,1,4,1,9,9,815,1,101,1,3,2,1,2),_Me1200IcfgStatusFileFileName_Type())
me1200IcfgStatusFileFileName.setMaxAccess(_E)
if mibBuilder.loadTexts:me1200IcfgStatusFileFileName.setStatus(_A)
_Me1200IcfgStatusFileBytes_Type=Unsigned32
_Me1200IcfgStatusFileBytes_Object=MibTableColumn
me1200IcfgStatusFileBytes=_Me1200IcfgStatusFileBytes_Object((1,3,6,1,4,1,9,9,815,1,101,1,3,2,1,3),_Me1200IcfgStatusFileBytes_Type())
me1200IcfgStatusFileBytes.setMaxAccess(_E)
if mibBuilder.loadTexts:me1200IcfgStatusFileBytes.setStatus(_A)
class _Me1200IcfgStatusFileModifiedTime_Type(ME1200DisplayString):subtypeSpec=ME1200DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,39))
_Me1200IcfgStatusFileModifiedTime_Type.__name__=_D
_Me1200IcfgStatusFileModifiedTime_Object=MibTableColumn
me1200IcfgStatusFileModifiedTime=_Me1200IcfgStatusFileModifiedTime_Object((1,3,6,1,4,1,9,9,815,1,101,1,3,2,1,4),_Me1200IcfgStatusFileModifiedTime_Type())
me1200IcfgStatusFileModifiedTime.setMaxAccess(_E)
if mibBuilder.loadTexts:me1200IcfgStatusFileModifiedTime.setStatus(_A)
class _Me1200IcfgStatusFileAttribute_Type(ME1200DisplayString):subtypeSpec=ME1200DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_Me1200IcfgStatusFileAttribute_Type.__name__=_D
_Me1200IcfgStatusFileAttribute_Object=MibTableColumn
me1200IcfgStatusFileAttribute=_Me1200IcfgStatusFileAttribute_Object((1,3,6,1,4,1,9,9,815,1,101,1,3,2,1,5),_Me1200IcfgStatusFileAttribute_Type())
me1200IcfgStatusFileAttribute.setMaxAccess(_E)
if mibBuilder.loadTexts:me1200IcfgStatusFileAttribute.setStatus(_A)
_Me1200IcfgStatusCopyConfig_ObjectIdentity=ObjectIdentity
me1200IcfgStatusCopyConfig=_Me1200IcfgStatusCopyConfig_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,101,1,3,3))
_Me1200IcfgStatusCopyConfigStatus_Type=ME1200ConfigStatus
_Me1200IcfgStatusCopyConfigStatus_Object=MibScalar
me1200IcfgStatusCopyConfigStatus=_Me1200IcfgStatusCopyConfigStatus_Object((1,3,6,1,4,1,9,9,815,1,101,1,3,3,1),_Me1200IcfgStatusCopyConfigStatus_Type())
me1200IcfgStatusCopyConfigStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:me1200IcfgStatusCopyConfigStatus.setStatus(_A)
_Me1200IcfgControl_ObjectIdentity=ObjectIdentity
me1200IcfgControl=_Me1200IcfgControl_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,101,1,4))
_Me1200IcfgControlGlobals_ObjectIdentity=ObjectIdentity
me1200IcfgControlGlobals=_Me1200IcfgControlGlobals_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,101,1,4,1))
_Me1200IcfgControlGlobalsReloadDefault_Type=ME1200ReloadDefault
_Me1200IcfgControlGlobalsReloadDefault_Object=MibScalar
me1200IcfgControlGlobalsReloadDefault=_Me1200IcfgControlGlobalsReloadDefault_Object((1,3,6,1,4,1,9,9,815,1,101,1,4,1,1),_Me1200IcfgControlGlobalsReloadDefault_Type())
me1200IcfgControlGlobalsReloadDefault.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200IcfgControlGlobalsReloadDefault.setStatus(_A)
class _Me1200IcfgControlGlobalsDeleteFile_Type(ME1200DisplayString):subtypeSpec=ME1200DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_Me1200IcfgControlGlobalsDeleteFile_Type.__name__=_D
_Me1200IcfgControlGlobalsDeleteFile_Object=MibScalar
me1200IcfgControlGlobalsDeleteFile=_Me1200IcfgControlGlobalsDeleteFile_Object((1,3,6,1,4,1,9,9,815,1,101,1,4,1,2),_Me1200IcfgControlGlobalsDeleteFile_Type())
me1200IcfgControlGlobalsDeleteFile.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200IcfgControlGlobalsDeleteFile.setStatus(_A)
_Me1200IcfgControlCopyConfig_ObjectIdentity=ObjectIdentity
me1200IcfgControlCopyConfig=_Me1200IcfgControlCopyConfig_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,101,1,4,2))
_Me1200IcfgControlCopyConfigCopy_Type=TruthValue
_Me1200IcfgControlCopyConfigCopy_Object=MibScalar
me1200IcfgControlCopyConfigCopy=_Me1200IcfgControlCopyConfigCopy_Object((1,3,6,1,4,1,9,9,815,1,101,1,4,2,1),_Me1200IcfgControlCopyConfigCopy_Type())
me1200IcfgControlCopyConfigCopy.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200IcfgControlCopyConfigCopy.setStatus(_A)
_Me1200IcfgControlCopyConfigSourceConfigType_Type=ME1200ConfigType
_Me1200IcfgControlCopyConfigSourceConfigType_Object=MibScalar
me1200IcfgControlCopyConfigSourceConfigType=_Me1200IcfgControlCopyConfigSourceConfigType_Object((1,3,6,1,4,1,9,9,815,1,101,1,4,2,2),_Me1200IcfgControlCopyConfigSourceConfigType_Type())
me1200IcfgControlCopyConfigSourceConfigType.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200IcfgControlCopyConfigSourceConfigType.setStatus(_A)
class _Me1200IcfgControlCopyConfigSourceConfigFile_Type(ME1200DisplayString):subtypeSpec=ME1200DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_Me1200IcfgControlCopyConfigSourceConfigFile_Type.__name__=_D
_Me1200IcfgControlCopyConfigSourceConfigFile_Object=MibScalar
me1200IcfgControlCopyConfigSourceConfigFile=_Me1200IcfgControlCopyConfigSourceConfigFile_Object((1,3,6,1,4,1,9,9,815,1,101,1,4,2,3),_Me1200IcfgControlCopyConfigSourceConfigFile_Type())
me1200IcfgControlCopyConfigSourceConfigFile.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200IcfgControlCopyConfigSourceConfigFile.setStatus(_A)
_Me1200IcfgControlCopyConfigDestinationConfigType_Type=ME1200ConfigType
_Me1200IcfgControlCopyConfigDestinationConfigType_Object=MibScalar
me1200IcfgControlCopyConfigDestinationConfigType=_Me1200IcfgControlCopyConfigDestinationConfigType_Object((1,3,6,1,4,1,9,9,815,1,101,1,4,2,4),_Me1200IcfgControlCopyConfigDestinationConfigType_Type())
me1200IcfgControlCopyConfigDestinationConfigType.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200IcfgControlCopyConfigDestinationConfigType.setStatus(_A)
class _Me1200IcfgControlCopyConfigDestinationConfigFile_Type(ME1200DisplayString):subtypeSpec=ME1200DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_Me1200IcfgControlCopyConfigDestinationConfigFile_Type.__name__=_D
_Me1200IcfgControlCopyConfigDestinationConfigFile_Object=MibScalar
me1200IcfgControlCopyConfigDestinationConfigFile=_Me1200IcfgControlCopyConfigDestinationConfigFile_Object((1,3,6,1,4,1,9,9,815,1,101,1,4,2,5),_Me1200IcfgControlCopyConfigDestinationConfigFile_Type())
me1200IcfgControlCopyConfigDestinationConfigFile.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200IcfgControlCopyConfigDestinationConfigFile.setStatus(_A)
_Me1200IcfgControlCopyConfigMerge_Type=TruthValue
_Me1200IcfgControlCopyConfigMerge_Object=MibScalar
me1200IcfgControlCopyConfigMerge=_Me1200IcfgControlCopyConfigMerge_Object((1,3,6,1,4,1,9,9,815,1,101,1,4,2,6),_Me1200IcfgControlCopyConfigMerge_Type())
me1200IcfgControlCopyConfigMerge.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200IcfgControlCopyConfigMerge.setStatus(_A)
_Me1200IcfgMIBConformance_ObjectIdentity=ObjectIdentity
me1200IcfgMIBConformance=_Me1200IcfgMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,101,2))
_Me1200IcfgMIBCompliances_ObjectIdentity=ObjectIdentity
me1200IcfgMIBCompliances=_Me1200IcfgMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,101,2,1))
_Me1200IcfgMIBGroups_ObjectIdentity=ObjectIdentity
me1200IcfgMIBGroups=_Me1200IcfgMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,101,2,2))
me1200IcfgStatusFileStatisticsInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,815,1,101,2,2,1))
me1200IcfgStatusFileStatisticsInfoGroup.setObjects(*((_B,_I),(_B,_J)))
if mibBuilder.loadTexts:me1200IcfgStatusFileStatisticsInfoGroup.setStatus(_A)
me1200IcfgStatusFileTableInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,815,1,101,2,2,2))
me1200IcfgStatusFileTableInfoGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:me1200IcfgStatusFileTableInfoGroup.setStatus(_A)
me1200IcfgStatusCopyConfigInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,815,1,101,2,2,3))
me1200IcfgStatusCopyConfigInfoGroup.setObjects((_B,_O))
if mibBuilder.loadTexts:me1200IcfgStatusCopyConfigInfoGroup.setStatus(_A)
me1200IcfgControlGlobalsInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,815,1,101,2,2,4))
me1200IcfgControlGlobalsInfoGroup.setObjects(*((_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:me1200IcfgControlGlobalsInfoGroup.setStatus(_A)
me1200IcfgControlCopyConfigInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,815,1,101,2,2,5))
me1200IcfgControlCopyConfigInfoGroup.setObjects(*((_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:me1200IcfgControlCopyConfigInfoGroup.setStatus(_A)
me1200IcfgMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,815,1,101,2,1,1))
me1200IcfgMIBCompliance.setObjects(*((_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:me1200IcfgMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ME1200ConfigStatus':ME1200ConfigStatus,'ME1200ConfigType':ME1200ConfigType,'ME1200ReloadDefault':ME1200ReloadDefault,'me1200IcfgMIB':me1200IcfgMIB,'me1200IcfgMIBObjects':me1200IcfgMIBObjects,'me1200IcfgStatus':me1200IcfgStatus,'me1200IcfgStatusFileStatistics':me1200IcfgStatusFileStatistics,_I:me1200IcfgStatusFileStatisticsNumberOfFiles,_J:me1200IcfgStatusFileStatisticsTotalBytes,'me1200IcfgStatusFileTable':me1200IcfgStatusFileTable,'me1200IcfgStatusFileEntry':me1200IcfgStatusFileEntry,_H:me1200IcfgStatusFileFileNo,_K:me1200IcfgStatusFileFileName,_L:me1200IcfgStatusFileBytes,_M:me1200IcfgStatusFileModifiedTime,_N:me1200IcfgStatusFileAttribute,'me1200IcfgStatusCopyConfig':me1200IcfgStatusCopyConfig,_O:me1200IcfgStatusCopyConfigStatus,'me1200IcfgControl':me1200IcfgControl,'me1200IcfgControlGlobals':me1200IcfgControlGlobals,_P:me1200IcfgControlGlobalsReloadDefault,_Q:me1200IcfgControlGlobalsDeleteFile,'me1200IcfgControlCopyConfig':me1200IcfgControlCopyConfig,_R:me1200IcfgControlCopyConfigCopy,_S:me1200IcfgControlCopyConfigSourceConfigType,_T:me1200IcfgControlCopyConfigSourceConfigFile,_U:me1200IcfgControlCopyConfigDestinationConfigType,_V:me1200IcfgControlCopyConfigDestinationConfigFile,_W:me1200IcfgControlCopyConfigMerge,'me1200IcfgMIBConformance':me1200IcfgMIBConformance,'me1200IcfgMIBCompliances':me1200IcfgMIBCompliances,'me1200IcfgMIBCompliance':me1200IcfgMIBCompliance,'me1200IcfgMIBGroups':me1200IcfgMIBGroups,_X:me1200IcfgStatusFileStatisticsInfoGroup,_Y:me1200IcfgStatusFileTableInfoGroup,_Z:me1200IcfgStatusCopyConfigInfoGroup,_a:me1200IcfgControlGlobalsInfoGroup,_b:me1200IcfgControlCopyConfigInfoGroup})