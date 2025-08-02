_U='fsPfcIndicationsRate3rdTime'
_T='fsPfcIndicationsRate3rd'
_S='fsPfcIndicationsRate2ndTime'
_R='fsPfcIndicationsRate2nd'
_Q='fsPfcIndicationsRate1stTime'
_P='fsPfcIndicationsRate1st'
_O='fsPfcIndicationsRate'
_N='fsPfcIndications'
_M='fsPfcRequestsRate3rdTime'
_L='fsPfcRequestsRate3rd'
_K='fsPfcRequestsRate2ndTime'
_J='fsPfcRequestsRate2nd'
_I='fsPfcRequestsRate1stTime'
_H='fsPfcRequestsRate1st'
_G='fsPfcRequestsRate'
_F='fsPfcRequests'
_E='fsPfcPriority'
_D='fsIfIndex'
_C='read-only'
_B='FS-PFC-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
ConfigStatus,IfIndex=mibBuilder.importSymbols('FS-TC','ConfigStatus','IfIndex')
InterfaceIndex,ifIndex=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','ifIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
fsPfcMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,157))
if mibBuilder.loadTexts:fsPfcMIB.setRevisions(('2017-12-18 00:00',))
_FsPfcCounterMIBObjects_ObjectIdentity=ObjectIdentity
fsPfcCounterMIBObjects=_FsPfcCounterMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,157,1))
_FsPfcIfPriorityCounterTable_Object=MibTable
fsPfcIfPriorityCounterTable=_FsPfcIfPriorityCounterTable_Object((1,3,6,1,4,1,52642,1,1,10,2,157,1,1))
if mibBuilder.loadTexts:fsPfcIfPriorityCounterTable.setStatus(_A)
_FsPfcIfPriorityCounterEntry_Object=MibTableRow
fsPfcIfPriorityCounterEntry=_FsPfcIfPriorityCounterEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,157,1,1,1))
fsPfcIfPriorityCounterEntry.setIndexNames((0,_B,_D),(0,_B,_E))
if mibBuilder.loadTexts:fsPfcIfPriorityCounterEntry.setStatus(_A)
_FsIfIndex_Type=IfIndex
_FsIfIndex_Object=MibTableColumn
fsIfIndex=_FsIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,157,1,1,1,1),_FsIfIndex_Type())
fsIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIfIndex.setStatus(_A)
_FsPfcPriority_Type=Integer32
_FsPfcPriority_Object=MibTableColumn
fsPfcPriority=_FsPfcPriority_Object((1,3,6,1,4,1,52642,1,1,10,2,157,1,1,1,2),_FsPfcPriority_Type())
fsPfcPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPfcPriority.setStatus(_A)
_FsPfcRequests_Type=Counter64
_FsPfcRequests_Object=MibTableColumn
fsPfcRequests=_FsPfcRequests_Object((1,3,6,1,4,1,52642,1,1,10,2,157,1,1,1,3),_FsPfcRequests_Type())
fsPfcRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPfcRequests.setStatus(_A)
_FsPfcRequestsRate_Type=Counter64
_FsPfcRequestsRate_Object=MibTableColumn
fsPfcRequestsRate=_FsPfcRequestsRate_Object((1,3,6,1,4,1,52642,1,1,10,2,157,1,1,1,4),_FsPfcRequestsRate_Type())
fsPfcRequestsRate.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPfcRequestsRate.setStatus(_A)
_FsPfcRequestsRate1st_Type=Counter64
_FsPfcRequestsRate1st_Object=MibTableColumn
fsPfcRequestsRate1st=_FsPfcRequestsRate1st_Object((1,3,6,1,4,1,52642,1,1,10,2,157,1,1,1,5),_FsPfcRequestsRate1st_Type())
fsPfcRequestsRate1st.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPfcRequestsRate1st.setStatus(_A)
_FsPfcRequestsRate1stTime_Type=DisplayString
_FsPfcRequestsRate1stTime_Object=MibTableColumn
fsPfcRequestsRate1stTime=_FsPfcRequestsRate1stTime_Object((1,3,6,1,4,1,52642,1,1,10,2,157,1,1,1,6),_FsPfcRequestsRate1stTime_Type())
fsPfcRequestsRate1stTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPfcRequestsRate1stTime.setStatus(_A)
_FsPfcRequestsRate2nd_Type=Counter64
_FsPfcRequestsRate2nd_Object=MibTableColumn
fsPfcRequestsRate2nd=_FsPfcRequestsRate2nd_Object((1,3,6,1,4,1,52642,1,1,10,2,157,1,1,1,7),_FsPfcRequestsRate2nd_Type())
fsPfcRequestsRate2nd.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPfcRequestsRate2nd.setStatus(_A)
_FsPfcRequestsRate2ndTime_Type=DisplayString
_FsPfcRequestsRate2ndTime_Object=MibTableColumn
fsPfcRequestsRate2ndTime=_FsPfcRequestsRate2ndTime_Object((1,3,6,1,4,1,52642,1,1,10,2,157,1,1,1,8),_FsPfcRequestsRate2ndTime_Type())
fsPfcRequestsRate2ndTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPfcRequestsRate2ndTime.setStatus(_A)
_FsPfcRequestsRate3rd_Type=Counter64
_FsPfcRequestsRate3rd_Object=MibTableColumn
fsPfcRequestsRate3rd=_FsPfcRequestsRate3rd_Object((1,3,6,1,4,1,52642,1,1,10,2,157,1,1,1,9),_FsPfcRequestsRate3rd_Type())
fsPfcRequestsRate3rd.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPfcRequestsRate3rd.setStatus(_A)
_FsPfcRequestsRate3rdTime_Type=DisplayString
_FsPfcRequestsRate3rdTime_Object=MibTableColumn
fsPfcRequestsRate3rdTime=_FsPfcRequestsRate3rdTime_Object((1,3,6,1,4,1,52642,1,1,10,2,157,1,1,1,10),_FsPfcRequestsRate3rdTime_Type())
fsPfcRequestsRate3rdTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPfcRequestsRate3rdTime.setStatus(_A)
_FsPfcIndications_Type=Counter64
_FsPfcIndications_Object=MibTableColumn
fsPfcIndications=_FsPfcIndications_Object((1,3,6,1,4,1,52642,1,1,10,2,157,1,1,1,11),_FsPfcIndications_Type())
fsPfcIndications.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPfcIndications.setStatus(_A)
_FsPfcIndicationsRate_Type=Counter64
_FsPfcIndicationsRate_Object=MibTableColumn
fsPfcIndicationsRate=_FsPfcIndicationsRate_Object((1,3,6,1,4,1,52642,1,1,10,2,157,1,1,1,12),_FsPfcIndicationsRate_Type())
fsPfcIndicationsRate.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPfcIndicationsRate.setStatus(_A)
_FsPfcIndicationsRate1st_Type=Counter64
_FsPfcIndicationsRate1st_Object=MibTableColumn
fsPfcIndicationsRate1st=_FsPfcIndicationsRate1st_Object((1,3,6,1,4,1,52642,1,1,10,2,157,1,1,1,13),_FsPfcIndicationsRate1st_Type())
fsPfcIndicationsRate1st.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPfcIndicationsRate1st.setStatus(_A)
_FsPfcIndicationsRate1stTime_Type=DisplayString
_FsPfcIndicationsRate1stTime_Object=MibTableColumn
fsPfcIndicationsRate1stTime=_FsPfcIndicationsRate1stTime_Object((1,3,6,1,4,1,52642,1,1,10,2,157,1,1,1,14),_FsPfcIndicationsRate1stTime_Type())
fsPfcIndicationsRate1stTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPfcIndicationsRate1stTime.setStatus(_A)
_FsPfcIndicationsRate2nd_Type=Counter64
_FsPfcIndicationsRate2nd_Object=MibTableColumn
fsPfcIndicationsRate2nd=_FsPfcIndicationsRate2nd_Object((1,3,6,1,4,1,52642,1,1,10,2,157,1,1,1,15),_FsPfcIndicationsRate2nd_Type())
fsPfcIndicationsRate2nd.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPfcIndicationsRate2nd.setStatus(_A)
_FsPfcIndicationsRate2ndTime_Type=DisplayString
_FsPfcIndicationsRate2ndTime_Object=MibTableColumn
fsPfcIndicationsRate2ndTime=_FsPfcIndicationsRate2ndTime_Object((1,3,6,1,4,1,52642,1,1,10,2,157,1,1,1,16),_FsPfcIndicationsRate2ndTime_Type())
fsPfcIndicationsRate2ndTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPfcIndicationsRate2ndTime.setStatus(_A)
_FsPfcIndicationsRate3rd_Type=Counter64
_FsPfcIndicationsRate3rd_Object=MibTableColumn
fsPfcIndicationsRate3rd=_FsPfcIndicationsRate3rd_Object((1,3,6,1,4,1,52642,1,1,10,2,157,1,1,1,17),_FsPfcIndicationsRate3rd_Type())
fsPfcIndicationsRate3rd.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPfcIndicationsRate3rd.setStatus(_A)
_FsPfcIndicationsRate3rdTime_Type=DisplayString
_FsPfcIndicationsRate3rdTime_Object=MibTableColumn
fsPfcIndicationsRate3rdTime=_FsPfcIndicationsRate3rdTime_Object((1,3,6,1,4,1,52642,1,1,10,2,157,1,1,1,18),_FsPfcIndicationsRate3rdTime_Type())
fsPfcIndicationsRate3rdTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPfcIndicationsRate3rdTime.setStatus(_A)
_FsPfcMIBConformance_ObjectIdentity=ObjectIdentity
fsPfcMIBConformance=_FsPfcMIBConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,157,2))
fsPfcIfPriorityCounterMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,157,2,1))
fsPfcIfPriorityCounterMIBGroup.setObjects(*((_B,_D),(_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:fsPfcIfPriorityCounterMIBGroup.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fsPfcMIB':fsPfcMIB,'fsPfcCounterMIBObjects':fsPfcCounterMIBObjects,'fsPfcIfPriorityCounterTable':fsPfcIfPriorityCounterTable,'fsPfcIfPriorityCounterEntry':fsPfcIfPriorityCounterEntry,_D:fsIfIndex,_E:fsPfcPriority,_F:fsPfcRequests,_G:fsPfcRequestsRate,_H:fsPfcRequestsRate1st,_I:fsPfcRequestsRate1stTime,_J:fsPfcRequestsRate2nd,_K:fsPfcRequestsRate2ndTime,_L:fsPfcRequestsRate3rd,_M:fsPfcRequestsRate3rdTime,_N:fsPfcIndications,_O:fsPfcIndicationsRate,_P:fsPfcIndicationsRate1st,_Q:fsPfcIndicationsRate1stTime,_R:fsPfcIndicationsRate2nd,_S:fsPfcIndicationsRate2ndTime,_T:fsPfcIndicationsRate3rd,_U:fsPfcIndicationsRate3rdTime,'fsPfcMIBConformance':fsPfcMIBConformance,'fsPfcIfPriorityCounterMIBGroup':fsPfcIfPriorityCounterMIBGroup})