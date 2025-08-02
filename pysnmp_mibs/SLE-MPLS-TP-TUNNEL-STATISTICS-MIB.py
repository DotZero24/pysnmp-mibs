_G='sleMplsTpTunnelStatsInfoIndex'
_F='SLE-MPLS-TP-TUNNEL-STATISTICS-MIB'
_E='Unsigned32'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
sleMgmt,=mibBuilder.importSymbols('DASAN-SMI','sleMgmt')
mplsStdMIB,=mibBuilder.importSymbols('MPLS-TC-STD-MIB','mplsStdMIB')
SleControlRequestResultType,SleControlStatusType=mibBuilder.importSymbols('SLE-TC-MIB','SleControlRequestResultType','SleControlStatusType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,zeroDotZero=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso','zeroDotZero')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
sleMplsTpTunnelStats=ModuleIdentity((1,3,6,1,4,1,6296,101,16,20))
if mibBuilder.loadTexts:sleMplsTpTunnelStats.setRevisions(('2016-01-18 00:00',))
_SleMpls_ObjectIdentity=ObjectIdentity
sleMpls=_SleMpls_ObjectIdentity((1,3,6,1,4,1,6296,101,16))
_SleMplsTpTunnelStatsTable_ObjectIdentity=ObjectIdentity
sleMplsTpTunnelStatsTable=_SleMplsTpTunnelStatsTable_ObjectIdentity((1,3,6,1,4,1,6296,101,16,20,1))
_SleMplsTpTunnelStatsInfoTable_Object=MibTable
sleMplsTpTunnelStatsInfoTable=_SleMplsTpTunnelStatsInfoTable_Object((1,3,6,1,4,1,6296,101,16,20,1,1))
if mibBuilder.loadTexts:sleMplsTpTunnelStatsInfoTable.setStatus(_A)
_SleMplsTpTunnelStatsInfoEntry_Object=MibTableRow
sleMplsTpTunnelStatsInfoEntry=_SleMplsTpTunnelStatsInfoEntry_Object((1,3,6,1,4,1,6296,101,16,20,1,1,1))
sleMplsTpTunnelStatsInfoEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:sleMplsTpTunnelStatsInfoEntry.setStatus(_A)
class _SleMplsTpTunnelStatsInfoIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SleMplsTpTunnelStatsInfoIndex_Type.__name__=_E
_SleMplsTpTunnelStatsInfoIndex_Object=MibTableColumn
sleMplsTpTunnelStatsInfoIndex=_SleMplsTpTunnelStatsInfoIndex_Object((1,3,6,1,4,1,6296,101,16,20,1,1,1,1),_SleMplsTpTunnelStatsInfoIndex_Type())
sleMplsTpTunnelStatsInfoIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:sleMplsTpTunnelStatsInfoIndex.setStatus(_A)
_SleMplsTpTunnelStatsInfoTunnelName_Type=OctetString
_SleMplsTpTunnelStatsInfoTunnelName_Object=MibTableColumn
sleMplsTpTunnelStatsInfoTunnelName=_SleMplsTpTunnelStatsInfoTunnelName_Object((1,3,6,1,4,1,6296,101,16,20,1,1,1,2),_SleMplsTpTunnelStatsInfoTunnelName_Type())
sleMplsTpTunnelStatsInfoTunnelName.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpTunnelStatsInfoTunnelName.setStatus(_A)
class _SleMplsTpTunnelStatsInfoRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('source',0),('transit',1),('destination',2)))
_SleMplsTpTunnelStatsInfoRole_Type.__name__=_C
_SleMplsTpTunnelStatsInfoRole_Object=MibTableColumn
sleMplsTpTunnelStatsInfoRole=_SleMplsTpTunnelStatsInfoRole_Object((1,3,6,1,4,1,6296,101,16,20,1,1,1,3),_SleMplsTpTunnelStatsInfoRole_Type())
sleMplsTpTunnelStatsInfoRole.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpTunnelStatsInfoRole.setStatus(_A)
_SleMplsTpTunnelStatsInfoFwdTxPkts_Type=Counter64
_SleMplsTpTunnelStatsInfoFwdTxPkts_Object=MibTableColumn
sleMplsTpTunnelStatsInfoFwdTxPkts=_SleMplsTpTunnelStatsInfoFwdTxPkts_Object((1,3,6,1,4,1,6296,101,16,20,1,1,1,4),_SleMplsTpTunnelStatsInfoFwdTxPkts_Type())
sleMplsTpTunnelStatsInfoFwdTxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpTunnelStatsInfoFwdTxPkts.setStatus(_A)
_SleMplsTpTunnelStatsInfoFwdTxBytes_Type=Counter64
_SleMplsTpTunnelStatsInfoFwdTxBytes_Object=MibTableColumn
sleMplsTpTunnelStatsInfoFwdTxBytes=_SleMplsTpTunnelStatsInfoFwdTxBytes_Object((1,3,6,1,4,1,6296,101,16,20,1,1,1,5),_SleMplsTpTunnelStatsInfoFwdTxBytes_Type())
sleMplsTpTunnelStatsInfoFwdTxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpTunnelStatsInfoFwdTxBytes.setStatus(_A)
_SleMplsTpTunnelStatsInfoFwdRxPkts_Type=Counter64
_SleMplsTpTunnelStatsInfoFwdRxPkts_Object=MibTableColumn
sleMplsTpTunnelStatsInfoFwdRxPkts=_SleMplsTpTunnelStatsInfoFwdRxPkts_Object((1,3,6,1,4,1,6296,101,16,20,1,1,1,6),_SleMplsTpTunnelStatsInfoFwdRxPkts_Type())
sleMplsTpTunnelStatsInfoFwdRxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpTunnelStatsInfoFwdRxPkts.setStatus(_A)
_SleMplsTpTunnelStatsInfoFwdRxBytes_Type=Counter64
_SleMplsTpTunnelStatsInfoFwdRxBytes_Object=MibTableColumn
sleMplsTpTunnelStatsInfoFwdRxBytes=_SleMplsTpTunnelStatsInfoFwdRxBytes_Object((1,3,6,1,4,1,6296,101,16,20,1,1,1,7),_SleMplsTpTunnelStatsInfoFwdRxBytes_Type())
sleMplsTpTunnelStatsInfoFwdRxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpTunnelStatsInfoFwdRxBytes.setStatus(_A)
_SleMplsTpTunnelStatsInfoRevTxPkts_Type=Counter64
_SleMplsTpTunnelStatsInfoRevTxPkts_Object=MibTableColumn
sleMplsTpTunnelStatsInfoRevTxPkts=_SleMplsTpTunnelStatsInfoRevTxPkts_Object((1,3,6,1,4,1,6296,101,16,20,1,1,1,8),_SleMplsTpTunnelStatsInfoRevTxPkts_Type())
sleMplsTpTunnelStatsInfoRevTxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpTunnelStatsInfoRevTxPkts.setStatus(_A)
_SleMplsTpTunnelStatsInfoRevTxBytes_Type=Counter64
_SleMplsTpTunnelStatsInfoRevTxBytes_Object=MibTableColumn
sleMplsTpTunnelStatsInfoRevTxBytes=_SleMplsTpTunnelStatsInfoRevTxBytes_Object((1,3,6,1,4,1,6296,101,16,20,1,1,1,9),_SleMplsTpTunnelStatsInfoRevTxBytes_Type())
sleMplsTpTunnelStatsInfoRevTxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpTunnelStatsInfoRevTxBytes.setStatus(_A)
_SleMplsTpTunnelStatsInfoRevRxPkts_Type=Counter64
_SleMplsTpTunnelStatsInfoRevRxPkts_Object=MibTableColumn
sleMplsTpTunnelStatsInfoRevRxPkts=_SleMplsTpTunnelStatsInfoRevRxPkts_Object((1,3,6,1,4,1,6296,101,16,20,1,1,1,10),_SleMplsTpTunnelStatsInfoRevRxPkts_Type())
sleMplsTpTunnelStatsInfoRevRxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpTunnelStatsInfoRevRxPkts.setStatus(_A)
_SleMplsTpTunnelStatsInfoRevRxBytes_Type=Counter64
_SleMplsTpTunnelStatsInfoRevRxBytes_Object=MibTableColumn
sleMplsTpTunnelStatsInfoRevRxBytes=_SleMplsTpTunnelStatsInfoRevRxBytes_Object((1,3,6,1,4,1,6296,101,16,20,1,1,1,11),_SleMplsTpTunnelStatsInfoRevRxBytes_Type())
sleMplsTpTunnelStatsInfoRevRxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpTunnelStatsInfoRevRxBytes.setStatus(_A)
_SleMplsTpTunnelStatsControl_ObjectIdentity=ObjectIdentity
sleMplsTpTunnelStatsControl=_SleMplsTpTunnelStatsControl_ObjectIdentity((1,3,6,1,4,1,6296,101,16,20,1,2))
class _SleMplsTpTunnelStatsControlRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('setToClearTunnelStats',1))
_SleMplsTpTunnelStatsControlRequest_Type.__name__=_C
_SleMplsTpTunnelStatsControlRequest_Object=MibScalar
sleMplsTpTunnelStatsControlRequest=_SleMplsTpTunnelStatsControlRequest_Object((1,3,6,1,4,1,6296,101,16,20,1,2,1),_SleMplsTpTunnelStatsControlRequest_Type())
sleMplsTpTunnelStatsControlRequest.setMaxAccess(_D)
if mibBuilder.loadTexts:sleMplsTpTunnelStatsControlRequest.setStatus(_A)
_SleMplsTpTunnelStatsControlStatus_Type=SleControlStatusType
_SleMplsTpTunnelStatsControlStatus_Object=MibScalar
sleMplsTpTunnelStatsControlStatus=_SleMplsTpTunnelStatsControlStatus_Object((1,3,6,1,4,1,6296,101,16,20,1,2,2),_SleMplsTpTunnelStatsControlStatus_Type())
sleMplsTpTunnelStatsControlStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpTunnelStatsControlStatus.setStatus(_A)
_SleMplsTpTunnelStatsControlTimer_Type=Gauge32
_SleMplsTpTunnelStatsControlTimer_Object=MibScalar
sleMplsTpTunnelStatsControlTimer=_SleMplsTpTunnelStatsControlTimer_Object((1,3,6,1,4,1,6296,101,16,20,1,2,3),_SleMplsTpTunnelStatsControlTimer_Type())
sleMplsTpTunnelStatsControlTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:sleMplsTpTunnelStatsControlTimer.setStatus(_A)
_SleMplsTpTunnelStatsControlTimeStamp_Type=TimeTicks
_SleMplsTpTunnelStatsControlTimeStamp_Object=MibScalar
sleMplsTpTunnelStatsControlTimeStamp=_SleMplsTpTunnelStatsControlTimeStamp_Object((1,3,6,1,4,1,6296,101,16,20,1,2,4),_SleMplsTpTunnelStatsControlTimeStamp_Type())
sleMplsTpTunnelStatsControlTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpTunnelStatsControlTimeStamp.setStatus(_A)
_SleMplsTpTunnelStatsReqResult_Type=SleControlRequestResultType
_SleMplsTpTunnelStatsReqResult_Object=MibScalar
sleMplsTpTunnelStatsReqResult=_SleMplsTpTunnelStatsReqResult_Object((1,3,6,1,4,1,6296,101,16,20,1,2,5),_SleMplsTpTunnelStatsReqResult_Type())
sleMplsTpTunnelStatsReqResult.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpTunnelStatsReqResult.setStatus(_A)
_SleMplsTpTunnelStatsControlName_Type=OctetString
_SleMplsTpTunnelStatsControlName_Object=MibScalar
sleMplsTpTunnelStatsControlName=_SleMplsTpTunnelStatsControlName_Object((1,3,6,1,4,1,6296,101,16,20,1,2,6),_SleMplsTpTunnelStatsControlName_Type())
sleMplsTpTunnelStatsControlName.setMaxAccess(_D)
if mibBuilder.loadTexts:sleMplsTpTunnelStatsControlName.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'sleMpls':sleMpls,'sleMplsTpTunnelStats':sleMplsTpTunnelStats,'sleMplsTpTunnelStatsTable':sleMplsTpTunnelStatsTable,'sleMplsTpTunnelStatsInfoTable':sleMplsTpTunnelStatsInfoTable,'sleMplsTpTunnelStatsInfoEntry':sleMplsTpTunnelStatsInfoEntry,_G:sleMplsTpTunnelStatsInfoIndex,'sleMplsTpTunnelStatsInfoTunnelName':sleMplsTpTunnelStatsInfoTunnelName,'sleMplsTpTunnelStatsInfoRole':sleMplsTpTunnelStatsInfoRole,'sleMplsTpTunnelStatsInfoFwdTxPkts':sleMplsTpTunnelStatsInfoFwdTxPkts,'sleMplsTpTunnelStatsInfoFwdTxBytes':sleMplsTpTunnelStatsInfoFwdTxBytes,'sleMplsTpTunnelStatsInfoFwdRxPkts':sleMplsTpTunnelStatsInfoFwdRxPkts,'sleMplsTpTunnelStatsInfoFwdRxBytes':sleMplsTpTunnelStatsInfoFwdRxBytes,'sleMplsTpTunnelStatsInfoRevTxPkts':sleMplsTpTunnelStatsInfoRevTxPkts,'sleMplsTpTunnelStatsInfoRevTxBytes':sleMplsTpTunnelStatsInfoRevTxBytes,'sleMplsTpTunnelStatsInfoRevRxPkts':sleMplsTpTunnelStatsInfoRevRxPkts,'sleMplsTpTunnelStatsInfoRevRxBytes':sleMplsTpTunnelStatsInfoRevRxBytes,'sleMplsTpTunnelStatsControl':sleMplsTpTunnelStatsControl,'sleMplsTpTunnelStatsControlRequest':sleMplsTpTunnelStatsControlRequest,'sleMplsTpTunnelStatsControlStatus':sleMplsTpTunnelStatsControlStatus,'sleMplsTpTunnelStatsControlTimer':sleMplsTpTunnelStatsControlTimer,'sleMplsTpTunnelStatsControlTimeStamp':sleMplsTpTunnelStatsControlTimeStamp,'sleMplsTpTunnelStatsReqResult':sleMplsTpTunnelStatsReqResult,'sleMplsTpTunnelStatsControlName':sleMplsTpTunnelStatsControlName})