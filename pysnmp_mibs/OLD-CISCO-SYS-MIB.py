_H='read-write'
_G='obsolete'
_F='noWarning'
_E='warning'
_D='write-only'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
local,=mibBuilder.importSymbols('CISCO-SMI','local')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
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
_Ping_Type=Integer32
_Ping_Object=MibScalar
ping=_Ping_Object((1,3,6,1,4,1,9,2,1,7),_Ping_Type())
ping.setMaxAccess(_H)
if mibBuilder.loadTexts:ping.setStatus(_G)
_FreeMem_Type=Integer32
_FreeMem_Object=MibScalar
freeMem=_FreeMem_Object((1,3,6,1,4,1,9,2,1,8),_FreeMem_Type())
freeMem.setMaxAccess(_B)
if mibBuilder.loadTexts:freeMem.setStatus(_G)
_BufferElFree_Type=Integer32
_BufferElFree_Object=MibScalar
bufferElFree=_BufferElFree_Object((1,3,6,1,4,1,9,2,1,9),_BufferElFree_Type())
bufferElFree.setMaxAccess(_B)
if mibBuilder.loadTexts:bufferElFree.setStatus(_A)
_BufferElMax_Type=Integer32
_BufferElMax_Object=MibScalar
bufferElMax=_BufferElMax_Object((1,3,6,1,4,1,9,2,1,10),_BufferElMax_Type())
bufferElMax.setMaxAccess(_B)
if mibBuilder.loadTexts:bufferElMax.setStatus(_A)
_BufferElHit_Type=Integer32
_BufferElHit_Object=MibScalar
bufferElHit=_BufferElHit_Object((1,3,6,1,4,1,9,2,1,11),_BufferElHit_Type())
bufferElHit.setMaxAccess(_B)
if mibBuilder.loadTexts:bufferElHit.setStatus(_A)
_BufferElMiss_Type=Integer32
_BufferElMiss_Object=MibScalar
bufferElMiss=_BufferElMiss_Object((1,3,6,1,4,1,9,2,1,12),_BufferElMiss_Type())
bufferElMiss.setMaxAccess(_B)
if mibBuilder.loadTexts:bufferElMiss.setStatus(_A)
_BufferElCreate_Type=Integer32
_BufferElCreate_Object=MibScalar
bufferElCreate=_BufferElCreate_Object((1,3,6,1,4,1,9,2,1,13),_BufferElCreate_Type())
bufferElCreate.setMaxAccess(_B)
if mibBuilder.loadTexts:bufferElCreate.setStatus(_A)
_BufferSmSize_Type=Integer32
_BufferSmSize_Object=MibScalar
bufferSmSize=_BufferSmSize_Object((1,3,6,1,4,1,9,2,1,14),_BufferSmSize_Type())
bufferSmSize.setMaxAccess(_B)
if mibBuilder.loadTexts:bufferSmSize.setStatus(_A)
_BufferSmTotal_Type=Integer32
_BufferSmTotal_Object=MibScalar
bufferSmTotal=_BufferSmTotal_Object((1,3,6,1,4,1,9,2,1,15),_BufferSmTotal_Type())
bufferSmTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:bufferSmTotal.setStatus(_A)
_BufferSmFree_Type=Integer32
_BufferSmFree_Object=MibScalar
bufferSmFree=_BufferSmFree_Object((1,3,6,1,4,1,9,2,1,16),_BufferSmFree_Type())
bufferSmFree.setMaxAccess(_B)
if mibBuilder.loadTexts:bufferSmFree.setStatus(_A)
_BufferSmMax_Type=Integer32
_BufferSmMax_Object=MibScalar
bufferSmMax=_BufferSmMax_Object((1,3,6,1,4,1,9,2,1,17),_BufferSmMax_Type())
bufferSmMax.setMaxAccess(_B)
if mibBuilder.loadTexts:bufferSmMax.setStatus(_A)
_BufferSmHit_Type=Integer32
_BufferSmHit_Object=MibScalar
bufferSmHit=_BufferSmHit_Object((1,3,6,1,4,1,9,2,1,18),_BufferSmHit_Type())
bufferSmHit.setMaxAccess(_B)
if mibBuilder.loadTexts:bufferSmHit.setStatus(_A)
_BufferSmMiss_Type=Integer32
_BufferSmMiss_Object=MibScalar
bufferSmMiss=_BufferSmMiss_Object((1,3,6,1,4,1,9,2,1,19),_BufferSmMiss_Type())
bufferSmMiss.setMaxAccess(_B)
if mibBuilder.loadTexts:bufferSmMiss.setStatus(_A)
_BufferSmTrim_Type=Integer32
_BufferSmTrim_Object=MibScalar
bufferSmTrim=_BufferSmTrim_Object((1,3,6,1,4,1,9,2,1,20),_BufferSmTrim_Type())
bufferSmTrim.setMaxAccess(_B)
if mibBuilder.loadTexts:bufferSmTrim.setStatus(_A)
_BufferSmCreate_Type=Integer32
_BufferSmCreate_Object=MibScalar
bufferSmCreate=_BufferSmCreate_Object((1,3,6,1,4,1,9,2,1,21),_BufferSmCreate_Type())
bufferSmCreate.setMaxAccess(_B)
if mibBuilder.loadTexts:bufferSmCreate.setStatus(_A)
_BufferMdSize_Type=Integer32
_BufferMdSize_Object=MibScalar
bufferMdSize=_BufferMdSize_Object((1,3,6,1,4,1,9,2,1,22),_BufferMdSize_Type())
bufferMdSize.setMaxAccess(_B)
if mibBuilder.loadTexts:bufferMdSize.setStatus(_A)
_BufferMdTotal_Type=Integer32
_BufferMdTotal_Object=MibScalar
bufferMdTotal=_BufferMdTotal_Object((1,3,6,1,4,1,9,2,1,23),_BufferMdTotal_Type())
bufferMdTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:bufferMdTotal.setStatus(_A)
_BufferMdFree_Type=Integer32
_BufferMdFree_Object=MibScalar
bufferMdFree=_BufferMdFree_Object((1,3,6,1,4,1,9,2,1,24),_BufferMdFree_Type())
bufferMdFree.setMaxAccess(_B)
if mibBuilder.loadTexts:bufferMdFree.setStatus(_A)
_BufferMdMax_Type=Integer32
_BufferMdMax_Object=MibScalar
bufferMdMax=_BufferMdMax_Object((1,3,6,1,4,1,9,2,1,25),_BufferMdMax_Type())
bufferMdMax.setMaxAccess(_B)
if mibBuilder.loadTexts:bufferMdMax.setStatus(_A)
_BufferMdHit_Type=Integer32
_BufferMdHit_Object=MibScalar
bufferMdHit=_BufferMdHit_Object((1,3,6,1,4,1,9,2,1,26),_BufferMdHit_Type())
bufferMdHit.setMaxAccess(_B)
if mibBuilder.loadTexts:bufferMdHit.setStatus(_A)
_BufferMdMiss_Type=Integer32
_BufferMdMiss_Object=MibScalar
bufferMdMiss=_BufferMdMiss_Object((1,3,6,1,4,1,9,2,1,27),_BufferMdMiss_Type())
bufferMdMiss.setMaxAccess(_B)
if mibBuilder.loadTexts:bufferMdMiss.setStatus(_A)
_BufferMdTrim_Type=Integer32
_BufferMdTrim_Object=MibScalar
bufferMdTrim=_BufferMdTrim_Object((1,3,6,1,4,1,9,2,1,28),_BufferMdTrim_Type())
bufferMdTrim.setMaxAccess(_B)
if mibBuilder.loadTexts:bufferMdTrim.setStatus(_A)
_BufferMdCreate_Type=Integer32
_BufferMdCreate_Object=MibScalar
bufferMdCreate=_BufferMdCreate_Object((1,3,6,1,4,1,9,2,1,29),_BufferMdCreate_Type())
bufferMdCreate.setMaxAccess(_B)
if mibBuilder.loadTexts:bufferMdCreate.setStatus(_A)
_BufferBgSize_Type=Integer32
_BufferBgSize_Object=MibScalar
bufferBgSize=_BufferBgSize_Object((1,3,6,1,4,1,9,2,1,30),_BufferBgSize_Type())
bufferBgSize.setMaxAccess(_B)
if mibBuilder.loadTexts:bufferBgSize.setStatus(_A)
_BufferBgTotal_Type=Integer32
_BufferBgTotal_Object=MibScalar
bufferBgTotal=_BufferBgTotal_Object((1,3,6,1,4,1,9,2,1,31),_BufferBgTotal_Type())
bufferBgTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:bufferBgTotal.setStatus(_A)
_BufferBgFree_Type=Integer32
_BufferBgFree_Object=MibScalar
bufferBgFree=_BufferBgFree_Object((1,3,6,1,4,1,9,2,1,32),_BufferBgFree_Type())
bufferBgFree.setMaxAccess(_B)
if mibBuilder.loadTexts:bufferBgFree.setStatus(_A)
_BufferBgMax_Type=Integer32
_BufferBgMax_Object=MibScalar
bufferBgMax=_BufferBgMax_Object((1,3,6,1,4,1,9,2,1,33),_BufferBgMax_Type())
bufferBgMax.setMaxAccess(_B)
if mibBuilder.loadTexts:bufferBgMax.setStatus(_A)
_BufferBgHit_Type=Integer32
_BufferBgHit_Object=MibScalar
bufferBgHit=_BufferBgHit_Object((1,3,6,1,4,1,9,2,1,34),_BufferBgHit_Type())
bufferBgHit.setMaxAccess(_B)
if mibBuilder.loadTexts:bufferBgHit.setStatus(_A)
_BufferBgMiss_Type=Integer32
_BufferBgMiss_Object=MibScalar
bufferBgMiss=_BufferBgMiss_Object((1,3,6,1,4,1,9,2,1,35),_BufferBgMiss_Type())
bufferBgMiss.setMaxAccess(_B)
if mibBuilder.loadTexts:bufferBgMiss.setStatus(_A)
_BufferBgTrim_Type=Integer32
_BufferBgTrim_Object=MibScalar
bufferBgTrim=_BufferBgTrim_Object((1,3,6,1,4,1,9,2,1,36),_BufferBgTrim_Type())
bufferBgTrim.setMaxAccess(_B)
if mibBuilder.loadTexts:bufferBgTrim.setStatus(_A)
_BufferBgCreate_Type=Integer32
_BufferBgCreate_Object=MibScalar
bufferBgCreate=_BufferBgCreate_Object((1,3,6,1,4,1,9,2,1,37),_BufferBgCreate_Type())
bufferBgCreate.setMaxAccess(_B)
if mibBuilder.loadTexts:bufferBgCreate.setStatus(_A)
_BufferLgSize_Type=Integer32
_BufferLgSize_Object=MibScalar
bufferLgSize=_BufferLgSize_Object((1,3,6,1,4,1,9,2,1,38),_BufferLgSize_Type())
bufferLgSize.setMaxAccess(_B)
if mibBuilder.loadTexts:bufferLgSize.setStatus(_A)
_BufferLgTotal_Type=Integer32
_BufferLgTotal_Object=MibScalar
bufferLgTotal=_BufferLgTotal_Object((1,3,6,1,4,1,9,2,1,39),_BufferLgTotal_Type())
bufferLgTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:bufferLgTotal.setStatus(_A)
_BufferLgFree_Type=Integer32
_BufferLgFree_Object=MibScalar
bufferLgFree=_BufferLgFree_Object((1,3,6,1,4,1,9,2,1,40),_BufferLgFree_Type())
bufferLgFree.setMaxAccess(_B)
if mibBuilder.loadTexts:bufferLgFree.setStatus(_A)
_BufferLgMax_Type=Integer32
_BufferLgMax_Object=MibScalar
bufferLgMax=_BufferLgMax_Object((1,3,6,1,4,1,9,2,1,41),_BufferLgMax_Type())
bufferLgMax.setMaxAccess(_B)
if mibBuilder.loadTexts:bufferLgMax.setStatus(_A)
_BufferLgHit_Type=Integer32
_BufferLgHit_Object=MibScalar
bufferLgHit=_BufferLgHit_Object((1,3,6,1,4,1,9,2,1,42),_BufferLgHit_Type())
bufferLgHit.setMaxAccess(_B)
if mibBuilder.loadTexts:bufferLgHit.setStatus(_A)
_BufferLgMiss_Type=Integer32
_BufferLgMiss_Object=MibScalar
bufferLgMiss=_BufferLgMiss_Object((1,3,6,1,4,1,9,2,1,43),_BufferLgMiss_Type())
bufferLgMiss.setMaxAccess(_B)
if mibBuilder.loadTexts:bufferLgMiss.setStatus(_A)
_BufferLgTrim_Type=Integer32
_BufferLgTrim_Object=MibScalar
bufferLgTrim=_BufferLgTrim_Object((1,3,6,1,4,1,9,2,1,44),_BufferLgTrim_Type())
bufferLgTrim.setMaxAccess(_B)
if mibBuilder.loadTexts:bufferLgTrim.setStatus(_A)
_BufferLgCreate_Type=Integer32
_BufferLgCreate_Object=MibScalar
bufferLgCreate=_BufferLgCreate_Object((1,3,6,1,4,1,9,2,1,45),_BufferLgCreate_Type())
bufferLgCreate.setMaxAccess(_B)
if mibBuilder.loadTexts:bufferLgCreate.setStatus(_A)
_BufferFail_Type=Integer32
_BufferFail_Object=MibScalar
bufferFail=_BufferFail_Object((1,3,6,1,4,1,9,2,1,46),_BufferFail_Type())
bufferFail.setMaxAccess(_B)
if mibBuilder.loadTexts:bufferFail.setStatus(_A)
_BufferNoMem_Type=Integer32
_BufferNoMem_Object=MibScalar
bufferNoMem=_BufferNoMem_Object((1,3,6,1,4,1,9,2,1,47),_BufferNoMem_Type())
bufferNoMem.setMaxAccess(_B)
if mibBuilder.loadTexts:bufferNoMem.setStatus(_A)
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
netConfigSet.setMaxAccess(_D)
if mibBuilder.loadTexts:netConfigSet.setStatus(_A)
_HostConfigAddr_Type=IpAddress
_HostConfigAddr_Object=MibScalar
hostConfigAddr=_HostConfigAddr_Object((1,3,6,1,4,1,9,2,1,51),_HostConfigAddr_Type())
hostConfigAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hostConfigAddr.setStatus(_G)
_HostConfigName_Type=DisplayString
_HostConfigName_Object=MibScalar
hostConfigName=_HostConfigName_Object((1,3,6,1,4,1,9,2,1,52),_HostConfigName_Type())
hostConfigName.setMaxAccess(_B)
if mibBuilder.loadTexts:hostConfigName.setStatus(_G)
_HostConfigSet_Type=DisplayString
_HostConfigSet_Object=MibScalar
hostConfigSet=_HostConfigSet_Object((1,3,6,1,4,1,9,2,1,53),_HostConfigSet_Type())
hostConfigSet.setMaxAccess(_D)
if mibBuilder.loadTexts:hostConfigSet.setStatus(_G)
_WriteMem_Type=Integer32
_WriteMem_Object=MibScalar
writeMem=_WriteMem_Object((1,3,6,1,4,1,9,2,1,54),_WriteMem_Type())
writeMem.setMaxAccess(_D)
if mibBuilder.loadTexts:writeMem.setStatus(_A)
_WriteNet_Type=DisplayString
_WriteNet_Object=MibScalar
writeNet=_WriteNet_Object((1,3,6,1,4,1,9,2,1,55),_WriteNet_Type())
writeNet.setMaxAccess(_D)
if mibBuilder.loadTexts:writeNet.setStatus(_A)
_BusyPer_Type=Integer32
_BusyPer_Object=MibScalar
busyPer=_BusyPer_Object((1,3,6,1,4,1,9,2,1,56),_BusyPer_Type())
busyPer.setMaxAccess(_B)
if mibBuilder.loadTexts:busyPer.setStatus(_A)
_AvgBusy1_Type=Integer32
_AvgBusy1_Object=MibScalar
avgBusy1=_AvgBusy1_Object((1,3,6,1,4,1,9,2,1,57),_AvgBusy1_Type())
avgBusy1.setMaxAccess(_B)
if mibBuilder.loadTexts:avgBusy1.setStatus(_A)
_AvgBusy5_Type=Integer32
_AvgBusy5_Object=MibScalar
avgBusy5=_AvgBusy5_Object((1,3,6,1,4,1,9,2,1,58),_AvgBusy5_Type())
avgBusy5.setMaxAccess(_B)
if mibBuilder.loadTexts:avgBusy5.setStatus(_A)
_IdleCount_Type=Integer32
_IdleCount_Object=MibScalar
idleCount=_IdleCount_Object((1,3,6,1,4,1,9,2,1,59),_IdleCount_Type())
idleCount.setMaxAccess(_H)
if mibBuilder.loadTexts:idleCount.setStatus(_A)
_IdleWired_Type=Integer32
_IdleWired_Object=MibScalar
idleWired=_IdleWired_Object((1,3,6,1,4,1,9,2,1,60),_IdleWired_Type())
idleWired.setMaxAccess(_H)
if mibBuilder.loadTexts:idleWired.setStatus(_A)
_CiscoContactInfo_Type=DisplayString
_CiscoContactInfo_Object=MibScalar
ciscoContactInfo=_CiscoContactInfo_Object((1,3,6,1,4,1,9,2,1,61),_CiscoContactInfo_Type())
ciscoContactInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:ciscoContactInfo.setStatus(_A)
_BufferHgSize_Type=Integer32
_BufferHgSize_Object=MibScalar
bufferHgSize=_BufferHgSize_Object((1,3,6,1,4,1,9,2,1,62),_BufferHgSize_Type())
bufferHgSize.setMaxAccess(_B)
if mibBuilder.loadTexts:bufferHgSize.setStatus(_A)
_BufferHgTotal_Type=Integer32
_BufferHgTotal_Object=MibScalar
bufferHgTotal=_BufferHgTotal_Object((1,3,6,1,4,1,9,2,1,63),_BufferHgTotal_Type())
bufferHgTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:bufferHgTotal.setStatus(_A)
_BufferHgFree_Type=Integer32
_BufferHgFree_Object=MibScalar
bufferHgFree=_BufferHgFree_Object((1,3,6,1,4,1,9,2,1,64),_BufferHgFree_Type())
bufferHgFree.setMaxAccess(_B)
if mibBuilder.loadTexts:bufferHgFree.setStatus(_A)
_BufferHgMax_Type=Integer32
_BufferHgMax_Object=MibScalar
bufferHgMax=_BufferHgMax_Object((1,3,6,1,4,1,9,2,1,65),_BufferHgMax_Type())
bufferHgMax.setMaxAccess(_B)
if mibBuilder.loadTexts:bufferHgMax.setStatus(_A)
_BufferHgHit_Type=Integer32
_BufferHgHit_Object=MibScalar
bufferHgHit=_BufferHgHit_Object((1,3,6,1,4,1,9,2,1,66),_BufferHgHit_Type())
bufferHgHit.setMaxAccess(_B)
if mibBuilder.loadTexts:bufferHgHit.setStatus(_A)
_BufferHgMiss_Type=Integer32
_BufferHgMiss_Object=MibScalar
bufferHgMiss=_BufferHgMiss_Object((1,3,6,1,4,1,9,2,1,67),_BufferHgMiss_Type())
bufferHgMiss.setMaxAccess(_B)
if mibBuilder.loadTexts:bufferHgMiss.setStatus(_A)
_BufferHgTrim_Type=Integer32
_BufferHgTrim_Object=MibScalar
bufferHgTrim=_BufferHgTrim_Object((1,3,6,1,4,1,9,2,1,68),_BufferHgTrim_Type())
bufferHgTrim.setMaxAccess(_B)
if mibBuilder.loadTexts:bufferHgTrim.setStatus(_A)
_BufferHgCreate_Type=Integer32
_BufferHgCreate_Object=MibScalar
bufferHgCreate=_BufferHgCreate_Object((1,3,6,1,4,1,9,2,1,69),_BufferHgCreate_Type())
bufferHgCreate.setMaxAccess(_B)
if mibBuilder.loadTexts:bufferHgCreate.setStatus(_A)
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
_SysConfigProto_Type=Integer32
_SysConfigProto_Object=MibScalar
sysConfigProto=_SysConfigProto_Object((1,3,6,1,4,1,9,2,1,74),_SysConfigProto_Type())
sysConfigProto.setMaxAccess(_B)
if mibBuilder.loadTexts:sysConfigProto.setStatus(_A)
_SysClearARP_Type=Integer32
_SysClearARP_Object=MibScalar
sysClearARP=_SysClearARP_Object((1,3,6,1,4,1,9,2,1,75),_SysClearARP_Type())
sysClearARP.setMaxAccess(_D)
if mibBuilder.loadTexts:sysClearARP.setStatus(_A)
_SysClearInt_Type=Integer32
_SysClearInt_Object=MibScalar
sysClearInt=_SysClearInt_Object((1,3,6,1,4,1,9,2,1,76),_SysClearInt_Type())
sysClearInt.setMaxAccess(_D)
if mibBuilder.loadTexts:sysClearInt.setStatus(_A)
_EnvPresent_Type=Integer32
_EnvPresent_Object=MibScalar
envPresent=_EnvPresent_Object((1,3,6,1,4,1,9,2,1,77),_EnvPresent_Type())
envPresent.setMaxAccess(_B)
if mibBuilder.loadTexts:envPresent.setStatus(_A)
_EnvTestPt1Descr_Type=DisplayString
_EnvTestPt1Descr_Object=MibScalar
envTestPt1Descr=_EnvTestPt1Descr_Object((1,3,6,1,4,1,9,2,1,78),_EnvTestPt1Descr_Type())
envTestPt1Descr.setMaxAccess(_B)
if mibBuilder.loadTexts:envTestPt1Descr.setStatus(_A)
_EnvTestPt1Measure_Type=Integer32
_EnvTestPt1Measure_Object=MibScalar
envTestPt1Measure=_EnvTestPt1Measure_Object((1,3,6,1,4,1,9,2,1,79),_EnvTestPt1Measure_Type())
envTestPt1Measure.setMaxAccess(_B)
if mibBuilder.loadTexts:envTestPt1Measure.setStatus(_A)
_EnvTestPt2Descr_Type=DisplayString
_EnvTestPt2Descr_Object=MibScalar
envTestPt2Descr=_EnvTestPt2Descr_Object((1,3,6,1,4,1,9,2,1,80),_EnvTestPt2Descr_Type())
envTestPt2Descr.setMaxAccess(_B)
if mibBuilder.loadTexts:envTestPt2Descr.setStatus(_A)
_EnvTestPt2Measure_Type=Integer32
_EnvTestPt2Measure_Object=MibScalar
envTestPt2Measure=_EnvTestPt2Measure_Object((1,3,6,1,4,1,9,2,1,81),_EnvTestPt2Measure_Type())
envTestPt2Measure.setMaxAccess(_B)
if mibBuilder.loadTexts:envTestPt2Measure.setStatus(_A)
_EnvTestPt3Descr_Type=DisplayString
_EnvTestPt3Descr_Object=MibScalar
envTestPt3Descr=_EnvTestPt3Descr_Object((1,3,6,1,4,1,9,2,1,82),_EnvTestPt3Descr_Type())
envTestPt3Descr.setMaxAccess(_B)
if mibBuilder.loadTexts:envTestPt3Descr.setStatus(_A)
_EnvTestPt3Measure_Type=Integer32
_EnvTestPt3Measure_Object=MibScalar
envTestPt3Measure=_EnvTestPt3Measure_Object((1,3,6,1,4,1,9,2,1,83),_EnvTestPt3Measure_Type())
envTestPt3Measure.setMaxAccess(_B)
if mibBuilder.loadTexts:envTestPt3Measure.setStatus(_A)
_EnvTestPt4Descr_Type=DisplayString
_EnvTestPt4Descr_Object=MibScalar
envTestPt4Descr=_EnvTestPt4Descr_Object((1,3,6,1,4,1,9,2,1,84),_EnvTestPt4Descr_Type())
envTestPt4Descr.setMaxAccess(_B)
if mibBuilder.loadTexts:envTestPt4Descr.setStatus(_A)
_EnvTestPt4Measure_Type=Integer32
_EnvTestPt4Measure_Object=MibScalar
envTestPt4Measure=_EnvTestPt4Measure_Object((1,3,6,1,4,1,9,2,1,85),_EnvTestPt4Measure_Type())
envTestPt4Measure.setMaxAccess(_B)
if mibBuilder.loadTexts:envTestPt4Measure.setStatus(_A)
_EnvTestPt5Descr_Type=DisplayString
_EnvTestPt5Descr_Object=MibScalar
envTestPt5Descr=_EnvTestPt5Descr_Object((1,3,6,1,4,1,9,2,1,86),_EnvTestPt5Descr_Type())
envTestPt5Descr.setMaxAccess(_B)
if mibBuilder.loadTexts:envTestPt5Descr.setStatus(_A)
_EnvTestPt5Measure_Type=Integer32
_EnvTestPt5Measure_Object=MibScalar
envTestPt5Measure=_EnvTestPt5Measure_Object((1,3,6,1,4,1,9,2,1,87),_EnvTestPt5Measure_Type())
envTestPt5Measure.setMaxAccess(_B)
if mibBuilder.loadTexts:envTestPt5Measure.setStatus(_A)
_EnvTestPt6Descr_Type=DisplayString
_EnvTestPt6Descr_Object=MibScalar
envTestPt6Descr=_EnvTestPt6Descr_Object((1,3,6,1,4,1,9,2,1,88),_EnvTestPt6Descr_Type())
envTestPt6Descr.setMaxAccess(_B)
if mibBuilder.loadTexts:envTestPt6Descr.setStatus(_A)
_EnvTestPt6Measure_Type=Integer32
_EnvTestPt6Measure_Object=MibScalar
envTestPt6Measure=_EnvTestPt6Measure_Object((1,3,6,1,4,1,9,2,1,89),_EnvTestPt6Measure_Type())
envTestPt6Measure.setMaxAccess(_B)
if mibBuilder.loadTexts:envTestPt6Measure.setStatus(_A)
_EnvTestPt1MarginVal_Type=Integer32
_EnvTestPt1MarginVal_Object=MibScalar
envTestPt1MarginVal=_EnvTestPt1MarginVal_Object((1,3,6,1,4,1,9,2,1,90),_EnvTestPt1MarginVal_Type())
envTestPt1MarginVal.setMaxAccess(_B)
if mibBuilder.loadTexts:envTestPt1MarginVal.setStatus(_A)
_EnvTestPt2MarginVal_Type=Integer32
_EnvTestPt2MarginVal_Object=MibScalar
envTestPt2MarginVal=_EnvTestPt2MarginVal_Object((1,3,6,1,4,1,9,2,1,91),_EnvTestPt2MarginVal_Type())
envTestPt2MarginVal.setMaxAccess(_B)
if mibBuilder.loadTexts:envTestPt2MarginVal.setStatus(_A)
_EnvTestPt3MarginPercent_Type=Integer32
_EnvTestPt3MarginPercent_Object=MibScalar
envTestPt3MarginPercent=_EnvTestPt3MarginPercent_Object((1,3,6,1,4,1,9,2,1,92),_EnvTestPt3MarginPercent_Type())
envTestPt3MarginPercent.setMaxAccess(_B)
if mibBuilder.loadTexts:envTestPt3MarginPercent.setStatus(_A)
_EnvTestPt4MarginPercent_Type=Integer32
_EnvTestPt4MarginPercent_Object=MibScalar
envTestPt4MarginPercent=_EnvTestPt4MarginPercent_Object((1,3,6,1,4,1,9,2,1,93),_EnvTestPt4MarginPercent_Type())
envTestPt4MarginPercent.setMaxAccess(_B)
if mibBuilder.loadTexts:envTestPt4MarginPercent.setStatus(_A)
_EnvTestPt5MarginPercent_Type=Integer32
_EnvTestPt5MarginPercent_Object=MibScalar
envTestPt5MarginPercent=_EnvTestPt5MarginPercent_Object((1,3,6,1,4,1,9,2,1,94),_EnvTestPt5MarginPercent_Type())
envTestPt5MarginPercent.setMaxAccess(_B)
if mibBuilder.loadTexts:envTestPt5MarginPercent.setStatus(_A)
_EnvTestPt6MarginPercent_Type=Integer32
_EnvTestPt6MarginPercent_Object=MibScalar
envTestPt6MarginPercent=_EnvTestPt6MarginPercent_Object((1,3,6,1,4,1,9,2,1,95),_EnvTestPt6MarginPercent_Type())
envTestPt6MarginPercent.setMaxAccess(_B)
if mibBuilder.loadTexts:envTestPt6MarginPercent.setStatus(_A)
_EnvTestPt1last_Type=Integer32
_EnvTestPt1last_Object=MibScalar
envTestPt1last=_EnvTestPt1last_Object((1,3,6,1,4,1,9,2,1,96),_EnvTestPt1last_Type())
envTestPt1last.setMaxAccess(_B)
if mibBuilder.loadTexts:envTestPt1last.setStatus(_A)
_EnvTestPt2last_Type=Integer32
_EnvTestPt2last_Object=MibScalar
envTestPt2last=_EnvTestPt2last_Object((1,3,6,1,4,1,9,2,1,97),_EnvTestPt2last_Type())
envTestPt2last.setMaxAccess(_B)
if mibBuilder.loadTexts:envTestPt2last.setStatus(_A)
_EnvTestPt3last_Type=Integer32
_EnvTestPt3last_Object=MibScalar
envTestPt3last=_EnvTestPt3last_Object((1,3,6,1,4,1,9,2,1,98),_EnvTestPt3last_Type())
envTestPt3last.setMaxAccess(_B)
if mibBuilder.loadTexts:envTestPt3last.setStatus(_A)
_EnvTestPt4last_Type=Integer32
_EnvTestPt4last_Object=MibScalar
envTestPt4last=_EnvTestPt4last_Object((1,3,6,1,4,1,9,2,1,99),_EnvTestPt4last_Type())
envTestPt4last.setMaxAccess(_B)
if mibBuilder.loadTexts:envTestPt4last.setStatus(_A)
_EnvTestPt5last_Type=Integer32
_EnvTestPt5last_Object=MibScalar
envTestPt5last=_EnvTestPt5last_Object((1,3,6,1,4,1,9,2,1,100),_EnvTestPt5last_Type())
envTestPt5last.setMaxAccess(_B)
if mibBuilder.loadTexts:envTestPt5last.setStatus(_A)
_EnvTestPt6last_Type=Integer32
_EnvTestPt6last_Object=MibScalar
envTestPt6last=_EnvTestPt6last_Object((1,3,6,1,4,1,9,2,1,101),_EnvTestPt6last_Type())
envTestPt6last.setMaxAccess(_B)
if mibBuilder.loadTexts:envTestPt6last.setStatus(_A)
class _EnvTestPt1warn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_EnvTestPt1warn_Type.__name__=_C
_EnvTestPt1warn_Object=MibScalar
envTestPt1warn=_EnvTestPt1warn_Object((1,3,6,1,4,1,9,2,1,102),_EnvTestPt1warn_Type())
envTestPt1warn.setMaxAccess(_B)
if mibBuilder.loadTexts:envTestPt1warn.setStatus(_A)
class _EnvTestPt2warn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_EnvTestPt2warn_Type.__name__=_C
_EnvTestPt2warn_Object=MibScalar
envTestPt2warn=_EnvTestPt2warn_Object((1,3,6,1,4,1,9,2,1,103),_EnvTestPt2warn_Type())
envTestPt2warn.setMaxAccess(_B)
if mibBuilder.loadTexts:envTestPt2warn.setStatus(_A)
class _EnvTestPt3warn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_EnvTestPt3warn_Type.__name__=_C
_EnvTestPt3warn_Object=MibScalar
envTestPt3warn=_EnvTestPt3warn_Object((1,3,6,1,4,1,9,2,1,104),_EnvTestPt3warn_Type())
envTestPt3warn.setMaxAccess(_B)
if mibBuilder.loadTexts:envTestPt3warn.setStatus(_A)
class _EnvTestPt4warn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_EnvTestPt4warn_Type.__name__=_C
_EnvTestPt4warn_Object=MibScalar
envTestPt4warn=_EnvTestPt4warn_Object((1,3,6,1,4,1,9,2,1,105),_EnvTestPt4warn_Type())
envTestPt4warn.setMaxAccess(_B)
if mibBuilder.loadTexts:envTestPt4warn.setStatus(_A)
class _EnvTestPt5warn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_EnvTestPt5warn_Type.__name__=_C
_EnvTestPt5warn_Object=MibScalar
envTestPt5warn=_EnvTestPt5warn_Object((1,3,6,1,4,1,9,2,1,106),_EnvTestPt5warn_Type())
envTestPt5warn.setMaxAccess(_B)
if mibBuilder.loadTexts:envTestPt5warn.setStatus(_A)
class _EnvTestPt6warn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_EnvTestPt6warn_Type.__name__=_C
_EnvTestPt6warn_Object=MibScalar
envTestPt6warn=_EnvTestPt6warn_Object((1,3,6,1,4,1,9,2,1,107),_EnvTestPt6warn_Type())
envTestPt6warn.setMaxAccess(_B)
if mibBuilder.loadTexts:envTestPt6warn.setStatus(_A)
_EnvFirmVersion_Type=DisplayString
_EnvFirmVersion_Object=MibScalar
envFirmVersion=_EnvFirmVersion_Object((1,3,6,1,4,1,9,2,1,108),_EnvFirmVersion_Type())
envFirmVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:envFirmVersion.setStatus(_A)
_EnvTechnicianID_Type=DisplayString
_EnvTechnicianID_Object=MibScalar
envTechnicianID=_EnvTechnicianID_Object((1,3,6,1,4,1,9,2,1,109),_EnvTechnicianID_Type())
envTechnicianID.setMaxAccess(_B)
if mibBuilder.loadTexts:envTechnicianID.setStatus(_A)
_EnvType_Type=DisplayString
_EnvType_Object=MibScalar
envType=_EnvType_Object((1,3,6,1,4,1,9,2,1,110),_EnvType_Type())
envType.setMaxAccess(_B)
if mibBuilder.loadTexts:envType.setStatus(_A)
_EnvBurnDate_Type=DisplayString
_EnvBurnDate_Object=MibScalar
envBurnDate=_EnvBurnDate_Object((1,3,6,1,4,1,9,2,1,111),_EnvBurnDate_Type())
envBurnDate.setMaxAccess(_B)
if mibBuilder.loadTexts:envBurnDate.setStatus(_A)
_EnvSerialNumber_Type=DisplayString
_EnvSerialNumber_Object=MibScalar
envSerialNumber=_EnvSerialNumber_Object((1,3,6,1,4,1,9,2,1,112),_EnvSerialNumber_Type())
envSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:envSerialNumber.setStatus(_A)
mibBuilder.exportSymbols('OLD-CISCO-SYS-MIB',**{'lsystem':lsystem,'romId':romId,'whyReload':whyReload,'hostName':hostName,'domainName':domainName,'authAddr':authAddr,'bootHost':bootHost,'ping':ping,'freeMem':freeMem,'bufferElFree':bufferElFree,'bufferElMax':bufferElMax,'bufferElHit':bufferElHit,'bufferElMiss':bufferElMiss,'bufferElCreate':bufferElCreate,'bufferSmSize':bufferSmSize,'bufferSmTotal':bufferSmTotal,'bufferSmFree':bufferSmFree,'bufferSmMax':bufferSmMax,'bufferSmHit':bufferSmHit,'bufferSmMiss':bufferSmMiss,'bufferSmTrim':bufferSmTrim,'bufferSmCreate':bufferSmCreate,'bufferMdSize':bufferMdSize,'bufferMdTotal':bufferMdTotal,'bufferMdFree':bufferMdFree,'bufferMdMax':bufferMdMax,'bufferMdHit':bufferMdHit,'bufferMdMiss':bufferMdMiss,'bufferMdTrim':bufferMdTrim,'bufferMdCreate':bufferMdCreate,'bufferBgSize':bufferBgSize,'bufferBgTotal':bufferBgTotal,'bufferBgFree':bufferBgFree,'bufferBgMax':bufferBgMax,'bufferBgHit':bufferBgHit,'bufferBgMiss':bufferBgMiss,'bufferBgTrim':bufferBgTrim,'bufferBgCreate':bufferBgCreate,'bufferLgSize':bufferLgSize,'bufferLgTotal':bufferLgTotal,'bufferLgFree':bufferLgFree,'bufferLgMax':bufferLgMax,'bufferLgHit':bufferLgHit,'bufferLgMiss':bufferLgMiss,'bufferLgTrim':bufferLgTrim,'bufferLgCreate':bufferLgCreate,'bufferFail':bufferFail,'bufferNoMem':bufferNoMem,'netConfigAddr':netConfigAddr,'netConfigName':netConfigName,'netConfigSet':netConfigSet,'hostConfigAddr':hostConfigAddr,'hostConfigName':hostConfigName,'hostConfigSet':hostConfigSet,'writeMem':writeMem,'writeNet':writeNet,'busyPer':busyPer,'avgBusy1':avgBusy1,'avgBusy5':avgBusy5,'idleCount':idleCount,'idleWired':idleWired,'ciscoContactInfo':ciscoContactInfo,'bufferHgSize':bufferHgSize,'bufferHgTotal':bufferHgTotal,'bufferHgFree':bufferHgFree,'bufferHgMax':bufferHgMax,'bufferHgHit':bufferHgHit,'bufferHgMiss':bufferHgMiss,'bufferHgTrim':bufferHgTrim,'bufferHgCreate':bufferHgCreate,'netConfigProto':netConfigProto,'hostConfigProto':hostConfigProto,'sysConfigAddr':sysConfigAddr,'sysConfigName':sysConfigName,'sysConfigProto':sysConfigProto,'sysClearARP':sysClearARP,'sysClearInt':sysClearInt,'envPresent':envPresent,'envTestPt1Descr':envTestPt1Descr,'envTestPt1Measure':envTestPt1Measure,'envTestPt2Descr':envTestPt2Descr,'envTestPt2Measure':envTestPt2Measure,'envTestPt3Descr':envTestPt3Descr,'envTestPt3Measure':envTestPt3Measure,'envTestPt4Descr':envTestPt4Descr,'envTestPt4Measure':envTestPt4Measure,'envTestPt5Descr':envTestPt5Descr,'envTestPt5Measure':envTestPt5Measure,'envTestPt6Descr':envTestPt6Descr,'envTestPt6Measure':envTestPt6Measure,'envTestPt1MarginVal':envTestPt1MarginVal,'envTestPt2MarginVal':envTestPt2MarginVal,'envTestPt3MarginPercent':envTestPt3MarginPercent,'envTestPt4MarginPercent':envTestPt4MarginPercent,'envTestPt5MarginPercent':envTestPt5MarginPercent,'envTestPt6MarginPercent':envTestPt6MarginPercent,'envTestPt1last':envTestPt1last,'envTestPt2last':envTestPt2last,'envTestPt3last':envTestPt3last,'envTestPt4last':envTestPt4last,'envTestPt5last':envTestPt5last,'envTestPt6last':envTestPt6last,'envTestPt1warn':envTestPt1warn,'envTestPt2warn':envTestPt2warn,'envTestPt3warn':envTestPt3warn,'envTestPt4warn':envTestPt4warn,'envTestPt5warn':envTestPt5warn,'envTestPt6warn':envTestPt6warn,'envFirmVersion':envFirmVersion,'envTechnicianID':envTechnicianID,'envType':envType,'envBurnDate':envBurnDate,'envSerialNumber':envSerialNumber})