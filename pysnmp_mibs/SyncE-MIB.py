_J='fsSynceIfIndex'
_I='not-accessible'
_H='fsSynceContextId'
_G='SyncE-MIB'
_F='TruthValue'
_E='Unsigned32'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_F)
fsSynceMIB=ModuleIdentity((1,3,6,1,4,1,10876,101,2,79))
if mibBuilder.loadTexts:fsSynceMIB.setRevisions(('2013-02-15 00:00',))
_FsSynceObjects_ObjectIdentity=ObjectIdentity
fsSynceObjects=_FsSynceObjects_ObjectIdentity((1,3,6,1,4,1,10876,101,2,79,1))
_FsSynceGeneralGroup_ObjectIdentity=ObjectIdentity
fsSynceGeneralGroup=_FsSynceGeneralGroup_ObjectIdentity((1,3,6,1,4,1,10876,101,2,79,1,1))
class _FsSynceGlobalSysCtrl_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('start',1),('shutdown',2)))
_FsSynceGlobalSysCtrl_Type.__name__=_C
_FsSynceGlobalSysCtrl_Object=MibScalar
fsSynceGlobalSysCtrl=_FsSynceGlobalSysCtrl_Object((1,3,6,1,4,1,10876,101,2,79,1,1,1),_FsSynceGlobalSysCtrl_Type())
fsSynceGlobalSysCtrl.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSynceGlobalSysCtrl.setStatus(_A)
_FsSynceTable_Object=MibTable
fsSynceTable=_FsSynceTable_Object((1,3,6,1,4,1,10876,101,2,79,1,1,2))
if mibBuilder.loadTexts:fsSynceTable.setStatus(_A)
_FsSynceEntry_Object=MibTableRow
fsSynceEntry=_FsSynceEntry_Object((1,3,6,1,4,1,10876,101,2,79,1,1,2,1))
fsSynceEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:fsSynceEntry.setStatus(_A)
class _FsSynceContextId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsSynceContextId_Type.__name__=_C
_FsSynceContextId_Object=MibTableColumn
fsSynceContextId=_FsSynceContextId_Object((1,3,6,1,4,1,10876,101,2,79,1,1,2,1,1),_FsSynceContextId_Type())
fsSynceContextId.setMaxAccess(_I)
if mibBuilder.loadTexts:fsSynceContextId.setStatus(_A)
class _FsSynceTraceOption_Type(Unsigned32):defaultValue=64
_FsSynceTraceOption_Type.__name__=_E
_FsSynceTraceOption_Object=MibTableColumn
fsSynceTraceOption=_FsSynceTraceOption_Object((1,3,6,1,4,1,10876,101,2,79,1,1,2,1,2),_FsSynceTraceOption_Type())
fsSynceTraceOption.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSynceTraceOption.setStatus(_A)
class _FsSynceQLMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disabled',0),('enabled',1)))
_FsSynceQLMode_Type.__name__=_C
_FsSynceQLMode_Object=MibTableColumn
fsSynceQLMode=_FsSynceQLMode_Object((1,3,6,1,4,1,10876,101,2,79,1,1,2,1,3),_FsSynceQLMode_Type())
fsSynceQLMode.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSynceQLMode.setStatus(_A)
class _FsSynceQLValue_Type(Unsigned32):defaultValue=15
_FsSynceQLValue_Type.__name__=_E
_FsSynceQLValue_Object=MibTableColumn
fsSynceQLValue=_FsSynceQLValue_Object((1,3,6,1,4,1,10876,101,2,79,1,1,2,1,4),_FsSynceQLValue_Type())
fsSynceQLValue.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSynceQLValue.setStatus(_A)
class _FsSynceSSMOptionMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('option1',1),('option2Gen1',2),('option2Gen2',3)))
_FsSynceSSMOptionMode_Type.__name__=_C
_FsSynceSSMOptionMode_Object=MibTableColumn
fsSynceSSMOptionMode=_FsSynceSSMOptionMode_Object((1,3,6,1,4,1,10876,101,2,79,1,1,2,1,5),_FsSynceSSMOptionMode_Type())
fsSynceSSMOptionMode.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSynceSSMOptionMode.setStatus(_A)
_FsSynceSelectedInterface_Type=InterfaceIndex
_FsSynceSelectedInterface_Object=MibTableColumn
fsSynceSelectedInterface=_FsSynceSelectedInterface_Object((1,3,6,1,4,1,10876,101,2,79,1,1,2,1,6),_FsSynceSelectedInterface_Type())
fsSynceSelectedInterface.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSynceSelectedInterface.setStatus(_A)
_FsSynceContextRowStatus_Type=RowStatus
_FsSynceContextRowStatus_Object=MibTableColumn
fsSynceContextRowStatus=_FsSynceContextRowStatus_Object((1,3,6,1,4,1,10876,101,2,79,1,1,2,1,7),_FsSynceContextRowStatus_Type())
fsSynceContextRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSynceContextRowStatus.setStatus(_A)
_FsSynceInterfaceConfiguration_ObjectIdentity=ObjectIdentity
fsSynceInterfaceConfiguration=_FsSynceInterfaceConfiguration_ObjectIdentity((1,3,6,1,4,1,10876,101,2,79,1,2))
_FsSynceIfTable_Object=MibTable
fsSynceIfTable=_FsSynceIfTable_Object((1,3,6,1,4,1,10876,101,2,79,1,2,1))
if mibBuilder.loadTexts:fsSynceIfTable.setStatus(_A)
_FsSynceIfEntry_Object=MibTableRow
fsSynceIfEntry=_FsSynceIfEntry_Object((1,3,6,1,4,1,10876,101,2,79,1,2,1,1))
fsSynceIfEntry.setIndexNames((0,_G,_J))
if mibBuilder.loadTexts:fsSynceIfEntry.setStatus(_A)
_FsSynceIfIndex_Type=InterfaceIndex
_FsSynceIfIndex_Object=MibTableColumn
fsSynceIfIndex=_FsSynceIfIndex_Object((1,3,6,1,4,1,10876,101,2,79,1,2,1,1,1),_FsSynceIfIndex_Type())
fsSynceIfIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:fsSynceIfIndex.setStatus(_A)
class _FsSynceIfSynceMode_Type(TruthValue):defaultValue=2
_FsSynceIfSynceMode_Type.__name__=_F
_FsSynceIfSynceMode_Object=MibTableColumn
fsSynceIfSynceMode=_FsSynceIfSynceMode_Object((1,3,6,1,4,1,10876,101,2,79,1,2,1,1,2),_FsSynceIfSynceMode_Type())
fsSynceIfSynceMode.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSynceIfSynceMode.setStatus(_A)
class _FsSynceIfEsmcMode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),('rx',1),('tx',2)))
_FsSynceIfEsmcMode_Type.__name__=_C
_FsSynceIfEsmcMode_Object=MibTableColumn
fsSynceIfEsmcMode=_FsSynceIfEsmcMode_Object((1,3,6,1,4,1,10876,101,2,79,1,2,1,1,3),_FsSynceIfEsmcMode_Type())
fsSynceIfEsmcMode.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSynceIfEsmcMode.setStatus(_A)
class _FsSynceIfPriority_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsSynceIfPriority_Type.__name__=_C
_FsSynceIfPriority_Object=MibTableColumn
fsSynceIfPriority=_FsSynceIfPriority_Object((1,3,6,1,4,1,10876,101,2,79,1,2,1,1,4),_FsSynceIfPriority_Type())
fsSynceIfPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSynceIfPriority.setStatus(_A)
class _FsSynceIfQLValue_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*(('qlPRC',1),('qlSSUA',2),('qlSSUB',3),('qlSEC',4),('qlDNU',5),('qlPRS',6),('qlSTU',7),('qlST2',8),('qlTNC',9),('qlST3E',10),('qlST3',11),('qlSMC',12),('qlRES',13),('qlPROV',14),('qlDUS',15)))
_FsSynceIfQLValue_Type.__name__=_C
_FsSynceIfQLValue_Object=MibTableColumn
fsSynceIfQLValue=_FsSynceIfQLValue_Object((1,3,6,1,4,1,10876,101,2,79,1,2,1,1,5),_FsSynceIfQLValue_Type())
fsSynceIfQLValue.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSynceIfQLValue.setStatus(_A)
_FsSynceIfIsRxQLForced_Type=TruthValue
_FsSynceIfIsRxQLForced_Object=MibTableColumn
fsSynceIfIsRxQLForced=_FsSynceIfIsRxQLForced_Object((1,3,6,1,4,1,10876,101,2,79,1,2,1,1,6),_FsSynceIfIsRxQLForced_Type())
fsSynceIfIsRxQLForced.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSynceIfIsRxQLForced.setStatus(_A)
class _FsSynceIfLockoutStatus_Type(TruthValue):defaultValue=2
_FsSynceIfLockoutStatus_Type.__name__=_F
_FsSynceIfLockoutStatus_Object=MibTableColumn
fsSynceIfLockoutStatus=_FsSynceIfLockoutStatus_Object((1,3,6,1,4,1,10876,101,2,79,1,2,1,1,7),_FsSynceIfLockoutStatus_Type())
fsSynceIfLockoutStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSynceIfLockoutStatus.setStatus(_A)
_FsSynceIfSignalFail_Type=TruthValue
_FsSynceIfSignalFail_Object=MibTableColumn
fsSynceIfSignalFail=_FsSynceIfSignalFail_Object((1,3,6,1,4,1,10876,101,2,79,1,2,1,1,8),_FsSynceIfSignalFail_Type())
fsSynceIfSignalFail.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSynceIfSignalFail.setStatus(_A)
_FsSynceIfPktsTx_Type=Unsigned32
_FsSynceIfPktsTx_Object=MibTableColumn
fsSynceIfPktsTx=_FsSynceIfPktsTx_Object((1,3,6,1,4,1,10876,101,2,79,1,2,1,1,9),_FsSynceIfPktsTx_Type())
fsSynceIfPktsTx.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSynceIfPktsTx.setStatus(_A)
_FsSynceIfPktsRx_Type=Unsigned32
_FsSynceIfPktsRx_Object=MibTableColumn
fsSynceIfPktsRx=_FsSynceIfPktsRx_Object((1,3,6,1,4,1,10876,101,2,79,1,2,1,1,10),_FsSynceIfPktsRx_Type())
fsSynceIfPktsRx.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSynceIfPktsRx.setStatus(_A)
_FsSynceIfPktsRxDropped_Type=Unsigned32
_FsSynceIfPktsRxDropped_Object=MibTableColumn
fsSynceIfPktsRxDropped=_FsSynceIfPktsRxDropped_Object((1,3,6,1,4,1,10876,101,2,79,1,2,1,1,11),_FsSynceIfPktsRxDropped_Type())
fsSynceIfPktsRxDropped.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSynceIfPktsRxDropped.setStatus(_A)
_FsSynceIfPktsRxErrored_Type=Unsigned32
_FsSynceIfPktsRxErrored_Object=MibTableColumn
fsSynceIfPktsRxErrored=_FsSynceIfPktsRxErrored_Object((1,3,6,1,4,1,10876,101,2,79,1,2,1,1,12),_FsSynceIfPktsRxErrored_Type())
fsSynceIfPktsRxErrored.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSynceIfPktsRxErrored.setStatus(_A)
_FsSynceIfRowStatus_Type=RowStatus
_FsSynceIfRowStatus_Object=MibTableColumn
fsSynceIfRowStatus=_FsSynceIfRowStatus_Object((1,3,6,1,4,1,10876,101,2,79,1,2,1,1,13),_FsSynceIfRowStatus_Type())
fsSynceIfRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSynceIfRowStatus.setStatus(_A)
_FsSynceNotifications_ObjectIdentity=ObjectIdentity
fsSynceNotifications=_FsSynceNotifications_ObjectIdentity((1,3,6,1,4,1,10876,101,2,79,2))
mibBuilder.exportSymbols(_G,**{'fsSynceMIB':fsSynceMIB,'fsSynceObjects':fsSynceObjects,'fsSynceGeneralGroup':fsSynceGeneralGroup,'fsSynceGlobalSysCtrl':fsSynceGlobalSysCtrl,'fsSynceTable':fsSynceTable,'fsSynceEntry':fsSynceEntry,_H:fsSynceContextId,'fsSynceTraceOption':fsSynceTraceOption,'fsSynceQLMode':fsSynceQLMode,'fsSynceQLValue':fsSynceQLValue,'fsSynceSSMOptionMode':fsSynceSSMOptionMode,'fsSynceSelectedInterface':fsSynceSelectedInterface,'fsSynceContextRowStatus':fsSynceContextRowStatus,'fsSynceInterfaceConfiguration':fsSynceInterfaceConfiguration,'fsSynceIfTable':fsSynceIfTable,'fsSynceIfEntry':fsSynceIfEntry,_J:fsSynceIfIndex,'fsSynceIfSynceMode':fsSynceIfSynceMode,'fsSynceIfEsmcMode':fsSynceIfEsmcMode,'fsSynceIfPriority':fsSynceIfPriority,'fsSynceIfQLValue':fsSynceIfQLValue,'fsSynceIfIsRxQLForced':fsSynceIfIsRxQLForced,'fsSynceIfLockoutStatus':fsSynceIfLockoutStatus,'fsSynceIfSignalFail':fsSynceIfSignalFail,'fsSynceIfPktsTx':fsSynceIfPktsTx,'fsSynceIfPktsRx':fsSynceIfPktsRx,'fsSynceIfPktsRxDropped':fsSynceIfPktsRxDropped,'fsSynceIfPktsRxErrored':fsSynceIfPktsRxErrored,'fsSynceIfRowStatus':fsSynceIfRowStatus,'fsSynceNotifications':fsSynceNotifications})