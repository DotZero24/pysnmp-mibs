_J='cienaCesTwampServerCtrlSessionId'
_I='accept'
_H='listen'
_G='cienaCesTwampServerSessionId'
_F='enable'
_E='disable'
_D='CIENA-CES-TWAMP-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cienaCesConfig,=mibBuilder.importSymbols('CIENA-SMI','cienaCesConfig')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
cienaCesTwampMIB=ModuleIdentity((1,3,6,1,4,1,1271,2,1,33))
if mibBuilder.loadTexts:cienaCesTwampMIB.setRevisions(('2017-06-07 00:00','2013-11-18 00:00'))
_CienaCesTwampMIBObjects_ObjectIdentity=ObjectIdentity
cienaCesTwampMIBObjects=_CienaCesTwampMIBObjects_ObjectIdentity((1,3,6,1,4,1,1271,2,1,33,1))
_CienaCesTwamp_ObjectIdentity=ObjectIdentity
cienaCesTwamp=_CienaCesTwamp_ObjectIdentity((1,3,6,1,4,1,1271,2,1,33,1,1))
_CienaCesTwampModule_ObjectIdentity=ObjectIdentity
cienaCesTwampModule=_CienaCesTwampModule_ObjectIdentity((1,3,6,1,4,1,1271,2,1,33,1,1,1))
class _CienaCesTwampPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(256,65535))
_CienaCesTwampPort_Type.__name__=_C
_CienaCesTwampPort_Object=MibScalar
cienaCesTwampPort=_CienaCesTwampPort_Object((1,3,6,1,4,1,1271,2,1,33,1,1,1,1),_CienaCesTwampPort_Type())
cienaCesTwampPort.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesTwampPort.setStatus(_A)
class _CienaCesTwampEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_CienaCesTwampEnable_Type.__name__=_C
_CienaCesTwampEnable_Object=MibScalar
cienaCesTwampEnable=_CienaCesTwampEnable_Object((1,3,6,1,4,1,1271,2,1,33,1,1,1,2),_CienaCesTwampEnable_Type())
cienaCesTwampEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesTwampEnable.setStatus(_A)
class _CienaCesTwampServerEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_CienaCesTwampServerEnable_Type.__name__=_C
_CienaCesTwampServerEnable_Object=MibScalar
cienaCesTwampServerEnable=_CienaCesTwampServerEnable_Object((1,3,6,1,4,1,1271,2,1,33,1,1,1,3),_CienaCesTwampServerEnable_Type())
cienaCesTwampServerEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesTwampServerEnable.setStatus(_A)
_CienaCesTwampServerSessionsTable_Object=MibTable
cienaCesTwampServerSessionsTable=_CienaCesTwampServerSessionsTable_Object((1,3,6,1,4,1,1271,2,1,33,1,1,1,4))
if mibBuilder.loadTexts:cienaCesTwampServerSessionsTable.setStatus(_A)
_CienaCesTwampServerSessionEntry_Object=MibTableRow
cienaCesTwampServerSessionEntry=_CienaCesTwampServerSessionEntry_Object((1,3,6,1,4,1,1271,2,1,33,1,1,1,4,1))
cienaCesTwampServerSessionEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:cienaCesTwampServerSessionEntry.setStatus(_A)
class _CienaCesTwampServerSessionId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_CienaCesTwampServerSessionId_Type.__name__=_C
_CienaCesTwampServerSessionId_Object=MibTableColumn
cienaCesTwampServerSessionId=_CienaCesTwampServerSessionId_Object((1,3,6,1,4,1,1271,2,1,33,1,1,1,4,1,1),_CienaCesTwampServerSessionId_Type())
cienaCesTwampServerSessionId.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesTwampServerSessionId.setStatus(_A)
class _CienaCesTwampServerSessionState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_H,0),('greet',1),('start',2),(_I,3),('test',4),('stop',5),('error',6)))
_CienaCesTwampServerSessionState_Type.__name__=_C
_CienaCesTwampServerSessionState_Object=MibTableColumn
cienaCesTwampServerSessionState=_CienaCesTwampServerSessionState_Object((1,3,6,1,4,1,1271,2,1,33,1,1,1,4,1,2),_CienaCesTwampServerSessionState_Type())
cienaCesTwampServerSessionState.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesTwampServerSessionState.setStatus(_A)
class _CienaCesTwampServerSessionPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CienaCesTwampServerSessionPort_Type.__name__=_C
_CienaCesTwampServerSessionPort_Object=MibTableColumn
cienaCesTwampServerSessionPort=_CienaCesTwampServerSessionPort_Object((1,3,6,1,4,1,1271,2,1,33,1,1,1,4,1,3),_CienaCesTwampServerSessionPort_Type())
cienaCesTwampServerSessionPort.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesTwampServerSessionPort.setStatus(_A)
_CienaCesTwampServerSessionHost_Type=IpAddress
_CienaCesTwampServerSessionHost_Object=MibTableColumn
cienaCesTwampServerSessionHost=_CienaCesTwampServerSessionHost_Object((1,3,6,1,4,1,1271,2,1,33,1,1,1,4,1,4),_CienaCesTwampServerSessionHost_Type())
cienaCesTwampServerSessionHost.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesTwampServerSessionHost.setStatus(_A)
_CienaCesTwampServerSessionNumPkts_Type=Integer32
_CienaCesTwampServerSessionNumPkts_Object=MibTableColumn
cienaCesTwampServerSessionNumPkts=_CienaCesTwampServerSessionNumPkts_Object((1,3,6,1,4,1,1271,2,1,33,1,1,1,4,1,5),_CienaCesTwampServerSessionNumPkts_Type())
cienaCesTwampServerSessionNumPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesTwampServerSessionNumPkts.setStatus(_A)
_CienaCesTwampServerSessionSeqNum_Type=Integer32
_CienaCesTwampServerSessionSeqNum_Object=MibTableColumn
cienaCesTwampServerSessionSeqNum=_CienaCesTwampServerSessionSeqNum_Object((1,3,6,1,4,1,1271,2,1,33,1,1,1,4,1,6),_CienaCesTwampServerSessionSeqNum_Type())
cienaCesTwampServerSessionSeqNum.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesTwampServerSessionSeqNum.setStatus(_A)
class _CienaCesTwampTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,86400))
_CienaCesTwampTimeout_Type.__name__=_C
_CienaCesTwampTimeout_Object=MibScalar
cienaCesTwampTimeout=_CienaCesTwampTimeout_Object((1,3,6,1,4,1,1271,2,1,33,1,1,1,5),_CienaCesTwampTimeout_Type())
cienaCesTwampTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesTwampTimeout.setStatus(_A)
class _CienaCesTwampServerDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_CienaCesTwampServerDscp_Type.__name__=_C
_CienaCesTwampServerDscp_Object=MibScalar
cienaCesTwampServerDscp=_CienaCesTwampServerDscp_Object((1,3,6,1,4,1,1271,2,1,33,1,1,1,6),_CienaCesTwampServerDscp_Type())
cienaCesTwampServerDscp.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesTwampServerDscp.setStatus(_A)
_CienaCesTwampServerCtrlSessionsTable_Object=MibTable
cienaCesTwampServerCtrlSessionsTable=_CienaCesTwampServerCtrlSessionsTable_Object((1,3,6,1,4,1,1271,2,1,33,1,1,1,7))
if mibBuilder.loadTexts:cienaCesTwampServerCtrlSessionsTable.setStatus(_A)
_CienaCesTwampServerCtrlSessionEntry_Object=MibTableRow
cienaCesTwampServerCtrlSessionEntry=_CienaCesTwampServerCtrlSessionEntry_Object((1,3,6,1,4,1,1271,2,1,33,1,1,1,7,1))
cienaCesTwampServerCtrlSessionEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:cienaCesTwampServerCtrlSessionEntry.setStatus(_A)
class _CienaCesTwampServerCtrlSessionId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_CienaCesTwampServerCtrlSessionId_Type.__name__=_C
_CienaCesTwampServerCtrlSessionId_Object=MibTableColumn
cienaCesTwampServerCtrlSessionId=_CienaCesTwampServerCtrlSessionId_Object((1,3,6,1,4,1,1271,2,1,33,1,1,1,7,1,1),_CienaCesTwampServerCtrlSessionId_Type())
cienaCesTwampServerCtrlSessionId.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesTwampServerCtrlSessionId.setStatus(_A)
class _CienaCesTwampServerCtrlSessionState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_H,0),('greet',1),('start',2),(_I,3),('test',4),('stop',5),('error',6)))
_CienaCesTwampServerCtrlSessionState_Type.__name__=_C
_CienaCesTwampServerCtrlSessionState_Object=MibTableColumn
cienaCesTwampServerCtrlSessionState=_CienaCesTwampServerCtrlSessionState_Object((1,3,6,1,4,1,1271,2,1,33,1,1,1,7,1,2),_CienaCesTwampServerCtrlSessionState_Type())
cienaCesTwampServerCtrlSessionState.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesTwampServerCtrlSessionState.setStatus(_A)
class _CienaCesTwampServerCtrlSessionPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CienaCesTwampServerCtrlSessionPort_Type.__name__=_C
_CienaCesTwampServerCtrlSessionPort_Object=MibTableColumn
cienaCesTwampServerCtrlSessionPort=_CienaCesTwampServerCtrlSessionPort_Object((1,3,6,1,4,1,1271,2,1,33,1,1,1,7,1,3),_CienaCesTwampServerCtrlSessionPort_Type())
cienaCesTwampServerCtrlSessionPort.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesTwampServerCtrlSessionPort.setStatus(_A)
_CienaCesTwampServerCtrlSessionHost_Type=IpAddress
_CienaCesTwampServerCtrlSessionHost_Object=MibTableColumn
cienaCesTwampServerCtrlSessionHost=_CienaCesTwampServerCtrlSessionHost_Object((1,3,6,1,4,1,1271,2,1,33,1,1,1,7,1,4),_CienaCesTwampServerCtrlSessionHost_Type())
cienaCesTwampServerCtrlSessionHost.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesTwampServerCtrlSessionHost.setStatus(_A)
_CienaCesTwampServerCtrlSessionTestMap_Type=Unsigned32
_CienaCesTwampServerCtrlSessionTestMap_Object=MibTableColumn
cienaCesTwampServerCtrlSessionTestMap=_CienaCesTwampServerCtrlSessionTestMap_Object((1,3,6,1,4,1,1271,2,1,33,1,1,1,7,1,5),_CienaCesTwampServerCtrlSessionTestMap_Type())
cienaCesTwampServerCtrlSessionTestMap.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesTwampServerCtrlSessionTestMap.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'cienaCesTwampMIB':cienaCesTwampMIB,'cienaCesTwampMIBObjects':cienaCesTwampMIBObjects,'cienaCesTwamp':cienaCesTwamp,'cienaCesTwampModule':cienaCesTwampModule,'cienaCesTwampPort':cienaCesTwampPort,'cienaCesTwampEnable':cienaCesTwampEnable,'cienaCesTwampServerEnable':cienaCesTwampServerEnable,'cienaCesTwampServerSessionsTable':cienaCesTwampServerSessionsTable,'cienaCesTwampServerSessionEntry':cienaCesTwampServerSessionEntry,_G:cienaCesTwampServerSessionId,'cienaCesTwampServerSessionState':cienaCesTwampServerSessionState,'cienaCesTwampServerSessionPort':cienaCesTwampServerSessionPort,'cienaCesTwampServerSessionHost':cienaCesTwampServerSessionHost,'cienaCesTwampServerSessionNumPkts':cienaCesTwampServerSessionNumPkts,'cienaCesTwampServerSessionSeqNum':cienaCesTwampServerSessionSeqNum,'cienaCesTwampTimeout':cienaCesTwampTimeout,'cienaCesTwampServerDscp':cienaCesTwampServerDscp,'cienaCesTwampServerCtrlSessionsTable':cienaCesTwampServerCtrlSessionsTable,'cienaCesTwampServerCtrlSessionEntry':cienaCesTwampServerCtrlSessionEntry,_J:cienaCesTwampServerCtrlSessionId,'cienaCesTwampServerCtrlSessionState':cienaCesTwampServerCtrlSessionState,'cienaCesTwampServerCtrlSessionPort':cienaCesTwampServerCtrlSessionPort,'cienaCesTwampServerCtrlSessionHost':cienaCesTwampServerCtrlSessionHost,'cienaCesTwampServerCtrlSessionTestMap':cienaCesTwampServerCtrlSessionTestMap})