_c='etsysR2MgmtBaseGroupV2'
_b='etsysR2MgmtBaseGroup'
_a='etsysR2MgmtVlan'
_Z='etsysR2MgmtUplineDumpMode'
_Y='etsysR2MgmtCrashUploadDirectory'
_X='etsysR2MgmtCrashUploadServerIP'
_W='etsysR2MgmtCrashUploadUseBootp'
_V='etsysR2MgmtErrLogInfo'
_U='etsysR2MgmtErrLogResetNumber'
_T='etsysR2MgmtErrLogTimeStamp'
_S='etsysR2MgmtErrLogNumEntries'
_R='etsysR2MgmtUnsolicitedResets'
_Q='etsysR2MgmtResets'
_P='etsysR2MgmtPowerups'
_O='deprecated'
_N='SnmpAdminString'
_M='OctetString'
_L='etsysR2MgmtLoaderGroup'
_K='etsysR2MgmtErrLogGroup'
_J='etsysR2MgmtCountersGroup'
_I='etsysR2MgmtTelnetInterface'
_H='etsysR2MgmtWEBInterface'
_G='etsysR2MgmtMemorySize'
_F='etsysR2MgmtErrLogIndex'
_E='Integer32'
_D='read-write'
_C='read-only'
_B='current'
_A='ENTERASYS-R2MGMT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_M,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
etsysModules,=mibBuilder.importSymbols('ENTERASYS-MIB-NAMES','etsysModules')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_N)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
enterasysR2MgmtMIB=ModuleIdentity((1,3,6,1,4,1,5624,1,2,11))
if mibBuilder.loadTexts:enterasysR2MgmtMIB.setRevisions(('2004-07-08 15:30','2002-03-07 19:35','2001-06-26 17:30'))
_EtsysR2MgmtObjects_ObjectIdentity=ObjectIdentity
etsysR2MgmtObjects=_EtsysR2MgmtObjects_ObjectIdentity((1,3,6,1,4,1,5624,1,2,11,1))
_EtsysR2MgmtParams_ObjectIdentity=ObjectIdentity
etsysR2MgmtParams=_EtsysR2MgmtParams_ObjectIdentity((1,3,6,1,4,1,5624,1,2,11,1,1))
_EtsysR2MgmtMemorySize_Type=Integer32
_EtsysR2MgmtMemorySize_Object=MibScalar
etsysR2MgmtMemorySize=_EtsysR2MgmtMemorySize_Object((1,3,6,1,4,1,5624,1,2,11,1,1,1),_EtsysR2MgmtMemorySize_Type())
etsysR2MgmtMemorySize.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysR2MgmtMemorySize.setStatus(_B)
_EtsysR2MgmtWEBInterface_Type=EnabledStatus
_EtsysR2MgmtWEBInterface_Object=MibScalar
etsysR2MgmtWEBInterface=_EtsysR2MgmtWEBInterface_Object((1,3,6,1,4,1,5624,1,2,11,1,1,2),_EtsysR2MgmtWEBInterface_Type())
etsysR2MgmtWEBInterface.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysR2MgmtWEBInterface.setStatus(_B)
_EtsysR2MgmtTelnetInterface_Type=EnabledStatus
_EtsysR2MgmtTelnetInterface_Object=MibScalar
etsysR2MgmtTelnetInterface=_EtsysR2MgmtTelnetInterface_Object((1,3,6,1,4,1,5624,1,2,11,1,1,3),_EtsysR2MgmtTelnetInterface_Type())
etsysR2MgmtTelnetInterface.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysR2MgmtTelnetInterface.setStatus(_B)
class _EtsysR2MgmtVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_EtsysR2MgmtVlan_Type.__name__=_E
_EtsysR2MgmtVlan_Object=MibScalar
etsysR2MgmtVlan=_EtsysR2MgmtVlan_Object((1,3,6,1,4,1,5624,1,2,11,1,1,4),_EtsysR2MgmtVlan_Type())
etsysR2MgmtVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysR2MgmtVlan.setStatus(_B)
_EtsysR2MgmtCounters_ObjectIdentity=ObjectIdentity
etsysR2MgmtCounters=_EtsysR2MgmtCounters_ObjectIdentity((1,3,6,1,4,1,5624,1,2,11,1,2))
_EtsysR2MgmtPowerups_Type=Counter32
_EtsysR2MgmtPowerups_Object=MibScalar
etsysR2MgmtPowerups=_EtsysR2MgmtPowerups_Object((1,3,6,1,4,1,5624,1,2,11,1,2,1),_EtsysR2MgmtPowerups_Type())
etsysR2MgmtPowerups.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysR2MgmtPowerups.setStatus(_B)
_EtsysR2MgmtResets_Type=Counter32
_EtsysR2MgmtResets_Object=MibScalar
etsysR2MgmtResets=_EtsysR2MgmtResets_Object((1,3,6,1,4,1,5624,1,2,11,1,2,2),_EtsysR2MgmtResets_Type())
etsysR2MgmtResets.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysR2MgmtResets.setStatus(_B)
_EtsysR2MgmtUnsolicitedResets_Type=Counter32
_EtsysR2MgmtUnsolicitedResets_Object=MibScalar
etsysR2MgmtUnsolicitedResets=_EtsysR2MgmtUnsolicitedResets_Object((1,3,6,1,4,1,5624,1,2,11,1,2,3),_EtsysR2MgmtUnsolicitedResets_Type())
etsysR2MgmtUnsolicitedResets.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysR2MgmtUnsolicitedResets.setStatus(_B)
_EtsysR2MgmtErrorLog_ObjectIdentity=ObjectIdentity
etsysR2MgmtErrorLog=_EtsysR2MgmtErrorLog_ObjectIdentity((1,3,6,1,4,1,5624,1,2,11,1,3))
class _EtsysR2MgmtErrLogNumEntries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_EtsysR2MgmtErrLogNumEntries_Type.__name__=_E
_EtsysR2MgmtErrLogNumEntries_Object=MibScalar
etsysR2MgmtErrLogNumEntries=_EtsysR2MgmtErrLogNumEntries_Object((1,3,6,1,4,1,5624,1,2,11,1,3,1),_EtsysR2MgmtErrLogNumEntries_Type())
etsysR2MgmtErrLogNumEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysR2MgmtErrLogNumEntries.setStatus(_B)
_EtsysR2MgmtErrLogTable_Object=MibTable
etsysR2MgmtErrLogTable=_EtsysR2MgmtErrLogTable_Object((1,3,6,1,4,1,5624,1,2,11,1,3,2))
if mibBuilder.loadTexts:etsysR2MgmtErrLogTable.setStatus(_B)
_EtsysR2MgmtErrLogEntry_Object=MibTableRow
etsysR2MgmtErrLogEntry=_EtsysR2MgmtErrLogEntry_Object((1,3,6,1,4,1,5624,1,2,11,1,3,2,1))
etsysR2MgmtErrLogEntry.setIndexNames((0,_A,_F))
if mibBuilder.loadTexts:etsysR2MgmtErrLogEntry.setStatus(_B)
class _EtsysR2MgmtErrLogIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_EtsysR2MgmtErrLogIndex_Type.__name__=_E
_EtsysR2MgmtErrLogIndex_Object=MibTableColumn
etsysR2MgmtErrLogIndex=_EtsysR2MgmtErrLogIndex_Object((1,3,6,1,4,1,5624,1,2,11,1,3,2,1,1),_EtsysR2MgmtErrLogIndex_Type())
etsysR2MgmtErrLogIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysR2MgmtErrLogIndex.setStatus(_B)
_EtsysR2MgmtErrLogTimeStamp_Type=TimeTicks
_EtsysR2MgmtErrLogTimeStamp_Object=MibTableColumn
etsysR2MgmtErrLogTimeStamp=_EtsysR2MgmtErrLogTimeStamp_Object((1,3,6,1,4,1,5624,1,2,11,1,3,2,1,2),_EtsysR2MgmtErrLogTimeStamp_Type())
etsysR2MgmtErrLogTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysR2MgmtErrLogTimeStamp.setStatus(_B)
class _EtsysR2MgmtErrLogResetNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_EtsysR2MgmtErrLogResetNumber_Type.__name__=_E
_EtsysR2MgmtErrLogResetNumber_Object=MibTableColumn
etsysR2MgmtErrLogResetNumber=_EtsysR2MgmtErrLogResetNumber_Object((1,3,6,1,4,1,5624,1,2,11,1,3,2,1,3),_EtsysR2MgmtErrLogResetNumber_Type())
etsysR2MgmtErrLogResetNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysR2MgmtErrLogResetNumber.setStatus(_B)
class _EtsysR2MgmtErrLogInfo_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_EtsysR2MgmtErrLogInfo_Type.__name__=_N
_EtsysR2MgmtErrLogInfo_Object=MibTableColumn
etsysR2MgmtErrLogInfo=_EtsysR2MgmtErrLogInfo_Object((1,3,6,1,4,1,5624,1,2,11,1,3,2,1,4),_EtsysR2MgmtErrLogInfo_Type())
etsysR2MgmtErrLogInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysR2MgmtErrLogInfo.setStatus(_B)
_EtsysR2MgmtLoader_ObjectIdentity=ObjectIdentity
etsysR2MgmtLoader=_EtsysR2MgmtLoader_ObjectIdentity((1,3,6,1,4,1,5624,1,2,11,1,4))
_EtsysR2MgmtCrashUploadUseBootp_Type=TruthValue
_EtsysR2MgmtCrashUploadUseBootp_Object=MibScalar
etsysR2MgmtCrashUploadUseBootp=_EtsysR2MgmtCrashUploadUseBootp_Object((1,3,6,1,4,1,5624,1,2,11,1,4,1),_EtsysR2MgmtCrashUploadUseBootp_Type())
etsysR2MgmtCrashUploadUseBootp.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysR2MgmtCrashUploadUseBootp.setStatus(_B)
_EtsysR2MgmtCrashUploadServerIP_Type=IpAddress
_EtsysR2MgmtCrashUploadServerIP_Object=MibScalar
etsysR2MgmtCrashUploadServerIP=_EtsysR2MgmtCrashUploadServerIP_Object((1,3,6,1,4,1,5624,1,2,11,1,4,2),_EtsysR2MgmtCrashUploadServerIP_Type())
etsysR2MgmtCrashUploadServerIP.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysR2MgmtCrashUploadServerIP.setStatus(_B)
class _EtsysR2MgmtCrashUploadDirectory_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_EtsysR2MgmtCrashUploadDirectory_Type.__name__=_M
_EtsysR2MgmtCrashUploadDirectory_Object=MibScalar
etsysR2MgmtCrashUploadDirectory=_EtsysR2MgmtCrashUploadDirectory_Object((1,3,6,1,4,1,5624,1,2,11,1,4,3),_EtsysR2MgmtCrashUploadDirectory_Type())
etsysR2MgmtCrashUploadDirectory.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysR2MgmtCrashUploadDirectory.setStatus(_B)
_EtsysR2MgmtUplineDumpMode_Type=EnabledStatus
_EtsysR2MgmtUplineDumpMode_Object=MibScalar
etsysR2MgmtUplineDumpMode=_EtsysR2MgmtUplineDumpMode_Object((1,3,6,1,4,1,5624,1,2,11,1,4,4),_EtsysR2MgmtUplineDumpMode_Type())
etsysR2MgmtUplineDumpMode.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysR2MgmtUplineDumpMode.setStatus(_B)
_EtsysR2MgmtConformance_ObjectIdentity=ObjectIdentity
etsysR2MgmtConformance=_EtsysR2MgmtConformance_ObjectIdentity((1,3,6,1,4,1,5624,1,2,11,2))
_EtsysR2MgmtGroups_ObjectIdentity=ObjectIdentity
etsysR2MgmtGroups=_EtsysR2MgmtGroups_ObjectIdentity((1,3,6,1,4,1,5624,1,2,11,2,1))
_EtsysR2MgmtCompliances_ObjectIdentity=ObjectIdentity
etsysR2MgmtCompliances=_EtsysR2MgmtCompliances_ObjectIdentity((1,3,6,1,4,1,5624,1,2,11,2,2))
etsysR2MgmtBaseGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,11,2,1,1))
etsysR2MgmtBaseGroup.setObjects(*((_A,_G),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:etsysR2MgmtBaseGroup.setStatus(_O)
etsysR2MgmtCountersGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,11,2,1,2))
etsysR2MgmtCountersGroup.setObjects(*((_A,_P),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:etsysR2MgmtCountersGroup.setStatus(_B)
etsysR2MgmtErrLogGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,11,2,1,3))
etsysR2MgmtErrLogGroup.setObjects(*((_A,_S),(_A,_F),(_A,_T),(_A,_U),(_A,_V)))
if mibBuilder.loadTexts:etsysR2MgmtErrLogGroup.setStatus(_B)
etsysR2MgmtLoaderGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,11,2,1,4))
etsysR2MgmtLoaderGroup.setObjects(*((_A,_W),(_A,_X),(_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:etsysR2MgmtLoaderGroup.setStatus(_B)
etsysR2MgmtBaseGroupV2=ObjectGroup((1,3,6,1,4,1,5624,1,2,11,2,1,5))
etsysR2MgmtBaseGroupV2.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_a)))
if mibBuilder.loadTexts:etsysR2MgmtBaseGroupV2.setStatus(_B)
etsysR2MgmtCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,11,2,2,1))
etsysR2MgmtCompliance.setObjects(*((_A,_b),(_A,_J),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:etsysR2MgmtCompliance.setStatus(_O)
etsysR2MgmtComplianceV2=ModuleCompliance((1,3,6,1,4,1,5624,1,2,11,2,2,2))
etsysR2MgmtComplianceV2.setObjects(*((_A,_c),(_A,_J),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:etsysR2MgmtComplianceV2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'enterasysR2MgmtMIB':enterasysR2MgmtMIB,'etsysR2MgmtObjects':etsysR2MgmtObjects,'etsysR2MgmtParams':etsysR2MgmtParams,_G:etsysR2MgmtMemorySize,_H:etsysR2MgmtWEBInterface,_I:etsysR2MgmtTelnetInterface,_a:etsysR2MgmtVlan,'etsysR2MgmtCounters':etsysR2MgmtCounters,_P:etsysR2MgmtPowerups,_Q:etsysR2MgmtResets,_R:etsysR2MgmtUnsolicitedResets,'etsysR2MgmtErrorLog':etsysR2MgmtErrorLog,_S:etsysR2MgmtErrLogNumEntries,'etsysR2MgmtErrLogTable':etsysR2MgmtErrLogTable,'etsysR2MgmtErrLogEntry':etsysR2MgmtErrLogEntry,_F:etsysR2MgmtErrLogIndex,_T:etsysR2MgmtErrLogTimeStamp,_U:etsysR2MgmtErrLogResetNumber,_V:etsysR2MgmtErrLogInfo,'etsysR2MgmtLoader':etsysR2MgmtLoader,_W:etsysR2MgmtCrashUploadUseBootp,_X:etsysR2MgmtCrashUploadServerIP,_Y:etsysR2MgmtCrashUploadDirectory,_Z:etsysR2MgmtUplineDumpMode,'etsysR2MgmtConformance':etsysR2MgmtConformance,'etsysR2MgmtGroups':etsysR2MgmtGroups,_b:etsysR2MgmtBaseGroup,_J:etsysR2MgmtCountersGroup,_K:etsysR2MgmtErrLogGroup,_L:etsysR2MgmtLoaderGroup,_c:etsysR2MgmtBaseGroupV2,'etsysR2MgmtCompliances':etsysR2MgmtCompliances,'etsysR2MgmtCompliance':etsysR2MgmtCompliance,'etsysR2MgmtComplianceV2':etsysR2MgmtComplianceV2})