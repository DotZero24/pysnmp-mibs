_I='fsIgmpCacheIfIndex'
_H='fsIgmpCacheAddress'
_G='fsIgmpInterfaceIfIndex'
_F='not-accessible'
_E='SUPERMICRO-IGMP-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
fsigmpMIB=ModuleIdentity((1,3,6,1,4,1,10876,101,1,36))
if mibBuilder.loadTexts:fsigmpMIB.setRevisions(('2012-09-05 00:00',))
_Fsigmp_ObjectIdentity=ObjectIdentity
fsigmp=_Fsigmp_ObjectIdentity((1,3,6,1,4,1,10876,101,1,36,1))
class _FsIgmpGlobalStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_FsIgmpGlobalStatus_Type.__name__=_C
_FsIgmpGlobalStatus_Object=MibScalar
fsIgmpGlobalStatus=_FsIgmpGlobalStatus_Object((1,3,6,1,4,1,10876,101,1,36,1,1),_FsIgmpGlobalStatus_Type())
fsIgmpGlobalStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIgmpGlobalStatus.setStatus(_A)
class _FsIgmpTraceLevel_Type(Integer32):defaultValue=0
_FsIgmpTraceLevel_Type.__name__=_C
_FsIgmpTraceLevel_Object=MibScalar
fsIgmpTraceLevel=_FsIgmpTraceLevel_Object((1,3,6,1,4,1,10876,101,1,36,1,2),_FsIgmpTraceLevel_Type())
fsIgmpTraceLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIgmpTraceLevel.setStatus(_A)
_FsIgmpInterfaceTable_Object=MibTable
fsIgmpInterfaceTable=_FsIgmpInterfaceTable_Object((1,3,6,1,4,1,10876,101,1,36,1,3))
if mibBuilder.loadTexts:fsIgmpInterfaceTable.setStatus(_A)
_FsIgmpInterfaceEntry_Object=MibTableRow
fsIgmpInterfaceEntry=_FsIgmpInterfaceEntry_Object((1,3,6,1,4,1,10876,101,1,36,1,3,1))
fsIgmpInterfaceEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:fsIgmpInterfaceEntry.setStatus(_A)
_FsIgmpInterfaceIfIndex_Type=InterfaceIndex
_FsIgmpInterfaceIfIndex_Object=MibTableColumn
fsIgmpInterfaceIfIndex=_FsIgmpInterfaceIfIndex_Object((1,3,6,1,4,1,10876,101,1,36,1,3,1,1),_FsIgmpInterfaceIfIndex_Type())
fsIgmpInterfaceIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fsIgmpInterfaceIfIndex.setStatus(_A)
class _FsIgmpInterfaceAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_FsIgmpInterfaceAdminStatus_Type.__name__=_C
_FsIgmpInterfaceAdminStatus_Object=MibTableColumn
fsIgmpInterfaceAdminStatus=_FsIgmpInterfaceAdminStatus_Object((1,3,6,1,4,1,10876,101,1,36,1,3,1,2),_FsIgmpInterfaceAdminStatus_Type())
fsIgmpInterfaceAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIgmpInterfaceAdminStatus.setStatus(_A)
class _FsIgmpInterfaceFastLeaveStatus_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disable',0),('enable',1)))
_FsIgmpInterfaceFastLeaveStatus_Type.__name__=_C
_FsIgmpInterfaceFastLeaveStatus_Object=MibTableColumn
fsIgmpInterfaceFastLeaveStatus=_FsIgmpInterfaceFastLeaveStatus_Object((1,3,6,1,4,1,10876,101,1,36,1,3,1,3),_FsIgmpInterfaceFastLeaveStatus_Type())
fsIgmpInterfaceFastLeaveStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIgmpInterfaceFastLeaveStatus.setStatus(_A)
class _FsIgmpInterfaceOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_FsIgmpInterfaceOperStatus_Type.__name__=_C
_FsIgmpInterfaceOperStatus_Object=MibTableColumn
fsIgmpInterfaceOperStatus=_FsIgmpInterfaceOperStatus_Object((1,3,6,1,4,1,10876,101,1,36,1,3,1,4),_FsIgmpInterfaceOperStatus_Type())
fsIgmpInterfaceOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIgmpInterfaceOperStatus.setStatus(_A)
_FsIgmpInterfaceIncomingPkts_Type=Counter32
_FsIgmpInterfaceIncomingPkts_Object=MibTableColumn
fsIgmpInterfaceIncomingPkts=_FsIgmpInterfaceIncomingPkts_Object((1,3,6,1,4,1,10876,101,1,36,1,3,1,5),_FsIgmpInterfaceIncomingPkts_Type())
fsIgmpInterfaceIncomingPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIgmpInterfaceIncomingPkts.setStatus(_A)
_FsIgmpInterfaceIncomingJoins_Type=Counter32
_FsIgmpInterfaceIncomingJoins_Object=MibTableColumn
fsIgmpInterfaceIncomingJoins=_FsIgmpInterfaceIncomingJoins_Object((1,3,6,1,4,1,10876,101,1,36,1,3,1,6),_FsIgmpInterfaceIncomingJoins_Type())
fsIgmpInterfaceIncomingJoins.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIgmpInterfaceIncomingJoins.setStatus(_A)
_FsIgmpInterfaceIncomingLeaves_Type=Counter32
_FsIgmpInterfaceIncomingLeaves_Object=MibTableColumn
fsIgmpInterfaceIncomingLeaves=_FsIgmpInterfaceIncomingLeaves_Object((1,3,6,1,4,1,10876,101,1,36,1,3,1,7),_FsIgmpInterfaceIncomingLeaves_Type())
fsIgmpInterfaceIncomingLeaves.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIgmpInterfaceIncomingLeaves.setStatus(_A)
_FsIgmpInterfaceIncomingQueries_Type=Counter32
_FsIgmpInterfaceIncomingQueries_Object=MibTableColumn
fsIgmpInterfaceIncomingQueries=_FsIgmpInterfaceIncomingQueries_Object((1,3,6,1,4,1,10876,101,1,36,1,3,1,8),_FsIgmpInterfaceIncomingQueries_Type())
fsIgmpInterfaceIncomingQueries.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIgmpInterfaceIncomingQueries.setStatus(_A)
_FsIgmpInterfaceOutgoingQueries_Type=Counter32
_FsIgmpInterfaceOutgoingQueries_Object=MibTableColumn
fsIgmpInterfaceOutgoingQueries=_FsIgmpInterfaceOutgoingQueries_Object((1,3,6,1,4,1,10876,101,1,36,1,3,1,9),_FsIgmpInterfaceOutgoingQueries_Type())
fsIgmpInterfaceOutgoingQueries.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIgmpInterfaceOutgoingQueries.setStatus(_A)
_FsIgmpInterfaceRxGenQueries_Type=Counter32
_FsIgmpInterfaceRxGenQueries_Object=MibTableColumn
fsIgmpInterfaceRxGenQueries=_FsIgmpInterfaceRxGenQueries_Object((1,3,6,1,4,1,10876,101,1,36,1,3,1,10),_FsIgmpInterfaceRxGenQueries_Type())
fsIgmpInterfaceRxGenQueries.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIgmpInterfaceRxGenQueries.setStatus(_A)
_FsIgmpInterfaceRxGrpQueries_Type=Counter32
_FsIgmpInterfaceRxGrpQueries_Object=MibTableColumn
fsIgmpInterfaceRxGrpQueries=_FsIgmpInterfaceRxGrpQueries_Object((1,3,6,1,4,1,10876,101,1,36,1,3,1,11),_FsIgmpInterfaceRxGrpQueries_Type())
fsIgmpInterfaceRxGrpQueries.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIgmpInterfaceRxGrpQueries.setStatus(_A)
_FsIgmpInterfaceRxGrpAndSrcQueries_Type=Counter32
_FsIgmpInterfaceRxGrpAndSrcQueries_Object=MibTableColumn
fsIgmpInterfaceRxGrpAndSrcQueries=_FsIgmpInterfaceRxGrpAndSrcQueries_Object((1,3,6,1,4,1,10876,101,1,36,1,3,1,12),_FsIgmpInterfaceRxGrpAndSrcQueries_Type())
fsIgmpInterfaceRxGrpAndSrcQueries.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIgmpInterfaceRxGrpAndSrcQueries.setStatus(_A)
_FsIgmpInterfaceRxv1v2Reports_Type=Counter32
_FsIgmpInterfaceRxv1v2Reports_Object=MibTableColumn
fsIgmpInterfaceRxv1v2Reports=_FsIgmpInterfaceRxv1v2Reports_Object((1,3,6,1,4,1,10876,101,1,36,1,3,1,13),_FsIgmpInterfaceRxv1v2Reports_Type())
fsIgmpInterfaceRxv1v2Reports.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIgmpInterfaceRxv1v2Reports.setStatus(_A)
_FsIgmpInterfaceRxv3Reports_Type=Counter32
_FsIgmpInterfaceRxv3Reports_Object=MibTableColumn
fsIgmpInterfaceRxv3Reports=_FsIgmpInterfaceRxv3Reports_Object((1,3,6,1,4,1,10876,101,1,36,1,3,1,14),_FsIgmpInterfaceRxv3Reports_Type())
fsIgmpInterfaceRxv3Reports.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIgmpInterfaceRxv3Reports.setStatus(_A)
_FsIgmpInterfaceTxGenQueries_Type=Counter32
_FsIgmpInterfaceTxGenQueries_Object=MibTableColumn
fsIgmpInterfaceTxGenQueries=_FsIgmpInterfaceTxGenQueries_Object((1,3,6,1,4,1,10876,101,1,36,1,3,1,15),_FsIgmpInterfaceTxGenQueries_Type())
fsIgmpInterfaceTxGenQueries.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIgmpInterfaceTxGenQueries.setStatus(_A)
_FsIgmpInterfaceTxGrpQueries_Type=Counter32
_FsIgmpInterfaceTxGrpQueries_Object=MibTableColumn
fsIgmpInterfaceTxGrpQueries=_FsIgmpInterfaceTxGrpQueries_Object((1,3,6,1,4,1,10876,101,1,36,1,3,1,16),_FsIgmpInterfaceTxGrpQueries_Type())
fsIgmpInterfaceTxGrpQueries.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIgmpInterfaceTxGrpQueries.setStatus(_A)
_FsIgmpInterfaceTxGrpAndSrcQueries_Type=Counter32
_FsIgmpInterfaceTxGrpAndSrcQueries_Object=MibTableColumn
fsIgmpInterfaceTxGrpAndSrcQueries=_FsIgmpInterfaceTxGrpAndSrcQueries_Object((1,3,6,1,4,1,10876,101,1,36,1,3,1,17),_FsIgmpInterfaceTxGrpAndSrcQueries_Type())
fsIgmpInterfaceTxGrpAndSrcQueries.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIgmpInterfaceTxGrpAndSrcQueries.setStatus(_A)
_FsIgmpInterfaceTxv1v2Reports_Type=Counter32
_FsIgmpInterfaceTxv1v2Reports_Object=MibTableColumn
fsIgmpInterfaceTxv1v2Reports=_FsIgmpInterfaceTxv1v2Reports_Object((1,3,6,1,4,1,10876,101,1,36,1,3,1,18),_FsIgmpInterfaceTxv1v2Reports_Type())
fsIgmpInterfaceTxv1v2Reports.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIgmpInterfaceTxv1v2Reports.setStatus(_A)
_FsIgmpInterfaceTxv3Reports_Type=Counter32
_FsIgmpInterfaceTxv3Reports_Object=MibTableColumn
fsIgmpInterfaceTxv3Reports=_FsIgmpInterfaceTxv3Reports_Object((1,3,6,1,4,1,10876,101,1,36,1,3,1,19),_FsIgmpInterfaceTxv3Reports_Type())
fsIgmpInterfaceTxv3Reports.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIgmpInterfaceTxv3Reports.setStatus(_A)
_FsIgmpInterfaceTxv2Leaves_Type=Counter32
_FsIgmpInterfaceTxv2Leaves_Object=MibTableColumn
fsIgmpInterfaceTxv2Leaves=_FsIgmpInterfaceTxv2Leaves_Object((1,3,6,1,4,1,10876,101,1,36,1,3,1,20),_FsIgmpInterfaceTxv2Leaves_Type())
fsIgmpInterfaceTxv2Leaves.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIgmpInterfaceTxv2Leaves.setStatus(_A)
_FsIgmpCacheTable_Object=MibTable
fsIgmpCacheTable=_FsIgmpCacheTable_Object((1,3,6,1,4,1,10876,101,1,36,1,4))
if mibBuilder.loadTexts:fsIgmpCacheTable.setStatus(_A)
_FsIgmpCacheEntry_Object=MibTableRow
fsIgmpCacheEntry=_FsIgmpCacheEntry_Object((1,3,6,1,4,1,10876,101,1,36,1,4,1))
fsIgmpCacheEntry.setIndexNames((0,_E,_H),(0,_E,_I))
if mibBuilder.loadTexts:fsIgmpCacheEntry.setStatus(_A)
_FsIgmpCacheAddress_Type=IpAddress
_FsIgmpCacheAddress_Object=MibTableColumn
fsIgmpCacheAddress=_FsIgmpCacheAddress_Object((1,3,6,1,4,1,10876,101,1,36,1,4,1,1),_FsIgmpCacheAddress_Type())
fsIgmpCacheAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:fsIgmpCacheAddress.setStatus(_A)
_FsIgmpCacheIfIndex_Type=InterfaceIndex
_FsIgmpCacheIfIndex_Object=MibTableColumn
fsIgmpCacheIfIndex=_FsIgmpCacheIfIndex_Object((1,3,6,1,4,1,10876,101,1,36,1,4,1,2),_FsIgmpCacheIfIndex_Type())
fsIgmpCacheIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fsIgmpCacheIfIndex.setStatus(_A)
_FsIgmpCacheGroupCompMode_Type=Integer32
_FsIgmpCacheGroupCompMode_Object=MibTableColumn
fsIgmpCacheGroupCompMode=_FsIgmpCacheGroupCompMode_Object((1,3,6,1,4,1,10876,101,1,36,1,4,1,3),_FsIgmpCacheGroupCompMode_Type())
fsIgmpCacheGroupCompMode.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIgmpCacheGroupCompMode.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'fsigmpMIB':fsigmpMIB,'fsigmp':fsigmp,'fsIgmpGlobalStatus':fsIgmpGlobalStatus,'fsIgmpTraceLevel':fsIgmpTraceLevel,'fsIgmpInterfaceTable':fsIgmpInterfaceTable,'fsIgmpInterfaceEntry':fsIgmpInterfaceEntry,_G:fsIgmpInterfaceIfIndex,'fsIgmpInterfaceAdminStatus':fsIgmpInterfaceAdminStatus,'fsIgmpInterfaceFastLeaveStatus':fsIgmpInterfaceFastLeaveStatus,'fsIgmpInterfaceOperStatus':fsIgmpInterfaceOperStatus,'fsIgmpInterfaceIncomingPkts':fsIgmpInterfaceIncomingPkts,'fsIgmpInterfaceIncomingJoins':fsIgmpInterfaceIncomingJoins,'fsIgmpInterfaceIncomingLeaves':fsIgmpInterfaceIncomingLeaves,'fsIgmpInterfaceIncomingQueries':fsIgmpInterfaceIncomingQueries,'fsIgmpInterfaceOutgoingQueries':fsIgmpInterfaceOutgoingQueries,'fsIgmpInterfaceRxGenQueries':fsIgmpInterfaceRxGenQueries,'fsIgmpInterfaceRxGrpQueries':fsIgmpInterfaceRxGrpQueries,'fsIgmpInterfaceRxGrpAndSrcQueries':fsIgmpInterfaceRxGrpAndSrcQueries,'fsIgmpInterfaceRxv1v2Reports':fsIgmpInterfaceRxv1v2Reports,'fsIgmpInterfaceRxv3Reports':fsIgmpInterfaceRxv3Reports,'fsIgmpInterfaceTxGenQueries':fsIgmpInterfaceTxGenQueries,'fsIgmpInterfaceTxGrpQueries':fsIgmpInterfaceTxGrpQueries,'fsIgmpInterfaceTxGrpAndSrcQueries':fsIgmpInterfaceTxGrpAndSrcQueries,'fsIgmpInterfaceTxv1v2Reports':fsIgmpInterfaceTxv1v2Reports,'fsIgmpInterfaceTxv3Reports':fsIgmpInterfaceTxv3Reports,'fsIgmpInterfaceTxv2Leaves':fsIgmpInterfaceTxv2Leaves,'fsIgmpCacheTable':fsIgmpCacheTable,'fsIgmpCacheEntry':fsIgmpCacheEntry,_H:fsIgmpCacheAddress,_I:fsIgmpCacheIfIndex,'fsIgmpCacheGroupCompMode':fsIgmpCacheGroupCompMode})