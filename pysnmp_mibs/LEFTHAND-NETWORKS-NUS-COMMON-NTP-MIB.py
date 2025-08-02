_E='read-create'
_D='ntpIndex'
_C='LEFTHAND-NETWORKS-NUS-COMMON-NTP-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lhnModules,=mibBuilder.importSymbols('LEFTHAND-NETWORKS-GLOBAL-REG','lhnModules')
lhnNusCommonNTP,=mibBuilder.importSymbols('LEFTHAND-NETWORKS-NUS-COMMON-MIB','lhnNusCommonNTP')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
lhnNusCommonNTPModule=ModuleIdentity((1,3,6,1,4,1,9804,1,1,7))
_NtpCount_Type=Integer32
_NtpCount_Object=MibScalar
ntpCount=_NtpCount_Object((1,3,6,1,4,1,9804,3,1,1,2,5,1),_NtpCount_Type())
ntpCount.setMaxAccess('read-only')
if mibBuilder.loadTexts:ntpCount.setStatus(_A)
_NtpTable_Object=MibTable
ntpTable=_NtpTable_Object((1,3,6,1,4,1,9804,3,1,1,2,5,2))
if mibBuilder.loadTexts:ntpTable.setStatus(_A)
_NtpEntry_Object=MibTableRow
ntpEntry=_NtpEntry_Object((1,3,6,1,4,1,9804,3,1,1,2,5,2,1))
ntpEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:ntpEntry.setStatus(_A)
_NtpIndex_Type=Integer32
_NtpIndex_Object=MibTableColumn
ntpIndex=_NtpIndex_Object((1,3,6,1,4,1,9804,3,1,1,2,5,2,1,1),_NtpIndex_Type())
ntpIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ntpIndex.setStatus(_A)
_NtpPreferred_Type=TruthValue
_NtpPreferred_Object=MibTableColumn
ntpPreferred=_NtpPreferred_Object((1,3,6,1,4,1,9804,3,1,1,2,5,2,1,2),_NtpPreferred_Type())
ntpPreferred.setMaxAccess(_B)
if mibBuilder.loadTexts:ntpPreferred.setStatus(_A)
_NtpServer_Type=OctetString
_NtpServer_Object=MibTableColumn
ntpServer=_NtpServer_Object((1,3,6,1,4,1,9804,3,1,1,2,5,2,1,3),_NtpServer_Type())
ntpServer.setMaxAccess(_B)
if mibBuilder.loadTexts:ntpServer.setStatus(_A)
_NtpRowStatus_Type=RowStatus
_NtpRowStatus_Object=MibTableColumn
ntpRowStatus=_NtpRowStatus_Object((1,3,6,1,4,1,9804,3,1,1,2,5,2,1,4),_NtpRowStatus_Type())
ntpRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:ntpRowStatus.setStatus(_A)
_NtpStart_Type=TruthValue
_NtpStart_Object=MibScalar
ntpStart=_NtpStart_Object((1,3,6,1,4,1,9804,3,1,1,2,5,3),_NtpStart_Type())
ntpStart.setMaxAccess(_B)
if mibBuilder.loadTexts:ntpStart.setStatus(_A)
_NtpStop_Type=TruthValue
_NtpStop_Object=MibScalar
ntpStop=_NtpStop_Object((1,3,6,1,4,1,9804,3,1,1,2,5,4),_NtpStop_Type())
ntpStop.setMaxAccess(_B)
if mibBuilder.loadTexts:ntpStop.setStatus(_A)
_NtpRestart_Type=TruthValue
_NtpRestart_Object=MibScalar
ntpRestart=_NtpRestart_Object((1,3,6,1,4,1,9804,3,1,1,2,5,5),_NtpRestart_Type())
ntpRestart.setMaxAccess(_B)
if mibBuilder.loadTexts:ntpRestart.setStatus(_A)
_NtpCheck_Type=TruthValue
_NtpCheck_Object=MibScalar
ntpCheck=_NtpCheck_Object((1,3,6,1,4,1,9804,3,1,1,2,5,6),_NtpCheck_Type())
ntpCheck.setMaxAccess(_B)
if mibBuilder.loadTexts:ntpCheck.setStatus(_A)
_TimeGMTTime_Type=OctetString
_TimeGMTTime_Object=MibScalar
timeGMTTime=_TimeGMTTime_Object((1,3,6,1,4,1,9804,3,1,1,2,5,7),_TimeGMTTime_Type())
timeGMTTime.setMaxAccess(_B)
if mibBuilder.loadTexts:timeGMTTime.setStatus(_A)
_TimeTimeZone_Type=OctetString
_TimeTimeZone_Object=MibScalar
timeTimeZone=_TimeTimeZone_Object((1,3,6,1,4,1,9804,3,1,1,2,5,8),_TimeTimeZone_Type())
timeTimeZone.setMaxAccess(_B)
if mibBuilder.loadTexts:timeTimeZone.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'lhnNusCommonNTPModule':lhnNusCommonNTPModule,'ntpCount':ntpCount,'ntpTable':ntpTable,'ntpEntry':ntpEntry,_D:ntpIndex,'ntpPreferred':ntpPreferred,'ntpServer':ntpServer,'ntpRowStatus':ntpRowStatus,'ntpStart':ntpStart,'ntpStop':ntpStop,'ntpRestart':ntpRestart,'ntpCheck':ntpCheck,'timeGMTTime':timeGMTTime,'timeTimeZone':timeTimeZone})