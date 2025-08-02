_Y='dpiAllVlanID'
_X='notUsed'
_W='dpiAllSlotID'
_V='dpiAllTemplateID'
_U='dpiAllServiceID'
_T='dpiAllSubserviceID'
_S='dpiAllFlowPoolID'
_R='dpiAllSignatureSymbolID'
_Q='dpiAllSignatureEntryID'
_P='disable'
_O='dpiServiceID'
_N='dpiSubserviceID'
_M='dpiStreamLimitType'
_L='dpiStreamLimitID'
_K='dpiSignatureSymbolID'
_J='dpiSignatureEntryID'
_I='OctetString'
_H='permit'
_G='deny'
_F='DPI-MIB'
_E='enable'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
fwdpi=ModuleIdentity((1,3,6,1,4,1,3902,51))
if mibBuilder.loadTexts:fwdpi.setRevisions(('2008-11-04 00:00',))
_Zte_ObjectIdentity=ObjectIdentity
zte=_Zte_ObjectIdentity((1,3,6,1,4,1,3902))
_ZxrDPI_ObjectIdentity=ObjectIdentity
zxrDPI=_ZxrDPI_ObjectIdentity((1,3,6,1,4,1,3902,51,1))
_DpiSystemControl_ObjectIdentity=ObjectIdentity
dpiSystemControl=_DpiSystemControl_ObjectIdentity((1,3,6,1,4,1,3902,51,1,1))
class _DpiSlotNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_DpiSlotNumber_Type.__name__=_B
_DpiSlotNumber_Object=MibScalar
dpiSlotNumber=_DpiSlotNumber_Object((1,3,6,1,4,1,3902,51,1,1,1),_DpiSlotNumber_Type())
dpiSlotNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiSlotNumber.setStatus(_A)
class _DpiRestartFunc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_E,1))
_DpiRestartFunc_Type.__name__=_B
_DpiRestartFunc_Object=MibScalar
dpiRestartFunc=_DpiRestartFunc_Object((1,3,6,1,4,1,3902,51,1,1,2),_DpiRestartFunc_Type())
dpiRestartFunc.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiRestartFunc.setStatus(_A)
_DpiConfigMode_ObjectIdentity=ObjectIdentity
dpiConfigMode=_DpiConfigMode_ObjectIdentity((1,3,6,1,4,1,3902,51,1,2))
_DpiBindMngServiceIp_ObjectIdentity=ObjectIdentity
dpiBindMngServiceIp=_DpiBindMngServiceIp_ObjectIdentity((1,3,6,1,4,1,3902,51,1,2,2))
class _DpiMngServerSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_DpiMngServerSlot_Type.__name__=_B
_DpiMngServerSlot_Object=MibScalar
dpiMngServerSlot=_DpiMngServerSlot_Object((1,3,6,1,4,1,3902,51,1,2,2,1),_DpiMngServerSlot_Type())
dpiMngServerSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiMngServerSlot.setStatus(_A)
_DpiMngIp_Type=IpAddress
_DpiMngIp_Object=MibScalar
dpiMngIp=_DpiMngIp_Object((1,3,6,1,4,1,3902,51,1,2,2,2),_DpiMngIp_Type())
dpiMngIp.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiMngIp.setStatus(_A)
_DpiServerIp_Type=IpAddress
_DpiServerIp_Object=MibScalar
dpiServerIp=_DpiServerIp_Object((1,3,6,1,4,1,3902,51,1,2,2,3),_DpiServerIp_Type())
dpiServerIp.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiServerIp.setStatus(_A)
class _DpiMngServerOK_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_E,1))
_DpiMngServerOK_Type.__name__=_B
_DpiMngServerOK_Object=MibScalar
dpiMngServerOK=_DpiMngServerOK_Object((1,3,6,1,4,1,3902,51,1,2,2,4),_DpiMngServerOK_Type())
dpiMngServerOK.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiMngServerOK.setStatus(_A)
_DpiSignatureEntry_ObjectIdentity=ObjectIdentity
dpiSignatureEntry=_DpiSignatureEntry_ObjectIdentity((1,3,6,1,4,1,3902,51,1,2,3))
class _DpiCurrentSignatureEntry_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12287))
_DpiCurrentSignatureEntry_Type.__name__=_B
_DpiCurrentSignatureEntry_Object=MibScalar
dpiCurrentSignatureEntry=_DpiCurrentSignatureEntry_Object((1,3,6,1,4,1,3902,51,1,2,3,1),_DpiCurrentSignatureEntry_Type())
dpiCurrentSignatureEntry.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiCurrentSignatureEntry.setStatus(_A)
_DpiShowSignatureEntry_ObjectIdentity=ObjectIdentity
dpiShowSignatureEntry=_DpiShowSignatureEntry_ObjectIdentity((1,3,6,1,4,1,3902,51,1,2,3,2))
_DpiSignatureEntryTable_Object=MibTable
dpiSignatureEntryTable=_DpiSignatureEntryTable_Object((1,3,6,1,4,1,3902,51,1,2,3,2,1))
if mibBuilder.loadTexts:dpiSignatureEntryTable.setStatus(_A)
_DpiSignatureTableEntry_Object=MibTableRow
dpiSignatureTableEntry=_DpiSignatureTableEntry_Object((1,3,6,1,4,1,3902,51,1,2,3,2,1,1))
dpiSignatureTableEntry.setIndexNames((0,_F,_J))
if mibBuilder.loadTexts:dpiSignatureTableEntry.setStatus(_A)
class _DpiSignatureEntryID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12287))
_DpiSignatureEntryID_Type.__name__=_B
_DpiSignatureEntryID_Object=MibTableColumn
dpiSignatureEntryID=_DpiSignatureEntryID_Object((1,3,6,1,4,1,3902,51,1,2,3,2,1,1,1),_DpiSignatureEntryID_Type())
dpiSignatureEntryID.setMaxAccess(_D)
if mibBuilder.loadTexts:dpiSignatureEntryID.setStatus(_A)
_DpiSignatureEntryContent_Type=DisplayString
_DpiSignatureEntryContent_Object=MibTableColumn
dpiSignatureEntryContent=_DpiSignatureEntryContent_Object((1,3,6,1,4,1,3902,51,1,2,3,2,1,1,2),_DpiSignatureEntryContent_Type())
dpiSignatureEntryContent.setMaxAccess(_D)
if mibBuilder.loadTexts:dpiSignatureEntryContent.setStatus(_A)
_DpiSetContent_Type=DisplayString
_DpiSetContent_Object=MibScalar
dpiSetContent=_DpiSetContent_Object((1,3,6,1,4,1,3902,51,1,2,3,3),_DpiSetContent_Type())
dpiSetContent.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiSetContent.setStatus(_A)
_DpiSignatureSymbol_ObjectIdentity=ObjectIdentity
dpiSignatureSymbol=_DpiSignatureSymbol_ObjectIdentity((1,3,6,1,4,1,3902,51,1,2,4))
class _DpiCurrentSignatureSymbol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6143))
_DpiCurrentSignatureSymbol_Type.__name__=_B
_DpiCurrentSignatureSymbol_Object=MibScalar
dpiCurrentSignatureSymbol=_DpiCurrentSignatureSymbol_Object((1,3,6,1,4,1,3902,51,1,2,4,1),_DpiCurrentSignatureSymbol_Type())
dpiCurrentSignatureSymbol.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiCurrentSignatureSymbol.setStatus(_A)
_DpiShowSignatureSymbol_ObjectIdentity=ObjectIdentity
dpiShowSignatureSymbol=_DpiShowSignatureSymbol_ObjectIdentity((1,3,6,1,4,1,3902,51,1,2,4,2))
_DpiSignatureSymbolTable_Object=MibTable
dpiSignatureSymbolTable=_DpiSignatureSymbolTable_Object((1,3,6,1,4,1,3902,51,1,2,4,2,1))
if mibBuilder.loadTexts:dpiSignatureSymbolTable.setStatus(_A)
_DpiSignatureSymbolTableEntry_Object=MibTableRow
dpiSignatureSymbolTableEntry=_DpiSignatureSymbolTableEntry_Object((1,3,6,1,4,1,3902,51,1,2,4,2,1,1))
dpiSignatureSymbolTableEntry.setIndexNames((0,_F,_K))
if mibBuilder.loadTexts:dpiSignatureSymbolTableEntry.setStatus(_A)
class _DpiSignatureSymbolID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6143))
_DpiSignatureSymbolID_Type.__name__=_B
_DpiSignatureSymbolID_Object=MibTableColumn
dpiSignatureSymbolID=_DpiSignatureSymbolID_Object((1,3,6,1,4,1,3902,51,1,2,4,2,1,1,1),_DpiSignatureSymbolID_Type())
dpiSignatureSymbolID.setMaxAccess(_D)
if mibBuilder.loadTexts:dpiSignatureSymbolID.setStatus(_A)
_DpiSignatureSymbolEntryID_Type=DisplayString
_DpiSignatureSymbolEntryID_Object=MibTableColumn
dpiSignatureSymbolEntryID=_DpiSignatureSymbolEntryID_Object((1,3,6,1,4,1,3902,51,1,2,4,2,1,1,2),_DpiSignatureSymbolEntryID_Type())
dpiSignatureSymbolEntryID.setMaxAccess(_D)
if mibBuilder.loadTexts:dpiSignatureSymbolEntryID.setStatus(_A)
class _DpiSignatureSymbolHitNumLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_DpiSignatureSymbolHitNumLimit_Type.__name__=_B
_DpiSignatureSymbolHitNumLimit_Object=MibTableColumn
dpiSignatureSymbolHitNumLimit=_DpiSignatureSymbolHitNumLimit_Object((1,3,6,1,4,1,3902,51,1,2,4,2,1,1,3),_DpiSignatureSymbolHitNumLimit_Type())
dpiSignatureSymbolHitNumLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:dpiSignatureSymbolHitNumLimit.setStatus(_A)
class _DpiAddSignatureEntry_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12287))
_DpiAddSignatureEntry_Type.__name__=_B
_DpiAddSignatureEntry_Object=MibScalar
dpiAddSignatureEntry=_DpiAddSignatureEntry_Object((1,3,6,1,4,1,3902,51,1,2,4,3),_DpiAddSignatureEntry_Type())
dpiAddSignatureEntry.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiAddSignatureEntry.setStatus(_A)
class _DpiNoAddSignatureEntry_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12287))
_DpiNoAddSignatureEntry_Type.__name__=_B
_DpiNoAddSignatureEntry_Object=MibScalar
dpiNoAddSignatureEntry=_DpiNoAddSignatureEntry_Object((1,3,6,1,4,1,3902,51,1,2,4,4),_DpiNoAddSignatureEntry_Type())
dpiNoAddSignatureEntry.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiNoAddSignatureEntry.setStatus(_A)
class _DpiSetHitNumLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_DpiSetHitNumLimit_Type.__name__=_B
_DpiSetHitNumLimit_Object=MibScalar
dpiSetHitNumLimit=_DpiSetHitNumLimit_Object((1,3,6,1,4,1,3902,51,1,2,4,5),_DpiSetHitNumLimit_Type())
dpiSetHitNumLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiSetHitNumLimit.setStatus(_A)
_DpiFlowPool_ObjectIdentity=ObjectIdentity
dpiFlowPool=_DpiFlowPool_ObjectIdentity((1,3,6,1,4,1,3902,51,1,2,5))
class _DpiCurrentFlowPool_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8191))
_DpiCurrentFlowPool_Type.__name__=_B
_DpiCurrentFlowPool_Object=MibScalar
dpiCurrentFlowPool=_DpiCurrentFlowPool_Object((1,3,6,1,4,1,3902,51,1,2,5,1),_DpiCurrentFlowPool_Type())
dpiCurrentFlowPool.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiCurrentFlowPool.setStatus(_A)
_DpiShowFlowPool_ObjectIdentity=ObjectIdentity
dpiShowFlowPool=_DpiShowFlowPool_ObjectIdentity((1,3,6,1,4,1,3902,51,1,2,5,2))
_DpiStreamLimitTable_Object=MibTable
dpiStreamLimitTable=_DpiStreamLimitTable_Object((1,3,6,1,4,1,3902,51,1,2,5,2,1))
if mibBuilder.loadTexts:dpiStreamLimitTable.setStatus(_A)
_DpiStreamLimitTableEntry_Object=MibTableRow
dpiStreamLimitTableEntry=_DpiStreamLimitTableEntry_Object((1,3,6,1,4,1,3902,51,1,2,5,2,1,1))
dpiStreamLimitTableEntry.setIndexNames((0,_F,_L),(0,_F,_M))
if mibBuilder.loadTexts:dpiStreamLimitTableEntry.setStatus(_A)
class _DpiStreamLimitID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,8191))
_DpiStreamLimitID_Type.__name__=_B
_DpiStreamLimitID_Object=MibTableColumn
dpiStreamLimitID=_DpiStreamLimitID_Object((1,3,6,1,4,1,3902,51,1,2,5,2,1,1,1),_DpiStreamLimitID_Type())
dpiStreamLimitID.setMaxAccess(_D)
if mibBuilder.loadTexts:dpiStreamLimitID.setStatus(_A)
class _DpiStreamLimitType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('down',1),('up',2)))
_DpiStreamLimitType_Type.__name__=_B
_DpiStreamLimitType_Object=MibTableColumn
dpiStreamLimitType=_DpiStreamLimitType_Object((1,3,6,1,4,1,3902,51,1,2,5,2,1,1,2),_DpiStreamLimitType_Type())
dpiStreamLimitType.setMaxAccess(_D)
if mibBuilder.loadTexts:dpiStreamLimitType.setStatus(_A)
class _DpiStreamRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,100000))
_DpiStreamRate_Type.__name__=_B
_DpiStreamRate_Object=MibTableColumn
dpiStreamRate=_DpiStreamRate_Object((1,3,6,1,4,1,3902,51,1,2,5,2,1,1,3),_DpiStreamRate_Type())
dpiStreamRate.setMaxAccess(_D)
if mibBuilder.loadTexts:dpiStreamRate.setStatus(_A)
_DpiStreamCbs_Type=Integer32
_DpiStreamCbs_Object=MibTableColumn
dpiStreamCbs=_DpiStreamCbs_Object((1,3,6,1,4,1,3902,51,1,2,5,2,1,1,4),_DpiStreamCbs_Type())
dpiStreamCbs.setMaxAccess(_D)
if mibBuilder.loadTexts:dpiStreamCbs.setStatus(_A)
_DpiStreamEbs_Type=Integer32
_DpiStreamEbs_Object=MibTableColumn
dpiStreamEbs=_DpiStreamEbs_Object((1,3,6,1,4,1,3902,51,1,2,5,2,1,1,5),_DpiStreamEbs_Type())
dpiStreamEbs.setMaxAccess(_D)
if mibBuilder.loadTexts:dpiStreamEbs.setStatus(_A)
_DpiUpStreamRateLimit_ObjectIdentity=ObjectIdentity
dpiUpStreamRateLimit=_DpiUpStreamRateLimit_ObjectIdentity((1,3,6,1,4,1,3902,51,1,2,5,3))
class _DpiUpStreamRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,100000))
_DpiUpStreamRate_Type.__name__=_B
_DpiUpStreamRate_Object=MibScalar
dpiUpStreamRate=_DpiUpStreamRate_Object((1,3,6,1,4,1,3902,51,1,2,5,3,1),_DpiUpStreamRate_Type())
dpiUpStreamRate.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiUpStreamRate.setStatus(_A)
_DpiUpStreamCbs_Type=Integer32
_DpiUpStreamCbs_Object=MibScalar
dpiUpStreamCbs=_DpiUpStreamCbs_Object((1,3,6,1,4,1,3902,51,1,2,5,3,2),_DpiUpStreamCbs_Type())
dpiUpStreamCbs.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiUpStreamCbs.setStatus(_A)
_DpiUpStreamEbs_Type=Integer32
_DpiUpStreamEbs_Object=MibScalar
dpiUpStreamEbs=_DpiUpStreamEbs_Object((1,3,6,1,4,1,3902,51,1,2,5,3,3),_DpiUpStreamEbs_Type())
dpiUpStreamEbs.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiUpStreamEbs.setStatus(_A)
class _DpiUpStreamOK_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_E,1))
_DpiUpStreamOK_Type.__name__=_B
_DpiUpStreamOK_Object=MibScalar
dpiUpStreamOK=_DpiUpStreamOK_Object((1,3,6,1,4,1,3902,51,1,2,5,3,4),_DpiUpStreamOK_Type())
dpiUpStreamOK.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiUpStreamOK.setStatus(_A)
class _DpiNoUpStreamRateLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_E,1))
_DpiNoUpStreamRateLimit_Type.__name__=_B
_DpiNoUpStreamRateLimit_Object=MibScalar
dpiNoUpStreamRateLimit=_DpiNoUpStreamRateLimit_Object((1,3,6,1,4,1,3902,51,1,2,5,4),_DpiNoUpStreamRateLimit_Type())
dpiNoUpStreamRateLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiNoUpStreamRateLimit.setStatus(_A)
_DpiDownStreamRateLimit_ObjectIdentity=ObjectIdentity
dpiDownStreamRateLimit=_DpiDownStreamRateLimit_ObjectIdentity((1,3,6,1,4,1,3902,51,1,2,5,5))
class _DpiDownStreamRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,100000))
_DpiDownStreamRate_Type.__name__=_B
_DpiDownStreamRate_Object=MibScalar
dpiDownStreamRate=_DpiDownStreamRate_Object((1,3,6,1,4,1,3902,51,1,2,5,5,1),_DpiDownStreamRate_Type())
dpiDownStreamRate.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiDownStreamRate.setStatus(_A)
_DpiDownStreamCbs_Type=Integer32
_DpiDownStreamCbs_Object=MibScalar
dpiDownStreamCbs=_DpiDownStreamCbs_Object((1,3,6,1,4,1,3902,51,1,2,5,5,2),_DpiDownStreamCbs_Type())
dpiDownStreamCbs.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiDownStreamCbs.setStatus(_A)
_DpiDownStreamEbs_Type=Integer32
_DpiDownStreamEbs_Object=MibScalar
dpiDownStreamEbs=_DpiDownStreamEbs_Object((1,3,6,1,4,1,3902,51,1,2,5,5,3),_DpiDownStreamEbs_Type())
dpiDownStreamEbs.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiDownStreamEbs.setStatus(_A)
class _DpiDownStreamOK_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_E,1))
_DpiDownStreamOK_Type.__name__=_B
_DpiDownStreamOK_Object=MibScalar
dpiDownStreamOK=_DpiDownStreamOK_Object((1,3,6,1,4,1,3902,51,1,2,5,5,4),_DpiDownStreamOK_Type())
dpiDownStreamOK.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiDownStreamOK.setStatus(_A)
class _DpiNoDownStreamRateLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_E,1))
_DpiNoDownStreamRateLimit_Type.__name__=_B
_DpiNoDownStreamRateLimit_Object=MibScalar
dpiNoDownStreamRateLimit=_DpiNoDownStreamRateLimit_Object((1,3,6,1,4,1,3902,51,1,2,5,6),_DpiNoDownStreamRateLimit_Type())
dpiNoDownStreamRateLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiNoDownStreamRateLimit.setStatus(_A)
_DpiSubservice_ObjectIdentity=ObjectIdentity
dpiSubservice=_DpiSubservice_ObjectIdentity((1,3,6,1,4,1,3902,51,1,2,6))
class _DpiCurrentSubservice_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8191))
_DpiCurrentSubservice_Type.__name__=_B
_DpiCurrentSubservice_Object=MibScalar
dpiCurrentSubservice=_DpiCurrentSubservice_Object((1,3,6,1,4,1,3902,51,1,2,6,1),_DpiCurrentSubservice_Type())
dpiCurrentSubservice.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiCurrentSubservice.setStatus(_A)
_DpiShowSubservice_ObjectIdentity=ObjectIdentity
dpiShowSubservice=_DpiShowSubservice_ObjectIdentity((1,3,6,1,4,1,3902,51,1,2,6,2))
_DpiSubserviceTable_Object=MibTable
dpiSubserviceTable=_DpiSubserviceTable_Object((1,3,6,1,4,1,3902,51,1,2,6,2,1))
if mibBuilder.loadTexts:dpiSubserviceTable.setStatus(_A)
_DpiSubserviceEntry_Object=MibTableRow
dpiSubserviceEntry=_DpiSubserviceEntry_Object((1,3,6,1,4,1,3902,51,1,2,6,2,1,1))
dpiSubserviceEntry.setIndexNames((0,_F,_N))
if mibBuilder.loadTexts:dpiSubserviceEntry.setStatus(_A)
class _DpiSubserviceID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8191))
_DpiSubserviceID_Type.__name__=_B
_DpiSubserviceID_Object=MibTableColumn
dpiSubserviceID=_DpiSubserviceID_Object((1,3,6,1,4,1,3902,51,1,2,6,2,1,1,1),_DpiSubserviceID_Type())
dpiSubserviceID.setMaxAccess(_D)
if mibBuilder.loadTexts:dpiSubserviceID.setStatus(_A)
class _DpiSubserviceSymbolNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6143))
_DpiSubserviceSymbolNum_Type.__name__=_B
_DpiSubserviceSymbolNum_Object=MibTableColumn
dpiSubserviceSymbolNum=_DpiSubserviceSymbolNum_Object((1,3,6,1,4,1,3902,51,1,2,6,2,1,1,2),_DpiSubserviceSymbolNum_Type())
dpiSubserviceSymbolNum.setMaxAccess(_D)
if mibBuilder.loadTexts:dpiSubserviceSymbolNum.setStatus(_A)
class _DpiSubserviceFlowpoolID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,8191))
_DpiSubserviceFlowpoolID_Type.__name__=_B
_DpiSubserviceFlowpoolID_Object=MibTableColumn
dpiSubserviceFlowpoolID=_DpiSubserviceFlowpoolID_Object((1,3,6,1,4,1,3902,51,1,2,6,2,1,1,3),_DpiSubserviceFlowpoolID_Type())
dpiSubserviceFlowpoolID.setMaxAccess(_D)
if mibBuilder.loadTexts:dpiSubserviceFlowpoolID.setStatus(_A)
class _DpiSubserviceAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_DpiSubserviceAction_Type.__name__=_B
_DpiSubserviceAction_Object=MibTableColumn
dpiSubserviceAction=_DpiSubserviceAction_Object((1,3,6,1,4,1,3902,51,1,2,6,2,1,1,4),_DpiSubserviceAction_Type())
dpiSubserviceAction.setMaxAccess(_D)
if mibBuilder.loadTexts:dpiSubserviceAction.setStatus(_A)
class _DpiSubserviceAgingTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_DpiSubserviceAgingTime_Type.__name__=_B
_DpiSubserviceAgingTime_Object=MibTableColumn
dpiSubserviceAgingTime=_DpiSubserviceAgingTime_Object((1,3,6,1,4,1,3902,51,1,2,6,2,1,1,5),_DpiSubserviceAgingTime_Type())
dpiSubserviceAgingTime.setMaxAccess(_D)
if mibBuilder.loadTexts:dpiSubserviceAgingTime.setStatus(_A)
_DpiSubserviceSymbolList_Type=DisplayString
_DpiSubserviceSymbolList_Object=MibTableColumn
dpiSubserviceSymbolList=_DpiSubserviceSymbolList_Object((1,3,6,1,4,1,3902,51,1,2,6,2,1,1,6),_DpiSubserviceSymbolList_Type())
dpiSubserviceSymbolList.setMaxAccess(_D)
if mibBuilder.loadTexts:dpiSubserviceSymbolList.setStatus(_A)
_DpiAddSignatureSymbol_ObjectIdentity=ObjectIdentity
dpiAddSignatureSymbol=_DpiAddSignatureSymbol_ObjectIdentity((1,3,6,1,4,1,3902,51,1,2,6,3))
_DpiAddSignatureSymbolId_Type=DisplayString
_DpiAddSignatureSymbolId_Object=MibScalar
dpiAddSignatureSymbolId=_DpiAddSignatureSymbolId_Object((1,3,6,1,4,1,3902,51,1,2,6,3,1),_DpiAddSignatureSymbolId_Type())
dpiAddSignatureSymbolId.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiAddSignatureSymbolId.setStatus(_A)
_DpiAddSignatureSymbolRelationName_Type=DisplayString
_DpiAddSignatureSymbolRelationName_Object=MibScalar
dpiAddSignatureSymbolRelationName=_DpiAddSignatureSymbolRelationName_Object((1,3,6,1,4,1,3902,51,1,2,6,3,2),_DpiAddSignatureSymbolRelationName_Type())
dpiAddSignatureSymbolRelationName.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiAddSignatureSymbolRelationName.setStatus(_A)
class _DpiAddSignatureSymbolOK_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_E,1))
_DpiAddSignatureSymbolOK_Type.__name__=_B
_DpiAddSignatureSymbolOK_Object=MibScalar
dpiAddSignatureSymbolOK=_DpiAddSignatureSymbolOK_Object((1,3,6,1,4,1,3902,51,1,2,6,3,3),_DpiAddSignatureSymbolOK_Type())
dpiAddSignatureSymbolOK.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiAddSignatureSymbolOK.setStatus(_A)
_DpiNoAddSignatureSymbol_Type=DisplayString
_DpiNoAddSignatureSymbol_Object=MibScalar
dpiNoAddSignatureSymbol=_DpiNoAddSignatureSymbol_Object((1,3,6,1,4,1,3902,51,1,2,6,4),_DpiNoAddSignatureSymbol_Type())
dpiNoAddSignatureSymbol.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiNoAddSignatureSymbol.setStatus(_A)
_DpiAddProtocol_Type=DisplayString
_DpiAddProtocol_Object=MibScalar
dpiAddProtocol=_DpiAddProtocol_Object((1,3,6,1,4,1,3902,51,1,2,6,5),_DpiAddProtocol_Type())
dpiAddProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiAddProtocol.setStatus(_A)
_DpiNoAddProtocol_Type=DisplayString
_DpiNoAddProtocol_Object=MibScalar
dpiNoAddProtocol=_DpiNoAddProtocol_Object((1,3,6,1,4,1,3902,51,1,2,6,6),_DpiNoAddProtocol_Type())
dpiNoAddProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiNoAddProtocol.setStatus(_A)
class _DpiBindFlowPool_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,8191))
_DpiBindFlowPool_Type.__name__=_B
_DpiBindFlowPool_Object=MibScalar
dpiBindFlowPool=_DpiBindFlowPool_Object((1,3,6,1,4,1,3902,51,1,2,6,7),_DpiBindFlowPool_Type())
dpiBindFlowPool.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiBindFlowPool.setStatus(_A)
class _DpiNoBindFlowPool_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,8191))
_DpiNoBindFlowPool_Type.__name__=_B
_DpiNoBindFlowPool_Object=MibScalar
dpiNoBindFlowPool=_DpiNoBindFlowPool_Object((1,3,6,1,4,1,3902,51,1,2,6,8),_DpiNoBindFlowPool_Type())
dpiNoBindFlowPool.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiNoBindFlowPool.setStatus(_A)
class _DpiSetAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_G,1)))
_DpiSetAction_Type.__name__=_B
_DpiSetAction_Object=MibScalar
dpiSetAction=_DpiSetAction_Object((1,3,6,1,4,1,3902,51,1,2,6,9),_DpiSetAction_Type())
dpiSetAction.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiSetAction.setStatus(_A)
class _DpiSetAgingTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_DpiSetAgingTime_Type.__name__=_B
_DpiSetAgingTime_Object=MibScalar
dpiSetAgingTime=_DpiSetAgingTime_Object((1,3,6,1,4,1,3902,51,1,2,6,10),_DpiSetAgingTime_Type())
dpiSetAgingTime.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiSetAgingTime.setStatus(_A)
_DpiService_ObjectIdentity=ObjectIdentity
dpiService=_DpiService_ObjectIdentity((1,3,6,1,4,1,3902,51,1,2,7))
class _DpiCurrentService_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2047))
_DpiCurrentService_Type.__name__=_B
_DpiCurrentService_Object=MibScalar
dpiCurrentService=_DpiCurrentService_Object((1,3,6,1,4,1,3902,51,1,2,7,1),_DpiCurrentService_Type())
dpiCurrentService.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiCurrentService.setStatus(_A)
_DpiShowService_ObjectIdentity=ObjectIdentity
dpiShowService=_DpiShowService_ObjectIdentity((1,3,6,1,4,1,3902,51,1,2,7,2))
_DpiServiceTable_Object=MibTable
dpiServiceTable=_DpiServiceTable_Object((1,3,6,1,4,1,3902,51,1,2,7,2,1))
if mibBuilder.loadTexts:dpiServiceTable.setStatus(_A)
_DpiServiceEntry_Object=MibTableRow
dpiServiceEntry=_DpiServiceEntry_Object((1,3,6,1,4,1,3902,51,1,2,7,2,1,1))
dpiServiceEntry.setIndexNames((0,_F,_O))
if mibBuilder.loadTexts:dpiServiceEntry.setStatus(_A)
class _DpiServiceID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2047))
_DpiServiceID_Type.__name__=_B
_DpiServiceID_Object=MibTableColumn
dpiServiceID=_DpiServiceID_Object((1,3,6,1,4,1,3902,51,1,2,7,2,1,1,1),_DpiServiceID_Type())
dpiServiceID.setMaxAccess(_D)
if mibBuilder.loadTexts:dpiServiceID.setStatus(_A)
class _DpiServiceFlowPoolID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,8191))
_DpiServiceFlowPoolID_Type.__name__=_B
_DpiServiceFlowPoolID_Object=MibTableColumn
dpiServiceFlowPoolID=_DpiServiceFlowPoolID_Object((1,3,6,1,4,1,3902,51,1,2,7,2,1,1,2),_DpiServiceFlowPoolID_Type())
dpiServiceFlowPoolID.setMaxAccess(_D)
if mibBuilder.loadTexts:dpiServiceFlowPoolID.setStatus(_A)
class _DpiServiceConnectionLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1310719))
_DpiServiceConnectionLimit_Type.__name__=_B
_DpiServiceConnectionLimit_Object=MibTableColumn
dpiServiceConnectionLimit=_DpiServiceConnectionLimit_Object((1,3,6,1,4,1,3902,51,1,2,7,2,1,1,3),_DpiServiceConnectionLimit_Type())
dpiServiceConnectionLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:dpiServiceConnectionLimit.setStatus(_A)
class _DpiServiceSubserviceNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8191))
_DpiServiceSubserviceNum_Type.__name__=_B
_DpiServiceSubserviceNum_Object=MibTableColumn
dpiServiceSubserviceNum=_DpiServiceSubserviceNum_Object((1,3,6,1,4,1,3902,51,1,2,7,2,1,1,4),_DpiServiceSubserviceNum_Type())
dpiServiceSubserviceNum.setMaxAccess(_D)
if mibBuilder.loadTexts:dpiServiceSubserviceNum.setStatus(_A)
_DpiServiceSubserviceList_Type=DisplayString
_DpiServiceSubserviceList_Object=MibTableColumn
dpiServiceSubserviceList=_DpiServiceSubserviceList_Object((1,3,6,1,4,1,3902,51,1,2,7,2,1,1,5),_DpiServiceSubserviceList_Type())
dpiServiceSubserviceList.setMaxAccess(_D)
if mibBuilder.loadTexts:dpiServiceSubserviceList.setStatus(_A)
class _DpiAddSubservice_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8191))
_DpiAddSubservice_Type.__name__=_B
_DpiAddSubservice_Object=MibScalar
dpiAddSubservice=_DpiAddSubservice_Object((1,3,6,1,4,1,3902,51,1,2,7,3),_DpiAddSubservice_Type())
dpiAddSubservice.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiAddSubservice.setStatus(_A)
class _DpiNoAddSubservice_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8191))
_DpiNoAddSubservice_Type.__name__=_B
_DpiNoAddSubservice_Object=MibScalar
dpiNoAddSubservice=_DpiNoAddSubservice_Object((1,3,6,1,4,1,3902,51,1,2,7,4),_DpiNoAddSubservice_Type())
dpiNoAddSubservice.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiNoAddSubservice.setStatus(_A)
_DpiImportSubservice_ObjectIdentity=ObjectIdentity
dpiImportSubservice=_DpiImportSubservice_ObjectIdentity((1,3,6,1,4,1,3902,51,1,2,7,5))
class _DpiImportDestSubservice_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8191))
_DpiImportDestSubservice_Type.__name__=_B
_DpiImportDestSubservice_Object=MibScalar
dpiImportDestSubservice=_DpiImportDestSubservice_Object((1,3,6,1,4,1,3902,51,1,2,7,5,1),_DpiImportDestSubservice_Type())
dpiImportDestSubservice.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiImportDestSubservice.setStatus(_A)
class _DpiImportSrcSubservice_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8191))
_DpiImportSrcSubservice_Type.__name__=_B
_DpiImportSrcSubservice_Object=MibScalar
dpiImportSrcSubservice=_DpiImportSrcSubservice_Object((1,3,6,1,4,1,3902,51,1,2,7,5,2),_DpiImportSrcSubservice_Type())
dpiImportSrcSubservice.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiImportSrcSubservice.setStatus(_A)
class _DpiImportSubserviceOK_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_E,1))
_DpiImportSubserviceOK_Type.__name__=_B
_DpiImportSubserviceOK_Object=MibScalar
dpiImportSubserviceOK=_DpiImportSubserviceOK_Object((1,3,6,1,4,1,3902,51,1,2,7,5,3),_DpiImportSubserviceOK_Type())
dpiImportSubserviceOK.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiImportSubserviceOK.setStatus(_A)
class _DpiNoImportSubservice_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_E,1))
_DpiNoImportSubservice_Type.__name__=_B
_DpiNoImportSubservice_Object=MibScalar
dpiNoImportSubservice=_DpiNoImportSubservice_Object((1,3,6,1,4,1,3902,51,1,2,7,5,4),_DpiNoImportSubservice_Type())
dpiNoImportSubservice.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiNoImportSubservice.setStatus(_A)
class _DpiServiceBindFlowPool_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,8191))
_DpiServiceBindFlowPool_Type.__name__=_B
_DpiServiceBindFlowPool_Object=MibScalar
dpiServiceBindFlowPool=_DpiServiceBindFlowPool_Object((1,3,6,1,4,1,3902,51,1,2,7,6),_DpiServiceBindFlowPool_Type())
dpiServiceBindFlowPool.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiServiceBindFlowPool.setStatus(_A)
class _DpiServiceNoBindFlowPool_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,8191))
_DpiServiceNoBindFlowPool_Type.__name__=_B
_DpiServiceNoBindFlowPool_Object=MibScalar
dpiServiceNoBindFlowPool=_DpiServiceNoBindFlowPool_Object((1,3,6,1,4,1,3902,51,1,2,7,7),_DpiServiceNoBindFlowPool_Type())
dpiServiceNoBindFlowPool.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiServiceNoBindFlowPool.setStatus(_A)
_DpiTemplate_ObjectIdentity=ObjectIdentity
dpiTemplate=_DpiTemplate_ObjectIdentity((1,3,6,1,4,1,3902,51,1,2,8))
class _DpiCurrentTemplate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_DpiCurrentTemplate_Type.__name__=_B
_DpiCurrentTemplate_Object=MibScalar
dpiCurrentTemplate=_DpiCurrentTemplate_Object((1,3,6,1,4,1,3902,51,1,2,8,1),_DpiCurrentTemplate_Type())
dpiCurrentTemplate.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiCurrentTemplate.setStatus(_A)
class _DpiBindSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_DpiBindSlot_Type.__name__=_B
_DpiBindSlot_Object=MibScalar
dpiBindSlot=_DpiBindSlot_Object((1,3,6,1,4,1,3902,51,1,2,8,2),_DpiBindSlot_Type())
dpiBindSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiBindSlot.setStatus(_A)
class _DpiNoBindSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_DpiNoBindSlot_Type.__name__=_B
_DpiNoBindSlot_Object=MibScalar
dpiNoBindSlot=_DpiNoBindSlot_Object((1,3,6,1,4,1,3902,51,1,2,8,3),_DpiNoBindSlot_Type())
dpiNoBindSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiNoBindSlot.setStatus(_A)
class _DpiBindService_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2047))
_DpiBindService_Type.__name__=_B
_DpiBindService_Object=MibScalar
dpiBindService=_DpiBindService_Object((1,3,6,1,4,1,3902,51,1,2,8,4),_DpiBindService_Type())
dpiBindService.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiBindService.setStatus(_A)
class _DpiNoBindService_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2047))
_DpiNoBindService_Type.__name__=_B
_DpiNoBindService_Object=MibScalar
dpiNoBindService=_DpiNoBindService_Object((1,3,6,1,4,1,3902,51,1,2,8,5),_DpiNoBindService_Type())
dpiNoBindService.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiNoBindService.setStatus(_A)
_DpiBindSipAddr_ObjectIdentity=ObjectIdentity
dpiBindSipAddr=_DpiBindSipAddr_ObjectIdentity((1,3,6,1,4,1,3902,51,1,2,8,6))
_DpiSipAddress_Type=IpAddress
_DpiSipAddress_Object=MibScalar
dpiSipAddress=_DpiSipAddress_Object((1,3,6,1,4,1,3902,51,1,2,8,6,1),_DpiSipAddress_Type())
dpiSipAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiSipAddress.setStatus(_A)
_DpiSipMask_Type=IpAddress
_DpiSipMask_Object=MibScalar
dpiSipMask=_DpiSipMask_Object((1,3,6,1,4,1,3902,51,1,2,8,6,2),_DpiSipMask_Type())
dpiSipMask.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiSipMask.setStatus(_A)
class _DpiSipServiceID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2047))
_DpiSipServiceID_Type.__name__=_B
_DpiSipServiceID_Object=MibScalar
dpiSipServiceID=_DpiSipServiceID_Object((1,3,6,1,4,1,3902,51,1,2,8,6,3),_DpiSipServiceID_Type())
dpiSipServiceID.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiSipServiceID.setStatus(_A)
class _DpiBindSipAddrOK_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_E,1))
_DpiBindSipAddrOK_Type.__name__=_B
_DpiBindSipAddrOK_Object=MibScalar
dpiBindSipAddrOK=_DpiBindSipAddrOK_Object((1,3,6,1,4,1,3902,51,1,2,8,6,4),_DpiBindSipAddrOK_Type())
dpiBindSipAddrOK.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiBindSipAddrOK.setStatus(_A)
class _DpiNoBindSipAddr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_E,1))
_DpiNoBindSipAddr_Type.__name__=_B
_DpiNoBindSipAddr_Object=MibScalar
dpiNoBindSipAddr=_DpiNoBindSipAddr_Object((1,3,6,1,4,1,3902,51,1,2,8,6,5),_DpiNoBindSipAddr_Type())
dpiNoBindSipAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiNoBindSipAddr.setStatus(_A)
class _DpiShowIpService_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2047))
_DpiShowIpService_Type.__name__=_B
_DpiShowIpService_Object=MibScalar
dpiShowIpService=_DpiShowIpService_Object((1,3,6,1,4,1,3902,51,1,2,8,6,6),_DpiShowIpService_Type())
dpiShowIpService.setMaxAccess(_D)
if mibBuilder.loadTexts:dpiShowIpService.setStatus(_A)
_DpiBindSwitchport_ObjectIdentity=ObjectIdentity
dpiBindSwitchport=_DpiBindSwitchport_ObjectIdentity((1,3,6,1,4,1,3902,51,1,2,8,7))
_DpiBindSwitchportPort_Type=DisplayString
_DpiBindSwitchportPort_Object=MibScalar
dpiBindSwitchportPort=_DpiBindSwitchportPort_Object((1,3,6,1,4,1,3902,51,1,2,8,7,2),_DpiBindSwitchportPort_Type())
dpiBindSwitchportPort.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiBindSwitchportPort.setStatus(_A)
class _DpiBindSwitchService_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2047))
_DpiBindSwitchService_Type.__name__=_B
_DpiBindSwitchService_Object=MibScalar
dpiBindSwitchService=_DpiBindSwitchService_Object((1,3,6,1,4,1,3902,51,1,2,8,7,3),_DpiBindSwitchService_Type())
dpiBindSwitchService.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiBindSwitchService.setStatus(_A)
class _DpiBindSwitchportOK_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_E,1))
_DpiBindSwitchportOK_Type.__name__=_B
_DpiBindSwitchportOK_Object=MibScalar
dpiBindSwitchportOK=_DpiBindSwitchportOK_Object((1,3,6,1,4,1,3902,51,1,2,8,7,4),_DpiBindSwitchportOK_Type())
dpiBindSwitchportOK.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiBindSwitchportOK.setStatus(_A)
class _DpiNoBindSwitchport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_E,1))
_DpiNoBindSwitchport_Type.__name__=_B
_DpiNoBindSwitchport_Object=MibScalar
dpiNoBindSwitchport=_DpiNoBindSwitchport_Object((1,3,6,1,4,1,3902,51,1,2,8,7,5),_DpiNoBindSwitchport_Type())
dpiNoBindSwitchport.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiNoBindSwitchport.setStatus(_A)
class _DpiShowPortService_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2047))
_DpiShowPortService_Type.__name__=_B
_DpiShowPortService_Object=MibScalar
dpiShowPortService=_DpiShowPortService_Object((1,3,6,1,4,1,3902,51,1,2,8,7,6),_DpiShowPortService_Type())
dpiShowPortService.setMaxAccess(_D)
if mibBuilder.loadTexts:dpiShowPortService.setStatus(_A)
class _DpiSetActiceConnectionSaveInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_DpiSetActiceConnectionSaveInterval_Type.__name__=_B
_DpiSetActiceConnectionSaveInterval_Object=MibScalar
dpiSetActiceConnectionSaveInterval=_DpiSetActiceConnectionSaveInterval_Object((1,3,6,1,4,1,3902,51,1,2,9),_DpiSetActiceConnectionSaveInterval_Type())
dpiSetActiceConnectionSaveInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiSetActiceConnectionSaveInterval.setStatus(_A)
class _DpiClearConnectionAll_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_E,1))
_DpiClearConnectionAll_Type.__name__=_B
_DpiClearConnectionAll_Object=MibScalar
dpiClearConnectionAll=_DpiClearConnectionAll_Object((1,3,6,1,4,1,3902,51,1,2,10),_DpiClearConnectionAll_Type())
dpiClearConnectionAll.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiClearConnectionAll.setStatus(_A)
_DpiMonitorLog_ObjectIdentity=ObjectIdentity
dpiMonitorLog=_DpiMonitorLog_ObjectIdentity((1,3,6,1,4,1,3902,51,1,3))
_DpiUploadAuto_ObjectIdentity=ObjectIdentity
dpiUploadAuto=_DpiUploadAuto_ObjectIdentity((1,3,6,1,4,1,3902,51,1,3,1))
class _DpiUploadAutoSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_DpiUploadAutoSlot_Type.__name__=_B
_DpiUploadAutoSlot_Object=MibScalar
dpiUploadAutoSlot=_DpiUploadAutoSlot_Object((1,3,6,1,4,1,3902,51,1,3,1,1),_DpiUploadAutoSlot_Type())
dpiUploadAutoSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiUploadAutoSlot.setStatus(_A)
class _DpiUploadAutoEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_P,0),(_E,1)))
_DpiUploadAutoEnable_Type.__name__=_B
_DpiUploadAutoEnable_Object=MibScalar
dpiUploadAutoEnable=_DpiUploadAutoEnable_Object((1,3,6,1,4,1,3902,51,1,3,1,2),_DpiUploadAutoEnable_Type())
dpiUploadAutoEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiUploadAutoEnable.setStatus(_A)
class _DpiUploadAutoOK_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_E,1))
_DpiUploadAutoOK_Type.__name__=_B
_DpiUploadAutoOK_Object=MibScalar
dpiUploadAutoOK=_DpiUploadAutoOK_Object((1,3,6,1,4,1,3902,51,1,3,1,3),_DpiUploadAutoOK_Type())
dpiUploadAutoOK.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiUploadAutoOK.setStatus(_A)
_DpiUploadInterval_ObjectIdentity=ObjectIdentity
dpiUploadInterval=_DpiUploadInterval_ObjectIdentity((1,3,6,1,4,1,3902,51,1,3,2))
class _DpiUploadIntervalSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_DpiUploadIntervalSlot_Type.__name__=_B
_DpiUploadIntervalSlot_Object=MibScalar
dpiUploadIntervalSlot=_DpiUploadIntervalSlot_Object((1,3,6,1,4,1,3902,51,1,3,2,1),_DpiUploadIntervalSlot_Type())
dpiUploadIntervalSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiUploadIntervalSlot.setStatus(_A)
class _DpiUploadTimeInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,60))
_DpiUploadTimeInterval_Type.__name__=_B
_DpiUploadTimeInterval_Object=MibScalar
dpiUploadTimeInterval=_DpiUploadTimeInterval_Object((1,3,6,1,4,1,3902,51,1,3,2,2),_DpiUploadTimeInterval_Type())
dpiUploadTimeInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiUploadTimeInterval.setStatus(_A)
class _DpiUploadIntervalOK_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_E,1))
_DpiUploadIntervalOK_Type.__name__=_B
_DpiUploadIntervalOK_Object=MibScalar
dpiUploadIntervalOK=_DpiUploadIntervalOK_Object((1,3,6,1,4,1,3902,51,1,3,2,3),_DpiUploadIntervalOK_Type())
dpiUploadIntervalOK.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiUploadIntervalOK.setStatus(_A)
_DpiLogFileListDir_ObjectIdentity=ObjectIdentity
dpiLogFileListDir=_DpiLogFileListDir_ObjectIdentity((1,3,6,1,4,1,3902,51,1,3,3))
class _DpiLogFileListDirSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_DpiLogFileListDirSlot_Type.__name__=_B
_DpiLogFileListDirSlot_Object=MibScalar
dpiLogFileListDirSlot=_DpiLogFileListDirSlot_Object((1,3,6,1,4,1,3902,51,1,3,3,1),_DpiLogFileListDirSlot_Type())
dpiLogFileListDirSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiLogFileListDirSlot.setStatus(_A)
_DpiLogFileListDirFtpFile_Type=DisplayString
_DpiLogFileListDirFtpFile_Object=MibScalar
dpiLogFileListDirFtpFile=_DpiLogFileListDirFtpFile_Object((1,3,6,1,4,1,3902,51,1,3,3,2),_DpiLogFileListDirFtpFile_Type())
dpiLogFileListDirFtpFile.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiLogFileListDirFtpFile.setStatus(_A)
_DpiLogFileListDirLocalDir_Type=DisplayString
_DpiLogFileListDirLocalDir_Object=MibScalar
dpiLogFileListDirLocalDir=_DpiLogFileListDirLocalDir_Object((1,3,6,1,4,1,3902,51,1,3,3,3),_DpiLogFileListDirLocalDir_Type())
dpiLogFileListDirLocalDir.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiLogFileListDirLocalDir.setStatus(_A)
class _DpiLogFileListDirOK_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_E,1))
_DpiLogFileListDirOK_Type.__name__=_B
_DpiLogFileListDirOK_Object=MibScalar
dpiLogFileListDirOK=_DpiLogFileListDirOK_Object((1,3,6,1,4,1,3902,51,1,3,3,4),_DpiLogFileListDirOK_Type())
dpiLogFileListDirOK.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiLogFileListDirOK.setStatus(_A)
_DpiLogFileDeleteDir_ObjectIdentity=ObjectIdentity
dpiLogFileDeleteDir=_DpiLogFileDeleteDir_ObjectIdentity((1,3,6,1,4,1,3902,51,1,3,4))
class _DpiLogFileDeleteDirSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_DpiLogFileDeleteDirSlot_Type.__name__=_B
_DpiLogFileDeleteDirSlot_Object=MibScalar
dpiLogFileDeleteDirSlot=_DpiLogFileDeleteDirSlot_Object((1,3,6,1,4,1,3902,51,1,3,4,1),_DpiLogFileDeleteDirSlot_Type())
dpiLogFileDeleteDirSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiLogFileDeleteDirSlot.setStatus(_A)
_DpiLogFileDeleteDirName_Type=DisplayString
_DpiLogFileDeleteDirName_Object=MibScalar
dpiLogFileDeleteDirName=_DpiLogFileDeleteDirName_Object((1,3,6,1,4,1,3902,51,1,3,4,2),_DpiLogFileDeleteDirName_Type())
dpiLogFileDeleteDirName.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiLogFileDeleteDirName.setStatus(_A)
class _DpiLogFileDeleteDirOK_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_E,1))
_DpiLogFileDeleteDirOK_Type.__name__=_B
_DpiLogFileDeleteDirOK_Object=MibScalar
dpiLogFileDeleteDirOK=_DpiLogFileDeleteDirOK_Object((1,3,6,1,4,1,3902,51,1,3,4,3),_DpiLogFileDeleteDirOK_Type())
dpiLogFileDeleteDirOK.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiLogFileDeleteDirOK.setStatus(_A)
_DpiLogFileDeleteFile_ObjectIdentity=ObjectIdentity
dpiLogFileDeleteFile=_DpiLogFileDeleteFile_ObjectIdentity((1,3,6,1,4,1,3902,51,1,3,5))
class _DpiLogFileDeleteFileSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_DpiLogFileDeleteFileSlot_Type.__name__=_B
_DpiLogFileDeleteFileSlot_Object=MibScalar
dpiLogFileDeleteFileSlot=_DpiLogFileDeleteFileSlot_Object((1,3,6,1,4,1,3902,51,1,3,5,1),_DpiLogFileDeleteFileSlot_Type())
dpiLogFileDeleteFileSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiLogFileDeleteFileSlot.setStatus(_A)
_DpiLogFileDeleteFileName_Type=DisplayString
_DpiLogFileDeleteFileName_Object=MibScalar
dpiLogFileDeleteFileName=_DpiLogFileDeleteFileName_Object((1,3,6,1,4,1,3902,51,1,3,5,2),_DpiLogFileDeleteFileName_Type())
dpiLogFileDeleteFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiLogFileDeleteFileName.setStatus(_A)
class _DpiLogFileDeleteFileOK_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_E,1))
_DpiLogFileDeleteFileOK_Type.__name__=_B
_DpiLogFileDeleteFileOK_Object=MibScalar
dpiLogFileDeleteFileOK=_DpiLogFileDeleteFileOK_Object((1,3,6,1,4,1,3902,51,1,3,5,3),_DpiLogFileDeleteFileOK_Type())
dpiLogFileDeleteFileOK.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiLogFileDeleteFileOK.setStatus(_A)
_DpiUpdateDpiLog_ObjectIdentity=ObjectIdentity
dpiUpdateDpiLog=_DpiUpdateDpiLog_ObjectIdentity((1,3,6,1,4,1,3902,51,1,3,6))
class _DpiUpdateDpiLogSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_DpiUpdateDpiLogSlot_Type.__name__=_B
_DpiUpdateDpiLogSlot_Object=MibScalar
dpiUpdateDpiLogSlot=_DpiUpdateDpiLogSlot_Object((1,3,6,1,4,1,3902,51,1,3,6,1),_DpiUpdateDpiLogSlot_Type())
dpiUpdateDpiLogSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiUpdateDpiLogSlot.setStatus(_A)
_DpiLogServerFileName_Type=DisplayString
_DpiLogServerFileName_Object=MibScalar
dpiLogServerFileName=_DpiLogServerFileName_Object((1,3,6,1,4,1,3902,51,1,3,6,3),_DpiLogServerFileName_Type())
dpiLogServerFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiLogServerFileName.setStatus(_A)
_DpiLogLocalFileName_Type=DisplayString
_DpiLogLocalFileName_Object=MibScalar
dpiLogLocalFileName=_DpiLogLocalFileName_Object((1,3,6,1,4,1,3902,51,1,3,6,5),_DpiLogLocalFileName_Type())
dpiLogLocalFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiLogLocalFileName.setStatus(_A)
class _DpiUpdateDpiLogOK_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_E,1))
_DpiUpdateDpiLogOK_Type.__name__=_B
_DpiUpdateDpiLogOK_Object=MibScalar
dpiUpdateDpiLogOK=_DpiUpdateDpiLogOK_Object((1,3,6,1,4,1,3902,51,1,3,6,6),_DpiUpdateDpiLogOK_Type())
dpiUpdateDpiLogOK.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiUpdateDpiLogOK.setStatus(_A)
class _DpiUploadTodayLog_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_DpiUploadTodayLog_Type.__name__=_B
_DpiUploadTodayLog_Object=MibScalar
dpiUploadTodayLog=_DpiUploadTodayLog_Object((1,3,6,1,4,1,3902,51,1,3,7),_DpiUploadTodayLog_Type())
dpiUploadTodayLog.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiUploadTodayLog.setStatus(_A)
class _DpiCommit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_E,1))
_DpiCommit_Type.__name__=_B
_DpiCommit_Object=MibScalar
dpiCommit=_DpiCommit_Object((1,3,6,1,4,1,3902,51,1,4),_DpiCommit_Type())
dpiCommit.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiCommit.setStatus(_A)
class _DpiUpdateSignatureVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_E,1))
_DpiUpdateSignatureVersion_Type.__name__=_B
_DpiUpdateSignatureVersion_Object=MibScalar
dpiUpdateSignatureVersion=_DpiUpdateSignatureVersion_Object((1,3,6,1,4,1,3902,51,1,5),_DpiUpdateSignatureVersion_Type())
dpiUpdateSignatureVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiUpdateSignatureVersion.setStatus(_A)
_DpiVlanBindDpiTemplate_ObjectIdentity=ObjectIdentity
dpiVlanBindDpiTemplate=_DpiVlanBindDpiTemplate_ObjectIdentity((1,3,6,1,4,1,3902,51,1,6))
_DpiVlanInterfaceName_Type=DisplayString
_DpiVlanInterfaceName_Object=MibScalar
dpiVlanInterfaceName=_DpiVlanInterfaceName_Object((1,3,6,1,4,1,3902,51,1,6,1),_DpiVlanInterfaceName_Type())
dpiVlanInterfaceName.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiVlanInterfaceName.setStatus(_A)
class _DpiBindDpiTemplate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_DpiBindDpiTemplate_Type.__name__=_B
_DpiBindDpiTemplate_Object=MibScalar
dpiBindDpiTemplate=_DpiBindDpiTemplate_Object((1,3,6,1,4,1,3902,51,1,6,2),_DpiBindDpiTemplate_Type())
dpiBindDpiTemplate.setMaxAccess(_C)
if mibBuilder.loadTexts:dpiBindDpiTemplate.setStatus(_A)
_DpiShowAllSignatureEntryTable_Object=MibTable
dpiShowAllSignatureEntryTable=_DpiShowAllSignatureEntryTable_Object((1,3,6,1,4,1,3902,51,1,7))
if mibBuilder.loadTexts:dpiShowAllSignatureEntryTable.setStatus(_A)
_DpiShowAllSignatureEntry_Object=MibTableRow
dpiShowAllSignatureEntry=_DpiShowAllSignatureEntry_Object((1,3,6,1,4,1,3902,51,1,7,1))
dpiShowAllSignatureEntry.setIndexNames((0,_F,_Q))
if mibBuilder.loadTexts:dpiShowAllSignatureEntry.setStatus(_A)
class _DpiAllSignatureEntryID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12287))
_DpiAllSignatureEntryID_Type.__name__=_B
_DpiAllSignatureEntryID_Object=MibTableColumn
dpiAllSignatureEntryID=_DpiAllSignatureEntryID_Object((1,3,6,1,4,1,3902,51,1,7,1,1),_DpiAllSignatureEntryID_Type())
dpiAllSignatureEntryID.setMaxAccess(_D)
if mibBuilder.loadTexts:dpiAllSignatureEntryID.setStatus(_A)
_DpiAllSignatureEntryContent_Type=DisplayString
_DpiAllSignatureEntryContent_Object=MibTableColumn
dpiAllSignatureEntryContent=_DpiAllSignatureEntryContent_Object((1,3,6,1,4,1,3902,51,1,7,1,2),_DpiAllSignatureEntryContent_Type())
dpiAllSignatureEntryContent.setMaxAccess(_D)
if mibBuilder.loadTexts:dpiAllSignatureEntryContent.setStatus(_A)
_DpiShowAllSignatureSymbolTable_Object=MibTable
dpiShowAllSignatureSymbolTable=_DpiShowAllSignatureSymbolTable_Object((1,3,6,1,4,1,3902,51,1,8))
if mibBuilder.loadTexts:dpiShowAllSignatureSymbolTable.setStatus(_A)
_DpiShowAllSignatureSymbolEntry_Object=MibTableRow
dpiShowAllSignatureSymbolEntry=_DpiShowAllSignatureSymbolEntry_Object((1,3,6,1,4,1,3902,51,1,8,1))
dpiShowAllSignatureSymbolEntry.setIndexNames((0,_F,_R))
if mibBuilder.loadTexts:dpiShowAllSignatureSymbolEntry.setStatus(_A)
class _DpiAllSignatureSymbolID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6143))
_DpiAllSignatureSymbolID_Type.__name__=_B
_DpiAllSignatureSymbolID_Object=MibTableColumn
dpiAllSignatureSymbolID=_DpiAllSignatureSymbolID_Object((1,3,6,1,4,1,3902,51,1,8,1,1),_DpiAllSignatureSymbolID_Type())
dpiAllSignatureSymbolID.setMaxAccess(_D)
if mibBuilder.loadTexts:dpiAllSignatureSymbolID.setStatus(_A)
_DpiAllSignatureSymbolEntryList_Type=DisplayString
_DpiAllSignatureSymbolEntryList_Object=MibTableColumn
dpiAllSignatureSymbolEntryList=_DpiAllSignatureSymbolEntryList_Object((1,3,6,1,4,1,3902,51,1,8,1,2),_DpiAllSignatureSymbolEntryList_Type())
dpiAllSignatureSymbolEntryList.setMaxAccess(_D)
if mibBuilder.loadTexts:dpiAllSignatureSymbolEntryList.setStatus(_A)
class _DpiAllSignatureSymbolHitNumLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_DpiAllSignatureSymbolHitNumLimit_Type.__name__=_B
_DpiAllSignatureSymbolHitNumLimit_Object=MibTableColumn
dpiAllSignatureSymbolHitNumLimit=_DpiAllSignatureSymbolHitNumLimit_Object((1,3,6,1,4,1,3902,51,1,8,1,3),_DpiAllSignatureSymbolHitNumLimit_Type())
dpiAllSignatureSymbolHitNumLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:dpiAllSignatureSymbolHitNumLimit.setStatus(_A)
class _DpiAllSignatureSymbolProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('normal',1),('inherit',2)))
_DpiAllSignatureSymbolProtocol_Type.__name__=_B
_DpiAllSignatureSymbolProtocol_Object=MibTableColumn
dpiAllSignatureSymbolProtocol=_DpiAllSignatureSymbolProtocol_Object((1,3,6,1,4,1,3902,51,1,8,1,4),_DpiAllSignatureSymbolProtocol_Type())
dpiAllSignatureSymbolProtocol.setMaxAccess(_D)
if mibBuilder.loadTexts:dpiAllSignatureSymbolProtocol.setStatus(_A)
_DpiShowAllFlowPoolTable_Object=MibTable
dpiShowAllFlowPoolTable=_DpiShowAllFlowPoolTable_Object((1,3,6,1,4,1,3902,51,1,9))
if mibBuilder.loadTexts:dpiShowAllFlowPoolTable.setStatus(_A)
_DpiShowAllFlowPoolEntry_Object=MibTableRow
dpiShowAllFlowPoolEntry=_DpiShowAllFlowPoolEntry_Object((1,3,6,1,4,1,3902,51,1,9,1))
dpiShowAllFlowPoolEntry.setIndexNames((0,_F,_S))
if mibBuilder.loadTexts:dpiShowAllFlowPoolEntry.setStatus(_A)
class _DpiAllFlowPoolID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,8191))
_DpiAllFlowPoolID_Type.__name__=_B
_DpiAllFlowPoolID_Object=MibTableColumn
dpiAllFlowPoolID=_DpiAllFlowPoolID_Object((1,3,6,1,4,1,3902,51,1,9,1,1),_DpiAllFlowPoolID_Type())
dpiAllFlowPoolID.setMaxAccess(_D)
if mibBuilder.loadTexts:dpiAllFlowPoolID.setStatus(_A)
class _DpiAllUpStreamRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,100000))
_DpiAllUpStreamRate_Type.__name__=_B
_DpiAllUpStreamRate_Object=MibTableColumn
dpiAllUpStreamRate=_DpiAllUpStreamRate_Object((1,3,6,1,4,1,3902,51,1,9,1,2),_DpiAllUpStreamRate_Type())
dpiAllUpStreamRate.setMaxAccess(_D)
if mibBuilder.loadTexts:dpiAllUpStreamRate.setStatus(_A)
_DpiAllUpStreamCbs_Type=Integer32
_DpiAllUpStreamCbs_Object=MibTableColumn
dpiAllUpStreamCbs=_DpiAllUpStreamCbs_Object((1,3,6,1,4,1,3902,51,1,9,1,3),_DpiAllUpStreamCbs_Type())
dpiAllUpStreamCbs.setMaxAccess(_D)
if mibBuilder.loadTexts:dpiAllUpStreamCbs.setStatus(_A)
_DpiAllUpStreamEbs_Type=Integer32
_DpiAllUpStreamEbs_Object=MibTableColumn
dpiAllUpStreamEbs=_DpiAllUpStreamEbs_Object((1,3,6,1,4,1,3902,51,1,9,1,4),_DpiAllUpStreamEbs_Type())
dpiAllUpStreamEbs.setMaxAccess(_D)
if mibBuilder.loadTexts:dpiAllUpStreamEbs.setStatus(_A)
class _DpiAllDownStreamRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,100000))
_DpiAllDownStreamRate_Type.__name__=_B
_DpiAllDownStreamRate_Object=MibTableColumn
dpiAllDownStreamRate=_DpiAllDownStreamRate_Object((1,3,6,1,4,1,3902,51,1,9,1,5),_DpiAllDownStreamRate_Type())
dpiAllDownStreamRate.setMaxAccess(_D)
if mibBuilder.loadTexts:dpiAllDownStreamRate.setStatus(_A)
_DpiAllDownStreamCbs_Type=Integer32
_DpiAllDownStreamCbs_Object=MibTableColumn
dpiAllDownStreamCbs=_DpiAllDownStreamCbs_Object((1,3,6,1,4,1,3902,51,1,9,1,6),_DpiAllDownStreamCbs_Type())
dpiAllDownStreamCbs.setMaxAccess(_D)
if mibBuilder.loadTexts:dpiAllDownStreamCbs.setStatus(_A)
_DpiAllDownStreamEbs_Type=Integer32
_DpiAllDownStreamEbs_Object=MibTableColumn
dpiAllDownStreamEbs=_DpiAllDownStreamEbs_Object((1,3,6,1,4,1,3902,51,1,9,1,7),_DpiAllDownStreamEbs_Type())
dpiAllDownStreamEbs.setMaxAccess(_D)
if mibBuilder.loadTexts:dpiAllDownStreamEbs.setStatus(_A)
_DpiShowAllSubserviceTable_Object=MibTable
dpiShowAllSubserviceTable=_DpiShowAllSubserviceTable_Object((1,3,6,1,4,1,3902,51,1,10))
if mibBuilder.loadTexts:dpiShowAllSubserviceTable.setStatus(_A)
_DpiShowAllSubserviceEntry_Object=MibTableRow
dpiShowAllSubserviceEntry=_DpiShowAllSubserviceEntry_Object((1,3,6,1,4,1,3902,51,1,10,1))
dpiShowAllSubserviceEntry.setIndexNames((0,_F,_T))
if mibBuilder.loadTexts:dpiShowAllSubserviceEntry.setStatus(_A)
class _DpiAllSubserviceID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8191))
_DpiAllSubserviceID_Type.__name__=_B
_DpiAllSubserviceID_Object=MibTableColumn
dpiAllSubserviceID=_DpiAllSubserviceID_Object((1,3,6,1,4,1,3902,51,1,10,1,1),_DpiAllSubserviceID_Type())
dpiAllSubserviceID.setMaxAccess(_D)
if mibBuilder.loadTexts:dpiAllSubserviceID.setStatus(_A)
class _DpiAllSubserviceFlowpoolID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,8191))
_DpiAllSubserviceFlowpoolID_Type.__name__=_B
_DpiAllSubserviceFlowpoolID_Object=MibTableColumn
dpiAllSubserviceFlowpoolID=_DpiAllSubserviceFlowpoolID_Object((1,3,6,1,4,1,3902,51,1,10,1,3),_DpiAllSubserviceFlowpoolID_Type())
dpiAllSubserviceFlowpoolID.setMaxAccess(_D)
if mibBuilder.loadTexts:dpiAllSubserviceFlowpoolID.setStatus(_A)
class _DpiAllSubserviceAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_DpiAllSubserviceAction_Type.__name__=_B
_DpiAllSubserviceAction_Object=MibTableColumn
dpiAllSubserviceAction=_DpiAllSubserviceAction_Object((1,3,6,1,4,1,3902,51,1,10,1,4),_DpiAllSubserviceAction_Type())
dpiAllSubserviceAction.setMaxAccess(_D)
if mibBuilder.loadTexts:dpiAllSubserviceAction.setStatus(_A)
class _DpiAllSubserviceAgingTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_DpiAllSubserviceAgingTime_Type.__name__=_B
_DpiAllSubserviceAgingTime_Object=MibTableColumn
dpiAllSubserviceAgingTime=_DpiAllSubserviceAgingTime_Object((1,3,6,1,4,1,3902,51,1,10,1,5),_DpiAllSubserviceAgingTime_Type())
dpiAllSubserviceAgingTime.setMaxAccess(_D)
if mibBuilder.loadTexts:dpiAllSubserviceAgingTime.setStatus(_A)
_DpiAllSubserviceSymbolList_Type=DisplayString
_DpiAllSubserviceSymbolList_Object=MibTableColumn
dpiAllSubserviceSymbolList=_DpiAllSubserviceSymbolList_Object((1,3,6,1,4,1,3902,51,1,10,1,6),_DpiAllSubserviceSymbolList_Type())
dpiAllSubserviceSymbolList.setMaxAccess(_D)
if mibBuilder.loadTexts:dpiAllSubserviceSymbolList.setStatus(_A)
_DpiAllSubserviceProtocol_Type=DisplayString
_DpiAllSubserviceProtocol_Object=MibTableColumn
dpiAllSubserviceProtocol=_DpiAllSubserviceProtocol_Object((1,3,6,1,4,1,3902,51,1,10,1,7),_DpiAllSubserviceProtocol_Type())
dpiAllSubserviceProtocol.setMaxAccess(_D)
if mibBuilder.loadTexts:dpiAllSubserviceProtocol.setStatus(_A)
_DpiShowAllServiceTable_Object=MibTable
dpiShowAllServiceTable=_DpiShowAllServiceTable_Object((1,3,6,1,4,1,3902,51,1,11))
if mibBuilder.loadTexts:dpiShowAllServiceTable.setStatus(_A)
_DpiShowAllServiceEntry_Object=MibTableRow
dpiShowAllServiceEntry=_DpiShowAllServiceEntry_Object((1,3,6,1,4,1,3902,51,1,11,1))
dpiShowAllServiceEntry.setIndexNames((0,_F,_U))
if mibBuilder.loadTexts:dpiShowAllServiceEntry.setStatus(_A)
class _DpiAllServiceID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2047))
_DpiAllServiceID_Type.__name__=_B
_DpiAllServiceID_Object=MibTableColumn
dpiAllServiceID=_DpiAllServiceID_Object((1,3,6,1,4,1,3902,51,1,11,1,1),_DpiAllServiceID_Type())
dpiAllServiceID.setMaxAccess(_D)
if mibBuilder.loadTexts:dpiAllServiceID.setStatus(_A)
class _DpiAllServiceFlowPoolID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,8191))
_DpiAllServiceFlowPoolID_Type.__name__=_B
_DpiAllServiceFlowPoolID_Object=MibTableColumn
dpiAllServiceFlowPoolID=_DpiAllServiceFlowPoolID_Object((1,3,6,1,4,1,3902,51,1,11,1,2),_DpiAllServiceFlowPoolID_Type())
dpiAllServiceFlowPoolID.setMaxAccess(_D)
if mibBuilder.loadTexts:dpiAllServiceFlowPoolID.setStatus(_A)
class _DpiAllServiceSubserviceNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8191))
_DpiAllServiceSubserviceNum_Type.__name__=_B
_DpiAllServiceSubserviceNum_Object=MibTableColumn
dpiAllServiceSubserviceNum=_DpiAllServiceSubserviceNum_Object((1,3,6,1,4,1,3902,51,1,11,1,4),_DpiAllServiceSubserviceNum_Type())
dpiAllServiceSubserviceNum.setMaxAccess(_D)
if mibBuilder.loadTexts:dpiAllServiceSubserviceNum.setStatus(_A)
class _DpiAllServiceSubserviceList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1049))
_DpiAllServiceSubserviceList_Type.__name__=_I
_DpiAllServiceSubserviceList_Object=MibTableColumn
dpiAllServiceSubserviceList=_DpiAllServiceSubserviceList_Object((1,3,6,1,4,1,3902,51,1,11,1,5),_DpiAllServiceSubserviceList_Type())
dpiAllServiceSubserviceList.setMaxAccess(_D)
if mibBuilder.loadTexts:dpiAllServiceSubserviceList.setStatus(_A)
_DpiShowAllTemplateTable_Object=MibTable
dpiShowAllTemplateTable=_DpiShowAllTemplateTable_Object((1,3,6,1,4,1,3902,51,1,12))
if mibBuilder.loadTexts:dpiShowAllTemplateTable.setStatus(_A)
_DpiShowAllTemplateEntry_Object=MibTableRow
dpiShowAllTemplateEntry=_DpiShowAllTemplateEntry_Object((1,3,6,1,4,1,3902,51,1,12,1))
dpiShowAllTemplateEntry.setIndexNames((0,_F,_V))
if mibBuilder.loadTexts:dpiShowAllTemplateEntry.setStatus(_A)
class _DpiAllTemplateID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_DpiAllTemplateID_Type.__name__=_B
_DpiAllTemplateID_Object=MibTableColumn
dpiAllTemplateID=_DpiAllTemplateID_Object((1,3,6,1,4,1,3902,51,1,12,1,1),_DpiAllTemplateID_Type())
dpiAllTemplateID.setMaxAccess(_D)
if mibBuilder.loadTexts:dpiAllTemplateID.setStatus(_A)
_DpiAllTemplateCfgCmd_Type=DisplayString
_DpiAllTemplateCfgCmd_Object=MibTableColumn
dpiAllTemplateCfgCmd=_DpiAllTemplateCfgCmd_Object((1,3,6,1,4,1,3902,51,1,12,1,2),_DpiAllTemplateCfgCmd_Type())
dpiAllTemplateCfgCmd.setMaxAccess(_D)
if mibBuilder.loadTexts:dpiAllTemplateCfgCmd.setStatus(_A)
_DpiShowAllMnpIpTable_Object=MibTable
dpiShowAllMnpIpTable=_DpiShowAllMnpIpTable_Object((1,3,6,1,4,1,3902,51,1,13))
if mibBuilder.loadTexts:dpiShowAllMnpIpTable.setStatus(_A)
_DpiShowAllMngIpEntry_Object=MibTableRow
dpiShowAllMngIpEntry=_DpiShowAllMngIpEntry_Object((1,3,6,1,4,1,3902,51,1,13,1))
dpiShowAllMngIpEntry.setIndexNames((0,_F,_W))
if mibBuilder.loadTexts:dpiShowAllMngIpEntry.setStatus(_A)
class _DpiAllSlotID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_DpiAllSlotID_Type.__name__=_B
_DpiAllSlotID_Object=MibTableColumn
dpiAllSlotID=_DpiAllSlotID_Object((1,3,6,1,4,1,3902,51,1,13,1,1),_DpiAllSlotID_Type())
dpiAllSlotID.setMaxAccess(_D)
if mibBuilder.loadTexts:dpiAllSlotID.setStatus(_A)
_DpiAllMngIp_Type=IpAddress
_DpiAllMngIp_Object=MibTableColumn
dpiAllMngIp=_DpiAllMngIp_Object((1,3,6,1,4,1,3902,51,1,13,1,2),_DpiAllMngIp_Type())
dpiAllMngIp.setMaxAccess(_D)
if mibBuilder.loadTexts:dpiAllMngIp.setStatus(_A)
_DpiAllServerIp_Type=IpAddress
_DpiAllServerIp_Object=MibTableColumn
dpiAllServerIp=_DpiAllServerIp_Object((1,3,6,1,4,1,3902,51,1,13,1,3),_DpiAllServerIp_Type())
dpiAllServerIp.setMaxAccess(_D)
if mibBuilder.loadTexts:dpiAllServerIp.setStatus(_A)
class _DpiAllMngIpIsUsed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_X,0),('used',1)))
_DpiAllMngIpIsUsed_Type.__name__=_B
_DpiAllMngIpIsUsed_Object=MibTableColumn
dpiAllMngIpIsUsed=_DpiAllMngIpIsUsed_Object((1,3,6,1,4,1,3902,51,1,13,1,4),_DpiAllMngIpIsUsed_Type())
dpiAllMngIpIsUsed.setMaxAccess(_D)
if mibBuilder.loadTexts:dpiAllMngIpIsUsed.setStatus(_A)
_DpiAllLogSaveInterval_Type=Integer32
_DpiAllLogSaveInterval_Object=MibTableColumn
dpiAllLogSaveInterval=_DpiAllLogSaveInterval_Object((1,3,6,1,4,1,3902,51,1,13,1,5),_DpiAllLogSaveInterval_Type())
dpiAllLogSaveInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:dpiAllLogSaveInterval.setStatus(_A)
class _DpiAllLogAutoUpload_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_P,0),(_E,1)))
_DpiAllLogAutoUpload_Type.__name__=_B
_DpiAllLogAutoUpload_Object=MibTableColumn
dpiAllLogAutoUpload=_DpiAllLogAutoUpload_Object((1,3,6,1,4,1,3902,51,1,13,1,6),_DpiAllLogAutoUpload_Type())
dpiAllLogAutoUpload.setMaxAccess(_D)
if mibBuilder.loadTexts:dpiAllLogAutoUpload.setStatus(_A)
_DpiAllLogUploadInterval_Type=Integer32
_DpiAllLogUploadInterval_Object=MibTableColumn
dpiAllLogUploadInterval=_DpiAllLogUploadInterval_Object((1,3,6,1,4,1,3902,51,1,13,1,7),_DpiAllLogUploadInterval_Type())
dpiAllLogUploadInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:dpiAllLogUploadInterval.setStatus(_A)
_DpiShowAllVlanDpiTable_Object=MibTable
dpiShowAllVlanDpiTable=_DpiShowAllVlanDpiTable_Object((1,3,6,1,4,1,3902,51,1,14))
if mibBuilder.loadTexts:dpiShowAllVlanDpiTable.setStatus(_A)
_DpiShowAllVlanDpiEntry_Object=MibTableRow
dpiShowAllVlanDpiEntry=_DpiShowAllVlanDpiEntry_Object((1,3,6,1,4,1,3902,51,1,14,1))
dpiShowAllVlanDpiEntry.setIndexNames((0,_F,_Y))
if mibBuilder.loadTexts:dpiShowAllVlanDpiEntry.setStatus(_A)
_DpiAllVlanID_Type=Integer32
_DpiAllVlanID_Object=MibTableColumn
dpiAllVlanID=_DpiAllVlanID_Object((1,3,6,1,4,1,3902,51,1,14,1,1),_DpiAllVlanID_Type())
dpiAllVlanID.setMaxAccess(_D)
if mibBuilder.loadTexts:dpiAllVlanID.setStatus(_A)
_DpiAllVlanBindTemplateID_Type=Integer32
_DpiAllVlanBindTemplateID_Object=MibTableColumn
dpiAllVlanBindTemplateID=_DpiAllVlanBindTemplateID_Object((1,3,6,1,4,1,3902,51,1,14,1,2),_DpiAllVlanBindTemplateID_Type())
dpiAllVlanBindTemplateID.setMaxAccess(_D)
if mibBuilder.loadTexts:dpiAllVlanBindTemplateID.setStatus(_A)
_DpiAllVlanBindSlotID_Type=Integer32
_DpiAllVlanBindSlotID_Object=MibTableColumn
dpiAllVlanBindSlotID=_DpiAllVlanBindSlotID_Object((1,3,6,1,4,1,3902,51,1,14,1,3),_DpiAllVlanBindSlotID_Type())
dpiAllVlanBindSlotID.setMaxAccess(_D)
if mibBuilder.loadTexts:dpiAllVlanBindSlotID.setStatus(_A)
_DpiAllVlanBindServiceID_Type=Integer32
_DpiAllVlanBindServiceID_Object=MibTableColumn
dpiAllVlanBindServiceID=_DpiAllVlanBindServiceID_Object((1,3,6,1,4,1,3902,51,1,14,1,4),_DpiAllVlanBindServiceID_Type())
dpiAllVlanBindServiceID.setMaxAccess(_D)
if mibBuilder.loadTexts:dpiAllVlanBindServiceID.setStatus(_A)
class _DpiAllVlanBindIsUsed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_X,0),('used',1)))
_DpiAllVlanBindIsUsed_Type.__name__=_B
_DpiAllVlanBindIsUsed_Object=MibTableColumn
dpiAllVlanBindIsUsed=_DpiAllVlanBindIsUsed_Object((1,3,6,1,4,1,3902,51,1,14,1,5),_DpiAllVlanBindIsUsed_Type())
dpiAllVlanBindIsUsed.setMaxAccess(_D)
if mibBuilder.loadTexts:dpiAllVlanBindIsUsed.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'zte':zte,'fwdpi':fwdpi,'zxrDPI':zxrDPI,'dpiSystemControl':dpiSystemControl,'dpiSlotNumber':dpiSlotNumber,'dpiRestartFunc':dpiRestartFunc,'dpiConfigMode':dpiConfigMode,'dpiBindMngServiceIp':dpiBindMngServiceIp,'dpiMngServerSlot':dpiMngServerSlot,'dpiMngIp':dpiMngIp,'dpiServerIp':dpiServerIp,'dpiMngServerOK':dpiMngServerOK,'dpiSignatureEntry':dpiSignatureEntry,'dpiCurrentSignatureEntry':dpiCurrentSignatureEntry,'dpiShowSignatureEntry':dpiShowSignatureEntry,'dpiSignatureEntryTable':dpiSignatureEntryTable,'dpiSignatureTableEntry':dpiSignatureTableEntry,_J:dpiSignatureEntryID,'dpiSignatureEntryContent':dpiSignatureEntryContent,'dpiSetContent':dpiSetContent,'dpiSignatureSymbol':dpiSignatureSymbol,'dpiCurrentSignatureSymbol':dpiCurrentSignatureSymbol,'dpiShowSignatureSymbol':dpiShowSignatureSymbol,'dpiSignatureSymbolTable':dpiSignatureSymbolTable,'dpiSignatureSymbolTableEntry':dpiSignatureSymbolTableEntry,_K:dpiSignatureSymbolID,'dpiSignatureSymbolEntryID':dpiSignatureSymbolEntryID,'dpiSignatureSymbolHitNumLimit':dpiSignatureSymbolHitNumLimit,'dpiAddSignatureEntry':dpiAddSignatureEntry,'dpiNoAddSignatureEntry':dpiNoAddSignatureEntry,'dpiSetHitNumLimit':dpiSetHitNumLimit,'dpiFlowPool':dpiFlowPool,'dpiCurrentFlowPool':dpiCurrentFlowPool,'dpiShowFlowPool':dpiShowFlowPool,'dpiStreamLimitTable':dpiStreamLimitTable,'dpiStreamLimitTableEntry':dpiStreamLimitTableEntry,_L:dpiStreamLimitID,_M:dpiStreamLimitType,'dpiStreamRate':dpiStreamRate,'dpiStreamCbs':dpiStreamCbs,'dpiStreamEbs':dpiStreamEbs,'dpiUpStreamRateLimit':dpiUpStreamRateLimit,'dpiUpStreamRate':dpiUpStreamRate,'dpiUpStreamCbs':dpiUpStreamCbs,'dpiUpStreamEbs':dpiUpStreamEbs,'dpiUpStreamOK':dpiUpStreamOK,'dpiNoUpStreamRateLimit':dpiNoUpStreamRateLimit,'dpiDownStreamRateLimit':dpiDownStreamRateLimit,'dpiDownStreamRate':dpiDownStreamRate,'dpiDownStreamCbs':dpiDownStreamCbs,'dpiDownStreamEbs':dpiDownStreamEbs,'dpiDownStreamOK':dpiDownStreamOK,'dpiNoDownStreamRateLimit':dpiNoDownStreamRateLimit,'dpiSubservice':dpiSubservice,'dpiCurrentSubservice':dpiCurrentSubservice,'dpiShowSubservice':dpiShowSubservice,'dpiSubserviceTable':dpiSubserviceTable,'dpiSubserviceEntry':dpiSubserviceEntry,_N:dpiSubserviceID,'dpiSubserviceSymbolNum':dpiSubserviceSymbolNum,'dpiSubserviceFlowpoolID':dpiSubserviceFlowpoolID,'dpiSubserviceAction':dpiSubserviceAction,'dpiSubserviceAgingTime':dpiSubserviceAgingTime,'dpiSubserviceSymbolList':dpiSubserviceSymbolList,'dpiAddSignatureSymbol':dpiAddSignatureSymbol,'dpiAddSignatureSymbolId':dpiAddSignatureSymbolId,'dpiAddSignatureSymbolRelationName':dpiAddSignatureSymbolRelationName,'dpiAddSignatureSymbolOK':dpiAddSignatureSymbolOK,'dpiNoAddSignatureSymbol':dpiNoAddSignatureSymbol,'dpiAddProtocol':dpiAddProtocol,'dpiNoAddProtocol':dpiNoAddProtocol,'dpiBindFlowPool':dpiBindFlowPool,'dpiNoBindFlowPool':dpiNoBindFlowPool,'dpiSetAction':dpiSetAction,'dpiSetAgingTime':dpiSetAgingTime,'dpiService':dpiService,'dpiCurrentService':dpiCurrentService,'dpiShowService':dpiShowService,'dpiServiceTable':dpiServiceTable,'dpiServiceEntry':dpiServiceEntry,_O:dpiServiceID,'dpiServiceFlowPoolID':dpiServiceFlowPoolID,'dpiServiceConnectionLimit':dpiServiceConnectionLimit,'dpiServiceSubserviceNum':dpiServiceSubserviceNum,'dpiServiceSubserviceList':dpiServiceSubserviceList,'dpiAddSubservice':dpiAddSubservice,'dpiNoAddSubservice':dpiNoAddSubservice,'dpiImportSubservice':dpiImportSubservice,'dpiImportDestSubservice':dpiImportDestSubservice,'dpiImportSrcSubservice':dpiImportSrcSubservice,'dpiImportSubserviceOK':dpiImportSubserviceOK,'dpiNoImportSubservice':dpiNoImportSubservice,'dpiServiceBindFlowPool':dpiServiceBindFlowPool,'dpiServiceNoBindFlowPool':dpiServiceNoBindFlowPool,'dpiTemplate':dpiTemplate,'dpiCurrentTemplate':dpiCurrentTemplate,'dpiBindSlot':dpiBindSlot,'dpiNoBindSlot':dpiNoBindSlot,'dpiBindService':dpiBindService,'dpiNoBindService':dpiNoBindService,'dpiBindSipAddr':dpiBindSipAddr,'dpiSipAddress':dpiSipAddress,'dpiSipMask':dpiSipMask,'dpiSipServiceID':dpiSipServiceID,'dpiBindSipAddrOK':dpiBindSipAddrOK,'dpiNoBindSipAddr':dpiNoBindSipAddr,'dpiShowIpService':dpiShowIpService,'dpiBindSwitchport':dpiBindSwitchport,'dpiBindSwitchportPort':dpiBindSwitchportPort,'dpiBindSwitchService':dpiBindSwitchService,'dpiBindSwitchportOK':dpiBindSwitchportOK,'dpiNoBindSwitchport':dpiNoBindSwitchport,'dpiShowPortService':dpiShowPortService,'dpiSetActiceConnectionSaveInterval':dpiSetActiceConnectionSaveInterval,'dpiClearConnectionAll':dpiClearConnectionAll,'dpiMonitorLog':dpiMonitorLog,'dpiUploadAuto':dpiUploadAuto,'dpiUploadAutoSlot':dpiUploadAutoSlot,'dpiUploadAutoEnable':dpiUploadAutoEnable,'dpiUploadAutoOK':dpiUploadAutoOK,'dpiUploadInterval':dpiUploadInterval,'dpiUploadIntervalSlot':dpiUploadIntervalSlot,'dpiUploadTimeInterval':dpiUploadTimeInterval,'dpiUploadIntervalOK':dpiUploadIntervalOK,'dpiLogFileListDir':dpiLogFileListDir,'dpiLogFileListDirSlot':dpiLogFileListDirSlot,'dpiLogFileListDirFtpFile':dpiLogFileListDirFtpFile,'dpiLogFileListDirLocalDir':dpiLogFileListDirLocalDir,'dpiLogFileListDirOK':dpiLogFileListDirOK,'dpiLogFileDeleteDir':dpiLogFileDeleteDir,'dpiLogFileDeleteDirSlot':dpiLogFileDeleteDirSlot,'dpiLogFileDeleteDirName':dpiLogFileDeleteDirName,'dpiLogFileDeleteDirOK':dpiLogFileDeleteDirOK,'dpiLogFileDeleteFile':dpiLogFileDeleteFile,'dpiLogFileDeleteFileSlot':dpiLogFileDeleteFileSlot,'dpiLogFileDeleteFileName':dpiLogFileDeleteFileName,'dpiLogFileDeleteFileOK':dpiLogFileDeleteFileOK,'dpiUpdateDpiLog':dpiUpdateDpiLog,'dpiUpdateDpiLogSlot':dpiUpdateDpiLogSlot,'dpiLogServerFileName':dpiLogServerFileName,'dpiLogLocalFileName':dpiLogLocalFileName,'dpiUpdateDpiLogOK':dpiUpdateDpiLogOK,'dpiUploadTodayLog':dpiUploadTodayLog,'dpiCommit':dpiCommit,'dpiUpdateSignatureVersion':dpiUpdateSignatureVersion,'dpiVlanBindDpiTemplate':dpiVlanBindDpiTemplate,'dpiVlanInterfaceName':dpiVlanInterfaceName,'dpiBindDpiTemplate':dpiBindDpiTemplate,'dpiShowAllSignatureEntryTable':dpiShowAllSignatureEntryTable,'dpiShowAllSignatureEntry':dpiShowAllSignatureEntry,_Q:dpiAllSignatureEntryID,'dpiAllSignatureEntryContent':dpiAllSignatureEntryContent,'dpiShowAllSignatureSymbolTable':dpiShowAllSignatureSymbolTable,'dpiShowAllSignatureSymbolEntry':dpiShowAllSignatureSymbolEntry,_R:dpiAllSignatureSymbolID,'dpiAllSignatureSymbolEntryList':dpiAllSignatureSymbolEntryList,'dpiAllSignatureSymbolHitNumLimit':dpiAllSignatureSymbolHitNumLimit,'dpiAllSignatureSymbolProtocol':dpiAllSignatureSymbolProtocol,'dpiShowAllFlowPoolTable':dpiShowAllFlowPoolTable,'dpiShowAllFlowPoolEntry':dpiShowAllFlowPoolEntry,_S:dpiAllFlowPoolID,'dpiAllUpStreamRate':dpiAllUpStreamRate,'dpiAllUpStreamCbs':dpiAllUpStreamCbs,'dpiAllUpStreamEbs':dpiAllUpStreamEbs,'dpiAllDownStreamRate':dpiAllDownStreamRate,'dpiAllDownStreamCbs':dpiAllDownStreamCbs,'dpiAllDownStreamEbs':dpiAllDownStreamEbs,'dpiShowAllSubserviceTable':dpiShowAllSubserviceTable,'dpiShowAllSubserviceEntry':dpiShowAllSubserviceEntry,_T:dpiAllSubserviceID,'dpiAllSubserviceFlowpoolID':dpiAllSubserviceFlowpoolID,'dpiAllSubserviceAction':dpiAllSubserviceAction,'dpiAllSubserviceAgingTime':dpiAllSubserviceAgingTime,'dpiAllSubserviceSymbolList':dpiAllSubserviceSymbolList,'dpiAllSubserviceProtocol':dpiAllSubserviceProtocol,'dpiShowAllServiceTable':dpiShowAllServiceTable,'dpiShowAllServiceEntry':dpiShowAllServiceEntry,_U:dpiAllServiceID,'dpiAllServiceFlowPoolID':dpiAllServiceFlowPoolID,'dpiAllServiceSubserviceNum':dpiAllServiceSubserviceNum,'dpiAllServiceSubserviceList':dpiAllServiceSubserviceList,'dpiShowAllTemplateTable':dpiShowAllTemplateTable,'dpiShowAllTemplateEntry':dpiShowAllTemplateEntry,_V:dpiAllTemplateID,'dpiAllTemplateCfgCmd':dpiAllTemplateCfgCmd,'dpiShowAllMnpIpTable':dpiShowAllMnpIpTable,'dpiShowAllMngIpEntry':dpiShowAllMngIpEntry,_W:dpiAllSlotID,'dpiAllMngIp':dpiAllMngIp,'dpiAllServerIp':dpiAllServerIp,'dpiAllMngIpIsUsed':dpiAllMngIpIsUsed,'dpiAllLogSaveInterval':dpiAllLogSaveInterval,'dpiAllLogAutoUpload':dpiAllLogAutoUpload,'dpiAllLogUploadInterval':dpiAllLogUploadInterval,'dpiShowAllVlanDpiTable':dpiShowAllVlanDpiTable,'dpiShowAllVlanDpiEntry':dpiShowAllVlanDpiEntry,_Y:dpiAllVlanID,'dpiAllVlanBindTemplateID':dpiAllVlanBindTemplateID,'dpiAllVlanBindSlotID':dpiAllVlanBindSlotID,'dpiAllVlanBindServiceID':dpiAllVlanBindServiceID,'dpiAllVlanBindIsUsed':dpiAllVlanBindIsUsed})