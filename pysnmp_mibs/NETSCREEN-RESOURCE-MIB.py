_G='nsResModCpuId'
_F='nsResModModId'
_E='NETSCREEN-RESOURCE-MIB'
_D='Integer32'
_C='current'
_B='mandatory'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
netscreenResource,=mibBuilder.importSymbols('NETSCREEN-SMI','netscreenResource')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
netscreenResourceMibModule=ModuleIdentity((1,3,6,1,4,1,3224,16,0))
if mibBuilder.loadTexts:netscreenResourceMibModule.setRevisions(('2004-05-03 00:00','2004-03-03 00:00','2003-11-10 00:00','2002-05-05 00:00','2001-04-30 00:00'))
_NsResCPU_ObjectIdentity=ObjectIdentity
nsResCPU=_NsResCPU_ObjectIdentity((1,3,6,1,4,1,3224,16,1))
_NsResCpuAvg_Type=Integer32
_NsResCpuAvg_Object=MibScalar
nsResCpuAvg=_NsResCpuAvg_Object((1,3,6,1,4,1,3224,16,1,1),_NsResCpuAvg_Type())
nsResCpuAvg.setMaxAccess(_A)
if mibBuilder.loadTexts:nsResCpuAvg.setStatus(_C)
_NsResCpuLast1Min_Type=Integer32
_NsResCpuLast1Min_Object=MibScalar
nsResCpuLast1Min=_NsResCpuLast1Min_Object((1,3,6,1,4,1,3224,16,1,2),_NsResCpuLast1Min_Type())
nsResCpuLast1Min.setMaxAccess(_A)
if mibBuilder.loadTexts:nsResCpuLast1Min.setStatus(_C)
_NsResCpuLast5Min_Type=Integer32
_NsResCpuLast5Min_Object=MibScalar
nsResCpuLast5Min=_NsResCpuLast5Min_Object((1,3,6,1,4,1,3224,16,1,3),_NsResCpuLast5Min_Type())
nsResCpuLast5Min.setMaxAccess(_A)
if mibBuilder.loadTexts:nsResCpuLast5Min.setStatus(_C)
_NsResCpuLast15Min_Type=Integer32
_NsResCpuLast15Min_Object=MibScalar
nsResCpuLast15Min=_NsResCpuLast15Min_Object((1,3,6,1,4,1,3224,16,1,4),_NsResCpuLast15Min_Type())
nsResCpuLast15Min.setMaxAccess(_A)
if mibBuilder.loadTexts:nsResCpuLast15Min.setStatus(_C)
_NsResMem_ObjectIdentity=ObjectIdentity
nsResMem=_NsResMem_ObjectIdentity((1,3,6,1,4,1,3224,16,2))
_NsResMemAllocate_Type=Integer32
_NsResMemAllocate_Object=MibScalar
nsResMemAllocate=_NsResMemAllocate_Object((1,3,6,1,4,1,3224,16,2,1),_NsResMemAllocate_Type())
nsResMemAllocate.setMaxAccess(_A)
if mibBuilder.loadTexts:nsResMemAllocate.setStatus(_C)
_NsResMemLeft_Type=Integer32
_NsResMemLeft_Object=MibScalar
nsResMemLeft=_NsResMemLeft_Object((1,3,6,1,4,1,3224,16,2,2),_NsResMemLeft_Type())
nsResMemLeft.setMaxAccess(_A)
if mibBuilder.loadTexts:nsResMemLeft.setStatus(_C)
_NsResMemFrag_Type=Integer32
_NsResMemFrag_Object=MibScalar
nsResMemFrag=_NsResMemFrag_Object((1,3,6,1,4,1,3224,16,2,3),_NsResMemFrag_Type())
nsResMemFrag.setMaxAccess(_A)
if mibBuilder.loadTexts:nsResMemFrag.setStatus(_C)
_NsResSession_ObjectIdentity=ObjectIdentity
nsResSession=_NsResSession_ObjectIdentity((1,3,6,1,4,1,3224,16,3))
_NsResSessAllocate_Type=Integer32
_NsResSessAllocate_Object=MibScalar
nsResSessAllocate=_NsResSessAllocate_Object((1,3,6,1,4,1,3224,16,3,2),_NsResSessAllocate_Type())
nsResSessAllocate.setMaxAccess(_A)
if mibBuilder.loadTexts:nsResSessAllocate.setStatus(_C)
_NsResSessMaxium_Type=Integer32
_NsResSessMaxium_Object=MibScalar
nsResSessMaxium=_NsResSessMaxium_Object((1,3,6,1,4,1,3224,16,3,3),_NsResSessMaxium_Type())
nsResSessMaxium.setMaxAccess(_A)
if mibBuilder.loadTexts:nsResSessMaxium.setStatus(_C)
_NsResSessFailed_Type=Integer32
_NsResSessFailed_Object=MibScalar
nsResSessFailed=_NsResSessFailed_Object((1,3,6,1,4,1,3224,16,3,4),_NsResSessFailed_Type())
nsResSessFailed.setMaxAccess(_A)
if mibBuilder.loadTexts:nsResSessFailed.setStatus(_C)
_NsResModTable_Object=MibTable
nsResModTable=_NsResModTable_Object((1,3,6,1,4,1,3224,16,4))
if mibBuilder.loadTexts:nsResModTable.setStatus(_B)
_NsResModEntry_Object=MibTableRow
nsResModEntry=_NsResModEntry_Object((1,3,6,1,4,1,3224,16,4,1))
nsResModEntry.setIndexNames((0,_E,_F),(0,_E,_G))
if mibBuilder.loadTexts:nsResModEntry.setStatus(_B)
class _NsResModModId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_NsResModModId_Type.__name__=_D
_NsResModModId_Object=MibTableColumn
nsResModModId=_NsResModModId_Object((1,3,6,1,4,1,3224,16,4,1,1),_NsResModModId_Type())
nsResModModId.setMaxAccess(_A)
if mibBuilder.loadTexts:nsResModModId.setStatus(_B)
class _NsResModCpuId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_NsResModCpuId_Type.__name__=_D
_NsResModCpuId_Object=MibTableColumn
nsResModCpuId=_NsResModCpuId_Object((1,3,6,1,4,1,3224,16,4,1,2),_NsResModCpuId_Type())
nsResModCpuId.setMaxAccess(_A)
if mibBuilder.loadTexts:nsResModCpuId.setStatus(_B)
class _NsResModCpuCurr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_NsResModCpuCurr_Type.__name__=_D
_NsResModCpuCurr_Object=MibTableColumn
nsResModCpuCurr=_NsResModCpuCurr_Object((1,3,6,1,4,1,3224,16,4,1,3),_NsResModCpuCurr_Type())
nsResModCpuCurr.setMaxAccess(_A)
if mibBuilder.loadTexts:nsResModCpuCurr.setStatus(_B)
class _NsResModCpuLast1Min_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_NsResModCpuLast1Min_Type.__name__=_D
_NsResModCpuLast1Min_Object=MibTableColumn
nsResModCpuLast1Min=_NsResModCpuLast1Min_Object((1,3,6,1,4,1,3224,16,4,1,4),_NsResModCpuLast1Min_Type())
nsResModCpuLast1Min.setMaxAccess(_A)
if mibBuilder.loadTexts:nsResModCpuLast1Min.setStatus(_B)
class _NsResModCpuLast5Min_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_NsResModCpuLast5Min_Type.__name__=_D
_NsResModCpuLast5Min_Object=MibTableColumn
nsResModCpuLast5Min=_NsResModCpuLast5Min_Object((1,3,6,1,4,1,3224,16,4,1,5),_NsResModCpuLast5Min_Type())
nsResModCpuLast5Min.setMaxAccess(_A)
if mibBuilder.loadTexts:nsResModCpuLast5Min.setStatus(_B)
class _NsResModCpuLast15Min_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_NsResModCpuLast15Min_Type.__name__=_D
_NsResModCpuLast15Min_Object=MibTableColumn
nsResModCpuLast15Min=_NsResModCpuLast15Min_Object((1,3,6,1,4,1,3224,16,4,1,6),_NsResModCpuLast15Min_Type())
nsResModCpuLast15Min.setMaxAccess(_A)
if mibBuilder.loadTexts:nsResModCpuLast15Min.setStatus(_B)
_NsResModMemAllocated_Type=Integer32
_NsResModMemAllocated_Object=MibTableColumn
nsResModMemAllocated=_NsResModMemAllocated_Object((1,3,6,1,4,1,3224,16,4,1,7),_NsResModMemAllocated_Type())
nsResModMemAllocated.setMaxAccess(_A)
if mibBuilder.loadTexts:nsResModMemAllocated.setStatus(_B)
_NsResModMemLeft_Type=Integer32
_NsResModMemLeft_Object=MibTableColumn
nsResModMemLeft=_NsResModMemLeft_Object((1,3,6,1,4,1,3224,16,4,1,8),_NsResModMemLeft_Type())
nsResModMemLeft.setMaxAccess(_A)
if mibBuilder.loadTexts:nsResModMemLeft.setStatus(_B)
_NsResModSessAllocated_Type=Integer32
_NsResModSessAllocated_Object=MibTableColumn
nsResModSessAllocated=_NsResModSessAllocated_Object((1,3,6,1,4,1,3224,16,4,1,9),_NsResModSessAllocated_Type())
nsResModSessAllocated.setMaxAccess(_A)
if mibBuilder.loadTexts:nsResModSessAllocated.setStatus(_B)
_NsResModSessMaximum_Type=Integer32
_NsResModSessMaximum_Object=MibTableColumn
nsResModSessMaximum=_NsResModSessMaximum_Object((1,3,6,1,4,1,3224,16,4,1,10),_NsResModSessMaximum_Type())
nsResModSessMaximum.setMaxAccess(_A)
if mibBuilder.loadTexts:nsResModSessMaximum.setStatus(_B)
_NsResModSessFailed_Type=Integer32
_NsResModSessFailed_Object=MibTableColumn
nsResModSessFailed=_NsResModSessFailed_Object((1,3,6,1,4,1,3224,16,4,1,11),_NsResModSessFailed_Type())
nsResModSessFailed.setMaxAccess(_A)
if mibBuilder.loadTexts:nsResModSessFailed.setStatus(_B)
_NsResModThresholdMem_Type=Integer32
_NsResModThresholdMem_Object=MibTableColumn
nsResModThresholdMem=_NsResModThresholdMem_Object((1,3,6,1,4,1,3224,16,4,1,12),_NsResModThresholdMem_Type())
nsResModThresholdMem.setMaxAccess(_A)
if mibBuilder.loadTexts:nsResModThresholdMem.setStatus(_B)
_NsResModThresholdCpu_Type=Integer32
_NsResModThresholdCpu_Object=MibTableColumn
nsResModThresholdCpu=_NsResModThresholdCpu_Object((1,3,6,1,4,1,3224,16,4,1,13),_NsResModThresholdCpu_Type())
nsResModThresholdCpu.setMaxAccess(_A)
if mibBuilder.loadTexts:nsResModThresholdCpu.setStatus(_B)
_NsResModThresholdSession_Type=Integer32
_NsResModThresholdSession_Object=MibTableColumn
nsResModThresholdSession=_NsResModThresholdSession_Object((1,3,6,1,4,1,3224,16,4,1,14),_NsResModThresholdSession_Type())
nsResModThresholdSession.setMaxAccess(_A)
if mibBuilder.loadTexts:nsResModThresholdSession.setStatus(_B)
mibBuilder.exportSymbols(_E,**{'netscreenResourceMibModule':netscreenResourceMibModule,'nsResCPU':nsResCPU,'nsResCpuAvg':nsResCpuAvg,'nsResCpuLast1Min':nsResCpuLast1Min,'nsResCpuLast5Min':nsResCpuLast5Min,'nsResCpuLast15Min':nsResCpuLast15Min,'nsResMem':nsResMem,'nsResMemAllocate':nsResMemAllocate,'nsResMemLeft':nsResMemLeft,'nsResMemFrag':nsResMemFrag,'nsResSession':nsResSession,'nsResSessAllocate':nsResSessAllocate,'nsResSessMaxium':nsResSessMaxium,'nsResSessFailed':nsResSessFailed,'nsResModTable':nsResModTable,'nsResModEntry':nsResModEntry,_F:nsResModModId,_G:nsResModCpuId,'nsResModCpuCurr':nsResModCpuCurr,'nsResModCpuLast1Min':nsResModCpuLast1Min,'nsResModCpuLast5Min':nsResModCpuLast5Min,'nsResModCpuLast15Min':nsResModCpuLast15Min,'nsResModMemAllocated':nsResModMemAllocated,'nsResModMemLeft':nsResModMemLeft,'nsResModSessAllocated':nsResModSessAllocated,'nsResModSessMaximum':nsResModSessMaximum,'nsResModSessFailed':nsResModSessFailed,'nsResModThresholdMem':nsResModThresholdMem,'nsResModThresholdCpu':nsResModThresholdCpu,'nsResModThresholdSession':nsResModThresholdSession})