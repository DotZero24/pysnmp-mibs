_b='altigaPppStatsGroup'
_a='alPppStatsGlobMppcOctRcvdUnComp'
_Z='alPppStatsGlobMppcOctRcvdAfterDeComp'
_Y='alPppStatsGlobMppcOctRcvdBeforeDeComp'
_X='alPppStatsGlobMppcOctSentUnComp'
_W='alPppStatsGlobMppcOctSentBeforeComp'
_V='alPppStatsGlobMppcOctSentAfterComp'
_U='alPppStatsGlobMppcMppeResetsSent'
_T='alPppStatsGlobMppcMppeResetsRcvd'
_S='alPppStatsMppcOctRcvdUnComp'
_R='alPppStatsMppcOctRcvdAfterDeComp'
_Q='alPppStatsMppcOctRcvdBeforeDeComp'
_P='alPppStatsMppcOctSentUnComp'
_O='alPppStatsMppcOctSentBeforeComp'
_N='alPppStatsMppcOctSentAfterComp'
_M='alPppStatsMppcMppeReset'
_L='alPppStatsMppeStatus'
_K='alPppStatsMppcStatus'
_J='alPppStatsPacketsRcvd'
_I='alPppStatsPacketsSent'
_H='alPppStatsOctetsRcvd'
_G='alPppStatsOctetsSent'
_F='alPppStatsRowStatus'
_E='Integer32'
_D='alPppStatsIfIndex'
_C='read-only'
_B='ALTIGA-PPP-STATS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
alPppMibModule,=mibBuilder.importSymbols('ALTIGA-GLOBAL-REG','alPppMibModule')
alPppGroup,alStatsPpp=mibBuilder.importSymbols('ALTIGA-MIB','alPppGroup','alStatsPpp')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
altigaPppStatsMibModule=ModuleIdentity((1,3,6,1,4,1,3076,1,1,11,2))
if mibBuilder.loadTexts:altigaPppStatsMibModule.setRevisions(('2002-09-05 13:00','2002-07-10 00:00'))
_AltigaPppStatsMibConformance_ObjectIdentity=ObjectIdentity
altigaPppStatsMibConformance=_AltigaPppStatsMibConformance_ObjectIdentity((1,3,6,1,4,1,3076,1,1,11,2,1))
_AltigaPppStatsMibCompliances_ObjectIdentity=ObjectIdentity
altigaPppStatsMibCompliances=_AltigaPppStatsMibCompliances_ObjectIdentity((1,3,6,1,4,1,3076,1,1,11,2,1,1))
_AlStatsPppGlobal_ObjectIdentity=ObjectIdentity
alStatsPppGlobal=_AlStatsPppGlobal_ObjectIdentity((1,3,6,1,4,1,3076,2,1,2,6,1))
_AlPppStatsTable_Object=MibTable
alPppStatsTable=_AlPppStatsTable_Object((1,3,6,1,4,1,3076,2,1,2,6,2))
if mibBuilder.loadTexts:alPppStatsTable.setStatus(_A)
_AlPppStatsEntry_Object=MibTableRow
alPppStatsEntry=_AlPppStatsEntry_Object((1,3,6,1,4,1,3076,2,1,2,6,2,1))
alPppStatsEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:alPppStatsEntry.setStatus(_A)
_AlPppStatsRowStatus_Type=RowStatus
_AlPppStatsRowStatus_Object=MibTableColumn
alPppStatsRowStatus=_AlPppStatsRowStatus_Object((1,3,6,1,4,1,3076,2,1,2,6,2,1,1),_AlPppStatsRowStatus_Type())
alPppStatsRowStatus.setMaxAccess('read-write')
if mibBuilder.loadTexts:alPppStatsRowStatus.setStatus(_A)
class _AlPppStatsIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AlPppStatsIfIndex_Type.__name__=_E
_AlPppStatsIfIndex_Object=MibTableColumn
alPppStatsIfIndex=_AlPppStatsIfIndex_Object((1,3,6,1,4,1,3076,2,1,2,6,2,1,2),_AlPppStatsIfIndex_Type())
alPppStatsIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:alPppStatsIfIndex.setStatus(_A)
_AlPppStatsOctetsSent_Type=Counter32
_AlPppStatsOctetsSent_Object=MibTableColumn
alPppStatsOctetsSent=_AlPppStatsOctetsSent_Object((1,3,6,1,4,1,3076,2,1,2,6,2,1,3),_AlPppStatsOctetsSent_Type())
alPppStatsOctetsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:alPppStatsOctetsSent.setStatus(_A)
_AlPppStatsOctetsRcvd_Type=Counter32
_AlPppStatsOctetsRcvd_Object=MibTableColumn
alPppStatsOctetsRcvd=_AlPppStatsOctetsRcvd_Object((1,3,6,1,4,1,3076,2,1,2,6,2,1,4),_AlPppStatsOctetsRcvd_Type())
alPppStatsOctetsRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:alPppStatsOctetsRcvd.setStatus(_A)
_AlPppStatsPacketsSent_Type=Counter32
_AlPppStatsPacketsSent_Object=MibTableColumn
alPppStatsPacketsSent=_AlPppStatsPacketsSent_Object((1,3,6,1,4,1,3076,2,1,2,6,2,1,5),_AlPppStatsPacketsSent_Type())
alPppStatsPacketsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:alPppStatsPacketsSent.setStatus(_A)
_AlPppStatsPacketsRcvd_Type=Counter32
_AlPppStatsPacketsRcvd_Object=MibTableColumn
alPppStatsPacketsRcvd=_AlPppStatsPacketsRcvd_Object((1,3,6,1,4,1,3076,2,1,2,6,2,1,6),_AlPppStatsPacketsRcvd_Type())
alPppStatsPacketsRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:alPppStatsPacketsRcvd.setStatus(_A)
_AlPppStatsMppcStatus_Type=TruthValue
_AlPppStatsMppcStatus_Object=MibTableColumn
alPppStatsMppcStatus=_AlPppStatsMppcStatus_Object((1,3,6,1,4,1,3076,2,1,2,6,2,1,7),_AlPppStatsMppcStatus_Type())
alPppStatsMppcStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:alPppStatsMppcStatus.setStatus(_A)
_AlPppStatsMppeStatus_Type=TruthValue
_AlPppStatsMppeStatus_Object=MibTableColumn
alPppStatsMppeStatus=_AlPppStatsMppeStatus_Object((1,3,6,1,4,1,3076,2,1,2,6,2,1,8),_AlPppStatsMppeStatus_Type())
alPppStatsMppeStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:alPppStatsMppeStatus.setStatus(_A)
_AlPppStatsMppcMppeReset_Type=Counter32
_AlPppStatsMppcMppeReset_Object=MibTableColumn
alPppStatsMppcMppeReset=_AlPppStatsMppcMppeReset_Object((1,3,6,1,4,1,3076,2,1,2,6,2,1,9),_AlPppStatsMppcMppeReset_Type())
alPppStatsMppcMppeReset.setMaxAccess(_C)
if mibBuilder.loadTexts:alPppStatsMppcMppeReset.setStatus(_A)
_AlPppStatsMppcOctSentAfterComp_Type=Counter32
_AlPppStatsMppcOctSentAfterComp_Object=MibTableColumn
alPppStatsMppcOctSentAfterComp=_AlPppStatsMppcOctSentAfterComp_Object((1,3,6,1,4,1,3076,2,1,2,6,2,1,10),_AlPppStatsMppcOctSentAfterComp_Type())
alPppStatsMppcOctSentAfterComp.setMaxAccess(_C)
if mibBuilder.loadTexts:alPppStatsMppcOctSentAfterComp.setStatus(_A)
_AlPppStatsMppcOctSentBeforeComp_Type=Counter32
_AlPppStatsMppcOctSentBeforeComp_Object=MibTableColumn
alPppStatsMppcOctSentBeforeComp=_AlPppStatsMppcOctSentBeforeComp_Object((1,3,6,1,4,1,3076,2,1,2,6,2,1,11),_AlPppStatsMppcOctSentBeforeComp_Type())
alPppStatsMppcOctSentBeforeComp.setMaxAccess(_C)
if mibBuilder.loadTexts:alPppStatsMppcOctSentBeforeComp.setStatus(_A)
_AlPppStatsMppcOctSentUnComp_Type=Counter32
_AlPppStatsMppcOctSentUnComp_Object=MibTableColumn
alPppStatsMppcOctSentUnComp=_AlPppStatsMppcOctSentUnComp_Object((1,3,6,1,4,1,3076,2,1,2,6,2,1,12),_AlPppStatsMppcOctSentUnComp_Type())
alPppStatsMppcOctSentUnComp.setMaxAccess(_C)
if mibBuilder.loadTexts:alPppStatsMppcOctSentUnComp.setStatus(_A)
_AlPppStatsMppcOctRcvdBeforeDeComp_Type=Counter32
_AlPppStatsMppcOctRcvdBeforeDeComp_Object=MibTableColumn
alPppStatsMppcOctRcvdBeforeDeComp=_AlPppStatsMppcOctRcvdBeforeDeComp_Object((1,3,6,1,4,1,3076,2,1,2,6,2,1,13),_AlPppStatsMppcOctRcvdBeforeDeComp_Type())
alPppStatsMppcOctRcvdBeforeDeComp.setMaxAccess(_C)
if mibBuilder.loadTexts:alPppStatsMppcOctRcvdBeforeDeComp.setStatus(_A)
_AlPppStatsMppcOctRcvdAfterDeComp_Type=Counter32
_AlPppStatsMppcOctRcvdAfterDeComp_Object=MibTableColumn
alPppStatsMppcOctRcvdAfterDeComp=_AlPppStatsMppcOctRcvdAfterDeComp_Object((1,3,6,1,4,1,3076,2,1,2,6,2,1,14),_AlPppStatsMppcOctRcvdAfterDeComp_Type())
alPppStatsMppcOctRcvdAfterDeComp.setMaxAccess(_C)
if mibBuilder.loadTexts:alPppStatsMppcOctRcvdAfterDeComp.setStatus(_A)
_AlPppStatsMppcOctRcvdUnComp_Type=Counter32
_AlPppStatsMppcOctRcvdUnComp_Object=MibTableColumn
alPppStatsMppcOctRcvdUnComp=_AlPppStatsMppcOctRcvdUnComp_Object((1,3,6,1,4,1,3076,2,1,2,6,2,1,15),_AlPppStatsMppcOctRcvdUnComp_Type())
alPppStatsMppcOctRcvdUnComp.setMaxAccess(_C)
if mibBuilder.loadTexts:alPppStatsMppcOctRcvdUnComp.setStatus(_A)
_AlStatsPppMppcGlobal_ObjectIdentity=ObjectIdentity
alStatsPppMppcGlobal=_AlStatsPppMppcGlobal_ObjectIdentity((1,3,6,1,4,1,3076,2,1,2,6,3))
_AlPppStatsGlobMppcMppeResetsRcvd_Type=Counter32
_AlPppStatsGlobMppcMppeResetsRcvd_Object=MibScalar
alPppStatsGlobMppcMppeResetsRcvd=_AlPppStatsGlobMppcMppeResetsRcvd_Object((1,3,6,1,4,1,3076,2,1,2,6,3,1),_AlPppStatsGlobMppcMppeResetsRcvd_Type())
alPppStatsGlobMppcMppeResetsRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:alPppStatsGlobMppcMppeResetsRcvd.setStatus(_A)
_AlPppStatsGlobMppcMppeResetsSent_Type=Counter32
_AlPppStatsGlobMppcMppeResetsSent_Object=MibScalar
alPppStatsGlobMppcMppeResetsSent=_AlPppStatsGlobMppcMppeResetsSent_Object((1,3,6,1,4,1,3076,2,1,2,6,3,2),_AlPppStatsGlobMppcMppeResetsSent_Type())
alPppStatsGlobMppcMppeResetsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:alPppStatsGlobMppcMppeResetsSent.setStatus(_A)
_AlPppStatsGlobMppcOctSentAfterComp_Type=Counter32
_AlPppStatsGlobMppcOctSentAfterComp_Object=MibScalar
alPppStatsGlobMppcOctSentAfterComp=_AlPppStatsGlobMppcOctSentAfterComp_Object((1,3,6,1,4,1,3076,2,1,2,6,3,3),_AlPppStatsGlobMppcOctSentAfterComp_Type())
alPppStatsGlobMppcOctSentAfterComp.setMaxAccess(_C)
if mibBuilder.loadTexts:alPppStatsGlobMppcOctSentAfterComp.setStatus(_A)
_AlPppStatsGlobMppcOctSentBeforeComp_Type=Counter32
_AlPppStatsGlobMppcOctSentBeforeComp_Object=MibScalar
alPppStatsGlobMppcOctSentBeforeComp=_AlPppStatsGlobMppcOctSentBeforeComp_Object((1,3,6,1,4,1,3076,2,1,2,6,3,4),_AlPppStatsGlobMppcOctSentBeforeComp_Type())
alPppStatsGlobMppcOctSentBeforeComp.setMaxAccess(_C)
if mibBuilder.loadTexts:alPppStatsGlobMppcOctSentBeforeComp.setStatus(_A)
_AlPppStatsGlobMppcOctSentUnComp_Type=Counter32
_AlPppStatsGlobMppcOctSentUnComp_Object=MibScalar
alPppStatsGlobMppcOctSentUnComp=_AlPppStatsGlobMppcOctSentUnComp_Object((1,3,6,1,4,1,3076,2,1,2,6,3,5),_AlPppStatsGlobMppcOctSentUnComp_Type())
alPppStatsGlobMppcOctSentUnComp.setMaxAccess(_C)
if mibBuilder.loadTexts:alPppStatsGlobMppcOctSentUnComp.setStatus(_A)
_AlPppStatsGlobMppcOctRcvdBeforeDeComp_Type=Counter32
_AlPppStatsGlobMppcOctRcvdBeforeDeComp_Object=MibScalar
alPppStatsGlobMppcOctRcvdBeforeDeComp=_AlPppStatsGlobMppcOctRcvdBeforeDeComp_Object((1,3,6,1,4,1,3076,2,1,2,6,3,6),_AlPppStatsGlobMppcOctRcvdBeforeDeComp_Type())
alPppStatsGlobMppcOctRcvdBeforeDeComp.setMaxAccess(_C)
if mibBuilder.loadTexts:alPppStatsGlobMppcOctRcvdBeforeDeComp.setStatus(_A)
_AlPppStatsGlobMppcOctRcvdAfterDeComp_Type=Counter32
_AlPppStatsGlobMppcOctRcvdAfterDeComp_Object=MibScalar
alPppStatsGlobMppcOctRcvdAfterDeComp=_AlPppStatsGlobMppcOctRcvdAfterDeComp_Object((1,3,6,1,4,1,3076,2,1,2,6,3,7),_AlPppStatsGlobMppcOctRcvdAfterDeComp_Type())
alPppStatsGlobMppcOctRcvdAfterDeComp.setMaxAccess(_C)
if mibBuilder.loadTexts:alPppStatsGlobMppcOctRcvdAfterDeComp.setStatus(_A)
_AlPppStatsGlobMppcOctRcvdUnComp_Type=Counter32
_AlPppStatsGlobMppcOctRcvdUnComp_Object=MibScalar
alPppStatsGlobMppcOctRcvdUnComp=_AlPppStatsGlobMppcOctRcvdUnComp_Object((1,3,6,1,4,1,3076,2,1,2,6,3,8),_AlPppStatsGlobMppcOctRcvdUnComp_Type())
alPppStatsGlobMppcOctRcvdUnComp.setMaxAccess(_C)
if mibBuilder.loadTexts:alPppStatsGlobMppcOctRcvdUnComp.setStatus(_A)
altigaPppStatsGroup=ObjectGroup((1,3,6,1,4,1,3076,2,1,1,1,6,2))
altigaPppStatsGroup.setObjects(*((_B,_F),(_B,_D),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:altigaPppStatsGroup.setStatus(_A)
altigaPppStatsMibCompliance=ModuleCompliance((1,3,6,1,4,1,3076,1,1,11,2,1,1,1))
altigaPppStatsMibCompliance.setObjects((_B,_b))
if mibBuilder.loadTexts:altigaPppStatsMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'altigaPppStatsMibModule':altigaPppStatsMibModule,'altigaPppStatsMibConformance':altigaPppStatsMibConformance,'altigaPppStatsMibCompliances':altigaPppStatsMibCompliances,'altigaPppStatsMibCompliance':altigaPppStatsMibCompliance,_b:altigaPppStatsGroup,'alStatsPppGlobal':alStatsPppGlobal,'alPppStatsTable':alPppStatsTable,'alPppStatsEntry':alPppStatsEntry,_F:alPppStatsRowStatus,_D:alPppStatsIfIndex,_G:alPppStatsOctetsSent,_H:alPppStatsOctetsRcvd,_I:alPppStatsPacketsSent,_J:alPppStatsPacketsRcvd,_K:alPppStatsMppcStatus,_L:alPppStatsMppeStatus,_M:alPppStatsMppcMppeReset,_N:alPppStatsMppcOctSentAfterComp,_O:alPppStatsMppcOctSentBeforeComp,_P:alPppStatsMppcOctSentUnComp,_Q:alPppStatsMppcOctRcvdBeforeDeComp,_R:alPppStatsMppcOctRcvdAfterDeComp,_S:alPppStatsMppcOctRcvdUnComp,'alStatsPppMppcGlobal':alStatsPppMppcGlobal,_T:alPppStatsGlobMppcMppeResetsRcvd,_U:alPppStatsGlobMppcMppeResetsSent,_V:alPppStatsGlobMppcOctSentAfterComp,_W:alPppStatsGlobMppcOctSentBeforeComp,_X:alPppStatsGlobMppcOctSentUnComp,_Y:alPppStatsGlobMppcOctRcvdBeforeDeComp,_Z:alPppStatsGlobMppcOctRcvdAfterDeComp,_a:alPppStatsGlobMppcOctRcvdUnComp})