_W='tptNgfwPerformanceGroup'
_V='tptNgfwPerfPacketDistSizeGrpCount'
_U='tptNgfwPerfPacketDistSizeGrp'
_T='tptNgfwPerfIPSTrustedStreams'
_S='tptNgfwPerfIPSBlockedStreams'
_R='tptNgfwPerfIPSAfcAppEntries'
_Q='tptNgfwPerfIPSAfcEntries'
_P='tptNgfwPerfIPSRateLimitCount'
_O='tptNgfwPerfIPSQuarantineCount'
_N='tptNgfwPerfIPSManagedStreams'
_M='tptNgfwPerfFWSessions'
_L='tptNgfwPerfFWPermits'
_K='tptNgfwPerfFWBlocks'
_J='tptNgfwPerfFragmentsOut'
_I='tptNgfwPerfFragmentsIn'
_H='tptNgfwPerfBytesOut'
_G='tptNgfwPerfBytesIn'
_F='tptNgfwPerfPacketsOut'
_E='tptNgfwPerfPacketsIn'
_D='tptNgfwPerfPacketDistEntryIndex'
_C='read-only'
_B='TPT-NGFW-PERFORMANCE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tpt_ngfw_compls,tpt_ngfw_groups,tpt_ngfw_objs=mibBuilder.importSymbols('TPT-NGFW-REG-MIB','tpt-ngfw-compls','tpt-ngfw-groups','tpt-ngfw-objs')
tptNgfwPerformance=ModuleIdentity((1,3,6,1,4,1,10734,3,9,2,3))
if mibBuilder.loadTexts:tptNgfwPerformance.setRevisions(('2016-05-25 18:54','2013-01-03 17:39'))
class TptNgfwPerfPacketSizeGrouping(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('bytes64',0),('bytes65to127',1),('bytes128to255',2),('bytes256to511',3),('bytes512to1023',4),('bytes1024to1518',5),('bytes1519to4095',6),('bytes4096to9216',7),('bytes9217to16383',8),('undersize',9),('oversize',10)))
_TptNgfwPerformanceObjs_ObjectIdentity=ObjectIdentity
tptNgfwPerformanceObjs=_TptNgfwPerformanceObjs_ObjectIdentity((1,3,6,1,4,1,10734,3,9,2,3,1))
if mibBuilder.loadTexts:tptNgfwPerformanceObjs.setStatus(_A)
_TptNgfwPerfPacketsIn_Type=Counter64
_TptNgfwPerfPacketsIn_Object=MibScalar
tptNgfwPerfPacketsIn=_TptNgfwPerfPacketsIn_Object((1,3,6,1,4,1,10734,3,9,2,3,1,1),_TptNgfwPerfPacketsIn_Type())
tptNgfwPerfPacketsIn.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwPerfPacketsIn.setStatus(_A)
_TptNgfwPerfPacketsOut_Type=Counter64
_TptNgfwPerfPacketsOut_Object=MibScalar
tptNgfwPerfPacketsOut=_TptNgfwPerfPacketsOut_Object((1,3,6,1,4,1,10734,3,9,2,3,1,2),_TptNgfwPerfPacketsOut_Type())
tptNgfwPerfPacketsOut.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwPerfPacketsOut.setStatus(_A)
_TptNgfwPerfBytesIn_Type=Counter64
_TptNgfwPerfBytesIn_Object=MibScalar
tptNgfwPerfBytesIn=_TptNgfwPerfBytesIn_Object((1,3,6,1,4,1,10734,3,9,2,3,1,3),_TptNgfwPerfBytesIn_Type())
tptNgfwPerfBytesIn.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwPerfBytesIn.setStatus(_A)
_TptNgfwPerfBytesOut_Type=Counter64
_TptNgfwPerfBytesOut_Object=MibScalar
tptNgfwPerfBytesOut=_TptNgfwPerfBytesOut_Object((1,3,6,1,4,1,10734,3,9,2,3,1,4),_TptNgfwPerfBytesOut_Type())
tptNgfwPerfBytesOut.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwPerfBytesOut.setStatus(_A)
_TptNgfwPerfFragmentsIn_Type=Counter64
_TptNgfwPerfFragmentsIn_Object=MibScalar
tptNgfwPerfFragmentsIn=_TptNgfwPerfFragmentsIn_Object((1,3,6,1,4,1,10734,3,9,2,3,1,5),_TptNgfwPerfFragmentsIn_Type())
tptNgfwPerfFragmentsIn.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwPerfFragmentsIn.setStatus(_A)
_TptNgfwPerfFragmentsOut_Type=Counter64
_TptNgfwPerfFragmentsOut_Object=MibScalar
tptNgfwPerfFragmentsOut=_TptNgfwPerfFragmentsOut_Object((1,3,6,1,4,1,10734,3,9,2,3,1,6),_TptNgfwPerfFragmentsOut_Type())
tptNgfwPerfFragmentsOut.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwPerfFragmentsOut.setStatus(_A)
_TptNgfwPerfPacketDistTable_Object=MibTable
tptNgfwPerfPacketDistTable=_TptNgfwPerfPacketDistTable_Object((1,3,6,1,4,1,10734,3,9,2,3,1,7))
if mibBuilder.loadTexts:tptNgfwPerfPacketDistTable.setStatus(_A)
_TptNgfwPerfPacketDistEntry_Object=MibTableRow
tptNgfwPerfPacketDistEntry=_TptNgfwPerfPacketDistEntry_Object((1,3,6,1,4,1,10734,3,9,2,3,1,7,1))
tptNgfwPerfPacketDistEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:tptNgfwPerfPacketDistEntry.setStatus(_A)
_TptNgfwPerfPacketDistEntryIndex_Type=Unsigned32
_TptNgfwPerfPacketDistEntryIndex_Object=MibTableColumn
tptNgfwPerfPacketDistEntryIndex=_TptNgfwPerfPacketDistEntryIndex_Object((1,3,6,1,4,1,10734,3,9,2,3,1,7,1,1),_TptNgfwPerfPacketDistEntryIndex_Type())
tptNgfwPerfPacketDistEntryIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:tptNgfwPerfPacketDistEntryIndex.setStatus(_A)
_TptNgfwPerfPacketDistSizeGrp_Type=TptNgfwPerfPacketSizeGrouping
_TptNgfwPerfPacketDistSizeGrp_Object=MibTableColumn
tptNgfwPerfPacketDistSizeGrp=_TptNgfwPerfPacketDistSizeGrp_Object((1,3,6,1,4,1,10734,3,9,2,3,1,7,1,2),_TptNgfwPerfPacketDistSizeGrp_Type())
tptNgfwPerfPacketDistSizeGrp.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwPerfPacketDistSizeGrp.setStatus(_A)
_TptNgfwPerfPacketDistSizeGrpCount_Type=Counter64
_TptNgfwPerfPacketDistSizeGrpCount_Object=MibTableColumn
tptNgfwPerfPacketDistSizeGrpCount=_TptNgfwPerfPacketDistSizeGrpCount_Object((1,3,6,1,4,1,10734,3,9,2,3,1,7,1,3),_TptNgfwPerfPacketDistSizeGrpCount_Type())
tptNgfwPerfPacketDistSizeGrpCount.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwPerfPacketDistSizeGrpCount.setStatus(_A)
_TptNgfwPerfFWObjs_ObjectIdentity=ObjectIdentity
tptNgfwPerfFWObjs=_TptNgfwPerfFWObjs_ObjectIdentity((1,3,6,1,4,1,10734,3,9,2,3,2))
if mibBuilder.loadTexts:tptNgfwPerfFWObjs.setStatus(_A)
_TptNgfwPerfFWBlocks_Type=Counter64
_TptNgfwPerfFWBlocks_Object=MibScalar
tptNgfwPerfFWBlocks=_TptNgfwPerfFWBlocks_Object((1,3,6,1,4,1,10734,3,9,2,3,2,1),_TptNgfwPerfFWBlocks_Type())
tptNgfwPerfFWBlocks.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwPerfFWBlocks.setStatus(_A)
_TptNgfwPerfFWPermits_Type=Counter64
_TptNgfwPerfFWPermits_Object=MibScalar
tptNgfwPerfFWPermits=_TptNgfwPerfFWPermits_Object((1,3,6,1,4,1,10734,3,9,2,3,2,2),_TptNgfwPerfFWPermits_Type())
tptNgfwPerfFWPermits.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwPerfFWPermits.setStatus(_A)
_TptNgfwPerfFWSessions_Type=Counter64
_TptNgfwPerfFWSessions_Object=MibScalar
tptNgfwPerfFWSessions=_TptNgfwPerfFWSessions_Object((1,3,6,1,4,1,10734,3,9,2,3,2,3),_TptNgfwPerfFWSessions_Type())
tptNgfwPerfFWSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwPerfFWSessions.setStatus(_A)
_TptNgfwPerfIPSObjs_ObjectIdentity=ObjectIdentity
tptNgfwPerfIPSObjs=_TptNgfwPerfIPSObjs_ObjectIdentity((1,3,6,1,4,1,10734,3,9,2,3,3))
if mibBuilder.loadTexts:tptNgfwPerfIPSObjs.setStatus(_A)
_TptNgfwPerfIPSManagedStreams_Type=Counter64
_TptNgfwPerfIPSManagedStreams_Object=MibScalar
tptNgfwPerfIPSManagedStreams=_TptNgfwPerfIPSManagedStreams_Object((1,3,6,1,4,1,10734,3,9,2,3,3,1),_TptNgfwPerfIPSManagedStreams_Type())
tptNgfwPerfIPSManagedStreams.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwPerfIPSManagedStreams.setStatus(_A)
_TptNgfwPerfIPSQuarantineCount_Type=Counter64
_TptNgfwPerfIPSQuarantineCount_Object=MibScalar
tptNgfwPerfIPSQuarantineCount=_TptNgfwPerfIPSQuarantineCount_Object((1,3,6,1,4,1,10734,3,9,2,3,3,2),_TptNgfwPerfIPSQuarantineCount_Type())
tptNgfwPerfIPSQuarantineCount.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwPerfIPSQuarantineCount.setStatus(_A)
_TptNgfwPerfIPSRateLimitCount_Type=Counter64
_TptNgfwPerfIPSRateLimitCount_Object=MibScalar
tptNgfwPerfIPSRateLimitCount=_TptNgfwPerfIPSRateLimitCount_Object((1,3,6,1,4,1,10734,3,9,2,3,3,3),_TptNgfwPerfIPSRateLimitCount_Type())
tptNgfwPerfIPSRateLimitCount.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwPerfIPSRateLimitCount.setStatus(_A)
_TptNgfwPerfIPSAfcEntries_Type=Counter64
_TptNgfwPerfIPSAfcEntries_Object=MibScalar
tptNgfwPerfIPSAfcEntries=_TptNgfwPerfIPSAfcEntries_Object((1,3,6,1,4,1,10734,3,9,2,3,3,4),_TptNgfwPerfIPSAfcEntries_Type())
tptNgfwPerfIPSAfcEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwPerfIPSAfcEntries.setStatus(_A)
_TptNgfwPerfIPSAfcAppEntries_Type=Counter64
_TptNgfwPerfIPSAfcAppEntries_Object=MibScalar
tptNgfwPerfIPSAfcAppEntries=_TptNgfwPerfIPSAfcAppEntries_Object((1,3,6,1,4,1,10734,3,9,2,3,3,5),_TptNgfwPerfIPSAfcAppEntries_Type())
tptNgfwPerfIPSAfcAppEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwPerfIPSAfcAppEntries.setStatus(_A)
_TptNgfwPerfIPSBlockedStreams_Type=Counter64
_TptNgfwPerfIPSBlockedStreams_Object=MibScalar
tptNgfwPerfIPSBlockedStreams=_TptNgfwPerfIPSBlockedStreams_Object((1,3,6,1,4,1,10734,3,9,2,3,3,6),_TptNgfwPerfIPSBlockedStreams_Type())
tptNgfwPerfIPSBlockedStreams.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwPerfIPSBlockedStreams.setStatus(_A)
_TptNgfwPerfIPSTrustedStreams_Type=Counter64
_TptNgfwPerfIPSTrustedStreams_Object=MibScalar
tptNgfwPerfIPSTrustedStreams=_TptNgfwPerfIPSTrustedStreams_Object((1,3,6,1,4,1,10734,3,9,2,3,3,7),_TptNgfwPerfIPSTrustedStreams_Type())
tptNgfwPerfIPSTrustedStreams.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwPerfIPSTrustedStreams.setStatus(_A)
tptNgfwPerformanceGroup=ObjectGroup((1,3,6,1,4,1,10734,3,9,1,1,6))
tptNgfwPerformanceGroup.setObjects(*((_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:tptNgfwPerformanceGroup.setStatus(_A)
tptNgfwPerformanceCompl=ModuleCompliance((1,3,6,1,4,1,10734,3,9,1,2,3))
tptNgfwPerformanceCompl.setObjects((_B,_W))
if mibBuilder.loadTexts:tptNgfwPerformanceCompl.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'TptNgfwPerfPacketSizeGrouping':TptNgfwPerfPacketSizeGrouping,_W:tptNgfwPerformanceGroup,'tptNgfwPerformanceCompl':tptNgfwPerformanceCompl,'tptNgfwPerformance':tptNgfwPerformance,'tptNgfwPerformanceObjs':tptNgfwPerformanceObjs,_E:tptNgfwPerfPacketsIn,_F:tptNgfwPerfPacketsOut,_G:tptNgfwPerfBytesIn,_H:tptNgfwPerfBytesOut,_I:tptNgfwPerfFragmentsIn,_J:tptNgfwPerfFragmentsOut,'tptNgfwPerfPacketDistTable':tptNgfwPerfPacketDistTable,'tptNgfwPerfPacketDistEntry':tptNgfwPerfPacketDistEntry,_D:tptNgfwPerfPacketDistEntryIndex,_U:tptNgfwPerfPacketDistSizeGrp,_V:tptNgfwPerfPacketDistSizeGrpCount,'tptNgfwPerfFWObjs':tptNgfwPerfFWObjs,_K:tptNgfwPerfFWBlocks,_L:tptNgfwPerfFWPermits,_M:tptNgfwPerfFWSessions,'tptNgfwPerfIPSObjs':tptNgfwPerfIPSObjs,_N:tptNgfwPerfIPSManagedStreams,_O:tptNgfwPerfIPSQuarantineCount,_P:tptNgfwPerfIPSRateLimitCount,_Q:tptNgfwPerfIPSAfcEntries,_R:tptNgfwPerfIPSAfcAppEntries,_S:tptNgfwPerfIPSBlockedStreams,_T:tptNgfwPerfIPSTrustedStreams})