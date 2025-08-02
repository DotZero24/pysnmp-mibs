_J='extremeSmartTrapInstanceSubindex'
_I='extremeSmartTrapRulesTrapDestIndex'
_H='modify'
_G='delete'
_F='extremeSmartTrapRulesIndex'
_E='Integer32'
_D='read-create'
_C='EXTREME-TRAPPOLL-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
extremeAgent,=mibBuilder.importSymbols('EXTREME-BASE-MIB','extremeAgent')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
extremeTrapPoll=ModuleIdentity((1,3,6,1,4,1,1916,1,6))
_ExtremeSmartTrapRulesTable_Object=MibTable
extremeSmartTrapRulesTable=_ExtremeSmartTrapRulesTable_Object((1,3,6,1,4,1,1916,1,6,1))
if mibBuilder.loadTexts:extremeSmartTrapRulesTable.setStatus(_A)
_ExtremeSmartTrapRulesEntry_Object=MibTableRow
extremeSmartTrapRulesEntry=_ExtremeSmartTrapRulesEntry_Object((1,3,6,1,4,1,1916,1,6,1,1))
extremeSmartTrapRulesEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:extremeSmartTrapRulesEntry.setStatus(_A)
_ExtremeSmartTrapRulesIndex_Type=Integer32
_ExtremeSmartTrapRulesIndex_Object=MibTableColumn
extremeSmartTrapRulesIndex=_ExtremeSmartTrapRulesIndex_Object((1,3,6,1,4,1,1916,1,6,1,1,1),_ExtremeSmartTrapRulesIndex_Type())
extremeSmartTrapRulesIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeSmartTrapRulesIndex.setStatus(_A)
_ExtremeSmartTrapRulesRowStatus_Type=RowStatus
_ExtremeSmartTrapRulesRowStatus_Object=MibTableColumn
extremeSmartTrapRulesRowStatus=_ExtremeSmartTrapRulesRowStatus_Object((1,3,6,1,4,1,1916,1,6,1,1,2),_ExtremeSmartTrapRulesRowStatus_Type())
extremeSmartTrapRulesRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeSmartTrapRulesRowStatus.setStatus(_A)
_ExtremeSmartTrapRulesDesiredOID_Type=ObjectIdentifier
_ExtremeSmartTrapRulesDesiredOID_Object=MibTableColumn
extremeSmartTrapRulesDesiredOID=_ExtremeSmartTrapRulesDesiredOID_Object((1,3,6,1,4,1,1916,1,6,1,1,3),_ExtremeSmartTrapRulesDesiredOID_Type())
extremeSmartTrapRulesDesiredOID.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeSmartTrapRulesDesiredOID.setStatus(_A)
_ExtremeSmartTrapRulesSupportedOID_Type=ObjectIdentifier
_ExtremeSmartTrapRulesSupportedOID_Object=MibTableColumn
extremeSmartTrapRulesSupportedOID=_ExtremeSmartTrapRulesSupportedOID_Object((1,3,6,1,4,1,1916,1,6,1,1,4),_ExtremeSmartTrapRulesSupportedOID_Type())
extremeSmartTrapRulesSupportedOID.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeSmartTrapRulesSupportedOID.setStatus(_A)
class _ExtremeSmartTrapRulesOperation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('add',1),(_G,2),(_H,3),('any',4)))
_ExtremeSmartTrapRulesOperation_Type.__name__=_E
_ExtremeSmartTrapRulesOperation_Object=MibTableColumn
extremeSmartTrapRulesOperation=_ExtremeSmartTrapRulesOperation_Object((1,3,6,1,4,1,1916,1,6,1,1,5),_ExtremeSmartTrapRulesOperation_Type())
extremeSmartTrapRulesOperation.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeSmartTrapRulesOperation.setStatus(_A)
_ExtremeSmartTrapRulesTrapDestIndex_Type=Integer32
_ExtremeSmartTrapRulesTrapDestIndex_Object=MibTableColumn
extremeSmartTrapRulesTrapDestIndex=_ExtremeSmartTrapRulesTrapDestIndex_Object((1,3,6,1,4,1,1916,1,6,1,1,6),_ExtremeSmartTrapRulesTrapDestIndex_Type())
extremeSmartTrapRulesTrapDestIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeSmartTrapRulesTrapDestIndex.setStatus(_A)
_ExtremeSmartTrapInstanceTable_Object=MibTable
extremeSmartTrapInstanceTable=_ExtremeSmartTrapInstanceTable_Object((1,3,6,1,4,1,1916,1,6,2))
if mibBuilder.loadTexts:extremeSmartTrapInstanceTable.setStatus(_A)
_ExtremeSmartTrapInstanceEntry_Object=MibTableRow
extremeSmartTrapInstanceEntry=_ExtremeSmartTrapInstanceEntry_Object((1,3,6,1,4,1,1916,1,6,2,1))
extremeSmartTrapInstanceEntry.setIndexNames((0,_C,_I),(0,_C,_J))
if mibBuilder.loadTexts:extremeSmartTrapInstanceEntry.setStatus(_A)
_ExtremeSmartTrapInstanceSubindex_Type=Integer32
_ExtremeSmartTrapInstanceSubindex_Object=MibTableColumn
extremeSmartTrapInstanceSubindex=_ExtremeSmartTrapInstanceSubindex_Object((1,3,6,1,4,1,1916,1,6,2,1,1),_ExtremeSmartTrapInstanceSubindex_Type())
extremeSmartTrapInstanceSubindex.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeSmartTrapInstanceSubindex.setStatus(_A)
_ExtremeSmartTrapInstanceRule_Type=Integer32
_ExtremeSmartTrapInstanceRule_Object=MibTableColumn
extremeSmartTrapInstanceRule=_ExtremeSmartTrapInstanceRule_Object((1,3,6,1,4,1,1916,1,6,2,1,2),_ExtremeSmartTrapInstanceRule_Type())
extremeSmartTrapInstanceRule.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeSmartTrapInstanceRule.setStatus(_A)
_ExtremeSmartTrapInstanceChangedOid_Type=ObjectIdentifier
_ExtremeSmartTrapInstanceChangedOid_Object=MibTableColumn
extremeSmartTrapInstanceChangedOid=_ExtremeSmartTrapInstanceChangedOid_Object((1,3,6,1,4,1,1916,1,6,2,1,3),_ExtremeSmartTrapInstanceChangedOid_Type())
extremeSmartTrapInstanceChangedOid.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeSmartTrapInstanceChangedOid.setStatus(_A)
class _ExtremeSmartTrapInstanceActualOperation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('add',1),(_G,2),(_H,3)))
_ExtremeSmartTrapInstanceActualOperation_Type.__name__=_E
_ExtremeSmartTrapInstanceActualOperation_Object=MibTableColumn
extremeSmartTrapInstanceActualOperation=_ExtremeSmartTrapInstanceActualOperation_Object((1,3,6,1,4,1,1916,1,6,2,1,4),_ExtremeSmartTrapInstanceActualOperation_Type())
extremeSmartTrapInstanceActualOperation.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeSmartTrapInstanceActualOperation.setStatus(_A)
_ExtremeSmartTrapInstanceChangeTime_Type=TimeTicks
_ExtremeSmartTrapInstanceChangeTime_Object=MibTableColumn
extremeSmartTrapInstanceChangeTime=_ExtremeSmartTrapInstanceChangeTime_Object((1,3,6,1,4,1,1916,1,6,2,1,5),_ExtremeSmartTrapInstanceChangeTime_Type())
extremeSmartTrapInstanceChangeTime.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeSmartTrapInstanceChangeTime.setStatus(_A)
_ExtremeSmartTrapFlushInstanceTableIndex_Type=Integer32
_ExtremeSmartTrapFlushInstanceTableIndex_Object=MibScalar
extremeSmartTrapFlushInstanceTableIndex=_ExtremeSmartTrapFlushInstanceTableIndex_Object((1,3,6,1,4,1,1916,1,6,3),_ExtremeSmartTrapFlushInstanceTableIndex_Type())
extremeSmartTrapFlushInstanceTableIndex.setMaxAccess('read-write')
if mibBuilder.loadTexts:extremeSmartTrapFlushInstanceTableIndex.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'extremeTrapPoll':extremeTrapPoll,'extremeSmartTrapRulesTable':extremeSmartTrapRulesTable,'extremeSmartTrapRulesEntry':extremeSmartTrapRulesEntry,_F:extremeSmartTrapRulesIndex,'extremeSmartTrapRulesRowStatus':extremeSmartTrapRulesRowStatus,'extremeSmartTrapRulesDesiredOID':extremeSmartTrapRulesDesiredOID,'extremeSmartTrapRulesSupportedOID':extremeSmartTrapRulesSupportedOID,'extremeSmartTrapRulesOperation':extremeSmartTrapRulesOperation,_I:extremeSmartTrapRulesTrapDestIndex,'extremeSmartTrapInstanceTable':extremeSmartTrapInstanceTable,'extremeSmartTrapInstanceEntry':extremeSmartTrapInstanceEntry,_J:extremeSmartTrapInstanceSubindex,'extremeSmartTrapInstanceRule':extremeSmartTrapInstanceRule,'extremeSmartTrapInstanceChangedOid':extremeSmartTrapInstanceChangedOid,'extremeSmartTrapInstanceActualOperation':extremeSmartTrapInstanceActualOperation,'extremeSmartTrapInstanceChangeTime':extremeSmartTrapInstanceChangeTime,'extremeSmartTrapFlushInstanceTableIndex':extremeSmartTrapFlushInstanceTableIndex})