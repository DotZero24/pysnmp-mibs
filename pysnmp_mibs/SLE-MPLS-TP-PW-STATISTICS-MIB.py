_G='sleMplsTpPwStatsInfoPwId'
_F='SLE-MPLS-TP-PW-STATISTICS-MIB'
_E='Integer32'
_D='PwIDType'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
sleMgmt,=mibBuilder.importSymbols('DASAN-SMI','sleMgmt')
PwIDType,=mibBuilder.importSymbols('PW-TC-STD-MIB',_D)
SleControlRequestResultType,SleControlStatusType=mibBuilder.importSymbols('SLE-TC-MIB','SleControlRequestResultType','SleControlStatusType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,zeroDotZero=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','zeroDotZero')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
sleMplsTpPwStats=ModuleIdentity((1,3,6,1,4,1,6296,101,16,21))
if mibBuilder.loadTexts:sleMplsTpPwStats.setRevisions(('2015-01-28 00:00',))
_SleMpls_ObjectIdentity=ObjectIdentity
sleMpls=_SleMpls_ObjectIdentity((1,3,6,1,4,1,6296,101,16))
_SleMplsTpPwStatsTable_ObjectIdentity=ObjectIdentity
sleMplsTpPwStatsTable=_SleMplsTpPwStatsTable_ObjectIdentity((1,3,6,1,4,1,6296,101,16,21,1))
_SleMplsTpPwStatsInfoTable_Object=MibTable
sleMplsTpPwStatsInfoTable=_SleMplsTpPwStatsInfoTable_Object((1,3,6,1,4,1,6296,101,16,21,1,1))
if mibBuilder.loadTexts:sleMplsTpPwStatsInfoTable.setStatus(_A)
_SleMplsTpPwStatsInfoEntry_Object=MibTableRow
sleMplsTpPwStatsInfoEntry=_SleMplsTpPwStatsInfoEntry_Object((1,3,6,1,4,1,6296,101,16,21,1,1,1))
sleMplsTpPwStatsInfoEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:sleMplsTpPwStatsInfoEntry.setStatus(_A)
class _SleMplsTpPwStatsInfoPwId_Type(PwIDType):subtypeSpec=PwIDType.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SleMplsTpPwStatsInfoPwId_Type.__name__=_D
_SleMplsTpPwStatsInfoPwId_Object=MibTableColumn
sleMplsTpPwStatsInfoPwId=_SleMplsTpPwStatsInfoPwId_Object((1,3,6,1,4,1,6296,101,16,21,1,1,1,1),_SleMplsTpPwStatsInfoPwId_Type())
sleMplsTpPwStatsInfoPwId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:sleMplsTpPwStatsInfoPwId.setStatus(_A)
_SleMplsTpPwStatsInfoPwName_Type=SnmpAdminString
_SleMplsTpPwStatsInfoPwName_Object=MibTableColumn
sleMplsTpPwStatsInfoPwName=_SleMplsTpPwStatsInfoPwName_Object((1,3,6,1,4,1,6296,101,16,21,1,1,1,2),_SleMplsTpPwStatsInfoPwName_Type())
sleMplsTpPwStatsInfoPwName.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpPwStatsInfoPwName.setStatus(_A)
_SleMplsTpPwStatsInfoTxPkts_Type=Counter64
_SleMplsTpPwStatsInfoTxPkts_Object=MibTableColumn
sleMplsTpPwStatsInfoTxPkts=_SleMplsTpPwStatsInfoTxPkts_Object((1,3,6,1,4,1,6296,101,16,21,1,1,1,3),_SleMplsTpPwStatsInfoTxPkts_Type())
sleMplsTpPwStatsInfoTxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpPwStatsInfoTxPkts.setStatus(_A)
_SleMplsTpPwStatsInfoRxPkts_Type=Counter64
_SleMplsTpPwStatsInfoRxPkts_Object=MibTableColumn
sleMplsTpPwStatsInfoRxPkts=_SleMplsTpPwStatsInfoRxPkts_Object((1,3,6,1,4,1,6296,101,16,21,1,1,1,4),_SleMplsTpPwStatsInfoRxPkts_Type())
sleMplsTpPwStatsInfoRxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpPwStatsInfoRxPkts.setStatus(_A)
_SleMplsTpPwStatsInfoTxBytes_Type=Counter64
_SleMplsTpPwStatsInfoTxBytes_Object=MibTableColumn
sleMplsTpPwStatsInfoTxBytes=_SleMplsTpPwStatsInfoTxBytes_Object((1,3,6,1,4,1,6296,101,16,21,1,1,1,5),_SleMplsTpPwStatsInfoTxBytes_Type())
sleMplsTpPwStatsInfoTxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpPwStatsInfoTxBytes.setStatus(_A)
_SleMplsTpPwStatsInfoRxBytes_Type=Counter64
_SleMplsTpPwStatsInfoRxBytes_Object=MibTableColumn
sleMplsTpPwStatsInfoRxBytes=_SleMplsTpPwStatsInfoRxBytes_Object((1,3,6,1,4,1,6296,101,16,21,1,1,1,6),_SleMplsTpPwStatsInfoRxBytes_Type())
sleMplsTpPwStatsInfoRxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpPwStatsInfoRxBytes.setStatus(_A)
_SleMplsTpPwStatsControl_ObjectIdentity=ObjectIdentity
sleMplsTpPwStatsControl=_SleMplsTpPwStatsControl_ObjectIdentity((1,3,6,1,4,1,6296,101,16,21,1,2))
class _SleMplsTpPwStatsControlRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('setToClearPwStats',1))
_SleMplsTpPwStatsControlRequest_Type.__name__=_E
_SleMplsTpPwStatsControlRequest_Object=MibScalar
sleMplsTpPwStatsControlRequest=_SleMplsTpPwStatsControlRequest_Object((1,3,6,1,4,1,6296,101,16,21,1,2,1),_SleMplsTpPwStatsControlRequest_Type())
sleMplsTpPwStatsControlRequest.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpPwStatsControlRequest.setStatus(_A)
_SleMplsTpPwStatsControlStatus_Type=SleControlStatusType
_SleMplsTpPwStatsControlStatus_Object=MibScalar
sleMplsTpPwStatsControlStatus=_SleMplsTpPwStatsControlStatus_Object((1,3,6,1,4,1,6296,101,16,21,1,2,2),_SleMplsTpPwStatsControlStatus_Type())
sleMplsTpPwStatsControlStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpPwStatsControlStatus.setStatus(_A)
_SleMplsTpPwStatsControlTimer_Type=Gauge32
_SleMplsTpPwStatsControlTimer_Object=MibScalar
sleMplsTpPwStatsControlTimer=_SleMplsTpPwStatsControlTimer_Object((1,3,6,1,4,1,6296,101,16,21,1,2,3),_SleMplsTpPwStatsControlTimer_Type())
sleMplsTpPwStatsControlTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpPwStatsControlTimer.setStatus(_A)
_SleMplsTpPwStatsControlTimeStamp_Type=TimeTicks
_SleMplsTpPwStatsControlTimeStamp_Object=MibScalar
sleMplsTpPwStatsControlTimeStamp=_SleMplsTpPwStatsControlTimeStamp_Object((1,3,6,1,4,1,6296,101,16,21,1,2,4),_SleMplsTpPwStatsControlTimeStamp_Type())
sleMplsTpPwStatsControlTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpPwStatsControlTimeStamp.setStatus(_A)
_SleMplsTpPwStatsReqResult_Type=SleControlRequestResultType
_SleMplsTpPwStatsReqResult_Object=MibScalar
sleMplsTpPwStatsReqResult=_SleMplsTpPwStatsReqResult_Object((1,3,6,1,4,1,6296,101,16,21,1,2,5),_SleMplsTpPwStatsReqResult_Type())
sleMplsTpPwStatsReqResult.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpPwStatsReqResult.setStatus(_A)
_SleMplsTpPwStatsControlPwId_Type=Unsigned32
_SleMplsTpPwStatsControlPwId_Object=MibScalar
sleMplsTpPwStatsControlPwId=_SleMplsTpPwStatsControlPwId_Object((1,3,6,1,4,1,6296,101,16,21,1,2,6),_SleMplsTpPwStatsControlPwId_Type())
sleMplsTpPwStatsControlPwId.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpPwStatsControlPwId.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'sleMpls':sleMpls,'sleMplsTpPwStats':sleMplsTpPwStats,'sleMplsTpPwStatsTable':sleMplsTpPwStatsTable,'sleMplsTpPwStatsInfoTable':sleMplsTpPwStatsInfoTable,'sleMplsTpPwStatsInfoEntry':sleMplsTpPwStatsInfoEntry,_G:sleMplsTpPwStatsInfoPwId,'sleMplsTpPwStatsInfoPwName':sleMplsTpPwStatsInfoPwName,'sleMplsTpPwStatsInfoTxPkts':sleMplsTpPwStatsInfoTxPkts,'sleMplsTpPwStatsInfoRxPkts':sleMplsTpPwStatsInfoRxPkts,'sleMplsTpPwStatsInfoTxBytes':sleMplsTpPwStatsInfoTxBytes,'sleMplsTpPwStatsInfoRxBytes':sleMplsTpPwStatsInfoRxBytes,'sleMplsTpPwStatsControl':sleMplsTpPwStatsControl,'sleMplsTpPwStatsControlRequest':sleMplsTpPwStatsControlRequest,'sleMplsTpPwStatsControlStatus':sleMplsTpPwStatsControlStatus,'sleMplsTpPwStatsControlTimer':sleMplsTpPwStatsControlTimer,'sleMplsTpPwStatsControlTimeStamp':sleMplsTpPwStatsControlTimeStamp,'sleMplsTpPwStatsReqResult':sleMplsTpPwStatsReqResult,'sleMplsTpPwStatsControlPwId':sleMplsTpPwStatsControlPwId})