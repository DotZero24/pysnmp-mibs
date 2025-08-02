_E='Integer32'
_D='obsolete'
_C='write-only'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
local,=mibBuilder.importSymbols('CISCO-SMI','local')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Lsystem_ObjectIdentity=ObjectIdentity
lsystem=_Lsystem_ObjectIdentity((1,3,6,1,4,1,9,2,1))
_RomId_Type=DisplayString
_RomId_Object=MibScalar
romId=_RomId_Object((1,3,6,1,4,1,9,2,1,1),_RomId_Type())
romId.setMaxAccess(_B)
if mibBuilder.loadTexts:romId.setStatus(_A)
_WhyReload_Type=DisplayString
_WhyReload_Object=MibScalar
whyReload=_WhyReload_Object((1,3,6,1,4,1,9,2,1,2),_WhyReload_Type())
whyReload.setMaxAccess(_B)
if mibBuilder.loadTexts:whyReload.setStatus(_A)
_HostName_Type=DisplayString
_HostName_Object=MibScalar
hostName=_HostName_Object((1,3,6,1,4,1,9,2,1,3),_HostName_Type())
hostName.setMaxAccess(_B)
if mibBuilder.loadTexts:hostName.setStatus(_A)
_DomainName_Type=DisplayString
_DomainName_Object=MibScalar
domainName=_DomainName_Object((1,3,6,1,4,1,9,2,1,4),_DomainName_Type())
domainName.setMaxAccess(_B)
if mibBuilder.loadTexts:domainName.setStatus(_A)
_AuthAddr_Type=IpAddress
_AuthAddr_Object=MibScalar
authAddr=_AuthAddr_Object((1,3,6,1,4,1,9,2,1,5),_AuthAddr_Type())
authAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:authAddr.setStatus(_A)
_BootHost_Type=IpAddress
_BootHost_Object=MibScalar
bootHost=_BootHost_Object((1,3,6,1,4,1,9,2,1,6),_BootHost_Type())
bootHost.setMaxAccess(_B)
if mibBuilder.loadTexts:bootHost.setStatus(_A)
_NetConfigAddr_Type=IpAddress
_NetConfigAddr_Object=MibScalar
netConfigAddr=_NetConfigAddr_Object((1,3,6,1,4,1,9,2,1,48),_NetConfigAddr_Type())
netConfigAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:netConfigAddr.setStatus(_A)
_NetConfigName_Type=DisplayString
_NetConfigName_Object=MibScalar
netConfigName=_NetConfigName_Object((1,3,6,1,4,1,9,2,1,49),_NetConfigName_Type())
netConfigName.setMaxAccess(_B)
if mibBuilder.loadTexts:netConfigName.setStatus(_A)
_NetConfigSet_Type=DisplayString
_NetConfigSet_Object=MibScalar
netConfigSet=_NetConfigSet_Object((1,3,6,1,4,1,9,2,1,50),_NetConfigSet_Type())
netConfigSet.setMaxAccess(_C)
if mibBuilder.loadTexts:netConfigSet.setStatus(_A)
_HostConfigAddr_Type=IpAddress
_HostConfigAddr_Object=MibScalar
hostConfigAddr=_HostConfigAddr_Object((1,3,6,1,4,1,9,2,1,51),_HostConfigAddr_Type())
hostConfigAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hostConfigAddr.setStatus(_D)
_HostConfigName_Type=DisplayString
_HostConfigName_Object=MibScalar
hostConfigName=_HostConfigName_Object((1,3,6,1,4,1,9,2,1,52),_HostConfigName_Type())
hostConfigName.setMaxAccess(_B)
if mibBuilder.loadTexts:hostConfigName.setStatus(_D)
_HostConfigSet_Type=DisplayString
_HostConfigSet_Object=MibScalar
hostConfigSet=_HostConfigSet_Object((1,3,6,1,4,1,9,2,1,53),_HostConfigSet_Type())
hostConfigSet.setMaxAccess(_C)
if mibBuilder.loadTexts:hostConfigSet.setStatus(_D)
_WriteMem_Type=Integer32
_WriteMem_Object=MibScalar
writeMem=_WriteMem_Object((1,3,6,1,4,1,9,2,1,54),_WriteMem_Type())
writeMem.setMaxAccess(_C)
if mibBuilder.loadTexts:writeMem.setStatus(_A)
_WriteNet_Type=DisplayString
_WriteNet_Object=MibScalar
writeNet=_WriteNet_Object((1,3,6,1,4,1,9,2,1,55),_WriteNet_Type())
writeNet.setMaxAccess(_C)
if mibBuilder.loadTexts:writeNet.setStatus(_A)
_CiscoContactInfo_Type=DisplayString
_CiscoContactInfo_Object=MibScalar
ciscoContactInfo=_CiscoContactInfo_Object((1,3,6,1,4,1,9,2,1,61),_CiscoContactInfo_Type())
ciscoContactInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoContactInfo.setStatus(_A)
_NetConfigProto_Type=Integer32
_NetConfigProto_Object=MibScalar
netConfigProto=_NetConfigProto_Object((1,3,6,1,4,1,9,2,1,70),_NetConfigProto_Type())
netConfigProto.setMaxAccess(_B)
if mibBuilder.loadTexts:netConfigProto.setStatus(_A)
_HostConfigProto_Type=Integer32
_HostConfigProto_Object=MibScalar
hostConfigProto=_HostConfigProto_Object((1,3,6,1,4,1,9,2,1,71),_HostConfigProto_Type())
hostConfigProto.setMaxAccess(_B)
if mibBuilder.loadTexts:hostConfigProto.setStatus(_A)
_SysConfigAddr_Type=IpAddress
_SysConfigAddr_Object=MibScalar
sysConfigAddr=_SysConfigAddr_Object((1,3,6,1,4,1,9,2,1,72),_SysConfigAddr_Type())
sysConfigAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:sysConfigAddr.setStatus(_A)
_SysConfigName_Type=DisplayString
_SysConfigName_Object=MibScalar
sysConfigName=_SysConfigName_Object((1,3,6,1,4,1,9,2,1,73),_SysConfigName_Type())
sysConfigName.setMaxAccess(_B)
if mibBuilder.loadTexts:sysConfigName.setStatus(_A)
class _SysConfigProto_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('tftp',1),('rom',2),('flash',3)))
_SysConfigProto_Type.__name__=_E
_SysConfigProto_Object=MibScalar
sysConfigProto=_SysConfigProto_Object((1,3,6,1,4,1,9,2,1,74),_SysConfigProto_Type())
sysConfigProto.setMaxAccess(_B)
if mibBuilder.loadTexts:sysConfigProto.setStatus(_A)
_SysClearARP_Type=Integer32
_SysClearARP_Object=MibScalar
sysClearARP=_SysClearARP_Object((1,3,6,1,4,1,9,2,1,75),_SysClearARP_Type())
sysClearARP.setMaxAccess(_C)
if mibBuilder.loadTexts:sysClearARP.setStatus(_A)
_SysClearInt_Type=Integer32
_SysClearInt_Object=MibScalar
sysClearInt=_SysClearInt_Object((1,3,6,1,4,1,9,2,1,76),_SysClearInt_Type())
sysClearInt.setMaxAccess(_C)
if mibBuilder.loadTexts:sysClearInt.setStatus(_A)
mibBuilder.exportSymbols('OLD-CISCO-SYSTEM-MIB',**{'lsystem':lsystem,'romId':romId,'whyReload':whyReload,'hostName':hostName,'domainName':domainName,'authAddr':authAddr,'bootHost':bootHost,'netConfigAddr':netConfigAddr,'netConfigName':netConfigName,'netConfigSet':netConfigSet,'hostConfigAddr':hostConfigAddr,'hostConfigName':hostConfigName,'hostConfigSet':hostConfigSet,'writeMem':writeMem,'writeNet':writeNet,'ciscoContactInfo':ciscoContactInfo,'netConfigProto':netConfigProto,'hostConfigProto':hostConfigProto,'sysConfigAddr':sysConfigAddr,'sysConfigName':sysConfigName,'sysConfigProto':sysConfigProto,'sysClearARP':sysClearARP,'sysClearInt':sysClearInt})