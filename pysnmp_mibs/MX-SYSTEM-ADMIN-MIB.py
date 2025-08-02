_P='sysAdminGroupVer1'
_O='sysAdminAppMode'
_N='sysAdminLastDownloadSoftware'
_M='sysAdminLastCheckRom'
_L='sysAdminLastCheckRam'
_K='sysAdminDefaultSettingsEnable'
_J='sysAdminCommand'
_I='sysAdminDownloadConfigFileStatus'
_H='read-write'
_G='MxEnableState'
_F='success'
_E='fail'
_D='read-only'
_C='Integer32'
_B='MX-SYSTEM-ADMIN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mediatrixAdmin,=mibBuilder.importSymbols('MX-SMI','mediatrixAdmin')
MxEnableState,=mibBuilder.importSymbols('MX-TC',_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
sysAdminMIB=ModuleIdentity((1,3,6,1,4,1,4935,5,1))
if mibBuilder.loadTexts:sysAdminMIB.setRevisions(('2006-03-06 00:00','2005-04-20 00:00','2004-02-12 00:00','1903-12-02 00:00'))
_SysAdminMIBObjects_ObjectIdentity=ObjectIdentity
sysAdminMIBObjects=_SysAdminMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,5,1,1))
class _SysAdminCommand_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('noOp',0),('checkRam',1),('checkRom',2),('downloadSoftware',3),('resetStats',4),('setConfigSourcesStatic',5),('updateConfiguration',6)))
_SysAdminCommand_Type.__name__=_C
_SysAdminCommand_Object=MibScalar
sysAdminCommand=_SysAdminCommand_Object((1,3,6,1,4,1,4935,5,1,1,1),_SysAdminCommand_Type())
sysAdminCommand.setMaxAccess(_H)
if mibBuilder.loadTexts:sysAdminCommand.setStatus(_A)
class _SysAdminDefaultSettingsEnable_Type(MxEnableState):defaultValue=1
_SysAdminDefaultSettingsEnable_Type.__name__=_G
_SysAdminDefaultSettingsEnable_Object=MibScalar
sysAdminDefaultSettingsEnable=_SysAdminDefaultSettingsEnable_Object((1,3,6,1,4,1,4935,5,1,1,5),_SysAdminDefaultSettingsEnable_Type())
sysAdminDefaultSettingsEnable.setMaxAccess(_H)
if mibBuilder.loadTexts:sysAdminDefaultSettingsEnable.setStatus(_A)
class _SysAdminLastCheckRam_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('notTested',0),(_E,1),(_F,2)))
_SysAdminLastCheckRam_Type.__name__=_C
_SysAdminLastCheckRam_Object=MibScalar
sysAdminLastCheckRam=_SysAdminLastCheckRam_Object((1,3,6,1,4,1,4935,5,1,1,11),_SysAdminLastCheckRam_Type())
sysAdminLastCheckRam.setMaxAccess(_D)
if mibBuilder.loadTexts:sysAdminLastCheckRam.setStatus(_A)
class _SysAdminLastCheckRom_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_SysAdminLastCheckRom_Type.__name__=_C
_SysAdminLastCheckRom_Object=MibScalar
sysAdminLastCheckRom=_SysAdminLastCheckRom_Object((1,3,6,1,4,1,4935,5,1,1,12),_SysAdminLastCheckRom_Type())
sysAdminLastCheckRom.setMaxAccess(_D)
if mibBuilder.loadTexts:sysAdminLastCheckRom.setStatus(_A)
class _SysAdminLastDownloadSoftware_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_SysAdminLastDownloadSoftware_Type.__name__=_C
_SysAdminLastDownloadSoftware_Object=MibScalar
sysAdminLastDownloadSoftware=_SysAdminLastDownloadSoftware_Object((1,3,6,1,4,1,4935,5,1,1,14),_SysAdminLastDownloadSoftware_Type())
sysAdminLastDownloadSoftware.setMaxAccess(_D)
if mibBuilder.loadTexts:sysAdminLastDownloadSoftware.setStatus(_A)
class _SysAdminDownloadConfigFileStatus_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('idle',0),(_E,1),(_F,2),('inProgress',3),('listening',4)))
_SysAdminDownloadConfigFileStatus_Type.__name__=_C
_SysAdminDownloadConfigFileStatus_Object=MibScalar
sysAdminDownloadConfigFileStatus=_SysAdminDownloadConfigFileStatus_Object((1,3,6,1,4,1,4935,5,1,1,30),_SysAdminDownloadConfigFileStatus_Type())
sysAdminDownloadConfigFileStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:sysAdminDownloadConfigFileStatus.setStatus(_A)
class _SysAdminAppMode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('normal',0),('recovery',1)))
_SysAdminAppMode_Type.__name__=_C
_SysAdminAppMode_Object=MibScalar
sysAdminAppMode=_SysAdminAppMode_Object((1,3,6,1,4,1,4935,5,1,1,50),_SysAdminAppMode_Type())
sysAdminAppMode.setMaxAccess(_D)
if mibBuilder.loadTexts:sysAdminAppMode.setStatus(_A)
_SysAdminConformance_ObjectIdentity=ObjectIdentity
sysAdminConformance=_SysAdminConformance_ObjectIdentity((1,3,6,1,4,1,4935,5,1,2))
_SysAdminCompliances_ObjectIdentity=ObjectIdentity
sysAdminCompliances=_SysAdminCompliances_ObjectIdentity((1,3,6,1,4,1,4935,5,1,2,1))
_SysAdminGroups_ObjectIdentity=ObjectIdentity
sysAdminGroups=_SysAdminGroups_ObjectIdentity((1,3,6,1,4,1,4935,5,1,2,2))
sysAdminGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,5,1,2,2,1))
sysAdminGroupVer1.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:sysAdminGroupVer1.setStatus(_A)
sysAdminComplVer1=ModuleCompliance((1,3,6,1,4,1,4935,5,1,2,1,1))
sysAdminComplVer1.setObjects((_B,_P))
if mibBuilder.loadTexts:sysAdminComplVer1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'sysAdminMIB':sysAdminMIB,'sysAdminMIBObjects':sysAdminMIBObjects,_J:sysAdminCommand,_K:sysAdminDefaultSettingsEnable,_L:sysAdminLastCheckRam,_M:sysAdminLastCheckRom,_N:sysAdminLastDownloadSoftware,_I:sysAdminDownloadConfigFileStatus,_O:sysAdminAppMode,'sysAdminConformance':sysAdminConformance,'sysAdminCompliances':sysAdminCompliances,'sysAdminComplVer1':sysAdminComplVer1,'sysAdminGroups':sysAdminGroups,_P:sysAdminGroupVer1})